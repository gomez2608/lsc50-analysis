"""Secondary metrics, confusion matrices and per-sign F1 from stored test predictions (R1.2, C24).

No model is trained: every number comes from the y_true / y_pred already stored by
each run (grid-search pickles, per-run JSON files, ViViT results.json).

Per run: accuracy, weighted F1, macro F1, macro precision and macro recall
(labels 0..49, zero_division=0). Aggregation as for the headline numbers:
- LOSO: per held-out signer, mean over seeds; then mean over the 5 signers with a
  95% t-interval over signers (df = 4), as in signer_ci.py;
- 80/20: mean and SD over seeds.

For the models named with --confusion (landmark or video models only: their label
is the sign index in the file name, named by the authors' correspondance.json; the
IMU tables number the signs alphabetically by folder and are not handled here):
- confusion counts, LOSO summed over signers and averaged over seeds (each row
  sums to 20 = 5 signers x 4 repetitions), 80/20 averaged over seeds (rows sum to 4);
- per-sign F1, LOSO per signer averaged over seeds, then mean and SD over signers;
  80/20 mean over seeds;
- the most frequent confusions (LOSO, off-diagonal).

Inputs, each NAME=PATTERN[,PATTERN...] (repeatable):
  --grid   NAME=LOSO_PATTERN|8020_PATTERN: grid-search pickles, per model in {svc, rf, knn} -> "NAME + RF" etc.;
           loso_part is read only from the first pattern (grouped inner CV, as in signer_ci.py) and balanced_part
           only from the second (the older 80/20 pickles also hold an ungrouped-inner-CV loso_part, not used)
  --json   per-run JSON with subject (int for LOSO, null for 80/20), seed, y_true, y_pred
  --vivit  ViViT results.json (no "subject" key = 80/20)

Usage:
    python scripts/revision/prediction_metrics.py --json "Late fusion=WORK/fusion/fused/fusion-*-seed?.json" \\
        --confusion "Late fusion" --sign-names docs/sign_names_lsc50_table2.json --output-dir prediction_metrics
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import pickle
import re
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support

MODELS = {"svc": "SVM", "rf": "RF", "knn": "KNN"}
LABELS = np.arange(50)
METRICS = ("accuracy", "f1_weighted", "f1_macro", "precision_macro", "recall_macro")


def _paths(spec: str) -> tuple[str, list[str]]:
    name, patterns = spec.split("=", 1)
    paths = sorted({p for pat in patterns.split(",") for p in glob.glob(pat)})
    return name.strip(), [p for p in paths if "shuffled" not in p]


def runs_from_grid(spec: str) -> dict[str, list[dict]]:
    name, patterns = spec.split("=", 1)
    loso_pat, tt_pat = patterns.split("|")
    out = defaultdict(list)
    for (part, split), pat in ((("loso_part", "loso"), loso_pat), (("balanced_part", "8020"), tt_pat)):
        for path in _paths(f"{name}={pat}")[1]:
            seed = int(re.search(r"seed(\d+)\.pkl$", path).group(1))
            d = pickle.load(open(path, "rb"))
            for key, res in d[part].items():
                model, rest = key.split("-", 1)
                subject = int(rest) if split == "loso" else None
                out[f"{name.strip()} + {MODELS[model]}"].append({"split": split, "subject": subject, "seed": seed, "file": path,
                                                         "y_true": np.asarray(res["y_true"]), "y_pred": np.asarray(res["y_pred"])})
    return out


def runs_from_json(spec: str, vivit: bool = False) -> dict[str, list[dict]]:
    name, paths = _paths(spec)
    runs = []
    for path in paths:
        r = json.load(open(path))
        subject = r.get("subject")
        if vivit and "subject" not in r:
            subject = None
        if isinstance(subject, bool) or (subject is not None and not isinstance(subject, int)):
            continue
        runs.append({"split": "loso" if subject is not None else "8020", "subject": subject, "seed": r["seed"], "file": path,
                     "y_true": np.asarray(r["y_true"]), "y_pred": np.asarray(r["y_pred"])})
    return {name: runs}


def run_metrics(yt: np.ndarray, yp: np.ndarray) -> dict:
    p, r, _, _ = precision_recall_fscore_support(yt, yp, labels=LABELS, average="macro", zero_division=0)
    return {"accuracy": accuracy_score(yt, yp), "f1_weighted": f1_score(yt, yp, average="weighted"),
            "f1_macro": f1_score(yt, yp, labels=LABELS, average="macro", zero_division=0),
            "precision_macro": p, "recall_macro": r}


def aggregate(model: str, runs: pd.DataFrame) -> list[dict]:
    rows = []
    loso = runs[runs.split == "loso"]
    if len(loso):
        per_signer = loso.groupby("subject")[list(METRICS)].mean()
        for m in METRICS:
            v = per_signer[m].to_numpy()
            half = stats.t.ppf(0.975, len(v) - 1) * v.std(ddof=1) / np.sqrt(len(v))
            rows.append({"model": model, "split": "loso", "metric": m, "n_signers": len(v),
                         "seeds": int(loso.groupby("subject").seed.nunique().max()), "mean": v.mean(), "sd": v.std(ddof=1),
                         "ci_t_low": v.mean() - half, "ci_t_high": v.mean() + half,
                         **{f"V{int(s) + 1}": per_signer.loc[s, m] for s in per_signer.index}})
    tt = runs[runs.split == "8020"]
    if len(tt):
        for m in METRICS:
            rows.append({"model": model, "split": "8020", "metric": m, "seeds": len(tt), "mean": tt[m].mean(),
                         "sd": tt[m].std(ddof=1) if len(tt) > 1 else np.nan})
    return rows


def confusion_tables(model: str, runs: list[dict], names: list[str], out_dir: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    slug = re.sub(r"[^a-z0-9]+", "_", model.lower()).strip("_")
    per_sign, top = [], []
    for split in ("loso", "8020"):
        rs = [r for r in runs if r["split"] == split]
        if not rs:
            continue
        groups = defaultdict(list)
        for r in rs:
            groups[r["subject"]].append(r)
        cm = sum(np.mean([confusion_matrix(r["y_true"], r["y_pred"], labels=LABELS) for r in g], axis=0) for g in groups.values())
        pd.DataFrame(cm, index=names, columns=names).to_csv(os.path.join(out_dir, f"confusion_{slug}_{split}.csv"),
                                                             float_format="%.6g")
        f1 = np.array([np.mean([f1_score(r["y_true"], r["y_pred"], labels=LABELS, average=None, zero_division=0) for r in g], axis=0)
                       for g in groups.values()])  # groups x signs
        for i, sign in enumerate(names):
            per_sign.append({"model": model, "split": split, "sign_id": i, "sign": sign, "f1_mean": f1[:, i].mean(),
                             "f1_sd_over_signers": f1[:, i].std(ddof=1) if split == "loso" else np.nan,
                             "correct_per_row": cm[i, i], "row_total": cm[i].sum()})
        if split == "loso":
            off = cm.copy()
            np.fill_diagonal(off, 0)
            for k in np.argsort(off, axis=None)[::-1][:15]:
                i, j = np.unravel_index(k, off.shape)
                top.append({"model": model, "true_sign": names[i], "predicted_as": names[j], "count": off[i, j],
                            "share_of_row": off[i, j] / cm[i].sum()})
    return pd.DataFrame(per_sign), pd.DataFrame(top)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--grid", action="append", default=[])
    parser.add_argument("--json", action="append", default=[])
    parser.add_argument("--vivit", action="append", default=[])
    parser.add_argument("--confusion", action="append", default=[], help="Model name as in the output (repeatable).")
    parser.add_argument("--sign-names", required=True, help="index -> sign name: docs/sign_names_lsc50_table2.json (Table 2 of the LSC50 data descriptor). Not the original workspace's correspondance.json, which is a different order (REVISION_LOG §9, 2026-11-03).")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    raw = json.load(open(args.sign_names))
    names = [raw[str(i)].strip() for i in LABELS]
    names = [f"¿{n[:-2]}?" if n.endswith("_q") else n for n in names]

    all_runs: dict[str, list[dict]] = {}
    for spec in args.grid:
        all_runs.update(runs_from_grid(spec))
    for spec in args.json:
        all_runs.update(runs_from_json(spec))
    for spec in args.vivit:
        all_runs.update(runs_from_json(spec, vivit=True))

    per_run, summary = [], []
    for model, runs in all_runs.items():
        if not runs:
            print(f"skip {model}: no runs")
            continue
        rows = [{"model": model, "split": r["split"], "subject": r["subject"], "seed": r["seed"], "n_test": len(r["y_true"]),
                 "file": os.path.basename(os.path.dirname(r["file"])) + "/" + os.path.basename(r["file"]),
                 **run_metrics(r["y_true"], r["y_pred"])} for r in runs]
        per_run += rows
        summary += aggregate(model, pd.DataFrame(rows))
    pd.DataFrame(per_run).to_csv(os.path.join(args.output_dir, "metrics_runs.csv"), index=False)
    s = pd.DataFrame(summary)
    s.to_csv(os.path.join(args.output_dir, "metrics_summary.csv"), index=False)
    wide = s.pivot_table(index=["model", "split"], columns="metric", values="mean")[list(METRICS)]
    print(wide.round(3).to_string())

    per_sign, top = [], []
    for model in args.confusion:
        a, b = confusion_tables(model, all_runs[model], names, args.output_dir)
        per_sign.append(a)
        top.append(b)
    if per_sign:
        pd.concat(per_sign).to_csv(os.path.join(args.output_dir, "per_sign_f1.csv"), index=False)
        t = pd.concat(top)
        t.to_csv(os.path.join(args.output_dir, "top_confusions_loso.csv"), index=False)
        print(t.groupby("model").head(5).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
