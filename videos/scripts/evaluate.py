"""CLI: evaluate a fine-tuned ViViT on a saved test split.

Replaces ``VIDEOS/inference_cm.py``. Single-pass batched inference; suitable
for the general (non-subject) ``test_dataset_v2``.

Usage:
    python videos/scripts/evaluate.py \\
        --model-dir ./vivit-finetuned \\
        --test-dataset test_dataset_v2 \\
        --output confusion_matrix.pkl
"""

from __future__ import annotations

import argparse
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.evaluate import evaluate_split_batched, load_model


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate ViViT on the general test split.")
    parser.add_argument("--model-dir", default="./vivit-finetuned", help="Directory of the fine-tuned model.")
    parser.add_argument("--test-dataset", default="test_dataset_v2", help="Saved HF dataset to evaluate on.")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--output", default="confusion_matrix.pkl", help="Pickle path for the results dict.")
    args = parser.parse_args()

    model = load_model(args.model_dir, prefer_best=False)
    result = evaluate_split_batched(model, args.test_dataset, device=args.device)

    with open(args.output, "wb") as f:
        pickle.dump(result["confusion_matrix"], f)
    print(f"Saved confusion matrix to {args.output}")


if __name__ == "__main__":
    main()
