#!/bin/bash
# LOSO with signer-grouped inner CV (the protocol adopted after P15), seeds 1-4,
# so every held-out-signer number has a seed spread (RF depends on the seed).
set -euo pipefail
PY="$1"; REPO="$2"; W="$3"
cd "$REPO"
LOG="$W/results/errors_groupcv_seeds.log"
run() { echo "[$(date +%H:%M)] $*"; "$@" > /dev/null 2>>"$LOG"; }
run "$PY" imu/scripts/grid_search.py --features-csv "$W/temporal.csv" "$W/general_db_imu_chronos.csv" --output-dir "$W/results/imu" --seeds 1 2 3 4 --inner-cv group
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/temporal_features.csv" "$W/general_db_lm_chronos.csv" --output-dir "$W/results/landmarks" --seeds 1 2 3 4 --parts loso --inner-cv group
echo "[$(date +%H:%M)] done"
