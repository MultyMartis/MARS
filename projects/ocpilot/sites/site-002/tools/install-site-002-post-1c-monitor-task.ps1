#Requires -Version 5.1
<#
.SYNOPSIS
  Install (disabled by default) Windows Scheduled Task for SITE-002 post-1C monitor.

.DESCRIPTION
  Creates task MARS_SITE_002_Post_1C_Catalog_Monitor pointing to site-002-post-1c-monitor-runner.ps1.
  Task is DISABLED unless -Enable is passed with explicit operator confirmation.

.PARAMETER Enable
  Create task in enabled state. Requires -ConfirmEnable switch for safety.

.PARAMETER ConfirmEnable
  Mandatory with -Enable — operator explicitly accepts automatic daily runs.

.PARAMETER At
  Daily local time HH:mm (default 12:30 — 30 min after 1C import at 12:00 Barnaul / 08:00 Moscow).

.PARAMETER Force
  Re-register task if it already exists (disabled state unless -Enable).
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [switch]$Enable,
    [switch]$ConfirmEnable,
    [string]$At = '12:30',
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$TaskName = 'MARS_SITE_002_Post_1C_Catalog_Monitor'
$RepoRoot = 'X:\AI MARS'
$RunnerScript = Join-Path $RepoRoot 'projects\ocpilot\sites\site-002\tools\site-002-post-1c-monitor-runner.ps1'
$InstallLogRoot = 'X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01\scheduler'
$InstallLog = Join-Path $InstallLogRoot ("install-{0}.log" -f (Get-Date -Format 'yyyy-MM-dd_HH-mm-ss'))

function Write-InstallLog([string]$Message) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'o'), $Message
    Write-Host $line
    New-Item -ItemType Directory -Force -Path $InstallLogRoot | Out-Null
    $line | Out-File -FilePath $InstallLog -Append -Encoding utf8
}

Write-InstallLog "=== SITE-002 post-1C monitor task install ==="
Write-InstallLog "Task name: $TaskName"
Write-InstallLog "Runner: $RunnerScript"
Write-InstallLog "Schedule (local): Daily at $At"
Write-InstallLog "Timezone: $([TimeZoneInfo]::Local.Id) - $([TimeZoneInfo]::Local.DisplayName)"
Write-InstallLog "Enable requested: $Enable"

if (-not (Test-Path -LiteralPath $RunnerScript)) {
    Write-InstallLog "ERROR: Runner script not found."
    exit 1
}

if ($Enable -and -not $ConfirmEnable) {
    Write-InstallLog "ERROR: -Enable requires -ConfirmEnable (operator safety gate)."
    Write-Host ""
    Write-Host "Safety: pass BOTH -Enable and -ConfirmEnable only after operator approval."
    Write-Host "Example (enabled task):"
    Write-Host "  .\install-site-002-post-1c-monitor-task.ps1 -Enable -ConfirmEnable"
    exit 2
}

if ($Enable) {
    Write-InstallLog "Operator confirmed automatic enabled task."
    $safetyText = @(
        'You are enabling automatic daily read-only post-1C monitor runs.',
        'Production is not mutated by the monitor.',
        'Workstation must be on and online at scheduled time.',
        'Disable via Task Scheduler or uninstall script if needed.'
    )
    $safetyText | ForEach-Object { Write-InstallLog "CONFIRM: $_" }
}

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing -and -not $Force) {
    Write-InstallLog "Task already exists. Use -Force to re-register."
    Write-Host "Task '$TaskName' already exists. Use -Force to replace."
    exit 3
}

$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$RunnerScript`"" `
    -WorkingDirectory $RepoRoot

# Daily at local time; start boundary today at requested time
$timeParts = $At -split ':'
$hour = [int]$timeParts[0]
$minute = [int]$timeParts[1]
$start = (Get-Date).Date.AddHours($hour).AddMinutes($minute)
if ($start -lt (Get-Date)) { $start = $start.AddDays(1) }

$trigger = New-ScheduledTaskTrigger -Daily -At $start
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
    -MultipleInstances IgnoreNew

# Network available — use COM if New-ScheduledTask principal settings insufficient on older PS
try {
    $settings | Add-Member -NotePropertyName 'DisallowStartIfOnBatteries' -NotePropertyValue $false -Force
} catch { }

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

$task = New-ScheduledTask -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'MARS SITE-002 read-only post-1C catalog onboarding monitor (local). No Production mutation.'

$registerParams = @{
    TaskName = $TaskName
    InputObject = $task
}
if ($Force -and $existing) {
    $registerParams['Force'] = $true
}

if ($PSCmdlet.ShouldProcess($TaskName, 'Register scheduled task')) {
    Register-ScheduledTask @registerParams | Out-Null
    Write-InstallLog "Task registered."
}

if (-not $Enable) {
    Disable-ScheduledTask -TaskName $TaskName | Out-Null
    Write-InstallLog "Task registered DISABLED (default safe mode)."
    Write-Host ""
    Write-Host "Task '$TaskName' installed DISABLED."
    Write-Host "Enable manually:  Enable-ScheduledTask -TaskName '$TaskName'"
    Write-Host "Or re-run:        .\install-site-002-post-1c-monitor-task.ps1 -Enable -ConfirmEnable -Force"
} else {
    Enable-ScheduledTask -TaskName $TaskName | Out-Null
    Write-InstallLog "Task ENABLED per operator -Enable -ConfirmEnable."
    Write-Host ""
    Write-Host "Task '$TaskName' installed and ENABLED."
    Write-Host "Disable: Disable-ScheduledTask -TaskName '$TaskName'"
}

Write-Host ""
Write-Host "Install log: $InstallLog"
Write-Host "Uninstall:   .\uninstall-site-002-post-1c-monitor-task.ps1"
Write-InstallLog "Install complete."
