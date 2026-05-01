# LSC50 — Colombian Sign Language Multimodal Analysis

Research code for a 50-sign Colombian Sign Language (LSC) recognition
project that combined **IMU** (inertial sensors), **landmark** (body /
face / hand keypoints), and **video** modalities. This repository is the
cleaned-up inheritor of an earlier research workspace (see
`docs/ORIGINAL_TREE.md` for the original layout); shared logic was
extracted into `common/`, hardcoded paths replaced with CLI arguments,
and a known dataset-split bug fixed in the video pipeline.

Released under the Apache License 2.0 — see [`LICENSE`](LICENSE).

The actual data files (CSV feature tables, OpenSim motion files, video
clips, model checkpoints) are *not* part of this repo — see
`docs/DATA.md` for the expected directory schema.

## Layout

```
LSC_REPO/
├── README.md                  # this file
├── pyproject.toml             # project metadata + Python version
├── requirements.txt           # consolidated runtime deps, grouped per modality
├── .gitignore
├── docs/
│   ├── DATA.md                # expected on-disk data layout (scripts read from here)
│   ├── PIPELINE.md            # per-modality pipeline overview
│   └── ORIGINAL_TREE.md       # snapshot of the original folder description
├── common/                    # split / grid-search / evaluation helpers shared across modalities
├── imu/
│   ├── src/                   # importable modules (volunteers, feature_extraction)
│   ├── scripts/               # CLI entry points (extract_features, grid_search, train, train_signant)
│   └── notebooks/             # exploratory / analysis notebooks
├── landmarks/
│   ├── src/                   # placeholder for shared landmark code
│   ├── scripts/               # CLI entry points (grid_search)
│   └── notebooks/
└── videos/
    ├── src/                   # dataset / training / evaluation library code
    ├── scripts/               # CLI entry points (build_dataset[_cv], train[_cv], evaluate[_cv])
    │   └── legacy/            # incomplete experimental stubs preserved for reference
    └── notebooks/
        └── legacy/            # byte-identical or otherwise superseded notebooks
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is grouped by modality — comment out the sections you
don't need. The video pipeline pulls in `torch`, `transformers`, `av`, and
`datasets` (large); the IMU/landmark pipelines only need the core stack.

## Quick reference

### IMU

```bash
# 1. Crop OpenSim motion to per-sign CSVs
python imu/src/volunteers.py --base-route path/to/IMU

# 2. Extract TSFEL features
python imu/scripts/extract_features.py --signs-dir path/to/IMU/SIGNS --output-dir path/to/IMU/FEATURES_NEW

# 3. Grid search (LOSO + optional balanced/signant)
python imu/scripts/grid_search.py --features-csv path/to/general_db_imu_chronos.csv --output-dir results/

# 4. LOSO classifier comparison
python imu/scripts/train.py --features-dir path/to/IMU/FEATURES_NEW --output-dir results/
```

### Landmarks

```bash
python landmarks/scripts/grid_search.py \
    --features-csv temporal_features.csv general_db_lm_chronos.csv \
    --output-dir results/
```

### Videos

```bash
# Build splits
python videos/scripts/build_dataset.py --video-dir path/to/COLOR_BODY
python videos/scripts/build_dataset_cv.py --video-dir path/to/COLOR_BODY --subject 0

# Fine-tune ViViT
python videos/scripts/train.py --train-dataset train_dataset_v2 --test-dataset test_dataset_v2
python videos/scripts/train_cv.py --subject 0

# Evaluate
python videos/scripts/evaluate.py --model-dir ./vivit-finetuned --test-dataset test_dataset_v2
python videos/scripts/evaluate_cv.py --subjects 0 1 2 3 4
```

Every CLI accepts `--help` for a full list of options.

## Notebooks

Notebooks under `*/notebooks/` cover work that has **no script
equivalent** — Chronos embedding pipelines, grid-search results analysis,
Sankey/circos visualizations, training-loss curves, exploratory analysis.
Each notebook starts with a title cell explaining its purpose and is
broken into clear sections.

Notebooks that simply duplicated the logic of a `.py` file (interactive
copies of feature extraction, grid search, training, inference) were
removed during the reorganization — their canonical versions live under
`scripts/`.

## What was preserved verbatim

- `videos/scripts/legacy/inference_v2.py` — incomplete experimental stub
  (loaded a pre-trained ViViT-Kinetics400 checkpoint and started a Trainer
  setup that was never finished).
- `videos/notebooks/legacy/inference copy.ipynb` — byte-identical
  duplicate of `videos/notebooks/inference.ipynb`.

## What changed in the refactor

- `common/` extracts the LOSO / balanced / signant splits and the
  tqdm-instrumented `GridSearchCV` loop that were previously copy-pasted
  between IMU and LANDMARKS grid-search scripts.
- All hardcoded `LSC/IMU/...` / `LSC/VIDEOS/...` relative paths are now
  CLI arguments.
- The bug at `dataset_generation.py:64` (`dataset[i]` instead of
  `dataset[j]`) is fixed in `videos/src/dataset.py:custom_train_test_split`.
- `IMU/training.py` and `IMU/training_signant.py` no longer call
  `os.remove(...)` before writing logs; they overwrite atomically.
- Type hints added in refactored modules; debug prints and dead commented
  blocks removed.
