#!/bin/bash
# Signer-level CIs and the planned paired comparisons for every LOSO model (audit M1, N3, K7).
# Inputs that do not exist yet (e.g. ST-GCN v2, SlowFast before they finish) are skipped.
# Planned comparisons, fixed 2026-10-20: the main classical pipeline (landmark TSFEL
# body-relative + RF) against every other model family's main configuration. Added 2026-10-27, before this run:
# official SPOTER against the reference (a main-text model family since the plan of 2026-10-26), and the two
# comparisons fixed in docs/FUSION.md before the fusion runs: fusion vs. SlowFast and fusion vs. SPOTER (seeds 0-2,
# the seeds fused). SlowFast = the fusion retraining, which replaces the stored runs (FUSION.md).
#   scripts/revision/run_signer_ci.sh PYTHON LSC_REVISION_DIR OUTDIR
set -euo pipefail
PY="$1"; R="$2"; O="$3"
cd "$(dirname "$0")/../.."
mkdir -p "$O"
git log --oneline -1 > "$O/commit.txt"
W="$R/WORK"; V="$R/vivit"
REF="Landmarks TSFEL body-relative + RF"
args=(
  --grid "Landmarks TSFEL body-relative=$W/bodynorm/grid_search_results_temporal_features_bodynorm_chronos_groupcv_seed?.pkl"
  --grid "Landmarks TSFEL image coordinates=$W/results/landmarks/grid_search_results_temporal_features_chronos_groupcv_seed?.pkl"
  --grid "Landmarks Chronos=$W/results/landmarks/grid_search_results_general_db_lm_chronos_chronos_groupcv_seed?.pkl"
  --grid "IMU TSFEL=$W/results/imu/grid_search_results_temporal_groupcv_seed?.pkl"
  --grid "IMU Chronos=$W/results/imu/grid_search_results_general_db_imu_chronos_groupcv_seed?.pkl"
  --grid "Frozen ViViT CLS=$W/vivit_frozen/grid_search_results_vivit_frozen_cls_chronos_groupcv_seed?.pkl"
  --json "Pose transformer, image coordinates=$W/pose/image/pose-loso-s?-seed?.json"
  --json "Pose transformer, body-relative=$W/pose/bodynorm/pose-loso-s?-seed?.json"
  --json "ST-GCN, image coordinates=$W/stgcn_v2/image/stgcn-loso-s?-seed?.json"
  --json "ST-GCN, body-relative=$W/stgcn_v2/bodynorm/stgcn-loso-s?-seed?.json"
  --json "SlowFast R50=$W/fusion/slowfast/slowfast-loso-s?-seed?.json"
  --json "Official SPOTER=$W/spoter/spoter-loso-s?-seed?.json"
  --json "Official SPOTER, seeds 0-2=$W/fusion/spoter/spoter-loso-s?-seed?.json"
  --json "Late fusion SlowFast + SPOTER=$W/fusion/fused/fusion-loso-s?-seed?.json"
  --vivit "ViViT fine-tuned, protocol B=$V/vivit-B-s?-seed?/results.json"
  --vivit "ViViT fine-tuned, protocol A=$V/vivit-s?-seed?/results.json"
)
for m in "Pose transformer, body-relative" "Pose transformer, image coordinates" "ST-GCN, body-relative" \
         "ST-GCN, image coordinates" "SlowFast R50" "ViViT fine-tuned, protocol B" "Frozen ViViT CLS + SVM" \
         "Landmarks TSFEL image coordinates + RF" "Landmarks Chronos + SVM" "IMU TSFEL + RF" "Official SPOTER"; do
  args+=(--compare "$m::$REF")
done
args+=(--compare "Late fusion SlowFast + SPOTER::SlowFast R50" --compare "Late fusion SlowFast + SPOTER::Official SPOTER, seeds 0-2")
printf '%q ' "$PY" scripts/revision/signer_ci.py "${args[@]}" --output-csv "$O/signer_ci.csv" --pairs-csv "$O/signer_pairs.csv" > "$O/command.txt"
"$PY" scripts/revision/signer_ci.py "${args[@]}" --output-csv "$O/signer_ci.csv" --pairs-csv "$O/signer_pairs.csv" | tee "$O/signer_ci.log"
