#!/bin/bash
# ViViT reruns on several GPUs, one job per GPU (P13, P14; R1.1, R2.5).
# Builds the full clip table once, then each GPU worker takes the next unclaimed
# job from a shared queue: per seed, 5 held-out-signer folds and one 80/20 split.
# Effective batch matches the original 4-GPU runs (logs: 16.75 steps per epoch on
# 800 clips): LOSO 1 x 48 accumulation = 48, 80/20 1 x 32 = 32. fp32, since fp16 is
# ~6.6x slower per clip on these Pascal GPUs (fp32 at batch 3 does not fit in 12 GB).
# Jobs whose results.json exists are skipped, so the script can be restarted
# (remove stale claims/ entries of jobs that were interrupted).
#
#   scripts/revision/run_vivit_gpus.sh PYTHON REPO WORKDIR VIDEO_DIR "GPUS" SEEDS...
#   e.g. scripts/revision/run_vivit_gpus.sh venv/bin/python lsc50-analysis vivit data/VIDEOS/COLOR_BODY "0 1 2 3" 0 1 2
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"; VIDEOS="$4"; GPUS=($5); shift 5
SEEDS=("${@:-0}")
mkdir -p "$W/claims" "$W/logs"; cd "$W"
LOG="$W/run_vivit.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
nvidia-smi --query-gpu=index,name,memory.total,driver_version --format=csv | tee -a "$LOG"
"$PY" -c "import torch, transformers; print('torch', torch.__version__, 'cuda', torch.version.cuda, 'transformers', transformers.__version__)" | tee -a "$LOG"
(cd "$REPO" && git log --oneline -1) | tee -a "$LOG"
# Fetch the backbone once so the workers do not race to download it.
"$PY" -c "from transformers import VivitForVideoClassification as M, VivitImageProcessor as P; M.from_pretrained('google/vivit-b-16x2-kinetics400'); P.from_pretrained('google/vivit-b-16x2-kinetics400')" >> "$LOG" 2>&1
if [ ! -d clips_all ]; then
  say "building clips_all from $VIDEOS"
  "$PY" "$REPO/videos/scripts/build_dataset_all.py" --video-dir "$VIDEOS" --output clips_all >> "$LOG" 2>&1
  say "clips_all built"
fi
JOBS=()
for SEED in "${SEEDS[@]}"; do
  for S in 0 1 2 3 4; do JOBS+=("loso:$S:$SEED"); done
  JOBS+=("8020:-:$SEED")
done
worker() {
  local GPU="$1" job kind S SEED out
  for job in "${JOBS[@]}"; do
    IFS=: read -r kind S SEED <<< "$job"
    if [ "$kind" = loso ]; then out="vivit-s$S-seed$SEED"; else out="vivit-8020-seed$SEED"; fi
    [ -f "$out/results.json" ] && continue
    mkdir "claims/$out" 2>/dev/null || continue
    say "GPU $GPU start $out"
    if [ "$kind" = loso ]; then
      CUDA_VISIBLE_DEVICES=$GPU "$PY" "$REPO/videos/scripts/train_cv.py" --dataset clips_all --subject "$S" --seed "$SEED" \
        --batch-size 1 --gradient-accumulation-steps 48 --precision fp32 --logging-dir "logs/$out" > "logs/$out.log" 2>&1 || say "GPU $GPU FAILED $out"
    else
      CUDA_VISIBLE_DEVICES=$GPU "$PY" "$REPO/videos/scripts/train.py" --dataset clips_all --seed "$SEED" \
        --batch-size 1 --gradient-accumulation-steps 32 --precision fp32 --logging-dir "logs/$out" > "logs/$out.log" 2>&1 || say "GPU $GPU FAILED $out"
    fi
    say "GPU $GPU end $out"
  done
}
for G in "${GPUS[@]}"; do worker "$G" & sleep 30; done
wait
"$PY" "$REPO/scripts/revision/vivit_summary.py" vivit-*/results.json --output-csv vivit_summary.csv | tee -a "$LOG" || true
say "done"
