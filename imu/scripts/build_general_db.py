"""CLI: build the long-format IMU table (``general_db_imu.csv``) for Chronos.

The script that produced the original ``general_db_imu.csv`` is not in the
repository. This stacks the per-sign motion CSVs written by
:mod:`imu.src.volunteers` into one table (one row per sample), using the same
label and subject numbering as :mod:`imu.src.feature_extraction`: ``label`` is
the index of the sign folder in sorted order and ``subject`` the index of the
volunteer file within it.

LSC50 has one IMU recording per (sign, volunteer), so each execution is
identified by ``(label, subject)``.

Usage:
    python imu/scripts/build_general_db.py --signs-dir SIGNS --output-csv general_db_imu.csv
"""

from __future__ import annotations

import argparse
import glob
import os

import pandas as pd


def build_general_db(signs_dir: str) -> pd.DataFrame:
    rows = []
    for sign_idx, sign_path in enumerate(sorted(glob.glob(os.path.join(signs_dir, "*")))):
        for subject_idx, csv_path in enumerate(sorted(glob.glob(os.path.join(sign_path, "*.csv")))):
            raw = pd.read_csv(csv_path)
            motion = raw.drop(columns=[c for c in ("time", "Unnamed: 0") if c in raw.columns])
            if motion.empty:
                continue
            motion["label"] = sign_idx
            motion["subject"] = subject_idx
            rows.append(motion)
    return pd.concat(rows, ignore_index=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Stack per-sign IMU motion CSVs into one long table.")
    parser.add_argument("--signs-dir", required=True, help="Output directory of imu/src/volunteers.py.")
    parser.add_argument("--output-csv", default="general_db_imu.csv")
    args = parser.parse_args()

    general_db = build_general_db(args.signs_dir)
    general_db.to_csv(args.output_csv, index=False, encoding="utf-8")
    n_exec = general_db.groupby(["label", "subject"]).ngroups
    print(f"Wrote {n_exec} executions, {general_db.shape[1] - 2} channels, {len(general_db)} rows to {args.output_csv}")


if __name__ == "__main__":
    main()
