#!/bin/bash
# SlowFast R50 baseline (official PyTorchVideo model + Kinetics-400 weights).
# 1. Build the clip table if missing (CPU). 2. Four GPU workers take jobs from a shared list
#    (claims via mkdir): LOSO 5 signers x seeds 0-2, 80/20 seeds 0-2, shuffled-label controls
#    (LOSO s0 and 80/20, seed 0). Each worker starts a job only when its GPU is usable: at least
#    MIN_FREE_MIB free and none of our processes on it (other users' small jobs do not block;
#    SlowFast needs ~7 GB, REVISION_LOG §7.11).
# Fixed 2026-10-22: the first version built job names with `$([ test ] && echo ...)`, which fails
# under `set -e` when the test is false, so every worker exited on its first job and no SlowFast
# run happened (REVISION_LOG §7.12). DRY_RUN=1 prints the jobs instead of running them.
#   scripts/revision/run_slowfast.sh PY REPO VIDEO_DIR WORKDIR
set -euo pipefail
PY="$1"; REPO="$2"; VIDEOS="$3"; W="$4"
MIN_FREE_MIB=${MIN_FREE_MIB:-9000}
DRY_RUN=${DRY_RUN:-0}
mkdir -p "$W/claims" "$W/logs" "$W/results"; cd "$W"
LOG="$W/run_slowfast.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
say "$(cd "$REPO" && git log --oneline -1)$([ "$DRY_RUN" = 1 ] && echo ' (dry run)' || true)"
S="$REPO/scripts/revision/slowfast_baseline.py"
if [ ! -f clips/meta.csv ]; then
  say "building clip table"; nice "$PY" "$S" build --video-dir "$VIDEOS" --output clips >> "$LOG" 2>&1; say "clip table built"
fi

gpu_usable() {
  local free uuid ours
  free=$(nvidia-smi -i "$1" --query-gpu=memory.free --format=csv,noheader,nounits)
  uuid=$(nvidia-smi -i "$1" --query-gpu=uuid --format=csv,noheader)
  ours=$(nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader | awk -F', ' -v u="$uuid" '$1 == u {print $2}' \
         | xargs -r ps -o user= -p 2>/dev/null | grep -c "^$USER$" || true)
  [ "$free" -ge "$MIN_FREE_MIB" ] && [ "${ours:-0}" -eq 0 ]
}

JOBS=()
for seed in 0 1 2; do
  for s in 0 1 2 3 4; do JOBS+=("loso:$s:$seed:"); done
  JOBS+=("8020:-:$seed:")
done
JOBS+=("loso:0:0:shuffled" "8020:-:0:shuffled")

worker() {
  local GPU="$1" job split s seed ctl name args
  for job in "${JOBS[@]}"; do
    IFS=: read -r split s seed ctl <<< "$job"
    name="slowfast-$split"
    if [ "$split" = loso ]; then name="$name-s$s"; fi
    name="$name-seed$seed"
    if [ -n "$ctl" ]; then name="$name-shuffled"; fi
    if [ -f "results/$name.json" ] || [ -d "claims/$name" ]; then continue; fi
    args=(train --clips clips --output-dir results --split "$split" --seed "$seed")
    if [ "$split" = loso ]; then args+=(--subject "$s"); fi
    if [ -n "$ctl" ]; then args+=(--shuffle-labels); fi
    if [ "$DRY_RUN" = 1 ]; then
      echo "GPU $GPU would run $name: ${args[*]}"
      continue
    fi
    until gpu_usable "$GPU"; do sleep 120; done
    mkdir "claims/$name" 2>/dev/null || continue
    say "GPU $GPU start $name"
    CUDA_VISIBLE_DEVICES=$GPU "$PY" "$S" "${args[@]}" > "logs/$name.log" 2>&1 || say "GPU $GPU FAILED $name"
    say "GPU $GPU end $name"
    sleep 20
  done
}
if [ "$DRY_RUN" = 1 ]; then worker 0; exit 0; fi
for G in ${GPUS:-2 3}; do worker "$G" & sleep 30; done
wait
say "slowfast queue done"
