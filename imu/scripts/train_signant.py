"""CLI: binary signant-vs-nonsignant classifier training over IMU features.

Replaces ``IMU/training_signant.py``. The split holds out one random row per
``(label, signant)`` partition and uses the rest for training. The Random
Forest result is used to plot top-3 feature importances per dataset.

Usage:
    python imu/scripts/train_signant.py --features-dir path/to/IMU/FEATURES_NEW
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

from common.splits import SIGNANT_SUBJECT_IDS

DEFAULT_MODELS = [
    ("Nearest centroid", NearestCentroid()),
    ("KNeighs", KNeighborsClassifier(3)),
    ("NaiveBayes", sklearn.naive_bayes.GaussianNB()),
    ("RF", sklearn.ensemble.RandomForestClassifier(random_state=42)),
]


def _signant_holdout_split(
    data: pd.DataFrame, signant_subjects: tuple[int, ...] = SIGNANT_SUBJECT_IDS
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Build a held-out signant-vs-nonsignant split.

    For each label, randomly draw one signant row and one non-signant row into
    the validation set; the rest go to train. Mirrors the original behavior in
    ``IMU/training_signant.py``.
    """
    data = data.copy()
    data["signant"] = data["subject"].apply(lambda x: 1 if x in signant_subjects else 0)

    signs = np.unique(data["label"])
    permuted = np.random.permutation(signs)

    X_train_parts: list[pd.DataFrame] = []
    X_val_rows: list[np.ndarray] = []
    y_train: list[int] = []
    y_val: list[int] = []

    half = len(permuted) // 2

    def _slice(sign: int, signant_value: int, label: int) -> None:
        bucket = data[(data["label"] == sign) & (data["signant"] == signant_value)]
        if bucket.empty:
            return
        bucket = bucket.drop(columns=["subject", "label", "signant"]).reset_index(drop=True)
        idx = np.random.randint(0, len(bucket))
        X_val_rows.append(bucket.loc[idx, :].to_numpy())
        y_val.append(label)
        X_train_parts.append(bucket.drop(idx, axis=0))
        y_train.extend([label] * (len(bucket) - 1))

    for sign in permuted[:half]:
        _slice(sign, 0, 0)
    for sign in permuted[half:]:
        _slice(sign, 1, 1)

    return (
        pd.concat(X_train_parts).to_numpy(),
        np.array(y_train),
        np.array(X_val_rows),
        np.array(y_val),
    )


def _plot_feature_importance(
    handle: pd.DataFrame, model: sklearn.ensemble.RandomForestClassifier, label: str, output_dir: str
) -> None:
    indx = np.argsort(model.feature_importances_)[-3:][::-1]
    fig, ax = plt.subplots()
    color = handle["subject"].apply(lambda x: 1 if x in SIGNANT_SUBJECT_IDS else 0)
    ax.scatter(handle[handle.columns[indx[0]]], handle[handle.columns[indx[1]]], c=color)
    ax.set(xlabel=handle.columns[indx[0]], ylabel=handle.columns[indx[1]], title=f"Model with {label}")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{label}.png"), format="png")
    plt.close()

    plt.figure(figsize=(20, 10))
    plt.barh(handle.columns[indx], model.feature_importances_[indx])
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{label}_feat_imp.png"), format="png")
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Binary signant vs non-signant classifier training.")
    parser.add_argument("--features-dir", required=True, help="Directory with feature CSVs.")
    parser.add_argument("--output-dir", default=".", help="Output directory for figures and logs.")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    np.random.seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    csv_paths = sorted(glob.glob(os.path.join(args.features_dir, "*.csv")))
    if not csv_paths:
        print(f"No feature CSVs found in {args.features_dir}")
        return

    log_parts: list[str] = []
    best_cm: np.ndarray | None = None
    best_acc = 0.0

    for csv_path in csv_paths:
        log_parts.append(csv_path)
        print("PROCESSING", csv_path)
        handle = pd.read_csv(csv_path, index_col=0)
        X_train, y_train, X_val, y_val = _signant_holdout_split(handle)

        nn = Path(csv_path).stem

        for name, model in DEFAULT_MODELS:
            print("Training", name)
            model.fit(X_train, y_train)
            acc = model.score(X_val, y_val)
            if acc > best_acc:
                best_acc = acc
                best_cm = confusion_matrix(y_val, model.predict(X_val))
            log_parts.append(f"{name}:{acc}")

            if "RF" in name:
                _plot_feature_importance(handle, model, f"{name}{nn}", args.output_dir)

        if best_cm is not None:
            fig, ax = plt.subplots()
            ax.set_title(f"Best model - acc:{round(best_acc, 2)}")
            sns.heatmap(best_cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
            ax.set_ylabel("True label")
            ax.set_xlabel("Predicted label")
            plt.savefig(os.path.join(args.output_dir, f"confusion_matrix_{nn}.png"), format="png")
            plt.close()

    log_path = os.path.join(args.output_dir, "logs_signant.txt")
    with open(log_path, "w") as handle:
        handle.write("\n".join(log_parts) + "\n")


if __name__ == "__main__":
    main()
