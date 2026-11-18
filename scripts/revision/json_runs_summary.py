"""One table of per-run JSON results (pose transformer, ST-GCN, SlowFast) and its summary (audit K7).

Each JSON (written by pose_transformer.py, stgcn_baseline.py or slowfast_baseline.py)
becomes one row: model/input tag, split, held-out signer, seed, shuffled flag, metrics,
training size, final training loss and, where recorded, training accuracy. The summary
gives, per tag, split and shuffled flag, the mean and SD (ddof 1) of weighted F1 over
runs; for LOSO also the per-signer mean over seeds and the mean over signers. The git
commit of this script is written beside the outputs (`<prefix>.commit.txt`).

Usage:
    python scripts/revision/json_runs_summary.py --runs "Pose transformer, image=WORK/pose/image/*.json" \\
        --runs "Pose transformer, image, control=WORK/pose_control/image/*.json" --output-prefix pose_transformer_runs
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess

import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", action="append", required=True, help="TAG=PATTERN")
    parser.add_argument("--output-prefix", required=True)
    args = parser.parse_args()
    rows = []
    for spec in args.runs:
        tag, pattern = spec.split("=", 1)
        for path in sorted(glob.glob(pattern)):
            r = json.load(open(path))
            if r.get("val_subject") is not None:  # selection runs are scored on a training signer
                continue
            hist = r.get("history") or []
            rows.append({"tag": tag, "file": os.path.basename(path), "split": r["split"], "subject": r.get("subject"),
                         "seed": r["seed"], "shuffled_labels": bool(r.get("shuffled_labels")),
                         "f1_weighted": r["f1_weighted"], "f1_macro": r["f1_macro"], "accuracy": r["accuracy"],
                         "n_train": r["n_train"], "n_test": r["n_test"],
                         "final_train_loss": hist[-1]["train_loss"] if hist else np.nan,
                         "train_accuracy": r.get("train_accuracy", np.nan), "minutes": r.get("minutes", np.nan)})
    runs = pd.DataFrame(rows)
    runs.to_csv(f"{args.output_prefix}.csv", index=False)
    out = []
    for (tag, split, shuf), g in runs.groupby(["tag", "split", "shuffled_labels"], sort=False):
        row = {"tag": tag, "split": split, "shuffled_labels": shuf, "n_runs": len(g), "seeds": g.seed.nunique(),
               "f1_mean_over_runs": g.f1_weighted.mean(), "f1_sd_over_runs": g.f1_weighted.std(ddof=1),
               "final_train_loss_min": g.final_train_loss.min(), "final_train_loss_max": g.final_train_loss.max(),
               "train_accuracy_min": g.train_accuracy.min()}
        if split == "loso":
            per = g.groupby("subject").f1_weighted.mean()
            row.update({"f1_mean_over_signers": per.mean(), "f1_sd_over_signers": per.std(ddof=1),
                        **{f"V{int(s) + 1}": v for s, v in per.items()}})
        out.append(row)
    summary = pd.DataFrame(out)
    summary.to_csv(f"{args.output_prefix}_summary.csv", index=False)
    try:
        commit = subprocess.run(["git", "log", "--oneline", "-1"], capture_output=True, text=True,
                                cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()
    except OSError:
        commit = "unknown"
    with open(f"{args.output_prefix}.commit.txt", "w") as f:
        f.write(commit + "\n")
    print(summary.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
