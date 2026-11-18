#!/bin/bash
# ViViT reruns for the revision (P13, P14; R1.1, R2.5). Needs a CUDA GPU.
# Builds the full clip table once, then trains held-out-signer folds and 80/20
# splits for each seed. Runs whose results.json already exists are skipped, so
# the script can be restarted after an interruption.
#
#   scripts/revision/run_vivit.sh PYTHON REPO WORKDIR VIDEO_DIR [SEEDS...]
#   e.g. scripts/revision/run_vivit.sh .venv/bin/python ~/lsc50-analysis ~/vivit ~/LSC50/VIDEOS/COLOR_BODY 0 1 2
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"; VIDEOS="$4"; shift 4
SEEDS=("${@:-0}")
mkdir -p "$W"; cd "$W"
LOG="$W/run_vivit.log"
run() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; "$@" >> "$LOG" 2>&1; }
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv | tee -a "$LOG"
"$PY" -c "import torch, transformers; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'transformers', transformers.__version__)" | tee -a "$LOG"
# 1. Full clip table (about 10 GB on disk).
[ -d clips_all ] || run "$PY" "$REPO/videos/scripts/build_dataset_all.py" --video-dir "$VIDEOS" --output clips_all
# 2. Held-out signer: 5 folds per seed (30 epochs, batch 3, lr 6e-5; checkpoint picked on one training signer).
for SEED in "${SEEDS[@]}"; do
  for S in 0 1 2 3 4; do
    [ -f "vivit-s$S-seed$SEED/results.json" ] || run "$PY" "$REPO/videos/scripts/train_cv.py" --dataset clips_all --subject "$S" --seed "$SEED"
  done
done
# 3. 80/20 per seed (13 epochs, batch 2, lr 5e-5; checkpoint picked on 10% of training rows).
for SEED in "${SEEDS[@]}"; do
  [ -f "vivit-8020-seed$SEED/results.json" ] || run "$PY" "$REPO/videos/scripts/train.py" --dataset clips_all --seed "$SEED"
done
"$PY" "$REPO/scripts/revision/vivit_summary.py" vivit-*/results.json | tee -a "$LOG"
echo "[$(date '+%F %H:%M')] done" | tee -a "$LOG"
