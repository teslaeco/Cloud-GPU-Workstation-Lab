#Requires -RunAsAdministrator
[CmdletBinding()]
param(
    [switch]$SkipVisualStudio
)

$ErrorActionPreference = 'Stop'

function Install-WingetPackage {
    param([Parameter(Mandatory)][string]$Id)

    Write-Host "Installing $Id..." -ForegroundColor Cyan
    & winget install --id $Id -e --accept-source-agreements --accept-package-agreements --silent
    if ($LASTEXITCODE -ne 0) {
        throw "winget failed for $Id with exit code $LASTEXITCODE"
    }
}

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
    throw 'winget is not available. Install or update App Installer.'
}

Install-WingetPackage -Id 'Git.Git'
Install-WingetPackage -Id 'GitHub.cli'
Install-WingetPackage -Id 'OpenJS.NodeJS.LTS'
Install-WingetPackage -Id 'Python.Python.3.13'

if (-not $SkipVisualStudio) {
    Write-Host 'Installing Visual Studio 2022 Community and native game workload...' -ForegroundColor Cyan
    & winget install --id Microsoft.VisualStudio.2022.Community -e `
        --accept-source-agreements --accept-package-agreements `
        --override '--wait --passive --add Microsoft.VisualStudio.Workload.NativeGame --includeRecommended'
    if ($LASTEXITCODE -ne 0) {
        throw "Visual Studio installation failed with exit code $LASTEXITCODE"
    }
}

Write-Host 'Installation completed. Restart Windows before using all tools.' -ForegroundColor Green
