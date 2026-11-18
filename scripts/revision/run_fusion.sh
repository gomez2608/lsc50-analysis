#!/bin/bash
# Pose + video late fusion (docs/FUSION.md, fixed before any run): SlowFast and official SPOTER retrained with their
# reported recipes, saving test probabilities and weights; LOSO 5 x seeds 0-2, 80/20 seeds 0-2, shuffled-label
# controls (LOSO signer 0 and 80/20, seed 0) = 20 runs per model. SPOTER LOSO runs also compute region-level
# permutation importance (SEQUENCE_IMPORTANCE.md, amendment of 2026-10-26, second).
#   spoter:   server CPU, P in parallel x 3 threads, nice 10.
#   slowfast: GPUs in $GPUS (default "2 3": since 2026-10-26 we may use only GPUs 2 and 3), a GPU used only with >= MIN_FREE_MIB free and none of our processes (run_slowfast_v2.sh).
#   fuse:     waits for both, then fusion.py, comparison with the stored runs, summaries.
#   scripts/revision/run_fusion.sh spoter   SPOTER_PY  CSV   O [P]
#   scripts/revision/run_fusion.sh slowfast SLOWFAST_PY CLIPS O LR_FILE
#   scripts/revision/run_fusion.sh fuse     PY  O  STORED_SPOTER_DIR STORED_SLOWFAST_DIR
set -euo pipefail
MODE="$1"; PY="$2"
cd "$(dirname "$0")/../.."
REPO=$(pwd)
jobs() {  # name|args
  for seed in 0 1 2; do
    for s in 0 1 2 3 4; do echo "loso-s$s-seed$seed|--split loso --subject $s --seed $seed"; done
    echo "8020-seed$seed|--split 8020 --seed $seed"
  done
  echo "loso-s0-seed0-shuffled|--split loso --subject 0 --seed 0 --shuffle-labels"
  echo "8020-seed0-shuffled|--split 8020 --seed 0 --shuffle-labels"
}

if [ "$MODE" = spoter ]; then
  CSV="$3"; O="$4"; P="${5:-8}"
  mkdir -p "$O/spoter" "$O/logs"; git log --oneline -1 > "$O/commit_spoter.txt"
  LOG="$O/spoter.log"
  echo "[$(date '+%F %H:%M')] SPOTER: 20 runs, $P in parallel, $(cat "$O/commit_spoter.txt")" | tee -a "$LOG"
  jobs | while IFS='|' read -r name args; do
    extra="--save-probs --save-weights $O/weights"
    case "$name" in loso-*seed?) extra="$extra --importance-repeats 10";; esac
    echo "$name $args $extra"
  done > "$O/spoter_jobs.txt"
  xargs -P "$P" -L 1 bash -c 'n="$1"; shift; [ -f '"$O"'/spoter/spoter-$n.json ] && exit 0;
    nice -n 10 '"$PY"' scripts/revision/spoter_baseline.py --input-csv '"$CSV"' --output-dir '"$O"'/spoter "$@" --threads 3 \
      > '"$O"'/logs/spoter-$n.log 2>&1 && tail -1 '"$O"'/logs/spoter-$n.log >> '"$O"'/spoter.log || echo "FAILED spoter-$n" >> '"$O"'/spoter.log' _ \
    < "$O/spoter_jobs.txt"
  echo "[$(date '+%F %H:%M')] spoter fusion runs done" | tee -a "$LOG"
  touch "$O/DONE_spoter"

elif [ "$MODE" = slowfast ]; then
  CLIPS="$3"; O="$4"; LR=$(cat "$5"); MIN_FREE_MIB=${MIN_FREE_MIB:-9000}; GPUS=${GPUS:-2 3}
  mkdir -p "$O/slowfast" "$O/logs" "$O/claims"; git log --oneline -1 > "$O/commit_slowfast.txt"
  LOG="$O/slowfast.log"
  say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
  say "SlowFast: 20 runs, lr $LR, $(cat "$O/commit_slowfast.txt")"
  jobs > "$O/slowfast_jobs.txt"
  gpu_usable() {
    local free uuid ours
    free=$(nvidia-smi -i "$1" --query-gpu=memory.free --format=csv,noheader,nounits)
    uuid=$(nvidia-smi -i "$1" --query-gpu=uuid --format=csv,noheader)
    ours=$(nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader | awk -F', ' -v u="$uuid" '$1 == u {print $2}' \
           | xargs -r ps -o user= -p 2>/dev/null | grep -c "^$USER$" || true)
    [ "$free" -ge "$MIN_FREE_MIB" ] && [ "${ours:-0}" -eq 0 ]
  }
  worker() {
    local G="$1" name args
    while IFS='|' read -r name args; do
      if [ -f "$O/slowfast/slowfast-$name.json" ] || [ -d "$O/claims/$name" ]; then continue; fi
      until gpu_usable "$G"; do sleep 120; done
      mkdir "$O/claims/$name" 2>/dev/null || continue
      say "GPU $G start $name"
      # shellcheck disable=SC2086
      CUDA_VISIBLE_DEVICES=$G "$PY" scripts/revision/slowfast_baseline.py train --clips "$CLIPS" --output-dir "$O/slowfast" \
        $args --lr "$LR" --epochs 30 --batch-size 4 --accumulation 12 --bn frozen --warmup-epochs 3 --stop-on-nan \
        --train-accuracy --save-probs --save-weights "$O/weights" > "$O/logs/slowfast-$name.log" 2>&1 || say "GPU $G FAILED $name"
      say "GPU $G end $name: $(tail -1 "$O/logs/slowfast-$name.log")"
      sleep 20
    done < "$O/slowfast_jobs.txt"
  }
  for G in $GPUS; do worker "$G" & sleep 30; done
  wait
  say "slowfast fusion runs done"
  touch "$O/DONE_slowfast"

elif [ "$MODE" = fuse ]; then
  O="$3"; SP="$4"; SF="$5"
  until [ -f "$O/DONE_spoter" ] && [ -f "$O/DONE_slowfast" ]; do sleep 300; done
  LOG="$O/fuse.log"
  git log --oneline -1 > "$O/commit_fuse.txt"
  "$PY" scripts/revision/fusion.py --video-dir "$O/slowfast" --pose-dir "$O/spoter" --output-dir "$O/fused" | tee -a "$LOG"
  "$PY" - "$O" "$SP" "$SF" <<'PYEOF' | tee -a "$LOG"
import glob, json, os, sys
O, SP, SF = sys.argv[1:]
for model, new, old in (("spoter", f"{O}/spoter", SP), ("slowfast", f"{O}/slowfast", SF)):
    for f in sorted(glob.glob(f"{new}/{model}-*.json")):
        ref = os.path.join(old, os.path.basename(f))
        if not os.path.exists(ref):
            print(f"{os.path.basename(f)[:-5]}: no stored run"); continue
        r, s = json.load(open(f)), json.load(open(ref))
        print(f"{os.path.basename(f)[:-5]}: F1 {r['f1_weighted']:.4f}, stored {s['f1_weighted']:.4f}, "
              f"predictions {'identical' if r['y_pred'] == s['y_pred'] else 'differ'}")
PYEOF
  "$PY" scripts/revision/json_runs_summary.py --runs "SlowFast (fusion runs)=$O/slowfast/*.json" --runs "SPOTER (fusion runs)=$O/spoter/*.json" \
    --runs "Fusion SlowFast + SPOTER=$O/fused/*.json" --output-prefix "$O/fusion_runs" | tee -a "$LOG"
  "$PY" scripts/revision/sequence_importance.py summarize --runs-dir "$O/spoter" --output-prefix "$O/importance_spoter" | tee -a "$LOG"
  echo "[$(date '+%F %H:%M')] fusion done" | tee -a "$LOG"
  touch "$O/DONE_fuse"
else
  echo "mode: spoter | slowfast | fuse" >&2; exit 1
fi
