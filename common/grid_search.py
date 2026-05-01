"""Hyperparameter grid search runner shared by IMU and LANDMARKS scripts.

The original code used ``GridSearchCV`` with a tqdm progress bar implemented
by monkey-patching ``_run_search``. That logic lived (verbatim) in two
separate scripts; this module is the single source of truth.
"""

from __future__ import annotations

from typing import Any, Iterable

import numpy as np
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from tqdm import tqdm

DEFAULT_SEED = 42

# Default parameter grids used in the original IMU and LANDMARKS scripts.
# Kept here so both modalities pull from the same spec.
RF_PARAMS: dict[str, list[Any]] = {
    "n_estimators": [10, 50, 100, 200],
    "criterion": ["gini", "entropy", "log_loss"],
    "max_depth": [None, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

SVC_PARAMS: dict[str, list[Any]] = {
    "C": [0.1, 1, 10, 100],
    "kernel": ["rbf", "sigmoid", "poly"],
    "degree": [2, 3, 4],
    "decision_function_shape": ["ovo", "ovr"],
}

KNN_PARAMS: dict[str, list[Any]] = {
    "n_neighbors": [3, 5, 7, 9],
    "weights": ["uniform", "distance"],
    "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
    "leaf_size": [10, 30, 50, 100],
}

PARAM_GRIDS: dict[str, dict[str, list[Any]]] = {
    "knn": KNN_PARAMS,
    "svc": SVC_PARAMS,
    "rf": RF_PARAMS,
}


def default_models(seed: int = DEFAULT_SEED) -> list[tuple[str, BaseEstimator]]:
    """Return the canonical (name, estimator) list used by both pipelines."""
    return [
        ("knn", KNeighborsClassifier()),
        ("svc", SVC(random_state=seed)),
        ("rf", RandomForestClassifier(random_state=seed)),
    ]


def _grid_total(grid: dict[str, Iterable[Any]]) -> int:
    total = 1
    for values in grid.values():
        total *= len(list(values))
    return total


def run_grid_search(
    estimator: BaseEstimator,
    param_grid: dict[str, Iterable[Any]],
    X_train: np.ndarray,
    y_train: np.ndarray,
    *,
    cv: int = 3,
    scoring: str = "f1_weighted",
    n_jobs: int = -1,
    desc: str = "GridSearchCV",
) -> GridSearchCV:
    """Fit a ``GridSearchCV`` while showing a tqdm progress bar.

    Mirrors the original monkey-patched ``_run_search`` trick — we keep it
    because it's the only way to surface progress without a sklearn callback.
    """
    search = GridSearchCV(
        estimator, dict(param_grid), n_jobs=n_jobs, cv=cv, scoring=scoring, verbose=0
    )

    total = _grid_total(param_grid)
    with tqdm(total=total, desc=desc, unit="comb") as pbar:
        original = search._run_search

        def with_progress(evaluate_candidates):  # type: ignore[no-untyped-def]
            def wrapped(candidate_params):  # type: ignore[no-untyped-def]
                pbar.update(len(candidate_params))
                return evaluate_candidates(candidate_params)

            return original(wrapped)

        search._run_search = with_progress  # type: ignore[assignment]
        search.fit(X_train, y_train)

    return search


def summarize_search(search: GridSearchCV, y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, Any]:
    """Build the per-(model, split) result dict used by the original scripts."""
    from sklearn.metrics import f1_score

    summary: dict[str, Any] = {
        "f1_score": f1_score(y_true, y_pred, average="weighted"),
        "best_params": search.best_params_,
        "train_scores": search.cv_results_,
    }
    if hasattr(search.best_estimator_, "feature_importances_"):
        summary["feature_importances"] = search.best_estimator_.feature_importances_
    return summary
