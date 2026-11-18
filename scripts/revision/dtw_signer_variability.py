"""Signer variability with dynamic time warping (R2.9).

For every sign, multivariate DTW distances between all pairs of its executions
(landmark sequences, body-relative coordinates, native length). Each distance
is divided by sqrt(n + m), so it is a per-step cost that does not grow with
sequence length. Pairs are labelled within-signer (repetitions by the same
person) or between-signer, and by signer group (interpreter / deaf).

Reports: within- vs. between-signer distance per sign with a Wilcoxon
signed-rank test over signs; a 5 x 5 signer-by-signer mean distance matrix
(diagonal = within-signer); and group-level within/between comparisons.

Usage:
    python scripts/revision/dtw_signer_variability.py --input-csv WORK/bodynorm/general_db_f0_bodynorm.csv \\
        --output-prefix dtw_all --channels all
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from dtaidistance import dtw_ndim
from scipy.stats import wilcoxon

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.splits import SIGNANT_SUBJECT_IDS

KEYS = ["label", "subject", "rep"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True, help="Per-frame landmark table (one row per frame).")
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument("--channels", choices=["all", "hands"], default="all")
    args = parser.parse_args()

    data = pd.read_csv(args.input_csv)
    chans = [c for c in data.columns if c.startswith("landmark_")]
    if args.channels == "hands":
        chans = [c for c in chans if c.endswith(("_LH", "_RH"))]
    data[chans] = data[chans].fillna(0.0)
    group_of = lambda s: "deaf" if s in SIGNANT_SUBJECT_IDS else "interpreter"  # noqa: E731

    rows = []
    for label, sign in data.groupby("label", sort=True):
        execs = [(k, g[chans].to_numpy(dtype=np.double)) for k, g in sign.groupby(["subject", "rep"], sort=True)]
        series = [np.ascontiguousarray(x) for _, x in execs]
        dist = dtw_ndim.distance_matrix_fast(series, parallel=True)
        for i, j in itertools.combinations(range(len(execs)), 2):
            (si, ri), (sj, rj) = execs[i][0], execs[j][0]
            d = dist[i, j] if np.isfinite(dist[i, j]) else dist[j, i]
            rows.append({
                "label": label, "subject_a": si, "rep_a": ri, "subject_b": sj, "rep_b": rj,
                "dtw": d / np.sqrt(len(series[i]) + len(series[j])),
                "pair": "within" if si == sj else "between",
                "groups": "-".join(sorted((group_of(si), group_of(sj)))),
            })
        print(f"sign {label}: {len(execs)} executions", flush=True)

    pairs = pd.DataFrame(rows)
    pairs.to_csv(f"{args.output_prefix}_pairs.csv", index=False)

    per_sign = pairs.groupby(["label", "pair"]).dtw.mean().unstack()
    stat = wilcoxon(per_sign["between"], per_sign["within"])
    ratio = per_sign["between"] / per_sign["within"]
    print(f"\nChannels: {args.channels} ({len(chans)}); {len(pairs)} pairs over {pairs.label.nunique()} signs")
    print(f"Mean per-step DTW cost: within-signer {per_sign['within'].mean():.4f}, between-signer {per_sign['between'].mean():.4f}")
    print(f"Between/within ratio per sign: median {ratio.median():.2f} (IQR {ratio.quantile(.25):.2f}-{ratio.quantile(.75):.2f}); "
          f"between > within in {int((ratio > 1).sum())}/{len(ratio)} signs; Wilcoxon p = {stat.pvalue:.2e}")

    sym = pd.concat([pairs, pairs.rename(columns={"subject_a": "subject_b", "subject_b": "subject_a"})])
    mat = sym.groupby(["label", "subject_a", "subject_b"]).dtw.mean().groupby(["subject_a", "subject_b"]).mean().unstack()
    mat.index = [f"V{s + 1}" for s in mat.index]
    mat.columns = [f"V{s + 1}" for s in mat.columns]
    mat.to_csv(f"{args.output_prefix}_signer_matrix.csv")
    print("\nSigner x signer mean per-step DTW cost (diagonal = within-signer; mean over signs):")
    print(mat.round(4).to_string())
    off = mat.where(~np.eye(len(mat), dtype=bool))
    print("Mean distance to the other signers:", off.mean(axis=1).round(4).to_dict())

    btw = pairs[pairs.pair == "between"].groupby(["label", "groups"]).dtw.mean().unstack()
    print("\nBetween-signer cost by group pair (mean over signs):", btw.mean().round(4).to_dict())


if __name__ == "__main__":
    main()
