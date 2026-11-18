# Results summary (status 2026-10-26)

Headline numbers of the revision, one place. **Nothing running (2026-10-27).** Pose + video late fusion finished (§5.25); the SlowFast row now uses the fusion retraining (as fixed in `FUSION.md`); SPOTER reproduced exactly. Final signer intervals and paired comparisons for every model: §5.17 (2026-10-27). Each line points to the full entry in `REVISION_LOG.md` (§) and its result file in `docs/results/`. Weighted F1 unless stated; chance ≈ 0.02 for the 50-sign task. LOSO = leave one signer out, mean ± SD over held-out signers (and seeds where stated). 80/20 = **seen signer, seen repetitions** (stratified by sign only; every test execution has another repetition of the same sign by the same signer in training). Signer-level 95% intervals for every LOSO model: §5.17 and `docs/results/signer_ci.csv`; the **t-interval over the 5 signers is primary** (the 5-cluster bootstrap under-covers): e.g. TSFEL + RF body-relative 0.29 [0.07, 0.51], ViViT B seeds 0–1 0.22 [0.15, 0.29]. Compare models by paired per-signer differences, not by interval overlap. Draft figures: `docs/figures/` (§5.18).

## Sign recognition (50 signs)

| Features + model | 80/20 (5 seeds) | LOSO | Paper 80/20 / LOSO | § |
|------------------|-----------------|------|--------------------|---|
| Landmarks, body-relative, TSFEL + RF | **0.68 ± 0.03** | **0.29 ± 0.16** (25 runs) | — | 5.9 |
| Landmarks, body-relative, TSFEL + SVM | 0.65 ± 0.04 | 0.26 ± 0.15 | — | 5.9 |
| Landmarks, body-relative, TSFEL + KNN | 0.62 ± 0.05 | 0.22 ± 0.09 | — | 5.9 |
| Landmarks, image coordinates, TSFEL + RF | 0.62 ± 0.02 | 0.25 ± 0.14 | 0.57 / 0.24 | 5.3, 5.7 |
| Landmarks, image coordinates, TSFEL + SVM | 0.59 ± 0.03 | 0.23 ± 0.15 | 0.55 / 0.19 | 5.3, 5.7 |
| Landmarks, image coordinates, TSFEL + KNN | 0.55 ± 0.03 | 0.16 ± 0.06 | 0.46 / 0.17 | 5.3, 5.7 |
| Landmarks, Chronos + SVM | 0.57 ± 0.02 | 0.23 ± 0.10 | **1.0** (leakage, P1) / 0.06 | 5.3, 5.7 |
| Landmarks, Chronos + RF | 0.44 ± 0.03 | 0.20 ± 0.08 | 1.0 / 0.06 | 5.3, 5.7 |
| Landmarks, Chronos + KNN | 0.47 ± 0.05 | 0.19 ± 0.08 | 1.0 / 0.05 | 5.3, 5.7 |
| IMU, TSFEL + RF | 0.10 ± 0.03\* | 0.18 ± 0.10 | 0.22 / **0.34** (duplicated volunteer, H1) | 5.4, 5.7, 6.1 |
| IMU, TSFEL + SVM / KNN | 0.05 / 0.03\* | 0.15 / 0.11 | 0.03 / 0.11, 0.03 / 0.09 | 5.4, 5.7 |
| IMU, Chronos (all models) | ≤ 0.05\* | ≤ 0.06 | ≤ 0.03 / ≤ 0.05 | 5.4, 5.7 |
| ViViT fine-tuned, 80/20 runs (epoch chosen on 10% of training rows; seeds 0, 1, 2) | 0.58 ± 0.07 (0.63, 0.51, 0.61) | — | **1.0** (test = train copies, P3) | 5.11, 5.15 |
| ViViT fine-tuned, LOSO protocol A (epoch chosen on a training signer; seeds 0, 1, 2) | — | 0.12 ± 0.02 (0.09, 0.13, 0.13) | 0.31 (test-selected checkpoint, P13) | 5.11, 5.15 |
| ViViT fine-tuned, LOSO protocol B (fixed 30 epochs, final model; seeds 0, 1, 2) | — | **0.22 ± 0.02** (0.21, 0.24, 0.20) | | 5.15 |
| ViViT frozen + linear probe (CLS) | 0.61 ± 0.03 | 0.07 ± 0.04 | — | 5.10 |
| ViViT frozen CLS + SVM / RF / KNN | 0.56 / 0.47 / 0.49 | 0.07 / 0.05 / 0.04 (seed 0) | — | 5.12 |
| ST-GCN (official code), revised recipe, image coordinates (lr 0.025, chosen on a training signer) | 0.63 ± 0.05 | 0.26 ± 0.12 | — | 5.21 |
| ST-GCN (official code), revised recipe, body-relative (lr 0.05) | 0.69 ± 0.02 | **0.32 ± 0.13** | — | 5.21 |
| ~~ST-GCN, NTU recipe ported by epochs~~ | ~~0.25 ± 0.16~~ | ~~0.12~~ | — | 5.19: did not train (4 of 30 runs never fit); **not to be quoted** |
| SlowFast R50 (official code, BatchNorm statistics frozen), revised recipe (warm-up, lr 0.003 chosen on a training signer; seeds 0–2) | 0.89 ± 0.02 | **0.57 ± 0.08** (per signer 0.46, 0.55, 0.54, 0.62, 0.66; fusion retraining; stored runs 0.57); t-interval [0.47, 0.66] | — | 5.25 (5.20 to write); `docs/results/fusion/slowfast/` |
| ~~SlowFast R50, first recipe~~ | — | — | — | 5.20: 8 of 18 runs never trained; **not to be quoted** |
| Official SPOTER (pose transformer; seeds 0–4; image coordinates with the input glue of protocol S7) | 0.90 ± 0.02 | 0.49 ± 0.21 (0.27, 0.26, 0.57, 0.62, 0.71); t-interval [0.23, 0.75]; seeds 0–2 retrained identically | — | 5.23 (to write), 5.25; `docs/results/spoter/` |
| **Late fusion SlowFast + SPOTER** (mean of class probabilities, untuned; seeds 0–2) | **0.92 ± 0.01** | **0.62 ± 0.14** (0.44, 0.50, 0.66, 0.70, 0.79); t-interval [0.44, 0.80] | — | 5.25; `docs/results/fusion/` |
| *Exploratory:* pose transformer (our implementation, following SPOTER), image coordinates | 0.94 ± 0.01 | 0.57 ± 0.21 | — | 5.16 |
| *Exploratory:* pose transformer, body-relative | 0.94 ± 0.02 | 0.54 ± 0.19 | — | 5.16 |

\*IMU has one recording per sign and signer, so its 80/20 split never sees the test signer on the test sign: not comparable with the landmark 80/20.

Planned paired comparisons (§5.17, final run 2026-10-27, **13 comparisons, Holm**): official SPOTER (+0.20), SlowFast (+0.28) and the exploratory pose transformer (+0.28 image / +0.25 body-relative) beat TSFEL + RF body-relative for 5/5 signers; unadjusted p 0.004–0.009, Holm p 0.046 (SPOTER), 0.052 / 0.063 (pose transformer), 0.085 (SlowFast); exact sign-flip 0.0625, its minimum. With the earlier 9-comparison family the pose transformer had Holm 0.039 / 0.046: where the 0.05 line falls depends on the family size, so report the four together. Fusion vs. SPOTER +0.13 (5/5, Holm 0.20), vs. SlowFast +0.06 (3/5, Holm 1.0). ST-GCN, ViViT B, frozen ViViT, TSFEL image coordinates, Chronos SVM, IMU RF vs. TSFEL + RF: Holm 0.64–1.0. The middle of the ranking cannot be separated with 5 signers.

Controls: shuffled training labels → chance (≤ 0.03) for landmark TSFEL (image and body-relative), landmark Chronos, IMU, frozen ViViT grids and linear probe (§5.2 and addendum), the pose transformer (§5.16) and ST-GCN with both recipes (§5.19, §5.21), ViViT protocol B (5 folds, 0.004–0.031; §5.15), SlowFast revised recipe (0.009 / 0.020) and SPOTER (0.003–0.027). Frame count 16–48 changes LOSO by ≤ 0.05 (TSFEL ≤ 0.02); native length without resampling is worse (§5.5).

## Native (deaf) vs. interpreter (binary), corrected labels (§5.8; exploratory)

| Split | Result |
|-------|--------|
| Rows 80/20, 10 signs held out | 0.67–1.00 (TSFEL 0.90–1.00); solvable by recognizing the signer |
| One signer held out, landmarks TSFEL + RF (image coordinates, seed 0) | balanced accuracy **0.93**; true grouping ranks 1st of 10 possible groupings: **p = 0.1, the minimum attainable, not significant**; chosen among 6 combinations |
| One signer held out, other landmark models | 0.46–0.68 |
| One signer held out, IMU | 0.06–0.21; the true grouping scores 0.04 (systematically inverted) and "Volunteers 2, 3, 4 deaf" 0.90. Same volunteers and order as video (confirmed 2026-10-20), so IMU separates Volunteers 1 and 5 from 2–4 by something other than hearing status (session or sensor setup; asked to the authors) |
| One signer held out, body-relative landmarks TSFEL, seeds 0–4 | RF **0.84 ± 0.04** (Volunteer 2 at 0.50), SVM 0.69, KNN 0.61; image-coordinate RF 0.93 ± 0.02 over seeds 0–4 |
| Permutation check, body-relative, RF / SVM / KNN | true grouping ranks 1st of 10 for all three (0.87 / 0.60 / 0.63); p = 0.1 each, not significant |

## Signer variability (§5.13) and feature importance (§5.14)

- DTW between executions of the same sign: between-signer 2.8× within-signer, 50/50 signs (p = 1.8e-15, descriptive: signs are not independent replicates). **At signer level** all 5 signers are farther from the others than from their own repetitions (ratio 1.88–3.93; paired t p = 0.0002; exact sign-flip 0.0625, its minimum); **without Volunteer 1** 50/50 signs and 4/4 signers. Deaf signers form a tight cluster; the two interpreters differ from everyone; Volunteer 1 is the most distant and the least consistent. Per sign: the deaf cluster holds in 50/50 signs; Volunteer 1 is the most distant signer in 39 signs and the least consistent in 48 (ratio range 1.55–5.23). Same results when normalized by the actual warping-path length (median ratio 2.69 vs. 2.76). Caveat: one recording session per signer (session and signer confounded).
- Permutation importance for the pose-sequence models (§5.24): pose transformer left-labelled hand 0.42 > right 0.22 ≈ body 0.21; ST-GCN left 0.23 > right 0.16 > body 0.08 (same order for every signer). Finger level: pose transformer led by the left-labelled thumb (0.21; ρ 0.86), ST-GCN finger groups ≤ 0.03. The left-labelled hand is the dominant hand for 4/5 signers (not Volunteer 2); our pipeline flips nothing (checked on the videos).
- Permutation importance (TSFEL + RF) on the held-out signer: hands > body in every fold (right and left hand swap order in 3 folds; stable, ρ 0.70); amount-of-movement TSFEL features dominate (ρ 0.53); single landmarks unstable (ρ 0.03; two folds near chance pull ρ down). IMU: shoulder flexion, arm rotation and adduction > elbow > wrist (ρ 0.31).
