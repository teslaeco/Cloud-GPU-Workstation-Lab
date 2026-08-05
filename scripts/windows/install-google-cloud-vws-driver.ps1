#Requires -RunAsAdministrator
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$Destination = 'C:\install_gpu_driver.ps1'
$Url = 'https://github.com/GoogleCloudPlatform/compute-gpu-installation/raw/main/windows/install_gpu_driver.ps1'

Write-Host 'Downloading the qualified Google Cloud NVIDIA driver installer...' -ForegroundColor Cyan
Invoke-WebRequest -Uri $Url -OutFile $Destination

Write-Host 'Running the driver installer...' -ForegroundColor Cyan
& $Destination

if ($LASTEXITCODE -ne 0) {
    throw "Driver installer exited with code $LASTEXITCODE"
}

Write-Host 'Installation completed. Restart when required, then run nvidia-smi.' -ForegroundColor Green
