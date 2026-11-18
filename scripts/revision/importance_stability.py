"""Fold stability of the grouped permutation importance, with and without near-chance folds (R2.6, audit M12).

Reads the table written by permutation_importance.py and reports, per grouping, the
baseline F1 of each held-out-signer fold and the mean (range) Spearman rho of the
group importances between fold pairs: over all folds, and over the folds whose
baseline weighted F1 is at least --min-baseline (near-chance folds have
importances near zero by construction, which pulls rho down).

Usage:
    python scripts/revision/importance_stability.py docs/results/importance_landmarks_bodynorm.csv --min-baseline 0.2
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np
import pandas as pd
from scipy.stats import spearmanr


def rho(piv: pd.DataFrame) -> tuple[float, float, float, int]:
    r = [spearmanr(piv[a], piv[b]).statistic for a, b in itertools.combinations(piv.columns, 2)]
    return float(np.mean(r)), float(np.min(r)), float(np.max(r)), len(r)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv")
    parser.add_argument("--min-baseline", type=float, default=0.2)
    parser.add_argument("--output-csv", default=None)
    args = parser.parse_args()
    t = pd.read_csv(args.csv)
    base = t.groupby("subject").baseline_f1.first()
    keep = base[base >= args.min_baseline].index
    print("baseline F1 per held-out signer:", {f"V{s + 1}": round(v, 3) for s, v in base.items()},
          f"-> folds kept at >= {args.min_baseline}: {[f'V{s + 1}' for s in keep]}")
    rows = []
    for grouping, g in t.groupby("grouping"):
        piv = g.pivot(index="group", columns="subject", values="importance")
        for name, cols in (("all folds", piv.columns), (f"baseline >= {args.min_baseline}", keep)):
            m, lo, hi, n = rho(piv[list(cols)])
            rows.append({"grouping": grouping, "folds": name, "n_folds": len(cols), "n_pairs": n,
                         "rho_mean": m, "rho_min": lo, "rho_max": hi})
    out = pd.DataFrame(rows)
    print(out.round(2).to_string(index=False))
    if args.output_csv:
        out.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
