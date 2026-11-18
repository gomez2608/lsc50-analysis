"""Summary of the native (deaf) vs. interpreter results from the grid-search pickles (R2.8, audit K3).

For each pickle (one per feature set and seed) and model:
- rows 80/20 (`signant_part` of the main pickle): weighted F1;
- 10 signs held out (`signant_part` of the `_new_schema` pickle, landmarks only): weighted F1;
- one signer held out (`signant_loso_part`): every test fold holds one class only, so
  predictions are pooled over the 5 folds and scored with balanced accuracy (chance 0.50),
  plus the accuracy on each held-out volunteer.
Then mean and SD (ddof = 1) over seeds per feature set and model.

Usage:
    python scripts/revision/signant_summary.py --pkl "Landmarks TSFEL body-relative=WORK/results/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed?.pkl" \\
        --output-prefix signant_summary
"""

from __future__ import annotations

import argparse
import glob
import os
import pickle
import re

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, balanced_accuracy_score

MODELS = {"svc": "SVM", "rf": "RF", "knn": "KNN"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pkl", action="append", required=True, help="NAME=PATTERN of the main signant pickles (one per seed).")
    parser.add_argument("--output-prefix", required=True)
    args = parser.parse_args()

    rows = []
    for spec in args.pkl:
        name, pattern = spec.split("=", 1)
        for path in sorted(glob.glob(pattern)):
            seed = int(re.search(r"seed(\d+)\.pkl$", path).group(1))
            res = pickle.load(open(path, "rb"))
            ns_path = path.replace(f"_seed{seed}.pkl", f"_new_schema_seed{seed}.pkl")
            ns = pickle.load(open(ns_path, "rb"))["signant_part"] if os.path.exists(ns_path) else {}
            for m, label in MODELS.items():
                row = {"features": name, "model": label, "seed": seed,
                       "rows_8020_f1": res.get("signant_part", {}).get(f"{m}-deaf", {}).get("f1_score"),
                       "signs_heldout_f1": ns.get(f"{m}-deaf", {}).get("f1_score")}
                folds = {int(k.split("-")[1]): v for k, v in res.get("signant_loso_part", {}).items() if k.startswith(m + "-")}
                if folds:
                    yt = np.concatenate([np.asarray(folds[i]["y_true"]) for i in sorted(folds)])
                    yp = np.concatenate([np.asarray(folds[i]["y_pred"]) for i in sorted(folds)])
                    row["signer_heldout_bal_acc"] = balanced_accuracy_score(yt, yp)
                    for i in sorted(folds):
                        row[f"acc_V{i + 1}"] = accuracy_score(folds[i]["y_true"], folds[i]["y_pred"])
                rows.append(row)
    runs = pd.DataFrame(rows)
    runs.to_csv(f"{args.output_prefix}_runs.csv", index=False)
    metrics = [c for c in runs.columns if c not in ("features", "model", "seed")]
    agg = runs.groupby(["features", "model"], sort=False)[metrics].agg(["mean", lambda x: x.std(ddof=1)])
    agg.columns = [f"{c}_{'mean' if s == 'mean' else 'sd'}" for c, s in agg.columns]
    agg.insert(0, "n_seeds", runs.groupby(["features", "model"], sort=False).seed.nunique())
    agg.reset_index().to_csv(f"{args.output_prefix}.csv", index=False)
    show = ["n_seeds", "rows_8020_f1_mean", "signs_heldout_f1_mean", "signer_heldout_bal_acc_mean", "signer_heldout_bal_acc_sd"] + \
        [f"acc_V{i}_mean" for i in range(1, 6)]
    print(agg[[c for c in show if c in agg.columns]].round(3).to_string())


if __name__ == "__main__":
    main()
