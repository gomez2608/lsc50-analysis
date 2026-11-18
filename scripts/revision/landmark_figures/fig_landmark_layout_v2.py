"""Landmark layout (Fig 1 replacement), drawn from the released LSC50 landmarks (no image of the participant).

The 65 landmarks used in the analysis on one frame of one execution (the same execution and frame as the
submitted photo, 0000_0000_0000, frame 10): 23 upper-body pose points, 21 points per hand. Same palette and
font as the other figures of the paper (make_figures.py).
Usage: python fig_landmark_layout_v2.py <LANDMARKS dir> <output.png> [dpi, default 300]
"""
import sys
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

D, OUT = sys.argv[1], sys.argv[2]
NAME, FRAME = "0000_0000_0000", 10
W, H = 1920, 1080
BLUE, ORANGE, AQUA, INK, INK2 = "#2a78d6", "#eb6834", "#1baf7a", "#0b0b0b", "#52514e"
GHOST, GHOST_EDGE = "#efeeea", "#d3d2cd"
plt.rcParams.update({"font.family": "Arial", "font.size": 8})
POSE_EDGES = [(11, 12), (11, 13), (13, 15), (12, 14), (14, 16), (15, 17), (15, 19), (15, 21), (17, 19),
              (16, 18), (16, 20), (16, 22), (18, 20), (0, 2), (2, 7), (0, 5), (5, 8), (9, 10)]
HAND_EDGES = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (10, 11), (11, 12),
              (9, 13), (13, 14), (14, 15), (15, 16), (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)]


def load(kind):
    a = pd.read_csv(f"{D}/{kind}/{NAME}.csv", index_col=0).to_numpy()
    n = a.shape[1] // 3
    return np.stack([a[FRAME, 0::3][:n] * W, -a[FRAME, 1::3][:n] * H], -1)   # y up


body = load("BODY_LANDMARKS")[:23]                 # pose points used: 0-22 (no hips or legs)
left = load("HANDS_LANDMARKS/LEFT_HAND_LANDMARKS")
right = load("HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS")
c = (body[11] + body[12]) / 2; s = np.linalg.norm(body[11] - body[12])
B, Lh, Rh = (body - c) / s, (left - c) / s, (right - c) / s

fig, ax = plt.subplots(figsize=(3.4, 4.0))
# neutral silhouette behind the landmarks
ls, rs = B[11], B[12]; drop = np.array([0, -1.35])
ax.add_patch(Polygon([rs, ls, ls + drop + [-0.08, 0], rs + drop + [0.08, 0]], closed=True, fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1))
for a, b in [(11, 13), (13, 15), (12, 14), (14, 16)]:
    ax.plot(B[[a, b], 0], B[[a, b], 1], color=GHOST_EDGE, lw=10.5, solid_capstyle="round", zorder=1)
    ax.plot(B[[a, b], 0], B[[a, b], 1], color=GHOST, lw=9, solid_capstyle="round", zorder=1.1)
face = B[[0, 2, 5, 7, 8, 9, 10]]; hc = face.mean(0); hw = np.linalg.norm(B[7] - B[8]) * 1.25
ax.plot([(ls[0] + rs[0]) / 2, hc[0]], [(ls[1] + rs[1]) / 2, hc[1] - hw * 0.6], color=GHOST_EDGE, lw=7, solid_capstyle="round", zorder=1)
ang = np.degrees(np.arctan2(*(B[7] - B[8])[::-1]))
ax.add_patch(Ellipse(hc, hw, hw * 1.3, angle=ang, fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1.2))

# landmarks and their connections
for pts, edges, col, lab in [(B, POSE_EDGES, AQUA, "Body (23 points)"), (Lh, HAND_EDGES, ORANGE, "Left-labelled hand (21)"),
                             (Rh, HAND_EDGES, BLUE, "Right-labelled hand (21)")]:
    for a, b in edges:
        ax.plot(pts[[a, b], 0], pts[[a, b], 1], color=col, lw=0.9, alpha=0.7, zorder=2)
    ax.scatter(pts[:, 0], pts[:, 1], s=11, color=col, edgecolors="white", linewidths=0.4, zorder=3, label=lab)

ax.set_aspect("equal"); ax.axis("off")
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=1, frameon=False, fontsize=7.5, handletextpad=0.2, markerscale=1.4)
fig.tight_layout()
fig.savefig(OUT, dpi=int(sys.argv[3]) if len(sys.argv) > 3 else 300, bbox_inches="tight", facecolor="white")
print(OUT)
