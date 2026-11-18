"""Robustness check for the DTW normalization of dtw_signer_variability.py (R2.9).

The main analysis divides each DTW distance by sqrt(n + m), an upper bound of
the warping-path length. That equals the root-mean-square cost per matched frame
pair only up to a factor sqrt(L / (n + m)) in [~0.71, 1], where L is the actual
path length, so pairs with more warping (e.g. signers of different speed) could
look slightly more distant. Here every pair is recomputed with its optimal
warping path (same data, same dtaidistance multivariate DTW, no window) and
normalized by the actual path length: sqrt(sum over the path / L).

Checks on each pair: the path cost reproduces the library distance, and
d / sqrt(n + m) reproduces the main analysis' value (`--reference-pairs`).

Outputs <prefix>_pairs.csv (same columns as the main pair table, `dtw` = path-
normalized; plus n, m, path_length, dtw_raw, dtw_sqrt_nm) and prints, for both
normalizations: within vs. between per sign (ratio, count, Wilcoxon), the signer
matrix, and the per-sign deaf-cluster count. Feed the pair table to
dtw_per_sign.py for per-sign matrices.

Usage:
    python scripts/revision/dtw_path_normalization_check.py --input-csv WORK/bodynorm/general_db_f0_bodynorm.csv \\
        --reference-pairs docs/results/dtw/dtw_all_pairs.csv --output-prefix dtw_all_pathnorm --channels all
"""

from __future__ import annotations

import argparse
import itertools
import sys
from multiprocessing import Pool
from pathlib import Path

import numpy as np
import pandas as pd
from dtaidistance import dtw, dtw_ndim
from scipy.stats import wilcoxon

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.splits import SIGNANT_SUBJECT_IDS


def pair_cost(args: tuple[np.ndarray, np.ndarray]) -> tuple[float, float, int]:
    """(library distance, distance recomputed along the optimal path, path length)."""
    a, b = args
    d, paths = dtw_ndim.warping_paths_fast(a, b)
    path = dtw.best_path(paths)
    s = sum(float(np.sum((a[i] - b[j]) ** 2)) for i, j in path)
    return float(d), float(np.sqrt(s)), len(path)


def report(pairs: pd.DataFrame, col: str, title: str) -> None:
    per_sign = pairs.groupby(["label", "pair"])[col].mean().unstack()
    ratio = per_sign["between"] / per_sign["within"]
    stat = wilcoxon(per_sign["between"], per_sign["within"])
    print(f"\n== {title}")
    print(f"within {per_sign['within'].mean():.4f}, between {per_sign['between'].mean():.4f}; ratio per sign median {ratio.median():.2f} "
          f"(IQR {ratio.quantile(.25):.2f}-{ratio.quantile(.75):.2f}, min {ratio.min():.2f} sign {ratio.idxmin()}); "
          f"between > within in {int((ratio > 1).sum())}/{len(ratio)} signs; Wilcoxon p = {stat.pvalue:.2e}")
    sym = pd.concat([pairs, pairs.rename(columns={"subject_a": "subject_b", "subject_b": "subject_a"})])
    mat = sym.groupby(["label", "subject_a", "subject_b"])[col].mean().groupby(["subject_a", "subject_b"]).mean().unstack()
    mat.index = mat.columns = [f"V{s + 1}" for s in mat.index]
    print(mat.round(3).to_string())
    btw = pairs[pairs.pair == "between"].groupby(["label", "groups"])[col].mean().unstack()
    cluster = (btw["deaf-deaf"] < btw[["deaf-interpreter", "interpreter-interpreter"]].min(axis=1)).sum()
    print(f"group pairs (mean over signs): {btw.mean().round(3).to_dict()}; deaf-deaf lowest in {int(cluster)}/{len(btw)} signs")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--reference-pairs", required=True, help="Pair table of the main analysis (same channels).")
    parser.add_argument("--output-prefix", required=True)
    parser.add_argument("--channels", choices=["all", "hands"], default="all")
    parser.add_argument("--labels", type=int, nargs="*", help="Only these signs (for testing).")
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    data = pd.read_csv(args.input_csv)
    chans = [c for c in data.columns if c.startswith("landmark_")]
    if args.channels == "hands":
        chans = [c for c in chans if c.endswith(("_LH", "_RH"))]
    data[chans] = data[chans].fillna(0.0)
    if args.labels:
        data = data[data.label.isin(args.labels)]
    group_of = lambda s: "deaf" if s in SIGNANT_SUBJECT_IDS else "interpreter"  # noqa: E731

    rows, jobs = [], []
    for label, sign in data.groupby("label", sort=True):
        execs = [(k, np.ascontiguousarray(g[chans].to_numpy(dtype=np.double)))
                 for k, g in sign.groupby(["subject", "rep"], sort=True)]
        for i, j in itertools.combinations(range(len(execs)), 2):
            (si, ri), a = execs[i]
            (sj, rj), b = execs[j]
            rows.append({"label": label, "subject_a": si, "rep_a": ri, "subject_b": sj, "rep_b": rj,
                         "n": len(a), "m": len(b), "pair": "within" if si == sj else "between",
                         "groups": "-".join(sorted((group_of(si), group_of(sj))))})
            jobs.append((a, b))
    with Pool(args.workers) as pool:
        costs = pool.map(pair_cost, jobs, chunksize=50)
    pairs = pd.DataFrame(rows)
    pairs["dtw_raw"] = [c[0] for c in costs]
    pairs["path_length"] = [c[2] for c in costs]
    path_check = np.max(np.abs(np.array([c[1] for c in costs]) - pairs.dtw_raw) / pairs.dtw_raw)
    pairs["dtw_sqrt_nm"] = pairs.dtw_raw / np.sqrt(pairs.n + pairs.m)
    pairs["dtw"] = pairs.dtw_raw / np.sqrt(pairs.path_length)

    ref = pd.read_csv(args.reference_pairs)
    keys = ["label", "subject_a", "rep_a", "subject_b", "rep_b"]
    merged = pairs.merge(ref[keys + ["dtw"]].rename(columns={"dtw": "dtw_ref"}), on=keys, how="left")
    assert merged.dtw_ref.notna().all(), "pair missing from the reference table"
    ref_check = np.max(np.abs(merged.dtw_sqrt_nm - merged.dtw_ref) / merged.dtw_ref)
    print(f"{len(pairs)} pairs, {len(chans)} channels; max relative difference: path cost vs. library {path_check:.1e}, "
          f"sqrt(n+m) value vs. main analysis {ref_check:.1e}")
    factor = np.sqrt(pairs.path_length / (pairs.n + pairs.m))
    print("factor sqrt(L/(n+m)) by pair type:", factor.groupby(pairs.pair).describe()[["min", "50%", "mean", "max"]].round(3).to_dict("index"))

    pairs.to_csv(f"{args.output_prefix}_pairs.csv", index=False)
    report(pairs, "dtw_sqrt_nm", "normalized by sqrt(n + m) (main analysis)")
    report(pairs, "dtw", "normalized by the actual path length")


if __name__ == "__main__":
    main()
