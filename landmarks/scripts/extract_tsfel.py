"""CLI: TSFEL features per landmark execution (``temporal_features.csv``).

The script that produced the original ``temporal_features.csv`` is not in the
repository; this rebuilds it from ``general_db.csv`` (one row per frame), one
feature row per ``(label, subject, rep)`` execution.

Usage:
    python landmarks/scripts/extract_tsfel.py \\
        --input-csv general_db.csv --output-csv temporal_features.csv
"""

from __future__ import annotations

import argparse

import pandas as pd
import tsfel
from tqdm import tqdm

GROUP_COLS = ["label", "subject", "rep"]


def main() -> None:
    parser = argparse.ArgumentParser(description="TSFEL features per landmark execution.")
    parser.add_argument("--input-csv", default="general_db.csv")
    parser.add_argument("--output-csv", default="temporal_features.csv")
    parser.add_argument("--domain", default="temporal", help="TSFEL feature domain.")
    parser.add_argument("--fs", type=float, default=24.0, help="Sampling rate in Hz (LSC50 videos are 24 FPS).")
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    config = tsfel.get_features_by_domain(args.domain)

    rows = []
    for key, group in tqdm(df.groupby(GROUP_COLS, sort=False), desc="TSFEL"):
        feats = tsfel.time_series_features_extractor(config, group.drop(columns=GROUP_COLS), fs=args.fs, verbose=0)
        for col, value in zip(GROUP_COLS, key):
            feats[col] = value
        rows.append(feats)

    out = pd.concat(rows, ignore_index=True)
    out.to_csv(args.output_csv, index=False, encoding="utf-8")
    print(f"Wrote {len(out)} executions x {out.shape[1] - len(GROUP_COLS)} features to {args.output_csv}")


if __name__ == "__main__":
    main()
