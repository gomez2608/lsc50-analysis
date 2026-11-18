#!/bin/bash
# ViViT job queue over several GPUs, for jobs added while others are running.
# Each GPU worker waits until its GPU is idle (memory use below 1 GB), then takes
# the next job that has no results.json, has not been started (no logs/<job>.log,
# so jobs of an earlier launcher are left alone) and is not claimed in claims2/.
# Job specs, in order:
#   A:S:SEED   held-out signer S, protocol A (train on 3 signers, pick the epoch on the 4th)
#   B:S:SEED   held-out signer S, protocol B (train on all 4 signers for 30 epochs, keep the final model)
#   8020:-:SEED  80/20 split (epoch picked on 10% of training rows)
#   BS:S:SEED  protocol B with shuffled training labels (control; needs train_cv.py --shuffle-labels)
# Effective batch as the original (LOSO 48, 80/20 32), fp32 (see run_vivit_gpus.sh).
#
#   scripts/revision/run_vivit_queue.sh PYTHON REPO WORKDIR "GPUS" JOB...
#   e.g. ... venv/bin/python lsc50-analysis vivit "0 1 2 3" B:0:0 B:1:0 A:2:1 8020:-:1
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"; GPUS=($4); shift 4
JOBS=("$@")
mkdir -p "$W/claims2" "$W/logs"; cd "$W"
LOG="$W/run_vivit.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
say "queue $(cd "$REPO" && git log --oneline -1): ${JOBS[*]}"
# A GPU is usable when at least MIN_FREE_MIB is free and none of *our* processes is on it, so
# small jobs of other users do not block the queue (2026-10-21: another user's ~1.5 GB jobs on
# GPUs 1-3; REVISION_LOG §7.11). ViViT needs ~7.4 GB.
MIN_FREE_MIB=${MIN_FREE_MIB:-9000}
gpu_idle() {
  local free uuid ours
  free=$(nvidia-smi -i "$1" --query-gpu=memory.free --format=csv,noheader,nounits)
  uuid=$(nvidia-smi -i "$1" --query-gpu=uuid --format=csv,noheader)
  ours=$(nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader | awk -F', ' -v u="$uuid" '$1 == u {print $2}' \
         | xargs -r ps -o user= -p 2>/dev/null | grep -c "^$USER$" || true)
  [ "$free" -ge "$MIN_FREE_MIB" ] && [ "${ours:-0}" -eq 0 ]
}
worker() {
  local GPU="$1" job kind S SEED out
  for job in "${JOBS[@]}"; do
    IFS=: read -r kind S SEED <<< "$job"
    case "$kind" in
      A) out="vivit-s$S-seed$SEED" ;;
      B) out="vivit-B-s$S-seed$SEED" ;;
      8020) out="vivit-8020-seed$SEED" ;;
      BS) out="vivit-B-s$S-seed$SEED-shuffled" ;;
    esac
    [ -f "$out/results.json" ] && continue
    [ -f "logs/$out.log" ] && continue
    [ -d "claims2/$out" ] && continue
    until gpu_idle "$GPU"; do sleep 120; done
    mkdir "claims2/$out" 2>/dev/null || continue
    say "GPU $GPU start $out"
    case "$kind" in
      A) args=(train_cv.py --subject "$S" --val-mode signer --batch-size 1 --gradient-accumulation-steps 48) ;;
      B) args=(train_cv.py --subject "$S" --val-mode none --output-dir "$out" --batch-size 1 --gradient-accumulation-steps 48) ;;
      8020) args=(train.py --batch-size 1 --gradient-accumulation-steps 32) ;;
      BS) args=(train_cv.py --subject "$S" --val-mode none --output-dir "$out" --batch-size 1 --gradient-accumulation-steps 48 --shuffle-labels) ;;
    esac
    CUDA_VISIBLE_DEVICES=$GPU "$PY" "$REPO/videos/scripts/${args[0]}" --dataset clips_all --seed "$SEED" --precision fp32 \
      "${args[@]:1}" --logging-dir "logs/$out" > "logs/$out.log" 2>&1 || say "GPU $GPU FAILED $out"
    say "GPU $GPU end $out"
    sleep 20
  done
}
for G in "${GPUS[@]}"; do worker "$G" & sleep 45; done
wait
"$PY" "$REPO/scripts/revision/vivit_summary.py" vivit-*/results.json --output-csv vivit_summary.csv | tee -a "$LOG" || true
say "queue done"
