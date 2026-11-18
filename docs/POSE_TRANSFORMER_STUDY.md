# Pose transformer: robustness study (protocol fixed 2026-10-22, before any run)

Our pose-sequence transformer (`scripts/revision/pose_transformer.py`, our implementation following SPOTER; REVISION_LOG §5.16, §7.9) is the strongest model on a new signer (0.57 image coordinates / 0.54 body-relative; better than TSFEL + RF for 5/5 signers, Holm p ≈ 0.04, §5.17). Its settings were fixed once without a validation split and there is no record of how they were chosen (audit M8). This study anticipates the reviewers' questions about it. Everything below was decided before any of these runs; nothing is chosen on test signers. Requested by the user on 2026-10-22.

**Default configuration** (the one already reported): d_model 128, 3 layers, 4 heads, feed-forward 512, dropout 0.1, class token, AdamW lr 5e-4, weight decay 0.05, batch 32, 150 epochs, OneCycle (10% warm-up, cosine), label smoothing 0.1, gradient clipping 1.0, augmentation (rotation ±10°, scaling 0.9–1.1 about the coordinate origin, noise sd 0.02), 24 frames. Main input for this study: **body-relative coordinates** (the main landmark pipeline); image coordinates where stated.

## Anticipated questions and the study that answers each

| Question | Study |
|----------|-------|
| Q1. Were the hyperparameters tuned on the test signers? | S1 nested selection |
| Q2. Is the reported score a lucky configuration? | S2 sensitivity (descriptive) |
| Q3. Is the comparison with ST-GCN fair, given that ST-GCN uses its published recipe without augmentation or label smoothing? Which components matter? | S3 ablations |
| Q4. What input information does it use? | S3 hands-only / body-only inputs |
| Q5. Does it depend on the 24-frame resampling? | S4 frame count |
| Q6. With 5 signers, how much does the number of training signers matter? | S5 learning curve |
| Q7. Is the augmentation implemented correctly? (audit K4: in image coordinates it acts as a shear) | S3 rotation about the body centre |
| Q8. How variable is it across seeds, and is the difference to other models real? | S6 statistics |

## S1. Nested hyperparameter selection (Q1)

- Grid (18 configurations): d_model ∈ {64, 128, 256} × layers ∈ {2, 3, 4} × learning rate ∈ {5e-4, 1e-3}; heads 4, feed-forward 4 × d_model, everything else as the default. The default is one grid point (128, 3, 5e-4).
- For each outer fold (held-out signer s): inner leave-one-signer-out over the 4 training signers (train on 3, validate on the 4th; 4 inner folds), seed 0. The test signer is never loaded into training or evaluation.
- Selection rule: highest mean inner-validation weighted F1 over the 4 inner folds; ties (within 0.005) go to the smaller model (fewer parameters), then the lower learning rate.
- Final: the selected configuration of each outer fold retrained on all 4 training signers, seeds 0–4, scored once on the held-out signer. Headline of the study: the mean over the 5 signers of these nested results, with its t-interval.
- 18 × 4 × 5 = 360 inner runs + 25 final runs.

## S2. Sensitivity (Q2; descriptive only)

All 18 configurations trained on the 4 training signers and scored on the held-out signer, seed 0 (90 runs). Reported as the distribution of new-signer F1 across configurations (min, median, max per signer and overall). **Not used for any choice**; labelled as a sensitivity analysis.

## S3. Ablations (Q3, Q4, Q7)

Default configuration, body-relative, LOSO 5 signers × seeds 0–4 (25 runs each), one component changed at a time:

| Ablation | Change |
|----------|--------|
| A1 no augmentation | augmentation off |
| A2 no label smoothing | label smoothing 0 |
| A3 plain recipe | no augmentation, no label smoothing, constant learning rate (no warm-up, no decay) — the closest analogue to ST-GCN's published recipe |
| A4 mean pooling | average of the frame tokens instead of the class token |
| A5 hands only | input = the 42 hand landmarks (84 coordinates) |
| A6 body only | input = the 23 pose landmarks (46 coordinates) |
| A7 image coordinates, rotation about the body centre | image-coordinate input; augmentation rotated and scaled about each execution's shoulder midpoint in pixel units (corrects the shear of the default in image coordinates, audit K4); compare with the existing image-coordinate runs |

## S4. Frame count (Q5)

Default configuration, body-relative, resampled to 16, 32 and 48 frames (same normalization, `normalize_landmarks.py` on the 16/32/48-frame tables of §5.5), LOSO × seeds 0–4 (75 runs); 24 frames = the default runs.

## S5. Learning curve over training signers (Q6)

Default configuration, body-relative, seed 0: for each held-out signer, train on every subset of k ∈ {1, 2, 3} of the other 4 signers (4 + 6 + 4 subsets) and score on the held-out signer (70 runs); k = 4 = the default runs. Reported as mean new-signer F1 against k (mean over subsets, then over held-out signers).

## S6. Statistics

- Every result: weighted F1 per held-out signer (seeds averaged), mean over the 5 signers, 95% t-interval (df 4), SD over seeds, training accuracy at the end of training.
- Paired per-signer comparisons against the default configuration, within each family (S1 nested vs. default; the 7 ablations; the 3 frame counts), Holm-adjusted within the family; exact sign-flip p reported alongside (floor 0.0625). Comparisons are interpreted as effect sizes with intervals, not as rankings.
- Shuffled-label control: already done for the default (§5.16, at chance).
- Everything stored per run (JSON with predictions, per-epoch loss, configuration), summarized with the committed scripts (`json_runs_summary.py`, `signer_ci.py`), copied to `docs/results/pose_study/`.

## S7. Official SPOTER (added 2026-10-22, user decision: "Yes, do the spoter one as well")

Official SPOTER (Boháček & Hrúz, WACV Workshops 2022; github.com/matyasbohacek/spoter) with its published code and training recipe, vendored unmodified with licence and commit like ST-GCN, as an external reference point for "pose transformers" (R2.7) and for our implementation. Only the data glue is ours (mapping our MediaPipe landmarks to SPOTER's input format). Same LOSO folds and 80/20 splits, seeds 0–4, shuffled-label control, signer-level statistics and a paired comparison with our default configuration. Details, fixed 2026-10-22 after reading the code (repository commit `0f909bf`, 2023-05-13; Apache 2.0) and before any run:

- **Code used unmodified:** `spoter/spoter_model.py` (model), `spoter/utils.py` (`train_epoch`), `spoter/gaussian_noise.py`, `datasets/czech_slr_dataset.py` (loading, augmentations, normalization), `augmentations/`, `normalization/`. Vendored as `third_party/spoter/` with its licence. Not used: the repository's `train.py`, because after training it **scores every saved checkpoint on the test set and reports the best one** (the same test-set selection as the original ViViT, P13); our runner trains with the same components and keeps the final model, scored once.
- **Recipe (repository defaults):** hidden dimension 108 (= 54 joints × 2), 9 heads, 6 encoder + 6 decoder layers, class query; SGD, learning rate 0.001, no momentum; cross-entropy; batch size 1; 100 epochs; Gaussian noise (sd 0.001) on training inputs; the authors' augmentations (each with probability 0.5: rotation ±13°, perspective shear, squeeze, arm-joint rotation) and their body and hand normalization. As in `train.py`, the ReduceLROnPlateau scheduler is created but never stepped, so the learning rate stays constant.
- **Input mapping (our glue):** native-length sequences in image coordinates (MediaPipe x, y in [0, 1]; `WORK/frames/general_db_f0.csv`, 997 executions), since SPOTER takes sequences of any length and applies its own normalization. Joints: nose = pose 0, leftEye = 2, rightEye = 5, leftEar = 7, rightEar = 8, leftShoulder = 11, rightShoulder = 12, leftElbow = 13, rightElbow = 14, leftWrist = 15, rightWrist = 16; hands: MediaPipe left hand → `_0`, right hand → `_1`, joints wrist = 0, thumbCMC = 1, thumbMP = 2, thumbIP = 3, thumbTip = 4, index MCP/PIP/DIP/Tip = 5–8, middle 9–12, ring 13–16, little 17–20. MediaPipe has no neck; SPOTER's loader sets a missing neck to 0 (its normalization uses the neck only when a shoulder is missing). Labels written 1-based (the loader subtracts 1).
- **Amendment 2026-10-23 (before any completed run; only a 1-epoch smoke test had been attempted, and it crashed):** the neck sentence above is wrong. (1) SPOTER's fallback for a missing neck writes an integer 0, which its own loader cannot parse (`ast.literal_eval` on an int: "malformed node or string: 0"); the authors' data always had a neck. (2) The neck is not used only when a shoulder is missing: the body normalization centres its signing-space box horizontally on `neck_X` (`normalize_single_dict`, starting point `neck_X − 3 × shoulder distance`), and the arm-joint augmentation rotates the shoulder–elbow–wrist chain about the neck, so a zero neck would put the box at x = 0 and rotate arms about the frame corner. (3) The box extends downwards from the eyes by 6 shoulder widths assuming y increases upwards (Apple Vision convention, origin lower left, which SPOTER's data used); MediaPipe's y increases downwards (our data: nose y ≈ 0.36, shoulders ≈ 0.48, wrists ≈ 0.62), so the box would cover the space above the head. **Changes, in our glue only (official code still unmodified):** neck = midpoint of MediaPipe shoulders 11 and 12 (Vision's neck joint is that point), and y → 1 − y for every joint (x unchanged). The input has no missing values (0 NaN, 0 zeros, checked; the glue asserts it, since SPOTER reads 0 as missing). Everything else as above.
- **Environment:** separate (`~/lsc-revision/venv-spoter`), following the repository's `requirements.txt` where possible (Python 3.9, torch 1.8.1 CPU, pandas 1.1.5, opencv-python-headless, scikit-learn), because newer PyTorch passes arguments that SPOTER's decoder layer does not accept, and the ViViT environment must not be changed.
- **Runs:** LOSO 5 signers × seeds 0–4, 80/20 seeds 0–4 (the same splits as every other model), shuffled-label controls (LOSO 5 + 80/20, seed 0): 36 runs on the server CPU. Per run: metrics, predictions, per-epoch training loss and accuracy, final training accuracy without augmentation. Statistics as S6, including a paired comparison with our default configuration (image coordinates) and with TSFEL + RF.
