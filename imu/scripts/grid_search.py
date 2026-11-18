"""CLI: hyperparameter grid search on IMU features.

Replaces ``IMU/grid_search.py``. The shared search/split/evaluation logic now
lives under :mod:`common`; this script wires it to IMU-specific defaults
(``general_db_imu_chronos.csv``) and orchestrates the LOSO loop.

Usage:
    python imu/scripts/grid_search.py --features-csv path/to/general_db_imu_chronos.csv

The original script also contained a commented-out balanced/signant block;
that flow is preserved here behind ``--include-balanced`` and
``--include-signant`` flags so it can be enabled when needed.
``--include-signant`` also runs the signer-held-out binary split.

Every split is repeated for each ``--seeds`` value (one pickle per seed), and
``--shuffle-labels`` runs the shuffled-label control (expect chance scores).
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.evaluation import save_confusion_matrix, save_results
from common.grid_search import PARAM_GRIDS, default_models, run_grid_search, shuffle_labels, summarize_search
from common.splits import (
    loso_interpreter_signant_split,
    loso_train_test_split,
    train_test_split_balanced,
    train_test_split_interpreter_signant,
)


def _inner_cv(cv: int, train_subjects, inner_cv: str):
    """Inner CV for hyperparameter selection: stratified K-fold over rows, or one signer per fold."""
    if inner_cv == "group" and train_subjects is not None:
        return GroupKFold(n_splits=len(np.unique(train_subjects))), np.asarray(train_subjects)
    return cv, None


def _fit_models(
    X_train, X_test, y_train, y_test, *, seed: int, shuffle: bool, cv: int, cm_name: str, output_dir: str, desc: str,
    train_subjects=None, inner_cv: str = "stratified",
) -> dict[str, dict]:
    """Scale, grid-search every model, and summarize it on the test split."""
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    if shuffle:
        y_train = shuffle_labels(y_train, seed)

    cv, groups = _inner_cv(cv, train_subjects, inner_cv)
    out: dict[str, dict] = {}
    for name, model in default_models(seed):
        search = run_grid_search(model, PARAM_GRIDS[name], X_train, y_train, cv=cv, groups=groups, desc=f"GridSearchCV {desc} {name}")
        y_pred = search.predict(X_test)
        if name == "rf":
            save_confusion_matrix(y_test, y_pred, f"{name}_{cm_name}", output_dir)
        out[name] = summarize_search(search, y_test, y_pred)
    return out


def _process_dataset(
    csv_path: str,
    output_dir: str,
    *,
    include_balanced: bool,
    include_signant: bool,
    n_subjects: int,
    seed: int,
    shuffle: bool,
    inner_cv: str = "stratified",
) -> str:
    print(f"Processing {csv_path} (seed {seed}{', shuffled labels' if shuffle else ''})")
    handle = pd.read_csv(csv_path, index_col=None)
    db_name = os.path.splitext(os.path.basename(csv_path))[0]
    tag = f"{'_groupcv' if inner_cv == 'group' else ''}{'_shuffled' if shuffle else ''}_seed{seed}"
    fit = lambda *split, cv, cm, desc, train_subjects=None: _fit_models(  # noqa: E731
        *split, seed=seed, shuffle=shuffle, cv=cv, cm_name=f"{db_name}_{cm}{tag}", output_dir=output_dir, desc=desc,
        train_subjects=train_subjects, inner_cv=inner_cv,
    )
    subjects = handle["subject"].to_numpy()

    agg: dict[str, dict] = {}

    if include_balanced:
        feature_names_path = os.path.join(output_dir, "names.txt")
        os.makedirs(output_dir, exist_ok=True)
        split = train_test_split_balanced(handle, test_size=0.2, seed=seed, feature_names_path=feature_names_path)
        for name, res in fit(*split, cv=3, cm="balanced", desc="balanced").items():
            agg.setdefault("balanced_part", {})[f"{name}-{db_name}"] = res

    print("Going to LOSO")
    for i in range(n_subjects):
        X_train, y_train, X_val, y_val = loso_train_test_split(handle, validation_subject=i)
        loso = fit(X_train, X_val, y_train, y_val, cv=3, cm=f"loso_{i}", desc=f"LOSO subj {i}", train_subjects=subjects[subjects != i])
        for name, res in loso.items():
            agg.setdefault("loso_part", {})[f"{name}-{i}"] = res

    if include_signant:
        print("Going to signant-nonsignant")
        split = train_test_split_interpreter_signant(handle, test_size=0.2, seed=seed)
        for name, res in fit(*split, cv=5, cm="deaf", desc="signant").items():
            agg.setdefault("signant_part", {})[f"{name}-deaf"] = res

        for i in range(n_subjects):
            split = loso_interpreter_signant_split(handle, validation_subject=i)
            loso = fit(*split, cv=5, cm=f"deaf_loso_{i}", desc=f"signant LOSO subj {i}", train_subjects=subjects[subjects != i])
            for name, res in loso.items():
                agg.setdefault("signant_loso_part", {})[f"{name}-{i}"] = res

    output_path = os.path.join(output_dir, f"grid_search_results_{db_name}{tag}.pkl")
    save_results(agg, output_path)
    print("Saved", output_path)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Grid search over IMU feature CSVs.")
    parser.add_argument(
        "--features-csv",
        nargs="+",
        default=["general_db_imu_chronos.csv"],
        help="One or more feature CSVs to run the grid search over.",
    )
    parser.add_argument("--output-dir", default=".", help="Directory for confusion matrices and results pickles.")
    parser.add_argument("--n-subjects", type=int, default=5, help="Number of LOSO folds (subjects).")
    parser.add_argument("--include-balanced", action="store_true", help="Also run the stratified balanced split (kept disabled by default to match the original script).")
    parser.add_argument("--include-signant", action="store_true", help="Also run the binary signant splits.")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42], help="Repeat every split/model for each seed.")
    parser.add_argument("--shuffle-labels", action="store_true", help="Shuffled-label control (expect chance-level scores).")
    parser.add_argument(
        "--inner-cv",
        choices=["stratified", "group"],
        default="stratified",
        help="Hyperparameter-selection CV for the LOSO parts: stratified K-fold over rows, or one training signer per fold (group).",
    )
    args = parser.parse_args()

    for seed in args.seeds:
        for path in args.features_csv:
            _process_dataset(
                path,
                args.output_dir,
                include_balanced=args.include_balanced,
                include_signant=args.include_signant,
                n_subjects=args.n_subjects,
                seed=seed,
                shuffle=args.shuffle_labels,
                inner_cv=args.inner_cv,
            )


if __name__ == "__main__":
    main()
