"""Summarize ViViT ``results.json`` files written by ``train.py`` / ``train_cv.py``.

Held-out-signer runs (``vivit-s{subject}-seed{seed}``) are averaged over folds
(mean ± SD across held-out signers, all seeds pooled); 80/20 runs
(``vivit-8020-seed{seed}``) over seeds.

Usage:
    python scripts/revision/vivit_summary.py vivit-*/results.json [--output-csv vivit.csv]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

METRICS = ["accuracy", "f1_weighted", "f1_macro"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="+")
    parser.add_argument("--output-csv", default=None)
    args = parser.parse_args()

    rows = []
    for path in args.paths:
        r = json.loads(Path(path).read_text())
        subject = r.get("subject") if isinstance(r.get("subject"), int) else None
        split = "balanced" if subject is None else f"loso_{r.get('val_mode', 'signer')}"
        rows.append({"split": split, "subject": subject, "seed": r["seed"],
                     "n_test": r["n_test"], "best_checkpoint": r["best_checkpoint"],
                     **{m: r[m] for m in METRICS}})
    runs = pd.DataFrame(rows).sort_values(["split", "seed", "subject"])
    print(runs.to_string(index=False, float_format="%.3f"))
    if args.output_csv:
        runs.to_csv(args.output_csv, index=False)

    print()
    for split, g in runs.groupby("split"):
        summary = ", ".join(f"{m} {g[m].mean():.2f} ± {g[m].std(ddof=1):.2f}" for m in METRICS)
        print(f"{split}: {len(g)} runs, seeds {sorted(g.seed.unique())}: {summary}")


if __name__ == "__main__":
    main()
