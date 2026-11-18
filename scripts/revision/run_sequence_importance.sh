#!/bin/bash
# Permutation importance for the pose-sequence models (docs/SEQUENCE_IMPORTANCE.md, fixed before any run).
# pose:  pose transformer, default configuration, body-relative, LOSO 5 x seeds 0-4, server CPU,
#        one run at a time x 3 threads, nice. Both modes then compare each run with the stored run.
# stgcn: ST-GCN revised recipe, body-relative, lr from selected_lr_bodynorm.txt, LOSO 5 x seeds 0-4;
#        waits for "slowfast v2 done" in SLOWFAST_LOG (one GPU queue of ours at a time, REVISION_LOG §7.14),
#        then the 4 GPUs, each used only with >= MIN_FREE_MIB free and none of our processes.
# GROUPINGS (default "region point") selects the groupings; 2026-10-26 run: GROUPINGS="region subregion".
#   scripts/revision/run_sequence_importance.sh pose  PYTHON WORK OUTDIR
#   scripts/revision/run_sequence_importance.sh stgcn PYTHON WORK OUTDIR SELECTED_LR_FILE SLOWFAST_LOG
set -euo pipefail
MODE="$1"; PY="$2"; W="$3"; O="$4"
cd "$(dirname "$0")/../.."
mkdir -p "$O/runs" "$O/logs"
git log --oneline -1 > "$O/commit.txt"
LOG="$O/run.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
BODY="$W/bodynorm/general_db_bodynorm.csv"
REPEATS=10
GROUPINGS=${GROUPINGS:-region point}

if [ "$MODE" = pose ]; then
  say "pose transformer importance ($GROUPINGS): 25 runs, one at a time, $(cat "$O/commit.txt")"
  for seed in 0 1 2 3 4; do for s in 0 1 2 3 4; do
    n="pose-loso-s$s-seed$seed"
    [ -f "$O/runs/$n.json" ] && continue
    nice -n 10 "$PY" scripts/revision/pose_transformer.py --input-csv "$BODY" --output-dir "$O/runs" \
      --split loso --subject "$s" --seed "$seed" --threads 3 --importance-repeats "$REPEATS" --importance-groupings $GROUPINGS > "$O/logs/$n.log" 2>&1 \
      && say "done $n" || say "FAILED $n"
  done; done
  REF=docs/results/pose/bodynorm
elif [ "$MODE" = stgcn ]; then
  LR=$(cat "$5"); SFLOG="$6"; MIN_FREE_MIB=${MIN_FREE_MIB:-9000}
  say "ST-GCN importance: waiting for SlowFast v2 to finish ($SFLOG)"
  until grep -q "slowfast v2 done" "$SFLOG"; do sleep 300; done
  say "ST-GCN importance ($GROUPINGS): 25 runs, lr $LR, $(cat "$O/commit.txt")"
  gpu_usable() {
    local free uuid ours
    free=$(nvidia-smi -i "$1" --query-gpu=memory.free --format=csv,noheader,nounits)
    uuid=$(nvidia-smi -i "$1" --query-gpu=uuid --format=csv,noheader)
    ours=$(nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader | awk -F', ' -v u="$uuid" '$1 == u {print $2}' \
           | xargs -r ps -o user= -p 2>/dev/null | grep -c "^$USER$" || true)
    [ "$free" -ge "$MIN_FREE_MIB" ] && [ "${ours:-0}" -eq 0 ]
  }
  mkdir -p "$O/claims"
  worker() {
    local G="$1" s seed n
    for seed in 0 1 2 3 4; do for s in 0 1 2 3 4; do
      n="stgcn-loso-s$s-seed$seed"
      if [ -f "$O/runs/$n.json" ] || [ -d "$O/claims/$n" ]; then continue; fi
      until gpu_usable "$G"; do sleep 120; done
      mkdir "$O/claims/$n" 2>/dev/null || continue
      say "GPU $G start $n"
      CUDA_VISIBLE_DEVICES=$G nice -n 5 "$PY" scripts/revision/stgcn_baseline.py --input-csv "$BODY" --output-dir "$O/runs" \
        --split loso --subject "$s" --seed "$seed" --base-lr "$LR" --epochs 200 --step 25 125 --warmup-epochs 5 \
        --batch-size 16 --device cuda --threads 2 --importance-repeats "$REPEATS" --importance-groupings $GROUPINGS > "$O/logs/$n.log" 2>&1 || say "GPU $G FAILED $n"
      say "GPU $G end $n"
      sleep 20
    done; done
  }
  for G in ${GPUS:-2 3}; do worker "$G" & sleep 30; done
  wait
  REF=docs/results/stgcn_v2/bodynorm
else
  echo "mode: pose | stgcn" >&2; exit 1
fi

"$PY" - "$O/runs" "$REF" <<'EOF' | tee -a "$LOG"
import glob, json, os, sys
runs, ref = sys.argv[1:]
for f in sorted(glob.glob(f"{runs}/*.json")):
    r, s = json.load(open(f)), json.load(open(os.path.join(ref, os.path.basename(f))))
    same = r["y_pred"] == s["y_pred"]
    print(f"{os.path.basename(f)[:-5]}: F1 {r['f1_weighted']:.6f}, stored {s['f1_weighted']:.6f}, "
          f"predictions {'identical' if same else 'differ'}")
EOF
"$PY" scripts/revision/sequence_importance.py summarize --runs-dir "$O/runs" --output-prefix "$O/importance_$MODE" | tee -a "$LOG"
say "$MODE importance done"
touch "$O/DONE_$MODE"
