#Requires -Version 5.1
<#
.SYNOPSIS
  SITE-002 read-only post-1C catalog onboarding monitor runner (scheduled/local).

.DESCRIPTION
  Invokes site-002-prod-post-1c-catalog-onboarding-monitor-02.py in read-only mode.
  Writes timestamped logs and hardened artifact contract under
  X:\AI MARS STORAGE\...\scheduled-monitors\post-1c\<timestamp>\
  Does not mutate Production. No credentials printed.

.PARAMETER DryRun
  Validate environment and optionally probe public sitemap only; do not run full monitor.
#>
[CmdletBinding()]
param(
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# Repository root derived from runner path (.../projects/ocpilot/sites/site-002/tools).
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..\..')).Path
$MonitorScript = Join-Path $RepoRoot 'projects\ocpilot\sites\site-002\tools\site-002-prod-post-1c-catalog-onboarding-monitor-02.py'
$ScheduledRoot = 'X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c'
$OperationId = 'SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01'
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
    $json = $Data | ConvertTo-Json -Depth 12
    [System.IO.File]::WriteAllText($Path, $json + "`n", [System.Text.UTF8Encoding]::new($false))
}

function Write-Utf8Line {
    param([string]$Path, [string]$Line, [switch]$Append)
    $utf8 = [System.Text.UTF8Encoding]::new($false)
    if ($Append -and (Test-Path -LiteralPath $Path)) {
        [System.IO.File]::AppendAllText($Path, $Line + "`n", $utf8)
    } else {
        [System.IO.File]::WriteAllText($Path, $Line + "`n", $utf8)
    }
}

function Format-DurationHuman {
    param([double]$Seconds)
    if ($Seconds -lt 1) { return ('{0:N2} seconds' -f $Seconds) }
    $total = [int][math]::Round($Seconds)
    if ($total -lt 60) { return "$total seconds" }
    $minutes = [math]::Floor($total / 60)
    $rem = $total % 60
    if ($minutes -lt 60) { return "${minutes}m ${rem}s" }
    $hours = [math]::Floor($minutes / 60)
    $minutes = $minutes % 60
    return "${hours}h ${minutes}m ${rem}s"
}

function Invoke-MonitorProcess {
    param(
        [string]$PythonPath,
        [string]$ScriptPath,
        [string[]]$ScriptArgs,
        [string]$StdoutPath,
        [string]$StderrPath
    )
    $argList = @($ScriptPath) + $ScriptArgs
    $quotedArgs = ($argList | ForEach-Object {
        if ($_ -match '\s') { '"' + ($_ -replace '"', '\"') + '"' } else { $_ }
    }) -join ' '

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $PythonPath
    $psi.Arguments = $quotedArgs
    $psi.WorkingDirectory = $RepoRoot
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.CreateNoWindow = $true
    $psi.StandardOutputEncoding = [System.Text.Encoding]::UTF8
    $psi.StandardErrorEncoding = [System.Text.Encoding]::UTF8

    $proc = New-Object System.Diagnostics.Process
    $proc.StartInfo = $psi
    [void]$proc.Start()
    $stdout = $proc.StandardOutput.ReadToEnd()
    $stderr = $proc.StandardError.ReadToEnd()
    $proc.WaitForExit()
    $utf8 = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllText($StdoutPath, $stdout, $utf8)
    [System.IO.File]::WriteAllText($StderrPath, $stderr, $utf8)
    return $proc.ExitCode
}

$startedAt = Get-Date
$runDirName = $startedAt.ToString('yyyy-MM-dd_HH-mm-ss')
$runDir = Join-Path $ScheduledRoot $runDirName
New-Item -ItemType Directory -Force -Path $runDir | Out-Null

$logPath = Join-Path $runDir 'run.log'
$stderrPath = Join-Path $runDir 'run.stderr.log'
$summaryJsonPath = Join-Path $runDir 'run-summary.json'
$summaryMdPath = Join-Path $runDir 'run-summary.md'

$summary = [ordered]@{
    run_id                          = $runDirName
    operation_id                    = $OperationId
    runner_script                   = $MyInvocation.MyCommand.Path
    monitor_script                  = $MonitorScript
    mode                            = if ($DryRun) { 'dry-run' } else { 'read-only-monitor' }
    production_url                  = $ProductionUrl
    repo_root                       = $RepoRoot
    run_directory                   = $runDir
    started_at_local                = $startedAt.ToString('o')
    timezone_id                     = [TimeZoneInfo]::Local.Id
    timezone_display                = [TimeZoneInfo]::Local.DisplayName
    python                          = $null
    monitor_script_exists           = (Test-Path -LiteralPath $MonitorScript)
    monitor_script_path_single_argument = $null
    exit_code                       = 0
    status                          = 'pending'
    duration_seconds                = $null
    duration_human                  = $null
    classification                  = $null
    next_action                     = $null
    dry_run_sitemap_probe           = $null
    error                           = $null
}

function Finish-Summary {
    param([int]$ExitCode)
    $finishedAt = Get-Date
    $durationSeconds = ($finishedAt - $startedAt).TotalSeconds
    $summary.exit_code = $ExitCode
    $summary.finished_at_local = $finishedAt.ToString('o')
    $summary.duration_seconds = [math]::Round($durationSeconds, 3)
    $summary.duration_human = Format-DurationHuman -Seconds $durationSeconds
    if (-not $summary.status -or $summary.status -eq 'pending') {
        $summary.status = if ($ExitCode -eq 0) { 'success' } else { 'failed' }
    }
    if (-not $summary.classification) {
        $summary.classification = if ($ExitCode -eq 0) { 'NO_ACTION_REQUIRED' } else { 'FAILURE_REVIEW_REQUIRED' }
    }
    if (-not $summary.next_action) {
        $summary.next_action = if ($ExitCode -eq 0) {
            'Review run-summary.json and monitor-classification.json in run directory.'
        } else {
            'Investigate run.log and run.stderr.log for monitor failure.'
        }
    }

  # Merge monitor-written run-summary if present (richer fields)
    $monitorSummaryPath = Join-Path $runDir 'run-summary.json'
    $merged = @{}
    foreach ($key in $summary.Keys) { $merged[$key] = $summary[$key] }
    if (Test-Path -LiteralPath $monitorSummaryPath) {
        try {
            $monitorSummary = Get-Content -LiteralPath $monitorSummaryPath -Raw -Encoding UTF8 | ConvertFrom-Json
            $monitorSummary.PSObject.Properties | ForEach-Object {
                $merged[$_.Name] = $_.Value
            }
            foreach ($key in $summary.Keys) {
                if ($null -ne $summary[$key]) { $merged[$key] = $summary[$key] }
            }
            $merged['duration_seconds'] = [math]::Round($durationSeconds, 3)
            $merged['duration_human'] = Format-DurationHuman -Seconds $durationSeconds
            $merged['runner_finished_at_local'] = $finishedAt.ToString('o')
        } catch {
            $merged['monitor_summary_merge_error'] = $_.Exception.Message
        }
    }
    Write-JsonFile -Path $summaryJsonPath -Data $merged
    $md = @(
        '# Post-1C monitor run summary',
        '',
        "| Field | Value |",
        '|-------|-------|',
        "| Mode | $($merged.mode) |",
        "| Status | $($merged.status) |",
        "| Exit code | $($merged.exit_code) |",
        "| Duration | $($merged.duration_human) ($($merged.duration_seconds)s) |",
        "| Classification | $($merged.classification) |",
        "| Next action | $($merged.next_action) |",
        "| Started | $($merged.started_at_local) |",
        "| Finished | $($merged.finished_at_local) |",
        "| Timezone | $($merged.timezone_id) |",
        "| Python | $($merged.python.Path) ($($merged.python.Version)) |",
        "| Monitor script | $($merged.monitor_script) |",
        "| Run directory | $($merged.run_directory) |",
        '',
        '## Notes',
        '',
        '- Read-only monitor; no Production mutation.',
        '- Hardened artifacts: added-urls.*, removed-urls.*, sitemap snapshots, hygiene-flags, monitor-classification.',
        "- Scheduled logs: ``$($merged.run_directory)``"
    ) -join "`n"
    [System.IO.File]::WriteAllText($summaryMdPath, $md + "`n", [System.Text.UTF8Encoding]::new($false))
    return $ExitCode
}

try {
    Set-Location -LiteralPath $RepoRoot
    Write-Utf8Line -Path $logPath -Line "[$($startedAt.ToString('o'))] Runner start mode=$($summary.mode)"

    $py = Get-PythonExecutable
    if (-not $py) {
        $summary.status = 'failed'
        $summary.error = 'Python executable not found (checked .venv, py, python)'
        Write-Utf8Line -Path $logPath -Line "ERROR: $($summary.error)" -Append
        exit (Finish-Summary -ExitCode 2)
    }
    $summary.python = $py
    Write-Utf8Line -Path $logPath -Line "Python: $($py.Path) $($py.Version)" -Append

    if (-not (Test-Path -LiteralPath $MonitorScript)) {
        $summary.status = 'failed'
        $summary.error = "Monitor script missing: $MonitorScript"
        Write-Utf8Line -Path $logPath -Line "ERROR: $($summary.error)" -Append
        exit (Finish-Summary -ExitCode 3)
    }

    if ($DryRun) {
        $summary.status = 'dry-run-ok'
        Write-Utf8Line -Path $logPath -Line 'DRY-RUN: environment OK; probing public sitemap HEAD/GET...' -Append
        try {
            $resp = Invoke-WebRequest -Uri $SitemapUrl -Method Get -UseBasicParsing -TimeoutSec 60 -Headers @{ 'User-Agent' = 'MARS-OCPilot/SITE-002-POST-1C-MONITOR-RUNNER-DRY-RUN' }
            $urlCount = ([regex]::Matches($resp.Content, '<loc>')).Count
            $summary.dry_run_sitemap_probe = @{
                url            = $SitemapUrl
                http_status    = [int]$resp.StatusCode
                content_length = $resp.RawContentLength
                loc_count      = $urlCount
            }
            Write-Utf8Line -Path $logPath -Line "DRY-RUN sitemap: HTTP $($resp.StatusCode) loc_count=$urlCount" -Append
        } catch {
            $summary.dry_run_sitemap_probe = @{ url = $SitemapUrl; error = $_.Exception.Message }
            Write-Utf8Line -Path $logPath -Line "DRY-RUN sitemap probe failed (non-fatal for validation): $($_.Exception.Message)" -Append
        }
        Write-Utf8Line -Path $logPath -Line 'DRY-RUN complete - full monitor not executed.' -Append
        $summary.classification = 'NO_ACTION_REQUIRED'
        $summary.next_action = 'Dry-run only — no monitor artifacts beyond runner summary.'
        exit (Finish-Summary -ExitCode 0)
    }

    Write-Utf8Line -Path $logPath -Line "Executing monitor: $MonitorScript" -Append
    Write-Utf8Line -Path $logPath -Line 'Monitor script path passed as single argument: true' -Append
    $summary.monitor_script_path_single_argument = $true

    $monitorArgs = @(
        '--skip-removed-crawl',
        '--scheduled-run-dir', $runDir
    )

    $monitorStdout = Join-Path $runDir 'monitor.stdout.tmp'
    $exitCode = Invoke-MonitorProcess -PythonPath $py.Path -ScriptPath $MonitorScript -ScriptArgs $monitorArgs -StdoutPath $monitorStdout -StderrPath $stderrPath
    if (Test-Path -LiteralPath $monitorStdout) {
        Get-Content -LiteralPath $monitorStdout -Encoding UTF8 | ForEach-Object {
            Write-Utf8Line -Path $logPath -Line $_ -Append
        }
        Remove-Item -LiteralPath $monitorStdout -Force
    }

    if ($null -eq $exitCode) { $exitCode = 0 }
    if ($exitCode -ne 0) {
        $summary.status = 'failed'
        $summary.error = "Monitor exited with code $exitCode"
        $summary.classification = 'FAILURE_REVIEW_REQUIRED'
        $summary.next_action = 'Investigate run.log and run.stderr.log for monitor failure.'
    } else {
        $summary.status = 'success'
    }
    Write-Utf8Line -Path $logPath -Line "Monitor exit code: $exitCode" -Append
    exit (Finish-Summary -ExitCode $exitCode)
}
catch {
    $summary.status = 'failed'
    $summary.error = $_.Exception.Message
    $summary.classification = 'FAILURE_REVIEW_REQUIRED'
    $summary.next_action = 'Investigate runner exception in run.log.'
    Write-Utf8Line -Path $logPath -Line "FATAL: $($_.Exception.Message)" -Append
    exit (Finish-Summary -ExitCode 1)
}
