"""CLI: hyperparameter grid search on landmark features.

Replaces ``LANDMARKS/grid_search_land.py``. The original ran four splits per
input CSV: balanced, LOSO, signant binary, and a "new schema" signant binary
that holds out test signs (not test rows). All shared logic now comes from
:mod:`common`; the new-schema split is the only landmark-specific addition.

Usage:
    python landmarks/scripts/grid_search.py \\
        --features-csv temporal_features.csv general_db_lm_chronos.csv
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.evaluation import save_confusion_matrix, save_results
from common.grid_search import PARAM_GRIDS, default_models, run_grid_search, summarize_search
from common.splits import (
    loso_train_test_split,
    train_test_split_balanced,
    train_test_split_interpreter_signant,
    train_test_split_interpreter_signant_by_signs,
)


def _scale(X_train, X_test):
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)


def _signant_block(
    X_train,
    X_test,
    y_train,
    y_test,
    db_name: str,
    output_dir: str,
    suffix: str,
    cv: int = 5,
) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for name, model in default_models():
        search = run_grid_search(
            model,
            PARAM_GRIDS[name],
            X_train,
            y_train,
            cv=cv,
            desc=f"GridSearchCV signant {name}",
        )
        y_pred = search.predict(X_test)
        if name == "rf":
            save_confusion_matrix(y_test, y_pred, f"{name}_{db_name}_{suffix}", output_dir)
        out.setdefault("signant_part", {})[f"{name}-deaf"] = summarize_search(search, y_test, y_pred)
    return out


def _process_dataset(csv_path: str, output_dir: str, n_subjects: int) -> None:
    print(f"Processing {csv_path}")
    handle = pd.read_csv(csv_path, index_col=None)
    if "rep" in handle.columns:
        handle = handle.drop(columns=["rep"])

    db_name = os.path.splitext(os.path.basename(csv_path))[0]
    agg: dict[str, dict] = {}

    # 1. Balanced stratified split.
    X_train, X_test, y_train, y_test = train_test_split_balanced(handle, test_size=0.2)
    X_train, X_test = _scale(X_train, X_test)

    for name, model in default_models():
        print(f"Training {name} (balanced)")
        search = run_grid_search(model, PARAM_GRIDS[name], X_train, y_train, cv=4, desc=f"GridSearchCV {name}")
        y_pred = search.predict(X_test)
        if name == "rf":
            save_confusion_matrix(y_test, y_pred, f"{name}_{db_name}_balanced", output_dir)
        agg.setdefault("balanced_part", {})[f"{name}-{db_name}"] = summarize_search(search, y_test, y_pred)

    # 2. LOSO.
    print("Going to LOSO")
    for i in range(n_subjects):
        print(f"Processing LOSO for subject {i + 1}")
        X_train_loso, y_train_loso, X_val_loso, y_val_loso = loso_train_test_split(handle, validation_subject=i)
        X_train_loso, X_val_loso = _scale(X_train_loso, X_val_loso)

        for name, model in default_models():
            search = run_grid_search(
                model,
                PARAM_GRIDS[name],
                X_train_loso,
                y_train_loso,
                cv=4,
                desc=f"GridSearchCV LOSO {name} subj {i + 1}",
            )
            y_pred = search.predict(X_val_loso)
            if name == "rf":
                save_confusion_matrix(y_val_loso, y_pred, f"{name}_{db_name}_loso_{i}", output_dir)
            agg.setdefault("loso_part", {})[f"{name}-{i}"] = summarize_search(search, y_val_loso, y_pred)

    # 3. Signant binary (rows split).
    print("Going to signant-nonsignant")
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split_interpreter_signant(handle, test_size=0.2)
    X_train_s, X_test_s = _scale(X_train_s, X_test_s)
    agg.update(_signant_block(X_train_s, X_test_s, y_train_s, y_test_s, db_name, output_dir, suffix="deaf"))

    save_results(agg, os.path.join(output_dir, f"grid_search_results_{db_name}_chronos.pkl"))

    # 4. Signant binary (signs split — landmark-specific "new schema").
    print("Going to signant-nonsignant new schema")
    X_train_n, X_test_n, y_train_n, y_test_n = train_test_split_interpreter_signant_by_signs(handle, n_test_signs=10)
    X_train_n, X_test_n = _scale(X_train_n, X_test_n)
    new_schema = _signant_block(X_train_n, X_test_n, y_train_n, y_test_n, db_name, output_dir, suffix="schema_new")

    save_results(new_schema, os.path.join(output_dir, f"grid_search_results_{db_name}_chronos_new_schema.pkl"))


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
    args = parser.parse_args()

    for path in args.features_csv:
        _process_dataset(path, args.output_dir, args.n_subjects)


if __name__ == "__main__":
    main()
