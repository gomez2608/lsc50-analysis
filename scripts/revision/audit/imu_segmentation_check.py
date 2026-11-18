"""Check the IMU sign segmentation given by `INFO/Timestamps.xlsx` (REVISION_LOG §3, IMU item 5).

For every volunteer and sign, looks at the joint-angle movement from 2 s before
the marked start until 0.5 s before the next sign's start (10 s after the end
for the last sign). Movement = speed of the 14 OpenSim joint angles (norm of the
per-sample change x sampling rate, deg/s), smoothed over 0.4 s. "Active" =
above 3 x the volunteer's 30th-percentile speed (a rest-level reference).
Active stretches closer than 0.3 s are merged; stretches shorter than 0.5 s are
ignored.

Per segment it reports: the main burst (the one overlapping the marked interval
most), how far it starts before the marked start (`lead_s`) and ends after the
marked end (`tail_s`), the fraction of the marked interval that is active, and
the number and duration of other bursts of at least --min-sign-s seconds outside
the marked interval (candidate unmarked executions).

Shape test for those extra bursts: the joint-angle trajectories of the burst and
of the marked segment are each resampled to 50 points and z-scored per joint;
the correlation between them is compared with the correlation between the burst
and the marked segments of the other signs of the same volunteer (median). A
repetition of the sign should resemble its own marked segment far more than
other signs; a return-to-rest movement should not.

Usage:
    python scripts/revision/audit/imu_segmentation_check.py --imu-dir LSC50_DATA/IMU --output-csv seg_check.csv
"""

from __future__ import annotations

import argparse

import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d

JOINTS = ("arm_add", "arm_flex", "arm_rot", "elbow_flex", "pro_sup", "wrist_dev", "wrist_flex")


def bursts(t: np.ndarray, active: np.ndarray, merge_s: float, min_s: float) -> list[tuple[float, float]]:
    edges = np.diff(np.r_[0, active.astype(int), 0])
    on, off = np.where(edges == 1)[0], np.where(edges == -1)[0] - 1
    out: list[list[float]] = []
    for a, b in zip(on, off):
        if out and t[a] - out[-1][1] < merge_s:
            out[-1][1] = t[b]
        else:
            out.append([t[a], t[b]])
    return [(a, b) for a, b in out if b - a >= min_s]


def shape(a: np.ndarray, n: int = 50) -> np.ndarray:
    """Resample a (samples x joints) trajectory to n points and z-score each joint."""
    x = np.linspace(0, 1, len(a))
    r = np.stack([np.interp(np.linspace(0, 1, n), x, a[:, j]) for j in range(a.shape[1])], axis=1)
    return (r - r.mean(0)) / (r.std(0) + 1e-9)


def corr(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.corrcoef(a.ravel(), b.ravel())[0, 1])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--imu-dir", required=True, help="LSC50 IMU folder (INFO/, OUT_OPENSIM/).")
    parser.add_argument("--output-csv", required=True)
    parser.add_argument("--min-sign-s", type=float, default=1.5, help="Minimum duration of a candidate unmarked execution.")
    args = parser.parse_args()

    xls = pd.ExcelFile(f"{args.imu_dir}/INFO/Timestamps.xlsx")
    rows = []
    for v in range(1, 6):
        sheet = next(s for s in xls.sheet_names if "".join(s.split()) == f"Volunteer{v}")
        ts = pd.read_excel(xls, sheet_name=sheet)
        ts.columns = ["n", "sign", "start", "end"]
        mot = pd.read_csv(f"{args.imu_dir}/OUT_OPENSIM/Volunteer_{v}.mot", sep="\t", header=6)
        t_all = mot["time"].to_numpy()
        fs = 1 / np.median(np.diff(t_all))
        cols = [c for c in mot.columns if c.startswith(JOINTS)]
        speed = np.linalg.norm(np.diff(mot[cols].to_numpy(), axis=0), axis=1) * fs
        speed = uniform_filter1d(speed, max(1, int(0.4 * fs)))
        t = t_all[1:]
        angles = mot[cols].to_numpy()[1:]
        marked_shapes = {}
        for k2, r2 in ts.iterrows():
            m2 = (t >= r2.start) & (t <= r2.end)
            if m2.sum() > 10:
                marked_shapes[k2] = shape(angles[m2])
        thr = 3 * np.percentile(speed, 30)
        for k, r in ts.iterrows():
            nxt = ts.start.iloc[k + 1] - 0.5 if k + 1 < len(ts) else r.end + 10
            w = (t >= r.start - 2) & (t < nxt)
            b = bursts(t[w], speed[w] > thr, merge_s=0.3, min_s=0.5)
            dur = r.end - r.start
            row = {"volunteer": v, "n": r.n, "sign": r.sign, "start": r.start, "end": r.end, "marked_s": dur,
                   "fs": fs, "threshold": thr, "n_bursts": len(b)}
            if dur <= 0:
                rows.append({**row, "note": "empty segment"})
                continue
            inside = (t >= r.start) & (t <= r.end)
            row["active_frac_marked"] = float((speed[inside] > thr).mean())
            overlap = [max(0.0, min(e, r.end) - max(s, r.start)) for s, e in b]
            if b and max(overlap) > 0:
                i = int(np.argmax(overlap))
                s, e = b[i]
                row.update(main_start=s, main_end=e, lead_s=r.start - s, tail_s=e - r.end)
                others = [(s2, e2) for j, (s2, e2) in enumerate(b) if j != i and e2 - s2 >= args.min_sign_s]
            else:
                others = [(s2, e2) for s2, e2 in b if e2 - s2 >= args.min_sign_s]
                row["note"] = "no movement burst overlaps the marked interval"
            row["n_other_long_bursts"] = len(others)
            if others and k in marked_shapes:
                s2, e2 = others[0]
                burst = shape(angles[(t >= s2) & (t <= e2)])
                own = corr(burst, marked_shapes[k])
                rest = [corr(burst, sh) for k2, sh in marked_shapes.items() if k2 != k]
                row.update(corr_own=own, corr_other_signs=float(np.median(rest)),
                           rank_own=int(1 + sum(c > own for c in rest)))
            row["other_long_bursts"] = "; ".join(f"{s2:.1f}-{e2:.1f}" for s2, e2 in others)
            rows.append(row)

    d = pd.DataFrame(rows)
    d.to_csv(args.output_csv, index=False)
    ok = d[d.marked_s > 0]
    print(f"{len(d)} segments ({(d.marked_s <= 0).sum()} empty), sampling rate {ok.fs.round().unique()} Hz")
    print(f"marked interval active: median {ok.active_frac_marked.median():.0%}, min {ok.active_frac_marked.min():.0%}")
    print(f"main burst starts before the mark (lead): median {ok.lead_s.median():.2f} s; > 0.5 s in {(ok.lead_s > 0.5).sum()} segments; > 1 s in {(ok.lead_s > 1).sum()}")
    print(f"main burst ends after the mark (tail): median {ok.tail_s.median():.2f} s; > 0.5 s in {(ok.tail_s > 0.5).sum()} segments; > 1 s in {(ok.tail_s > 1).sum()}")
    print(f"segments with other bursts >= {args.min_sign_s} s before the next sign: {(ok.n_other_long_bursts > 0).sum()} of {len(ok)}; "
          f"distribution {ok.n_other_long_bursts.value_counts().sort_index().to_dict()}")
    sh = ok.dropna(subset=["corr_own"])
    if len(sh):
        print(f"shape test on {len(sh)} extra bursts: correlation with own marked sign median {sh.corr_own.median():.2f} "
              f"vs. other signs {sh.corr_other_signs.median():.2f}; own sign ranked first among 50 in {(sh.rank_own == 1).sum()}, "
              f"top 5 in {(sh.rank_own <= 5).sum()}")
    print("per volunteer:")
    print(ok.groupby("volunteer").agg(marked_s=("marked_s", "median"), lead_s=("lead_s", "median"), tail_s=("tail_s", "median"),
                                      tail_gt_1s=("tail_s", lambda x: int((x > 1).sum())),
                                      with_other_bursts=("n_other_long_bursts", lambda x: int((x > 0).sum()))).round(2).to_string())
    if (ok.get("note") is not None) and ok.note.notna().any():
        print("notes:", ok[ok.note.notna()][["volunteer", "sign", "note"]].to_string(index=False))


if __name__ == "__main__":
    main()
