"""Markdown table of the hyperparameters selected by grid search (R2.11).

For every (feature table, split, model) it lists the setting chosen most often
across runs (LOSO folds / seeds) and how many runs chose it.

Usage:
    python scripts/revision/hyperparams_table.py WORK/results/*/grid_search_results_*_seed0.pkl
"""

from __future__ import annotations

import argparse
import collections
import os
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from common.summarize_results import _parse_name

# Parameters that cannot change predictions for these models; omitted from the table.
INERT = {
    "knn": {"algorithm", "leaf_size"},
    "svc": {"decision_function_shape"},
    "rf": set(),
}
MODEL_NAMES = {"svc": "SVM", "rf": "RF", "knn": "KNN"}


def _fmt(model: str, params: dict) -> str:
    shown = {k: v for k, v in params.items() if k not in INERT[model]}
    if model == "svc" and shown.get("kernel") != "poly":
        shown.pop("degree", None)
    return ", ".join(f"{k}={v}" for k, v in sorted(shown.items()))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    chosen: dict[tuple, collections.Counter] = collections.defaultdict(collections.Counter)
    for path in args.paths:
        db, variant, _ = _parse_name(path)
        with open(path, "rb") as f:
            results = pickle.load(f)
        for part, entries in results.items():
            split = part.removesuffix("_part") + ("" if variant == "main" else f" ({variant})")
            for key, res in entries.items():
                model = key.split("-")[0]
                chosen[(db, split, model)][_fmt(model, res["best_params"])] += 1

    print("| Features | Split | Model | Most frequent setting | Runs |")
    print("|----------|-------|-------|-----------------------|------|")
    for (db, split, model), counter in sorted(chosen.items()):
        setting, n = counter.most_common(1)[0]
        print(f"| {db} | {split} | {MODEL_NAMES[model]} | {setting} | {n}/{sum(counter.values())} |")


if __name__ == "__main__":
    main()
