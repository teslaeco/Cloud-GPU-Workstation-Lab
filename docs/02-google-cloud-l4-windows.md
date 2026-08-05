# Google Cloud: Windows workstation with NVIDIA L4

This guide describes a practical cloud workstation for Unreal Engine, 3D tools, and AI-assisted development.

## Example configuration

- Machine family: G2
- Machine type: `g2-standard-8`
- GPU: 1× NVIDIA L4 with 24 GB VRAM
- Memory: 32 GB
- Operating system: a Windows Server image supported by the applications
- Boot disk: 200–500 GB balanced persistent disk
- NVIDIA RTX Virtual Workstation driver/license where required

Availability, supported images, quotas, and prices vary by region and date.

## Before creation

1. Create a separate project for the workstation.
2. Enable billing and Compute Engine.
3. Create a billing budget and alerts.
4. Request only the GPU quota that is needed.
5. Choose a region close to the user and confirm L4 capacity.
6. Plan source-code and asset backups before installing large tools.

## Console workflow

1. Open **Compute Engine → VM instances**.
2. Choose **Create instance**.
3. Select a G2 machine containing NVIDIA L4.
4. Select a compatible Windows Server image.
5. Increase the boot disk for Unreal Engine, Visual Studio, caches, and assets.
6. Restrict network access. Do not expose RDP to the whole internet.
7. Create the VM and Windows credentials.
8. Connect through RDP or an approved workstation protocol.

## Install the qualified NVIDIA driver

Run PowerShell as Administrator:

```powershell
Invoke-WebRequest `
  https://github.com/GoogleCloudPlatform/compute-gpu-installation/raw/main/windows/install_gpu_driver.ps1 `
  -OutFile C:\install_gpu_driver.ps1

C:\install_gpu_driver.ps1
```

Restart when required, then verify:

```powershell
nvidia-smi
```

Official references:

- https://docs.cloud.google.com/compute/docs/virtual-workstation/windows-gpu
- https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers
- https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu

## Install development tools

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\scripts\windows\install-dev-tools.ps1
```

Review the script before running it and remove packages that are not needed.

## Remote display

RDP is useful for setup and administration. Demanding high-frame-rate, multi-monitor, color-sensitive, or low-latency work may need a protocol designed for professional cloud workstations. Google documents HP Anyware/PCoIP for this class of use.

## Stop after work

Closing the remote desktop application does not stop the VM.

Console path:

**Compute Engine → VM instances → select instance → Stop**

Wait for state `TERMINATED`.

CLI alternative:

```bash
gcloud compute instances stop VM_NAME --zone=ZONE
```

Stopped instances do not incur VM usage charges, but persistent disks, static IP addresses, snapshots, reservations, and other attached resources may continue to be billed.

Official reference:

- https://docs.cloud.google.com/compute/docs/instances/stop-start-instance

## Backup recommendation

Before major upgrades:

- commit and push source code,
- copy large binary assets to durable storage,
- create a disk snapshot only when it is useful,
- record driver and application versions.
