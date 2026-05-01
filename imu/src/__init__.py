"""IMU pipeline source modules.

- ``volunteers``: load per-volunteer raw data, motion files, and timestamps;
  crop the OpenSim-derived motion to per-sign segments.
- ``feature_extraction``: extract TSFEL time-series features from per-sign
  motion CSVs and aggregate into a single feature table per domain.
"""
