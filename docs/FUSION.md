# Pose + video late fusion (protocol fixed 2026-10-26, before any run)

Requested by the user on 2026-10-26 (R2.7 lists "multimodal fusion" among the modern baselines; "No, let's cover that as well, not as future work but now"). Decisions (user): fuse **SlowFast R50** (video) with **official SPOTER** (MediaPipe landmarks), **equal-weight average of the class probabilities**. A joint (early-fusion) network was not chosen: it would be a custom architecture, and with 4 training signers it would likely over-fit. IMU cannot be fused per execution (one IMU recording per sign and signer, four videos).

## Models and retraining

- No earlier run saved class probabilities, so both models are **retrained with their reported configurations** (SlowFast: revised recipe, lr 0.003 from `slowfast_v2/selected_lr.txt`, 30 epochs, batch 4 × 12, 3-epoch warm-up, frozen BatchNorm statistics; SPOTER: repository defaults with our input glue, 100 epochs, final model). Training code unchanged; new options only save the test-set softmax probabilities, the test execution keys (sign, signer, repetition) and the weights.
- Runs per model: LOSO 5 signers × seeds 0–2, 80/20 seeds 0–2, shuffled-label controls (LOSO signer 0 and 80/20, seed 0) = 20 runs, as in the SlowFast design. SlowFast on the GPUs (4 at launch; from 2026-10-26 19:24 UTC only GPUs 2 and 3, a server rule; shared with another user; a GPU is used only with ≥ 9 GB free and none of our processes), SPOTER on the CPU at the same time.
- Both models use the same 997 executions (the 3 duplicate executions removed) and the same 80/20 test sets (audit K6); checked again per run by comparing the test execution keys, which must be identical.

## Fusion rule

For each test execution: p_fusion = (p_SlowFast + p_SPOTER) / 2; prediction = argmax. No weight, no tuning, nothing chosen on any data. SlowFast seed k is paired with SPOTER seed k. The shuffled-label fusion control pairs the two shuffled-label runs (both trained on the same permutation of the training labels, which both scripts draw with the same generator and seed over the same training rows).

## Reporting

- Metrics as for every model (weighted F1 primary; accuracy, macro F1), per signer and seed; signer-level 95% t-interval.
- **Planned comparisons, added now to the paired per-signer list (Holm with the rest):** fusion vs. SlowFast, fusion vs. SPOTER.
- **Which single-model runs appear in the paper:** the retrained runs (same recipe, now with probabilities) replace the stored SlowFast and SPOTER runs in every table, whatever their result, so that fusion and its components come from the same models. The stored runs are kept, and the differences are reported (SlowFast is GPU-trained and not bit-reproducible; SPOTER on the CPU is expected to reproduce its stored seeds 0–2 exactly). SPOTER seeds 3–4 (stored) are reported as well, since the stored SPOTER has 5 seeds.
- Outputs: `docs/results/fusion/` (component runs with probabilities, fused runs, summary); weights stay on the server (`~/lsc-revision/WORK/fusion/weights/`).

## Permutation importance for SPOTER (same retraining; amendment to `SEQUENCE_IMPORTANCE.md`)

See the amendment of 2026-10-26 (second) in `SEQUENCE_IMPORTANCE.md`.
