# Architecture: choose the right machine

## Principle

Separate interactive work from parallel compute.

### Interactive workstation

Use it for Unreal Engine, 3D modelling, CAD/BIM, debugging, profiling, video editing, and visualization.

Typical configuration:

- Windows,
- one graphics-capable GPU such as NVIDIA L4,
- 32–64 GB RAM,
- persistent boot disk,
- low-latency remote-display protocol.

### Compute node or cluster

Use it for model training, reinforcement-learning self-play, batch rendering, simulation sweeps, large-scale inference, and dataset preprocessing.

Typical configuration:

- Linux,
- CUDA-ready framework image,
- 1–8 compute GPUs,
- fast checkpoint storage,
- scripted and reproducible setup.

## Reference architecture

```text
Android / laptop
      |
      +--> GitHub: code, issues, pull requests, CI
      |
      +--> Windows GPU workstation: editor and interactive development
      |
      +--> Linux GPU cluster: training, rendering, simulation
      |
      +--> Durable storage: checkpoints and build artifacts
```

## Decision checklist

1. Does the task need interactive graphics or raw compute?
2. Can it use several GPUs efficiently?
3. How much VRAM is required?
4. Can the work survive interruption?
5. Where will results and checkpoints be stored?
6. What is the maximum acceptable hourly cost?
7. What stop or maximum-runtime mechanism is available?
8. Is latency acceptable from the user's location?

## Provider independence

- Keep source code in Git.
- Store secrets outside the repository.
- Keep build and setup steps in scripts.
- Store large assets and checkpoints in durable storage.
- Document infrastructure decisions.
- Use portable data formats.
