"""Grouped permutation importance on the held-out signer, with stability across folds (R2.6).

Replaces the impurity-based Random Forest importances of the original paper,
which are computed on training data and favour high-cardinality features.

For each LOSO fold the model is refitted on the training signers with the
hyperparameters selected in that fold by the grid search (read from its result
pickle), and importance is measured on the *held-out signer*: the drop in
weighted F1 when a group of features is permuted jointly across test rows
(same row permutation for every column in the group, so the group's internal
structure is kept). Groups:

- landmarks: body point (65: LH_0..20, RH_0..20, B_0..22), region (left hand,
  right hand, body), TSFEL feature type (14);
- IMU: joint angle (14), TSFEL feature type (14).

Stability: Spearman rank correlation of the group importances between every
pair of folds, and how many folds share each of the overall top-k groups.

Usage:
    python scripts/revision/permutation_importance.py --kind landmarks \\
        --features-csv WORK/bodynorm/temporal_features_bodynorm.csv \\
        --results-pkl WORK/bodynorm/grid_search_results_..._groupcv_seed0.pkl \\
        --output-csv importance_landmarks.csv
"""

from __future__ import annotations

import argparse
import itertools
import pickle

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler

TSFEL_TYPES = [
    "Area under the curve", "Autocorrelation", "Centroid", "Mean absolute diff", "Mean diff",
    "Median absolute diff", "Median diff", "Negative turning points", "Neighbourhood peaks",
    "Positive turning points", "Signal distance", "Slope", "Sum absolute diff", "Zero crossing rate",
]
REGIONS = {"LH": "left hand", "RH": "right hand", "B": "body"}


def split_name(col: str) -> tuple[str, str]:
    """(channel, TSFEL feature type) for a TSFEL column name."""
    for t in TSFEL_TYPES:
        if col.endswith("_" + t):
            return col[: -len(t) - 1], t
    raise ValueError(f"Unrecognised feature column {col!r}")


def groupings(columns: list[str], kind: str) -> dict[str, dict[str, list[int]]]:
    out: dict[str, dict[str, list[int]]] = {}
    for j, col in enumerate(columns):
        channel, ftype = split_name(col)
        if kind == "landmarks":
            # landmark_{i}_{x|y}_{LH|RH|B}
            _, idx, _, region = channel.split("_")
            keys = {"point": f"{region}_{idx}", "region": REGIONS[region], "feature": ftype}
        else:
            keys = {"joint": channel, "feature": ftype}
        for grouping, key in keys.items():
            out.setdefault(grouping, {}).setdefault(key, []).append(j)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--kind", choices=["landmarks", "imu"], required=True)
    parser.add_argument("--features-csv", required=True)
    parser.add_argument("--results-pkl", required=True, help="Grid-search pickle with the per-fold best_params.")
    parser.add_argument("--model", default="rf")
    parser.add_argument("--n-repeats", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--output-csv", required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.features_csv)
    data = data.drop(columns=[c for c in data.columns if c.startswith("Unnamed") or c == "rep"])
    y, subjects = data["label"].to_numpy(), data["subject"].to_numpy()
    cols = [c for c in data.columns if c not in ("label", "subject")]
    X = data[cols].to_numpy(dtype=float)
    groups = groupings(cols, args.kind)
    with open(args.results_pkl, "rb") as f:
        loso = pickle.load(f)["loso_part"]

    rng = np.random.default_rng(args.seed)
    rows = []
    for s in np.unique(subjects):
        tr, te = subjects != s, subjects == s
        params = loso[f"{args.model}-{s}"]["best_params"]
        scaler = StandardScaler().fit(X[tr])
        model = RandomForestClassifier(**params, random_state=args.seed, n_jobs=-1).fit(scaler.transform(X[tr]), y[tr])
        X_te = scaler.transform(X[te])
        base = f1_score(y[te], model.predict(X_te), average="weighted")
        print(f"held-out subject {s}: baseline F1 {base:.3f}, params {params}", flush=True)
        for grouping, members in groups.items():
            for key, idx in members.items():
                drops = []
                for _ in range(args.n_repeats):
                    Xp = X_te.copy()
                    Xp[:, idx] = Xp[rng.permutation(len(Xp))][:, idx]
                    drops.append(base - f1_score(y[te], model.predict(Xp), average="weighted"))
                rows.append({"subject": int(s), "grouping": grouping, "group": key, "n_features": len(idx),
                             "baseline_f1": base, "importance": float(np.mean(drops)), "importance_sd": float(np.std(drops))})

    out = pd.DataFrame(rows)
    out.to_csv(args.output_csv, index=False)

    for grouping, g in out.groupby("grouping"):
        piv = g.pivot(index="group", columns="subject", values="importance")
        rhos = [spearmanr(piv[a], piv[b]).statistic for a, b in itertools.combinations(piv.columns, 2)]
        mean_imp = piv.mean(axis=1).sort_values(ascending=False)
        k = min(args.top_k, len(mean_imp))
        top = mean_imp.index[:k]
        in_fold_top = {grp: int(sum(grp in piv[c].sort_values(ascending=False).index[:k] for c in piv.columns)) for grp in top}
        print(f"\n== {grouping}: {len(piv)} groups; fold-pair Spearman rho mean {np.mean(rhos):.2f} "
              f"(range {np.min(rhos):.2f} to {np.max(rhos):.2f})")
        for grp in top:
            print(f"  {grp:28s} mean drop {mean_imp[grp]:.4f}  per fold {' '.join(f'{v:.3f}' for v in piv.loc[grp])}  "
                  f"in top-{k} of {in_fold_top[grp]}/{piv.shape[1]} folds")


if __name__ == "__main__":
    main()
