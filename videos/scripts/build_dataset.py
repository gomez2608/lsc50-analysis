"""CLI: build the general (random per-class) train/test split.

Replaces ``VIDEOS/dataset_generation.py``. Note that the original had a bug:
the test loop appended ``dataset[i]`` instead of ``dataset[j]``. The shared
helper :func:`videos.src.dataset.custom_train_test_split` fixes this.

Usage:
    python videos/scripts/build_dataset.py \\
        --video-dir path/to/VIDEOS/COLOR_BODY \\
        --train-out train_dataset_v2 \\
        --test-out test_dataset_v2
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.dataset import (
    DEFAULT_NUM_FRAMES,
    DEFAULT_VIVIT_CHECKPOINT,
    build_clip_dataset,
    custom_train_test_split,
    make_image_processor,
    save_split,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build random-split ViViT training dataset.")
    parser.add_argument("--video-dir", required=True, help="Directory with .avi clips.")
    parser.add_argument("--train-out", default="train_dataset_v2", help="Path to save the train split.")
    parser.add_argument("--test-out", default="test_dataset_v2", help="Path to save the test split.")
    parser.add_argument("--test-split", type=float, default=0.2, help="Fraction of clips per class held out for test.")
    parser.add_argument("--num-frames", type=int, default=DEFAULT_NUM_FRAMES, help="Number of frames sampled per clip.")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT, help="ViViT checkpoint for the image processor.")
    parser.add_argument("--limit", type=int, default=None, help="Optional cap on the number of clips processed.")
    args = parser.parse_args()

    print("Loading videos")
    processor = make_image_processor(args.checkpoint)
    rows = build_clip_dataset(args.video_dir, processor, limit=args.limit, num_frames=args.num_frames)

    print("Splitting")
    train_rows, test_rows = custom_train_test_split(rows, test_split=args.test_split)

    print("Saving splits")
    save_split(train_rows, args.train_out)
    save_split(test_rows, args.test_out)
    print("Done")


if __name__ == "__main__":
    main()
