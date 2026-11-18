"""Draw the raw MediaPipe landmark files on the video frames (left/right check, REVISION_LOG §5.24).

For each execution: the frame where the left-labelled hand's wrist is highest
(or --frame), with the points of LEFT_HAND_LANDMARKS (blue, "MP left hand"),
RIGHT_HAND_LANDMARKS (orange, "MP right hand") and pose shoulders/elbows/wrists
(11/13/15 = MediaPipe left, 12/14/16 = right). Also checks that our table
(general_db, native length) holds the same values as the raw files under the
same _LH / _RH / _B suffixes. Images show identifiable volunteers: keep them
out of git and do not publish them.

Usage:
    python scripts/revision/audit/landmark_overlay.py --videos-dir VIDEOS/COLOR_BODY --landmarks-dir LANDMARKS \\
        --general-db WORK/frames/general_db_f0.csv --executions 0001_0000_0000 0001_0001_0000 --output-dir overlay
"""

from __future__ import annotations

import argparse
import os

import cv2
import numpy as np
import pandas as pd

BLUE, ORANGE, GREEN, RED, WHITE = (255, 120, 0), (0, 140, 255), (60, 200, 60), (60, 60, 230), (255, 255, 255)
POSE_LEFT, POSE_RIGHT = (11, 13, 15), (12, 14, 16)


def xy(frame: pd.DataFrame, i: int, row: int, w: int, h: int):
    x, y = frame.iloc[row][f"landmark_{i}_x"], frame.iloc[row][f"landmark_{i}_y"]
    return None if np.isnan(x) else (int(x * w), int(y * h))


def label(img, text, at, colour):
    cv2.putText(img, text, at, cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 0), 6, cv2.LINE_AA)
    cv2.putText(img, text, at, cv2.FONT_HERSHEY_SIMPLEX, 1.1, colour, 2, cv2.LINE_AA)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--videos-dir", required=True)
    parser.add_argument("--landmarks-dir", required=True)
    parser.add_argument("--general-db", default=None)
    parser.add_argument("--executions", nargs="+", required=True, help="{sign}_{subject}_{rep}")
    parser.add_argument("--frame", type=int, default=None)
    parser.add_argument("--pick", choices=["left-highest", "active"], default="left-highest",
                        help="Frame choice without --frame: left-labelled wrist highest, or the more-moving hand at its largest displacement.")
    parser.add_argument("--align-end", action="store_true", help="Shift video frames by (video frames - landmark rows).")
    parser.add_argument("--output-prefix", default="", help="Prefix for the contact sheet name.")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    db = pd.read_csv(args.general_db) if args.general_db else None
    panels = []
    for ex in args.executions:
        raw = {s: pd.read_csv(os.path.join(args.landmarks_dir, sub, ex + ".csv")) for s, sub in
               (("LH", "HANDS_LANDMARKS/LEFT_HAND_LANDMARKS"), ("RH", "HANDS_LANDMARKS/RIGHT_HAND_LANDMARKS"), ("B", "BODY_LANDMARKS"))}
        cap = cv2.VideoCapture(os.path.join(args.videos_dir, ex + ".avi"))
        n_video, w, h = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if args.frame is not None:
            k = args.frame
        elif args.pick == "active":  # the more-moving hand at its largest displacement from the first frame
            wr = {p: raw[p][["landmark_0_x", "landmark_0_y"]].to_numpy() for p in ("LH", "RH")}
            act = max(wr, key=lambda p: np.nansum(np.abs(np.diff(wr[p], axis=0))))
            k = int(np.nanargmax(np.linalg.norm(wr[act] - wr[act][0], axis=1)))
        else:
            k = int(np.nanargmin(raw["LH"]["landmark_0_y"].to_numpy()))
        # landmark files can be shorter than the video; --align-end assumes the missing frames are at the start
        shift = max(n_video - len(raw["LH"]), 0) if args.align_end else 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, k + shift)
        ok, img = cap.read()
        assert ok, f"{ex}: cannot read frame {k}"
        for part, colour, text in (("LH", BLUE, "MP left hand"), ("RH", ORANGE, "MP right hand")):
            pts = [xy(raw[part], i, k, w, h) for i in range(21)]
            for p in pts:
                if p:
                    cv2.circle(img, p, 6, colour, -1)
            if pts[0]:
                label(img, text, (pts[0][0] - 120, pts[0][1] + 60), colour)
        for idx, colour, side in ((POSE_LEFT, GREEN, "L"), (POSE_RIGHT, RED, "R")):
            pts = [xy(raw["B"], i, k, w, h) for i in idx]
            for a, b in zip(pts, pts[1:]):
                if a and b:
                    cv2.line(img, a, b, colour, 4)
            for p, name in zip(pts, ("shoulder", "elbow", "wrist")):
                if p:
                    cv2.circle(img, p, 10, colour, -1)
                    label(img, f"pose {side} {name}", (p[0] + 14, p[1] - 10), colour)
        label(img, "image left", (20, 50), WHITE)
        label(img, "image right", (w - 230, 50), WHITE)
        label(img, f"{ex}  landmark row {k} on video frame {k + shift}  (rows {len(raw['LH'])}, video frames {n_video})", (20, h - 30), WHITE)
        cv2.imwrite(os.path.join(args.output_dir, ex + ".jpg"), img, [cv2.IMWRITE_JPEG_QUALITY, 85])
        panels.append(cv2.resize(img, (w // 2, h // 2)))
        msg = f"{ex}: landmark row {k}, video frame {k + shift} (rows {len(raw['LH'])}, video frames {n_video})"
        if db is not None:  # our table holds the raw values under the same names
            sign, subject, rep = (int(p) for p in ex.split("_"))
            e = db[(db.label == sign) & (db.subject == subject) & (db.rep == rep)].reset_index(drop=True)
            diffs = []
            for part in ("LH", "RH", "B"):
                cols = [c for c in raw[part].columns if c.endswith(("_x", "_y")) and (part != "B" or int(c.split("_")[1]) < 23)]
                r = raw[part][cols].to_numpy(dtype=float)
                t = e[[f"{c}_{part}" for c in cols]].to_numpy(dtype=float)
                m = ~np.isnan(r)  # missing raw values were interpolated in the table
                diffs.append(float(np.abs(r[m] - t[m]).max()))
            msg += f"; max |raw - table| LH {diffs[0]:.2e}, RH {diffs[1]:.2e}, B {diffs[2]:.2e}"
        print(msg)
    while len(panels) % 2:
        panels.append(np.zeros_like(panels[0]))
    sheet = np.vstack([np.hstack(panels[i:i + 2]) for i in range(0, len(panels), 2)])
    cv2.imwrite(os.path.join(args.output_dir, args.output_prefix + "contact_sheet.jpg"), sheet, [cv2.IMWRITE_JPEG_QUALITY, 85])


if __name__ == "__main__":
    main()
