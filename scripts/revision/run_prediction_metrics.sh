#!/bin/bash
# Secondary metrics (accuracy, macro precision / recall / F1), confusion matrices and per-sign F1 from the stored
# test predictions of every model in the final signer-interval run (R1.2, C24). Same sources as run_signer_ci.sh,
# plus the 80/20 runs. Nothing is trained. Sign names: the original workspace's correspondance.json (video and
# landmark file index -> sign), copied to OUTDIR.
#   scripts/revision/run_prediction_metrics.sh PYTHON LSC_REVISION_DIR OUTDIR
set -euo pipefail
PY="$1"; R="$2"; O="$3"
cd "$(dirname "$0")/../.."
mkdir -p "$O"
git log --oneline -1 > "$O/commit.txt"
W="$R/WORK"; V="$R/vivit"
cp "$HOME/LSC/IMU/correspondance.json" "$O/sign_names.json"
args=(
  --grid "Landmarks TSFEL body-relative=$W/bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed?.pkl|$W/bodynorm/grid_search_results_temporal_features_bodynorm_chronos_seed?.pkl"
  --grid "Landmarks TSFEL image coordinates=$W/results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed?.pkl|$W/results/landmarks/grid_search_results_temporal_features_chronos_seed?.pkl"
  --grid "Landmarks Chronos=$W/results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed?.pkl|$W/results/landmarks/grid_search_results_general_db_lm_chronos_chronos_seed?.pkl"
  --grid "IMU TSFEL=$W/results/imu/grid_search_results_temporal_groupcv_seed?.pkl|$W/results/imu/grid_search_results_temporal_seed?.pkl"
  --grid "IMU Chronos=$W/results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed?.pkl|$W/results/imu/grid_search_results_general_db_imu_chronos_seed?.pkl"
  --grid "Frozen ViViT CLS=$W/vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_groupcv_seed?.pkl|$W/vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_seed?.pkl"
  --json "Pose transformer, image coordinates=$W/pose/image/pose-*-seed?.json"
  --json "Pose transformer, body-relative=$W/pose/bodynorm/pose-*-seed?.json"
  --json "ST-GCN, image coordinates=$W/stgcn_v2/image/stgcn-*-seed?.json"
  --json "ST-GCN, body-relative=$W/stgcn_v2/bodynorm/stgcn-*-seed?.json"
  --json "SlowFast R50=$W/fusion/slowfast/slowfast-*-seed?.json"
  --json "Official SPOTER=$W/spoter/spoter-*-seed?.json"
  --json "Late fusion SlowFast + SPOTER=$W/fusion/fused/fusion-*-seed?.json"
  --vivit "ViViT fine-tuned, protocol B=$V/vivit-B-s?-seed?/results.json"
  --vivit "ViViT fine-tuned, protocol A=$V/vivit-s?-seed?/results.json"
  --vivit "ViViT fine-tuned, 80/20 recipe=$V/vivit-8020-seed?/results.json"  # own recipe (13 epochs), not protocol A or B
)
for m in "Late fusion SlowFast + SPOTER" "SlowFast R50" "Official SPOTER" "Landmarks TSFEL body-relative + RF"; do
  args+=(--confusion "$m")
done
printf '%q ' "$PY" scripts/revision/prediction_metrics.py "${args[@]}" --sign-names "$O/sign_names.json" --output-dir "$O" > "$O/command.txt"
"$PY" scripts/revision/prediction_metrics.py "${args[@]}" --sign-names "$O/sign_names.json" --output-dir "$O" | tee "$O/prediction_metrics.log"
