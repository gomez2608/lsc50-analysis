"""Signer-level permutation check for native vs. interpreter (R2.8).

With 5 signers, a held-out-signer score can be high for any grouping of
signers if the groups happen to be separable. This runs the same pipeline
(StandardScaler + fixed RandomForest, one signer held out at a time) for all
10 ways of labelling 3 of the 5 signers as "deaf", and reports pooled balanced
accuracy for each. The true grouping (subjects 2, 3, 4) should stand out; with
10 labellings the smallest attainable p-value is 0.1.

Usage:
    python scripts/revision/signant_labeling_permutation.py --features-csv WORK/temporal_features.csv
"""

from __future__ import annotations

import argparse
import itertools
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.splits import SIGNANT_SUBJECT_IDS


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--features-csv", required=True)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output-csv", default=None)
    parser.add_argument("--model", choices=["rf", "svm", "knn"], default="rf",
                        help="Fixed settings: RF 200 trees; SVM RBF C=1; KNN k=5 (no tuning).")
    args = parser.parse_args()

    data = pd.read_csv(args.features_csv)
    data = data.drop(columns=[c for c in data.columns if c.startswith("Unnamed")])
    subjects = data["subject"].to_numpy()
    X = data.drop(columns=[c for c in ("label", "subject", "rep") if c in data.columns]).to_numpy()

    rows = []
    for deaf in itertools.combinations(sorted(np.unique(subjects)), 3):
        y = np.isin(subjects, deaf).astype(int)
        y_pred = np.empty_like(y)
        for s in np.unique(subjects):
            train, test = subjects != s, subjects == s
            clf = {"rf": lambda: RandomForestClassifier(n_estimators=200, random_state=args.seed, n_jobs=-1),
                   "svm": lambda: SVC(C=1.0, kernel="rbf"),
                   "knn": lambda: KNeighborsClassifier(n_neighbors=5)}[args.model]()
            model = make_pipeline(StandardScaler(), clf)
            model.fit(X[train], y[train])
            y_pred[test] = model.predict(X[test])
        per_signer = {f"acc_v{s + 1}": float((y_pred[subjects == s] == y[subjects == s]).mean()) for s in np.unique(subjects)}
        rows.append({
            "deaf_volunteers": "+".join(str(d + 1) for d in deaf),
            "true_grouping": tuple(deaf) == tuple(sorted(SIGNANT_SUBJECT_IDS)),
            "balanced_accuracy": balanced_accuracy_score(y, y_pred),
            **per_signer,
        })
        print(rows[-1], flush=True)

    out = pd.DataFrame(rows).sort_values("balanced_accuracy", ascending=False)
    rank = int(np.where(out["true_grouping"].to_numpy())[0][0]) + 1
    print(out.to_string(index=False, float_format="%.2f"))
    print(f"True grouping ranks {rank} of {len(out)} (permutation p = {rank / len(out):.1f})")
    if args.output_csv:
        out.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
