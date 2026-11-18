"""Shared ViViT fine-tuning helpers.

The original ``model_train.py`` and ``model_train_custom.py`` differed only in
hyperparameters and output paths. This module centralizes the model and
``Trainer`` construction so the two CLIs in :mod:`videos.scripts` only have
to supply the differing arguments.

Revision changes (P13 in ``docs/REVISION_LOG.md``): the checkpoint is chosen on
a validation split carved out of the *training* data
(:func:`validation_split`), never on the test split; the test split is scored
once at the end (:func:`score_split`). Runs are seeded, and weighted/macro F1
are reported alongside accuracy.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import numpy as np
import torch
from datasets import load_from_disk
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from transformers import (
    Trainer,
    TrainingArguments,
    VivitForVideoClassification,
    VivitImageProcessor,
)

DEFAULT_VIVIT_CHECKPOINT = "google/vivit-b-16x2-kinetics400"


def metrics_from_preds(y_true, y_pred) -> dict[str, float]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "f1_weighted": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
    }


def compute_metrics(p: Any) -> dict[str, float]:
    preds = np.argmax(p.predictions, axis=1)
    return metrics_from_preds(p.label_ids, preds)


def validation_split(train_ds, mode: str, seed: int, fraction: float = 0.1):
    """Split ``train_ds`` into (fit, validation) for checkpoint selection.

    ``mode="signer"`` holds out one training signer (chosen with ``seed``), so
    the checkpoint is selected for cross-signer transfer; it needs a
    ``subject`` column. ``mode="rows"`` holds out ``fraction`` of the rows,
    stratified by sign.
    """
    if mode == "signer":
        subjects = column(train_ds, "subject")
        val_subject = np.random.default_rng(seed).choice(np.unique(subjects))
        fit_idx = np.where(subjects != val_subject)[0]
        val_idx = np.where(subjects == val_subject)[0]
    elif mode == "none":
        return train_ds, None
    elif mode == "rows":
        labels = column(train_ds, "labels")
        fit_idx, val_idx = train_test_split(
            np.arange(len(labels)), test_size=fraction, stratify=labels, random_state=seed
        )
    else:
        raise ValueError(f"Unknown validation mode {mode!r}")
    return train_ds.select(np.sort(fit_idx)), train_ds.select(np.sort(val_idx))


def score_split(trainer: Trainer, ds) -> dict[str, Any]:
    """Predict ``ds`` once with the trainer's current (best) model."""
    out = trainer.predict(ds, metric_key_prefix="test")
    y_pred = np.argmax(out.predictions, axis=1).tolist()
    y_true = np.asarray(out.label_ids).tolist()
    result: dict[str, Any] = metrics_from_preds(y_true, y_pred)
    result.update(y_true=y_true, y_pred=y_pred)
    if "subject" in ds.column_names:
        result["clip_subject"] = column(ds, "subject").tolist()
    return result


def collate_float32(rows: list[dict]) -> dict[str, torch.Tensor]:
    """Stack rows into a batch, upcasting float16-stored pixels to float32."""
    return {
        "pixel_values": torch.stack([torch.as_tensor(r["pixel_values"]) for r in rows]).float(),
        "labels": torch.tensor([int(r["labels"]) for r in rows]),
    }


def column(ds, name: str) -> np.ndarray:
    """A dataset column as a NumPy array, whatever the dataset's output format."""
    return np.asarray(ds.with_format(None)[name])


def load_split(base_dir: str, name: str):
    # Torch format: rows come back as tensors instead of nested Python lists,
    # which otherwise dominates training time for 32-frame clips.
    return load_from_disk(os.path.join(base_dir, name)).with_format("torch")


def load_model(num_labels: int, checkpoint: str = DEFAULT_VIVIT_CHECKPOINT) -> VivitForVideoClassification:
    return VivitForVideoClassification.from_pretrained(
        checkpoint, num_labels=num_labels, ignore_mismatched_sizes=True
    )


def load_processor(checkpoint: str = DEFAULT_VIVIT_CHECKPOINT) -> VivitImageProcessor:
    return VivitImageProcessor.from_pretrained(checkpoint)


@dataclass
class TrainingConfig:
    output_dir: str
    num_train_epochs: int = 13
    per_device_train_batch_size: int = 2
    per_device_eval_batch_size: int = 2
    learning_rate: float = 5e-5
    gradient_accumulation_steps: int = 4
    logging_dir: str = "./logs-train"
    seed: int = 42
    metric_for_best_model: str = "f1_weighted"
    # fp16 is ~6.6x slower than fp32 per clip on Pascal GPUs (TITAN X), which lack fast
    # half-precision math (benchmark 2026-10-17); the original runs used fp16.
    fp16: bool = False
    # False = no validation split: train for a fixed number of epochs and keep the
    # final model (protocol B in docs/REVISION_LOG.md).
    evaluate: bool = True

    def to_training_arguments(self) -> TrainingArguments:
        return TrainingArguments(
            num_train_epochs=self.num_train_epochs,
            per_device_train_batch_size=self.per_device_train_batch_size,
            per_device_eval_batch_size=self.per_device_eval_batch_size,
            output_dir=self.output_dir,
            eval_strategy="epoch" if self.evaluate else "no",
            save_strategy="epoch" if self.evaluate else "no",
            # One training-loss point per epoch for the learning curves (the default,
            # every 500 steps, logs nothing in a 390-step run).
            logging_strategy="epoch",
            learning_rate=self.learning_rate,
            logging_dir=self.logging_dir,
            report_to="none",
            do_train=True,
            do_eval=self.evaluate,
            do_predict=True,
            fp16=self.fp16 and torch.cuda.is_available(),
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            ddp_find_unused_parameters=False,
            load_best_model_at_end=self.evaluate,
            metric_for_best_model=self.metric_for_best_model if self.evaluate else None,
            greater_is_better=True,
            save_total_limit=2,
            seed=self.seed,
            data_seed=self.seed,
            remove_unused_columns=False,
        )


def make_trainer(
    model: VivitForVideoClassification,
    train_ds,
    eval_ds,
    processor: VivitImageProcessor,
    config: TrainingConfig,
) -> Trainer:
    return Trainer(
        model=model,
        args=config.to_training_arguments(),
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        processing_class=processor,
        data_collator=collate_float32,
        compute_metrics=compute_metrics,
    )
