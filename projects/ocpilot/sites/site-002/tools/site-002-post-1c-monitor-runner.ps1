#Requires -Version 5.1
<#
.SYNOPSIS
  SITE-002 read-only post-1C catalog onboarding monitor runner (scheduled/local).

.DESCRIPTION
  Invokes site-002-prod-post-1c-catalog-onboarding-monitor-02.py in read-only mode.
  Writes timestamped logs under X:\AI MARS STORAGE\...\scheduled-monitors\post-1c\
  Does not mutate Production. No credentials printed.

.PARAMETER DryRun
  Validate environment and optionally probe public sitemap only; do not run full monitor.
#>
[CmdletBinding()]
param(
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$RepoRoot = 'X:\AI MARS'
$MonitorScript = Join-Path $RepoRoot 'projects\ocpilot\sites\site-002\tools\site-002-prod-post-1c-catalog-onboarding-monitor-02.py'
$ScheduledRoot = 'X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c'
$OperationId = 'SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01'
$ProductionUrl = 'https://bzpm.ru/'
$SitemapUrl = 'https://bzpm.ru/sitemap.xml'

function Get-PythonExecutable {
    $candidates = @()
    $venvPy = Join-Path $RepoRoot '.venv\Scripts\python.exe'
    if (Test-Path -LiteralPath $venvPy) { $candidates += $venvPy }
    if (Get-Command py -ErrorAction SilentlyContinue) { $candidates += 'py' }
    if (Get-Command python -ErrorAction SilentlyContinue) { $candidates += 'python' }
    foreach ($c in $candidates) {
        try {
            $ver = & $c --version 2>&1
            if ($LASTEXITCODE -eq 0 -or $ver) { return @{ Path = $c; Version = "$ver".Trim() } }
        } catch { continue }
    }
    return $null
}

function Write-JsonFile {
    param([string]$Path, [object]$Data)
    $json = $Data | ConvertTo-Json -Depth 8
    [System.IO.File]::WriteAllText($Path, $json + "`n", [System.Text.UTF8Encoding]::new($false))
}

$startedAt = Get-Date
$runDirName = $startedAt.ToString('yyyy-MM-dd_HH-mm-ss')
$runDir = Join-Path $ScheduledRoot $runDirName
New-Item -ItemType Directory -Force -Path $runDir | Out-Null

$logPath = Join-Path $runDir 'run.log'
$summaryJsonPath = Join-Path $runDir 'run-summary.json'
$summaryMdPath = Join-Path $runDir 'run-summary.md'

$summary = [ordered]@{
    operation_id       = $OperationId
    runner_script      = $MyInvocation.MyCommand.Path
    monitor_script     = $MonitorScript
    mode               = if ($DryRun) { 'dry-run' } else { 'read-only-monitor' }
    production_url     = $ProductionUrl
    repo_root          = $RepoRoot
    run_directory      = $runDir
    started_at_local   = $startedAt.ToString('o')
    timezone_id        = [TimeZoneInfo]::Local.Id
    timezone_display   = [TimeZoneInfo]::Local.DisplayName
    python             = $null
    monitor_script_exists = (Test-Path -LiteralPath $MonitorScript)
    exit_code          = 0
    status             = 'pending'
    dry_run_sitemap_probe = $null
    error              = $null
}

function Finish-Summary {
    param([int]$ExitCode)
    $summary.exit_code = $ExitCode
    $summary.finished_at_local = (Get-Date).ToString('o')
    if (-not $summary.status -or $summary.status -eq 'pending') {
        $summary.status = if ($ExitCode -eq 0) { 'success' } else { 'failed' }
    }
    Write-JsonFile -Path $summaryJsonPath -Data $summary
    $md = @(
        '# Post-1C monitor run summary',
        '',
        "| Field | Value |",
        '|-------|-------|',
        "| Mode | $($summary.mode) |",
        "| Status | $($summary.status) |",
        "| Exit code | $($summary.exit_code) |",
        "| Started | $($summary.started_at_local) |",
        "| Finished | $($summary.finished_at_local) |",
        "| Timezone | $($summary.timezone_id) |",
        "| Python | $($summary.python.Path) ($($summary.python.Version)) |",
        "| Monitor script | $($summary.monitor_script) |",
        "| Run directory | $($summary.run_directory) |",
        '',
        '## Notes',
        '',
        '- Read-only monitor; no Production mutation.',
        '- Full monitor artefacts remain under deployments/SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02/.',
        "- Scheduled logs: ``$($summary.run_directory)``"
    ) -join "`n"
    [System.IO.File]::WriteAllText($summaryMdPath, $md + "`n", [System.Text.UTF8Encoding]::new($false))
    return $ExitCode
}

try {
    Set-Location -LiteralPath $RepoRoot
    "[$($startedAt.ToString('o'))] Runner start mode=$($summary.mode)" | Out-File -FilePath $logPath -Encoding utf8

    $py = Get-PythonExecutable
    if (-not $py) {
        $summary.status = 'failed'
        $summary.error = 'Python executable not found (checked .venv, py, python)'
        "ERROR: $($summary.error)" | Out-File -FilePath $logPath -Append -Encoding utf8
        exit (Finish-Summary -ExitCode 2)
    }
    $summary.python = $py
    "Python: $($py.Path) $($py.Version)" | Out-File -FilePath $logPath -Append -Encoding utf8

    if (-not (Test-Path -LiteralPath $MonitorScript)) {
        $summary.status = 'failed'
        $summary.error = "Monitor script missing: $MonitorScript"
        "ERROR: $($summary.error)" | Out-File -FilePath $logPath -Append -Encoding utf8
        exit (Finish-Summary -ExitCode 3)
    }

    if ($DryRun) {
        $summary.status = 'dry-run-ok'
        "DRY-RUN: environment OK; probing public sitemap HEAD/GET..." | Out-File -FilePath $logPath -Append -Encoding utf8
        try {
            $resp = Invoke-WebRequest -Uri $SitemapUrl -Method Get -UseBasicParsing -TimeoutSec 60 -Headers @{ 'User-Agent' = 'MARS-OCPilot/SITE-002-POST-1C-MONITOR-RUNNER-DRY-RUN' }
            $urlCount = ([regex]::Matches($resp.Content, '<loc>')).Count
            $summary.dry_run_sitemap_probe = @{
                url            = $SitemapUrl
                http_status    = [int]$resp.StatusCode
                content_length = $resp.RawContentLength
                loc_count      = $urlCount
            }
            "DRY-RUN sitemap: HTTP $($resp.StatusCode) loc_count=$urlCount" | Out-File -FilePath $logPath -Append -Encoding utf8
        } catch {
            $summary.dry_run_sitemap_probe = @{ url = $SitemapUrl; error = $_.Exception.Message }
            "DRY-RUN sitemap probe failed (non-fatal for validation): $($_.Exception.Message)" | Out-File -FilePath $logPath -Append -Encoding utf8
        }
        "DRY-RUN complete - full monitor not executed." | Out-File -FilePath $logPath -Append -Encoding utf8
        exit (Finish-Summary -ExitCode 0)
    }

    "Executing monitor: $MonitorScript" | Out-File -FilePath $logPath -Append -Encoding utf8
    $proc = Start-Process -FilePath $py.Path -ArgumentList @($MonitorScript, '--skip-removed-crawl') -WorkingDirectory $RepoRoot -NoNewWindow -Wait -PassThru -RedirectStandardOutput $logPath -RedirectStandardError (Join-Path $runDir 'run.stderr.log')
    $exitCode = $proc.ExitCode
    if ($exitCode -ne 0) {
        $summary.status = 'failed'
        $summary.error = "Monitor exited with code $exitCode"
    } else {
        $summary.status = 'success'
    }
    "Monitor exit code: $exitCode" | Out-File -FilePath $logPath -Append -Encoding utf8
    exit (Finish-Summary -ExitCode $exitCode)
}
catch {
    $summary.status = 'failed'
    $summary.error = $_.Exception.Message
    "FATAL: $($_.Exception.Message)" | Out-File -FilePath $logPath -Append -Encoding utf8
    exit (Finish-Summary -ExitCode 1)
}
