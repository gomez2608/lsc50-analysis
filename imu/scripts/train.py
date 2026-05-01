"""CLI: LOSO classifier training over the per-domain IMU feature CSVs.

Replaces ``IMU/training.py``. Iterates over every CSV under ``--features-dir``,
runs LOSO with four classifiers, logs per-fold accuracy, and writes the best
fold's confusion matrix as a heatmap.

Usage:
    python imu/scripts/train.py --features-dir path/to/IMU/FEATURES_NEW
"""

from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn.ensemble
import sklearn.naive_bayes
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.splits import loso_train_test_split

DEFAULT_MODELS = [
    ("Nearest centroid", NearestCentroid()),
    ("KNeighs", KNeighborsClassifier(3)),
    ("NaiveBayes", sklearn.naive_bayes.GaussianNB()),
    ("RF", sklearn.ensemble.RandomForestClassifier(random_state=42)),
]


def _process_csv(csv_path: str, output_dir: str, n_subjects: int) -> tuple[str, float, np.ndarray | None]:
    log_lines = [csv_path]
    handle = pd.read_csv(csv_path, index_col=None)
    best_cm: np.ndarray | None = None
    best_acc = 0.0

    for i in range(n_subjects):
        log_lines.append(f"SUBJECT {i} AS VALIDATION")
        X_train, y_train, X_val, y_val = loso_train_test_split(handle, validation_subject=i)
        for name, model in DEFAULT_MODELS:
            model.fit(X_train, y_train)
            acc = model.score(X_val, y_val)
            if acc > best_acc:
                best_acc = acc
                best_cm = confusion_matrix(y_val, model.predict(X_val))
            log_lines.append(f"{name}:{acc}")

    if best_cm is not None:
        os.makedirs(output_dir, exist_ok=True)
        fig, ax = plt.subplots(figsize=(20, 20))
        ax.set_title(f"Best model - acc:{round(best_acc, 2)}")
        sns.heatmap(best_cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
        ax.set_ylabel("True label")
        ax.set_xlabel("Predicted label")
        out = os.path.join(output_dir, f"confusion_matrix_big_{Path(csv_path).stem}.png")
        plt.savefig(out, format="png")
        plt.close()

    return "\n".join(log_lines) + "\n", best_acc, best_cm


def main() -> None:
    parser = argparse.ArgumentParser(description="LOSO training over IMU feature CSVs.")
    parser.add_argument("--features-dir", required=True, help="Directory with feature CSVs (output of extract_features.py).")
    parser.add_argument("--output-dir", default=".", help="Directory for logs and figures.")
    parser.add_argument("--n-subjects", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--log-name", default="logs.txt")
    args = parser.parse_args()

    np.random.seed(args.seed)

    csv_paths = sorted(glob.glob(os.path.join(args.features_dir, "*.csv")))
    if not csv_paths:
        print(f"No feature CSVs found in {args.features_dir}")
        return

    full_log: list[str] = []
    for csv_path in csv_paths:
        print("PROCESSING", csv_path)
        section, _, _ = _process_csv(csv_path, args.output_dir, args.n_subjects)
        full_log.append(section)

    os.makedirs(args.output_dir, exist_ok=True)
    log_path = os.path.join(args.output_dir, args.log_name)
    with open(log_path, "w") as handle:
        handle.write("".join(full_log))


if __name__ == "__main__":
    main()
