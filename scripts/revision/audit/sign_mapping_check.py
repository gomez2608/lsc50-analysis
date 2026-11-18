"""Independent check of the sign names given to the video / landmark sign index (C24, per-sign tables).

The only index -> name list is the original workspace's `IMU/correspondance.json`, which
equals the unsorted listing of the IMU sign folders on that filesystem. The video files
(`VIDEOS/COLOR_BODY/SSSS_VVVV_RRRR.avi`) are numbered by sign at recording, with no name.
If the list is right for the videos, a signer's clip duration for video sign i should
follow the duration of the IMU segment of the sign it names (same people, same order,
REVISION_LOG §6.2). Per volunteer: Spearman rho between the mean clip duration of the 4
repetitions of each video sign and the IMU segment duration (Timestamps.xlsx, end - start)
of the named sign, for the correspondance mapping, the alphabetical mapping, and 10,000
random mappings (permutation p-value).

Usage:
    python scripts/revision/audit/sign_mapping_check.py --videos data/VIDEOS/COLOR_BODY \\
        --timestamps data/IMU/INFO/Timestamps.xlsx --names correspondance.json --output sign_mapping_check.csv
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import unicodedata

import av
import numpy as np
import pandas as pd
from scipy.stats import spearmanr


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.replace("_q", "").strip("¿? ").lower().replace("?", "").replace("  ", " ").strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--videos", required=True)
    parser.add_argument("--timestamps", required=True)
    parser.add_argument("--names", required=True)
    parser.add_argument("--n-perm", type=int, default=10000)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = []
    for path in sorted(glob.glob(os.path.join(args.videos, "*.avi"))):
        sign, signer, rep = (int(t) for t in os.path.basename(path)[:-4].split("_"))
        with av.open(path) as c:  # PyAV, the reader used by slowfast_baseline.py
            s = c.streams.video[0]
            n = s.frames or sum(1 for _ in c.decode(s))
            rows.append({"sign": sign, "signer": signer, "rep": rep, "seconds": n / float(s.average_rate)})
    video = pd.DataFrame(rows).groupby(["signer", "sign"]).seconds.mean().unstack()  # signer x sign index

    names = json.load(open(args.names))
    mapping = {"correspondance.json": [norm(names[str(i)]) for i in range(50)]}
    sheets = pd.read_excel(args.timestamps, sheet_name=None)
    imu = {}
    for sheet, t in sheets.items():
        v = int(sheet.split()[-1]) - 1
        imu[v] = {norm(s): e - b for s, b, e in zip(t["Sign"], t["Time Start (s)"], t["Time End (s)"])}
    assert all(set(d) == set(mapping["correspondance.json"]) for d in imu.values()), "sign names do not match"
    mapping["alphabetical"] = sorted(mapping["correspondance.json"])

    rng = np.random.default_rng(0)
    out = []
    for v in sorted(imu):
        vid = video.loc[v].to_numpy()
        for label, m in mapping.items():
            rho = spearmanr(vid, [imu[v][n] for n in m]).statistic
            null = np.array([spearmanr(vid, [imu[v][n] for n in rng.permutation(m)]).statistic for _ in range(args.n_perm)])
            out.append({"volunteer": v + 1, "mapping": label, "spearman_rho": rho,
                        "p_perm_one_sided": (1 + (null >= rho).sum()) / (1 + args.n_perm), "null_rho_95": np.quantile(null, 0.95)})
    # Control: is duration a stable property of a sign within each modality? (mean pairwise rho across signers)
    names_sorted = sorted(mapping["correspondance.json"])
    imu_m = np.array([[imu[v][n] for n in names_sorted] for v in sorted(imu)])
    for label, mat in (("within video, across signers", video.to_numpy()), ("within IMU, across volunteers", imu_m)):
        r = [spearmanr(mat[i], mat[j]).statistic for i in range(len(mat)) for j in range(i + 1, len(mat))]
        out.append({"volunteer": "all pairs", "mapping": label, "spearman_rho": float(np.mean(r)),
                    "p_perm_one_sided": np.nan, "null_rho_95": np.nan, "rho_min": min(r), "rho_max": max(r)})
    video.to_csv(os.path.splitext(args.output)[0] + "_video_seconds.csv")
    res = pd.DataFrame(out)
    res.to_csv(args.output, index=False)
    print(res.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
