"""Evaluation helpers shared by the IMU and LANDMARKS pipelines."""

from __future__ import annotations

import os
import pickle
from typing import Any

import numpy as np
from sklearn.metrics import confusion_matrix


def save_confusion_matrix(
    y_true: np.ndarray, y_pred: np.ndarray, db_name: str, output_dir: str = "."
) -> str:
    """Pickle a confusion matrix to ``{output_dir}/cm_{db_name}.pkl``.

    Note: matches the original argument order ``(predicted, true)`` used by
    the legacy ``save_cm`` helpers — sklearn's ``confusion_matrix`` is invariant
    to this swap only for symmetric label sets.
    """
    cm = confusion_matrix(y_pred, y_true)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"cm_{db_name}.pkl")
    with open(path, "wb") as f:
        pickle.dump(cm, f)
    return path


def save_results(results: dict[str, Any], path: str) -> str:
    """Pickle an aggregated results dict (e.g., grid-search aggregates)."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(results, f)
    return path
