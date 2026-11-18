"""Summary tables of the pose transformer robustness study (docs/POSE_TRANSFORMER_STUDY.md).

Reads the per-run JSON files under the study folder and the default runs, and writes:
- `s1_nested.csv`: selected configuration per outer fold and the nested result per signer (seeds averaged);
- `s2_sensitivity.csv`: new-signer F1 of each of the 18 configurations (seed 0) per signer, plus the
  distribution across configurations (descriptive only, not used for any choice);
- `s3_s4_variants.csv`: each ablation and frame-count variant: per-signer F1 (seeds averaged), mean over
  signers, SD over seeds, minimum training accuracy;
- `s5_learning_curve.csv`: new-signer F1 against the number of training signers k (mean over subsets,
  then over held-out signers; k = 4 from the default runs, seed 0).
Paired comparisons with Holm correction are made by signer_ci.py (see run_pose_study_stats.sh).

Usage:
    python scripts/revision/pose_study_summary.py --study-dir WORK/pose_study --default-dir WORK/pose/bodynorm \\
        --default-image-dir WORK/pose/image --output-dir pose_study_summary
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np
import pandas as pd


def load(pattern: str) -> pd.DataFrame:
    rows = []
    for path in sorted(glob.glob(pattern, recursive=True)):
        r = json.load(open(path))
        if r.get("shuffled_labels"):
            continue
        c = r["config"]
        rows.append({"file": os.path.basename(path), "subject": r["subject"], "seed": r["seed"], "f1": r["f1_weighted"],
                     "train_acc": r.get("train_accuracy", np.nan), "train_subjects": tuple(r.get("train_subjects") or ()),
                     "d_model": c["d_model"], "layers": c["layers"], "lr": c["lr"], "split": r["split"],
                     "n_params": r["n_params"], "final_loss": r["history"][-1]["train_loss"]})
    return pd.DataFrame(rows)


def signer_summary(t: pd.DataFrame) -> dict:
    per = t.groupby("subject").f1.mean()
    seed_means = t.groupby("seed").f1.mean()
    half = 2.776 * per.std(ddof=1) / np.sqrt(len(per)) if len(per) > 1 else np.nan  # t(0.975, df 4)
    return {"mean_over_signers": per.mean(), "ci_t_low": per.mean() - half, "ci_t_high": per.mean() + half,
            "sd_over_seeds": seed_means.std(ddof=1) if len(seed_means) > 1 else np.nan, "n_runs": len(t),
            "min_train_acc": t.train_acc.min(), **{f"V{int(s) + 1}": v for s, v in per.items()}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--study-dir", required=True)
    parser.add_argument("--default-dir", required=True, help="Default body-relative LOSO runs (§5.16).")
    parser.add_argument("--default-image-dir", required=True, help="Default image-coordinate LOSO runs (§5.16).")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    S, O = args.study_dir, args.output_dir
    os.makedirs(O, exist_ok=True)
    default = load(os.path.join(args.default_dir, "pose-loso-s?-seed?.json"))
    default_img = load(os.path.join(args.default_image_dir, "pose-loso-s?-seed?.json"))

    # S1 nested
    sel = pd.read_csv(os.path.join(S, "nested_selection.csv"))
    nested = load(os.path.join(S, "nested", "pose-loso-s?-seed?.json"))
    s1 = pd.DataFrame([{"variant": "default (d128, L3, lr 5e-4)", **signer_summary(default)},
                       {"variant": "nested selection", **signer_summary(nested)}])
    s1.to_csv(os.path.join(O, "s1_nested.csv"), index=False)
    sel.to_csv(os.path.join(O, "s1_selected_configs.csv"), index=False)
    print("== S1 selected configurations\n", sel.to_string(index=False))
    print("== S1 nested vs. default\n", s1.round(3).to_string(index=False))

    # S2 sensitivity
    sens = load(os.path.join(S, "sensitivity", "*.json"))
    sens["config"] = sens.apply(lambda r: f"d{r.d_model}-L{r.layers}-lr{r.lr:g}", axis=1)
    piv = sens.pivot(index="config", columns="subject", values="f1")
    piv.columns = [f"V{int(c) + 1}" for c in piv.columns]
    piv["mean_over_signers"] = piv.mean(axis=1)
    piv = piv.sort_values("mean_over_signers", ascending=False)
    piv["rank"] = np.arange(1, len(piv) + 1)
    piv.to_csv(os.path.join(O, "s2_sensitivity.csv"))
    m = piv.mean_over_signers
    print(f"== S2 sensitivity (descriptive): 18 configs, new-signer F1 min {m.min():.3f}, median {m.median():.3f}, "
          f"max {m.max():.3f}; default d128-L3-lr0.0005 rank {int(piv.loc['d128-L3-lr0.0005', 'rank'])} "
          f"({piv.loc['d128-L3-lr0.0005', 'mean_over_signers']:.3f})")

    # S3 and S4 variants
    rows = [{"variant": "default, body-relative, 24 frames", **signer_summary(default)},
            {"variant": "default, image coordinates", **signer_summary(default_img)}]
    for d in sorted(glob.glob(os.path.join(S, "ablation", "*"))) + sorted(glob.glob(os.path.join(S, "frames", "*"))):
        t = load(os.path.join(d, "pose-loso-s?-seed?.json"))
        if len(t):
            rows.append({"variant": os.path.relpath(d, S), **signer_summary(t)})
    var = pd.DataFrame(rows)
    var.to_csv(os.path.join(O, "s3_s4_variants.csv"), index=False)
    print("== S3/S4 variants\n", var[["variant", "mean_over_signers", "ci_t_low", "ci_t_high", "sd_over_seeds", "n_runs", "min_train_acc"]]
          .round(3).to_string(index=False))

    # S5 learning curve
    cur = load(os.path.join(S, "curve", "*.json"))
    cur["k"] = cur.train_subjects.map(len)
    d0 = default[default.seed == 0].assign(k=4)
    allk = pd.concat([cur, d0])
    per = allk.groupby(["k", "subject"]).f1.mean().reset_index()
    lc = per.groupby("k").f1.agg(["mean", lambda x: x.std(ddof=1), "count"]).rename(columns={"<lambda_0>": "sd_over_signers", "count": "n_signers"})
    piv5 = per.pivot(index="k", columns="subject", values="f1")
    piv5.columns = [f"V{int(c) + 1}" for c in piv5.columns]
    lc = lc.join(piv5)
    lc.to_csv(os.path.join(O, "s5_learning_curve.csv"))
    print("== S5 learning curve (seed 0)\n", lc.round(3).to_string())

    allruns = load(os.path.join(S, "**", "*.json"))
    print(f"== training accuracy over all study runs: min {allruns.train_acc.min():.3f}, median {allruns.train_acc.median():.3f}")


if __name__ == "__main__":
    main()
