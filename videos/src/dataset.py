"""Build HuggingFace datasets of pre-processed video clips for ViViT.

Two split strategies are supported:

- ``custom_train_test_split`` (random per-class hold-out) — used by the
  general dataset builder.
- ``per_subject_split`` (filename-encoded subject id) — used by the
  cross-validation / per-subject builder.

For the revision, ``build_all_clips_dataset`` builds a single table of all
clips with ``labels``, ``subject`` and ``rep`` columns; the training scripts
then split it by seed or held-out signer without rebuilding (P13, P14 in
``docs/REVISION_LOG.md``).

Filenames are expected to encode ``label_subject_id_clip.avi`` (the
underscore-separated tokens used by the original dataset). The class label
is the first token; the subject id is the second token.
"""

from __future__ import annotations

import os
from typing import Iterable, Sequence

import av
import numpy as np
from datasets import Array4D, Dataset, Features, Value
from tqdm import tqdm
from transformers import VivitImageProcessor

DEFAULT_VIVIT_CHECKPOINT = "google/vivit-b-16x2-kinetics400"
DEFAULT_NUM_FRAMES = 32


def make_image_processor(checkpoint: str = DEFAULT_VIVIT_CHECKPOINT) -> VivitImageProcessor:
    """Return the ViViT image processor used everywhere downstream."""
    return VivitImageProcessor.from_pretrained(
        checkpoint,
        do_resize=True,
        size=224,
        do_center_crop=True,
        crop_size=224,
    )


def read_video_pyav(container: "av.container.input.InputContainer", indices: Sequence[int]) -> np.ndarray:
    """Decode the requested frame indices into an ``(N, H, W, 3)`` array."""
    frames = []
    container.seek(0)
    start_index = indices[0]
    end_index = indices[-1]
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    return np.stack([f.to_ndarray(format="rgb24") for f in frames])


def sample_frame_indices(frame_sample_rate: float, seg_len: int) -> np.ndarray:
    """Uniformly sample frame indices across ``seg_len`` frames."""
    return np.arange(0, seg_len, frame_sample_rate).astype(np.int64)


def parse_clip_name(fname: str) -> tuple[int, int, int]:
    """Return ``(label, subject, rep)`` from ``{label}_{subject}_{rep}.avi``."""
    label, subject, rep = os.path.splitext(os.path.basename(fname))[0].split("_")[:3]
    return int(label), int(subject), int(rep)


def list_clips(video_dir: str) -> list[str]:
    """``.avi`` files in ``video_dir``, sorted so the order is reproducible."""
    return sorted(f for f in os.listdir(video_dir) if f.lower().endswith(".avi"))


def _process_clip(path: str, image_processor: VivitImageProcessor, num_frames: int) -> dict:
    container = av.open(path)
    total = container.streams.video[0].frames
    indices = sample_frame_indices(frame_sample_rate=total / num_frames, seg_len=total)
    video = read_video_pyav(container, indices)
    container.close()
    pix = image_processor(list(video), return_tensors="pt")
    label, subject, rep = parse_clip_name(path)
    return {
        "pixel_values": pix["pixel_values"].squeeze(),
        "labels": label,
        "subject": subject,
        "rep": rep,
    }


def build_clip_dataset(
    video_dir: str,
    image_processor: VivitImageProcessor,
    *,
    limit: int | None = None,
    num_frames: int = DEFAULT_NUM_FRAMES,
) -> list[dict]:
    """Process every ``.avi`` file in ``video_dir`` into a list of dataset rows."""
    files = list_clips(video_dir)
    if limit is not None:
        files = files[:limit]

    rows: list[dict] = []
    for fname in tqdm(files, desc="Processing clips"):
        rows.append(_process_clip(os.path.join(video_dir, fname), image_processor, num_frames))
    return rows


def custom_train_test_split(
    dataset: list[dict], test_split: float = 0.2, seed: int = 42
) -> tuple[list[dict], list[dict]]:
    """Random per-class hold-out split.

    Fixes the long-standing bug in the original ``dataset_generation.py`` where
    the test loop appended ``dataset[i]`` (the train index) instead of
    ``dataset[j]`` (the test index).
    """
    train_ds: list[dict] = []
    test_ds: list[dict] = []
    labels = np.array([row["labels"] for row in dataset])
    rng = np.random.default_rng(seed)

    classes = np.unique(labels)
    imgs_per_class = len(labels) // len(classes)
    test_imgs_per_class = int(imgs_per_class * test_split)

    for class_idx in tqdm(classes, desc="Splitting"):
        img_indx = rng.permutation(np.where(labels == class_idx)[0])
        test_indx = img_indx[:test_imgs_per_class]
        train_indx = img_indx[test_imgs_per_class:]
        for i in train_indx:
            train_ds.append(dataset[i])
        for j in test_indx:
            test_ds.append(dataset[j])  # bug fix: was dataset[i]
    return train_ds, test_ds


def per_subject_split(
    video_dir: str,
    image_processor: VivitImageProcessor,
    holdout_subject: int,
    *,
    limit: int | None = None,
    num_frames: int = DEFAULT_NUM_FRAMES,
) -> tuple[list[dict], list[dict]]:
    """LOSO split: clips matching ``holdout_subject`` go to test, rest to train.

    The filename convention is ``{label}_{subject}_{clip}.avi``.
    """
    files = list_clips(video_dir)
    if limit is not None:
        files = files[:limit]

    train_videos: list[dict] = []
    test_videos: list[dict] = []
    for fname in tqdm(files, desc="Per-subject"):
        path = os.path.join(video_dir, fname)
        row = _process_clip(path, image_processor, num_frames)
        subject = int(fname.split("_")[1])
        (test_videos if subject == holdout_subject else train_videos).append(row)
    return train_videos, test_videos


def save_split(rows: Iterable[dict], output_path: str) -> str:
    """Persist a list of dataset rows to disk via ``Dataset.from_list``."""
    ds = Dataset.from_list(list(rows))
    ds.save_to_disk(output_path)
    return output_path


def build_all_clips_dataset(
    video_dir: str,
    image_processor: VivitImageProcessor,
    output_path: str,
    *,
    num_frames: int = DEFAULT_NUM_FRAMES,
    crop_size: int = 224,
    limit: int | None = None,
) -> str:
    """Process every clip once and stream it to ``output_path`` (Arrow on disk).

    Pixel values are stored as float16 (about 9.6 MB per 32-frame clip), so
    the full 1,000-clip set is roughly 10 GB and never has to sit in memory.
    """
    files = list_clips(video_dir)
    if limit is not None:
        files = files[:limit]

    def rows():
        for fname in tqdm(files, desc="Processing clips"):
            row = _process_clip(os.path.join(video_dir, fname), image_processor, num_frames)
            row["pixel_values"] = row["pixel_values"].numpy().astype(np.float16)
            yield row

    features = Features(
        {
            "pixel_values": Array4D(shape=(num_frames, 3, crop_size, crop_size), dtype="float16"),
            "labels": Value("int64"),
            "subject": Value("int64"),
            "rep": Value("int64"),
        }
    )
    # ~9.6 MB per clip: keep each Arrow write batch well under the 2 GB limit.
    ds = Dataset.from_generator(rows, features=features, writer_batch_size=50)
    ds.save_to_disk(output_path, max_shard_size="1GB")
    return output_path
