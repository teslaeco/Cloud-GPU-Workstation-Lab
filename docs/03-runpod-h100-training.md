# RunPod and H100-class workloads

A Linux GPU node or cluster is normally better than a Windows graphics workstation for large training runs, reinforcement-learning self-play, rendering farms, and batch compute.

## Appropriate workloads

- distributed PyTorch training,
- reinforcement-learning self-play,
- evaluation of many checkpoints,
- rendering independent frames,
- scientific parameter sweeps,
- dataset preprocessing,
- inference benchmarks.

## When 8× H100 helps

Eight GPUs are useful only when software can distribute work effectively through data, tensor, or pipeline parallelism, independent experiment workers, simulation workers, or separate rendering tasks.

For small models or poorly parallelized code, one GPU may be cheaper and finish sooner.

## Safe deployment workflow

1. Prepare code and tests before renting the GPU.
2. Use an official maintained framework template where possible.
3. Attach persistent storage for checkpoints.
4. Keep API keys in environment secrets.
5. Run a short smoke test on one GPU.
6. Validate multi-GPU communication.
7. Estimate runtime and maximum cost.
8. Start the full run.
9. Save checkpoints frequently.
10. Sync results.
11. Terminate compute after completion.
12. Review remaining volumes and snapshots.

Official references:

- https://docs.runpod.io/pods/overview
- https://docs.runpod.io/pods/templates/overview
- https://docs.runpod.io/pods/connect-to-a-pod
- https://docs.runpod.io/instant-clusters/slurm-clusters

## Checkpoint contents

A resumable training run should store model weights, optimizer and scheduler state, random-number-generator state, current step, configuration, Git commit SHA, and evaluation metrics.

## Verification

```bash
bash scripts/linux/check-gpu.sh
```
