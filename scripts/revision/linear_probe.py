"""Linear probe on frozen features: logistic regression, the analogue of training
only the classification head (item 6 / R2.5).

Same splits as the other models: 80/20 stratified by sign (one split per seed)
and leave-one-signer-out (LOSO). The regularization strength C is chosen by
inner CV on the training rows only (grouped by signer for LOSO, stratified for
80/20), scored by weighted F1. Writes one row per run (split, seed, held-out
signer) with accuracy, weighted and macro F1.

Usage:
    python scripts/revision/linear_probe.py --features-csv vivit_frozen_cls.csv --output-csv probe_cls.csv --seeds 0 1 2 3 4
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV, GroupKFold, StratifiedKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

C_GRID = {"logisticregression__C": [0.001, 0.01, 0.1, 1, 10]}


def fit_score(X_tr, y_tr, X_te, y_te, cv, groups=None, seed=0) -> dict:
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000, random_state=seed))
    search = GridSearchCV(model, C_GRID, cv=cv, scoring="f1_weighted", n_jobs=-1)
    search.fit(X_tr, y_tr, groups=groups)
    y_pred = search.predict(X_te)
    return {
        "C": search.best_params_["logisticregression__C"],
        "accuracy": accuracy_score(y_te, y_pred),
        "f1_weighted": f1_score(y_te, y_pred, average="weighted"),
        "f1_macro": f1_score(y_te, y_pred, average="macro"),
        "n_test": len(y_te),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--features-csv", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--seeds", type=int, nargs="+", default=[0])
    parser.add_argument("--shuffle-labels", action="store_true",
                        help="Shuffled-label control: permute the training labels only (expect chance).")
    args = parser.parse_args()

    data = pd.read_csv(args.features_csv)
    y, subjects = data["label"].to_numpy(), data["subject"].to_numpy()
    X = data.drop(columns=[c for c in ("label", "subject", "rep") if c in data.columns]).to_numpy()

    def train_labels(idx, seed: int) -> np.ndarray:
        return np.random.default_rng(seed).permutation(y[idx]) if args.shuffle_labels else y[idx]

    rows = []
    for seed in args.seeds:
        tr, te = train_test_split(np.arange(len(y)), test_size=0.2, stratify=y, random_state=seed)
        cv = StratifiedKFold(4, shuffle=True, random_state=seed)
        rows.append({"split": "8020", "seed": seed, "subject": None, **fit_score(X[tr], train_labels(tr, seed), X[te], y[te], cv, seed=seed)})
        print(rows[-1], flush=True)
    for s in np.unique(subjects):
        tr, te = subjects != s, subjects == s
        cv = GroupKFold(len(np.unique(subjects[tr])))
        rows.append({"split": "loso", "seed": 0, "subject": int(s),
                     **fit_score(X[tr], train_labels(tr, 0), X[te], y[te], cv, groups=subjects[tr])})
        print(rows[-1], flush=True)

    out = pd.DataFrame(rows)
    out.to_csv(args.output_csv, index=False)
    for split, g in out.groupby("split"):
        print(f"{split}: F1 weighted {g.f1_weighted.mean():.2f} ± {g.f1_weighted.std(ddof=1):.2f} "
              f"(accuracy {g.accuracy.mean():.2f}, {len(g)} runs)")


if __name__ == "__main__":
    main()
