"""Draft figures for the revised manuscript (static, print; PNG at 300 dpi and TIFF).

Colour follows the validated default palette (categorical slots in fixed order:
blue #2a78d6, orange #eb6834, aqua #1baf7a, yellow #eda100; aqua and yellow are
below 3:1 on white, so every series is also labelled directly). Sequential magnitude uses the blue ramp.
Thin marks, recessive grey axes, one y-axis per panel. Text in ink colours,
never in series colours.

Figures:
  fig_loso_models       LOSO weighted F1 per model: mean, 95% t-interval over signers (primary, audit M1), per-signer points
  fig_loso_per_signer   per held-out volunteer, four key models
  fig_dtw_matrix        signer x signer DTW cost (diagonal = within-signer)
  fig_importance        permutation importance by region and by TSFEL feature type
  fig_importance_pose   region permutation importance of ST-GCN and official SPOTER (held-out signer)
  fig_learning_curves   ViViT protocol A (training loss, validation F1), protocol B and pose transformer (training loss)
  fig_confusion_fusion  LOSO confusion matrix of the late fusion, row-normalised (supporting information; R1.2, C24)
  fig_per_sign_f1       LOSO per-sign F1 of fusion, SlowFast, SPOTER and TSFEL + RF (supporting information)

Usage:
    python scripts/revision/make_figures.py --signer-ci signer_ci.csv --dtw dtw_all_signer_matrix.csv \\
        --importance importance_landmarks_bodynorm.csv --vivit-dir vivit --pose-dir pose/image --output-dir figures
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0"
BLUE_RAMP = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#2a78d6", "#1c5cab", "#104281", "#0d366b"]
GROUP = {1: "interp.", 2: "interp.", 3: "deaf", 4: "deaf", 5: "deaf"}
HELPER_ROWS = ("Official SPOTER, seeds 0-2",)  # in signer_ci.csv only to pair SPOTER with fusion on the same seeds
KEY_MODELS = [("Late fusion SlowFast + SPOTER", "Fusion", BLUE), ("SlowFast R50", "SlowFast", ORANGE),
              ("Official SPOTER", "SPOTER", AQUA), ("Landmarks TSFEL body-relative + RF", "TSFEL + RF", YELLOW)]
LABELS = {"Pose transformer, image coordinates": "Pose transformer (ours, exploratory), image coord.",
          "Pose transformer, body-relative": "Pose transformer (ours, exploratory), body-relative"}

plt.rcParams.update({
    "font.family": "Arial", "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6, "axes.titlesize": 9,
    "axes.titleweight": "bold", "axes.titlecolor": INK, "axes.titlelocation": "left", "legend.frameon": False,
})


def save(fig, out_dir: str, name: str) -> None:
    for ext in ("png", "tiff"):
        fig.savefig(os.path.join(out_dir, f"{name}.{ext}"), dpi=300, bbox_inches="tight", facecolor="white",
                    **({"pil_kwargs": {"compression": "tiff_lzw"}} if ext == "tiff" else {}))
    plt.close(fig)
    print("wrote", name)


def grid_x(ax) -> None:
    ax.grid(axis="x", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def fig_loso_models(ci: pd.DataFrame, out: str) -> None:
    d = ci[~ci.model.isin(HELPER_ROWS)].sort_values("mean_f1")
    fig, ax = plt.subplots(figsize=(3.6, 0.3 * len(d) + 0.6))
    y = np.arange(len(d))
    for i, (_, r) in enumerate(d.iterrows()):
        pts = [r[f"V{s}"] for s in range(1, 6)]
        ax.scatter(pts, [i] * 5, s=9, color=MUTED, alpha=0.7, linewidths=0, zorder=2)
        ax.plot([r.ci_t_low, r.ci_t_high], [i, i], color=BLUE, linewidth=2, solid_capstyle="round", zorder=3)
        ax.scatter([r.mean_f1], [i], s=28, color=BLUE, edgecolors="white", linewidths=0.8, zorder=4)
        ax.text(1.005, i, f"{r.mean_f1:.2f} [{max(r.ci_t_low, 0):.2f}, {min(r.ci_t_high, 1):.2f}]", transform=ax.get_yaxis_transform(),
                va="center", ha="left", color=INK2, fontsize=8)
    ax.set_yticks(y, [LABELS.get(m, m) for m in d.model])
    ax.set_xlim(0, 1)
    ax.axvline(0.02, color=MUTED, linewidth=0.6, linestyle=(0, (2, 2)))
    ax.text(0.025, len(d) - 0.4, "chance", color=MUTED, fontsize=8, va="bottom")
    ax.set_xlabel("Weighted F1 on the held-out signer")
    grid_x(ax)
    save(fig, out, "fig_loso_models")


def fig_loso_per_signer(ci: pd.DataFrame, out: str, picks: list[tuple[str, str, str]]) -> None:
    fig, ax = plt.subplots(figsize=(4.6, 3.0))
    x = np.arange(1, 6)
    for name, label, colour in picks:
        r = ci[ci.model == name]
        if r.empty:
            continue
        vals = [r.iloc[0][f"V{s}"] for s in x]
        ax.plot(x, vals, color=colour, linewidth=2, marker="o", markersize=5, markeredgecolor="white", markeredgewidth=0.8)
        ax.text(5.15, vals[-1], label, color=INK, fontsize=8, va="center")
    ax.set_xticks(x, [f"V{s}\n{GROUP[s]}" for s in x])
    ax.set_xlim(0.7, 5.1)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Weighted F1 on the held-out signer")
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    save(fig, out, "fig_loso_per_signer")


def fig_dtw(path: str, out: str) -> None:
    m = pd.read_csv(path, index_col=0)
    labels = [f"{c}\n{GROUP[int(c[1:])]}" for c in m.columns]
    cmap = LinearSegmentedColormap.from_list("blue", BLUE_RAMP)
    fig, ax = plt.subplots(figsize=(3.4, 3.0))
    im = ax.imshow(m.values, cmap=cmap, vmin=0, vmax=np.ceil(m.values.max()))
    for i in range(len(m)):
        for j in range(len(m)):
            v = m.values[i, j]
            ax.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=8,
                    color="white" if v > 0.55 * m.values.max() else INK, fontweight="bold" if i == j else "normal")
    ax.set_xticks(range(len(m)), labels)
    ax.set_yticks(range(len(m)), labels)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.outline.set_visible(False)
    cb.set_label("Per-step DTW cost (lower = more similar)", color=INK2)
    save(fig, out, "fig_dtw_matrix")


def fig_importance_pose(paths: list[tuple[str, str]], out: str) -> None:
    fig, axes = plt.subplots(1, len(paths), figsize=(6.6, 2.2), sharex=True)
    for ax, (title, path) in zip(axes, paths):
        d = pd.read_csv(path)
        piv = d[d.grouping == "region"].pivot(index="group", columns="subject", values="importance")
        piv = piv.loc[piv.mean(axis=1).sort_values().index]
        y = np.arange(len(piv))
        ax.barh(y, piv.mean(axis=1), height=0.6, color=BLUE, edgecolor="white", linewidth=1)
        for i, (_, row) in enumerate(piv.iterrows()):
            ax.scatter(row.values, [i] * len(row), s=7, color=INK2, alpha=0.6, linewidths=0, zorder=3)
        ax.set_yticks(y, piv.index)
        ax.axvline(0, color=MUTED, linewidth=0.6)
        ax.set_xlabel("Drop in weighted F1 when permuted")
        ax.set_title(title)
        grid_x(ax)
    fig.tight_layout()
    save(fig, out, "fig_importance_pose")


def fig_importance(path: str, out: str) -> None:
    d = pd.read_csv(path)
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.0), gridspec_kw={"width_ratios": [1, 1.6]})
    for ax, grouping, title in ((axes[0], "region", "By body region"), (axes[1], "feature", "By TSFEL feature type")):
        g = d[d.grouping == grouping]
        piv = g.pivot(index="group", columns="subject", values="importance")
        order = piv.mean(axis=1).sort_values().index
        piv = piv.loc[order]
        y = np.arange(len(piv))
        ax.barh(y, piv.mean(axis=1), height=0.6, color=BLUE, edgecolor="white", linewidth=1)
        for i, (_, row) in enumerate(piv.iterrows()):
            ax.scatter(row.values, [i] * len(row), s=7, color=INK2, alpha=0.6, linewidths=0, zorder=3)
        ax.set_yticks(y, order)
        ax.axvline(0, color=MUTED, linewidth=0.6)
        ax.set_xlabel("Drop in weighted F1 when permuted")
        ax.set_title(title)
        grid_x(ax)
    fig.tight_layout()
    save(fig, out, "fig_importance")


def _curves(paths: list[str], key: str, epoch_key: str = "epoch") -> list[pd.DataFrame]:
    out = []
    for p in paths:
        h = pd.read_csv(p) if p.endswith(".csv") else pd.DataFrame(json.load(open(p))["history"])
        if key in h:
            out.append(h.dropna(subset=[key])[[epoch_key, key]])
    return out


def _panel(ax, curves: list[pd.DataFrame], key: str, title: str, ylabel: str) -> None:
    for c in curves:
        ax.plot(c.iloc[:, 0], c[key], color="#86b6ef", linewidth=0.8, alpha=0.8)
    if curves:
        m = pd.concat([c.set_index(c.columns[0])[key] for c in curves], axis=1).mean(axis=1)
        ax.plot(m.index, m.values, color=BLUE, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel("Epoch")
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    if "loss" in key:
        ax.set_ylim(bottom=0)
    ax.text(0.98, 0.95, f"{len(curves)} runs", transform=ax.transAxes, ha="right", va="top", color=MUTED, fontsize=7)


def fig_learning_curves(vivit_dir: str, pose_dir: str, out: str) -> None:
    a = sorted(p for p in glob.glob(f"{vivit_dir}/vivit-s*-seed*/log_history.csv") if "shuffled" not in p)
    b = sorted(p for p in glob.glob(f"{vivit_dir}/vivit-B-s*-seed*/log_history.csv") if "shuffled" not in p)  # controls excluded
    pose = sorted(p for p in glob.glob(f"{pose_dir}/pose-loso-*.json") if "shuffled" not in p)
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 2.4))
    _panel(axes[0], _curves(a, "loss"), "loss", "ViViT, protocol A", "Training loss")
    _panel(axes[1], _curves(a, "eval_f1_weighted"), "eval_f1_weighted", "ViViT, protocol A", "Validation-signer F1")
    _panel(axes[2], _curves(b, "loss"), "loss", "ViViT, protocol B", "Training loss")
    _panel(axes[3], _curves(pose, "train_loss"), "train_loss", "Pose transformer", "Training loss")
    axes[1].set_ylim(0, 1)
    fig.text(0.01, -0.06, "Thin lines: individual leave-one-signer-out runs; bold: mean. Protocol A validates on a 4th training "
             "signer; protocol B and the pose transformer train for a fixed number of epochs and keep the final model.",
             color=MUTED, fontsize=6.5)
    fig.tight_layout()
    save(fig, out, "fig_learning_curves")


def fig_confusion(path: str, out: str) -> None:
    cm = pd.read_csv(path, index_col=0)
    cm = cm.loc[sorted(cm.index, key=_sort_key), sorted(cm.columns, key=_sort_key)]
    share = cm.div(cm.sum(axis=1), axis=0)
    cmap = LinearSegmentedColormap.from_list("blue0", ["#ffffff"] + BLUE_RAMP)
    fig, ax = plt.subplots(figsize=(7.4, 7.0))
    im = ax.imshow(share.values, cmap=cmap, vmin=0, vmax=1, interpolation="nearest")
    n = len(share)
    ax.set_xticks(range(n), share.columns, rotation=90, fontsize=5.5)
    ax.set_yticks(range(n), share.index, fontsize=5.5)
    ax.tick_params(length=0)
    ax.set_xlabel("Predicted sign")
    ax.set_ylabel("True sign")
    for s in ax.spines.values():
        s.set_visible(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cb.outline.set_visible(False)
    cb.set_label("Share of the true sign's executions", color=INK2)
    ax.set_title("Late fusion (SlowFast + SPOTER), held-out signer: confusion matrix")
    fig.text(0.01, -0.02, "Pooled over the 5 held-out signers, averaged over 3 seeds; each row sums to 1 (20 executions, "
             "19 for the three signs with a removed duplicate). Signs in alphabetical order.", color=MUTED, fontsize=6.5, va="top")
    save(fig, out, "fig_confusion_fusion")


def _sort_key(name: str) -> str:
    # Spanish alphabetical order: accents ignored, ñ after n
    import unicodedata
    base = name.strip("¿?").lower().replace("ñ", "n~")
    return "".join(c for c in unicodedata.normalize("NFKD", base) if not unicodedata.combining(c))


def fig_per_sign_f1(path: str, out: str, picks: list[tuple[str, str, str]]) -> None:
    d = pd.read_csv(path)
    d = d[d.split == "loso"].pivot(index="sign", columns="model", values="f1_mean")
    d = d.loc[d[picks[0][0]].sort_values().index]
    fig, ax = plt.subplots(figsize=(4.8, 7.6))
    y = np.arange(len(d))
    lo, hi = d[[p[0] for p in picks]].min(axis=1), d[[p[0] for p in picks]].max(axis=1)
    ax.hlines(y, lo, hi, color=GRID, linewidth=1, zorder=1)
    for name, label, colour in reversed(picks):
        size = 22 if name == picks[0][0] else 12
        ax.scatter(d[name], y, s=size, color=colour, edgecolors="white", linewidths=0.6, zorder=3, label=label)
    ax.set_yticks(y, d.index, fontsize=6)
    ax.set_ylim(-0.7, len(d) - 0.3)
    ax.set_xlim(0, 1)
    ax.set_xlabel("F1 on the held-out signer (mean over 5 signers)")
    ax.set_title("Per-sign F1, leave one signer out")
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc="lower right", fontsize=7, handletextpad=0.2, borderaxespad=0.2)
    grid_x(ax)
    fig.text(0.01, 0.0, "Signs sorted by the fusion's F1. Per sign: F1 per held-out signer, averaged over seeds, then over signers.",
             color=MUTED, fontsize=6.5)
    save(fig, out, "fig_per_sign_f1")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--signer-ci", required=True)
    parser.add_argument("--dtw", required=True)
    parser.add_argument("--importance", required=True)
    parser.add_argument("--vivit-dir", required=True)
    parser.add_argument("--pose-dir", required=True)
    parser.add_argument("--importance-stgcn", default=None, help="importance_stgcn_per_signer.csv")
    parser.add_argument("--importance-spoter", default=None, help="importance_spoter_per_signer.csv")
    parser.add_argument("--confusion-fusion", default=None, help="confusion_late_fusion_slowfast_spoter_loso.csv")
    parser.add_argument("--per-sign", default=None, help="per_sign_f1.csv (prediction_metrics.py)")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    ci = pd.read_csv(args.signer_ci)
    fig_loso_models(ci, args.output_dir)
    fig_loso_per_signer(ci, args.output_dir, KEY_MODELS)
    fig_dtw(args.dtw, args.output_dir)
    fig_importance(args.importance, args.output_dir)
    if args.importance_stgcn and args.importance_spoter:
        fig_importance_pose([("ST-GCN", args.importance_stgcn), ("Official SPOTER", args.importance_spoter)], args.output_dir)
    fig_learning_curves(args.vivit_dir, args.pose_dir, args.output_dir)
    if args.confusion_fusion:
        fig_confusion(args.confusion_fusion, args.output_dir)
    if args.per_sign:
        fig_per_sign_f1(args.per_sign, args.output_dir, KEY_MODELS)


if __name__ == "__main__":
    main()
