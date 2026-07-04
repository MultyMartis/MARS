$ErrorActionPreference = 'Stop'
if ($env:CORVONERO_OPERATOR_GATE -ne 'APPROVED') {
    Write-Host 'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This script is not safe for casual execution.'
    exit 1
}
$RepoRoot = 'X:\AI MARS'
Set-Location $RepoRoot

# Stage corvonero pilot tree
git add -- 'projects/mars-search-ppc-production/pilots/corvonero/'

# Stage corvonero reports
Get-ChildItem 'projects/mars-search-ppc-production/reports' -Filter '*corvonero*' -File | ForEach-Object {
  git add -- $_.FullName.Replace("$RepoRoot\", '').Replace('\','/')
}

# Stage ORCA repair evidence (explicit paths)
$orcaPaths = @(
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
foreach ($p in $orcaPaths) {
  if (Test-Path $p) { git add -- $p }
}
foreach ($d in $orcaReportDirs) {
  $base = "projects/orca/semantic-intelligence/live-model/reports/$d"
  if (Test-Path $base) { git add -- "$base/" }
}

Write-Output '=== STAGED FILES ==='
git diff --cached --name-status
Write-Output '=== STAGED STAT ==='
git diff --cached --stat

# Verify no forbidden paths staged
$staged = git diff --cached --name-only
$forbidden = $staged | Where-Object {
  $_ -match '^workspaces/fp-0002|^projects/ocpilot|^projects/projects/' -or
  $_ -match '\.secrets|\.env$|credentials'
}
if ($forbidden) {
  Write-Output "FORBIDDEN_STAGED=$($forbidden -join ',')"
  foreach ($f in $forbidden) { git reset HEAD -- $f }
  Write-Output 'UNSTAGED_FORBIDDEN'
}

$commitMsg = @'
checkpoint(corvonero): freeze partial semantic authority before phase 6

Run: corv-semantic-v2-20260626-004
Phase 5.2: PASS
Assessed: 1599/2368
ACCEPT: 935
REJECT: 368
ABSTAIN: 296
Backlog: 769
OpenRouter: frozen
Phase 6: not started
'@

git commit -m $commitMsg
if ($LASTEXITCODE -ne 0) { throw 'Commit failed' }

$commitSha = git rev-parse HEAD
Write-Output "COMMIT_SHA=$commitSha"
git show --stat --oneline --decorate HEAD
Write-Output '=== COMMIT DIFF NAME-STATUS ==='
git diff HEAD^ HEAD --name-status

# Update checkpoint receipt with commit SHA
$cpPath = 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PRE-PHASE-6-CHECKPOINT-v1.json'
$cp = Get-Content $cpPath -Raw | ConvertFrom-Json
$cp.git_commit_sha = $commitSha
$cp | ConvertTo-Json -Depth 6 | Set-Content -Encoding UTF8 $cpPath
git add -- $cpPath
git commit --amend --no-edit

$tagName = 'corvonero-phase5.2-partial-semantic-approved-2026-06'
$tagMsg = @'
Corvonero Run 004 — Phase 5.2 operator-approved partial semantic authority.
1599/2368 assessed; 935 ACCEPT, 368 REJECT, 296 ABSTAIN.
769 IDs preserved as unprocessed backlog.
OpenRouter frozen. Phase 6 not started.
'@
git tag -a $tagName -m $tagMsg
Write-Output "TAG_CREATED=$tagName"

Write-Output '=== PUSH BRANCH ==='
git push origin mars/canonical-post-recovery 2>&1
Write-Output "PUSH_BRANCH_EXIT=$LASTEXITCODE"
Write-Output '=== PUSH TAG ==='
git push origin $tagName 2>&1
Write-Output "PUSH_TAG_EXIT=$LASTEXITCODE"
