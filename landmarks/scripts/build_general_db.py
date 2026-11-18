"""CLI: build the long-format landmark table (``general_db.csv``).

Replaces the table-building cells of ``landmarks/notebooks/new_analysis.ipynb``.
That notebook did ``reindex(range(min_len)).interpolate()``, which truncates
every execution to the length of the shortest one (24 frames in LSC50) instead
of resampling it. Here each execution is linearly resampled over its full
duration to ``--n-frames`` frames (``0`` keeps the native length).

Input layout (from LSC50 ``LANDMARKS.zip``), files named ``{sign}_{subject}_{rep}.csv``:
    {landmarks_dir}/HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/
    {landmarks_dir}/HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS/
    {landmarks_dir}/BODY_LANDMARKS/

Kept channels match the original notebook: x/y of the 21 left-hand, 21
right-hand and the first 23 body landmarks (130 columns).

Usage:
    python landmarks/scripts/build_general_db.py \\
        --landmarks-dir path/to/LANDMARKS --output-csv general_db.csv --n-frames 24
"""

from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd
from tqdm import tqdm

N_BODY_LANDMARKS = 23


def _xy_columns(frame: pd.DataFrame, max_landmark: int | None = None) -> list[str]:
    cols = []
    for col in frame.columns:
        parts = col.split("_")  # landmark_{i}_{axis}
        if len(parts) != 3 or parts[2] not in ("x", "y"):
            continue
        if max_landmark is not None and int(parts[1]) >= max_landmark:
            continue
        cols.append(col)
    return cols


def resample(values: np.ndarray, n_frames: int) -> np.ndarray:
    """Linearly resample a ``(frames, channels)`` array to ``n_frames`` over its full duration."""
    if n_frames <= 0 or len(values) == n_frames:
        return values
    src = np.linspace(0.0, 1.0, len(values))
    dst = np.linspace(0.0, 1.0, n_frames)
    return np.stack([np.interp(dst, src, values[:, c]) for c in range(values.shape[1])], axis=1)


def load_execution(landmarks_dir: str, fname: str) -> pd.DataFrame:
    """Concatenate left-hand, right-hand and body x/y channels for one execution."""
    parts = []
    for sub, suffix, max_landmark in (
        ("HANDS_LANDMARKS/LEFT_HAND_LANDMARKS", "LH", None),
        ("HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS", "RH", None),
        ("BODY_LANDMARKS", "B", N_BODY_LANDMARKS),
    ):
        frame = pd.read_csv(os.path.join(landmarks_dir, sub, fname))
        frame = frame[_xy_columns(frame, max_landmark)]
        frame.columns = [f"{c}_{suffix}" for c in frame.columns]
        parts.append(frame)
    # Fill missed detections along time before resampling.
    return pd.concat(parts, axis=1).interpolate(limit_direction="both")


def build_general_db(landmarks_dir: str, n_frames: int) -> pd.DataFrame:
    """Build the table, skipping executions identical to an earlier one.

    The public LSC50 release ships a few byte-identical repetitions (e.g.
    ``0002_0001_0000`` and ``0002_0001_0001``); keeping both would put the same
    execution on both sides of a random split.
    """
    fnames = sorted(f for f in os.listdir(os.path.join(landmarks_dir, "BODY_LANDMARKS")) if f.endswith(".csv"))
    rows = []
    seen: dict[bytes, str] = {}
    for fname in tqdm(fnames, desc="Executions"):
        sign, subject, rep = (int(p) for p in fname[:-4].split("_"))
        execution = load_execution(landmarks_dir, fname)
        digest = execution.to_numpy().tobytes()
        if digest in seen:
            print(f"Skipping {fname}: identical to {seen[digest]}")
            continue
        seen[digest] = fname
        values = resample(execution.to_numpy(dtype=np.float64), n_frames)
        out = pd.DataFrame(values, columns=execution.columns)
        out["label"], out["subject"], out["rep"] = sign, subject, rep
        rows.append(out)
    return pd.concat(rows, ignore_index=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the long-format landmark table.")
    parser.add_argument("--landmarks-dir", required=True, help="LSC50 LANDMARKS/ directory.")
    parser.add_argument("--output-csv", default="general_db.csv")
    parser.add_argument("--n-frames", type=int, default=24, help="Frames per execution after resampling (0 = native length).")
    args = parser.parse_args()

    general_db = build_general_db(args.landmarks_dir, args.n_frames)
    general_db.to_csv(args.output_csv, index=False, encoding="utf-8")
    n_exec = general_db.groupby(["label", "subject", "rep"]).ngroups
    print(f"Wrote {n_exec} executions, {general_db.shape[1] - 3} channels, {len(general_db)} rows to {args.output_csv}")


if __name__ == "__main__":
    main()
