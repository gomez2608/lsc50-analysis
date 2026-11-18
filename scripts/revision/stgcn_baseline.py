"""ST-GCN baseline on LSC50 landmark sequences (R2.7).

Model: the official ST-GCN implementation (Yan et al., AAAI 2018), vendored
unmodified in `third_party/st_gcn/` (commit 221c0e1). The only addition is the
LSC50 skeleton: the 65 MediaPipe points (left hand 0-20, right hand 0-20, pose
0-22) with the MediaPipe hand and pose connections, the two face clusters joined
to the nose, the nose joined to both shoulders, and each hand's wrist joined to
the matching pose wrist (left hand <-> pose 15, right hand <-> pose 16; checked
on the data: median 10-11 px apart). Centre node: pose 0 (nose). Partition
strategy "spatial", as in the paper.

Training: the authors' NTU recipe, fixed in advance (config/st_gcn/ntu-xsub/train.yaml
and processor/recognition.py): SGD, Nesterov momentum 0.9, base learning rate
0.1 multiplied by 0.1 at epochs 10 and 50, weight decay 1e-4, 80 epochs, batch
64, dropout 0.5, learnable edge importance. No augmentation (none in that
config). Final model kept; nothing is chosen on test data. These are the
defaults; on LSC50 they give only ~13 updates per epoch (~1,000 in total vs.
~50,000 on NTU) and several runs do not fit (REVISION_LOG §5.19, audit M3).

Revised recipe (fixed 2026-10-20, run by run_stgcn_v2.sh): batch 16, 200 epochs
(~10,000 updates), learning-rate drops x0.1 at the same fractions of training
as NTU (epochs 25 and 125), 5-epoch linear warm-up; base learning rate chosen
from {0.05, 0.025, 0.01} on a held-out *training* signer (--val-subject; the
test signer is not loaded into training or evaluation in that mode).

Input: per execution (C=2: x, y) x T frames x V=65 x M=1; same tables, splits,
seeds, overlap assertions and shuffled-label control as the pose transformer.

Usage:
    python scripts/revision/stgcn_baseline.py --input-csv WORK/general_db.csv --output-dir stgcn/image \\
        --split loso --subject 0 --seed 0
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from torch import nn

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "third_party" / "st_gcn"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import net.st_gcn as st_gcn_module  # noqa: E402  (official ST-GCN)
from net.st_gcn import Model  # noqa: E402
from net.utils import graph as stgcn_graph  # noqa: E402
from pose_transformer import load_sequences  # noqa: E402
from sequence_importance import GROUPINGS, grouped_importance  # noqa: E402

HAND = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
        (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]
POSE = [(0, 1), (1, 2), (2, 3), (3, 7), (0, 4), (4, 5), (5, 6), (6, 8), (9, 10), (0, 9), (0, 10),
        (0, 11), (0, 12), (11, 12), (11, 13), (13, 15), (15, 17), (15, 19), (15, 21), (17, 19),
        (12, 14), (14, 16), (16, 18), (16, 20), (16, 22), (18, 20)]


class LSC50Graph(stgcn_graph.Graph):
    """ST-GCN graph with the LSC50 MediaPipe layout ('lsc50'); other layouts unchanged."""

    def get_edge(self, layout):
        if layout != "lsc50":
            return super().get_edge(layout)
        lh, rh, body = 0, 21, 42  # node offsets, matching the column order of the landmark tables
        self.num_node = 65
        links = [(lh + i, lh + j) for i, j in HAND] + [(rh + i, rh + j) for i, j in HAND]
        links += [(body + i, body + j) for i, j in POSE]
        links += [(lh + 0, body + 15), (rh + 0, body + 16)]
        self.edge = [(i, i) for i in range(self.num_node)] + links
        self.center = body + 0


# st_gcn.py imported Graph by name, so the layout is registered there (the vendored files stay unchanged).
st_gcn_module.Graph = LSC50Graph


def node_order(chans: list[str]) -> list[tuple[int, int]]:
    """(x column, y column) per node, in the order LH 0-20, RH 0-20, B 0-22."""
    order = []
    for part, n in (("LH", 21), ("RH", 21), ("B", 23)):
        for i in range(n):
            order.append((chans.index(f"landmark_{i}_x_{part}"), chans.index(f"landmark_{i}_y_{part}")))
    return order


def to_graph(X: np.ndarray, order: list[tuple[int, int]]) -> np.ndarray:
    """(N, T, C_flat) -> (N, 2, T, V, 1)."""
    return np.stack([np.stack([X[:, :, xi] for xi, _ in order], axis=-1),
                     np.stack([X[:, :, yi] for _, yi in order], axis=-1)], axis=1)[..., None].astype(np.float32)


def run(args) -> dict:
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    torch.set_num_threads(args.threads)
    X, y, subjects, chans = load_sequences(args.input_csv)  # (N, T, C_flat), missing -> 0
    order = node_order(chans)
    G = to_graph(X, order)

    if args.split == "loso" and args.val_subject is not None:
        # selection mode: the test signer is dropped entirely; validate on one training signer
        assert args.val_subject != args.subject, "validation signer must be a training signer"
        tr = np.where((subjects != args.subject) & (subjects != args.val_subject))[0]
        te = np.where(subjects == args.val_subject)[0]
    elif args.split == "loso":
        tr, te = np.where(subjects != args.subject)[0], np.where(subjects == args.subject)[0]
    else:
        tr, te = train_test_split(np.arange(len(y)), test_size=0.2, stratify=y, random_state=args.seed)
    assert not set(tr) & set(te), "train/test overlap"
    if args.split == "loso":
        assert args.subject not in set(subjects[tr]), "held-out signer in training"
        if args.val_subject is not None:
            assert args.subject not in set(subjects[te]), "test signer in validation"
    y_train = y.copy()
    if args.shuffle_labels:
        y_train[tr] = np.random.default_rng(args.seed).permutation(y[tr])

    dev = torch.device(args.device)
    Gt, yt = torch.tensor(G).to(dev), torch.tensor(y_train, dtype=torch.long).to(dev)
    model = Model(in_channels=2, num_class=int(y.max()) + 1, graph_args={"layout": "lsc50", "strategy": "spatial"},
                  edge_importance_weighting=True, dropout=0.5).to(dev)
    opt = torch.optim.SGD(model.parameters(), lr=args.base_lr, momentum=0.9, nesterov=True, weight_decay=1e-4)
    loss_fn = nn.CrossEntropyLoss()
    gen = torch.Generator().manual_seed(args.seed)
    history, t0 = [], time.time()
    for epoch in range(args.epochs):
        lr = args.base_lr * 0.1 ** sum(epoch >= s for s in args.step)
        if epoch < args.warmup_epochs:
            lr *= (epoch + 1) / args.warmup_epochs
        for g in opt.param_groups:
            g["lr"] = lr
        model.train()
        perm = torch.tensor(tr)[torch.randperm(len(tr), generator=gen)].to(dev)
        total = 0.0
        for k in range(0, len(perm), args.batch_size):
            idx = perm[k:k + args.batch_size]
            if len(idx) < 2:  # BatchNorm needs more than one sample
                continue
            loss = loss_fn(model(Gt[idx]), yt[idx])
            opt.zero_grad()
            loss.backward()
            opt.step()
            total += loss.item() * len(idx)
        history.append({"epoch": epoch + 1, "lr": lr, "train_loss": total / len(tr)})
    model.eval()
    with torch.no_grad():
        pred = torch.cat([model(Gt[te][k:k + 64]) for k in range(0, len(te), 64)]).argmax(1).cpu().numpy()
        pred_tr = torch.cat([model(Gt[tr][k:k + 64]) for k in range(0, len(tr), 64)]).argmax(1).cpu().numpy()
    importance = None
    if args.importance_repeats:  # grouped permutation importance on the test set (docs/SEQUENCE_IMPORTANCE.md)
        def predict(Xs):
            Gs = torch.tensor(to_graph(Xs, order)).to(dev)
            with torch.no_grad():
                return torch.cat([model(Gs[k:k + 64]) for k in range(0, len(Gs), 64)]).argmax(1).cpu().numpy()
        importance = grouped_importance(predict, X[te], y[te], chans, args.importance_repeats, args.seed,
                                      args.importance_groupings)
    return {
        "model": "ST-GCN (official, Yan et al. 2018)", "split": args.split,
        "subject": args.subject if args.split == "loso" else None, "seed": args.seed, "shuffled_labels": args.shuffle_labels,
        "accuracy": accuracy_score(y[te], pred), "f1_weighted": f1_score(y[te], pred, average="weighted"),
        "f1_macro": f1_score(y[te], pred, average="macro"), "n_train": len(tr), "n_test": len(te),
        "val_subject": args.val_subject, "train_accuracy": accuracy_score(y_train[tr], pred_tr),
        "n_frames": int(G.shape[2]), "n_params": sum(p.numel() for p in model.parameters()),
        "minutes": (time.time() - t0) / 60, "y_true": y[te].tolist(), "y_pred": pred.tolist(),
        "history": history, "config": {k: v for k, v in vars(args).items() if k != "output_dir"},
        **({"importance": importance} if importance is not None else {}),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--input-csv", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--split", choices=["loso", "8020"], required=True)
    parser.add_argument("--subject", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--step", type=int, nargs="+", default=[10, 50])
    parser.add_argument("--base-lr", type=float, default=0.1)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--shuffle-labels", action="store_true")
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--warmup-epochs", type=int, default=0)
    parser.add_argument("--val-subject", type=int, default=None,
                        help="Selection mode: train without --subject and this signer, score on this signer only.")
    parser.add_argument("--tag", default="", help="Suffix for the output name (e.g. the learning rate).")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--importance-repeats", type=int, default=0,
                        help="> 0: grouped permutation importance on the test set with this many repeats.")
    parser.add_argument("--importance-groupings", nargs="+", choices=GROUPINGS, default=["region", "point"],
                        help="Groupings for the importance, evaluated in this order.")
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    name = f"stgcn-{args.split}" + (f"-s{args.subject}" if args.split == "loso" else "") + f"-seed{args.seed}" + \
        ("-shuffled" if args.shuffle_labels else "") + \
        (f"-val{args.val_subject}" if args.val_subject is not None else "") + (f"-{args.tag}" if args.tag else "")
    result = run(args)
    with open(os.path.join(args.output_dir, name + ".json"), "w") as f:
        json.dump(result, f)
    print(f"{name}: F1 weighted {result['f1_weighted']:.3f}, accuracy {result['accuracy']:.3f}, "
          f"final train loss {result['history'][-1]['train_loss']:.3f}, train acc {result['train_accuracy']:.3f}, {result['minutes']:.1f} min, {result['n_params']} params")


if __name__ == "__main__":
    main()
