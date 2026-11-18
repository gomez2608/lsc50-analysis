"""Official SPOTER on LSC50 landmark sequences (R2.7; POSE_TRANSFORMER_STUDY.md, S7).

Model, dataset (augmentations, body and hand normalization), Gaussian noise and the training step are the
authors' code, vendored unmodified in `third_party/spoter/` (github.com/matyasbohacek/spoter, commit 0f909bf,
Apache 2.0; Boháček & Hrúz, WACV Workshops 2022). This script is only the glue: it writes our landmarks in
SPOTER's CSV format, builds the same splits as every other model, trains with the repository's defaults
(hidden 108, SGD lr 0.001, batch 1, 100 epochs, noise sd 0.001, augmentations on) and keeps the **final**
model, scored once. The repository's `train.py` is not used because it scores every saved checkpoint on the
test set and reports the best (test-set selection).

Input mapping: MediaPipe pose 0, 2, 5, 7, 8, 11-16 -> nose, leftEye, rightEye, leftEar, rightEar, left/right
shoulder, elbow, wrist; MediaPipe left/right hand -> SPOTER hand 0/1 (21 joints each); image coordinates in [0, 1];
native-length sequences; labels written 1-based. SPOTER was built on Apple Vision landmarks, so two conversions
(protocol amendment 2026-10-23, before any completed run): neck = midpoint of the shoulders (Vision's neck joint;
MediaPipe has none, and SPOTER's fallback of an integer 0 fails in its own loader, centres the body normalization
box at x = 0 and makes the arm-joint augmentation rotate about the frame corner), and y -> 1 - y (Vision's origin is
the lower left, y up; the body box extends downwards from the eyes in that convention).

Usage (in the SPOTER environment):
    python scripts/revision/spoter_baseline.py --input-csv WORK/frames/general_db_f0.csv --output-dir spoter \\
        --split loso --subject 0 --seed 0
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from torch import nn

SPOTER_DIR = Path(__file__).resolve().parents[2] / "third_party" / "spoter"
sys.path.insert(0, str(SPOTER_DIR))

from datasets.czech_slr_dataset import CzechSLRDataset  # noqa: E402  (official)
from normalization.body_normalization import BODY_IDENTIFIERS  # noqa: E402
from normalization.hand_normalization import HAND_IDENTIFIERS  # noqa: E402
from spoter.gaussian_noise import GaussianNoise  # noqa: E402
from spoter.spoter_model import SPOTER  # noqa: E402
from spoter.utils import train_epoch  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sequence_importance import grouped_importance_ragged  # noqa: E402

KEYS = ["label", "subject", "rep"]
BODY_MAP = {"nose": 0, "leftEye": 2, "rightEye": 5, "leftEar": 7, "rightEar": 8, "leftShoulder": 11, "rightShoulder": 12,
            "leftElbow": 13, "rightElbow": 14, "leftWrist": 15, "rightWrist": 16}  # "neck": shoulder midpoint, below
HAND_MAP = {"wrist": 0, "thumbCMC": 1, "thumbMP": 2, "thumbIP": 3, "thumbTip": 4, "indexMCP": 5, "indexPIP": 6, "indexDIP": 7,
            "indexTip": 8, "middleMCP": 9, "middlePIP": 10, "middleDIP": 11, "middleTip": 12, "ringMCP": 13, "ringPIP": 14,
            "ringDIP": 15, "ringTip": 16, "littleMCP": 17, "littlePIP": 18, "littleDIP": 19, "littleTip": 20}


def to_spoter_rows(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """One row per execution in SPOTER's CSV schema (lists as strings), plus the (label, subject, rep) keys."""
    assert set(BODY_MAP) | {"neck"} == set(BODY_IDENTIFIERS) and set(HAND_MAP) == set(HAND_IDENTIFIERS)
    cols = [c for c in data.columns if c.startswith("landmark_")]
    assert not data[cols].isna().any().any() and not (data[cols] == 0).any().any(), "SPOTER reads 0 as missing"
    rows, keys = [], []
    for key, g in data.groupby(KEYS, sort=True):
        g = g.sort_index()
        row = {}
        for name, i in BODY_MAP.items():
            row[f"{name}_X"], row[f"{name}_Y"] = str(g[f"landmark_{i}_x_B"].tolist()), str((1 - g[f"landmark_{i}_y_B"]).tolist())
        row["neck_X"] = str(((g["landmark_11_x_B"] + g["landmark_12_x_B"]) / 2).tolist())
        row["neck_Y"] = str((1 - (g["landmark_11_y_B"] + g["landmark_12_y_B"]) / 2).tolist())
        for side, part in (("0", "LH"), ("1", "RH")):
            for name, i in HAND_MAP.items():
                row[f"{name}_{side}_X"] = str(g[f"landmark_{i}_x_{part}"].tolist())
                row[f"{name}_{side}_Y"] = str((1 - g[f"landmark_{i}_y_{part}"]).tolist())
        row["labels"] = int(key[0]) + 1  # the loader subtracts 1
        rows.append(row)
        keys.append(key)
    return pd.DataFrame(rows), pd.DataFrame(keys, columns=KEYS)


def predict(model, dataset) -> np.ndarray:
    model.train(False)
    out = []
    with torch.no_grad():
        for i in range(len(dataset)):
            x, _ = dataset[i]
            out.append(int(model(x).expand(1, -1, -1).argmax(dim=2)))  # as in spoter/utils.py `evaluate`
    return np.array(out)


def predict_proba(model, dataset) -> np.ndarray:
    """Softmax over the class scores, one row per execution (its argmax is `predict`)."""
    model.train(False)
    with torch.no_grad():
        return np.stack([torch.softmax(model(dataset[i][0]).reshape(-1), 0).numpy() for i in range(len(dataset))])


IMPORTANCE_CHANS = [f"landmark_{i}_{a}_B" for i in BODY_MAP.values() for a in "xy"] + \
    [f"landmark_{i}_{a}_{p}" for p in ("LH", "RH") for i in HAND_MAP.values() for a in "xy"]


def dataset_from(rows: pd.DataFrame) -> CzechSLRDataset:
    with tempfile.TemporaryDirectory() as tmp:
        rows.to_csv(os.path.join(tmp, "set.csv"), index=False)
        return CzechSLRDataset(os.path.join(tmp, "set.csv"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True, help="Per-frame landmark table, image coordinates, native length.")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--split", choices=["loso", "8020"], required=True)
    parser.add_argument("--subject", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--hidden-dim", type=int, default=108)
    parser.add_argument("--gaussian-std", type=float, default=0.001)
    parser.add_argument("--shuffle-labels", action="store_true")
    parser.add_argument("--threads", type=int, default=3)
    parser.add_argument("--save-probs", action="store_true", help="Store test-set class probabilities and execution keys (fusion).")
    parser.add_argument("--save-weights", default=None, help="Directory for the final model's state_dict.")
    parser.add_argument("--importance-repeats", type=int, default=0,
                        help="> 0: region-level permutation importance on the test set (docs/SEQUENCE_IMPORTANCE.md).")
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.set_num_threads(args.threads)
    g = torch.Generator()
    g.manual_seed(args.seed)

    data = pd.read_csv(args.input_csv)
    rows, keys = to_spoter_rows(data)
    y, subjects = keys.label.to_numpy(), keys.subject.to_numpy()
    if args.split == "loso":
        tr, te = np.where(subjects != args.subject)[0], np.where(subjects == args.subject)[0]
        assert args.subject not in set(subjects[tr]), "held-out signer in training"
    else:
        tr, te = train_test_split(np.arange(len(y)), test_size=0.2, stratify=y, random_state=args.seed)
    assert not set(tr) & set(te), "train/test overlap"
    train_rows = rows.iloc[tr].copy()
    if args.shuffle_labels:
        train_rows["labels"] = np.random.default_rng(args.seed).permutation(train_rows["labels"].to_numpy())

    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        train_rows.to_csv(os.path.join(tmp, "train.csv"), index=False)
        rows.iloc[te].to_csv(os.path.join(tmp, "test.csv"), index=False)
        train_set = CzechSLRDataset(os.path.join(tmp, "train.csv"), transform=GaussianNoise(0, args.gaussian_std), augmentations=True)
        train_eval_set = CzechSLRDataset(os.path.join(tmp, "train.csv"))
        test_set = CzechSLRDataset(os.path.join(tmp, "test.csv"))
    loader = torch.utils.data.DataLoader(train_set, shuffle=True, generator=g)

    model = SPOTER(num_classes=int(y.max()) + 1, hidden_dim=args.hidden_dim)
    model.train(True)
    loss_fn = nn.CrossEntropyLoss()
    opt = torch.optim.SGD(model.parameters(), lr=args.lr)
    history = []
    for epoch in range(args.epochs):
        loss, _, _, acc = train_epoch(model, loader, loss_fn, opt, torch.device("cpu"))
        history.append({"epoch": epoch + 1, "train_loss": loss.item() / len(loader), "train_acc_augmented": acc})
    pred = predict(model, test_set)
    pred_tr = predict(model, train_eval_set)
    probs = predict_proba(model, test_set) if args.save_probs else None
    if probs is not None:
        assert np.array_equal(probs.argmax(1), pred), "probabilities disagree with predictions"
    importance = None
    if args.importance_repeats:  # permute our table's columns, then SPOTER's own input conversion
        assert args.split == "loso", "importance is defined on the held-out signer"
        te_keys = [tuple(k) for k in keys.iloc[te].to_numpy()]
        by_key = {k: g.sort_index() for k, g in data.groupby(KEYS, sort=True)}
        seqs = [by_key[k][IMPORTANCE_CHANS].to_numpy(dtype=float) for k in te_keys]

        def predict_seqs(ss: list[np.ndarray]) -> np.ndarray:
            frame = pd.concat([pd.DataFrame(s, columns=IMPORTANCE_CHANS).assign(label=k[0], subject=k[1], rep=k[2])
                               for s, k in zip(ss, te_keys)], ignore_index=True)
            r, kk = to_spoter_rows(frame)
            assert [tuple(x) for x in kk.to_numpy()] == te_keys, "execution order changed"
            return predict(model, dataset_from(r))

        assert np.array_equal(predict_seqs(seqs), pred), "rebuilt test set predicts differently"
        importance = grouped_importance_ragged(predict_seqs, seqs, y[te], IMPORTANCE_CHANS, args.importance_repeats, args.seed)
    y_tr_used = train_rows["labels"].to_numpy() - 1

    result = {
        "model": "SPOTER (official code, commit 0f909bf)", "split": args.split, "seed": args.seed,
        "subject": args.subject if args.split == "loso" else None, "shuffled_labels": args.shuffle_labels,
        "accuracy": accuracy_score(y[te], pred), "f1_weighted": f1_score(y[te], pred, average="weighted"),
        "f1_macro": f1_score(y[te], pred, average="macro"), "n_train": len(tr), "n_test": len(te),
        "train_accuracy": accuracy_score(y_tr_used, pred_tr), "n_params": sum(p.numel() for p in model.parameters()),
        "minutes": (time.time() - t0) / 60, "y_true": y[te].tolist(), "y_pred": pred.tolist(), "history": history,
        "config": {k: v for k, v in vars(args).items() if k != "output_dir"},
        **({"test_keys": keys.iloc[te].to_numpy().tolist(), "probs": probs.round(7).tolist()} if probs is not None else {}),
        **({"importance": importance} if importance is not None else {}),
    }
    os.makedirs(args.output_dir, exist_ok=True)
    name = f"spoter-{args.split}" + (f"-s{args.subject}" if args.split == "loso" else "") + f"-seed{args.seed}" + \
        ("-shuffled" if args.shuffle_labels else "")
    with open(os.path.join(args.output_dir, name + ".json"), "w") as f:
        json.dump(result, f)
    if args.save_weights:
        os.makedirs(args.save_weights, exist_ok=True)
        torch.save(model.state_dict(), os.path.join(args.save_weights, name + ".pt"))
    print(f"{name}: F1 weighted {result['f1_weighted']:.3f}, accuracy {result['accuracy']:.3f}, "
          f"train acc {result['train_accuracy']:.3f}, final loss {history[-1]['train_loss']:.3f}, {result['minutes']:.1f} min")


if __name__ == "__main__":
    main()
