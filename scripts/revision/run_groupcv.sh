#!/bin/bash
# SLR LOSO with signer-grouped inner CV for hyperparameter selection (P15).
# Waits for run_slr.sh and run_frames.sh so runs don't compete for CPU.
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"
cd "$REPO"
LOG="$W/results/errors_groupcv.log"
run() { echo "[$(date +%H:%M)] $*"; "$@" > /dev/null 2>>"$LOG"; }
echo "[$(date +%H:%M)] waiting for run_slr.sh / run_frames.sh"
while pgrep -f "results/run_slr.sh|results/run_frames.sh" > /dev/null; do sleep 60; done
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/temporal_features.csv" "$W/general_db_lm_chronos.csv" --output-dir "$W/results/landmarks" --seeds 0 --parts loso --inner-cv group
run "$PY" imu/scripts/grid_search.py --features-csv "$W/temporal.csv" "$W/general_db_imu_chronos.csv" --output-dir "$W/results/imu" --seeds 0 --inner-cv group
echo "[$(date +%H:%M)] done"
