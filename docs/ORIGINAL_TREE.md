# LSC Folder Overview

`LSC` is a research workspace for sign-language recognition and related multimodal experiments. It combines inertial sensor data, landmark extraction, and video-based pipelines, together with preprocessing scripts, feature engineering, model training, and evaluation artifacts.

## Top-Level Structure

```text
LSC/
├── IMU/
├── LANDMARKS/
├── MISC/
└── VIDEOS/
```

## Folder Purpose

### `IMU/`
Inertial measurement unit processing, feature extraction, and classification experiments.

Main contents:

- `CHRONOS_FEATURES/` - Chronos-based feature outputs.
- `FEATURES/` - Feature tables used in the IMU pipeline.
- `FEATURES_NEW/` - Updated feature tables and cropped variants.
- `INFO/` - Supporting metadata such as the OpenSim model, timestamps, and volunteer reference files.
- `NW_Volunteers/` - Volunteer-level raw input spreadsheets (`.xlsx`).
- `OUT_OPENSIM/` - OpenSim motion outputs (`.mot`).
- `RAW/` - Raw source spreadsheets for the IMU workflow.
- `RESULTS/` - Plots, logs, and evaluation figures for IMU experiments.
- `SIGNS/` - Sign class folders used in the IMU experiments.
- `STO/` - OpenSim storage files (`.sto`).
- `delete_new_1.py`, `feature_extraction.py`, `grid_search.py`, `helper_functions.py`, `training.py`, `training_signant.py` - Python scripts used for preprocessing, feature generation, search, and training.
- `*.ipynb` notebooks - Interactive exploration, preprocessing, feature extraction, analysis, and synchronization work.
- `*.csv`, `*.pkl`, `*.png` - Derived datasets, trained-model artifacts, confusion matrices, feature importance outputs, and summary figures.
- `__pycache__/` - Python bytecode cache.

### `LANDMARKS/`
Landmark-based pipelines and experiments built from body, face, and hand keypoints.

Main contents:

- `BODY_LANDMARKS/` - Body landmark sequences and derived outputs.
- `FACE_LANDMARKS/` - Face landmark sequences and derived outputs.
- `HANDS_LANDMARKS/` - Hand landmark sequences and derived outputs.
- `grid_search_land.py` - Grid-search script for landmark experiments.
- `feature_extraction_chronos_lm.ipynb` - Landmark feature extraction notebook.
- `new_analysis.ipynb`, `results_analysis.ipynb`, `results_analysis_chronos.ipynb`, `sankey_diagram.ipynb`, `Analisis.ipynb` - Analysis notebooks for landmark experiments.
- `*.csv`, `*.pkl`, `*.png` - Feature tables, confusion matrices, feature importance data, and summary plots.

### `MISC/`
Supplementary assets and experiment outputs that do not fit cleanly in the main IMU/landmark/video branches.

Main contents:

- `SIGNS/` - A larger experiment area with trained models, logs, confusion matrices, dataset splits, finetuned video models, and evaluation outputs for sign classification.
- `=0.26.0`, `=4.2.0` - Small version-marker files present in the folder.

### `VIDEOS/`
Video-based data organization and the code used to generate datasets, train models, and run inference.

Main contents:

- `COLOR_BODY/` - Color video clips focused on the body crop.
- `COLOR_FACE/` - Color video clips focused on the face crop.
- `DATASET_COLOR_BODY/` - Body-crop dataset variant used for training or evaluation.
- `DATASET_COLOR_BODY_WITHOUT/` - Alternate body-crop dataset variant without the corresponding filtering or preprocessing step.
- `GRAY_DEPTH/` - Grayscale depth videos.
- `GRAY_IR/` - Grayscale infrared videos.
- `NOTEBOOKS/` - Video pipeline code, notebooks, and model artifacts.

Inside `VIDEOS/NOTEBOOKS/`:

- `dataset_generation.py`, `dataset_generation_cross_v.py` - Dataset-building scripts.
- `dataset/` - Generated dataset stored as Hugging Face-style shards, with `train/` and `test/` splits plus metadata files.
- `inference.py`, `inference_v2.py`, `inference_cm.py` - Inference and evaluation scripts.
- `model_train.py`, `model_train_custom.py` - Training scripts.
- `train_loss_curves.ipynb`, `model_train.ipynb`, `inference.ipynb`, `inference_cm.ipynb`, `init_expl.ipynb`, `circle_diagram.ipynb` - Supporting notebooks.
- `vivit-finetuned/` - Saved finetuned ViViT checkpoint.
- `# Code Citations.md` - Notes documenting external code snippets and their sources.

## Common File Types

- `.ipynb` - exploratory analysis and pipeline notebooks.
- `.py` - preprocessing, training, inference, and utility scripts.
- `.csv` - feature tables, datasets, and experiment summaries.
- `.pkl` - serialized model outputs, confusion matrices, and experiment results.
- `.png` - plots, confusion matrices, and feature-importance figures.
- `.avi` - video clips used by the video pipeline.
- `.xlsx` / `.txt` / `.mot` / `.sto` - source data, volunteer metadata, and OpenSim outputs.

## Notes

- The folder is organized by modality, not by a single dataset version, so many subfolders contain both intermediate artifacts and final outputs.
- Several notebooks and scripts appear to be research-stage tooling rather than production code.
- Most generated files are intentionally kept alongside the scripts that produced them so experiment results remain reproducible.