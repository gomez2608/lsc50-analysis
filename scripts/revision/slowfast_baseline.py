"""SlowFast R50 baseline on LSC50 video (R2.7, R1.4).

Model: the official PyTorchVideo implementation and Kinetics-400 weights of
SlowFast R50, 8x8 (Feichtenhofer et al., ICCV 2019; `pytorchvideo.models.hub.slowfast_r50`,
pytorchvideo 0.1.5, Apache-2.0; weights SLOWFAST_8x8_R50.pyth, top-1 76.4 on
Kinetics-400). Loaded as published; only the final linear layer is replaced
(2304 -> 50 classes). All layers are fine-tuned, as for ViViT.

Input (the authors' Kinetics evaluation transform): 32 frames sampled uniformly
over the clip, short side resized to 256, centre crop 256 x 256, RGB scaled to
[0, 1], normalized with mean 0.45 / std 0.225; slow pathway = every 4th frame
(alpha = 4), fast pathway = all 32. No augmentation (in particular no horizontal
flip, which would swap the signing hands).

Training (fixed in advance, matching ViViT protocol B): all training signers,
30 epochs, final model kept, nothing chosen on test data; effective batch 48
(batch 4 x 12 accumulation); fp32. The authors publish no recipe for fine-tuning
on a small dataset, so the optimizer is our choice within their standard family:
SGD, momentum 0.9, weight decay 1e-4, learning rate 0.01 with cosine decay.
BatchNorm statistics are frozen at their Kinetics values (`--bn frozen`, the
default; fixed 2026-10-20 before any run, audit K5): with micro-batches of 4
clips, updating the running statistics is a known cause of poor fine-tuning
(the authors' Kinetics recipe uses 8 clips per GPU). The BatchNorm scale and
shift are still trained. cuDNN is left non-deterministic (deterministic 3D
convolutions are much slower on these GPUs); seeds fix data order and labels.

Revised recipe (2026-10-23, REVISION_LOG §5.20; fixed before any revised run): with the first recipe 8 of the
18 non-control runs never trained (5 diverged to NaN loss by epoch 3-7, 3 stayed at loss ln 50), depending only
on the seed. Added, as for ST-GCN (§5.21): a linear warm-up of the learning rate (`--warmup-epochs`, per
optimizer step) before the cosine decay, as in the authors' own SlowFast recipes; the learning rate chosen from a
pre-set grid on a held-out *training* signer (`--val-subject`); training accuracy recorded; a run whose training
loss becomes non-finite stops and is flagged `diverged` (reported, not dropped). Defaults reproduce the first runs.

Subcommands:
  build  decode all clips once into a uint8 memmap (N, 32, 256, 256, 3) + metadata CSV
  train  one run: --split loso --subject S | --split 8020; --seed; --shuffle-labels (control)

Usage:
    python scripts/revision/slowfast_baseline.py build --video-dir data/VIDEOS/COLOR_BODY --output slowfast_clips
    python scripts/revision/slowfast_baseline.py train --clips slowfast_clips --split loso --subject 0 --seed 0 --output-dir slowfast
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time

import av
import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from torch import nn

N_FRAMES, SIDE, ALPHA = 32, 256, 4
# (label, subject, rep) of the second copy of the 3 byte-identical pairs in LSC50 (P7; the .avi
# files are identical too, checked 2026-10-20). Dropped so video and landmark models use the
# same 997 executions (audit K6).
DUPLICATES = [(2, 1, 1), (8, 2, 1), (16, 2, 1)]
MEAN, STD = 0.45, 0.225


def decode(path: str) -> np.ndarray:
    """32 uniformly sampled frames, short side 256, centre crop 256 -> uint8 (32, 256, 256, 3)."""
    with av.open(path) as c:
        frames = [f.to_ndarray(format="rgb24") for f in c.decode(video=0)]
    idx = np.linspace(0, len(frames) - 1, N_FRAMES).round().astype(int)
    out = []
    for i in idx:
        f = torch.from_numpy(frames[i]).permute(2, 0, 1)[None].float()
        h, w = f.shape[-2:]
        scale = SIDE / min(h, w)
        f = torch.nn.functional.interpolate(f, size=(round(h * scale), round(w * scale)), mode="bilinear", align_corners=False)
        h, w = f.shape[-2:]
        top, left = (h - SIDE) // 2, (w - SIDE) // 2
        out.append(f[0, :, top:top + SIDE, left:left + SIDE].round().clamp(0, 255).byte().permute(1, 2, 0).numpy())
    return np.stack(out)


def build(args) -> None:
    files = sorted(f for f in os.listdir(args.video_dir) if f.lower().endswith(".avi"))
    os.makedirs(args.output, exist_ok=True)
    mm = np.lib.format.open_memmap(os.path.join(args.output, "frames.npy"), mode="w+", dtype=np.uint8,
                                   shape=(len(files), N_FRAMES, SIDE, SIDE, 3))
    meta = []
    for k, name in enumerate(files):
        mm[k] = decode(os.path.join(args.video_dir, name))
        label, subject, rep = (int(t) for t in os.path.splitext(name)[0].split("_")[:3])
        meta.append({"file": name, "label": label, "subject": subject, "rep": rep})
        if k % 100 == 0:
            print(f"{k}/{len(files)}", flush=True)
    mm.flush()
    pd.DataFrame(meta).to_csv(os.path.join(args.output, "meta.csv"), index=False)
    print(f"built {len(files)} clips -> {args.output}")


def to_pathways(batch_uint8: torch.Tensor) -> list[torch.Tensor]:
    """(B, T, H, W, 3) uint8 -> [slow (B, 3, T/alpha, H, W), fast (B, 3, T, H, W)] normalized float."""
    x = batch_uint8.permute(0, 4, 1, 2, 3).float().div_(255).sub_(MEAN).div_(STD)
    slow = x.index_select(2, torch.linspace(0, x.shape[2] - 1, x.shape[2] // ALPHA).long().to(x.device))
    return [slow, x]


def train(args) -> None:
    from pytorchvideo.models import hub
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)
    frames = np.load(os.path.join(args.clips, "frames.npy"), mmap_mode="r")
    meta = pd.read_csv(os.path.join(args.clips, "meta.csv"))
    keep = np.ones(len(meta), bool)
    if not args.keep_duplicates:
        for lab, sub, r in DUPLICATES:
            dup = np.where((meta.label == lab) & (meta.subject == sub) & (meta.rep == r))[0]
            orig = np.where((meta.label == lab) & (meta.subject == sub) & (meta.rep == r - 1))[0]
            assert len(dup) == 1 and len(orig) == 1 and np.array_equal(frames[dup[0]], frames[orig[0]]), f"not a duplicate: {lab, sub, r}"
            keep[dup[0]] = False
    rows = np.where(keep)[0]  # indices into the clip table
    meta = meta.iloc[rows].reset_index(drop=True)
    y, subjects = meta.label.to_numpy(), meta.subject.to_numpy()
    if args.split == "loso" and args.val_subject is not None:
        # selection: the test signer is not loaded; train on the other 3, score on the validation signer
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
    y_train = y.copy()
    if args.shuffle_labels:
        y_train[tr] = np.random.default_rng(args.seed).permutation(y[tr])

    dev = args.device
    model = hub.slowfast_r50(pretrained=True)
    model.blocks[-1].proj = nn.Linear(model.blocks[-1].proj.in_features, int(y.max()) + 1)
    model.to(dev)
    opt = torch.optim.SGD(model.parameters(), lr=args.lr, momentum=0.9, weight_decay=1e-4)
    steps_per_epoch = math.ceil(len(tr) / (args.batch_size * args.accumulation))
    steps = args.epochs * steps_per_epoch
    if args.warmup_epochs:
        warm = args.warmup_epochs * steps_per_epoch
        sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda i: (i + 1) / warm if i < warm else
                                                  0.5 * (1 + math.cos(math.pi * (i - warm) / (steps - warm))))
    else:
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=steps)
    loss_fn = nn.CrossEntropyLoss()
    gen = torch.Generator().manual_seed(args.seed)
    history, t0, diverged = [], time.time(), False
    def set_train_mode() -> None:
        model.train()
        if args.bn == "frozen":
            for m in model.modules():
                if isinstance(m, nn.modules.batchnorm._BatchNorm):
                    m.eval()

    for epoch in range(args.epochs):
        set_train_mode()
        perm = tr[torch.randperm(len(tr), generator=gen).numpy()]
        total, opt_steps = 0.0, 0
        for k in range(0, len(perm), args.batch_size):
            idx = np.sort(perm[k:k + args.batch_size])
            xb = to_pathways(torch.from_numpy(np.ascontiguousarray(frames[rows[idx]])).to(dev))
            loss = loss_fn(model(xb), torch.tensor(y_train[idx], device=dev))
            (loss / args.accumulation).backward()
            total += loss.item() * len(idx)
            if (k // args.batch_size + 1) % args.accumulation == 0 or k + args.batch_size >= len(perm):
                opt.step()
                opt.zero_grad()
                sched.step()
                opt_steps += 1
        history.append({"epoch": epoch + 1, "train_loss": total / len(tr), "lr": sched.get_last_lr()[0]})
        print(f"epoch {epoch + 1}: train loss {history[-1]['train_loss']:.4f} ({(time.time() - t0) / 60:.1f} min)", flush=True)
        if args.stop_on_nan and not math.isfinite(history[-1]["train_loss"]):
            diverged = True
            print("training loss not finite: stopping (run flagged as diverged)", flush=True)
            break
    model.eval()

    def predict(ix: np.ndarray) -> np.ndarray:
        out = []
        with torch.no_grad():
            for k in range(0, len(ix), args.batch_size):
                idx = ix[k:k + args.batch_size]
                out.append(model(to_pathways(torch.from_numpy(np.ascontiguousarray(frames[rows[idx]])).to(dev))).argmax(1).cpu())
        return torch.cat(out).numpy()

    if args.save_probs:
        with torch.no_grad():
            probs = torch.cat([torch.softmax(model(to_pathways(torch.from_numpy(np.ascontiguousarray(
                frames[rows[te[k:k + args.batch_size]]])).to(dev))), 1).cpu() for k in range(0, len(te), args.batch_size)]).numpy()
        pred = probs.argmax(1)
    else:
        pred = predict(te)
    train_accuracy = accuracy_score(y_train[tr], predict(tr)) if args.train_accuracy else None
    result = {
        "model": "SlowFast R50 8x8 (PyTorchVideo, Kinetics-400 pretrained)", "split": args.split,
        "subject": args.subject if args.split == "loso" else None, "seed": args.seed, "shuffled_labels": args.shuffle_labels,
        "val_subject": args.val_subject, "diverged": diverged, "train_accuracy": train_accuracy,
        "accuracy": accuracy_score(y[te], pred), "f1_weighted": f1_score(y[te], pred, average="weighted"),
        "f1_macro": f1_score(y[te], pred, average="macro"), "n_train": len(tr), "n_test": len(te),
        "n_params": sum(p.numel() for p in model.parameters()), "minutes": (time.time() - t0) / 60,
        "y_true": y[te].tolist(), "y_pred": pred.tolist(), "history": history,
        "config": {k: v for k, v in vars(args).items() if k not in ("output_dir", "func")},
        **({"test_keys": meta.iloc[te][["label", "subject", "rep"]].to_numpy().tolist(), "probs": probs.round(7).tolist()}
           if args.save_probs else {}),
    }
    os.makedirs(args.output_dir, exist_ok=True)
    name = f"slowfast-{args.split}" + (f"-s{args.subject}" if args.split == "loso" else "") + f"-seed{args.seed}" + \
        ("-shuffled" if args.shuffle_labels else "") + (f"-val{args.val_subject}" if args.val_subject is not None else "") + \
        (f"-{args.tag}" if args.tag else "")
    with open(os.path.join(args.output_dir, name + ".json"), "w") as f:
        json.dump(result, f)
    if args.save_weights:
        os.makedirs(args.save_weights, exist_ok=True)
        torch.save(model.state_dict(), os.path.join(args.save_weights, name + ".pt"))
    print(f"{name}: F1 weighted {result['f1_weighted']:.3f}, accuracy {result['accuracy']:.3f}, {result['minutes']:.0f} min")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--video-dir", required=True)
    b.add_argument("--output", required=True)
    t = sub.add_parser("train")
    t.add_argument("--clips", required=True)
    t.add_argument("--output-dir", required=True)
    t.add_argument("--split", choices=["loso", "8020"], required=True)
    t.add_argument("--subject", type=int, default=0)
    t.add_argument("--seed", type=int, default=0)
    t.add_argument("--epochs", type=int, default=30)
    t.add_argument("--batch-size", type=int, default=4)
    t.add_argument("--accumulation", type=int, default=12)
    t.add_argument("--lr", type=float, default=0.01)
    t.add_argument("--shuffle-labels", action="store_true")
    t.add_argument("--device", default="cuda")
    t.add_argument("--keep-duplicates", action="store_true", help="Keep the 3 duplicate executions (P7).")
    t.add_argument("--bn", choices=["frozen", "train"], default="frozen",
                   help="frozen: keep the pretrained BatchNorm running statistics (scale/shift still trained).")
    t.add_argument("--warmup-epochs", type=int, default=0, help="Linear warm-up (per optimizer step), then cosine.")
    t.add_argument("--val-subject", type=int, default=None,
                   help="LOSO selection: drop the test signer, train on the other 3, score on this training signer.")
    t.add_argument("--stop-on-nan", action="store_true", help="Stop when the epoch loss is not finite; flag the run.")
    t.add_argument("--train-accuracy", action="store_true", help="Also score the final model on its training clips.")
    t.add_argument("--tag", default="", help="Suffix for the output name (e.g. lr0.003).")
    t.add_argument("--save-probs", action="store_true", help="Store test-set class probabilities and execution keys (fusion).")
    t.add_argument("--save-weights", default=None, help="Directory for the final model's state_dict.")
    args = parser.parse_args()
    build(args) if args.cmd == "build" else train(args)


if __name__ == "__main__":
    main()
