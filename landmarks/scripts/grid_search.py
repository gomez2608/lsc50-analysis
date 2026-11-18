"""CLI: hyperparameter grid search on landmark features.

Replaces ``LANDMARKS/grid_search_land.py``. The original ran four splits per
input CSV: balanced, LOSO, signant binary, and a "new schema" signant binary
that holds out test signs (not test rows). All shared logic now comes from
:mod:`common`; the new-schema split is the only landmark-specific addition.

Each part is repeated for every ``--seeds`` value and written to its own
pickle (``..._seed{n}.pkl``). ``--shuffle-labels`` runs the shuffled-label
control: training labels are permuted, so scores should fall to chance.
``signant_loso`` holds out one whole signer in the binary task.

Usage:
    python landmarks/scripts/grid_search.py \\
        --features-csv temporal_features.csv general_db_lm_chronos.csv \\
        --seeds 0 1 2 3 4
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
    train_test_split_interpreter_signant_by_signs,
)


PARTS = ("balanced", "loso", "signant", "signant_new_schema", "signant_loso")


def _scale(X_train, X_test):
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)


def _inner_cv(cv: int, train_subjects, inner_cv: str):
    """Inner CV for hyperparameter selection: stratified K-fold over rows, or one signer per fold."""
    if inner_cv == "group" and train_subjects is not None:
        return GroupKFold(n_splits=len(np.unique(train_subjects))), np.asarray(train_subjects)
    return cv, None


def _fit_models(
    X_train,
    X_test,
    y_train,
    y_test,
    *,
    seed: int,
    shuffle: bool,
    cv: int,
    cm_name: str,
    output_dir: str,
    desc: str,
    train_subjects=None,
    inner_cv: str = "stratified",
) -> dict[str, dict]:
    """Scale, grid-search every model, and summarize it on the test split."""
    X_train, X_test = _scale(X_train, X_test)
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
    csv_path: str, output_dir: str, n_subjects: int, seed: int, parts: tuple[str, ...], shuffle: bool, inner_cv: str = "stratified"
) -> None:
    print(f"Processing {csv_path} (seed {seed}{', shuffled labels' if shuffle else ''})")
    handle = pd.read_csv(csv_path, index_col=None)
    if "rep" in handle.columns:
        handle = handle.drop(columns=["rep"])

    db_name = os.path.splitext(os.path.basename(csv_path))[0]
    tag = f"{'_groupcv' if inner_cv == 'group' else ''}{'_shuffled' if shuffle else ''}_seed{seed}"
    fit = lambda *split, cv, cm, desc, train_subjects=None: _fit_models(  # noqa: E731
        *split, seed=seed, shuffle=shuffle, cv=cv, cm_name=f"{db_name}_{cm}{tag}", output_dir=output_dir, desc=desc,
        train_subjects=train_subjects, inner_cv=inner_cv,
    )
    subjects = handle["subject"].to_numpy()
    agg: dict[str, dict] = {}
    new_schema: dict[str, dict] = {}

    # 1. Balanced stratified split.
    if "balanced" in parts:
        split = train_test_split_balanced(handle, test_size=0.2, seed=seed)
        for name, res in fit(*split, cv=4, cm="balanced", desc="balanced").items():
            agg.setdefault("balanced_part", {})[f"{name}-{db_name}"] = res

    # 2. LOSO.
    if "loso" in parts:
        for i in range(n_subjects):
            X_train, y_train, X_val, y_val = loso_train_test_split(handle, validation_subject=i)
            loso = fit(X_train, X_val, y_train, y_val, cv=4, cm=f"loso_{i}", desc=f"LOSO subj {i}", train_subjects=subjects[subjects != i])
            for name, res in loso.items():
                agg.setdefault("loso_part", {})[f"{name}-{i}"] = res

    # 3. Signant binary (rows split).
    if "signant" in parts:
        split = train_test_split_interpreter_signant(handle, test_size=0.2, seed=seed)
        for name, res in fit(*split, cv=5, cm="deaf", desc="signant").items():
            agg.setdefault("signant_part", {})[f"{name}-deaf"] = res

    # 4. Signant binary, one whole signer held out per fold.
    if "signant_loso" in parts:
        for i in range(n_subjects):
            split = loso_interpreter_signant_split(handle, validation_subject=i)
            loso = fit(*split, cv=5, cm=f"deaf_loso_{i}", desc=f"signant LOSO subj {i}", train_subjects=subjects[subjects != i])
            for name, res in loso.items():
                agg.setdefault("signant_loso_part", {})[f"{name}-{i}"] = res

    save_results(agg, os.path.join(output_dir, f"grid_search_results_{db_name}_chronos{tag}.pkl"))

    # 5. Signant binary (signs split — landmark-specific "new schema").
    if "signant_new_schema" in parts:
        split = train_test_split_interpreter_signant_by_signs(handle, n_test_signs=10, seed=seed)
        for name, res in fit(*split, cv=5, cm="schema_new", desc="signant new schema").items():
            new_schema.setdefault("signant_part", {})[f"{name}-deaf"] = res
        save_results(new_schema, os.path.join(output_dir, f"grid_search_results_{db_name}_chronos_new_schema{tag}.pkl"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Grid search over landmark feature CSVs.")
    parser.add_argument(
        "--features-csv",
        nargs="+",
        default=["temporal_features.csv", "general_db_lm_chronos.csv"],
        help="One or more feature CSVs to run the grid search over.",
    )
    parser.add_argument("--output-dir", default=".", help="Directory for confusion matrices and results pickles.")
    parser.add_argument("--n-subjects", type=int, default=5)
    parser.add_argument("--seeds", type=int, nargs="+", default=[42], help="Repeat every split/model for each seed.")
    parser.add_argument("--parts", nargs="+", choices=PARTS, default=list(PARTS), help="Which splits to run.")
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
            _process_dataset(path, args.output_dir, args.n_subjects, seed, tuple(args.parts), args.shuffle_labels, args.inner_cv)


if __name__ == "__main__":
    main()
