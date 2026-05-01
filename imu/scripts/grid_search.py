"""CLI: hyperparameter grid search on IMU features.

Replaces ``IMU/grid_search.py``. The shared search/split/evaluation logic now
lives under :mod:`common`; this script wires it to IMU-specific defaults
(``general_db_imu_chronos.csv``) and orchestrates the LOSO loop.

Usage:
    python imu/scripts/grid_search.py --features-csv path/to/general_db_imu_chronos.csv

The original script also contained a commented-out balanced/signant block;
that flow is preserved here behind ``--include-balanced`` and
``--include-signant`` flags so it can be enabled when needed.
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
)


def _process_dataset(
    csv_path: str,
    output_dir: str,
    *,
    include_balanced: bool,
    include_signant: bool,
    n_subjects: int,
) -> str:
    print(f"Processing {csv_path}")
    handle = pd.read_csv(csv_path, index_col=None)
    db_name = os.path.splitext(os.path.basename(csv_path))[0]

    agg: dict[str, dict] = {}

    if include_balanced:
        feature_names_path = os.path.join(output_dir, "names.txt")
        os.makedirs(output_dir, exist_ok=True)
        X_train, X_test, y_train, y_test = train_test_split_balanced(
            handle, test_size=0.2, feature_names_path=feature_names_path
        )
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        for name, model in default_models():
            print(f"Training {name} (balanced)")
            search = run_grid_search(model, PARAM_GRIDS[name], X_train, y_train, desc=f"GridSearchCV {name}")
            y_pred = search.predict(X_test)
            if name == "rf":
                save_confusion_matrix(y_test, y_pred, f"{name}_{db_name}_balanced", output_dir)
            agg.setdefault("balanced_part", {})[f"{name}-{db_name}"] = summarize_search(search, y_test, y_pred)

    print("Going to LOSO")
    for i in range(n_subjects):
        print(f"Processing LOSO for subject {i + 1}")
        X_train_loso, y_train_loso, X_val_loso, y_val_loso = loso_train_test_split(handle, validation_subject=i)

        scaler = StandardScaler()
        X_train_loso = scaler.fit_transform(X_train_loso)
        X_val_loso = scaler.transform(X_val_loso)

        for name, model in default_models():
            search = run_grid_search(
                model,
                PARAM_GRIDS[name],
                X_train_loso,
                y_train_loso,
                desc=f"GridSearchCV LOSO {name} subj {i + 1}",
            )
            y_pred = search.predict(X_val_loso)
            if name == "rf":
                save_confusion_matrix(y_val_loso, y_pred, f"{name}_{db_name}_loso_{i}", output_dir)
            agg.setdefault("loso_part", {})[f"{name}-{i}"] = summarize_search(search, y_val_loso, y_pred)

    if include_signant:
        print("Going to signant-nonsignant")
        X_train_s, X_test_s, y_train_s, y_test_s = train_test_split_interpreter_signant(handle, test_size=0.2)
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train_s)
        X_test_s = scaler.transform(X_test_s)

        for name, model in default_models():
            search = run_grid_search(
                model,
                PARAM_GRIDS[name],
                X_train_s,
                y_train_s,
                cv=5,
                desc=f"GridSearchCV signant {name}",
            )
            y_pred = search.predict(X_test_s)
            if name == "rf":
                save_confusion_matrix(y_test_s, y_pred, f"{name}_{db_name}_deaf", output_dir)
            agg.setdefault("signant_part", {})[f"{name}-deaf"] = summarize_search(search, y_test_s, y_pred)

    output_path = os.path.join(output_dir, f"grid_search_results_{db_name}.pkl")
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
    parser.add_argument("--include-signant", action="store_true", help="Also run the binary signant split.")
    args = parser.parse_args()

    for path in args.features_csv:
        _process_dataset(
            path,
            args.output_dir,
            include_balanced=args.include_balanced,
            include_signant=args.include_signant,
            n_subjects=args.n_subjects,
        )


if __name__ == "__main__":
    main()
