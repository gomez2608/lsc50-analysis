"""CLI: fine-tune ViViT on a per-subject (LOSO) split.

Replaces ``VIDEOS/model_train_custom.py``. Defaults match the original
(30 epochs, batch=3, lr=6e-5).

Revision mode (``--dataset clips_all``): the held-out signer is taken from the
full clip table built by ``build_dataset_all.py``; the checkpoint is selected
on a validation split of the *training* signers (``--val-mode``, P13); the
test signer is scored once at the end and written to ``results.json`` in the
output directory.

Legacy mode (no ``--dataset``): loads the per-subject train/test datasets built
by ``build_dataset_cv.py``. The validation split is still drawn from the
training data, by rows, since those datasets carry no signer column.

Usage:
    python videos/scripts/train_cv.py --dataset clips_all --subject 0 --seed 0
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
from transformers import VivitForVideoClassification

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


class ShuffledLabels(torch.utils.data.Dataset):
    """A training set whose labels are replaced by a fixed permutation (shuffled-label control)."""

    def __init__(self, ds, labels: np.ndarray) -> None:
        self.ds, self.labels = ds, labels

    def __len__(self) -> int:
        return len(self.ds)

    def __getitem__(self, i: int) -> dict:
        row = dict(self.ds[i])
        row["labels"] = int(self.labels[i])
        return row


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune ViViT on a per-subject split.")
    parser.add_argument("-s", "--subject", type=int, required=True, help="Subject id held out for testing.")
    parser.add_argument("--dataset", default=None, help="Full clip table from build_dataset_all.py.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--val-mode", choices=["signer", "rows", "none"], default="signer",
                        help="Validation split from the training data: one training signer (protocol A), 10%% of rows, "
                             "or none: train on all training signers for --epochs and keep the final model (protocol B).")
    parser.add_argument("--resume", action="store_true", help="Resume from an existing per-subject model.")
    parser.add_argument("--shuffle-labels", action="store_true",
                        help="Shuffled-label control: permute the training labels (seeded); test labels unchanged.")
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=3)
    parser.add_argument("--learning-rate", type=float, default=6e-5)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=4)
    parser.add_argument("--logging-dir", default="./models/logs")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--precision", choices=["fp32", "fp16"], default="fp32",
                        help="fp32 is much faster on Pascal GPUs; the original runs used fp16.")
    parser.add_argument("--train-prefix", default="train_dataset_v2_subject_")
    parser.add_argument("--test-prefix", default="test_dataset_v2_subject_")
    parser.add_argument("--output-dir", default=None,
                        help="Defaults to vivit-s{subject}-seed{seed} (revision) or vivit-finetuned-s{subject} (legacy).")
    args = parser.parse_args()

    torch.cuda.empty_cache()
    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()

    base_dir = os.getcwd()
    if args.dataset:
        full = load_split(base_dir, args.dataset)
        subjects = column(full, "subject")
        train_ds = full.select(np.where(subjects != args.subject)[0])
        test_ds = full.select(np.where(subjects == args.subject)[0])
        output_dir = args.output_dir or f"vivit-s{args.subject}-seed{args.seed}"
        val_mode = args.val_mode
    else:
        train_ds = load_split(base_dir, f"{args.train_prefix}{args.subject}")
        test_ds = load_split(base_dir, f"{args.test_prefix}{args.subject}")
        output_dir = args.output_dir or f"vivit-finetuned-s{args.subject}"
        val_mode = "rows"
    fit_ds, val_ds = validation_split(train_ds, val_mode, args.seed)
    if args.shuffle_labels:
        # Wrap instead of rewriting the Arrow table (a rewrite of the 9.7 GB clip table hits Arrow's
        # 2 GB array limit); the collator reads only pixel_values and labels.
        assert val_mode == "none", "shuffled-label control is defined for protocol B (--val-mode none)"
        fit_ds = ShuffledLabels(fit_ds, np.random.default_rng(args.seed).permutation(column(fit_ds, "labels")))
    print(f"Held-out subject {args.subject}: fit {len(fit_ds)}, validation {len(val_ds) if val_ds is not None else 0} ({val_mode}), test {len(test_ds)}")

    num_labels = len(set(column(train_ds, "labels")) | set(column(test_ds, "labels")))
    if args.resume:
        try:
            model = VivitForVideoClassification.from_pretrained(output_dir)
        except OSError as exc:
            raise FileNotFoundError(f"No existing model at {output_dir}") from exc
    else:
        model = load_model(num_labels=num_labels, checkpoint=args.checkpoint)

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
        evaluate=val_ds is not None,
    )

    trainer = make_trainer(model, fit_ds, val_ds, processor, config)
    trainer.train()
    trainer.save_model(output_dir)
    pd.DataFrame(trainer.state.log_history).to_csv(os.path.join(output_dir, "log_history.csv"))

    result = score_split(trainer, test_ds)
    result.update(
        subject=args.subject,
        seed=args.seed,
        val_mode=val_mode,
        best_checkpoint=trainer.state.best_model_checkpoint,
        best_val_metric=trainer.state.best_metric,
        n_fit=len(fit_ds),
        n_val=len(val_ds) if val_ds is not None else 0,
        n_test=len(test_ds),
        config=vars(args),
    )
    with open(os.path.join(output_dir, "results.json"), "w") as f:
        json.dump(result, f)
    print(f"Test subject {args.subject}: accuracy {result['accuracy']:.3f}, "
          f"F1 weighted {result['f1_weighted']:.3f}, F1 macro {result['f1_macro']:.3f}")

    if torch.distributed.is_initialized():
        torch.distributed.destroy_process_group()


if __name__ == "__main__":
    main()
