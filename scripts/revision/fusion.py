"""Late fusion of SlowFast (video) and SPOTER (landmarks): equal-weight average of the class probabilities (docs/FUSION.md).

For each SlowFast run saved with --save-probs, the SPOTER run with the same split, held-out signer, seed and
shuffled flag is read; the test executions are matched by their (sign, signer, repetition) keys, which must be
the same set; p = (p_video + p_pose) / 2, prediction = argmax. Nothing is fitted. One JSON per fused run, in the
format of the other models (read by json_runs_summary.py and signer_ci.py).

Usage:
    python scripts/revision/fusion.py --video-dir WORK/fusion/slowfast --pose-dir WORK/fusion/spoter --output-dir WORK/fusion/fused
"""

from __future__ import annotations

import argparse
import glob
import json
import os

import numpy as np
from sklearn.metrics import accuracy_score, f1_score


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--video-dir", required=True)
    parser.add_argument("--pose-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    n = 0
    for fv in sorted(glob.glob(os.path.join(args.video_dir, "slowfast-*.json"))):
        name = os.path.basename(fv)[len("slowfast-"):]
        fp = os.path.join(args.pose_dir, "spoter-" + name)
        if not os.path.exists(fp):
            print(f"no SPOTER run for {name}: skipped")
            continue
        v, p = json.load(open(fv)), json.load(open(fp))
        for k in ("split", "subject", "seed", "shuffled_labels", "n_train"):
            assert v[k] == p[k], f"{name}: {k} differs"
        kv, kp = [tuple(x) for x in v["test_keys"]], [tuple(x) for x in p["test_keys"]]
        assert len(kv) == len(set(kv)) and set(kv) == set(kp), f"{name}: different test executions"
        order = {k: i for i, k in enumerate(kp)}
        ip = [order[k] for k in kv]
        pv, pp = np.array(v["probs"]), np.array(p["probs"])[ip]
        y = np.array(v["y_true"])
        assert np.array_equal(y, np.array(p["y_true"])[ip]), f"{name}: labels differ"
        prob = (pv + pp) / 2
        pred = prob.argmax(1)
        out = {"model": "Late fusion: SlowFast R50 + SPOTER, mean of class probabilities", "split": v["split"],
               "subject": v["subject"], "seed": v["seed"], "shuffled_labels": v["shuffled_labels"],
               "accuracy": accuracy_score(y, pred), "f1_weighted": f1_score(y, pred, average="weighted"),
               "f1_macro": f1_score(y, pred, average="macro"), "n_train": v["n_train"], "n_test": len(y),
               "components_f1_weighted": {"slowfast": v["f1_weighted"], "spoter": p["f1_weighted"]},
               "y_true": y.tolist(), "y_pred": pred.tolist(), "test_keys": [list(k) for k in kv]}
        with open(os.path.join(args.output_dir, "fusion-" + name), "w") as f:
            json.dump(out, f)
        print(f"fusion-{name[:-5]}: F1 {out['f1_weighted']:.3f} (SlowFast {v['f1_weighted']:.3f}, SPOTER {p['f1_weighted']:.3f})")
        n += 1
    print(f"{n} fused runs")


if __name__ == "__main__":
    main()
