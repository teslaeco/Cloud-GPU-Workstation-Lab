#!/usr/bin/env bash
set -euo pipefail

echo '=== NVIDIA SMI ==='
if ! command -v nvidia-smi >/dev/null 2>&1; then
  echo 'ERROR: nvidia-smi is not available.' >&2
  exit 1
fi
nvidia-smi

echo
echo '=== Python ==='
python3 --version || true

echo
echo '=== PyTorch CUDA ==='
python3 -c "import torch; print('PyTorch:', torch.__version__); print('CUDA available:', torch.cuda.is_available()); print('GPU count:', torch.cuda.device_count()); [print(f'GPU {i}: {torch.cuda.get_device_name(i)}') for i in range(torch.cuda.device_count())]" || true
