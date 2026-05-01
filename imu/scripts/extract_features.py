"""CLI: extract TSFEL features from per-sign motion CSVs.

Equivalent to the original ``IMU/feature_extraction.py``, but with explicit
input/output paths so the script can run from any working directory.

Usage:
    python imu/scripts/extract_features.py \\
        --signs-dir /path/to/IMU/SIGNS \\
        --output-dir /path/to/IMU/FEATURES_NEW
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Make the repository root importable when this script is invoked directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from imu.src.feature_extraction import DEFAULT_DOMAINS, extract_all


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract TSFEL features from per-sign motion CSVs.")
    parser.add_argument("--signs-dir", required=True, help="Directory with one subfolder per sign.")
    parser.add_argument("--output-dir", default="FEATURES_NEW", help="Directory to write feature CSVs to.")
    parser.add_argument("--domains", nargs="+", default=list(DEFAULT_DOMAINS), help="TSFEL domains to extract.")
    args = parser.parse_args()

    extract_all(args.signs_dir, args.output_dir, args.domains)


if __name__ == "__main__":
    main()
