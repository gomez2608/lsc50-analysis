"""Pose-sequence baseline: transformer encoder (our implementation, following SPOTER) on landmark sequences (item 6, R1/R2 baselines).

Unlike the TSFEL / Chronos pipelines, the model sees the landmark *sequence*
directly. Input: per execution, F frames x 130 body-relative coordinates (65
points, x and y; `normalize_landmarks.py`), missing points set to 0, each
coordinate standardized with training-set statistics. Model: linear frame
embedding + learned positional embedding + learned class token, transformer
encoder (pre-norm), linear head on the class token.

Settings are fixed in advance (no tuning on test data, no validation split, no
alternatives tried; chosen once by us when the script was written, 7465bfc;
there is no further record of how): d_model 128, 3 layers, 4 heads, dropout 0.1, AdamW (lr 5e-4, weight decay 0.05), batch 32, 150
epochs, one-cycle schedule (`OneCycleLR`: 10% warm-up, then cosine decay),
cross-entropy with label smoothing 0.1, gradient-norm clipping at 1.0, final
model kept. Training-time augmentation per execution: rotation of all (x, y)
points by U(-10, 10) degrees and scaling by U(0.9, 1.1) about the coordinate
origin, then Gaussian noise (sd 0.02 in standardized units). In body-relative
coordinates the origin is the shoulder midpoint, so this is a rotation about
the body; in image coordinates (x and y each scaled to [0, 1] on a 1920 x 1080
frame) it is about the image corner on non-square axes, i.e. a shear plus a
translation rather than a rotation (audit K4; documented, not changed, since
the runs are done and the model is exploratory).

Splits as elsewhere: 80/20 stratified by sign (one split per seed) and
leave-one-signer-out. Writes one JSON per run (metrics, predictions, per-epoch
training loss) and a summary CSV.

Usage:
    python scripts/revision/pose_transformer.py --input-csv WORK/bodynorm/general_db_bodynorm.csv \\
        --output-dir pose --split loso --subject 0 --seed 0
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from torch import nn

from sequence_importance import GROUPINGS, grouped_importance

KEYS = ["label", "subject", "rep"]


def load_sequences(path: str):
    data = pd.read_csv(path)
    chans = [c for c in data.columns if c.startswith("landmark_")]
    seqs, meta = [], []
    for key, g in data.groupby(KEYS, sort=True):
        seqs.append(g[chans].to_numpy(dtype=np.float32))
        meta.append(key)
    lengths = {len(s) for s in seqs}
    if len(lengths) != 1:
        raise ValueError(f"Expected equal-length sequences, got lengths {sorted(lengths)[:5]}...")
    X = np.nan_to_num(np.stack(seqs))  # (N, F, C)
    meta = pd.DataFrame(meta, columns=KEYS)
    return X, meta["label"].to_numpy(), meta["subject"].to_numpy(), chans


class PoseTransformer(nn.Module):
    def __init__(self, n_in: int, n_frames: int, n_classes: int, d: int = 128, heads: int = 4, layers: int = 3, dropout: float = 0.1,
                 pooling: str = "cls"):
        super().__init__()
        self.pooling = pooling
        self.embed = nn.Linear(n_in, d)
        self.cls = nn.Parameter(torch.zeros(1, 1, d))
        self.pos = nn.Parameter(torch.zeros(1, n_frames + 1, d))
        nn.init.trunc_normal_(self.pos, std=0.02)
        nn.init.trunc_normal_(self.cls, std=0.02)
        layer = nn.TransformerEncoderLayer(d, heads, dim_feedforward=4 * d, dropout=dropout, batch_first=True, norm_first=True)
        self.encoder = nn.TransformerEncoder(layer, layers)
        self.norm = nn.LayerNorm(d)
        self.head = nn.Linear(d, n_classes)

    def forward(self, x):
        h = self.embed(x)
        h = torch.cat([self.cls.expand(len(h), -1, -1), h], dim=1) + self.pos
        h = self.encoder(h)
        pooled = h[:, 0] if self.pooling == "cls" else h[:, 1:].mean(1)
        return self.head(self.norm(pooled))


def augment(x: torch.Tensor, xy_idx: tuple[np.ndarray, np.ndarray], mean, std, gen: torch.Generator,
            centre_idx: tuple[list[int], list[int]] | None = None, frame_size: tuple[float, float] | None = None) -> torch.Tensor:
    """Rotate and scale the raw (x, y) points, then re-standardize and add noise.

    Default: about the coordinate origin (the shoulder midpoint for body-relative input).
    With `centre_idx` (x and y columns of pose 11 and 12) the rotation and scaling are about each
    execution's mean shoulder midpoint, and with `frame_size` the points are first converted to
    pixels so that the rotation is a rotation on the non-square frame (audit K4).
    """
    raw = x * std + mean
    b = len(raw)
    sx, sy = frame_size if frame_size else (1.0, 1.0)
    if centre_idx is not None:
        cx = raw[:, :, centre_idx[0]].mean(dim=(1, 2))[:, None, None] * sx
        cy = raw[:, :, centre_idx[1]].mean(dim=(1, 2))[:, None, None] * sy
    else:
        cx = cy = torch.zeros(b, 1, 1)
    theta = (torch.rand(b, generator=gen) * 20 - 10) * math.pi / 180
    scale = torch.rand(b, generator=gen) * 0.2 + 0.9
    cos, sin = (torch.cos(theta) * scale)[:, None, None], (torch.sin(theta) * scale)[:, None, None]
    px, py = raw[:, :, xy_idx[0]] * sx - cx, raw[:, :, xy_idx[1]] * sy - cy
    raw = raw.clone()
    raw[:, :, xy_idx[0]] = (cos * px - sin * py + cx) / sx
    raw[:, :, xy_idx[1]] = (sin * px + cos * py + cy) / sy
    out = (raw - mean) / std
    return out + 0.02 * torch.randn(out.shape, generator=gen)


def run(args) -> dict:
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    torch.set_num_threads(args.threads)
    X, y, subjects, chans = load_sequences(args.input_csv)
    if args.channels != "all":  # input ablation: hand landmarks only or body (pose) landmarks only
        keep = [i for i, c in enumerate(chans) if (c.endswith(("_LH", "_RH")) if args.channels == "hands" else c.endswith("_B"))]
        X, chans = X[:, :, keep], [chans[i] for i in keep]
    if args.split == "loso":
        tr, te = np.where(subjects != args.subject)[0], np.where(subjects == args.subject)[0]
    elif args.split == "subjects":  # train on --train-subjects, score on --eval-subject (nested selection, learning curve)
        assert args.eval_subject not in args.train_subjects, "evaluation signer in training"
        tr = np.where(np.isin(subjects, args.train_subjects))[0]
        te = np.where(subjects == args.eval_subject)[0]
    else:
        tr, te = train_test_split(np.arange(len(y)), test_size=0.2, stratify=y, random_state=args.seed)
    assert not set(tr) & set(te), "train/test overlap"
    if args.split == "loso":
        assert args.subject not in set(subjects[tr]), "held-out signer in training"
    if args.split == "subjects":
        assert args.eval_subject not in set(subjects[tr]) and set(subjects[te]) == {args.eval_subject}
        if args.exclude_subject is not None:
            assert args.exclude_subject not in set(subjects[tr]) | set(subjects[te]), "excluded (outer test) signer used"
    y_train = y.copy()
    if args.shuffle_labels:  # control: permute training labels only; test labels untouched
        y_train[tr] = np.random.default_rng(args.seed).permutation(y[tr])
    mean = torch.tensor(X[tr].reshape(-1, X.shape[2]).mean(0))
    std = torch.tensor(X[tr].reshape(-1, X.shape[2]).std(0) + 1e-6)
    Xt = (torch.tensor(X) - mean) / std
    yt = torch.tensor(y_train, dtype=torch.long)
    # pair each x column with its y column (same point and part)
    xs = [i for i, c in enumerate(chans) if "_x_" in c]
    ys = [chans.index(chans[i].replace("_x_", "_y_")) for i in xs]
    xy_idx = (np.array(xs), np.array(ys))
    centre_idx = None
    if args.aug_centre == "shoulders":
        centre_idx = ([chans.index("landmark_11_x_B"), chans.index("landmark_12_x_B")],
                      [chans.index("landmark_11_y_B"), chans.index("landmark_12_y_B")])
    frame_size = tuple(args.frame_size) if args.frame_size else None

    n_classes = int(y.max()) + 1
    model = PoseTransformer(X.shape[2], X.shape[1], n_classes, d=args.d_model, layers=args.layers, pooling=args.pooling)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    steps_per_epoch = math.ceil(len(tr) / args.batch_size)
    if args.schedule == "onecycle":
        sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=args.lr, total_steps=args.epochs * steps_per_epoch,
                                                    pct_start=0.1, anneal_strategy="cos")
    else:  # constant learning rate
        sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda _: 1.0)
    gen = torch.Generator().manual_seed(args.seed)
    loss_fn = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)
    history = []
    t0 = time.time()
    for epoch in range(args.epochs):
        model.train()
        perm = torch.tensor(tr)[torch.randperm(len(tr), generator=gen)]
        total = 0.0
        for k in range(0, len(perm), args.batch_size):
            idx = perm[k:k + args.batch_size]
            xb = augment(Xt[idx], xy_idx, mean, std, gen, centre_idx, frame_size) if args.augment else Xt[idx]
            loss = loss_fn(model(xb), yt[idx])
            opt.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            sched.step()
            total += loss.item() * len(idx)
        history.append({"epoch": epoch + 1, "train_loss": total / len(tr)})
    model.eval()
    with torch.no_grad():
        pred = model(Xt[te]).argmax(1).numpy()
        pred_tr = model(Xt[tr]).argmax(1).numpy()
    importance = None
    if args.importance_repeats:  # grouped permutation importance on the test set (docs/SEQUENCE_IMPORTANCE.md)
        def predict(Xs):
            with torch.no_grad():
                return model(torch.from_numpy(Xs)).argmax(1).numpy()
        importance = grouped_importance(predict, Xt[te].numpy(), y[te], chans, args.importance_repeats, args.seed,
                                      args.importance_groupings)
    return {
        "split": args.split, "seed": args.seed,
        "subject": args.subject if args.split == "loso" else (args.eval_subject if args.split == "subjects" else None),
        "train_subjects": sorted(int(v) for v in set(subjects[tr])), "train_accuracy": accuracy_score(y_train[tr], pred_tr),
        "shuffled_labels": args.shuffle_labels,
        "accuracy": accuracy_score(y[te], pred), "f1_weighted": f1_score(y[te], pred, average="weighted"),
        "f1_macro": f1_score(y[te], pred, average="macro"), "n_train": len(tr), "n_test": len(te),
        "n_frames": X.shape[1], "n_params": sum(p.numel() for p in model.parameters()),
        "minutes": (time.time() - t0) / 60, "y_true": y[te].tolist(), "y_pred": pred.tolist(),
        "history": history, "config": {k: v for k, v in vars(args).items() if k != "output_dir"},
        **({"importance": importance} if importance is not None else {}),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--split", choices=["loso", "8020", "subjects"], required=True)
    parser.add_argument("--train-subjects", type=int, nargs="+", default=None, help="--split subjects: training signers.")
    parser.add_argument("--eval-subject", type=int, default=None, help="--split subjects: signer scored.")
    parser.add_argument("--exclude-subject", type=int, default=None, help="--split subjects: outer test signer, asserted unused.")
    parser.add_argument("--channels", choices=["all", "hands", "body"], default="all")
    parser.add_argument("--pooling", choices=["cls", "mean"], default="cls")
    parser.add_argument("--schedule", choices=["onecycle", "constant"], default="onecycle")
    parser.add_argument("--label-smoothing", type=float, default=0.1)
    parser.add_argument("--aug-centre", choices=["origin", "shoulders"], default="origin")
    parser.add_argument("--frame-size", type=float, nargs=2, default=None, help="Width height: rotate in pixel units.")
    parser.add_argument("--name", default=None, help="Output file name (without .json); default from split/subject/seed.")
    parser.add_argument("--subject", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--epochs", type=int, default=150)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=5e-4)
    parser.add_argument("--weight-decay", type=float, default=0.05)
    parser.add_argument("--d-model", type=int, default=128)
    parser.add_argument("--layers", type=int, default=3)
    parser.add_argument("--no-augment", dest="augment", action="store_false")
    parser.add_argument("--shuffle-labels", action="store_true", help="Control: permute training labels.")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--importance-repeats", type=int, default=0,
                        help="> 0: grouped permutation importance on the test set with this many repeats.")
    parser.add_argument("--importance-groupings", nargs="+", choices=GROUPINGS, default=["region", "point"],
                        help="Groupings for the importance, evaluated in this order.")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    name = args.name or (f"pose-{args.split}" + (f"-s{args.subject}" if args.split == "loso" else "") + f"-seed{args.seed}"
                         + ("-shuffled" if args.shuffle_labels else ""))
    result = run(args)
    with open(os.path.join(args.output_dir, name + ".json"), "w") as f:
        json.dump(result, f)
    print(f"{name}: F1 weighted {result['f1_weighted']:.3f}, accuracy {result['accuracy']:.3f}, "
          f"final train loss {result['history'][-1]['train_loss']:.3f}, {result['minutes']:.1f} min, {result['n_params']} params")


if __name__ == "__main__":
    main()
