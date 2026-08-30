#Requires -Version 5.1
<#
.SYNOPSIS
  Lightweight read-only health / soak checker for accepted MARS VPN nodes.

.DESCRIPTION
  Launches the Python checker defined under this folder.
  Supports FRIENDHOSTING-DE and MCA-VPN-001 (VEESP).
  READ-ONLY against live servers. No secrets in this script.

.PARAMETER Checkpoint
  Soak label: T0 | T+24h | T+72h | T+7d

.PARAMETER Node
  Optional node id filter (repeatable). Default: all nodes in nodes.json

.PARAMETER EvidenceDir
  Evidence output directory

.EXAMPLE
  powershell -NoProfile -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\tools\vpn-nodes-health\Invoke-VpnNodesHealth.ps1" -Checkpoint T0
#>
[CmdletBinding()]
param(
    [ValidateSet('T0', 'T+24h', 'T+72h', 'T+7d')]
    [string]$Checkpoint = 'T0',

    [string[]]$Node = @(),

    [string]$EvidenceDir = 'X:\AI MARS\projects\mars-server-ops\evidence\DUAL-NODE-SOAK-MONITORING-T0-01',

    [string]$Python = 'python'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ToolDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Checker = Join-Path $ToolDir 'vpn-nodes-lightweight-health-01.py'
$NodesJson = Join-Path $ToolDir 'nodes.json'

if (-not (Test-Path -LiteralPath $Checker)) {
    throw "Checker missing: $Checker"
}
if (-not (Test-Path -LiteralPath $NodesJson)) {
    throw "nodes.json missing: $NodesJson"
}

New-Item -ItemType Directory -Force -Path $EvidenceDir | Out-Null

$argList = @(
    $Checker,
    '--nodes', $NodesJson,
    '--evidence-dir', $EvidenceDir,
    '--checkpoint', $Checkpoint
)
foreach ($n in $Node) {
    $argList += @('--node', $n)
}

Write-Host "MARS VPN nodes lightweight health — checkpoint $Checkpoint" -ForegroundColor Cyan
Write-Host "Tool: $Checker"
Write-Host "Evidence: $EvidenceDir"
& $Python @argList
exit $LASTEXITCODE
