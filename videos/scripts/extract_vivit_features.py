"""CLI: frozen ViViT features for every clip (linear-probe baseline).

Runs the pretrained, *not* fine-tuned ViViT once over the clip table built by
``build_dataset_all.py`` and writes two CSVs in the format of the other feature
tables (``label, subject, rep, features_*``):

- ``*_cls.csv``: the final-layer CLS token (768 values). This is exactly what the
  classification head of ``VivitForVideoClassification`` sees, so a linear
  classifier on it is "fine-tuning only the head".
- ``*_mean.csv``: the mean over all final-layer tokens.

Usage:
    python videos/scripts/extract_vivit_features.py --dataset clips_all --output-prefix vivit_frozen
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from tqdm import tqdm
from transformers import VivitModel

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.train import DEFAULT_VIVIT_CHECKPOINT, column, load_split


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dataset", required=True, help="Clip table from build_dataset_all.py.")
    parser.add_argument("--output-prefix", default="vivit_frozen")
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    ds = load_split(".", args.dataset)
    model = VivitModel.from_pretrained(args.checkpoint, add_pooling_layer=False).to(args.device).eval()

    cls_rows, mean_rows = [], []
    with torch.no_grad():
        for row in tqdm(ds, desc="Frozen ViViT"):
            pixels = row["pixel_values"].float().unsqueeze(0).to(args.device)
            hidden = model(pixel_values=pixels).last_hidden_state[0]
            cls_rows.append(hidden[0].cpu().numpy())
            mean_rows.append(hidden.mean(dim=0).cpu().numpy())

    meta = pd.DataFrame({k: column(ds, k) for k in ("labels", "subject", "rep")}).rename(columns={"labels": "label"})
    for name, rows in (("cls", cls_rows), ("mean", mean_rows)):
        feats = pd.DataFrame(np.vstack(rows), columns=[f"features_{i}" for i in range(len(rows[0]))])
        out = f"{args.output_prefix}_{name}.csv"
        pd.concat([meta, feats], axis=1).to_csv(out, index=False)
        print(f"Wrote {len(feats)} clips x {feats.shape[1]} features to {out}")


if __name__ == "__main__":
    main()
