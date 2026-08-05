[CmdletBinding()]
param()

$ErrorActionPreference = 'Continue'

Write-Host '=== Operating system ===' -ForegroundColor Cyan
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, OSArchitecture,
        @{Name='RAM_GB'; Expression={[math]::Round($_.TotalVisibleMemorySize / 1MB, 1)}}

Write-Host "`n=== CPU ===" -ForegroundColor Cyan
Get-CimInstance Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

Write-Host "`n=== Disks ===" -ForegroundColor Cyan
Get-Volume | Where-Object DriveLetter |
    Select-Object DriveLetter,
        @{Name='Size_GB'; Expression={[math]::Round($_.Size / 1GB, 1)}},
        @{Name='Free_GB'; Expression={[math]::Round($_.SizeRemaining / 1GB, 1)}}

Write-Host "`n=== NVIDIA GPU ===" -ForegroundColor Cyan
if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
    nvidia-smi
} else {
    Write-Warning 'nvidia-smi is not available. Check the NVIDIA driver.'
}

Write-Host "`n=== Development tools ===" -ForegroundColor Cyan
foreach ($Command in @('git', 'gh', 'node', 'npm', 'python')) {
    $Resolved = Get-Command $Command -ErrorAction SilentlyContinue
    if ($Resolved) {
        Write-Host "[OK] $Command -> $($Resolved.Source)" -ForegroundColor Green
    } else {
        Write-Warning "[MISSING] $Command"
    }
}
