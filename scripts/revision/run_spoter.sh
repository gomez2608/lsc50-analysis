#!/bin/bash
# Official SPOTER (POSE_TRANSFORMER_STUDY.md, S7) on the server CPU: LOSO 5 signers x seeds 0-4, 80/20 seeds 0-4,
# shuffled-label controls (LOSO 5 + 80/20, seed 0) = 36 runs, P in parallel, 3 threads each. DRY_RUN=1 lists jobs.
#   scripts/revision/run_spoter.sh SPOTER_PYTHON INPUT_CSV OUTDIR [P]
set -euo pipefail
PY="$1"; CSV="$2"; O="$3"; P="${4:-6}"
DRY_RUN=${DRY_RUN:-0}
cd "$(dirname "$0")/../.."
mkdir -p "$O"; git log --oneline -1 > "$O/commit.txt"
J="$O/jobs.txt"; : > "$J"
for seed in 0 1 2 3 4; do
  for s in 0 1 2 3 4; do echo "--split loso --subject $s --seed $seed" >> "$J"; done
  echo "--split 8020 --seed $seed" >> "$J"
done
for s in 0 1 2 3 4; do echo "--split loso --subject $s --seed 0 --shuffle-labels" >> "$J"; done
echo "--split 8020 --seed 0 --shuffle-labels" >> "$J"
echo "[$(date '+%F %H:%M')] $(wc -l < "$J") runs" | tee -a "$O/run.log"
if [ "$DRY_RUN" = 1 ]; then cat "$J"; exit 0; fi
xargs -P "$P" -L 1 bash -c 'nice -n 10 '"$PY"' scripts/revision/spoter_baseline.py --input-csv '"$CSV"' --output-dir '"$O"' "$@" --threads 3 >> '"$O"'/run.log 2>&1 || echo "FAILED $*" >> '"$O"'/run.log' _ < "$J"
echo "[$(date '+%F %H:%M')] spoter done" | tee -a "$O/run.log"
echo done > "$O/DONE"
