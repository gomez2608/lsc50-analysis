# IMU pipeline

Inertial measurement unit processing, feature extraction, and classification
experiments.

## `src/`

- `volunteers.py` — `VolunteerInformation` class: load timestamps,
  parameters, raw IMU data, and OpenSim motion files for one volunteer;
  crop the motion file into per-sign CSVs.
- `feature_extraction.py` — TSFEL feature extraction over per-sign CSVs;
  emits one feature CSV per (domain, cropped) combination.

## `scripts/`

| Script                  | Replaces                          | Purpose                                           |
| ----------------------- | --------------------------------- | ------------------------------------------------- |
| `extract_features.py`   | `IMU/feature_extraction.py`       | Thin CLI over `src.feature_extraction.extract_all` |
| `grid_search.py`        | `IMU/grid_search.py`              | LOSO grid search over feature CSVs (uses `common/`) |
| `train.py`              | `IMU/training.py`                 | LOSO classifier comparison + best-fold heatmap    |
| `train_signant.py`      | `IMU/training_signant.py`         | Binary signant-vs-nonsignant classification       |

## `notebooks/`

Analysis and visualization work that has no script equivalent. Notebooks
that just duplicated the contents of `src/` and `scripts/` were removed
during the reorganization.

- `feature_extraction_chronos.ipynb` — Chronos (Amazon's pretrained
  time-series transformer) embeddings over IMU motion.
- `Embeddings.ipynb` — train classifiers on Chronos embeddings.
- `results_analysis.ipynb`, `results_analysis_chronos.ipynb` —
  grid-search pickle/CSV results inspection.
- `sankey_diagram.ipynb` — circos-style sign flow visualization
  (consumes `correspondance.json` produced by `sincronizacion.ipynb`).
- `sincronizacion.ipynb` — IMU/motion temporal alignment debugging;
  also generates `correspondance.json`.
