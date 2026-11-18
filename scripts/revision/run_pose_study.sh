#!/bin/bash
# Pose transformer robustness study (docs/POSE_TRANSFORMER_STUDY.md, protocol fixed in 77128f3).
# Phase 1 (one shared queue): S1 inner folds (360), S2 sensitivity (90), S3 ablations (175),
# S4 frame count (75), S5 learning curve (70). Phase 2: nested selection, then S1 final (25).
# Server CPU, P runs in parallel, 3 threads each, nice. DRY_RUN=1 prints the job list.
#   scripts/revision/run_pose_study.sh PYTHON WORK OUTDIR [P]
set -euo pipefail
PY="$1"; W="$2"; O="$3"; P="${4:-8}"
DRY_RUN=${DRY_RUN:-0}
cd "$(dirname "$0")/../.."
mkdir -p "$O"
git log --oneline -1 > "$O/commit.txt"
LOG="$O/run.log"
say() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; }
BODY="$W/bodynorm/general_db_bodynorm.csv"; IMAGE="$W/general_db.csv"
J="$O/jobs_phase1.txt"; : > "$J"
add() { echo "$*" >> "$J"; }   # line: OUTDIR NAME ARGS...

# S1 inner folds and S2 sensitivity: 18 configurations
for d in 64 128 256; do for L in 2 3 4; do for lr in 5e-4 1e-3; do
  cfg="d$d-L$L-lr$lr"
  for s in 0 1 2 3 4; do
    others=(); for t in 0 1 2 3 4; do if [ "$t" != "$s" ]; then others+=("$t"); fi; done
    for v in "${others[@]}"; do
      tr=(); for t in "${others[@]}"; do if [ "$t" != "$v" ]; then tr+=("$t"); fi; done
      add "$O/inner $cfg-out$s-val$v --input-csv $BODY --split subjects --train-subjects ${tr[*]} --eval-subject $v --exclude-subject $s --seed 0 --d-model $d --layers $L --lr $lr"
    done
    add "$O/sensitivity $cfg-s$s --input-csv $BODY --split loso --subject $s --seed 0 --d-model $d --layers $L --lr $lr"
  done
done; done; done
# S3 ablations
declare -A ABL=(
  [A1_no_augmentation]="--input-csv $BODY --no-augment"
  [A2_no_label_smoothing]="--input-csv $BODY --label-smoothing 0"
  [A3_plain_recipe]="--input-csv $BODY --no-augment --label-smoothing 0 --schedule constant"
  [A4_mean_pooling]="--input-csv $BODY --pooling mean"
  [A5_hands_only]="--input-csv $BODY --channels hands"
  [A6_body_only]="--input-csv $BODY --channels body"
  [A7_image_rotation_about_shoulders]="--input-csv $IMAGE --aug-centre shoulders --frame-size 1920 1080"
)
for a in "${!ABL[@]}"; do for seed in 0 1 2 3 4; do for s in 0 1 2 3 4; do
  add "$O/ablation/$a pose-loso-s$s-seed$seed ${ABL[$a]} --split loso --subject $s --seed $seed"
done; done; done
# S4 frame count
for n in 16 32 48; do for seed in 0 1 2 3 4; do for s in 0 1 2 3 4; do
  add "$O/frames/f$n pose-loso-s$s-seed$seed --input-csv $W/bodynorm/general_db_f${n}_bodynorm.csv --split loso --subject $s --seed $seed"
done; done; done
# S5 learning curve: every subset of k = 1, 2, 3 of the 4 training signers, seed 0
for s in 0 1 2 3 4; do
  others=(); for t in 0 1 2 3 4; do if [ "$t" != "$s" ]; then others+=("$t"); fi; done
  "$PY" - "${others[@]}" <<'PYEOF' | while read -r sub; do
import itertools, sys
o = sys.argv[1:]
for k in (1, 2, 3):
    for c in itertools.combinations(o, k):
        print(" ".join(c))
PYEOF
    k=$(wc -w <<< "$sub"); tag=$(tr -d ' ' <<< "$sub")
    add "$O/curve k$k-s$s-train$tag --input-csv $BODY --split subjects --train-subjects $sub --eval-subject $s --seed 0"
  done
done

say "phase 1: $(wc -l < "$J") runs ($P in parallel)"
if [ "$DRY_RUN" = 1 ]; then
  awk '{print $1}' "$J" | sed "s#$O/##" | sort | uniq -c
  head -3 "$J"; grep -m1 curve "$J"; grep -m1 A7 "$J"; exit 0
fi
run_list() {
  xargs -P "$P" -L 1 bash -c '
    out="$0"; name="$1"
    [ -f "$out/$name.json" ] && exit 0
    mkdir -p "$out"
    nice -n 10 '"$PY"' scripts/revision/pose_transformer.py --output-dir "$out" --name "$name" "${@:2}" --threads 3 \
      > /dev/null 2>> "'"$O"'/errors.log" || echo "[$(date "+%F %H:%M")] FAILED $out/$name" >> "'"$LOG"'"' < "$1"
}
run_list "$J"
say "phase 1 done; failures: $(grep -c FAILED "$LOG" || true)"

"$PY" scripts/revision/pose_nested_select.py --inner-dir "$O/inner" --output-csv "$O/nested_selection.csv" | tee -a "$LOG"
J2="$O/jobs_phase2.txt"; : > "$J2"
tail -n +2 "$O/nested_selection.csv" | while IFS=, read -r outer d L lr rest; do
  for seed in 0 1 2 3 4; do
    echo "$O/nested pose-loso-s$outer-seed$seed --input-csv $BODY --split loso --subject $outer --seed $seed --d-model $d --layers $L --lr $lr" >> "$J2"
  done
done
say "phase 2: $(wc -l < "$J2") nested final runs"
run_list "$J2"
say "pose study done; failures: $(grep -c FAILED "$LOG" || true)"
echo done > "$O/DONE"
