# Troubleshooting

## VM cannot be created

Possible causes include insufficient quota, missing regional quota, no capacity in the selected zone, inactive billing, organization policy, or incompatible machine and image.

Try a nearby zone, request only the required quota, verify billing and APIs, and read the exact provider error before changing many settings.

## GPU is not visible

Run:

```powershell
nvidia-smi
```

Verify the VM contains a GPU, install the qualified driver, restart the VM, inspect Device Manager, and compare the image against provider support.

## Unreal Engine is slow remotely

Check region latency, remote resolution, display protocol, GPU driver, CPU, RAM, disk throughput, shader compilation, and asset imports separately.

## VM is stopped but costs remain

Review persistent disks, snapshots, static IP addresses, network egress, licenses, commitments, support plans, and other resources in the project.

## H100 training does not scale

Profile communication overhead, test one GPU first, verify NCCL and interconnect setup, compare examples per second, and use independent workers when distributed training is unnecessary.
