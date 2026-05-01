# Legacy video scripts

Files in this folder are preserved for historical reference. They are
**not** part of the current pipeline — the canonical entry points live one
level up in `videos/scripts/`.

- `inference_v2.py` — earlier, incomplete inference experiment. Loads a
  pre-trained ViViT-Kinetics400 checkpoint, runs a single forward pass on
  one clip, and starts a Trainer setup that was never finished. Superseded
  by `videos/scripts/evaluate.py` and `videos/scripts/evaluate_cv.py`.
