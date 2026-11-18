"""Body-relative landmark coordinates (P16: camera framing differs per signer).

For each execution, coordinates are converted to pixels (MediaPipe x, y are
fractions of the frame width and height), centred on the mean shoulder
midpoint (pose landmarks 11 and 12) and divided by the mean shoulder width.
This removes the signer's distance from the camera and position in the frame
but keeps the movement within the execution.

Usage:
    python scripts/revision/normalize_landmarks.py --input-csv WORK/general_db.csv \\
        --output-csv WORK/general_db_bodynorm.csv
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

KEYS = ["label", "subject", "rep"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--width", type=float, default=1920.0)
    parser.add_argument("--height", type=float, default=1080.0)
    args = parser.parse_args()

    data = pd.read_csv(args.input_csv)
    xs = [c for c in data.columns if "_x_" in c]
    ys = [c for c in data.columns if "_y_" in c]
    out = data.copy()
    out[xs] = out[xs] * args.width
    out[ys] = out[ys] * args.height

    groups = out.groupby(KEYS, sort=False)
    lx, ly = groups["landmark_11_x_B"].transform("mean"), groups["landmark_11_y_B"].transform("mean")
    rx, ry = groups["landmark_12_x_B"].transform("mean"), groups["landmark_12_y_B"].transform("mean")
    cx, cy = (lx + rx) / 2, (ly + ry) / 2
    width = np.hypot(lx - rx, ly - ry)
    out[xs] = out[xs].sub(cx, axis=0).div(width, axis=0)
    out[ys] = out[ys].sub(cy, axis=0).div(width, axis=0)

    per_subject = pd.DataFrame({"subject": out["subject"], "shoulder_px": width}).groupby("subject")["shoulder_px"].median()
    print("median shoulder width (px) per subject:", per_subject.round(1).to_dict())
    out.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
