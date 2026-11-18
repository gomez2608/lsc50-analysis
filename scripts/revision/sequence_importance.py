"""Grouped permutation importance for the pose-sequence models on the held-out signer (R2.6; docs/SEQUENCE_IMPORTANCE.md).

Same procedure as `permutation_importance.py` (TSFEL + RF), applied to
landmark sequences: for a group of landmarks, the whole sequence of the group's
x and y coordinates (every frame) is permuted jointly across the test
executions (one execution permutation per repeat, shared by every column of the
group), the trained model predicts again, and the importance is the drop in
weighted F1, averaged over the repeats. Groups: region (left hand, right hand,
body), single point (LH_0..20, RH_0..20, B_0..22), named as in the RF tables, and
subregion (per hand: wrist, thumb, index, middle, ring, little finger; body: face,
left arm, right arm, left and right pose-hand points; added 2026-10-26).
Our implementation (Breiman 2001; Fisher et al. 2019).

`grouped_importance` is called by `pose_transformer.py` and `stgcn_baseline.py`, `grouped_importance_ragged`
by `spoter_baseline.py` (--importance-repeats); `summarize` collects the run JSONs:
    python scripts/revision/sequence_importance.py summarize --runs-dir DIR --output-prefix PREFIX
"""

from __future__ import annotations

import argparse
import glob
import itertools
import json
import os

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import f1_score

REGIONS = {"LH": "left hand", "RH": "right hand", "B": "body"}
# MediaPipe hand points 0-20 and pose points 0-22 (left/right as MediaPipe labels them)
HAND_PARTS = {"wrist": [0], "thumb": [1, 2, 3, 4], "index": [5, 6, 7, 8], "middle": [9, 10, 11, 12],
              "ring": [13, 14, 15, 16], "little": [17, 18, 19, 20]}
BODY_PARTS = {"face": list(range(11)), "left arm": [11, 13, 15], "right arm": [12, 14, 16],
              "left pose hand": [17, 19, 21], "right pose hand": [18, 20, 22]}
GROUPINGS = ("region", "point", "subregion")


def subregion(part: str, idx: int) -> str:
    names = HAND_PARTS if part != "B" else BODY_PARTS
    name = next(k for k, v in names.items() if idx in v)
    return name if part == "B" else f"{part} {name}"


def groups(chans: list[str], groupings=("region", "point")) -> dict[str, dict[str, list[int]]]:
    """Column indices per group; columns are landmark_{i}_{x|y}_{LH|RH|B}. Groupings are evaluated in the
    order given (the random generator is shared, so region first keeps region values comparable between runs)."""
    out: dict[str, dict[str, list[int]]] = {g: {} for g in groupings}
    for j, c in enumerate(chans):
        _, idx, _, part = c.split("_")
        key = {"region": REGIONS[part], "point": f"{part}_{idx}", "subregion": subregion(part, int(idx))}
        for g in groupings:
            out[g].setdefault(key[g], []).append(j)
    return out


def grouped_importance(predict, X: np.ndarray, y: np.ndarray, chans: list[str], n_repeats: int, seed: int,
                       groupings=("region", "point")) -> list[dict]:
    """predict: (N, F, C) array -> labels. X: the test executions, (N, F, C)."""
    rng = np.random.default_rng(seed)
    base = f1_score(y, predict(X), average="weighted")
    rows = []
    for grouping, members in groups(chans, groupings).items():
        for key, idx in members.items():
            drops = []
            for _ in range(n_repeats):
                Xp = X.copy()
                Xp[:, :, idx] = X[rng.permutation(len(X))][:, :, idx]
                drops.append(base - f1_score(y, predict(Xp), average="weighted"))
            rows.append({"grouping": grouping, "group": key, "n_columns": len(idx), "baseline_f1": float(base),
                         "importance": float(np.mean(drops)), "importance_sd": float(np.std(drops))})
    return rows


def resample(a: np.ndarray, n: int) -> np.ndarray:
    """(T, C) -> (n, C), linear over the full duration."""
    if len(a) == n:
        return a.copy()
    src, dst = np.linspace(0, 1, len(a)), np.linspace(0, 1, n)
    return np.stack([np.interp(dst, src, a[:, j]) for j in range(a.shape[1])], axis=1)


def grouped_importance_ragged(predict, seqs: list[np.ndarray], y: np.ndarray, chans: list[str], n_repeats: int, seed: int,
                              groupings=("region",)) -> list[dict]:
    """As `grouped_importance` for sequences of different lengths (SPOTER, native length): the donor execution's
    group sequence is linearly resampled to the recipient's length. predict: list of (T_i, C) arrays -> labels."""
    rng = np.random.default_rng(seed)
    base = f1_score(y, predict(seqs), average="weighted")
    rows = []
    for grouping, members in groups(chans, groupings).items():
        for key, idx in members.items():
            drops = []
            for _ in range(n_repeats):
                perm = rng.permutation(len(seqs))
                new = [s.copy() for s in seqs]
                for i, j in enumerate(perm):
                    new[i][:, idx] = resample(seqs[j][:, idx], len(seqs[i]))
                drops.append(base - f1_score(y, predict(new), average="weighted"))
            rows.append({"grouping": grouping, "group": key, "n_columns": len(idx), "baseline_f1": float(base),
                         "importance": float(np.mean(drops)), "importance_sd": float(np.std(drops))})
    return rows


def summarize(runs_dir: str, prefix: str) -> None:
    rows = []
    for f in sorted(glob.glob(os.path.join(runs_dir, "*.json"))):
        r = json.load(open(f))
        if "importance" not in r:  # e.g. 80/20 or control runs in the same folder
            continue
        for row in r["importance"]:
            rows.append({"run": os.path.basename(f)[:-5], "subject": r["subject"], "seed": r["seed"], **row})
    runs = pd.DataFrame(rows)
    runs.to_csv(prefix + "_runs.csv", index=False)
    # per signer: mean over seeds; then mean over signers with a 95% t-interval (df = signers - 1)
    per_signer = runs.groupby(["grouping", "group", "subject"], as_index=False)[["importance", "baseline_f1"]].mean()
    per_signer.to_csv(prefix + "_per_signer.csv", index=False)
    out = []
    for (grouping, group), g in per_signer.groupby(["grouping", "group"]):
        v = g["importance"].to_numpy()
        half = stats.t.ppf(0.975, len(v) - 1) * v.std(ddof=1) / np.sqrt(len(v))
        out.append({"grouping": grouping, "group": group, "mean": v.mean(), "ci_low": v.mean() - half, "ci_high": v.mean() + half,
                    **{f"s{int(s)}": x for s, x in zip(g["subject"], v)}})
    summary = pd.DataFrame(out).sort_values(["grouping", "mean"], ascending=[True, False])
    summary.to_csv(prefix + "_summary.csv", index=False)
    base = per_signer.drop_duplicates("subject").set_index("subject")["baseline_f1"]
    print("baseline F1 per signer (mean over seeds): " + ", ".join(f"s{int(s)} {b:.3f}" for s, b in base.items()))
    stab = []
    for grouping, g in per_signer.groupby("grouping"):
        piv = g.pivot(index="group", columns="subject", values="importance")
        for keep, cols in (("all", list(piv.columns)), ("baseline_ge_0.2", [s for s in piv.columns if base[s] >= 0.2])):
            rhos = [stats.spearmanr(piv[a], piv[b]).statistic for a, b in itertools.combinations(cols, 2)]
            if rhos:
                stab.append({"grouping": grouping, "folds": keep, "n_folds": len(cols), "rho_mean": np.mean(rhos),
                             "rho_min": np.min(rhos), "rho_max": np.max(rhos)})
        s = summary[summary.grouping == grouping]
        print(f"\n== {grouping} ({len(s)} groups)")
        for _, row in s.head(10).iterrows():
            print(f"  {row['group']:12s} {row['mean']:.4f} [{row['ci_low']:.4f}, {row['ci_high']:.4f}]  per signer "
                  + " ".join(f"{row[c]:.3f}" for c in s.columns if c.startswith("s") and c[1:].isdigit()))
    stab = pd.DataFrame(stab)
    stab.to_csv(prefix + "_stability.csv", index=False)
    print("\n" + stab.to_string(index=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("summarize")
    p.add_argument("--runs-dir", required=True)
    p.add_argument("--output-prefix", required=True)
    args = parser.parse_args()
    summarize(args.runs_dir, args.output_prefix)


if __name__ == "__main__":
    main()
