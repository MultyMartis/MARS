# Corvonero Pre-Phase-6 Checkpoint Builder
$ErrorActionPreference = 'Stop'
if ($env:CORVONERO_OPERATOR_GATE -ne 'APPROVED') {
    Write-Host 'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This script is not safe for casual execution.'
    exit 1
}
$RepoRoot = 'X:\AI MARS'
Set-Location $RepoRoot

function Get-FileSha256($path) {
    if (-not (Test-Path $path)) { return $null }
    return (Get-FileHash -Path $path -Algorithm SHA256).Hash.ToLower()
}

function Get-GitStatusChar($relPath) {
    $s = git status --short -- "$relPath" 2>$null
    if (-not $s) {
        $tracked = git ls-files --error-unmatch -- "$relPath" 2>$null
        if ($LASTEXITCODE -eq 0) { return '  ' } else { return '??' }
    }
    return ($s -split "`n" | Select-Object -First 1).Substring(0,2).TrimEnd()
}

function Test-SecretPatterns($relPath, $fullPath) {
    $name = Split-Path $relPath -Leaf
    if ($name -match '\.env$|\.secrets|credentials|api[_-]?key|authorization') { return $true }
    if ($relPath -match '\.secrets/|node_modules/') { return $true }
    if ($fullPath -and (Test-Path $fullPath)) {
        $ext = [IO.Path]::GetExtension($fullPath).ToLower()
        if ($ext -in @('.env','.pem','.key')) { return $true }
        if ($name -match 'raw-auth|authorization-header') { return $true }
    }
    return $false
}

# ORCA live-model report dirs referenced by repair v2 + run 003
$orcaReportDirs = @(
    'sppc05-defect-repro-1782433956822',
    'sppc05-defect-repro-1782467510540',
    'sppc05-defect-repro-1782478143382',
    'platform-compatibility-regression-1782478501903',
    'problem-policy-regression-1782478317421',
    'confirmation-sppc05-repair-v2-product-pass-pass-1782481444825',
    'confirmation-sppc05-repair-v2-geo-pass-pass-1782485788024',
    'closed-regression-1782485791111',
    'sppc05-variance-1782485788046',
    'sppc05-variance-1782434048887',
    'confirmation-sppc05-repair-product-pass-1782434048184',
    'confirmation-sppc05-repair-geo-pass-1782434729512'
)

$orcaFiles = @(
    'projects/orca/reports/REPORT-orca-wave31f-targeted-sppc05-repair-v1.md',
    'projects/orca/reports/REPORT-orca-wave31f-targeted-sppc05-repair-v2.md',
    'projects/orca/semantic-intelligence/ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v1.json',
    'projects/orca/semantic-intelligence/ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v1.md',
    'projects/orca/semantic-intelligence/ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.json',
    'projects/orca/semantic-intelligence/ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.md',
    'projects/orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs',
    'projects/orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs',
    'projects/orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs',
    'projects/orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs',
    'projects/orca/semantic-intelligence/production/assessors/hard-rules.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-platform-compatibility-regression.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-variance-check.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs',
    'projects/orca/semantic-intelligence/live-model/tests/run-closed-dataset-regression.mjs'
)

foreach ($d in $orcaReportDirs) {
    $base = "projects/orca/semantic-intelligence/live-model/reports/$d"
    if (Test-Path $base) {
        Get-ChildItem -Path $base -Recurse -File | ForEach-Object {
            $rel = $_.FullName.Substring($RepoRoot.Length + 1).Replace('\','/')
            $orcaFiles += $rel
        }
    }
}
$orcaFiles = $orcaFiles | Select-Object -Unique

# Collect corvonero pilot + report files
$inventory = @()
Get-ChildItem -Path 'projects/mars-search-ppc-production/pilots/corvonero' -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($RepoRoot.Length + 1).Replace('\','/')
    if (Test-SecretPatterns $rel $_.FullName) { return }
    $inventory += [PSCustomObject]@{
        path = $rel
        git_status = Get-GitStatusChar $rel
        size_bytes = $_.Length
        sha256 = Get-FileSha256 $_.FullName
        inclusion_reason = 'corvonero pilot directory'
        source_phase = 'Run 004 lifecycle'
        sanitized = ($rel -match 'sanitized')
        secrets_or_raw_provider = $false
    }
}

Get-ChildItem -Path 'projects/mars-search-ppc-production/reports' -Filter '*corvonero*' -File | ForEach-Object {
    $rel = $_.FullName.Substring($RepoRoot.Length + 1).Replace('\','/')
    $inventory += [PSCustomObject]@{
        path = $rel
        git_status = Get-GitStatusChar $rel
        size_bytes = $_.Length
        sha256 = Get-FileSha256 $_.FullName
        inclusion_reason = 'corvonero report'
        source_phase = 'Run 004 lifecycle'
        sanitized = $false
        secrets_or_raw_provider = $false
    }
}

foreach ($of in $orcaFiles) {
    $full = Join-Path $RepoRoot ($of -replace '/','\')
    if (-not (Test-Path $full)) { continue }
    if ($inventory.path -contains $of) { continue }
    $fi = Get-Item $full
    $inventory += [PSCustomObject]@{
        path = $of
        git_status = Get-GitStatusChar $of
        size_bytes = $fi.Length
        sha256 = Get-FileSha256 $full
        inclusion_reason = 'ORCA SPPC-05 repair evidence'
        source_phase = 'ORCA Wave 3.1F repair'
        sanitized = $false
        secrets_or_raw_provider = (Test-SecretPatterns $of $full)
    }
}

$inventory = $inventory | Where-Object { -not $_.secrets_or_raw_provider } | Sort-Object path -Unique
$inventory | ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 '.tools/corvonero-checkpoint-inventory.json'
Write-Output "INVENTORY_COUNT=$($inventory.Count)"

# Phase 5.2 verification
$base = 'projects/mars-search-ppc-production/pilots/corvonero'
$accept = Get-Content "$base/CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json" -Raw | ConvertFrom-Json
$reject = Get-Content "$base/CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json" -Raw | ConvertFrom-Json
$abstain = Get-Content "$base/CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json" -Raw | ConvertFrom-Json
$reviewed = Get-Content "$base/CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json" -Raw | ConvertFrom-Json
$signoff = Get-Content "$base/CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json" -Raw | ConvertFrom-Json

Write-Output "PHASE52 reviewed=$($reviewed.count) accept=$($accept.count) reject=$($reject.count) abstain=$($abstain.count)"
Write-Output "PHASE52 integrity=$($signoff.integrity.pass) union=$($signoff.integrity.union) unprocessed=$($signoff.integrity.unprocessed_ids)"

$preHead = git rev-parse HEAD
Write-Output "PRE_HEAD=$preHead"
