"""Audit of the original ViViT results and datasets (P3, P13, P14; REVISION_LOG §5.11, §7, §7.8).

Read-only checks on the original workspace (`~/LSC/MISC` on the server):

- ``metrics``: weighted / macro F1 and accuracy per held-out subject from the
  stored predictions (`confusion_matrix_subject_{i}.pkl`), and test accuracy at
  epochs 5, 10, 20 and the last epoch from the training logs (`logs_s{i}.csv`).
- ``rows``: row and per-label counts of saved Hugging Face datasets.
- ``duplicates``: MD5 of every clip's pixel values in a train and a test
  dataset; reports distinct clips, copies, and test clips also in train.
- ``weights``: compares a fine-tuned checkpoint with the pretrained ViViT
  (trainable parameters; how many tensors changed).

Usage (from ~/LSC/MISC):
    python original_vivit_audit.py metrics
    python original_vivit_audit.py rows train_dataset_v2 test_dataset_v2 train_dataset_v2_subject_0
    python original_vivit_audit.py duplicates train_dataset_v2 test_dataset_v2
    python original_vivit_audit.py weights vivit-finetuned-s0
"""

from __future__ import annotations

import argparse
import collections
import glob
import hashlib
import pickle

import numpy as np
import pandas as pd


def _batches(d: str):
    import pyarrow as pa
    for f in sorted(glob.glob(f"{d}/data-*.arrow")):
        with pa.memory_map(f) as src:
            yield from pa.ipc.open_stream(src)


def metrics(_args) -> None:
    from sklearn.metrics import accuracy_score, f1_score
    rows = []
    for i in range(5):
        r = pickle.load(open(f"confusion_matrix_subject_{i}.pkl", "rb"))
        yt, yp = np.array(r["real_labels"]), np.array(r["inferences"])
        rows.append((accuracy_score(yt, yp), f1_score(yt, yp, average="weighted"), f1_score(yt, yp, average="macro")))
        print(f"subject {i}: n={len(yt)} accuracy {rows[-1][0]:.3f} F1 weighted {rows[-1][1]:.3f} F1 macro {rows[-1][2]:.3f}")
    a = np.array(rows)
    print(f"mean: accuracy {a[:, 0].mean():.2f} ± {a[:, 0].std():.2f} | F1 weighted {a[:, 1].mean():.2f} ± {a[:, 1].std():.2f}")
    for i in range(5):
        e = pd.read_csv(f"logs_s{i}.csv").dropna(subset=["eval_accuracy"])
        acc = [round(e.eval_accuracy.iloc[min(k, len(e) - 1)], 2) for k in (4, 9, 19, len(e) - 1)]
        print(f"logs_s{i}: test accuracy at epochs 5, 10, 20, last = {acc}; best {e.eval_accuracy.max():.2f}")


def rows(args) -> None:
    for d in args.datasets:
        labels = [lab for b in _batches(d) for lab in b.column("labels").to_pylist()]
        counts = collections.Counter(labels)
        print(f"{d}: {len(labels)} rows, {len(counts)} labels, per label {min(counts.values())}-{max(counts.values())}")


def _hashes(d: str):
    import pyarrow as pa
    out = []
    for b in _batches(d):
        col = b.column("pixel_values")
        for i in range(b.num_rows):
            a = col.slice(i, 1)
            while pa.types.is_list(a.type) or pa.types.is_large_list(a.type) or pa.types.is_fixed_size_list(a.type):
                a = a.flatten()
            out.append(hashlib.md5(a.to_numpy(zero_copy_only=False).tobytes()).hexdigest())
    return out


def duplicates(args) -> None:
    tr, te = collections.Counter(_hashes(args.train)), collections.Counter(_hashes(args.test))
    print(f"train: {sum(tr.values())} rows, {len(tr)} distinct, copies per clip {sorted(collections.Counter(tr.values()).items())}")
    print(f"test: {sum(te.values())} rows, {len(te)} distinct, copies per clip {sorted(collections.Counter(te.values()).items())}")
    print(f"distinct test clips also in train: {sum(h in tr for h in te)} of {len(te)}")


def weights(args) -> None:
    import torch
    from transformers import VivitForVideoClassification as M
    base = M.from_pretrained("google/vivit-b-16x2-kinetics400")
    print("trainable after from_pretrained:", sum(p.numel() for p in base.parameters() if p.requires_grad),
          "of", sum(p.numel() for p in base.parameters()))
    ck = sorted(glob.glob(f"{args.run_dir}/checkpoint-*"), key=lambda x: int(x.rsplit("-", 1)[1]))
    ft = M.from_pretrained(ck[-1] if ck else args.run_dir)
    bs, fs = base.state_dict(), ft.state_dict()
    shared = [k for k in bs if k in fs and bs[k].shape == fs[k].shape]
    changed = [k for k in shared if not torch.allclose(bs[k].float(), fs[k].float())]
    print(f"{ck[-1] if ck else args.run_dir}: {len(changed)} of {len(shared)} shared tensors changed vs. pretrained")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("metrics")
    p = sub.add_parser("rows"); p.add_argument("datasets", nargs="+")
    p = sub.add_parser("duplicates"); p.add_argument("train"); p.add_argument("test")
    p = sub.add_parser("weights"); p.add_argument("run_dir")
    args = parser.parse_args()
    {"metrics": metrics, "rows": rows, "duplicates": duplicates, "weights": weights}[args.cmd](args)


if __name__ == "__main__":
    main()
