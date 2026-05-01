# VIDEOS pipeline

ViViT (Vision Transformer for Video) fine-tuning on Colombian sign
language clips. The base checkpoint is
`google/vivit-b-16x2-kinetics400`.

## `src/`

- `dataset.py` — frame sampling (`PyAV`), image processor wiring, and
  dataset assembly. Two split strategies: random per-class
  (`custom_train_test_split`, with the `dataset[i]`→`dataset[j]` bug
  fixed) and per-subject LOSO (`per_subject_split`).
- `train.py` — `TrainingConfig` dataclass and shared Trainer/processor/model
  setup used by both training scripts.
- `evaluate.py` — confusion-matrix evaluation, plus the
  `find_best_checkpoint` helper that walks `checkpoint-*` folders inside
  a per-subject run directory.

## `scripts/`

| Script                | Replaces                              | Purpose                                              |
| --------------------- | ------------------------------------- | ---------------------------------------------------- |
| `build_dataset.py`    | `VIDEOS/dataset_generation.py`        | Random per-class train/test split                    |
| `build_dataset_cv.py` | `VIDEOS/dataset_generation_cross_v.py` | Per-subject LOSO dataset (`--subject N`)             |
| `train.py`            | `VIDEOS/model_train.py`               | Fine-tune ViViT on the general split                 |
| `train_cv.py`         | `VIDEOS/model_train_custom.py`        | Per-subject fine-tune (`--subject N`, `--resume`)    |
| `evaluate.py`         | `VIDEOS/inference_cm.py`              | Single-pass CM on `test_dataset_v2`                  |
| `evaluate_cv.py`      | `VIDEOS/inference.py`                 | Per-subject streamed CM (auto-discovers best ckpt)   |

## `scripts/legacy/`

- `inference_v2.py` — incomplete experimental stub (loads a pre-trained
  ViViT-Kinetics400 checkpoint, starts a Trainer setup that's never run).
  Kept for reference.

## `notebooks/`

Analysis and visualization work that has no script equivalent. Notebooks
that just duplicated the contents of `src/` and `scripts/` were removed
during the reorganization.

- `init_expl.ipynb` — initial dataset exploration; counts clips per
  subject/class, builds `DATASET_COLOR_BODY_WITHOUT/`.
- `train_loss_curves.ipynb` — plot training/validation loss + accuracy
  from per-subject `logs_s{i}.csv` files emitted by `train_cv.py`.
- `circle_diagram.ipynb` — circos visualization aggregating the
  per-subject confusion matrices produced by `evaluate_cv.py`.

## `notebooks/legacy/`

- `inference copy.ipynb` — byte-identical duplicate of
  `notebooks/inference.ipynb` (preserved per "every file accounted for").
