"""CLI: fine-tune ViViT on the general (random) split.

Replaces ``VIDEOS/model_train.py``. Mirrors the original hyperparameters
(13 epochs, batch=2, lr=5e-5) but accepts overrides via CLI.

Usage:
    python videos/scripts/train.py \\
        --train-dataset train_dataset_v2 \\
        --test-dataset test_dataset_v2 \\
        --output-dir ./vivit-finetuned-def
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.train import (
    DEFAULT_VIVIT_CHECKPOINT,
    TrainingConfig,
    load_model,
    load_processor,
    load_split,
    make_trainer,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune ViViT on the general dataset.")
    parser.add_argument("--train-dataset", default="train_dataset_v2")
    parser.add_argument("--test-dataset", default="test_dataset_v2")
    parser.add_argument("--output-dir", default="./vivit-finetuned-def")
    parser.add_argument("--epochs", type=int, default=13)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=5e-5)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=4)
    parser.add_argument("--logging-dir", default="./logs-train")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--logs-csv", default="logs_general.csv")
    args = parser.parse_args()

    torch.cuda.empty_cache()
    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()

    base_dir = os.getcwd()
    train_ds = load_split(base_dir, args.train_dataset)
    test_ds = load_split(base_dir, args.test_dataset)

    model = load_model(num_labels=len(set(train_ds["labels"])), checkpoint=args.checkpoint)
    processor = load_processor(args.checkpoint)

    config = TrainingConfig(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        logging_dir=args.logging_dir,
    )

    trainer = make_trainer(model, train_ds, test_ds, processor, config)
    trainer.train()

    pd.DataFrame(trainer.state.log_history).to_csv(args.logs_csv)
    trainer.save_model(args.output_dir)


if __name__ == "__main__":
    main()
