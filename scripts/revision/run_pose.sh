#!/bin/bash
# Pose-transformer baseline on the server CPU: body-relative and image-coordinate
# landmarks (24 frames), LOSO 5 signers x seeds 0-4 and 80/20 seeds 0-4, 8 runs in parallel.
#   scripts/revision/run_pose.sh PYTHON WORK OUTDIR
set -euo pipefail
PY="$1"; W="$2"; O="$3"
cd "$(dirname "$0")/../.."
git log --oneline -1 | tee "$O/commit.txt"
jobs=()
for name in bodynorm:$W/bodynorm/general_db_bodynorm.csv image:$W/general_db.csv; do
  tag=${name%%:*}; csv=${name#*:}
  for seed in 0 1 2 3 4; do
    for s in 0 1 2 3 4; do jobs+=("$csv $O/$tag --split loso --subject $s --seed $seed"); done
    jobs+=("$csv $O/$tag --split 8020 --seed $seed")
  done
done
printf '%s\n' "${jobs[@]}" | xargs -P 8 -L 1 bash -c 'nice -n 5 '"$PY"' scripts/revision/pose_transformer.py --input-csv "$0" --output-dir "$1" "${@:2}" --threads 3 2>&1 | grep -v -i warn'
echo done > "$O/DONE"
