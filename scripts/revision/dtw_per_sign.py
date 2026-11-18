"""Per-sign signer x signer DTW matrices from the pair table of dtw_signer_variability.py (R2.9).

No new DTW is computed: the pair table (one row per pair of executions of the
same sign, per-step DTW cost) is averaged per sign and signer pair.

Outputs:
  <prefix>_per_sign_matrix.csv  long table: label, signer_a, signer_b, mean cost, number of pairs
                                (both orders of each signer pair; signer_a == signer_b is within-signer)
  <prefix>_per_sign_summary.csv one row per sign: within / between means and ratio, deaf-deaf,
                                deaf-interpreter and interpreter-interpreter between-signer cost,
                                each signer's mean distance to the others, the most distant signer,
                                and whether the deaf-cluster pattern holds for that sign

Usage:
    python scripts/revision/dtw_per_sign.py --pairs-csv docs/results/dtw/dtw_all_pairs.csv \\
        --output-prefix docs/results/dtw/dtw_all
"""

from __future__ import annotations

import argparse

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--pairs-csv", required=True)
    parser.add_argument("--output-prefix", required=True)
    args = parser.parse_args()

    pairs = pd.read_csv(args.pairs_csv)
    sym = pd.concat([pairs, pairs[pairs.subject_a != pairs.subject_b].rename(
        columns={"subject_a": "subject_b", "subject_b": "subject_a"})])
    long = (sym.groupby(["label", "subject_a", "subject_b"]).dtw.agg(["mean", "size"]).reset_index()
            .rename(columns={"subject_a": "signer_a", "subject_b": "signer_b", "mean": "dtw_mean", "size": "n_pairs"}))
    long["signer_a"] = "V" + (long.signer_a + 1).astype(str)
    long["signer_b"] = "V" + (long.signer_b + 1).astype(str)
    long.to_csv(f"{args.output_prefix}_per_sign_matrix.csv", index=False)

    rows = []
    for label, g in pairs.groupby("label"):
        mat = long[long.label == label].pivot(index="signer_a", columns="signer_b", values="dtw_mean")
        off = mat.where(mat.index.values[:, None] != mat.columns.values[None, :])
        to_others = off.mean(axis=1)
        within, between = g[g.pair == "within"].dtw.mean(), g[g.pair == "between"].dtw.mean()
        btw = g[g.pair == "between"].groupby("groups").dtw.mean()
        row = {"label": label, "n_executions": len(set(zip(g.subject_a, g.rep_a)) | set(zip(g.subject_b, g.rep_b))),
               "within": within, "between": between, "ratio": between / within,
               "deaf_deaf": btw.get("deaf-deaf"), "deaf_interpreter": btw.get("deaf-interpreter"),
               "interpreter_interpreter": btw.get("interpreter-interpreter"),
               "most_distant_signer": to_others.idxmax()}
        row.update({f"{s}_to_others": v for s, v in to_others.items()})
        row.update({f"{s}_within": mat.loc[s, s] for s in mat.index})
        row["deaf_cluster"] = row["deaf_deaf"] < min(row["deaf_interpreter"], row["interpreter_interpreter"])
        rows.append(row)
    summary = pd.DataFrame(rows)
    summary.to_csv(f"{args.output_prefix}_per_sign_summary.csv", index=False)

    print(f"{len(summary)} signs; ratio between/within: min {summary.ratio.min():.2f}, median {summary.ratio.median():.2f}, "
          f"max {summary.ratio.max():.2f}")
    print(f"deaf-deaf < both other group pairs in {int(summary.deaf_cluster.sum())}/{len(summary)} signs")
    print("most distant signer:", summary.most_distant_signer.value_counts().to_dict())
    cols = ["label", "within", "between", "ratio", "deaf_deaf", "deaf_interpreter", "interpreter_interpreter", "most_distant_signer"]
    print("\nlowest ratio (least signer-specific):\n", summary.nsmallest(5, "ratio")[cols].round(2).to_string(index=False))
    print("\nhighest ratio (most signer-specific):\n", summary.nlargest(5, "ratio")[cols].round(2).to_string(index=False))


if __name__ == "__main__":
    main()
