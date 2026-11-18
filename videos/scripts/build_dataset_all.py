"""CLI: build one on-disk table of every clip, with sign / signer / repetition.

Used by the revision runs instead of ``build_dataset.py`` and
``build_dataset_cv.py``: the 80/20 split (per seed) and every held-out-signer
split are drawn from this single table inside ``train.py`` / ``train_cv.py``,
so nothing is rebuilt per split and no clip cap applies (P14).

Usage:
    python videos/scripts/build_dataset_all.py \\
        --video-dir path/to/VIDEOS/COLOR_BODY \\
        --output clips_all
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from videos.src.dataset import (
    DEFAULT_NUM_FRAMES,
    DEFAULT_VIVIT_CHECKPOINT,
    build_all_clips_dataset,
    make_image_processor,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the full ViViT clip table.")
    parser.add_argument("--video-dir", required=True, help="Directory with .avi clips.")
    parser.add_argument("--output", default="clips_all", help="Output dataset directory.")
    parser.add_argument("--num-frames", type=int, default=DEFAULT_NUM_FRAMES)
    parser.add_argument("--checkpoint", default=DEFAULT_VIVIT_CHECKPOINT)
    parser.add_argument("--limit", type=int, default=None, help="Optional cap, for smoke tests only.")
    args = parser.parse_args()

    processor = make_image_processor(args.checkpoint)
    build_all_clips_dataset(
        args.video_dir, processor, args.output, num_frames=args.num_frames, limit=args.limit
    )
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
