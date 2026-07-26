#Requires -Version 5.1
<#
.SYNOPSIS
  Offline regression for SITE-002 Finish-Summary semantic authority (D5R-MON).

.DESCRIPTION
  Side-effect safe: does NOT execute the production runner top-level flow,
  does NOT invoke the Python monitor, does NOT touch Storage scheduled roots,
  does NOT contact the network. Uses AST extraction of pure merge helpers from
  site-002-post-1c-monitor-runner.ps1 and temp-local JSON only.
#>
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$RunnerPath = Join-Path $PSScriptRoot 'site-002-post-1c-monitor-runner.ps1'
if (-not (Test-Path -LiteralPath $RunnerPath)) {
    Write-Error "Runner not found: $RunnerPath"
    exit 2
}

function Assert-True {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) { throw "ASSERT: $Message" }
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

function Add-Result {
    param(
        [System.Collections.Generic.List[object]]$Results,
        [string]$Id,
        [bool]$Pass,
        [string]$Detail
    )
    $Results.Add([pscustomobject]@{ id = $Id; pass = $Pass; detail = $Detail })
    $mark = if ($Pass) { 'PASS' } else { 'FAIL' }
    Write-Host "[$mark] $Id - $Detail"
}

function Invoke-FinishSummarySimulation {
    param(
        [hashtable]$RunnerSummary,
        [object]$MonitorSummaryObject,
        [string]$RunDirectory,
        [int]$ExitCode = 0,
        [double]$DurationSeconds = 1.5
    )
    $finishedAt = Get-Date
    $merged = Merge-RunnerMetadataPreservingMonitorSemantics `
        -RunnerSummary $RunnerSummary `
        -MonitorSummaryObject $MonitorSummaryObject `
        -DurationSeconds $DurationSeconds `
        -FinishedAt $finishedAt `
        -FormatDuration ${function:Format-DurationHuman}
    $present = $null -ne $MonitorSummaryObject
    return (Complete-RunSummarySemanticDefaults `
        -Merged $merged `
        -ExitCode $ExitCode `
        -RunDirectory $RunDirectory `
        -MonitorSummaryPresent $present)
}

# --- Static / syntax proofs (no execution of runner top-level) ---
$tokens = $null
$parseErrors = $null
$ast = [System.Management.Automation.Language.Parser]::ParseFile($RunnerPath, [ref]$tokens, [ref]$parseErrors)
$errText = (($parseErrors | ForEach-Object { $_.ToString() }) -join '; ')
Assert-True ($parseErrors.Count -eq 0) "Runner parse errors: $errText"

$runnerText = [System.IO.File]::ReadAllText($RunnerPath)
Assert-True ($runnerText -match 'Merge-RunnerMetadataPreservingMonitorSemantics') 'Helper Merge-RunnerMetadataPreservingMonitorSemantics missing'
Assert-True ($runnerText -match 'Complete-RunSummarySemanticDefaults') 'Helper Complete-RunSummarySemanticDefaults missing'
Assert-True ($runnerText -match 'Do not default classification/next_action before merge') 'Preservation comment missing'
$oldBugPattern = 'if\s*\(-not\s*\$summary\.classification\)\s*\{\s*\$summary\.classification\s*=\s*if\s*\(\$ExitCode\s*-eq\s*0\)\s*\{\s*''NO_ACTION_REQUIRED'''
$oldBug = [regex]::Match($runnerText, $oldBugPattern)
Assert-True (-not $oldBug.Success) 'Old pre-merge NO_ACTION_REQUIRED default still present on summary'

$wanted = @(
    'Test-NonEmptySemanticValue',
    'Merge-RunnerMetadataPreservingMonitorSemantics',
    'Complete-RunSummarySemanticDefaults'
)
$funcAsts = $ast.FindAll({
        param($node)
        $node -is [System.Management.Automation.Language.FunctionDefinitionAst] -and $wanted -contains $node.Name
    }, $true)

Assert-True ($funcAsts.Count -eq 3) "Expected 3 helper functions via AST, got $($funcAsts.Count)"
foreach ($fn in $funcAsts) {
    Invoke-Expression $fn.Extent.Text
}

$results = New-Object 'System.Collections.Generic.List[object]'
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ('site002-d5r-mon-reg-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null

try {
    # CASE A — ONBOARDING preserved despite runner empty/default temptation
    $runA = Join-Path $tempRoot 'case-a'
    New-Item -ItemType Directory -Force -Path $runA | Out-Null
    $monitorA = [pscustomobject]@{
        classification = 'ONBOARDING_REQUIRED'
        next_action    = 'SYNTHETIC_ONBOARDING_ACTION'
        added_count    = 119
        status         = 'success'
    }
    $runnerA = @{
        classification = 'NO_ACTION_REQUIRED'
        next_action    = 'Review run-summary.json and monitor-classification.json in run directory.'
        exit_code      = 0
        status         = 'success'
        runner_script  = 'synthetic'
    }
    $outA = Invoke-FinishSummarySimulation -RunnerSummary $runnerA -MonitorSummaryObject $monitorA -RunDirectory $runA -ExitCode 0
    Add-Result -Results $results -Id 'A_ONBOARDING_PRESERVE' -Pass (
        $outA.classification -eq 'ONBOARDING_REQUIRED' -and $outA.next_action -eq 'SYNTHETIC_ONBOARDING_ACTION'
    ) -Detail ("classification=$($outA.classification); next_action=$($outA.next_action)")

    # CASE B — NO_ACTION preserved
    $runB = Join-Path $tempRoot 'case-b'
    New-Item -ItemType Directory -Force -Path $runB | Out-Null
    $monitorB = [pscustomobject]@{ classification = 'NO_ACTION_REQUIRED'; next_action = 'NONE'; status = 'success' }
    $runnerB = @{ classification = $null; next_action = $null; exit_code = 0; status = 'success' }
    $outB = Invoke-FinishSummarySimulation -RunnerSummary $runnerB -MonitorSummaryObject $monitorB -RunDirectory $runB -ExitCode 0
    Add-Result -Results $results -Id 'B_NO_ACTION_PRESERVE' -Pass ($outB.classification -eq 'NO_ACTION_REQUIRED') -Detail ("classification=$($outB.classification)")

    # CASE C — HYGIENE preserved
    $runC = Join-Path $tempRoot 'case-c'
    New-Item -ItemType Directory -Force -Path $runC | Out-Null
    $monitorC = [pscustomobject]@{ classification = 'HYGIENE_REVIEW_REQUIRED'; next_action = 'REVIEW_HYGIENE'; status = 'success' }
    $runnerC = @{ classification = 'NO_ACTION_REQUIRED'; next_action = 'default'; exit_code = 0; status = 'success' }
    $outC = Invoke-FinishSummarySimulation -RunnerSummary $runnerC -MonitorSummaryObject $monitorC -RunDirectory $runC -ExitCode 0
    Add-Result -Results $results -Id 'C_HYGIENE_PRESERVE' -Pass (
        $outC.classification -eq 'HYGIENE_REVIEW_REQUIRED' -and $outC.next_action -eq 'REVIEW_HYGIENE'
    ) -Detail ("classification=$($outC.classification); next_action=$($outC.next_action)")

    # CASE D — FAILURE preserved when canonical summary exists
    $runD = Join-Path $tempRoot 'case-d'
    New-Item -ItemType Directory -Force -Path $runD | Out-Null
    $monitorD = [pscustomobject]@{ classification = 'FAILURE_REVIEW_REQUIRED'; next_action = 'CHECK_LOGS'; status = 'failed' }
    $runnerD = @{ classification = 'FAILURE_REVIEW_REQUIRED'; next_action = 'Investigate run.log'; exit_code = 1; status = 'failed' }
    $outD = Invoke-FinishSummarySimulation -RunnerSummary $runnerD -MonitorSummaryObject $monitorD -RunDirectory $runD -ExitCode 1
    Add-Result -Results $results -Id 'D_FAILURE_PRESERVE' -Pass (
        $outD.classification -eq 'FAILURE_REVIEW_REQUIRED' -and $outD.next_action -eq 'CHECK_LOGS'
    ) -Detail ("classification=$($outD.classification); next_action=$($outD.next_action)")

    # CASE E — missing classification in run-summary; prefer monitor-classification.json
    $runE = Join-Path $tempRoot 'case-e'
    New-Item -ItemType Directory -Force -Path $runE | Out-Null
    @{ classification = 'ONBOARDING_REQUIRED'; next_action = 'FROM_MONITOR_CLASSIFICATION' } |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $runE 'monitor-classification.json') -Encoding UTF8
    $monitorE = [pscustomobject]@{ status = 'success'; added_count = 3 }
    $runnerE = @{ classification = $null; next_action = $null; exit_code = 0; status = 'success' }
    $outE = Invoke-FinishSummarySimulation -RunnerSummary $runnerE -MonitorSummaryObject $monitorE -RunDirectory $runE -ExitCode 0
    Add-Result -Results $results -Id 'E_MISSING_USE_MONITOR_CLASSIFICATION' -Pass (
        $outE.classification -eq 'ONBOARDING_REQUIRED' -and $outE.next_action -eq 'FROM_MONITOR_CLASSIFICATION'
    ) -Detail ("classification=$($outE.classification); next_action=$($outE.next_action)")

    # CASE E2 — missing everywhere with summary present → fail-safe FAILURE_REVIEW (no silent OK)
    $runE2 = Join-Path $tempRoot 'case-e2'
    New-Item -ItemType Directory -Force -Path $runE2 | Out-Null
    $monitorE2 = [pscustomobject]@{ status = 'success'; added_count = 1 }
    $runnerE2 = @{ classification = $null; next_action = $null; exit_code = 0; status = 'success' }
    $outE2 = Invoke-FinishSummarySimulation -RunnerSummary $runnerE2 -MonitorSummaryObject $monitorE2 -RunDirectory $runE2 -ExitCode 0
    Add-Result -Results $results -Id 'E2_MISSING_FAILSAFE_NO_SILENT_OK' -Pass (
        $outE2.classification -eq 'FAILURE_REVIEW_REQUIRED'
    ) -Detail ("classification=$($outE2.classification)")

    # CASE F — no monitor summary (process failed before artifacts) → runner failure semantics
    $runF = Join-Path $tempRoot 'case-f'
    New-Item -ItemType Directory -Force -Path $runF | Out-Null
    $runnerF = @{
        classification = 'FAILURE_REVIEW_REQUIRED'
        next_action    = 'Investigate runner exception in run.log.'
        exit_code      = 1
        status         = 'failed'
    }
    $outF = Invoke-FinishSummarySimulation -RunnerSummary $runnerF -MonitorSummaryObject $null -RunDirectory $runF -ExitCode 1
    Add-Result -Results $results -Id 'F_NO_MONITOR_SUMMARY_FAILURE' -Pass (
        $outF.classification -eq 'FAILURE_REVIEW_REQUIRED'
    ) -Detail ("classification=$($outF.classification)")

    Add-Result -Results $results -Id 'G_METADATA_ENRICHMENT' -Pass (
        $null -ne $outA.duration_seconds -and $null -ne $outA.duration_human -and $null -ne $outA.runner_finished_at_local -and $outA.exit_code -eq 0
    ) -Detail ("duration=$($outA.duration_seconds); human=$($outA.duration_human)")

    Add-Result -Results $results -Id 'H_NEXT_ACTION_PRESERVE' -Pass ($outA.next_action -eq 'SYNTHETIC_ONBOARDING_ACTION') -Detail $outA.next_action
    Add-Result -Results $results -Id 'I_RUNNER_SYNTAX' -Pass ($parseErrors.Count -eq 0) -Detail 'Parser errors=0'
    Add-Result -Results $results -Id 'J_NO_STORAGE_PATH_IN_TEMP_PROOF' -Pass ($tempRoot -notmatch 'AI MARS STORAGE') -Detail ("tempRoot=$tempRoot")
}
finally {
    if (Test-Path -LiteralPath $tempRoot) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}

$failed = @($results | Where-Object { -not $_.pass }).Count
$passed = @($results | Where-Object { $_.pass }).Count
Write-Host ''
Write-Host "RESULT: $passed/$($results.Count) PASS (failed=$failed)"
if ($failed -gt 0) { exit 1 }
exit 0
