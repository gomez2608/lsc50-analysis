"""Inference + confusion-matrix helpers for a fine-tuned ViViT.

The general flow runs a single forward pass over an entire test split.
For per-subject runs, the original code had to discover the best checkpoint
inside ``vivit-finetuned-s{subject}/checkpoint-*``; that logic is preserved
here as :func:`find_best_checkpoint`.
"""

from __future__ import annotations

import json
import os
import re
from typing import Any

import torch
from datasets import load_from_disk
from sklearn.metrics import confusion_matrix
from tqdm import tqdm
from transformers import VivitForVideoClassification

# Static class mapping used by the original per-subject inference script.
CLASS_MAPPING: dict[int, str] = {
    0: "Niña", 1: "Poco", 2: "Feliz", 3: "Hola", 4: "Sentir", 5: "Contento", 6: "Jucioso",
    7: "Diferente", 8: "Abuelo", 9: "Hombre", 10: "Seña", 11: "Permiso", 12: "Mal",
    13: "Con Gusto", 14: "Ustedes", 15: "Perdon", 16: "¿Como estas?", 17: "Tio ", 18: "Hermano",
    19: "Nunca", 20: "Trabajar", 21: "Aburrido", 22: "Vivir", 23: "Buenos Dias", 24: "Todos",
    25: "Bienvenido", 26: "¿Como?", 27: "¿Quien?", 28: "Por favor", 29: "¿Cuando?", 30: "Tu",
    31: "Buenas Tardes", 32: "Gracias", 33: "Hambre", 34: "Niño", 35: "Mujer", 36: "Adios",
    37: "Personas", 38: "Bien", 39: "Yo", 40: "Triste", 41: "¿Por que?", 42: "Mucho",
    43: "Nombre", 44: "¿Que?", 45: "Comer", 46: "Buenas Noches", 47: "¿Donde?", 48: "Familia",
    49: "Mas o menos",
}


def _list_checkpoint_dirs(run_dir: str) -> list[str]:
    if not os.path.isdir(run_dir):
        return []

    def step(name: str) -> int:
        m = re.search(r"checkpoint-(\d+)", name)
        return int(m.group(1)) if m else -1

    dirs = [d for d in os.listdir(run_dir) if d.startswith("checkpoint-")]
    return sorted([os.path.join(run_dir, d) for d in dirs], key=lambda p: step(os.path.basename(p)))


def _extract_best_from_state(state_path: str) -> str | None:
    try:
        with open(state_path) as f:
            state = json.load(f)
        return state.get("best_model_checkpoint")
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def find_best_checkpoint(run_dir: str) -> str | None:
    """Walk the ``checkpoint-*`` folders inside ``run_dir`` and return the one
    flagged by the most recent ``trainer_state.json`` as best, or the last
    checkpoint if none is flagged.
    """
    checkpoints = _list_checkpoint_dirs(run_dir)
    if not checkpoints:
        return None

    best_found: str | None = None
    for ckpt in checkpoints:
        candidate = _extract_best_from_state(os.path.join(ckpt, "trainer_state.json"))
        if candidate:
            best_found = candidate

    if best_found and os.path.isdir(best_found):
        return best_found
    return checkpoints[-1]


def load_model(run_dir: str, prefer_best: bool = True) -> VivitForVideoClassification:
    if prefer_best:
        best = find_best_checkpoint(run_dir)
        if best:
            return VivitForVideoClassification.from_pretrained(best)
    return VivitForVideoClassification.from_pretrained(run_dir)


def evaluate_split_streamed(
    model: VivitForVideoClassification,
    dataset_path: str,
    *,
    device: str = "cuda",
) -> dict[str, Any]:
    """One-row-at-a-time evaluation (used by the per-subject CV pipeline)."""
    ds = load_from_disk(dataset_path)
    model = model.to(device)
    model.eval()

    preds: list[int] = []
    labels: list[int] = []
    with torch.no_grad():
        for row in tqdm(ds, desc="Inference"):
            inputs = torch.tensor(row["pixel_values"], dtype=torch.float32).unsqueeze(0).to(device)
            out = model(inputs)
            preds.append(int(out.logits.argmax(dim=-1).item()))
            labels.append(int(row["labels"]))

    return {
        "confusion_matrix": confusion_matrix(labels, preds),
        "inferences": preds,
        "real_labels": labels,
        "class_mapping": CLASS_MAPPING,
    }


def evaluate_split_batched(
    model: VivitForVideoClassification,
    dataset_path: str,
    *,
    device: str = "cuda",
) -> dict[str, Any]:
    """Single-pass evaluation (used by the general pipeline).

    Loads the entire test split's pixel values onto the GPU at once, matching
    the behavior of the original ``inference_cm.py``. Use the streamed version
    for larger datasets that would not fit in memory.
    """
    ds = load_from_disk(dataset_path)
    model = model.to(device)
    model.eval()

    with torch.no_grad():
        outputs = model(torch.tensor(ds["pixel_values"]).to(device))
        logits = outputs.logits

    preds = [int(torch.argmax(logits[i]).item()) for i in range(logits.shape[0])]
    labels = ds["labels"] if "labels" in ds.column_names else ds["label"]
    return {
        "confusion_matrix": confusion_matrix(labels, preds),
        "inferences": preds,
        "real_labels": list(labels),
    }
