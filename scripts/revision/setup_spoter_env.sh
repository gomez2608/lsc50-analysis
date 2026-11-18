#!/bin/bash
# Separate environment for official SPOTER (POSE_TRANSFORMER_STUDY.md, S7), following the repository's
# requirements.txt where possible (torch 1.8.1, pandas 1.1.5): newer PyTorch passes arguments to the decoder
# layer that SPOTER's subclass does not accept, and the ViViT environment must not be changed.
# Writes the installed package list next to the environment.
#   scripts/revision/setup_spoter_env.sh ENV_DIR
set -euo pipefail
E="$1"
uv venv --python 3.9 "$E"
uv pip install --python "$E/bin/python" "torch==1.8.1+cpu" -f https://download.pytorch.org/whl/torch_stable.html
uv pip install --python "$E/bin/python" "pandas==1.1.5" "numpy==1.19.5" "scikit-learn==0.24.2" "opencv-python-headless==4.5.5.64"
"$E/bin/python" -c "import torch, pandas, numpy, sklearn, cv2; print(torch.__version__, pandas.__version__, numpy.__version__, sklearn.__version__, cv2.__version__)"
uv pip freeze --python "$E/bin/python" > "$E/requirements-lock.txt"
