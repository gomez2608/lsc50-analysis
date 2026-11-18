# Pipeline overview

> **Note (2026-10-20):** this file describes the *original* pipeline. The revision for PLOS One (leakage fixes, reruns, new baselines and analyses) is documented in [`README_REVISION.md`](README_REVISION.md) and the files it indexes.


Each modality has the same conceptual flow: raw input → features → train/
evaluate. The shapes differ; the abstractions in `common/` (splits, grid
search, evaluation) are shared by IMU and LANDMARKS because both end up as
tabular feature CSVs.

## IMU

```
RAW/Volunteer_*.xlsx + INFO/Timestamps.xlsx + OUT_OPENSIM/*.mot
        │
        │  imu/src/volunteers.py:VolunteerInformation.crop_motion_to_signs
        ▼
SIGNS/{sign}/nw_Volunteer_{n}.csv
        │
        │  imu/src/feature_extraction.py:extract_all (TSFEL)
        ▼
FEATURES_NEW/{domain}[_cropped].csv          ← also: general_db_imu_chronos.csv
        │
        ├─ imu/scripts/grid_search.py        (LOSO + optional balanced/signant)
        ├─ imu/scripts/train.py              (LOSO classifier comparison)
        └─ imu/scripts/train_signant.py      (binary signant vs non-signant)
```

## Landmarks

```
{BODY,FACE,HANDS}_LANDMARKS/  +  Chronos embeddings
        │
        │  notebooks/feature_extraction_chronos_lm.ipynb
        ▼
temporal_features.csv  +  general_db_lm_chronos.csv
        │
        │  landmarks/scripts/grid_search.py
        ▼
results/
  ├─ cm_{model}_{db}_{split}.pkl
  └─ grid_search_results_{db}_chronos[_new_schema].pkl
```

The landmark grid-search runs four splits per CSV: balanced (stratified
random), LOSO, signant binary (rows split), and signant binary "new schema"
(test signs held out by sign id, not by row).

## Videos

```
COLOR_BODY/*.avi
        │
        ├─ videos/scripts/build_dataset.py        (random per-class split)
        │      └─ train_dataset_v2 / test_dataset_v2
        │
        └─ videos/scripts/build_dataset_cv.py     (per-subject LOSO)
               └─ train_dataset_v2_subject_{i} / test_dataset_v2_subject_{i}
        │
        │  videos/scripts/train.py    or    videos/scripts/train_cv.py
        ▼
vivit-finetuned-def/   or   vivit-finetuned-s{i}/
        │
        │  videos/scripts/evaluate.py    or    videos/scripts/evaluate_cv.py
        ▼
confusion_matrix.pkl    or    confusion_matrix_subject_{i}.pkl
```

The general flow uses `model_train.py` defaults (13 epochs, batch=2,
lr=5e-5). The per-subject flow uses larger numbers (30 epochs, batch=3,
lr=6e-5) and supports resume-from-checkpoint via `--resume`.

## Shared layer (`common/`)

| Module                  | Used by                                                           |
| ----------------------- | ----------------------------------------------------------------- |
| `common.splits`         | both grid_search scripts; `imu/scripts/train.py`                  |
| `common.grid_search`    | both grid_search scripts (param grids, models, runner)            |
| `common.evaluation`     | both grid_search scripts (CM saving, results pickling)            |
