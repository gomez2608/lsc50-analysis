"""CLI: per-subject (LOSO) evaluation of fine-tuned ViViT models.

Replaces ``VIDEOS/inference.py``. For each subject ``i``:
  - Loads ``test_dataset_v2_subject_{i}``.
  - Loads the best checkpoint inside ``vivit-finetuned-s{i}/`` (auto-detected
    via ``trainer_state.json``; falls back to the latest checkpoint).
  - Runs streamed inference and pickles a result dict containing the
    confusion matrix, per-row predictions/labels, and the class mapping.

Usage:
    python videos/scripts/evaluate_cv.py --subjects 0 1 2 3 4
"""

from __future__ import annotations

import argparse
import os
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.evaluate import evaluate_split_streamed, load_model


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate per-subject ViViT models.")
    parser.add_argument("--subjects", type=int, nargs="+", default=list(range(5)), help="Subject ids to evaluate.")
    parser.add_argument("--dataset-prefix", default="test_dataset_v2_subject_", help="Prefix for the per-subject test dataset paths.")
    parser.add_argument("--model-prefix", default="vivit-finetuned-s", help="Prefix for the per-subject model directories.")
    parser.add_argument("--output-prefix", default="confusion_matrix_subject_", help="Prefix for the output pickles.")
    parser.add_argument("--base-dir", default=os.getcwd(), help="Base directory containing the datasets and models.")
    parser.add_argument("--device", default="cuda")
    args = parser.parse_args()

    print(f"[INFO] Base dir: {args.base_dir}")

    for i in args.subjects:
        ds_path = os.path.join(args.base_dir, f"{args.dataset_prefix}{i}")
        if not os.path.isdir(ds_path):
            print(f"[WARN] Missing dataset for subject {i}: {ds_path}")
            continue

        model_dir = os.path.join(args.base_dir, f"{args.model_prefix}{i}")
        if not os.path.isdir(model_dir):
            print(f"[WARN] Missing model dir for subject {i}: {model_dir}")
            continue

        model = load_model(model_dir, prefer_best=True)
        result = evaluate_split_streamed(model, ds_path, device=args.device)

        out_path = os.path.join(args.base_dir, f"{args.output_prefix}{i}.pkl")
        with open(out_path, "wb") as f:
            pickle.dump(result, f)
        print(f"[INFO] Saved {out_path}")


if __name__ == "__main__":
    main()
