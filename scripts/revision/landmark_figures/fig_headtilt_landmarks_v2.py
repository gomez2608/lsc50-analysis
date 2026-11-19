"""Head tilt at sign onset, drawn from the released LSC50 landmarks (no image of the participants).

Grey silhouette: first frame of the execution. Blue: frame of largest head tilt in the first 30% of the
execution. Same palette and font as the other figures of the paper (make_figures.py).
Usage: python fig_headtilt_landmarks_v2.py <LANDMARKS dir> <output.png>
"""
import sys
import numpy as np, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Arc
from scipy.spatial import ConvexHull

D, OUT = sys.argv[1], sys.argv[2]
W, H, ONSET = 1920, 1080, 0.3
SIGN = 32                                  # POR FAVOR (LSC50 data descriptor, Table 2)
PANELS = [("A", "Deaf signer", [2, 3, 4]), ("B", "Interpreter", [0, 1])]
BLUE, INK, INK2, MUTED = "#2a78d6", "#0b0b0b", "#52514e", "#8a8984"
GHOST, GHOST_EDGE = "#e9e8e4", "#c9c8c3"
plt.rcParams.update({"font.family": "Arial", "font.size": 8})


def load(kind, name):
    a = pd.read_csv(f"{D}/{kind}/{name}.csv", index_col=0).to_numpy()
    n = a.shape[1] // 3
    return np.stack([a[:, 0::3][:, :n] * W, -a[:, 1::3][:, :n] * H], -1)   # y up


def head_angle(P):
    d1, d2 = P[:, 7] - P[:, 8], P[:, 3] - P[:, 6]          # ears, outer eyes (person's right -> left)
    a = lambda d: np.degrees(np.arctan2(d[:, 1], d[:, 0]))
    return (a(d1) + a(d2)) / 2


def shoulder_angle(P):
    d = P[:, 11] - P[:, 12]
    return np.degrees(np.arctan2(d[:, 1], d[:, 0]))


def pick(subjects):
    best = None
    for subj in subjects:
        for clip in range(4):
            name = f"{SIGN:04d}_{subj:04d}_{clip:04d}"
            try:
                P = load("BODY_LANDMARKS", name)
            except FileNotFoundError:
                continue
            h = head_angle(P); k = max(2, int(ONSET * len(h)))
            i = int(np.argmax(np.abs(h[:k] - h[0])))
            if best is None or abs(h[i] - h[0]) > best[0]:
                best = (abs(h[i] - h[0]), name, i)
    return best


def figure(ax, P, hands, f, c, s, ang, ghost):
    Q = (P[f] - c) / s
    ls, rs = Q[11], Q[12]
    mid = (ls + rs) / 2
    face = Q[[0, 2, 5, 7, 8, 9, 10]]
    hc = face.mean(0); hw = np.linalg.norm(Q[7] - Q[8]) * 1.2
    if ghost:
        # filled silhouette: torso, arms, neck, head, hands
        drop = np.array([0, -1.55])
        torso = [rs, ls, ls + drop + [-0.08, 0], rs + drop + [0.08, 0]]
        ax.add_patch(Polygon(torso, closed=True, fc=GHOST, ec=GHOST_EDGE, lw=0.8, joinstyle="round", zorder=1))
        for a, b in [(11, 13), (13, 15), (12, 14), (14, 16)]:
            ax.plot(Q[[a, b], 0], Q[[a, b], 1], color=GHOST_EDGE, lw=9.5, solid_capstyle="round", zorder=1)
            ax.plot(Q[[a, b], 0], Q[[a, b], 1], color=GHOST, lw=8, solid_capstyle="round", zorder=1.1)
        ax.plot([mid[0], hc[0]], [mid[1], hc[1] - hw * 0.6], color=GHOST_EDGE, lw=6, solid_capstyle="round", zorder=1)
        ax.add_patch(Ellipse(hc, hw, hw * 1.3, angle=ang, fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1.2))
        hand_style = dict(fc=GHOST, ec=GHOST_EDGE, lw=0.8, zorder=1.2)
        line_col = GHOST_EDGE
    else:
        for a, b in [(11, 13), (13, 15), (12, 14), (14, 16)]:
            ax.plot(Q[[a, b], 0], Q[[a, b], 1], color=BLUE, lw=2.2, solid_capstyle="round", zorder=3)
        ax.plot([mid[0], hc[0]], [mid[1], hc[1] - hw * 0.6], color=BLUE, lw=2.2, solid_capstyle="round", zorder=3)
        ax.add_patch(Ellipse(hc, hw, hw * 1.3, angle=ang, fc=(0.165, 0.47, 0.84, 0.10), ec=BLUE, lw=2.2, zorder=3))
        ax.plot(Q[[11, 12], 0], Q[[11, 12], 1], color=BLUE, lw=2.2, solid_capstyle="round", zorder=3)
        ax.scatter(Q[[11, 12, 13, 14], 0], Q[[11, 12, 13, 14], 1], s=14, color=BLUE, zorder=4)
        hand_style = dict(fc=(0.165, 0.47, 0.84, 0.18), ec=BLUE, lw=1.2, zorder=3)
        line_col = BLUE
    for hnd in hands:
        if f < len(hnd) and np.isfinite(hnd[f]).all() and (hnd[f] != 0).any():
            R = (hnd[f] - c) / s
            hull = ConvexHull(R)
            ax.add_patch(Polygon(R[hull.vertices], closed=True, joinstyle="round", **hand_style))
    return hc, hw, line_col


fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.6))
for ax, (L, lab, subjects) in zip(axes, PANELS):
    _, name, peak = pick(subjects)
    P = load("BODY_LANDMARKS", name)
    hands = [load(f"HANDS_LANDMARKS/{x}_HAND_LANDMARKS", name) for x in ("LEFT", "RIGHT")]
    head, sh = head_angle(P), shoulder_angle(P)
    c = (P[0, 11] + P[0, 12]) / 2; s = np.linalg.norm(P[0, 11] - P[0, 12])
    figure(ax, P, hands, 0, c, s, head[0], ghost=True)
    hc, hw, _ = figure(ax, P, hands, peak, c, s, head[peak], ghost=False)
    # head axes and the tilt angle
    r = hw * 1.05
    for a, col, style in [(head[0], MUTED, (0, (3, 2))), (head[peak], BLUE, "-")]:
        v = np.array([np.cos(np.radians(a)), np.sin(np.radians(a))])
        ax.plot([hc[0] - v[0] * r, hc[0] + v[0] * r], [hc[1] - v[1] * r, hc[1] + v[1] * r],
                color=col, lw=1.0, linestyle=style, zorder=5)
    lo, hi = sorted([head[0], head[peak]])
    ax.add_patch(Arc(hc, 2 * r * 0.85, 2 * r * 0.85, theta1=lo, theta2=hi, color=INK2, lw=1.0, zorder=5))
    side = 1 if np.cos(np.radians((lo + hi) / 2)) >= 0 else -1
    ax.text(hc[0] + side * r * 1.15, hc[1] + 0.05, f"{abs(head[peak] - head[0]):.0f}°", ha="left" if side > 0 else "right",
            va="center", fontsize=10, color=INK, fontweight="bold", zorder=6)
    ax.set_title(f"$\\bf{{{L}}}$   {lab}", loc="left", fontsize=10, color=INK, pad=4)
    ax.text(0.0, 0.0, f"Head tilt {abs(head[peak] - head[0]):.0f}°, shoulder line {abs(sh[peak] - sh[0]):.0f}°",
            transform=ax.transAxes, fontsize=8, color=INK2, va="bottom")
    ax.set_aspect("equal"); ax.axis("off")
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.75, 1.15)

h1 = plt.Line2D([], [], color=GHOST_EDGE, lw=6, solid_capstyle="round", label="Start of the sign")
h2 = plt.Line2D([], [], color=BLUE, lw=2.2, label="Largest head tilt")
fig.legend(handles=[h1, h2], loc="lower center", ncol=2, frameon=False, fontsize=8, bbox_to_anchor=(0.5, -0.01))
fig.tight_layout(rect=(0, 0.06, 1, 1))
fig.savefig(OUT, dpi=300, bbox_inches="tight", facecolor="white")
print(OUT)
