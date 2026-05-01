"""CLI: build a per-subject (LOSO) train/test split.

Replaces ``VIDEOS/dataset_generation_cross_v.py``. ``--subject N`` puts every
clip whose filename starts with ``*_N_*`` into the test split.

Usage:
    python videos/scripts/build_dataset_cv.py \\
        --video-dir path/to/VIDEOS/COLOR_BODY \\
        --subject 0
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.dataset import (
    DEFAULT_NUM_FRAMES,
    DEFAULT_VIVIT_CHECKPOINT,
    make_image_processor,
    per_subject_split,
    save_split,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build per-subject ViViT training dataset.")
    parser.add_argument("--video-dir", required=True, help="Directory with .avi clips.")
    parser.add_argument("--subject", type=int, required=True, help="Subject id held out for testing.")
    parser.add_argument("--train-prefix", default="p_train_dataset_v2_subject_", help="Prefix for the train split path.")
    parser.add_argument("--test-prefix", default="p_test_dataset_v2_subject_", help="Prefix for the test split path.")
    parser.add_argument("--num-frames", type=int, default=DEFAULT_NUM_FRAMES)
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--limit", type=int, default=75, help="Cap on clips processed (matches the original script).")
    args = parser.parse_args()

    print(f"Building per-subject split, holding out subject {args.subject}")
    processor = make_image_processor(args.checkpoint)
    train_rows, test_rows = per_subject_split(
        args.video_dir, processor, holdout_subject=args.subject, limit=args.limit, num_frames=args.num_frames
    )

    print("Saving splits")
    save_split(train_rows, f"{args.train_prefix}{args.subject}")
    save_split(test_rows, f"{args.test_prefix}{args.subject}")
    print("Done")


if __name__ == "__main__":
    main()
