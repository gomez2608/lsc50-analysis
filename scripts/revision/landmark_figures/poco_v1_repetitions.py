"""POCO (sign 9), Volunteer 1: the signing hand in each of the 4 repetitions, at 5 moments of the execution.

Contact sheet to choose which repetitions show POCO-CANTIDAD and POCO-TAMANO (drawn from the released landmarks).
Usage: python poco_v1_repetitions.py <LANDMARKS dir> <output.png>
"""
import sys
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

D, OUT = sys.argv[1], sys.argv[2]
W, H = 1920, 1080
BLUE, ORANGE, AQUA, INK, INK2, MUTED = "#2a78d6", "#eb6834", "#1baf7a", "#0b0b0b", "#52514e", "#8a8984"
plt.rcParams.update({"font.family": "Arial", "font.size": 8})
EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
         (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]
THUMB, INDEX = {(1, 2), (2, 3), (3, 4)}, {(5, 6), (6, 7), (7, 8)}
MOMENTS = [0.1, 0.2, 0.3, 0.4, 0.5]


def load(kind, name):
    a = pd.read_csv(f"{D}/{kind}/{name}.csv", index_col=0).to_numpy()
    n = a.shape[1] // 3
    return np.stack([a[:, 0::3][:, :n] * W, -a[:, 1::3][:, :n] * H], -1)


fig, axes = plt.subplots(4, len(MOMENTS), figsize=(7.2, 6.4))
for r in range(4):
    name = f"0009_0000_{r:04d}"
    hands = {s: load(f"HANDS_LANDMARKS/{s}_HAND_LANDMARKS", name) for s in ("LEFT", "RIGHT")}
    ok = {s: (h != 0).any(axis=(1, 2)) & np.isfinite(h).all(axis=(1, 2)) for s, h in hands.items()}
    # signing hand: the one detected higher (closer to the face) on average
    s = min(hands, key=lambda k: -hands[k][ok[k], 0, 1].mean() if ok[k].sum() else np.inf)
    h, idx = hands[s], np.where(ok[s])[0]
    for j, m in enumerate(MOMENTS):
        ax = axes[r, j]
        f = idx[min(len(idx) - 1, int(round(m * (len(idx) - 1))))]
        p = h[f]; ctr = (p.max(0) + p.min(0)) / 2; q = (p - ctr) / (np.ptp(p, axis=0).max() / 2.4)
        for a, b in EDGES:
            col = ORANGE if (a, b) in THUMB else AQUA if (a, b) in INDEX else BLUE
            ax.plot(q[[a, b], 0], q[[a, b], 1], color=col, lw=2.0 if col != BLUE else 1.3, solid_capstyle="round")
        ax.scatter(q[:, 0], q[:, 1], s=8, color=INK2, zorder=3)
        ax.scatter(q[[4, 8], 0], q[[4, 8], 1], s=26, color=[ORANGE, AQUA], edgecolors="white", linewidths=0.6, zorder=4)
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color("#e6e5e0")
        if r == 0:
            ax.set_title(f"{int(m * 100)}% of the sign", fontsize=8, color=INK2)
        ax.text(0.03, 0.03, f"frame {f}", transform=ax.transAxes, fontsize=6, color=MUTED)
    axes[r, 0].set_ylabel(f"Repetition {r + 1}\n({s.lower()}-labelled hand)", fontsize=9, color=INK, rotation=0, ha="right", va="center", labelpad=8)

h1 = plt.Line2D([], [], color=ORANGE, lw=2, marker="o", label="Thumb (tip dot)")
h2 = plt.Line2D([], [], color=AQUA, lw=2, marker="o", label="Index (tip dot)")
h3 = plt.Line2D([], [], color=BLUE, lw=1.3, label="Other fingers")
fig.legend(handles=[h1, h2, h3], loc="lower center", ncol=3, frameon=False, fontsize=8)
fig.suptitle("POCO, Volunteer 1: signing hand in each repetition (image orientation, hand-centred and size-normalized)", fontsize=9, color=INK)
fig.tight_layout(rect=(0, 0.04, 1, 0.97))
fig.savefig(OUT, dpi=200, facecolor="white")
print(OUT)
