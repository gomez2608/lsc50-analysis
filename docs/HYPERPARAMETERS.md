# Hyperparameter search and selected settings

Addresses R2.11 (and the setup part of R1.8). Source of truth: `common/grid_search.py`,
`landmarks/scripts/grid_search.py`, `imu/scripts/grid_search.py`, `videos/src/train.py`.
Selected settings are regenerated with `scripts/revision/hyperparams_table.py`.

## Classical models (SVM, RF, KNN)

**Pipeline per split.** Features are standardized with `StandardScaler` fitted on
the training rows only. Each model is tuned with scikit-learn `GridSearchCV`
(exhaustive grid, scoring = weighted F1) on the training rows, refitted on all
training rows with the best setting, and evaluated once on the test rows.
Ties in inner-CV score go to the first setting in grid order.

**Inner cross-validation** (hyperparameter selection only):

| Split | Landmarks | IMU |
|-------|-----------|-----|
| 80/20 (SLR) | stratified 4-fold over rows | stratified 3-fold over rows |
| LOSO (SLR) | stratified 4-fold over rows; `--inner-cv group`: one training signer per fold (4 folds) | stratified 3-fold; `--inner-cv group`: as landmarks |
| Native vs. interpreter | stratified 5-fold | stratified 5-fold |

Random seeds: `random_state = seed` for SVM and RF; the 80/20 split uses the same
seed. Seeds 0–4 are reported as mean ± SD.

**Grids** (`common/grid_search.py`):

| Model | Parameter | Values |
|-------|-----------|--------|
| SVM (`SVC`) | `C` | 0.1, 1, 10, 100 |
| | `kernel` | rbf, sigmoid, poly |
| | `degree` (poly only) | 2, 3, 4 |
| | `decision_function_shape` | ovo, ovr |
| | `gamma` | `scale` (default, not searched) |
| RF (`RandomForestClassifier`) | `n_estimators` | 10, 50, 100, 200 |
| | `criterion` | gini, entropy, log_loss |
| | `max_depth` | None, 5, 10, 20 |
| | `min_samples_split` | 2, 5, 10 |
| | `min_samples_leaf` | 1, 2, 4 |
| KNN (`KNeighborsClassifier`) | `n_neighbors` | 3, 5, 7, 9 |
| | `weights` | uniform, distance |
| | `algorithm` | auto, ball_tree, kd_tree, brute |
| | `leaf_size` | 10, 30, 50, 100 |

Grid sizes are 72 (SVM), 432 (RF) and 128 (KNN) combinations, but several
parameters do not change predictions: `decision_function_shape` (SVC always
trains one-vs-one), `degree` outside the poly kernel, and KNN `algorithm` /
`leaf_size` (search structure only). The **effective** grids are 20 distinct
SVM models, 432 RF models and 8 KNN models. Because ties go to the first grid
entry, the selected `ovo`, `auto`, `leaf_size=10` and `degree=2` values carry no
information. For the revision we suggest reporting the effective grids only.

## Selected settings, SLR, seed 0 (2026-10-15) — superseded

*Superseded by the next section (2026-10-20, audit D4): this table is from the first protocol (seed 0, stratified inner CV, image coordinates). Kept as a record.*

Most frequent setting across runs (1 run for 80/20, 5 LOSO folds); inert parameters omitted.

| Features | Split | Model | Most frequent setting | Runs |
|----------|-------|-------|-----------------------|------|
| Landmarks TSFEL | 80/20 | SVM | C=10, kernel=rbf | 1/1 |
| Landmarks TSFEL | 80/20 | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 1/1 |
| Landmarks TSFEL | 80/20 | KNN | n_neighbors=3, weights=distance | 1/1 |
| Landmarks TSFEL | LOSO | SVM | C=10, kernel=rbf | 4/5 |
| Landmarks TSFEL | LOSO | RF | criterion=entropy, max_depth=10, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 2/5 |
| Landmarks TSFEL | LOSO | KNN | n_neighbors=7, weights=distance | 2/5 |
| Landmarks Chronos | 80/20 | SVM | C=100, kernel=rbf | 1/1 |
| Landmarks Chronos | 80/20 | RF | criterion=gini, max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 1/1 |
| Landmarks Chronos | 80/20 | KNN | n_neighbors=3, weights=distance | 1/1 |
| Landmarks Chronos | LOSO | SVM | C=100, kernel=rbf | 3/5 |
| Landmarks Chronos | LOSO | RF | criterion=gini, max_depth=None, min_samples_leaf=2, min_samples_split=2, n_estimators=200 | 1/5 |
| Landmarks Chronos | LOSO | KNN | n_neighbors=3, weights=distance | 3/5 |
| IMU TSFEL | 80/20 | SVM | C=100, kernel=sigmoid | 1/1 |
| IMU TSFEL | 80/20 | RF | criterion=entropy, max_depth=None, min_samples_leaf=2, min_samples_split=5, n_estimators=200 | 1/1 |
| IMU TSFEL | 80/20 | KNN | n_neighbors=5, weights=uniform | 1/1 |
| IMU TSFEL | LOSO | SVM | C=100, kernel=sigmoid | 3/5 |
| IMU TSFEL | LOSO | RF | criterion=gini, max_depth=20, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 1/5 |
| IMU TSFEL | LOSO | KNN | n_neighbors=5, weights=distance | 2/5 |
| IMU Chronos | 80/20 | SVM | C=10, degree=2, kernel=poly | 1/1 |
| IMU Chronos | 80/20 | RF | criterion=gini, max_depth=20, min_samples_leaf=2, min_samples_split=2, n_estimators=50 | 1/1 |
| IMU Chronos | 80/20 | KNN | n_neighbors=5, weights=distance | 1/1 |
| IMU Chronos | LOSO | SVM | C=10, kernel=sigmoid | 4/5 |
| IMU Chronos | LOSO | RF | criterion=gini, max_depth=10, min_samples_leaf=1, min_samples_split=5, n_estimators=100 | 1/5 |
| IMU Chronos | LOSO | KNN | n_neighbors=3, weights=distance | 2/5 |

RF settings vary from fold to fold (no setting chosen in more than 2 of 5
folds), which is expected with a 432-point grid and many near-tied settings.

## ViViT (`videos/`)

Backbone `google/vivit-b-16x2-kinetics400` (ViViT-B, spatio-temporal attention, 88,954,000 parameters, **all fine-tuned**; checked against the original checkpoints, `REVISION_LOG.md` §7.8). Input: 32 frames sampled uniformly over the clip, resized and centre-cropped to 224 × 224 with the checkpoint's image processor (16 × 14 × 14 = 3,136 tokens). Optimizer: Hugging Face `Trainer` default AdamW, linear learning-rate decay, no warm-up. Classification head re-initialized for 50 classes. No hyperparameter search.

| Setting | Original 80/20 | Original LOSO | Revision 80/20 | Revision LOSO, protocol A | Revision LOSO, protocol B |
|---------|----------------|---------------|----------------|---------------------------|---------------------------|
| Script | `train.py` | `train_cv.py` | `train.py --dataset clips_all` | `train_cv.py --val-mode signer` | `train_cv.py --val-mode none` |
| Training data | 1,600 rows (2,000-row set; test = 100 training clips × 4, P3) | 800 clips (4 signers) | 720 clips (80% of 1,000, minus 10% validation) | 600 clips (3 signers) | 800 clips (4 signers) |
| Checkpoint kept | best epoch by **test** accuracy (P13) | best epoch by **test** accuracy (P13) | best epoch by weighted F1 on 10% of training rows | best epoch by weighted F1 on the 4th training signer | final epoch (no selection) |
| Epochs | 13 | 30 | 13 | 30 | 30 |
| Learning rate | 5e-5 | 6e-5 | 5e-5 | 6e-5 | 6e-5 |
| Batch | 2 per GPU × 4 GPUs × 4 accumulation (log: 25 steps/epoch on 1,600) | 3 per GPU × 4 GPUs × 4 accumulation = 48 | 1 × 32 accumulation = 32 | 1 × 48 accumulation = 48 | 1 × 48 accumulation = 48 |
| Precision | fp16 | fp16 | fp32 | fp32 | fp32 |
| Hardware | 4 × TITAN X (Pascal) 12 GB, DataParallel | same | 1 TITAN X (Pascal) per job | same | same |
| Time per job | 7.2 h | 18.2 h per fold | ~4.5 h | ~9 h | ~12.5 h |
| Seeds | 1 (unseeded split) | 1 | 0, 1, 2 | 0, 1, 2 | 0, 1, 2 |
| Logged per epoch | test accuracy | test accuracy | training loss; validation loss, accuracy, F1 | training loss; validation loss, accuracy, F1 | training loss |

fp32 instead of fp16: on Pascal GPUs fp16 is ~6.6× slower per clip (benchmark, `REVISION_LOG.md` §7.4); the effective batch sizes are kept. Every revision job scores the test split once, after training, and writes `results.json` (accuracy, weighted and macro F1, all predictions).

## Linear probe on frozen ViViT (`scripts/revision/linear_probe.py`)

Frozen pretrained ViViT (not fine-tuned), one forward pass per clip; features = final-layer CLS token (768) or mean over all tokens. Standardized logistic regression (`lbfgs`, `max_iter=5000`), C ∈ {0.001, 0.01, 0.1, 1, 10} chosen by inner CV on the training rows (LOSO: one training signer per inner fold; 80/20: stratified 4-fold), scoring weighted F1. The same CLS features also go through the SVM / RF / KNN grids above.

## Selected settings, main pipelines (2026-10-20)

Regenerated with `scripts/revision/hyperparams_table.py` on the server from the result pickles of the pipelines reported in the revision: grouped inner CV for LOSO (5 signers × seeds 0–4 = 25 runs; frozen ViViT seed 0 only = 5 runs) and, for body-relative TSFEL and frozen ViViT, the 80/20 runs (seeds 0–4). Most frequent setting and how many runs chose it; inert parameters omitted.

| Features | Split | Model | Most frequent setting | Runs |
|----------|-------|-------|-----------------------|------|
| IMU Chronos | LOSO, grouped inner CV | KNN | n_neighbors=5, weights=distance | 10/25 |
| IMU Chronos | LOSO, grouped inner CV | RF | criterion=gini, max_depth=None, min_samples_leaf=2, min_samples_split=10, n_estimators=100 | 2/25 |
| IMU Chronos | LOSO, grouped inner CV | SVM | C=10, kernel=rbf | 10/25 |
| Landmarks Chronos (image coordinates) | LOSO, grouped inner CV | KNN | n_neighbors=3, weights=distance | 15/25 |
| Landmarks Chronos (image coordinates) | LOSO, grouped inner CV | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 4/25 |
| Landmarks Chronos (image coordinates) | LOSO, grouped inner CV | SVM | C=100, kernel=rbf | 15/25 |
| IMU TSFEL | LOSO, grouped inner CV | KNN | n_neighbors=7, weights=distance | 15/25 |
| IMU TSFEL | LOSO, grouped inner CV | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=5, n_estimators=200 | 3/25 |
| IMU TSFEL | LOSO, grouped inner CV | SVM | C=10, kernel=rbf | 20/25 |
| Landmarks TSFEL, image coordinates | LOSO, grouped inner CV | KNN | n_neighbors=7, weights=distance | 10/25 |
| Landmarks TSFEL, image coordinates | LOSO, grouped inner CV | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 4/25 |
| Landmarks TSFEL, image coordinates | LOSO, grouped inner CV | SVM | C=10, kernel=rbf | 20/25 |
| Landmarks TSFEL, body-relative | 80/20 | KNN | n_neighbors=3, weights=distance | 5/5 |
| Landmarks TSFEL, body-relative | 80/20 | RF | criterion=entropy, max_depth=10, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 3/5 |
| Landmarks TSFEL, body-relative | 80/20 | SVM | C=10, kernel=rbf | 5/5 |
| Landmarks TSFEL, body-relative | LOSO, grouped inner CV | KNN | n_neighbors=5, weights=distance | 20/25 |
| Landmarks TSFEL, body-relative | LOSO, grouped inner CV | RF | criterion=entropy, max_depth=None, min_samples_leaf=2, min_samples_split=2, n_estimators=200 | 4/25 |
| Landmarks TSFEL, body-relative | LOSO, grouped inner CV | SVM | C=10, kernel=rbf | 20/25 |
| Frozen ViViT CLS | 80/20 | KNN | n_neighbors=3, weights=distance | 5/5 |
| Frozen ViViT CLS | 80/20 | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=2, n_estimators=200 | 3/5 |
| Frozen ViViT CLS | 80/20 | SVM | C=100, kernel=rbf | 4/5 |
| Frozen ViViT CLS | LOSO, grouped inner CV | KNN | n_neighbors=3, weights=distance | 2/5 |
| Frozen ViViT CLS | LOSO, grouped inner CV | RF | criterion=entropy, max_depth=None, min_samples_leaf=1, min_samples_split=5, n_estimators=200 | 1/5 |
| Frozen ViViT CLS | LOSO, grouped inner CV | SVM | C=0.1, kernel=sigmoid | 3/5 |

RF settings are spread over many near-tied grid points (no setting chosen in more than 4 of 25 runs). SVM settles on an RBF kernel with C = 10 or 100 for every landmark and IMU table.

## Linear probe, selected C

C ∈ {0.001, 0.01, 0.1, 1, 10}, chosen by inner CV (`docs/results/vivit_frozen_probe_cls.csv`): 80/20 seeds 0–4: C = 1 in 5/5; LOSO: C = 0.01 in 4/5 folds (Volunteer 3's fold: C = 1).

## Native vs. interpreter (binary)

Same SVM / RF / KNN grids and scaler as the sign task; inner CV stratified, 5 folds (a signer-grouped inner fold can leave one class only); splits: rows 80/20, 10 signs held out, one signer held out (`landmarks/scripts/grid_search.py --parts signant signant_new_schema signant_loso`; `imu/scripts/grid_search.py --include-signant`). Signer-level permutation check (`signant_labeling_permutation.py`): fixed settings, no search — RF 200 trees (random state = seed), SVM RBF C = 1, KNN k = 5, each after a standard scaler.

## ST-GCN (`scripts/revision/stgcn_baseline.py`; official code, `third_party/st_gcn`, commit 221c0e1)

Model as published: 10 ST-GCN blocks, spatial partition, learnable edge importance, dropout 0.5, 3,204,180 parameters with the LSC50 graph (65 nodes; input 2 channels × 24 frames × 65 nodes × 1 person). SGD, Nesterov momentum 0.9, weight decay 1e-4, cross-entropy; final model kept.

| Setting | NTU recipe, ported by epochs (stopped, §5.19) | Revised recipe (`run_stgcn_v2.sh`, 9c68806) |
|---------|------------------------------------------------|---------------------------------------------|
| Batch | 64 (~13 updates per epoch) | 16 (~50 updates per epoch) |
| Epochs / updates | 80 / ~1,000 | 200 / ~10,000 |
| Learning rate | 0.1, ×0.1 at epochs 10 and 50 | chosen from {0.05, 0.025, 0.01}, ×0.1 at epochs 25 and 125 (the NTU fractions), 5-epoch linear warm-up |
| Learning-rate choice | none (published value) | per input, highest mean validation F1 over the 5 LOSO folds, validating on training signer (s + 1) mod 5 with the test signer dropped; seed 0 |
| Hardware | server CPU, 3 threads | 1 GPU, shared with ViViT |
| Training fit | final loss 0.32–3.87; 4 of 30 runs never fit | training accuracy ≥ 0.99 in every final run |
| Selected learning rate | — | image coordinates **0.025** (mean validation F1 0.223 vs. 0.212 at 0.05, 0.216 at 0.01); body-relative **0.05** (0.277 vs. 0.266 at 0.025, 0.249 at 0.01; the top of the pre-set grid, kept as the rule says) |

Selection runs and validation scores: `docs/results/stgcn_v2/` (REVISION_LOG §5.21).

## SlowFast R50 (`scripts/revision/slowfast_baseline.py`; PyTorchVideo 0.1.5, `slowfast_r50`, Kinetics-400 weights)

| Setting | Value | Source |
|---------|-------|--------|
| Input | 32 frames sampled uniformly; short side 256, centre crop 256 × 256; mean 0.45, std 0.225; slow pathway every 4th frame (α = 4) | authors' Kinetics evaluation transform |
| Head | final linear layer replaced, 2304 → 50 | — |
| Fine-tuning | all 33,759,738 parameters of the 50-class model (34.6 M with the 400-class Kinetics head); BatchNorm running statistics frozen (scale and shift trained) | our choice (audit K5) |
| Optimizer | SGD, momentum 0.9, weight decay 1e-4, cosine decay over all updates | our choice within the authors' standard family (no published small-data recipe) |
| Warm-up | 3 epochs, linear, per optimizer step (revised recipe, 2026-10-23) | authors' SlowFast recipes use a linear warm-up |
| Learning rate | chosen from {0.01, 0.003, 0.001}: each LOSO fold with the test signer dropped, validation on training signer (s + 1) mod 5, seed 0; highest mean validation F1 (ties within 0.005 → lower rate). Mean validation F1 0.192 (2 of 5 diverged), **0.441**, 0.317 → **0.003** | as ST-GCN |
| First recipe (not reported) | lr 0.01, no warm-up: 8 of 18 runs never trained (REVISION_LOG §5.20) | — |
| Schedule | 30 epochs, final model kept; batch 4 × 12 accumulation = 48 | matched to ViViT protocol B |
| Precision, augmentation | fp32; no augmentation (no horizontal flip: it would swap the signing hands) | — |
| Data | 997 clips (the 3 duplicate executions dropped, P7, audit K6) | — |
| Divergence guard | a run whose epoch loss becomes non-finite stops and is flagged, reported and counted (none in the final runs) | — |

Selection runs: `docs/results/slowfast_v2/selection/`; reported runs: the fusion retraining, `docs/results/fusion/slowfast/` (same recipe; REVISION_LOG §5.25).

## Official SPOTER (`third_party/spoter/`, commit 0f909bf, unmodified; glue `scripts/revision/spoter_baseline.py`)

Repository defaults, nothing tuned (protocol S7 in `POSE_TRANSFORMER_STUDY.md`):

| Setting | Value |
|---------|-------|
| Model | hidden dimension 108 (54 joints × 2), 9 heads, 6 encoder + 6 decoder layers, class query |
| Input | native-length sequences, image coordinates; 54 joints = 11 MediaPipe pose points + neck (shoulder midpoint, our glue) + 21 + 21 hand points; y → 1 − y (SPOTER's Apple Vision convention); SPOTER's body and hand normalization |
| Optimizer | SGD, lr 0.001, no momentum; the repository's ReduceLROnPlateau is created but never stepped, so the rate is constant |
| Schedule | batch 1, 100 epochs, final model kept (the repository's `train.py` reports the best checkpoint on the test set: not used) |
| Regularization | Gaussian noise sd 0.001 on training inputs; the authors' augmentations, each with probability 0.5: rotation ±13°, perspective shear, squeeze, arm-joint rotation |
| Environment | Python 3.9, torch 1.8.1 CPU, pandas 1.1.5 (repository requirements) |

## Late fusion (SlowFast + SPOTER; `scripts/revision/fusion.py`)

No hyperparameters: the mean of the two models' class probabilities, argmax; equal weights fixed before any run (`docs/FUSION.md`).

## Pose transformer (exploratory; `scripts/revision/pose_transformer.py`, 7465bfc)

Our own implementation, following SPOTER. Settings fixed once when the script was written (no validation split, no alternatives tried; there is no further record of how they were chosen): d_model 128, 3 encoder layers (pre-norm), 4 heads, feed-forward 512, dropout 0.1, learned positional embedding and class token; AdamW lr 5e-4, weight decay 0.05, batch 32, 150 epochs, `OneCycleLR` (10% warm-up, cosine), label smoothing 0.1, gradient clipping 1.0; augmentation: rotation U(−10°, 10°) and scaling U(0.9, 1.1) about the coordinate origin, Gaussian noise sd 0.02 (in image coordinates the rotation acts as a shear plus translation, audit K4). Final model kept. Robustness of these settings (sensitivity over 18 configurations and settings chosen on training signers only): REVISION_LOG §5.22.
