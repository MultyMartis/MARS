$ErrorActionPreference = 'Stop'
if ($env:CORVONERO_OPERATOR_GATE -ne 'APPROVED') {
    Write-Host 'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This script is not safe for casual execution.'
    exit 1
}
$RepoRoot = 'X:\AI MARS'
$StorageRoot = 'X:\AI MARS STORAGE'
Set-Location $RepoRoot
$ts = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffZ')
$preHead = '9e8fa083cf957e0b05a212db88165709bd488e8b'
$inv = Get-Content '.tools/corvonero-checkpoint-inventory.json' -Raw | ConvertFrom-Json

$md = @()
$md += '# REPORT — Corvonero Pre-Phase-6 Checkpoint Inventory v1'
$md += ''
$md += "Generated: $ts"
$md += "Pre-commit HEAD: ``$preHead``"
$md += 'Run ID: corv-semantic-v2-20260626-004'
$md += "Eligible file count: $($inv.Count)"
$md += ''
$md += '## Inclusion families'
$md += '- ``projects/mars-search-ppc-production/pilots/corvonero/**``'
$md += '- ``projects/mars-search-ppc-production/reports/*corvonero*``'
$md += '- ORCA SPPC-05 repair evidence (referenced live-model reports + repair code/tests/decisions)'
$md += ''
$md += '## Excluded patterns'
$md += '- API keys, ``.secrets``, credentials, raw authorization headers'
$md += '- ``projects/projects/`` duplicate tree'
$md += '- Unrelated OCPilot, FP-0002, Website Factory WIP'
$md += '- Unreferenced ORCA live-model report directories'
$md += ''
$md += '## File inventory'
$md += ''
$md += '| Path | Git | Size | SHA-256 prefix | Reason | Phase | Sanitized |'
$md += '|------|-----|------|----------------|--------|-------|-----------|'
foreach ($f in ($inv | Sort-Object path)) {
  $sha = if ($f.sha256.Length -gt 16) { $f.sha256.Substring(0,16) + '...' } else { $f.sha256 }
  $line = '| ``' + $f.path + '`` | ' + $f.git_status + ' | ' + $f.size_bytes + ' | ``' + $sha + '`` | ' + $f.inclusion_reason + ' | ' + $f.source_phase + ' | ' + $f.sanitized + ' |'
  $md += $line
}
$mdPath = 'projects/mars-search-ppc-production/reports/REPORT-corvonero-pre-phase6-checkpoint-inventory-v1.md'
$md -join "`n" | Set-Content -Encoding UTF8 $mdPath

$checkpoint = @{
  checkpoint_id = 'CORVONERO-PRE-PHASE-6-CHECKPOINT-v1'
  purpose = 'Freeze partial semantic authority (Phase 5.2 PASS) before Phase 6 campaign planning'
  repository_path = $RepoRoot
  branch = 'mars/canonical-post-recovery'
  pre_commit_head = $preHead
  run_id = 'corv-semantic-v2-20260626-004'
  lifecycle = 'READY_FOR_PARTIAL_CAMPAIGN_PLANNING'
  phase_52 = @{
    verdict = 'PASS'
    partial_semantic_authority = 'OPERATOR APPROVED'
    assessed = 1599
    canonical_total = 2368
    accept = 935
    reject = 368
    abstain = 296
    unprocessed_backlog = 769
    blocking_review_flags = 0
    duplicates = 0
    overlap = 0
    union = 2368
  }
  partial_coverage_limitation = '769 IDs preserved as unprocessed backlog; not part of partial semantic authority'
  provider_calls = 'FROZEN'
  phase_6 = 'NOT STARTED'
  campaign_architecture = 'NOT STARTED'
  inventory_reference = 'projects/mars-search-ppc-production/reports/REPORT-corvonero-pre-phase6-checkpoint-inventory-v1.md'
  inventory_file_count = $inv.Count
  excluded_unrelated_wip = @('workspaces/fp-0002-*','projects/ocpilot/*','unreferenced ORCA live-model reports','projects/projects/')
  external_archive_target = "$StorageRoot\backups\corvonero\CORVONERO-PRE-PHASE-6-CHECKPOINT-2026-06-28"
  git_commit_sha = 'PENDING'
  git_tag = 'corvonero-phase5.2-partial-semantic-approved-2026-06'
  created_at = $ts
  historical_boundaries = @{
    run_002 = 'IMMUTABLE FAILED EVIDENCE'
    run_003 = 'IMMUTABLE FAILED EVIDENCE'
    run_004 = 'CURRENT APPROVED PARTIAL AUTHORITY'
    phase3_attempt1 = 'IMMUTABLE FAILED HARNESS EVIDENCE'
    phase3_attempt2 = 'APPROVED CANARY AUTHORITY'
  }
}
$cpJson = 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PRE-PHASE-6-CHECKPOINT-v1.json'
$checkpoint | ConvertTo-Json -Depth 6 | Set-Content -Encoding UTF8 $cpJson

$cpMd = @(
'# CORVONERO PRE-PHASE-6 CHECKPOINT v1',
'',
'**Purpose:** Safe selective backup and Git checkpoint freezing Run 004 Phase 5.2 partial semantic authority before Phase 6.',
'',
'| Field | Value |',
'|-------|-------|',
"| Repository | ``$RepoRoot`` |",
'| Branch | ``mars/canonical-post-recovery`` |',
"| Pre-commit HEAD | ``$preHead`` |",
'| Run ID | ``corv-semantic-v2-20260626-004`` |',
'| Lifecycle | ``READY_FOR_PARTIAL_CAMPAIGN_PLANNING`` |',
'| Phase 5.2 | **PASS** — partial semantic authority **OPERATOR APPROVED** |',
'| Assessed | 1599 / 2368 |',
'| ACCEPT | 935 |',
'| REJECT | 368 |',
'| ABSTAIN | 296 |',
'| Unprocessed backlog | 769 |',
'| Provider calls | **FROZEN** |',
'| Phase 6 | **NOT STARTED** |',
'',
'## Partial coverage limitation',
'769 phrase IDs remain unprocessed and are explicitly excluded from partial semantic authority until a future operator decision.',
'',
'## Inventory',
"See ``$($checkpoint.inventory_reference)`` ($($inv.Count) eligible repository files).",
'',
'## Excluded unrelated WIP',
'- FP-0002 workspace changes',
'- OCPilot site-002 work',
'- Unreferenced ORCA live-model reports',
'- ``projects/projects/`` duplicate tree',
'',
'## External archive',
"Target: ``$($checkpoint.external_archive_target)``",
'',
'## Git checkpoint placeholders',
'- Commit SHA: *pending*',
'- Tag: ``corvonero-phase5.2-partial-semantic-approved-2026-06``',
'',
"Generated: $ts"
) -join "`n"
$cpMd | Set-Content -Encoding UTF8 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PRE-PHASE-6-CHECKPOINT-v1.md'
Write-Output 'RECEIPTS_CREATED'
