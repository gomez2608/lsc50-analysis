"""CLI: fine-tune ViViT on the general (random) split.

Replaces ``VIDEOS/model_train.py``. Mirrors the original hyperparameters
(13 epochs, batch=2, lr=5e-5) but accepts overrides via CLI.

Revision mode (``--dataset clips_all``): draws a stratified 80/20 split of the
full clip table with ``--seed``, selects the checkpoint on 10% of the training
rows (P13), scores the test split once at the end and writes ``results.json``
to the output directory.

Legacy mode (no ``--dataset``): loads ``--train-dataset`` / ``--test-dataset``
built by ``build_dataset.py``; the validation split is still drawn from the
training rows.

Usage:
    python videos/scripts/train.py --dataset clips_all --seed 0
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.train import (
    DEFAULT_VIVIT_CHECKPOINT,
    TrainingConfig,
    load_model,
    load_processor,
    column,
    load_split,
    make_trainer,
    score_split,
    validation_split,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune ViViT on the general dataset.")
    parser.add_argument("--dataset", default=None, help="Full clip table from build_dataset_all.py.")
    parser.add_argument("--test-split", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train-dataset", default="train_dataset_v2")
    parser.add_argument("--test-dataset", default="test_dataset_v2")
    parser.add_argument("--output-dir", default=None,
                        help="Defaults to vivit-8020-seed{seed} (revision) or vivit-finetuned-def (legacy).")
    parser.add_argument("--epochs", type=int, default=13)
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=5e-5)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=4)
    parser.add_argument("--logging-dir", default="./logs-train")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--precision", choices=["fp32", "fp16"], default="fp32",
                        help="fp32 is much faster on Pascal GPUs; the original runs used fp16.")
    args = parser.parse_args()

    torch.cuda.empty_cache()
    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()

    base_dir = os.getcwd()
    if args.dataset:
        full = load_split(base_dir, args.dataset)
        labels = column(full, "labels")
        train_idx, test_idx = train_test_split(
            np.arange(len(labels)), test_size=args.test_split, stratify=labels, random_state=args.seed
        )
        train_ds, test_ds = full.select(np.sort(train_idx)), full.select(np.sort(test_idx))
        output_dir = args.output_dir or f"vivit-8020-seed{args.seed}"
    else:
        train_ds = load_split(base_dir, args.train_dataset)
        test_ds = load_split(base_dir, args.test_dataset)
        output_dir = args.output_dir or "vivit-finetuned-def"
    fit_ds, val_ds = validation_split(train_ds, "rows", args.seed)
    print(f"80/20: fit {len(fit_ds)}, validation {len(val_ds)}, test {len(test_ds)}")

    model = load_model(num_labels=len(set(column(train_ds, "labels"))), checkpoint=args.checkpoint)
    processor = load_processor(args.checkpoint)

    config = TrainingConfig(
        output_dir=output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        logging_dir=args.logging_dir,
        seed=args.seed,
        fp16=args.precision == "fp16",
    )

    trainer = make_trainer(model, fit_ds, val_ds, processor, config)
    trainer.train()
    trainer.save_model(output_dir)
    pd.DataFrame(trainer.state.log_history).to_csv(os.path.join(output_dir, "log_history.csv"))

    result = score_split(trainer, test_ds)
    result.update(
        seed=args.seed,
        best_checkpoint=trainer.state.best_model_checkpoint,
        best_val_metric=trainer.state.best_metric,
        n_fit=len(fit_ds),
        n_val=len(val_ds),
        n_test=len(test_ds),
        config=vars(args),
    )
    with open(os.path.join(output_dir, "results.json"), "w") as f:
        json.dump(result, f)
    print(f"Test: accuracy {result['accuracy']:.3f}, F1 weighted {result['f1_weighted']:.3f}, "
          f"F1 macro {result['f1_macro']:.3f}")


if __name__ == "__main__":
    main()
