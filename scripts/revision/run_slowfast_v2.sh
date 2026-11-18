#!/bin/bash
# SlowFast R50 with the revised recipe (REVISION_LOG §5.20; fixed 2026-10-23 before any revised run): the first
# recipe (run_slowfast.sh) left 8 of 18 runs untrained (NaN or loss ln 50). Same model, input, 30 epochs, batch
# 4 x 12, SGD momentum 0.9, wd 1e-4, frozen BatchNorm statistics; added a 3-epoch linear warm-up before the cosine
# decay, and the learning rate chosen on a training signer, as for ST-GCN (run_stgcn_v2.sh):
# Phase 1, selection: base lr in {0.01, 0.003, 0.001}, the 5 LOSO folds with the test signer dropped and the next
#   signer ((s + 1) mod 5) as validation, seed 0. Rule fixed in advance: the lr with the highest mean validation
#   weighted F1 wins; within 0.005, the lower lr.
# Phase 2, final: the chosen lr; LOSO 5 x seeds 0-2, 80/20 seeds 0-2, shuffled-label controls (LOSO s0 and 80/20,
#   seed 0), as in the first recipe; final model scored once. Runs whose loss becomes non-finite stop and are
#   flagged "diverged"; they are reported, not rerun or dropped.
# A worker starts a job only when its GPU has >= MIN_FREE_MIB free and none of our processes (run_slowfast.sh).
# DRY_RUN=1 prints the phase-1 jobs.
#   scripts/revision/run_slowfast_v2.sh PY REPO CLIPS OUTDIR
set -euo pipefail
PY="$1"; REPO="$2"; CLIPS="$3"; O="$4"
MIN_FREE_MIB=${MIN_FREE_MIB:-9000}
DRY_RUN=${DRY_RUN:-0}
mkdir -p "$O/claims" "$O/logs"
(cd "$REPO" && git log --oneline -1) > "$O/commit.txt"
LOG="$O/run.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
S="$REPO/scripts/revision/slowfast_baseline.py"
COMMON=(--clips "$CLIPS" --epochs 30 --batch-size 4 --accumulation 12 --bn frozen --warmup-epochs 3 --stop-on-nan --train-accuracy)

gpu_usable() {
  local free uuid ours
  free=$(nvidia-smi -i "$1" --query-gpu=memory.free --format=csv,noheader,nounits)
  uuid=$(nvidia-smi -i "$1" --query-gpu=uuid --format=csv,noheader)
  ours=$(nvidia-smi --query-compute-apps=gpu_uuid,pid --format=csv,noheader | awk -F', ' -v u="$uuid" '$1 == u {print $2}' \
         | xargs -r ps -o user= -p 2>/dev/null | grep -c "^$USER$" || true)
  [ "$free" -ge "$MIN_FREE_MIB" ] && [ "${ours:-0}" -eq 0 ]
}

run_jobs() {  # each line: name|outdir|args...
  local list="$1"
  worker() {
    local G="$1" line name out args
    while IFS= read -r line; do
      IFS='|' read -r name out args <<< "$line"
      if [ -f "$out/$name.json" ] || [ -d "$O/claims/$(basename "$out")__$name" ]; then continue; fi
      until gpu_usable "$G"; do sleep 120; done
      mkdir "$O/claims/$(basename "$out")__$name" 2>/dev/null || continue
      say "GPU $G start $name"
      # shellcheck disable=SC2086
      CUDA_VISIBLE_DEVICES=$G "$PY" "$S" train --output-dir "$out" $args "${COMMON[@]}" > "$O/logs/$name.log" 2>&1 \
        || say "GPU $G FAILED $name"
      say "GPU $G end $name"
      sleep 20
    done < "$list"
  }
  for G in ${GPUS:-2 3}; do worker "$G" & sleep 30; done
  wait
}

# Phase 1: selection on a training signer
SEL="$O/selection_jobs.txt"; : > "$SEL"
for lr in 0.01 0.003 0.001; do
  for s in 0 1 2 3 4; do
    v=$(( (s + 1) % 5 ))
    echo "slowfast-loso-s$s-seed0-val$v-lr$lr|$O/selection|--split loso --subject $s --val-subject $v --seed 0 --lr $lr --tag lr$lr" >> "$SEL"
  done
done
if [ "$DRY_RUN" = 1 ]; then cat "$SEL"; exit 0; fi
say "phase 1: selection ($(wc -l < "$SEL") runs), $(cat "$O/commit.txt")"
run_jobs "$SEL"
"$PY" - "$O" <<'EOF' | tee -a "$LOG"
import collections, glob, json, sys
O = sys.argv[1]
scores, div = collections.defaultdict(list), collections.Counter()
for f in glob.glob(f"{O}/selection/*.json"):
    r = json.load(open(f))
    scores[r["config"]["lr"]].append(r["f1_weighted"])
    div[r["config"]["lr"]] += bool(r["diverged"])
means = {lr: sum(v) / len(v) for lr, v in scores.items()}
for lr in sorted(means, reverse=True):
    print(f"lr {lr}: mean validation F1 {means[lr]:.3f} over {len(scores[lr])} folds, diverged {div[lr]}")
assert all(len(v) == 5 for v in scores.values()) and len(scores) == 3, "selection incomplete"
best = max(means.values())
chosen = min(lr for lr, m in means.items() if m >= best - 0.005)
print(f"selected lr {chosen}")
open(f"{O}/selected_lr.txt", "w").write(f"{chosen}\n")
EOF
LR=$(cat "$O/selected_lr.txt")

# Phase 2: final runs with the selected lr
FIN="$O/final_jobs.txt"; : > "$FIN"
for seed in 0 1 2; do
  for s in 0 1 2 3 4; do echo "slowfast-loso-s$s-seed$seed|$O/results|--split loso --subject $s --seed $seed --lr $LR" >> "$FIN"; done
  echo "slowfast-8020-seed$seed|$O/results|--split 8020 --seed $seed --lr $LR" >> "$FIN"
done
echo "slowfast-loso-s0-seed0-shuffled|$O/results|--split loso --subject 0 --seed 0 --lr $LR --shuffle-labels" >> "$FIN"
echo "slowfast-8020-seed0-shuffled|$O/results|--split 8020 --seed 0 --lr $LR --shuffle-labels" >> "$FIN"
say "phase 2: final ($(wc -l < "$FIN") runs, lr $LR)"
run_jobs "$FIN"
say "slowfast v2 done"
