"""CLI: fine-tune ViViT on a per-subject (LOSO) split.

Replaces ``VIDEOS/model_train_custom.py``. Defaults match the original
(30 epochs, batch=3, lr=6e-5). Pass ``--resume`` to continue training from
the existing ``vivit-finetuned-s{subject}`` directory.

Usage:
    python videos/scripts/train_cv.py --subject 0
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
import torch
from transformers import VivitForVideoClassification

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.train import (
    DEFAULT_VIVIT_CHECKPOINT,
    TrainingConfig,
    load_processor,
    load_split,
    make_trainer,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune ViViT on a per-subject split.")
    parser.add_argument("-s", "--subject", type=int, required=True, help="Subject id held out for testing.")
    parser.add_argument("--resume", action="store_true", help="Resume from an existing per-subject model.")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=3)
    parser.add_argument("--learning-rate", type=float, default=6e-5)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=4)
    parser.add_argument("--logging-dir", default="./models/logs")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--train-prefix", default="train_dataset_v2_subject_")
    parser.add_argument("--test-prefix", default="test_dataset_v2_subject_")
    parser.add_argument("--output-prefix", default="./vivit-finetuned-s")
    args = parser.parse_args()

    torch.cuda.empty_cache()
    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()

    base_dir = os.getcwd()
    train_ds = load_split(base_dir, f"{args.train_prefix}{args.subject}")
    test_ds = load_split(base_dir, f"{args.test_prefix}{args.subject}")
    output_dir = f"{args.output_prefix}{args.subject}"

    if args.resume:
        try:
            model = VivitForVideoClassification.from_pretrained(output_dir)
        except OSError as exc:
            raise FileNotFoundError(f"No existing model at {output_dir}") from exc
    else:
        model = VivitForVideoClassification.from_pretrained(
            args.checkpoint, num_labels=len(set(train_ds["labels"])), ignore_mismatched_sizes=True
        )

    processor = load_processor(args.checkpoint)
    config = TrainingConfig(
        output_dir=output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        logging_dir=args.logging_dir,
    )

    trainer = make_trainer(model, train_ds, test_ds, processor, config)
    trainer.train()

    csv_name = f"logs_s{args.subject}{'_compl' if args.resume else ''}.csv"
    pd.DataFrame(trainer.state.log_history).to_csv(csv_name)
    trainer.save_model(output_dir)

    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()


if __name__ == "__main__":
    main()
