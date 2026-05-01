"""Train/test split strategies shared by the IMU and LANDMARKS pipelines.

All splits expect a pandas DataFrame with two reserved columns:
- ``subject``: integer subject id (1..N).
- ``label``: integer sign id.

The remaining columns are treated as feature columns. ``Unnamed: 0`` (an
artifact of pandas' ``to_csv`` default behavior) is dropped if present.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

DEFAULT_SEED = 42

# Subject ids treated as "signant" (deaf signers) in the binary signant task.
# Everyone else is treated as "non-signant".
SIGNANT_SUBJECT_IDS: tuple[int, ...] = (1, 2)


def _drop_unnamed(data: pd.DataFrame) -> pd.DataFrame:
    if "Unnamed: 0" in data.columns:
        return data.drop(columns=["Unnamed: 0"])
    return data


def loso_train_test_split(
    data: pd.DataFrame, validation_subject: int = 1, no_sign_label: int = 42
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Leave-one-subject-out split.

    The ``no_sign_label`` argument lets the caller drop a sentinel "no sign"
    class from the validation set (matches the original IMU behavior).

    Returns ``(X_train, y_train, X_val, y_val)``.
    """
    data = _drop_unnamed(data)

    subjects = data["subject"].to_numpy()
    y = data["label"].to_numpy()
    X = data.drop(["subject", "label"], axis=1).to_numpy()

    val_index = np.where(subjects == validation_subject)
    train_index = np.where(subjects != validation_subject)

    X_val, y_val = X[val_index], y[val_index]
    X_train, y_train = X[train_index], y[train_index]

    if no_sign_label in y_val:
        no_sign_index = np.where(y_val == no_sign_label)
        y_val = np.delete(y_val, no_sign_index)
        X_val = np.delete(X_val, no_sign_index, axis=0)

    return X_train, y_train, X_val, y_val


def train_test_split_balanced(
    data: pd.DataFrame,
    test_size: float = 0.2,
    seed: int = DEFAULT_SEED,
    feature_names_path: str | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Stratified random split on the ``label`` column.

    Optionally writes the column names to ``feature_names_path`` (used by the
    IMU pipeline to persist the schema for later analysis).
    """
    data = _drop_unnamed(data)

    if feature_names_path is not None:
        with open(feature_names_path, "w") as f:
            for col in data.columns:
                f.write(f"{col}\n")

    y = data["label"].to_numpy()
    X = data.drop(["label", "subject"], axis=1).to_numpy()
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=seed)


def train_test_split_interpreter_signant(
    data: pd.DataFrame,
    test_size: float = 0.2,
    seed: int = DEFAULT_SEED,
    signant_subjects: tuple[int, ...] = SIGNANT_SUBJECT_IDS,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Stratified split for the binary "signant vs non-signant" task."""
    data = _drop_unnamed(data)

    y = np.array([0 if s in signant_subjects else 1 for s in data["subject"].to_numpy()])
    X = data.drop(["label", "subject"], axis=1).to_numpy()
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=seed)


def train_test_split_interpreter_signant_by_signs(
    data: pd.DataFrame,
    n_test_signs: int = 10,
    seed: int = DEFAULT_SEED,
    signant_subjects: tuple[int, ...] = SIGNANT_SUBJECT_IDS,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Signant binary split where the test set is held out by *sign*, not by row.

    ``n_test_signs`` distinct sign labels are sampled into the test set; rows
    for those signs (across all subjects) become the test split. Used by the
    LANDMARKS pipeline as the "new schema" experiment.
    """
    data = _drop_unnamed(data)

    signs = np.unique(data["label"])
    rng = np.random.default_rng(seed)
    test_signs = rng.choice(signs, size=n_test_signs, replace=False)
    train_signs = np.setdiff1d(signs, test_signs)

    train_data = data[data["label"].isin(train_signs)]
    test_data = data[data["label"].isin(test_signs)]

    def _binary(subjects: np.ndarray) -> np.ndarray:
        return np.array([0 if s in signant_subjects else 1 for s in subjects])

    y_train = _binary(train_data["subject"].to_numpy())
    X_train = train_data.drop(["label", "subject"], axis=1).to_numpy()

    y_test = _binary(test_data["subject"].to_numpy())
    X_test = test_data.drop(["label", "subject"], axis=1).to_numpy()

    return X_train, X_test, y_train, y_test
