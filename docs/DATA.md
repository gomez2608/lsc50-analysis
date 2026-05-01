# Expected data layout

The companion dataset is published on figshare:

> **LSC50: Colombian Sign Language Video and Inertial Measurement Dataset**
> <https://figshare.com/articles/dataset/LSC50_Colombian_Sign_Language_Video_and_Inertial_Measurement_Dataset/27383016>

The scripts in this repo expect specific directory structures and file
conventions (the layout the data has when decompressed from figshare). The
sections below describe each modality's expected tree; arrange your local
copy accordingly and pass the prefix to the CLIs (most accept `--base-route`,
`--signs-dir`, `--features-csv`, or `--video-dir`).

## IMU

```
{IMU_ROOT}/
├── INFO/
│   ├── Timestamps.xlsx           # one sheet per "Volunteer N", columns: sign, start, end (seconds)
│   ├── Volunteer_1.txt           # KEY: VALUE lines (height, age, etc.)
│   ├── Volunteer_2.txt
│   └── ...
├── RAW/
│   ├── Volunteer_1.xlsx          # one sheet per IMU channel (hand_l_imu, ...)
│   └── ...
├── OUT_OPENSIM/
│   ├── Volunteer_1.mot           # OpenSim motion (TSV with 6-row header)
│   └── ...
├── SIGNS/                        # produced by `imu/src/volunteers.py`
│   ├── {sign_name}/
│   │   └── nw_Volunteer_{n}.csv
│   └── ...
├── FEATURES_NEW/                 # produced by `imu/scripts/extract_features.py`
│   ├── statistical.csv
│   ├── statistical_cropped.csv
│   ├── temporal.csv
│   ├── temporal_cropped.csv
│   ├── spectral.csv
│   ├── spectral_cropped.csv
│   ├── all.csv
│   └── all_cropped.csv
├── CHRONOS_FEATURES/             # Chronos embeddings; see notebooks/feature_extraction_chronos.ipynb
└── general_db_imu_chronos.csv    # consolidated feature table consumed by `imu/scripts/grid_search.py`
```

### Feature CSV schema

Every feature CSV consumed downstream (`imu/scripts/grid_search.py`,
`imu/scripts/train.py`, `imu/scripts/train_signant.py`) has the following
columns:

| column     | type | description                                                  |
| ---------- | ---- | ------------------------------------------------------------ |
| feature_*  | float | TSFEL or Chronos features, one column per derived statistic |
| `label`    | int  | sign id (`0..49`)                                            |
| `subject`  | int  | volunteer id (`0..N-1`)                                      |
| `Unnamed: 0` (optional) | int | pandas-emitted index, dropped by the loaders |

## Landmarks

```
{LANDMARKS_ROOT}/
├── BODY_LANDMARKS/
├── FACE_LANDMARKS/
├── HANDS_LANDMARKS/
├── temporal_features.csv          # consumed by landmarks/scripts/grid_search.py
└── general_db_lm_chronos.csv
```

The CSV schema matches the IMU feature CSVs. The `rep` column, if present,
is dropped by the grid-search script before training.

## Videos

```
{VIDEOS_ROOT}/
├── COLOR_BODY/                    # body-cropped color clips (consumed by build_dataset[_cv])
│   ├── 0000_0000_0001.avi
│   ├── 0000_0001_0001.avi         # filename: {label}_{subject}_{clip}.avi
│   └── ...
├── COLOR_FACE/
├── GRAY_DEPTH/
├── GRAY_IR/
├── DATASET_COLOR_BODY/             # alternative datasets used in some experiments
├── DATASET_COLOR_BODY_WITHOUT/
├── train_dataset_v2/               # produced by build_dataset.py (HF dataset on disk)
├── test_dataset_v2/
├── train_dataset_v2_subject_{i}/   # produced by build_dataset_cv.py
├── test_dataset_v2_subject_{i}/
├── vivit-finetuned*/               # fine-tuned model checkpoints
└── confusion_matrix*.pkl           # outputs of evaluate[_cv].py
```

### Filename convention

The video scripts split out `label` and `subject` from the underscore-separated
filename: the first token is the integer label, the second is the integer
subject id.

## Class mapping

The 50 sign classes are statically mapped in
`videos/src/evaluate.py:CLASS_MAPPING`. If the IMU/LANDMARKS pipelines
produce labels in the same order (which the original notebooks assume), this
mapping applies there too.
