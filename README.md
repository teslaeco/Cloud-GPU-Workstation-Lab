# Cloud GPU Workstation Lab

[![CI](https://github.com/teslaeco/Cloud-GPU-Workstation-Lab/actions/workflows/ci.yml/badge.svg)](https://github.com/teslaeco/Cloud-GPU-Workstation-Lab/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](pyproject.toml)
[![Documentation](https://img.shields.io/badge/docs-English%20%7C%20Polski-informational.svg)](README.pl.md)

**Open-source practical guides and tested utilities for building on-demand cloud GPU workstations for game development, AI, 3D, CAD, rendering, simulation, and scientific computing.**

[Polska wersja](README.pl.md) · [Documentation index](docs/README.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

> Rent powerful hardware only when it is needed. Stop it after work. Keep source code, backups, security, and costs under control.

## Project status

This repository is an actively developed educational project. Cloud products, quotas, driver versions, prices, and partner-program rules change. Always verify current provider documentation before creating paid resources.

## Why this repository exists

Independent developers and small teams do not always need to purchase a high-end workstation or an eight-GPU server. A cloud workstation can be started for focused work in Unreal Engine, while a separate GPU cluster can be rented only for model training, rendering, simulation, or batch processing.

This repository is based on practical experience with:

- an 8× NVIDIA H100 environment used during OpenAI Parameter Golf,
- a Google Cloud Windows workstation with an NVIDIA L4 GPU,
- remote development from an Android device,
- Unreal Engine, AI tooling, 3D workflows, and Git-based project management.

The goal is not to claim that one provider is best for every task. The goal is to help people select the right machine, prepare the workload before renting it, and avoid paying for idle compute.

## Who can benefit

- game developers using Unreal Engine or other GPU-heavy tools,
- AI engineers training or evaluating models,
- 3D artists, animators, and VFX teams,
- architects and CAD/BIM users,
- researchers and scientific-computing teams,
- geospatial, remote-sensing, and digital-twin projects,
- video creators and render farms,
- students and independent creators without expensive local hardware.

## Two-machine strategy

| Workload | Recommended class | Example |
|---|---|---|
| Interactive editor, game development, 3D work | GPU virtual workstation | Windows + NVIDIA L4 |
| Large model training, self-play, batch simulation | Linux GPU node or cluster | 1–8× H100 |
| Documentation, Git, issue tracking | Low-cost CPU machine or local device | GitHub + browser |

A large H100 cluster does not make normal desktop work eight times faster. It is valuable when the workload can be parallelized across GPUs.

## Start here

1. Read the [architecture guide](docs/01-architecture.md).
2. Choose either the [Google Cloud L4 workstation](docs/02-google-cloud-l4-windows.md) or the [H100 training workflow](docs/03-runpod-h100-training.md).
3. Review [cost controls](docs/04-cost-control.md) and [security](docs/05-security.md) before creating resources.
4. Run the verification scripts after installation.
5. Stop compute resources when work is complete and confirm their final state in the provider console.

## Repository map

```text
.
├── .github/                 # CI, issue forms, pull request template
├── docs/                    # Architecture, setup, cost, security, use cases
├── scripts/
│   ├── linux/               # Linux GPU checks
│   └── windows/             # Windows setup and verification
├── tests/                   # Unit and CLI integration tests
├── tools/                   # Provider-neutral helper utilities
├── README.md                # English landing page
└── README.pl.md             # Polish landing page
```

Detailed documentation: [`docs/README.md`](docs/README.md).

## Quick start

### Estimate rental versus purchase

```bash
python tools/cost_estimator.py \
  --purchase-cost 55000 \
  --hourly-rate 10 \
  --hours 100 \
  --storage-monthly 150 \
  --months 1 \
  --currency PLN
```

### Install development tools on Windows

Run PowerShell as Administrator after reviewing the script:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\scripts\windows\install-dev-tools.ps1
.\scripts\windows\verify-workstation.ps1
```

### Verify a Linux GPU node

```bash
bash scripts/linux/check-gpu.sh
```

### Run local checks

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
```

## Cost principles

1. Closing Remote Desktop does not stop a VM.
2. A budget alert is usually not a hard spending cap.
3. Stopping and deleting are different operations.
4. Persistent storage, snapshots, static IP addresses, and network traffic can still cost money.
5. Long jobs need checkpoints.
6. Compare the complete task cost, not only the advertised GPU hourly rate.

## Affiliate disclosure

Any referral link must be clearly labelled. A referral relationship must not change the technical recommendation or hide costs, limitations, risks, or alternatives. See [`docs/07-affiliate-and-ethics.md`](docs/07-affiliate-and-ethics.md).

This repository does not currently embed an unlabelled referral link.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Every material change should explain its purpose, risks, compatibility, tests, and documentation impact. Changes are developed through focused pull requests and merged only after green CI.

## Citation

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
