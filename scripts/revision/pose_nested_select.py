"""Nested hyperparameter selection for the pose transformer (POSE_TRANSFORMER_STUDY.md, S1).

Reads the inner-fold runs (train on 3 of the 4 training signers, validate on the 4th; the outer
test signer never used) and, per outer test signer, picks the configuration with the highest mean
inner-validation weighted F1 over the 4 inner folds. Ties within --tie (0.005) go to the smaller
model (fewer parameters), then the lower learning rate. Rule fixed in the protocol before any run.

Usage:
    python scripts/revision/pose_nested_select.py --inner-dir WORK/pose_study/inner --output-csv selection.csv
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--inner-dir", required=True)
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--tie", type=float, default=0.005)
    args = parser.parse_args()
    rows = []
    for path in glob.glob(os.path.join(args.inner_dir, "*.json")):
        r = json.load(open(path))
        c = r["config"]
        rows.append({"outer": c["exclude_subject"], "val": r["subject"], "d_model": c["d_model"], "layers": c["layers"],
                     "lr": c["lr"], "n_params": r["n_params"], "val_f1": r["f1_weighted"]})
    t = pd.DataFrame(rows)
    grid = t.groupby(["outer", "d_model", "layers", "lr"]).agg(val_f1=("val_f1", "mean"), n_inner=("val", "nunique"),
                                                               n_params=("n_params", "first")).reset_index()
    assert (grid.n_inner == 4).all(), f"incomplete inner folds:\n{grid[grid.n_inner != 4]}"
    assert grid.groupby("outer").size().eq(18).all(), "expected 18 configurations per outer fold"
    out = []
    for outer, g in grid.groupby("outer"):
        best = g.val_f1.max()
        cand = g[g.val_f1 >= best - args.tie].sort_values(["n_params", "lr"])
        pick = cand.iloc[0]
        out.append({"outer": int(outer), "d_model": int(pick.d_model), "layers": int(pick.layers), "lr": pick.lr,
                    "n_params": int(pick.n_params), "val_f1": pick.val_f1, "best_val_f1": best, "n_tied": len(cand)})
        print(f"outer V{int(outer) + 1}: d_model {int(pick.d_model)}, layers {int(pick.layers)}, lr {pick.lr} "
              f"(val F1 {pick.val_f1:.3f}; best {best:.3f}; {len(cand)} within the tie margin)")
    pd.DataFrame(out).to_csv(args.output_csv, index=False)
    grid.to_csv(args.output_csv.replace(".csv", "_grid.csv"), index=False)


if __name__ == "__main__":
    main()
