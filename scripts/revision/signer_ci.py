"""Signer-level confidence intervals for leave-one-signer-out results (R1.3, R1.8, R2.2).

The bootstrap in `common/summarize_results.py` resamples test items pooled over
all held-out signers, which treats items as independent and ignores that the
signers themselves are a sample of 5. Here, for every model:

- per held-out signer, weighted F1 averaged over seeds;
- headline = mean over the 5 signers (the number reported elsewhere);
- 95% CI from a two-level (hierarchical) bootstrap: resample signers with
  replacement, then each chosen signer's test items with replacement; the same
  item indices are used for every seed of that signer, F1 is averaged over
  seeds, then over the resampled signers (2,000 replicates);
- 95% t-interval over the 5 per-signer means (df = 4). With only 5 signers the
  percentile bootstrap under-covers (its half-width is ~0.6x the t-interval's),
  so the t-interval is the primary interval (audit M1).

Paired comparisons (`--compare "A::B"`, repeatable; the list is fixed in advance in
run_signer_ci.sh): per-signer difference A - B (seed-averaged F1), its mean, the
number of signers where A > B, a paired t-interval and paired t-test (df = 4), the
exact sign-flip test over all 2^5 sign patterns (two-sided; its smallest
attainable p is 2/32 = 0.0625), and Holm-adjusted p-values across the listed pairs.

Inputs (all optional, repeatable), each giving model name and source:
  --grid NAME=PATTERN   grid-search pickles (one per seed), loso part, per model in {svc, rf, knn}
  --json NAME=PATTERN   per-run JSON with subject, seed, y_true, y_pred (pose transformer)
  --vivit NAME=PATTERN  ViViT results.json files

Usage:
    python scripts/revision/signer_ci.py --grid "Landmarks TSFEL body-relative=WORK/bodynorm/grid_search_results_*_groupcv_seed?.pkl" \\
        --json "Pose transformer, image=WORK/pose/image/pose-loso-*.json" --vivit "ViViT B=vivit/vivit-B-s*-seed*/results.json" \\
        --output-csv signer_ci.csv
"""

from __future__ import annotations

import argparse
import glob
import itertools
import json
import pickle
import re
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import f1_score

MODELS = {"svc": "SVM", "rf": "RF", "knn": "KNN"}


def runs_from_grid(pattern: str) -> dict[str, dict[int, dict[int, tuple]]]:
    """{model: {signer: {seed: (y_true, y_pred)}}} from seeded grid-search pickles."""
    out: dict = defaultdict(lambda: defaultdict(dict))
    for path in sorted(glob.glob(pattern)):
        seed = int(re.search(r"seed(\d+)\.pkl$", path).group(1))
        loso = pickle.load(open(path, "rb"))["loso_part"]
        for key, res in loso.items():
            model, signer = key.split("-")
            out[model][int(signer)][seed] = (np.asarray(res["y_true"]), np.asarray(res["y_pred"]))
    return out


def runs_from_json(pattern: str, vivit: bool = False) -> dict[int, dict[int, tuple]]:
    out: dict = defaultdict(dict)
    for path in sorted(glob.glob(pattern)):
        r = json.load(open(path))
        if not isinstance(r.get("subject"), int):
            continue
        out[r["subject"]][r["seed"]] = (np.asarray(r["y_true"]), np.asarray(r["y_pred"]))
    return out


def summarize(name: str, runs: dict[int, dict[int, tuple]], n_boot: int, rng: np.random.Generator) -> dict:
    signers = sorted(runs)
    for s in signers:  # every seed of a signer must use the same test items in the same order
        ys = [yt for yt, _ in runs[s].values()]
        assert all(np.array_equal(ys[0], y) for y in ys), f"{name}: test items differ across seeds for signer {s}"
    per_signer = {s: np.mean([f1_score(yt, yp, average="weighted") for yt, yp in runs[s].values()]) for s in signers}
    means = np.array([per_signer[s] for s in signers])
    boot = np.empty(n_boot)
    for b in range(n_boot):
        chosen = rng.choice(signers, size=len(signers), replace=True)
        vals = []
        for s in chosen:
            n = len(next(iter(runs[s].values()))[0])
            idx = rng.integers(0, n, n)
            vals.append(np.mean([f1_score(yt[idx], yp[idx], average="weighted") for yt, yp in runs[s].values()]))
        boot[b] = np.mean(vals)
    half = stats.t.ppf(0.975, len(means) - 1) * means.std(ddof=1) / np.sqrt(len(means))
    return {
        "model": name, "n_signers": len(signers), "seeds": max(len(v) for v in runs.values()),
        "mean_f1": means.mean(), "sd_over_signers": means.std(ddof=1),
        "ci_hier_low": np.percentile(boot, 2.5), "ci_hier_high": np.percentile(boot, 97.5),
        "ci_t_low": means.mean() - half, "ci_t_high": means.mean() + half,
        **{f"V{s + 1}": per_signer[s] for s in signers},
    }


def sign_flip_p(d: np.ndarray) -> float:
    """Exact two-sided sign-flip p-value for the mean of paired differences."""
    signs = np.array(list(itertools.product([1, -1], repeat=len(d))))
    null = np.abs((signs * d).mean(axis=1))
    return float(np.mean(null >= abs(d.mean()) - 1e-12))


def compare(table: pd.DataFrame, specs: list[str]) -> pd.DataFrame:
    by_name = table.set_index("model")
    cols = [f"V{s}" for s in range(1, 6)]
    rows = []
    for spec in specs:
        a, b = (x.strip() for x in spec.split("::"))
        if a not in by_name.index or b not in by_name.index:
            print(f"skip comparison {a} vs {b}: model not in this run")
            continue
        d = by_name.loc[a, cols].to_numpy(float) - by_name.loc[b, cols].to_numpy(float)
        n, m, sd = len(d), d.mean(), d.std(ddof=1)
        half = stats.t.ppf(0.975, n - 1) * sd / np.sqrt(n)
        rows.append({"model_a": a, "model_b": b, **{f"diff_{c}": v for c, v in zip(cols, d)},
                     "mean_diff": m, "sd_diff": sd, "ci_t_low": m - half, "ci_t_high": m + half,
                     "a_better_in": int((d > 0).sum()), "p_paired_t": float(stats.ttest_1samp(d, 0).pvalue),
                     "p_sign_flip": sign_flip_p(d)})
    out = pd.DataFrame(rows)
    if len(out):  # Holm across the listed comparisons
        order = np.argsort(out.p_paired_t.to_numpy())
        adj, running = np.empty(len(out)), 0.0
        for rank, i in enumerate(order):
            running = max(running, min(1.0, (len(out) - rank) * out.p_paired_t.iloc[i]))
            adj[i] = running
        out["p_paired_t_holm"] = adj
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--grid", action="append", default=[])
    parser.add_argument("--json", action="append", default=[])
    parser.add_argument("--vivit", action="append", default=[])
    parser.add_argument("--n-boot", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--compare", action="append", default=[], help='"MODEL A::MODEL B" (names as in the output).')
    parser.add_argument("--pairs-csv", default=None)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    rows = []
    for spec in args.grid:
        name, pattern = spec.split("=", 1)
        for model, runs in sorted(runs_from_grid(pattern).items()):
            rows.append(summarize(f"{name} + {MODELS[model]}", runs, args.n_boot, rng))
    for spec in args.json + args.vivit:
        name, pattern = spec.split("=", 1)
        runs = runs_from_json(pattern)
        if runs:
            rows.append(summarize(name, runs, args.n_boot, rng))

    out = pd.DataFrame(rows)
    out.to_csv(args.output_csv, index=False)
    if args.compare:
        pairs = compare(out, args.compare)
        if args.pairs_csv:
            pairs.to_csv(args.pairs_csv, index=False)
        print(pairs.round(4).to_string(index=False))
    for r in rows:
        signers = " ".join(f"{r.get(f'V{s}', float('nan')):.2f}" for s in range(1, 6))
        print(f"{r['model']:48s} seeds {r['seeds']}: {r['mean_f1']:.3f}  hierarchical 95% CI [{r['ci_hier_low']:.3f}, {r['ci_hier_high']:.3f}]"
              f"  t-interval [{r['ci_t_low']:.3f}, {r['ci_t_high']:.3f}]  per signer {signers}")


if __name__ == "__main__":
    main()
