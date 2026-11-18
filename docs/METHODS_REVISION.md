# Methods as implemented for the revision

What each analysis in the revised paper does, exactly as the code runs it, with the script and commit that implement it. This is the reference for rewriting the manuscript's Methods. Numbers referenced as §n are in `REVISION_LOG.md`; problems P1–P16 are listed in its §1; settings in `HYPERPARAMETERS.md`; files and checksums in `DATA_MANIFEST.md`. Status 2026-10-20 (updated after the external audit, `REVISION_LOG.md` §6.2).

## 1. Data

- **Source:** public LSC50 release, figshare article 27383016 (`IMU.zip`, `LANDMARKS.zip`, `VIDEOS.zip`; all three MD5s match figshare's). 50 signs, 5 volunteers, 4 repetitions each.
- **Signers:** Volunteers 1 and 2 are hearing interpreters, Volunteers 3–5 deaf native signers (confirmed by the authors, 2026-10-16; code subjects are 0-indexed, so deaf = subjects 2, 3, 4; `common/splits.py`, d7136e2).
- **Landmarks:** 1,000 executions in the release, of which 3 are byte-identical duplicates of another repetition (P7) and are dropped → **997 executions** (`landmarks/scripts/build_general_db.py`, af812db, c29d24f).
- **IMU:** one recording per (sign, volunteer); Volunteer 5's MUCHO segment is empty in `Timestamps.xlsx` → **249 recordings** (P10), segmented by the timestamps, 14 joint angles each: shoulder (arm) adduction, flexion and rotation; elbow flexion; forearm pronation/supination; wrist deviation and flexion; left and right (`imu/scripts/build_general_db.py`, af812db). Files are read in sorted order, so IMU subject *i* = Volunteer *i*+1 (the original read them in file-system order; §6.1 item 6).
- **Video:** `VIDEOS/COLOR_BODY`, 1,000 clips (all 1920 × 1080, 24 fps, checked 2026-10-20), 200 per signer. The 3 duplicate landmark executions (P7) are byte-identical `.avi` files too. ViViT and the linear probe used all 1,000 clips (at most 3 of 200 80/20 test clips can have an identical copy in training; LOSO is unaffected); SlowFast drops the 3 copies (997 clips).

## 2. Preprocessing

### 2.1 Landmarks
- 65 MediaPipe points per frame: 21 left hand, 21 right hand, 23 pose (indices 0–22: face, shoulders, elbows, wrists, hand points; hips and legs excluded); **x and y only** (z dropped) → 130 coordinates (P8).
- **Temporal length:** each execution is linearly resampled over its full duration to **24 frames** (the original truncated every sequence to its first frames, P5). Native lengths: 25–134 frames, median 62. Sensitivity (§5.5, `run_frames.sh`): the same pipeline rerun with 16, 32 and 48 resampled frames and at native length (TSFEL with fs = number of frames, 24 Hz at native length; Chronos on the raw series); seed 0 only, the same 80/20 split and the same 5 LOSO folds for every variant.
- **Body-relative coordinates (main pipeline from 2026-10-18):** per execution, coordinates in pixels (x × 1920, y × 1080) are centred on the mean shoulder midpoint (pose 11, 12) and divided by the mean shoulder width (`scripts/revision/normalize_landmarks.py`, d1a0955). This removes the signer's distance from the camera and position in the frame and keeps the movement. Effect: §5.9.

### 2.2 IMU
- Per recording, the 14 joint-angle time series between the sign's start and end timestamps. Sampling rate for TSFEL = samples / duration of the recording.
- **Segmentation:** no algorithm; each volunteer's continuous recording (~750–920 s, 120 Hz) is cut with the start/end times in the dataset's `INFO/Timestamps.xlsx`. Checked over all 250 segments: one execution per sign, the start is not cut, extra movement at the end is the return to rest (`scripts/revision/audit/imu_segmentation_check.py`; `REVISION_LOG.md` §3 item 5; C35).

### 2.3 Video
- 32 frames sampled uniformly over the clip, resized and centre-cropped to 224 × 224 with the ViViT image processor (`videos/src/dataset.py`). All 1,000 clips are processed once into one on-disk table with sign, signer and repetition columns (`videos/scripts/build_dataset_all.py`, b40d10a, e96d409); every split is drawn from it. No clip cap (P14).

## 3. Features

- **TSFEL temporal domain** (TSFEL 0.1.9, 14 features per channel: area under the curve, autocorrelation, centroid, mean / median / sum absolute diff, mean / median diff, negative / positive turning points, neighbourhood peaks, signal distance, slope, zero-crossing rate). Landmarks: 130 channels × 14 = **1,820 features**, fs = 24 (`landmarks/scripts/extract_tsfel.py`). IMU: 14 × 14 = **196 features**.
- **Chronos embeddings** (`amazon/chronos-t5-small`, chronos-forecasting 1.5.3, no fine-tuning): each channel of an execution is embedded as its own univariate series; encoder token embeddings are averaged over time (EOS token dropped), then over channels → 512 values per execution (`common/chronos_features.py`, 1211209). The original fed Chronos the frames as a batch (no temporal modelling, P2) and embedded all repetitions together (duplicated rows, P1).
- **Frozen ViViT features:** final-layer CLS token (768) or mean over all tokens of the pretrained, not fine-tuned ViViT (`videos/scripts/extract_vivit_features.py`, abf5e5b).

## 4. Models

- **SVM, Random Forest, KNN** (scikit-learn 1.5.2) on standardized features (scaler fitted on training rows only); exhaustive grid search, scoring weighted F1; refit on all training rows (`common/grid_search.py`). Grids and effective grid sizes: `HYPERPARAMETERS.md`.
- **ViViT** (`google/vivit-b-16x2-kinetics400`, all 88,954,000 parameters fine-tuned; §7.8): two LOSO protocols, A (train on 3 signers, choose the epoch on the 4th) and B (train on all 4 for 30 epochs, keep the final model), plus 80/20; fp32; effective batch as the original; settings in `HYPERPARAMETERS.md` (`videos/`, b40d10a → 0552f3a).
- **Linear probe:** standardized logistic regression on frozen ViViT features, C chosen by inner CV (`scripts/revision/linear_probe.py`, abf5e5b).
- **ST-GCN** (reviewer-named; official code vendored unmodified, `third_party/st_gcn`, commit 221c0e1, BSD-2): landmark sequences (2 × 24 frames × 65 nodes) on an LSC50 MediaPipe graph (hands, upper-body pose, wrists joined to the pose wrists), spatial partition, learnable edge importance. The NTU recipe ported by epochs did not train (§5.19); revised recipe with ~10,000 updates and the learning rate chosen on a held-out training signer (`run_stgcn_v2.sh`, 9c68806); final model kept; training accuracy recorded (`HYPERPARAMETERS.md`).
- **SlowFast R50** (reviewer-named; PyTorchVideo 0.1.5 `slowfast_r50`, Kinetics-400 weights): authors' Kinetics evaluation transform (32 frames, 256 × 256, α = 4), head replaced, all layers fine-tuned with BatchNorm statistics frozen, 30 epochs, final model; optimizer our choice (`scripts/revision/slowfast_baseline.py`, 58c07d3 → 9c0f6c7; `HYPERPARAMETERS.md`).
- **Pose transformer** (exploratory; our implementation, following SPOTER; not a reviewer-named model): transformer encoder on the landmark sequences, settings fixed once without a validation split (`scripts/revision/pose_transformer.py`, 7465bfc; `HYPERPARAMETERS.md`).

## 5. Evaluation protocols

- **80/20 (seen signer, seen repetitions):** executions split 80/20 **stratified by sign only**, one split per seed (seeds 0–4). Every signer appears on both sides, and every test execution has another repetition of the same sign by the same signer in training (audit M2). For IMU (one recording per sign and signer) the test signer is never seen on the test sign, so IMU 80/20 is not comparable with the landmark 80/20.
- **Leave-one-signer-out (LOSO), primary:** each of the 5 signers held out in turn; all 50 signs evaluated (the original dropped sign 42, P4).
- **Inner CV for hyperparameters:** in LOSO, one training signer per inner fold (`--inner-cv group`, 53ff121; P15); 80/20: stratified (4 folds landmarks, 3 IMU).
- **Seeds:** 0–4 for split and model seeds; LOSO folds are fixed, so only RF varies with the seed (§5.7).
- **Native vs. interpreter (binary):** rows 80/20, 10 signs held out, and one signer held out (`loso_interpreter_signant_split`). Inner CV stays stratified for this task (a signer-grouped inner fold can leave a single class).
- **Signer-level permutation check:** the signer-held-out binary task repeated for all 10 ways of labelling 3 of the 5 signers as deaf, fixed RF (`scripts/revision/signant_labeling_permutation.py`, 70658ae); smallest attainable p = 0.1.
- **Shuffled-label control:** training labels permuted (seeded), test labels intact; expect chance. Seed 0; for LOSO all 5 folds, for 80/20 one split (§5.2, §5.16, §5.19; `run_controls.sh`, `run_vivit_control.sh`).

## 6. Metrics and statistics

- Weighted F1 (headline), macro F1 and accuracy; chance ≈ 0.02 (50 balanced classes). For the signer-held-out binary task, each test fold holds one class, so pooled **balanced accuracy** is reported (chance 0.50).
- Mean ± SD (ddof 1 from 2026-10-20; earlier tables ddof 0) over seeds (80/20) or over held-out signers × seeds (LOSO); the headline LOSO value is the mean over the 5 per-signer means (seeds averaged within signer).
- 95% CI: for 80/20, percentile bootstrap (2,000 resamples) of the pooled test predictions (`common/summarize_results.py`, 7aa1602). For LOSO, a **two-level bootstrap**: resample the held-out signers, then each chosen signer's test items, F1 averaged over seeds and signers (2,000 replicates; `scripts/revision/signer_ci.py`, 75df458; §5.17); a t-interval over the 5 per-signer means (df 4) is reported alongside. **The t-interval is primary**: with 5 clusters the percentile bootstrap under-covers (half-width ≈ 0.6× the t-interval; audit M1). The pooled-item bootstrap is not used for LOSO (it treats the 25 pooled runs' items as independent and is ~√5 too narrow; audit K1).
- **Model comparisons:** paired per-signer differences of the seed-averaged F1 for a list of comparisons fixed in advance (`run_signer_ci.sh`: the main classical pipeline, landmark TSFEL body-relative + RF, against every other model family's main configuration): mean difference, number of signers where one model is better, paired t-interval and paired t-test (df 4), exact two-sided sign-flip test over all 2^5 sign patterns (smallest attainable p = 0.0625), Holm-adjusted p across the listed comparisons. Comparisons outside that list are descriptive. Interval overlap is not used to rank models.
- **What 5 signers allow:** minimum attainable p = 0.0625 (sign-flip, 5 signers), 0.125 (4 signers), 0.1 (the 10-grouping permutation); minimum detectable paired difference ≈ 1.66 × SD of the per-signer differences (paired t, df 4); no inference on gender (3 women, 2 men) or on interpreters as a group (2 interpreters) (C37).
- DTW: Wilcoxon signed-rank test (SciPy default, two-sided) over the 50 signs of between- vs. within-signer distance, reported as descriptive (signs are not independent replicates of signers); at signer level, paired t and exact sign-flip test over the 5 signers' within vs. mean-to-others cost, and the same without Volunteer 1 (`dtw_signer_level.py`; §5.13).
- Permutation importance: 10 permutations per group and fold; fold stability = Spearman ρ over fold pairs, over all folds and over folds with baseline F1 ≥ 0.2 (`importance_stability.py`; §5.14).

## 7. Additional analyses

- **Frame-count sensitivity** (R2.10): §5.5.
- **Grouped permutation importance on the held-out signer** (R2.6): RF refitted per fold with that fold's selected hyperparameters; F1 drop when a feature group is permuted jointly (10 repeats); groups = body point, region, TSFEL feature type (landmarks), joint angle, feature type (IMU); stability = Spearman ρ between folds (`scripts/revision/permutation_importance.py`, f8eb2b9; §5.14). Our implementation (scikit-learn's `permutation_importance` cannot permute groups): one row permutation of the held-out signer's rows applied to all columns of a group; cite Breiman 2001 and Fisher, Rudin & Dominici 2019 (C23).
- **Signer variability with DTW** (R2.9): multivariate DTW between all executions of a sign on native-length body-relative landmark sequences, distance / sqrt(n + m); within- vs. between-signer, signer × signer matrix, group comparisons (`scripts/revision/dtw_signer_variability.py`, dtaidistance 2.3.13; §5.13). One warping path for all coordinates, no window; sqrt(n + m) normalization as in Sakoe & Chiba 1978. Per-sign matrices from the same pairs (`dtw_per_sign.py`); robustness check normalizing by the actual path length gives the same results (`dtw_path_normalization_check.py`; C31); signer-level test and analysis without Volunteer 1 (`dtw_signer_level.py`). Within-signer pairs come from one recording session per signer, so session and signer are confounded.

## 8. Software and hardware

- Mac (until 2026-10-16): Python 3.11.9, scikit-learn 1.5.2, TSFEL 0.1.9, chronos-forecasting 1.5.3, torch 2.14.1 (MPS), transformers 4.57.6 (`docs/requirements-revision-lock.txt`).
- GPU server (from 2026-10-17): Ubuntu 22.04.5, 32 cores, 4 × NVIDIA TITAN X (Pascal) 12 GB, driver 535.288.01; Python 3.11.9, torch 2.6.0+cu118, transformers 4.57.6, datasets 3.1.0, scikit-learn 1.5.2, dtaidistance 2.3.13, matplotlib 3.9.2 (`docs/requirements-revision-lock-server.txt`, regenerated 2026-10-20). SlowFast: separate environment with torch 2.6.0+cu118, torchvision 0.21.0+cu118, pytorchvideo 0.1.5 (`docs/requirements-revision-lock-slowfast.txt`). §7.
