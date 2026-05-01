"""Shared ViViT fine-tuning helpers.

The original ``model_train.py`` and ``model_train_custom.py`` differed only in
hyperparameters and output paths. This module centralizes the model and
``Trainer`` construction so the two CLIs in :mod:`videos.scripts` only have
to supply the differing arguments.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import numpy as np
from datasets import load_from_disk
from sklearn.metrics import accuracy_score
from transformers import (
    Trainer,
    TrainingArguments,
    VivitForVideoClassification,
    VivitImageProcessor,
)

DEFAULT_VIVIT_CHECKPOINT = "google/vivit-b-16x2-kinetics400"


def compute_metrics(p: Any) -> dict[str, float]:
    preds = np.argmax(p.predictions, axis=1)
    return {"accuracy": accuracy_score(p.label_ids, preds)}


def load_split(base_dir: str, name: str):
    return load_from_disk(os.path.join(base_dir, name))


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

    def to_training_arguments(self) -> TrainingArguments:
        return TrainingArguments(
            num_train_epochs=self.num_train_epochs,
            per_device_train_batch_size=self.per_device_train_batch_size,
            per_device_eval_batch_size=self.per_device_eval_batch_size,
            output_dir=self.output_dir,
            eval_strategy="epoch",
            save_strategy="epoch",
            learning_rate=self.learning_rate,
            logging_dir=self.logging_dir,
            report_to=None,
            do_train=True,
            do_eval=True,
            do_predict=True,
            fp16=True,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            ddp_find_unused_parameters=False,
            load_best_model_at_end=True,
            metric_for_best_model="accuracy",
            greater_is_better=True,
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
        compute_metrics=compute_metrics,
    )
