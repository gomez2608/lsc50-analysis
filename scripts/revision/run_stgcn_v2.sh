#!/bin/bash
# ST-GCN with the revised recipe (audit M3; fixed 2026-10-20 before any run):
# batch 16, 200 epochs, lr x0.1 at epochs 25 and 125, 5-epoch warm-up, on the GPUs
# (shared with the ViViT queue; ST-GCN needs < 1 GB).
# Phase 1, selection: for each input and each base lr in {0.05, 0.025, 0.01}, the 5 LOSO
#   folds with the test signer dropped and the next signer ((s + 1) mod 5) as validation.
#   Rule fixed in advance: the lr with the highest mean validation weighted F1 wins (per input).
# Phase 2, final: the chosen lr; LOSO 5 x seeds 0-4, 80/20 seeds 0-4, shuffled-label
#   controls (LOSO 5 + 80/20, seed 0); final model scored once on the test signer.
#   scripts/revision/run_stgcn_v2.sh PYTHON WORK OUTDIR
set -euo pipefail
PY="$1"; W="$2"; O="$3"
cd "$(dirname "$0")/../.."
mkdir -p "$O/claims" "$O/logs"
git log --oneline -1 | tee "$O/commit.txt"
LOG="$O/run.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
COMMON=(--epochs 200 --step 25 125 --warmup-epochs 5 --batch-size 16 --device cuda --threads 2)
declare -A CSV=([image]="$W/general_db.csv" [bodynorm]="$W/bodynorm/general_db_bodynorm.csv")

run_jobs() {  # each line: name|outdir|args...
  local list="$1"
  worker() {
    local G="$1" line name out args
    while IFS= read -r line; do
      IFS='|' read -r name out args <<< "$line"
      [ -f "$out/$name.json" ] && continue
      # claim per output folder + name: the same run name exists for both inputs
      mkdir "$O/claims/$(basename "$out")__$name" 2>/dev/null || continue
      say "GPU $G start $name"
      # shellcheck disable=SC2086
      CUDA_VISIBLE_DEVICES=$G nice -n 5 "$PY" scripts/revision/stgcn_baseline.py --output-dir "$out" $args "${COMMON[@]}" \
        > "$O/logs/$name.log" 2>&1 || say "GPU $G FAILED $name"
      say "GPU $G end $name"
    done < "$list"
  }
  for G in ${GPUS:-2 3}; do worker "$G" & sleep 5; done
  wait
}

# Phase 1: selection on a training signer
SEL="$O/selection_jobs.txt"; : > "$SEL"
for tag in image bodynorm; do
  for lr in 0.05 0.025 0.01; do
    for s in 0 1 2 3 4; do
      v=$(( (s + 1) % 5 ))
      echo "stgcn-loso-s$s-seed0-val$v-lr$lr|$O/selection/$tag|--input-csv ${CSV[$tag]} --split loso --subject $s --val-subject $v --seed 0 --base-lr $lr --tag lr$lr" >> "$SEL"
    done
  done
done
say "phase 1: selection ($(wc -l < "$SEL") runs)"
run_jobs "$SEL"
"$PY" - "$O" <<'EOF' | tee -a "$LOG"
import glob, json, sys, collections
O = sys.argv[1]
for tag in ("image", "bodynorm"):
    scores = collections.defaultdict(list)
    for f in glob.glob(f"{O}/selection/{tag}/*.json"):
        r = json.load(open(f))
        scores[r["config"]["base_lr"]].append(r["f1_weighted"])
    assert all(len(v) == 5 for v in scores.values()) and len(scores) == 3, f"incomplete selection for {tag}"
    means = {lr: sum(v) / 5 for lr, v in scores.items()}
    best = max(means, key=means.get)
    print(f"selection {tag}: " + ", ".join(f"lr {lr}: val F1 {m:.3f}" for lr, m in sorted(means.items())) + f" -> lr {best}")
    open(f"{O}/selected_lr_{tag}.txt", "w").write(f"{best}\n")
EOF

# Phase 2: final runs with the selected lr
FIN="$O/final_jobs.txt"; : > "$FIN"
for tag in image bodynorm; do
  lr=$(cat "$O/selected_lr_$tag.txt")
  for seed in 0 1 2 3 4; do
    for s in 0 1 2 3 4; do echo "stgcn-loso-s$s-seed$seed|$O/$tag|--input-csv ${CSV[$tag]} --split loso --subject $s --seed $seed --base-lr $lr" >> "$FIN"; done
    echo "stgcn-8020-seed$seed|$O/$tag|--input-csv ${CSV[$tag]} --split 8020 --seed $seed --base-lr $lr" >> "$FIN"
  done
  for s in 0 1 2 3 4; do echo "stgcn-loso-s$s-seed0-shuffled|$O/${tag}_control|--input-csv ${CSV[$tag]} --split loso --subject $s --seed 0 --base-lr $lr --shuffle-labels" >> "$FIN"; done
  echo "stgcn-8020-seed0-shuffled|$O/${tag}_control|--input-csv ${CSV[$tag]} --split 8020 --seed 0 --base-lr $lr --shuffle-labels" >> "$FIN"
done
say "phase 2: final ($(wc -l < "$FIN") runs)"
run_jobs "$FIN"
say "stgcn v2 done"
echo done > "$O/DONE"
