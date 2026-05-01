# LANDMARKS pipeline

Landmark-based experiments using body, face, and hand keypoints. Most
shared logic lives in `common/`; this modality is light because it consumes
already-extracted feature CSVs.

## `src/`

Currently a placeholder package — landmark feature extraction lives
in `notebooks/feature_extraction_chronos_lm.ipynb` and `notebooks/new_analysis.ipynb`.
Move common landmark utilities here when they appear.

## `scripts/`

| Script           | Replaces                       | Purpose                                                      |
| ---------------- | ------------------------------ | ------------------------------------------------------------ |
| `grid_search.py` | `LANDMARKS/grid_search_land.py` | Four-split grid search (balanced, LOSO, signant, signant-by-sign) over landmark CSVs |

## `notebooks/`

Analysis, feature engineering, and visualization work — none of these
duplicate code in `scripts/` or `common/`.

- `feature_extraction_chronos_lm.ipynb` — Chronos embeddings on landmarks.
- `new_analysis.ipynb` — TSFEL temporal-domain features over
  `HANDS_LANDMARKS/LEFT_HAND_LANDMARKS/*.csv`.
- `Analisis.ipynb` — exploratory mediapipe-based analysis (large file —
  re-execute it cell by cell rather than top-to-bottom).
- `results_analysis.ipynb`, `results_analysis_chronos.ipynb` — grid-search
  result inspection.
- `sankey_diagram.ipynb` — circos diagrams for landmark experiments.
