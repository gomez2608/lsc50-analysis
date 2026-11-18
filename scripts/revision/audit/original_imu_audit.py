"""Audit of the paper's IMU RF + TSFEL LOSO result (H1, REVISION_LOG §6.1).

Three steps, each printed:

1. ``simulate``: append an exact copy of one volunteer as an extra subject to a
   clean IMU feature table (upper bound of the duplicated-volunteer leak; the
   2026-10-15 simulation, `WORK/dup_test/temporal_dupv1.csv`).
2. ``identify``: for the original 6-subject table, match each of its subjects
   to the clean 5-subject table (identical rows) and report, for the unmatched
   extra subject, which volunteer it resembles per sign (feature-profile
   correlation).
3. ``reproduce``: run the original notebook's LOSO procedure
   (`~/LSC/IMU/grid_search_notebook.ipynb`: RF grid, no scaling, 5-fold
   stratified inner CV, seed 42, folds 0-4 only, sign 42 kept) and compare
   with the stored original pickle.

Usage:
    python scripts/revision/audit/original_imu_audit.py simulate --clean WORK/temporal.csv --copy-subject 0 --output dup.csv
    python scripts/revision/audit/original_imu_audit.py identify --clean original_server/IMU/temporal.csv \\
        --six original_server/IMU/IMU_FEATURES_NEW_6subjects/temporal.csv
    python scripts/revision/audit/original_imu_audit.py reproduce --table original_server/IMU/IMU_FEATURES_NEW_6subjects/temporal.csv \\
        --original-pkl original_server/IMU/grid_search_results_temporal.pkl
"""

from __future__ import annotations

import argparse
import collections
import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

RF_PARAMS = {"n_estimators": [10, 50, 100, 200], "criterion": ["gini", "entropy", "log_loss"],
             "max_depth": [None, 5, 10, 20], "min_samples_split": [2, 5, 10], "min_samples_leaf": [1, 2, 4]}


def feature_columns(d: pd.DataFrame) -> list[str]:
    return [c for c in d.columns if c not in ("label", "subject") and not c.startswith("Unnamed")]


def simulate(args) -> None:
    d = pd.read_csv(args.clean)
    extra = d[d.subject == args.copy_subject].copy()
    extra["subject"] = d.subject.max() + 1
    pd.concat([d, extra]).to_csv(args.output, index=False)
    print(f"Wrote {args.output}: subject {args.copy_subject} copied as subject {extra.subject.iloc[0]} ({len(extra)} rows)")


def identify(args) -> None:
    clean, six = pd.read_csv(args.clean), pd.read_csv(args.six)
    feats = feature_columns(six)
    matched = {}
    for s in sorted(clean.subject.unique()):
        a = clean[clean.subject == s].sort_values("label")[feats].to_numpy()
        for t in sorted(six.subject.unique()):
            b = six[six.subject == t].sort_values("label")[feats].to_numpy()
            if len(a) == len(b) and np.allclose(a, b, equal_nan=True):
                matched[t] = s
    print("6-subject table subject -> clean table subject (identical rows):", matched)
    extra = [t for t in sorted(six.subject.unique()) if t not in matched]
    print("unmatched (extra) subject(s):", extra)
    z = ((six[feats] - six[feats].mean()) / six[feats].std().replace(0, 1)).fillna(0).to_numpy()
    for e in extra:
        nearest, corr = collections.Counter(), collections.defaultdict(list)
        for lab in six.label.unique():
            ie = np.where((six.subject == e) & (six.label == lab))[0]
            if not len(ie):
                continue
            best = None
            for t in matched:
                j = np.where((six.subject == t) & (six.label == lab))[0]
                if not len(j):
                    continue
                c = np.corrcoef(z[ie[0]], z[j[0]])[0, 1]
                corr[t].append(c)
                best = (t, c) if best is None or c > best[1] else best
            nearest[best[0]] += 1
        print(f"extra subject {e}: most similar subject per sign {dict(nearest)}; "
              f"mean correlation {{{', '.join(f'{t}: {np.mean(v):.2f}' for t, v in sorted(corr.items()))}}}")


def reproduce(args) -> None:
    d = pd.read_csv(args.table, index_col=None)
    subjects, y = d.subject.to_numpy(), d.label.to_numpy()
    X = d.drop(columns=["subject", "label"]).to_numpy()  # as the notebook: "Unnamed: 0" stays (constant)
    orig = pickle.load(open(args.original_pkl, "rb"))["loso_part"] if args.original_pkl else {}
    scores = []
    for i in range(5):
        tr, te = subjects != i, subjects == i
        search = GridSearchCV(RandomForestClassifier(random_state=42), RF_PARAMS, n_jobs=-1, cv=5,
                              scoring="f1_weighted").fit(X[tr], y[tr])
        f = f1_score(y[te], search.predict(X[te]), average="weighted")
        scores.append(f)
        o = orig.get(f"rf-{i}")
        print(f"fold {i}: reproduced {f:.3f}" + (f" | original {float(o['f1_score']):.3f} | same params "
                                                 f"{search.best_params_ == o['best_params']}" if o else ""), flush=True)
    print(f"RF LOSO mean {np.mean(scores):.2f} ± {np.std(scores):.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("simulate"); p.add_argument("--clean", required=True); p.add_argument("--copy-subject", type=int, default=0); p.add_argument("--output", required=True)
    p = sub.add_parser("identify"); p.add_argument("--clean", required=True); p.add_argument("--six", required=True)
    p = sub.add_parser("reproduce"); p.add_argument("--table", required=True); p.add_argument("--original-pkl")
    args = parser.parse_args()
    {"simulate": simulate, "identify": identify, "reproduce": reproduce}[args.cmd](args)


if __name__ == "__main__":
    main()
