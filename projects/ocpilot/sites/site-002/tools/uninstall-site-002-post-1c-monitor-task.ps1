#Requires -Version 5.1
<#
.SYNOPSIS
  Unregister SITE-002 post-1C monitor Windows Scheduled Task (exact name only).
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param()

$ErrorActionPreference = 'Stop'

$TaskName = 'MARS_SITE_002_Post_1C_Catalog_Monitor'
$LogRoot = 'X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01\scheduler'
$LogPath = Join-Path $LogRoot ("uninstall-{0}.log" -f (Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'))

function Write-Log([string]$Message) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'o'), $Message
    Write-Host $line
    New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
    $line | Out-File -FilePath $LogPath -Append -Encoding utf8
}

Write-Log "Uninstall request for exact task: $TaskName"

$task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if (-not $task) {
    Write-Log "Task not found - nothing to remove."
    Write-Host "Task '$TaskName' not found."
    exit 0
}

if ($PSCmdlet.ShouldProcess($TaskName, 'Unregister scheduled task')) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Log "Task unregistered."
    Write-Host "Task '$TaskName' removed."
}

Write-Host "Uninstall log: $LogPath"
