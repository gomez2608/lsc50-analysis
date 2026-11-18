#!/bin/bash
# Statistics for the pose transformer study (protocol S6): summary tables, then paired per-signer
# comparisons against the default configuration with Holm correction within each family:
# (1) nested selection vs. default; (2) ablations A1-A6 vs. default body-relative, A7 vs. default
# image coordinates; (3) frame counts 16/32/48 vs. default 24.
#   scripts/revision/run_pose_study_stats.sh PYTHON WORK OUTDIR
set -euo pipefail
PY="$1"; W="$2"; O="$3"
cd "$(dirname "$0")/../.."
mkdir -p "$O"; git log --oneline -1 > "$O/commit.txt"
S="$W/pose_study"; D="$W/pose/bodynorm"; DI="$W/pose/image"
"$PY" scripts/revision/pose_study_summary.py --study-dir "$S" --default-dir "$D" --default-image-dir "$DI" --output-dir "$O" | tee "$O/summary.log"
DEF="Default, body-relative"
"$PY" scripts/revision/signer_ci.py --json "$DEF=$D/pose-loso-s?-seed?.json" --json "Nested selection=$S/nested/pose-loso-s?-seed?.json" \
  --compare "Nested selection::$DEF" --output-csv "$O/ci_nested.csv" --pairs-csv "$O/pairs_nested.csv" | tee "$O/ci_nested.log"
args=(--json "$DEF=$D/pose-loso-s?-seed?.json" --json "Default, image coordinates=$DI/pose-loso-s?-seed?.json")
for a in A1_no_augmentation A2_no_label_smoothing A3_plain_recipe A4_mean_pooling A5_hands_only A6_body_only; do
  args+=(--json "$a=$S/ablation/$a/pose-loso-s?-seed?.json" --compare "$a::$DEF")
done
args+=(--json "A7_image_rotation_about_shoulders=$S/ablation/A7_image_rotation_about_shoulders/pose-loso-s?-seed?.json"
       --compare "A7_image_rotation_about_shoulders::Default, image coordinates")
"$PY" scripts/revision/signer_ci.py "${args[@]}" --output-csv "$O/ci_ablations.csv" --pairs-csv "$O/pairs_ablations.csv" | tee "$O/ci_ablations.log"
args=(--json "$DEF=$D/pose-loso-s?-seed?.json")
for n in 16 32 48; do args+=(--json "$n frames=$S/frames/f$n/pose-loso-s?-seed?.json" --compare "$n frames::$DEF"); done
"$PY" scripts/revision/signer_ci.py "${args[@]}" --output-csv "$O/ci_frames.csv" --pairs-csv "$O/pairs_frames.csv" | tee "$O/ci_frames.log"
