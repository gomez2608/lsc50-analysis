"""Chronos time-series embeddings shared by the IMU and LANDMARKS pipelines.

Replaces the embedding loops in ``imu/notebooks/feature_extraction_chronos.ipynb``
and ``landmarks/notebooks/feature_extraction_chronos_lm.ipynb``. The original
loops had two problems:

- They passed a ``(frames, channels)`` array straight to ``pipeline.embed``.
  Chronos reads a 2D input as a *batch of series*, so each frame's channel
  vector was embedded as if it were a time series and the temporal axis was
  only averaged over afterwards.
- The landmark loop iterated over ``rep`` without filtering by it, so every
  repetition of a (label, subject) pair got the same embedding (computed on
  all repetitions concatenated). Those identical rows leaked across the
  80/20 split.

Here every execution (one group of ``group_cols``) is embedded on its own, and
each channel is passed to Chronos as a separate univariate series over time.

Usage:
    python -m common.chronos_features \\
        --input-csv general_db.csv --output-csv general_db_lm_chronos.csv \\
        --group-cols label subject rep
"""

from __future__ import annotations

import argparse
from typing import Sequence

import numpy as np
import pandas as pd
import torch
from tqdm import tqdm

DEFAULT_CHRONOS_MODEL = "amazon/chronos-t5-small"


def load_pipeline(model_id: str = DEFAULT_CHRONOS_MODEL, device: str | None = None):
    """Load a ``ChronosPipeline`` on CUDA, Apple MPS, or CPU (in that order)."""
    from chronos import ChronosPipeline

    if device is None:
        if torch.cuda.is_available():
            device = "cuda"
        elif torch.backends.mps.is_available():
            device = "mps"
        else:
            device = "cpu"
    dtype = torch.bfloat16 if device == "cuda" else torch.float32
    return ChronosPipeline.from_pretrained(model_id, device_map=device, torch_dtype=dtype)


def embed_execution(pipeline, sequence: np.ndarray, channel_pooling: str = "mean") -> np.ndarray:
    """Embed one execution of shape ``(frames, channels)`` into a fixed-length vector.

    Each channel is embedded as its own series; token embeddings are averaged
    over time (dropping Chronos' trailing EOS token), giving ``(channels, d_model)``.
    ``channel_pooling="mean"`` then averages over channels (``d_model`` dims);
    ``"concat"`` keeps them side by side (``channels * d_model`` dims).
    """
    n_frames = sequence.shape[0]
    series = [torch.tensor(sequence[:, c], dtype=torch.float32) for c in range(sequence.shape[1])]
    with torch.no_grad():
        embeddings, _ = pipeline.embed(series)
    embeddings = embeddings.to(torch.float32).cpu().numpy()  # (channels, tokens, d_model)
    if embeddings.shape[1] == n_frames + 1:
        embeddings = embeddings[:, :n_frames]
    per_channel = embeddings.mean(axis=1)

    if channel_pooling == "mean":
        return per_channel.mean(axis=0)
    if channel_pooling == "concat":
        return per_channel.reshape(-1)
    raise ValueError(f"Unknown channel_pooling: {channel_pooling!r}")


def embed_dataframe(
    pipeline,
    df: pd.DataFrame,
    group_cols: Sequence[str],
    channel_pooling: str = "mean",
) -> pd.DataFrame:
    """Embed every execution in a long-format frame (one row per frame).

    Rows are grouped by ``group_cols`` (e.g. ``label, subject, rep``); within a
    group, row order is taken as time order. Returns one row per execution with
    the ``group_cols`` followed by ``features_{i}`` columns.
    """
    group_cols = list(group_cols)
    feature_cols = [c for c in df.columns if c not in group_cols and c != "Unnamed: 0"]

    keys: list[tuple] = []
    vectors: list[np.ndarray] = []
    for key, group in tqdm(df.groupby(group_cols, sort=False), desc="Chronos"):
        keys.append(key if isinstance(key, tuple) else (key,))
        vectors.append(embed_execution(pipeline, group[feature_cols].to_numpy(dtype=np.float32), channel_pooling))

    out = pd.DataFrame(keys, columns=group_cols)
    features = pd.DataFrame(np.stack(vectors), columns=[f"features_{i}" for i in range(len(vectors[0]))])
    return pd.concat([out, features], axis=1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Per-execution Chronos embeddings.")
    parser.add_argument("--input-csv", required=True, help="Long-format CSV, one row per frame.")
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--group-cols", nargs="+", default=["label", "subject", "rep"], help="Columns that identify one execution.")
    parser.add_argument("--model", default=DEFAULT_CHRONOS_MODEL)
    parser.add_argument("--device", default=None, help="cuda, mps or cpu (default: auto).")
    parser.add_argument("--channel-pooling", choices=["mean", "concat"], default="mean")
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    pipeline = load_pipeline(args.model, args.device)
    out = embed_dataframe(pipeline, df, args.group_cols, args.channel_pooling)

    n_dupes = out.drop(columns=args.group_cols).duplicated().sum()
    if n_dupes:
        print(f"WARNING: {n_dupes} executions have identical embeddings")
    out.to_csv(args.output_csv, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} executions x {out.shape[1] - len(args.group_cols)} features to {args.output_csv}")


if __name__ == "__main__":
    main()
