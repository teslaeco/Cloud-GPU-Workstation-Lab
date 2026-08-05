# Cost control

## Central rule

**A remote-desktop disconnect is not a VM shutdown.**

For Google Compute Engine, wait until the instance state is `TERMINATED`. Google states that stopped instances do not incur VM usage charges, but attached resources such as persistent disks and static IP addresses can continue to be billed.

Official references:

- https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop
- https://docs.cloud.google.com/compute/docs/instances/stop-start-instance
- https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview

## Complete cost categories

- GPU and VM runtime,
- Windows and virtual-workstation licensing,
- persistent disks and network volumes,
- snapshots and backups,
- static public IP addresses,
- outbound network traffic,
- taxes and currency conversion,
- support plans,
- configuration and maintenance time.

## Manual stop checklist

- [ ] Save the project
- [ ] Commit and push source code
- [ ] Close Unreal Engine cleanly
- [ ] Confirm jobs are finished
- [ ] Copy results to durable storage
- [ ] Stop compute in the provider console
- [ ] Confirm stopped or terminated state
- [ ] Review disks, snapshots, IP addresses, and volumes

## Budgets are not hard caps

A budget generally sends alerts. Do not assume it will automatically stop resources unless an automation has been deliberately implemented and tested.

## Calculator

```bash
python tools/cost_estimator.py   --purchase-cost 55000   --hourly-rate 10   --hours 100   --storage-monthly 150   --months 1
```

The calculator is a simplified estimate, not a provider quote or financial advice.
