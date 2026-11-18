"""CLI: summarize grid-search result pickles into paper-ready tables.

For every (feature table, split, model) it reports:
- weighted F1, macro F1 and accuracy as mean ± SD (ddof = 1) across runs; the
  `sd_over` column says what the runs are (seeds for the 80/20 split; held-out
  signers x seeds for LOSO, so that SD mixes the two);
- for row splits only, a 95% bootstrap CI of weighted F1 over the pooled test
  predictions (`f1_ci95_pooled_items`). For LOSO this interval is not reported:
  pooling 25 runs (5 signers x 5 seeds, the same items repeated per seed) treats
  items as independent and makes it ~sqrt(5) too narrow (audit K1); use the
  signer-level intervals of scripts/revision/signer_ci.py instead.

Usage:
    python -m common.summarize_results results/landmarks/*.pkl results/imu/*.pkl
"""

from __future__ import annotations

import argparse
import os
import pickle
import re
from collections import defaultdict

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

MODELS = ("svc", "rf", "knn")


def bootstrap_ci(y_true: np.ndarray, y_pred: np.ndarray, n_boot: int = 2000, seed: int = 0) -> tuple[float, float]:
    """95% percentile bootstrap CI of weighted F1."""
    rng = np.random.default_rng(seed)
    n = len(y_true)
    scores = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        scores.append(f1_score(y_true[idx], y_pred[idx], average="weighted", zero_division=0))
    return float(np.percentile(scores, 2.5)), float(np.percentile(scores, 97.5))


def _parse_name(path: str) -> tuple[str, str, int]:
    """``grid_search_results_{db}[_chronos][_new_schema][_groupcv][_shuffled]_seed{n}.pkl`` -> (db, variant, seed)."""
    name = os.path.basename(path)[len("grid_search_results_") : -len(".pkl")]
    match = re.match(r"(.*?)(_chronos)?(_new_schema)?(_groupcv)?(_shuffled)?_seed(\d+)$", name)
    if match is None:
        raise ValueError(f"Unrecognized results file: {path}")
    db, _, new_schema, groupcv, shuffled, seed = match.groups()
    variant = "_".join(v for v, on in (("new_schema", new_schema), ("groupcv", groupcv), ("shuffled", shuffled)) if on)
    return db, variant or "main", int(seed)


def summarize(paths: list[str], n_boot: int) -> pd.DataFrame:
    runs: dict[tuple, list[dict]] = defaultdict(list)
    for path in paths:
        db, variant, seed = _parse_name(path)
        with open(path, "rb") as f:
            results = pickle.load(f)
        for part, entries in results.items():
            split = part.removesuffix("_part") + ("_new_schema" if "new_schema" in variant else "") + ("_groupcv" if "groupcv" in variant else "")
            for key, res in entries.items():
                model = key.split("-")[0]
                runs[(db, split, "shuffled" in variant, model)].append({**res, "seed": seed})

    rows = []
    for (db, split, shuffled, model), items in sorted(runs.items()):
        y_true = np.concatenate([r["y_true"] for r in items])
        y_pred = np.concatenate([r["y_pred"] for r in items])
        is_loso = "loso" in split
        lo, hi = (np.nan, np.nan) if is_loso else bootstrap_ci(y_true, y_pred, n_boot)
        f1 = [r["f1_score"] for r in items]
        rows.append(
            {
                "features": db,
                "split": split,
                "shuffled_labels": shuffled,
                "model": model,
                "n_runs": len(items),
                "seeds": ",".join(sorted({str(r["seed"]) for r in items})),
                "f1_weighted": f"{np.mean(f1):.2f} ± {np.std(f1, ddof=1) if len(f1) > 1 else 0:.2f}",
                "sd_over": "held-out signers x seeds" if is_loso else "seeds",
                "f1_ci95_pooled_items": "" if is_loso else f"[{lo:.2f}, {hi:.2f}]",
                "f1_macro": f"{np.mean([r['f1_macro'] for r in items]):.2f}",
                "accuracy": f"{np.mean([r['accuracy'] for r in items]):.2f}",
                "n_test": len(y_true),
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize grid-search result pickles.")
    parser.add_argument("paths", nargs="+", help="grid_search_results_*_seed*.pkl files.")
    parser.add_argument("--n-boot", type=int, default=2000)
    parser.add_argument("--output-csv", default=None)
    args = parser.parse_args()

    table = summarize(args.paths, args.n_boot)
    print(table.to_string(index=False))
    if args.output_csv:
        table.to_csv(args.output_csv, index=False)


if __name__ == "__main__":
    main()
