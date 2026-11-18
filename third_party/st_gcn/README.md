# ST-GCN (vendored, unmodified)

Model code from the official implementation of Yan, Xiong & Lin, "Spatial Temporal Graph Convolutional Networks for Skeleton-Based Action Recognition", AAAI 2018.

- Source: https://github.com/yysijie/st-gcn, commit `221c0e152054b8da593774c0d483e59befdb9061` (2019-08-31).
- Files copied unchanged: `net/st_gcn.py`, `net/utils/graph.py`, `net/utils/tgcn.py`, `LICENSE` (BSD 2-Clause). Empty `__init__.py` files added so the package imports.
- Used by `scripts/revision/stgcn_baseline.py`, which adds the LSC50 MediaPipe skeleton as a subclass of `Graph` (no edits here) and follows the authors' NTU training recipe (`config/st_gcn/ntu-xsub/train.yaml`).
