"""Signer-level DTW analysis and the analysis without Volunteer 1 (R2.9, audit M5).

The per-sign Wilcoxon test of dtw_signer_variability.py treats the 50 signs as
independent units, while the question is about 5 signers; Volunteer 1 is an
outlier and takes part in 4 of the 10 signer pairs. From the existing pair table
(no new DTW):

1. Signer level: for each signer, the within-signer cost (mean over signs of the
   mean over that signer's repetition pairs) and the mean cost to the other
   signers; the paired difference across the 5 signers, how many signers have
   between > within, a paired t-test and the exact sign-flip test (smallest
   attainable two-sided p = 2/32 = 0.0625).
2. Without Volunteer 1: the per-sign analysis repeated on pairs not involving
   Volunteer 1 (median between/within ratio, count of signs, Wilcoxon over signs),
   and the signer-level analysis on the remaining 4 signers (smallest p = 2/16).

Within-signer pairs come from one recording session per signer, so within-signer
cost also reflects session; this cannot be separated with these data.

Usage:
    python scripts/revision/dtw_signer_level.py --pairs-csv docs/results/dtw/dtw_all_pairs.csv --output-prefix dtw_all
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import wilcoxon


def sign_flip_p(d: np.ndarray) -> float:
    signs = np.array(list(itertools.product([1, -1], repeat=len(d))))
    return float(np.mean(np.abs((signs * d).mean(axis=1)) >= abs(d.mean()) - 1e-12))


def per_sign(pairs: pd.DataFrame) -> dict:
    ps = pairs.groupby(["label", "pair"]).dtw.mean().unstack()
    ratio = ps["between"] / ps["within"]
    return {"n_signs": len(ps), "median_ratio": ratio.median(), "q1": ratio.quantile(.25), "q3": ratio.quantile(.75),
            "signs_between_gt_within": int((ratio > 1).sum()), "wilcoxon_p": wilcoxon(ps["between"], ps["within"]).pvalue}


def signer_level(pairs: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    sym = pd.concat([pairs, pairs[pairs.subject_a != pairs.subject_b].rename(
        columns={"subject_a": "subject_b", "subject_b": "subject_a"})])
    cell = sym.groupby(["label", "subject_a", "subject_b"]).dtw.mean().groupby(["subject_a", "subject_b"]).mean().unstack()
    signers = list(cell.index)
    rows = [{"signer": f"V{s + 1}", "within": cell.loc[s, s],
             "to_others": np.mean([cell.loc[s, t] for t in signers if t != s])} for s in signers]
    tab = pd.DataFrame(rows)
    tab["ratio"] = tab.to_others / tab.within
    d = (tab.to_others - tab.within).to_numpy()
    return tab, {"n_signers": len(d), "signers_between_gt_within": int((d > 0).sum()), "mean_diff": d.mean(),
                 "paired_t_p": stats.ttest_1samp(d, 0).pvalue, "sign_flip_p": sign_flip_p(d),
                 "median_signer_ratio": tab.ratio.median()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pairs-csv", required=True)
    parser.add_argument("--output-prefix", required=True)
    args = parser.parse_args()
    pairs = pd.read_csv(args.pairs_csv)
    no_v1 = pairs[(pairs.subject_a != 0) & (pairs.subject_b != 0)]

    out = []
    for name, p in (("all signers", pairs), ("without V1", no_v1)):
        tab, sl = signer_level(p)
        tab.insert(0, "analysis", name)
        tab.to_csv(f"{args.output_prefix}_signer_level_{name.replace(' ', '_')}.csv", index=False)
        out.append({"analysis": name, **{f"per_sign_{k}": v for k, v in per_sign(p).items()},
                    **{f"signer_{k}": v for k, v in sl.items()}})
        print(f"\n== {name}\n{tab.round(3).to_string(index=False)}")
    summary = pd.DataFrame(out)
    summary.to_csv(f"{args.output_prefix}_signer_level_summary.csv", index=False)
    print("\n" + summary.T.to_string(header=False))


if __name__ == "__main__":
    main()
