"""The two variants of POCO (Fig 7 replacement), drawn from the released LSC50 landmarks (no image of the participant).

Volunteer 1, sign 9 (POCO): repetition 2 (POCO-CANTIDAD) and repetition 1 (POCO-TAMAÑO), each at 40% of the execution (chosen and identified by the authors).
Each panel: a neutral silhouette with the signing hand at its position relative to the face, and an enlarged
view of the handshape (thumb and index highlighted; dashed line = gap between their tips).
Usage: python fig_poco_variants_v2.py <LANDMARKS dir> <output.png>
"""
import sys
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Rectangle
from scipy.spatial import ConvexHull

D, OUT = sys.argv[1], sys.argv[2]
W, H, MOMENT = 1920, 1080, 0.4
PANELS = [("A", "POCO-CANTIDAD (quantity)", 1), ("B", "POCO-TAMAÑO (size)", 0)]   # repetition index (0-based): A = rep. 2, B = rep. 1 (identified by the authors)
BLUE, ORANGE, AQUA, INK, INK2, MUTED = "#2a78d6", "#eb6834", "#1baf7a", "#0b0b0b", "#52514e", "#8a8984"
GHOST, GHOST_EDGE = "#efeeea", "#d3d2cd"
plt.rcParams.update({"font.family": "Arial", "font.size": 8})
EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
         (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]
THUMB, INDEX = {(1, 2), (2, 3), (3, 4)}, {(5, 6), (6, 7), (7, 8)}


def load(kind, name):
    a = pd.read_csv(f"{D}/{kind}/{name}.csv", index_col=0).to_numpy()
    n = a.shape[1] // 3
    return np.stack([a[:, 0::3][:, :n] * W, -a[:, 1::3][:, :n] * H], -1)   # y up


def draw_hand(ax, q, lw_scale=1.0, dots=True):
    hull = ConvexHull(q)
    ax.add_patch(Polygon(q[hull.vertices], closed=True, fc=(0.165, 0.47, 0.84, 0.12), ec="none", zorder=2))
    for a, b in EDGES:
        col = ORANGE if (a, b) in THUMB else AQUA if (a, b) in INDEX else BLUE
        ax.plot(q[[a, b], 0], q[[a, b], 1], color=col, lw=(2.6 if col != BLUE else 1.5) * lw_scale,
                solid_capstyle="round", zorder=3)
    if dots:
        ax.scatter(q[:, 0], q[:, 1], s=10 * lw_scale, color=INK2, zorder=4)
        ax.scatter(q[[4, 8], 0], q[[4, 8], 1], s=46 * lw_scale, color=[ORANGE, AQUA], edgecolors="white", linewidths=0.8, zorder=5)
        ax.plot(q[[4, 8], 0], q[[4, 8], 1], color=INK, lw=1.0, linestyle=(0, (2.5, 2)), zorder=6)


fig = plt.figure(figsize=(7.0, 3.1))
outer = fig.add_gridspec(1, 2, wspace=0.08)
for k, (L, lab, rep) in enumerate(PANELS):
    name = f"0009_0000_{rep:04d}"
    body = load("BODY_LANDMARKS", name)
    hands = {s: load(f"HANDS_LANDMARKS/{s}_HAND_LANDMARKS", name) for s in ("LEFT", "RIGHT")}
    ok = {s: (h != 0).any(axis=(1, 2)) & np.isfinite(h).all(axis=(1, 2)) for s, h in hands.items()}
    s = min(hands, key=lambda x: -hands[x][ok[x], 0, 1].mean() if ok[x].sum() else np.inf)   # signing hand
    idx = np.where(ok[s])[0]
    f = idx[int(round(MOMENT * (len(idx) - 1)))]
    B, hand = body[f], hands[s][f]
    c = (B[11] + B[12]) / 2; sc = np.linalg.norm(B[11] - B[12])
    Bq, hq = (B - c) / sc, (hand - c) / sc

    inner = outer[k].subgridspec(1, 2, width_ratios=[1, 1.15], wspace=0.02)
    ax0, ax1 = fig.add_subplot(inner[0]), fig.add_subplot(inner[1])
    # context: silhouette with the hand at its position
    ls, rs = Bq[11], Bq[12]; drop = np.array([0, -0.9])
    ax0.add_patch(Polygon([rs, ls, ls + drop + [-0.06, 0], rs + drop + [0.06, 0]], closed=True, fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1))
    face = Bq[[0, 2, 5, 7, 8, 9, 10]]; hc = face.mean(0); hw = np.linalg.norm(Bq[7] - Bq[8]) * 1.25
    ax0.plot([c[0] * 0, hc[0]], [0, hc[1] - hw * 0.6], color=GHOST_EDGE, lw=6, solid_capstyle="round", zorder=1)
    ax0.add_patch(Ellipse(hc, hw, hw * 1.3, angle=np.degrees(np.arctan2(*(Bq[7] - Bq[8])[::-1])), fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1.2))
    for a, b in [(11, 13), (13, 15), (12, 14), (14, 16)]:
        ax0.plot(Bq[[a, b], 0], Bq[[a, b], 1], color=GHOST_EDGE, lw=7.5, solid_capstyle="round", zorder=1)
        ax0.plot(Bq[[a, b], 0], Bq[[a, b], 1], color=GHOST, lw=6.2, solid_capstyle="round", zorder=1.1)
    draw_hand(ax0, hq, lw_scale=0.55, dots=False)
    lo, hi = hq.min(0), hq.max(0); pad = 0.06
    ax0.add_patch(Rectangle(lo - pad, *(hi - lo + 2 * pad), fill=False, ec=INK2, lw=0.8, linestyle=(0, (2, 1.5)), zorder=6))
    ax0.set_aspect("equal"); ax0.axis("off"); ax0.set_xlim(-1.25, 1.25); ax0.set_ylim(-1.0, 1.55)
    # enlarged handshape
    ctr = (hand.max(0) + hand.min(0)) / 2; q = (hand - ctr) / (np.ptp(hand, axis=0).max() / 2.2)
    draw_hand(ax1, q)
    ax1.set_aspect("equal"); ax1.set_xlim(-1.35, 1.35); ax1.set_ylim(-1.35, 1.35)
    ax1.set_xticks([]); ax1.set_yticks([])
    for sp in ax1.spines.values():
        sp.set_color("#d3d2cd"); sp.set_linestyle((0, (2, 1.5)))
    fig.text(0.02 + 0.5 * k, 0.95, f"$\\bf{{{L}}}$   {lab}", fontsize=9.5, color=INK, ha="left", va="top")

h1 = plt.Line2D([], [], color=ORANGE, lw=2.6, marker="o", label="Thumb")
h2 = plt.Line2D([], [], color=AQUA, lw=2.6, marker="o", label="Index")
h3 = plt.Line2D([], [], color=INK, lw=1.0, linestyle=(0, (2.5, 2)), label="Thumb–index gap")
fig.legend(handles=[h1, h2, h3], loc="lower center", ncol=3, frameon=False, fontsize=8, bbox_to_anchor=(0.5, -0.01))
fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.12)
fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
print(OUT, )
