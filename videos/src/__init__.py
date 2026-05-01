"""VIDEOS pipeline source modules.

- ``dataset``: PyAV-based frame sampling, ViViT image processor wiring,
  and dataset assembly (general split or per-subject split).
- ``train``: shared Trainer/TrainingArguments + ``compute_metrics`` setup
  for fine-tuning ViViT on the LSC sign clips.
- ``evaluate``: confusion-matrix evaluation on a saved test split, with
  optional checkpoint discovery for per-subject runs.
"""
