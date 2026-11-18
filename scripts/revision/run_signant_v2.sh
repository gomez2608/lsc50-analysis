#!/bin/bash
# Native vs. interpreter, completed (audit M4, K3): body-relative landmark TSFEL (new), and seeds 1-4
# for the image-coordinate landmark TSFEL / Chronos and IMU runs (seed 0 exists, run_signant.sh);
# all with the corrected mapping (deaf = volunteers 3-5), SVM/RF/KNN grids, stratified inner CV as before.
# Then the 10-grouping permutation check on body-relative TSFEL for RF, SVM and KNN (fixed settings),
# and the summary tables (signant_summary.py). Server CPU.
#   scripts/revision/run_signant_v2.sh PYTHON WORK
set -euo pipefail
PY="$1"; W="$2"
cd "$(dirname "$0")/../.."
O="$W/results"; LOG="$O/signant_v2.log"
git log --oneline -1 > "$O/signant_v2.commit"
run() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; nice -n 10 "$@" >> "$LOG" 2>&1; }
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/bodynorm/temporal_features_bodynorm.csv" --output-dir "$O/signant_bodynorm" --seeds 0 1 2 3 4 --parts signant signant_new_schema signant_loso
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/temporal_features.csv" "$W/general_db_lm_chronos.csv" --output-dir "$O/signant_landmarks" --seeds 1 2 3 4 --parts signant signant_new_schema signant_loso
run "$PY" imu/scripts/grid_search.py --features-csv "$W/temporal.csv" "$W/general_db_imu_chronos.csv" --output-dir "$O/signant_imu" --seeds 1 2 3 4 --include-signant
for m in rf svm knn; do
  run "$PY" scripts/revision/signant_labeling_permutation.py --features-csv "$W/bodynorm/temporal_features_bodynorm.csv" --model $m --output-csv "$O/signant_labeling_permutation_bodynorm_$m.csv"
done
run "$PY" scripts/revision/signant_summary.py \
  --pkl "Landmarks TSFEL body-relative=$O/signant_bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed?.pkl" \
  --pkl "Landmarks TSFEL image coordinates=$O/signant_landmarks/grid_search_results_temporal_features_chronos_seed?.pkl" \
  --pkl "Landmarks Chronos=$O/signant_landmarks/grid_search_results_general_db_lm_chronos_chronos_seed?.pkl" \
  --pkl "IMU TSFEL=$O/signant_imu/grid_search_results_temporal_seed?.pkl" \
  --pkl "IMU Chronos=$O/signant_imu/grid_search_results_general_db_imu_chronos_seed?.pkl" \
  --output-prefix "$O/signant_summary"
echo "[$(date '+%F %H:%M')] signant v2 done" | tee -a "$LOG"
