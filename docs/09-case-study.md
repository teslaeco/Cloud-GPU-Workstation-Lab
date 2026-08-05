# Case study: from 8× H100 to an L4 workstation

Participation in OpenAI Parameter Golf provided practical experience with professional AI infrastructure and an 8× NVIDIA H100 environment. The important lesson was not only access to expensive hardware. It was learning to prepare code, connect to remote systems, control runtime, preserve results, and stop resources after the job.

That experience later made it possible to configure a cloud Windows workstation with NVIDIA L4 without owning a physical high-end PC. The workstation can be started for Unreal Engine, 3D, and development work, then stopped when it is no longer needed.

| Environment | Main purpose |
|---|---|
| 8× H100 Linux cluster | training, parallel evaluation, self-play, simulation, batch processing |
| NVIDIA L4 Windows workstation | Unreal Engine, 3D editor, visualization, development, remote desktop |

The savings exist only with a disciplined workflow: prepare first, run focused jobs, checkpoint results, stop compute, and audit remaining storage.

## Skills transferred

- GPU quotas and capacity,
- workload-based hardware selection,
- remote terminal and desktop operation,
- driver installation and verification,
- reproducible dependencies,
- cost monitoring,
- checkpointing,
- Git-based collaboration,
- separation of interactive work and parallel compute.

## Cube Chess 512 AI

The L4 workstation can support interactive Unreal Engine development. H100-class infrastructure can later support massive self-play, AI evaluation, neural position evaluation, search experiments, dataset generation, and performance benchmarking.

Expensive compute should accelerate a verified engine. It must not replace correct rules, architecture, unit tests, integration tests, or regression tests.
