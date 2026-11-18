#!/bin/bash
# Shuffled-label control for fine-tuned ViViT, protocol B, seed 0, all 5 held-out signers (audit N1).
# Waits until the SlowFast queue has finished, then runs through run_vivit_queue.sh (kind BS)
# from the CPU code copy (which has train_cv.py --shuffle-labels); ~10 GPU-hours per job.
#   scripts/revision/run_vivit_control.sh PYTHON REPO VIVIT_WORKDIR SLOWFAST_LOG
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"; SLOG="$4"
until grep -q "slowfast queue done" "$SLOG" 2>/dev/null; do sleep 300; done
bash "$REPO/scripts/revision/run_vivit_queue.sh" "$PY" "$REPO" "$W" "0 1 2 3" BS:0:0 BS:1:0 BS:2:0 BS:3:0 BS:4:0
