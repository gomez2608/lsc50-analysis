#!/bin/bash
# SLR reruns after the leakage fixes (commit on branch fix/leakage-audit).
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"
cd "$REPO"
LM=("$W/temporal_features.csv" "$W/general_db_lm_chronos.csv")
IMU=("$W/temporal.csv" "$W/general_db_imu_chronos.csv")
run() { echo "[$(date +%H:%M)] $*"; "$@" > /dev/null 2>>"$W/results/errors.log"; }
# 1. All SLR splits, seed 0
run "$PY" landmarks/scripts/grid_search.py --features-csv "${LM[@]}" --output-dir "$W/results/landmarks" --seeds 0 --parts balanced loso
run "$PY" imu/scripts/grid_search.py --features-csv "${IMU[@]}" --output-dir "$W/results/imu" --seeds 0 --include-balanced
# 2. Shuffled-label control, seed 0
run "$PY" landmarks/scripts/grid_search.py --features-csv "${LM[@]}" --output-dir "$W/results/landmarks" --seeds 0 --parts balanced loso --shuffle-labels
run "$PY" imu/scripts/grid_search.py --features-csv "${IMU[@]}" --output-dir "$W/results/imu" --seeds 0 --include-balanced --shuffle-labels
# 3. Extra seeds for the 80/20 split
run "$PY" landmarks/scripts/grid_search.py --features-csv "${LM[@]}" --output-dir "$W/results/landmarks" --seeds 1 2 3 4 --parts balanced
echo "[$(date +%H:%M)] done"
