#!/bin/bash
# Shuffled-label controls that were missing (audit N1), seed 0, same pipelines as the main runs:
# body-relative landmark TSFEL (LOSO with grouped inner CV; 80/20 with stratified inner CV),
# frozen-ViViT CLS features through the same SVM/RF/KNN grids, and the frozen-ViViT linear probe.
# Training labels are permuted; test labels are the true ones. Server CPU, nice.
#   scripts/revision/run_controls.sh PYTHON WORK
set -euo pipefail
PY="$1"; W="$2"
cd "$(dirname "$0")/../.."
LOG="$W/controls.log"
git log --oneline -1 > "$W/controls.commit"
run() { echo "[$(date '+%F %H:%M')] $*" | tee -a "$LOG"; nice -n 10 "$@" >> "$LOG" 2>&1; }
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/bodynorm/temporal_features_bodynorm.csv" --output-dir "$W/bodynorm" --seeds 0 --parts loso --inner-cv group --shuffle-labels
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/bodynorm/temporal_features_bodynorm.csv" --output-dir "$W/bodynorm" --seeds 0 --parts balanced --shuffle-labels
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/vivit_frozen/vivit_frozen_cls.csv" --output-dir "$W/vivit_frozen" --seeds 0 --parts loso --inner-cv group --shuffle-labels
run "$PY" landmarks/scripts/grid_search.py --features-csv "$W/vivit_frozen/vivit_frozen_cls.csv" --output-dir "$W/vivit_frozen" --seeds 0 --parts balanced --shuffle-labels
run "$PY" scripts/revision/linear_probe.py --features-csv "$W/vivit_frozen/vivit_frozen_cls.csv" --output-csv "$W/vivit_frozen/probe_cls_shuffled.csv" --seeds 0 --shuffle-labels
echo "[$(date '+%F %H:%M')] controls done" | tee -a "$LOG"
