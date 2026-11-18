"""Which hand moves more, per signer (exploratory check for REVISION_LOG §5.24, added 2026-10-23 after the results).

Motion of a hand in one execution = mean absolute frame-to-frame change of its
wrist (hand point 0), x plus y, in body-relative coordinates; averaged over a
signer's executions. Also the fraction of frames where the wrist is missing.
Hands are named as MediaPipe labels them (`_LH`, `_RH`).

Usage:
    python scripts/revision/hand_motion_check.py --input-csv WORK/bodynorm/general_db_bodynorm.csv --output-csv hand_motion.csv
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--output-csv", required=True)
    args = parser.parse_args()
    data = pd.read_csv(args.input_csv)
    rows = []
    for (label, subject, rep), e in data.groupby(["label", "subject", "rep"]):
        for part in ("LH", "RH"):
            x, y = e[f"landmark_0_x_{part}"].to_numpy(), e[f"landmark_0_y_{part}"].to_numpy()
            rows.append({"subject": subject, "hand": part,
                         "motion": np.nanmean(np.abs(np.diff(x))) + np.nanmean(np.abs(np.diff(y))),
                         "missing": float(np.mean(np.isnan(x) | (x == 0)))})
    out = pd.DataFrame(rows).groupby(["subject", "hand"])[["motion", "missing"]].mean().unstack()
    out.columns = [f"{a}_{b}" for a, b in out.columns]
    out["more_motion"] = np.where(out["motion_LH"] > out["motion_RH"], "LH", "RH")
    out.round(4).to_csv(args.output_csv)
    print(out.round(3).to_string())


if __name__ == "__main__":
    main()
