# Permutation importance for the pose-sequence models (protocol fixed 2026-10-23, before any run)

Requested by the user on 2026-10-23 ("Do it"), after asking in which other models feature importance can be measured. Extends REVISION_LOG §5.14 (grouped permutation importance for TSFEL + RF, R2.6) to the two pose-sequence models with complete results: our pose transformer (our implementation, exploratory) and the official ST-GCN. Not planned: official SPOTER (optional, only if it is kept in the paper; decided after its runs), ViViT and SlowFast (new-signer F1 ≈ 0.2, so importances would be near zero, as in the near-chance folds of §5.14), attention maps (not a measure of importance).

## Method

- **Same procedure as §5.14**, applied to sequences (our implementation, `scripts/revision/sequence_importance.py`; Breiman 2001, Fisher et al. 2019): on the held-out signer, the whole sequence of a group's x and y coordinates (all frames) is permuted jointly across the test executions, one execution permutation per repeat shared by every column of the group; the trained model predicts again; importance = drop in weighted F1, mean over **10 repeats**. Generator seeded with the run seed.
- **Groups**, as in §5.14: region (left hand, right hand, body; 42 / 42 / 46 columns) and single point (65 points). Missing points stay 0 in the permuted execution, as in the input.
- **Models and runs**: no weights were saved by the earlier runs, so each model is retrained with exactly its reported configuration and the importance is computed at the end of the same run. Input: body-relative coordinates (main landmark pipeline, as the RF importance). LOSO 5 signers × seeds 0–4 per model (25 runs each).
  - Pose transformer: default configuration (`pose_transformer.py` defaults), CPU, 3 threads. CPU training is deterministic (regression test, REVISION_LOG §2 ce1ceac), so the retrained runs must reproduce the stored runs `docs/results/pose/bodynorm/` exactly; checked per run (baseline F1 vs. stored F1), and any mismatch is reported.
  - ST-GCN: the revised recipe with the learning rate already selected for body-relative input (0.05; §5.21), GPU. GPU training is not bit-reproducible, so baseline F1 is compared with `docs/results/stgcn_v2/bodynorm/` and the differences are reported. Starts only after the SlowFast v2 queue has finished (no two GPU queues of ours at once, §7.14).
- The training part of both scripts is unchanged; `--importance-repeats` (default 0 = off) only adds the computation after the final model is scored.

## Statistics (descriptive; no tests)

- Per signer: importance averaged over seeds. Per group: mean over the 5 signers with a 95% t-interval (df 4), and every signer's value.
- Stability: Spearman ρ of group importances between every pair of folds, over all 5 folds and over the folds with baseline F1 ≥ 0.2 (as §5.14 / audit M12).
- Reported next to the RF importances (§5.14) and the retraining ablations of the pose transformer (A5 hands only, A6 body only; §5.22): permutation measures what the trained model uses, the ablations measure what information suffices.
- Outputs: per-run JSON (with predictions and the importance rows) and `*_runs.csv`, `*_per_signer.csv`, `*_summary.csv`, `*_stability.csv` in `docs/results/importance_sequence/`.

## Amendment 2026-10-26 (before any run): finger-level groups

Requested by the user on 2026-10-26 ("Just the finger-level groups is fine"), after the region and single-point results (§5.24): single points are too fine to be informative (pose transformer: the 65 point drops sum to 0.31 against 0.42 for the left hand alone, point stability ρ 0.41; ST-GCN: point drops ≈ 0, sum slightly negative), because neighbouring points carry the same information. A shape-vs-movement split was offered and not chosen.

- **New grouping `subregion`, 17 groups** (MediaPipe numbering, left/right as MediaPipe labels them): per hand (LH and RH) wrist (0), thumb (1–4), index (5–8), middle (9–12), ring (13–16), little finger (17–20); body face (0–10), left arm (11, 13, 15), right arm (12, 14, 16), left pose-hand points (17, 19, 21), right pose-hand points (18, 20, 22). The groups cover all 130 columns once. The body's pose-hand points are split by side (17 groups, not the 16 first proposed to the user).
- Same method, models, inputs, seeds, 10 repeats and statistics as above. Both models are retrained again (no weights saved); groupings evaluated in the order **region, subregion** (single points not repeated).
- Checks: the pose transformer runs must again reproduce the stored runs exactly, and because the random generator is consumed in the same order, their region importances must equal the 2026-10-23 values exactly. ST-GCN (GPU) is not reproducible: baseline F1 and region importances are compared with the 2026-10-24 runs and the differences reported.
- Runs at the same time: pose transformer on the server CPU, ST-GCN on the 4 GPUs (the only GPU queue of ours). Outputs `docs/results/importance_sequence/{pose,stgcn}_subregion/`.

## Amendment 2026-10-26, second (before any run): official SPOTER

Requested by the user on 2026-10-26 ("let's continue with the fusion and feature importance"), because SPOTER now goes in the main text. Computed in the SPOTER retraining for the fusion (`docs/FUSION.md`), so no extra training.

- **Region level only** (left hand, right hand, body), the level reported in the main text; LOSO 5 signers × **seeds 0–2** (the fusion seeds; the pose transformer and ST-GCN used 0–4), 10 repeats, same statistics.
- **Same permutation**, applied to our landmark table before SPOTER's input conversion: SPOTER reads image coordinates of native length, so a donor execution's group sequence is linearly resampled over its full duration to the recipient's length (the pose transformer and ST-GCN inputs were already all 24 frames). Columns: the 21 + 21 hand points and the 11 pose points SPOTER reads (nose, eyes, ears, shoulders, elbows, wrists; 22 columns); SPOTER's neck is the shoulder midpoint, so it follows the body group.
- Reported next to RF and ST-GCN (main text) and the pose transformer (Supporting Information).
