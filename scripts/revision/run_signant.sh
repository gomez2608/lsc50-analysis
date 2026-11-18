#!/bin/bash
# Native (deaf) vs. interpreter with the corrected mapping (P6): rows 80/20,
# 10 signs held out, and one whole signer held out (R2.8). Seed 0.
# Separate output dir so the SLR pickles are not overwritten. Inner CV stays
# stratified: with a signer held out, a grouped inner fold could leave a single
# class in training. Waits for run_groupcv_seeds.sh.
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"
cd "$REPO"
LOG="$W/results/errors_signant.log"
run() { echo "[$(date +%H:%M)] $*"; "$@" > /dev/null 2>>"$LOG"; }
echo "[$(date +%H:%M)] waiting for run_groupcv_seeds.sh"
while pgrep -f "results/run_groupcv_seeds.sh" > /dev/null; do sleep 60; done
run "$PY" imu/scripts/grid_search.py --features-csv "$W/temporal.csv" "$W/general_db_imu_chronos.csv" --output-dir "$W/results/signant_imu" --seeds 0 --include-signant
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/temporal_features.csv" "$W/general_db_lm_chronos.csv" --output-dir "$W/results/signant_landmarks" --seeds 0 --parts signant signant_new_schema signant_loso
echo "[$(date +%H:%M)] done"
