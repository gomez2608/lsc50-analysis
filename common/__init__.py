"""Shared utilities used by the IMU and LANDMARKS classification pipelines.

Contents:
- splits: train/test split strategies (LOSO, balanced, signant binary).
- grid_search: hyperparameter search runner with tqdm progress and CV.
- evaluation: confusion-matrix persistence helpers.
"""
