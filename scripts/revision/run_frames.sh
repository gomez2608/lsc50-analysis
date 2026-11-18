#!/bin/bash
# Frame-count sensitivity (R2.10) + extra IMU seeds. Data builds run immediately;
# grid searches wait until run_slr.sh has finished so they don't compete for CPU.
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"; DATA="$4"
cd "$REPO"
LOG="$W/results/errors_frames.log"
run() { echo "[$(date +%H:%M)] $*"; "$@" > /dev/null 2>>"$LOG"; }
# 1. Data: landmark tables at 16/32/48 frames and native length (0); TSFEL fs = N (24 for native, the video rate); Chronos.
for N in 16 32 48 0; do
  FS=$N; [ "$N" -eq 0 ] && FS=24
  run "$PY" landmarks/scripts/build_general_db.py --landmarks-dir "$DATA/LANDMARKS" --output-csv "$W/frames/general_db_f$N.csv" --n-frames $N
  run "$PY" landmarks/scripts/extract_tsfel.py --input-csv "$W/frames/general_db_f$N.csv" --output-csv "$W/frames/temporal_features_f$N.csv" --fs $FS
  run "$PY" -m common.chronos_features --input-csv "$W/frames/general_db_f$N.csv" --output-csv "$W/frames/general_db_lm_chronos_f$N.csv" --group-cols label subject rep
done
md5 "$W"/frames/*.csv
# 2. Wait for the SLR/shuffled/seed runs.
echo "[$(date +%H:%M)] waiting for run_slr.sh"
while pgrep -f "results/run_slr.sh" > /dev/null; do sleep 60; done
# 3. IMU 80/20 + LOSO, seeds 1-4 (RF seed variability vs. the paper's 0.34).
run "$PY" imu/scripts/grid_search.py --features-csv "$W/temporal.csv" "$W/general_db_imu_chronos.csv" --output-dir "$W/results/imu" --seeds 1 2 3 4 --include-balanced
# 4. Frame-count sensitivity, seed 0, 80/20 + LOSO.
for N in 16 32 48 0; do
  run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/frames/temporal_features_f$N.csv" "$W/frames/general_db_lm_chronos_f$N.csv" --output-dir "$W/results/frames" --seeds 0 --parts balanced loso
done
echo "[$(date +%H:%M)] done"
