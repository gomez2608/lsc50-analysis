"""TSFEL feature extraction over the per-sign motion CSVs produced by
:mod:`imu.src.volunteers`.

For each ``signs_dir/{sign_name}/nw_Volunteer_{n}.csv``, the module:

1. Reads the motion CSV, optionally cropping to upper-limb columns.
2. Computes the sampling frequency from the ``time`` column.
3. Runs ``tsfel.time_series_features_extractor`` for the requested domain.
4. Tags the resulting row with the sign label and subject id.

Outputs one CSV per (domain, cropped) combination under ``output_dir``.
"""

from __future__ import annotations

import glob
import os
from typing import Iterable

import pandas as pd
import tsfel

DEFAULT_DOMAINS: tuple[str, ...] = ("statistical", "temporal", "spectral", "all")
CROPPED_COLUMNS: tuple[str, ...] = (
    "arm_rot_l",
    "arm_rot_r",
    "pro_sup_r",
    "pro_sup_l",
    "elbow_flex_l",
    "elbow_flex_r",
)


def extract_features_for_domain(
    signs_dir: str,
    output_dir: str,
    domain: str,
    name: str,
    crop: bool = False,
) -> str:
    """Extract features for one ``(domain, crop)`` combination.

    Returns the path of the written CSV.
    """
    config = tsfel.get_features_by_domain(domain)
    rows: list[pd.DataFrame] = []

    for sign_idx, sign_path in enumerate(sorted(glob.glob(os.path.join(signs_dir, "*")))):
        for subject_idx, csv_path in enumerate(sorted(glob.glob(os.path.join(sign_path, "*.csv")))):
            raw = pd.read_csv(csv_path)
            if crop:
                features_input = raw[list(CROPPED_COLUMNS)]
            else:
                features_input = raw.drop(columns=[c for c in ("time", "Unnamed: 0") if c in raw.columns])

            if features_input.empty:
                continue

            duration = raw["time"].max() - raw["time"].min()
            if duration <= 0:
                continue

            freq = int(len(features_input) / duration)
            feats = tsfel.time_series_features_extractor(config, features_input, fs=freq, verbose=0)
            feats["label"] = sign_idx
            feats["subject"] = subject_idx
            rows.append(feats)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{name}.csv")
    pd.concat(rows).to_csv(output_path)
    return output_path


def extract_all(
    signs_dir: str,
    output_dir: str,
    domains: Iterable[str] = DEFAULT_DOMAINS,
) -> list[str]:
    """Run ``extract_features_for_domain`` for every domain, both cropped and full."""
    written: list[str] = []
    for domain in domains:
        print(f"Extracting features for {domain} (cropped)")
        written.append(extract_features_for_domain(signs_dir, output_dir, domain, f"{domain}_cropped", crop=True))
        print(f"Extracting features for {domain}")
        written.append(extract_features_for_domain(signs_dir, output_dir, domain, domain, crop=False))
    return written


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract TSFEL features from per-sign motion CSVs.")
    parser.add_argument("--signs-dir", required=True, help="Directory with one subfolder per sign (output of volunteers.py).")
    parser.add_argument("--output-dir", default="FEATURES_NEW", help="Directory to write feature CSVs to.")
    parser.add_argument("--domains", nargs="+", default=list(DEFAULT_DOMAINS), help="TSFEL domains to extract.")
    args = parser.parse_args()

    extract_all(args.signs_dir, args.output_dir, args.domains)
