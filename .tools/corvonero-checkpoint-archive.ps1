$ErrorActionPreference = 'Stop'
if ($env:CORVONERO_OPERATOR_GATE -ne 'APPROVED') {
    Write-Host 'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This script is not safe for casual execution.'
    exit 1
}
$RepoRoot = 'X:\AI MARS'
$StorageRoot = 'X:\AI MARS STORAGE'
$BackupBase = Join-Path $StorageRoot 'backups\corvonero'
$ArchiveDirName = 'CORVONERO-PRE-PHASE-6-CHECKPOINT-2026-06-28'
$ArchiveDir = Join-Path $BackupBase $ArchiveDirName
$suffix = 2
while (Test-Path $ArchiveDir) {
  $ArchiveDir = Join-Path $BackupBase "$ArchiveDirName-{0:D3}" -f $suffix
  $suffix++
}
New-Item -ItemType Directory -Path $ArchiveDir -Force | Out-Null
$Staging = Join-Path $ArchiveDir 'staging'
New-Item -ItemType Directory -Path $Staging -Force | Out-Null

$commitSha = (git -C $RepoRoot rev-parse HEAD).Trim()
$tagName = 'corvonero-phase5.2-partial-semantic-approved-2026-06'
$ts = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.fffZ')

function Copy-Tree($src, $dest) {
  if (-not (Test-Path $src)) { return }
  New-Item -ItemType Directory -Path (Split-Path $dest -Parent) -Force | Out-Null
  Copy-Item -Path $src -Destination $dest -Recurse -Force
}

# Repository snapshot paths
$repoStaging = Join-Path $Staging 'repository'
Copy-Tree (Join-Path $RepoRoot 'projects\mars-search-ppc-production\pilots\corvonero') (Join-Path $repoStaging 'projects\mars-search-ppc-production\pilots\corvonero')

Get-ChildItem (Join-Path $RepoRoot 'projects\mars-search-ppc-production\reports') -Filter '*corvonero*' | ForEach-Object {
  $destDir = Join-Path $repoStaging 'projects\mars-search-ppc-production\reports'
  New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  Copy-Item $_.FullName (Join-Path $destDir $_.Name) -Force
}

$orcaReportDirs = @(
  'sppc05-defect-repro-1782433956822','sppc05-defect-repro-1782467510540','sppc05-defect-repro-1782478143382',
  'platform-compatibility-regression-1782478501903','problem-policy-regression-1782478317421',
  'confirmation-sppc05-repair-v2-product-pass-pass-1782481444825','confirmation-sppc05-repair-v2-geo-pass-pass-1782485788024',
  'closed-regression-1782485791111','sppc05-variance-1782485788046','sppc05-variance-1782434048887',
  'confirmation-sppc05-repair-product-pass-1782434048184','confirmation-sppc05-repair-geo-pass-1782434729512'
)
$orcaFiles = @(
  'projects\orca\reports\REPORT-orca-wave31f-targeted-sppc05-repair-v1.md',
  'projects\orca\reports\REPORT-orca-wave31f-targeted-sppc05-repair-v2.md',
  'projects\orca\semantic-intelligence\ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v1.json',
  'projects\orca\semantic-intelligence\ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v1.md',
  'projects\orca\semantic-intelligence\ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.json',
  'projects\orca\semantic-intelligence\ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.md',
  'projects\orca\semantic-intelligence\live-model\adjudication\semantic-adjudicator.mjs',
  'projects\orca\semantic-intelligence\live-model\contracts\prompt-contract.mjs',
  'projects\orca\semantic-intelligence\live-model\evidence\service-intent-evidence.mjs',
  'projects\orca\semantic-intelligence\live-model\evidence\platform-compatibility.mjs',
  'projects\orca\semantic-intelligence\production\assessors\hard-rules.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-sppc05-defect-repro.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-platform-compatibility-regression.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-under-admission-regression.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-sppc05-variance-check.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-wave31f-bypass-audit.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-problem-query-policy-regression.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-confirmation-validation.mjs',
  'projects\orca\semantic-intelligence\live-model\tests\run-closed-dataset-regression.mjs'
)
foreach ($rel in $orcaFiles) {
  $src = Join-Path $RepoRoot $rel
  if (Test-Path $src) {
    $dest = Join-Path $repoStaging ($rel -replace '\\','\\')
    New-Item -ItemType Directory -Path (Split-Path $dest -Parent) -Force | Out-Null
    Copy-Item $src $dest -Force
  }
}
foreach ($d in $orcaReportDirs) {
  $src = Join-Path $RepoRoot "projects\orca\semantic-intelligence\live-model\reports\$d"
  $dest = Join-Path $repoStaging "projects\orca\semantic-intelligence\live-model\reports\$d"
  Copy-Tree $src $dest
}

# Git metadata
$gitMeta = Join-Path $repoStaging 'git-metadata'
New-Item -ItemType Directory -Path $gitMeta -Force | Out-Null
@{
  branch = 'mars/canonical-post-recovery'
  checkpoint_commit = $commitSha
  pre_commit_head = '9e8fa083cf957e0b05a212db88165709bd488e8b'
  tag = $tagName
  run_id = 'corv-semantic-v2-20260626-004'
  created_at = $ts
} | ConvertTo-Json -Depth 4 | Set-Content (Join-Path $gitMeta 'checkpoint-git-metadata-v1.json') -Encoding UTF8
git -C $RepoRoot log -1 --format=fuller $commitSha | Set-Content (Join-Path $gitMeta 'commit-log-v1.txt') -Encoding UTF8
git -C $RepoRoot cat-file -p $tagName | Set-Content (Join-Path $gitMeta 'tag-object-v1.txt') -Encoding UTF8

# STORAGE snapshot — Run 004, exclude locks and secrets
$storageSrc = Join-Path $StorageRoot 'mig\corvonero\semantic-runs\corv-semantic-v2-20260626-004'
$storageDest = Join-Path $Staging 'storage\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-004'
if (Test-Path $storageSrc) {
  $excludeDirs = @('locks')
  Get-ChildItem $storageSrc -Directory | Where-Object { $_.Name -notin $excludeDirs } | ForEach-Object {
    Copy-Tree $_.FullName (Join-Path $storageDest $_.Name)
  }
}

# Build file list for manifest
$allFiles = Get-ChildItem $Staging -Recurse -File
$fileEntries = @()
foreach ($f in $allFiles) {
  $rel = $f.FullName.Substring($Staging.Length + 1).Replace('\','/')
  if ($rel -match '\.env$|\.secrets|credentials|api[_-]?key') { continue }
  $fileEntries += [PSCustomObject]@{
    path = $rel
    size_bytes = $f.Length
    sha256 = (Get-FileHash $f.FullName -Algorithm SHA256).Hash.ToLower()
  }
}

# Critical registry hashes from repo
$critical = @(
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-CORRECTION-LEDGER-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json',
  'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'
)
$criticalHashes = @{}
foreach ($c in $critical) {
  $full = Join-Path $RepoRoot ($c -replace '/','\')
  if (Test-Path $full) {
    $criticalHashes[$c] = (Get-FileHash $full -Algorithm SHA256).Hash.ToLower()
  }
}

$receiptPath = Join-Path $RepoRoot 'projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-PRE-PHASE-6-CHECKPOINT-v1.json'
$receiptSha = (Get-FileHash $receiptPath -Algorithm SHA256).Hash.ToLower()

# Create ZIP
$zipBaseName = 'CORVONERO-PRE-PHASE-6-CHECKPOINT-2026-06-28'
$zipPath = Join-Path $ArchiveDir "$zipBaseName.zip"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $Staging '*') -DestinationPath $zipPath -CompressionLevel Optimal
$zipSize = (Get-Item $zipPath).Length
$zipSha = (Get-FileHash $zipPath -Algorithm SHA256).Hash.ToLower()

$manifest = @{
  archive_filename = "$zipBaseName.zip"
  archive_byte_size = $zipSize
  archive_sha256 = $zipSha
  creation_timestamp = $ts
  repository_branch = 'mars/canonical-post-recovery'
  checkpoint_commit_sha = $commitSha
  tag = $tagName
  run_id = 'corv-semantic-v2-20260626-004'
  phase_52 = @{
    assessed = 1599; accept = 935; reject = 368; abstain = 296
    unprocessed = 769; union = 2368; blocking_flags = 0
  }
  included_file_count = $fileEntries.Count
  excluded_security_patterns = @('.secrets','*.env','credentials','api_key','authorization-header','locks/')
  source_roots = @(
    'X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero',
    'X:\AI MARS\projects\mars-search-ppc-production\reports\*corvonero*',
    'X:\AI MARS\projects\orca\ (SPPC-05 repair evidence only)',
    'X:\AI MARS STORAGE\mig\corvonero\semantic-runs\corv-semantic-v2-20260626-004'
  )
  partial_coverage_warning = '769 IDs unprocessed; partial semantic authority only covers 1599 assessed IDs'
  restore_notes = 'Extract ZIP to isolated path; verify archive_sha256; compare critical registry hashes; do not overwrite live STORAGE without operator approval'
  critical_registry_hashes = $criticalHashes
  checkpoint_receipt_sha256 = $receiptSha
  files = $fileEntries
}
$manifestPath = Join-Path $ArchiveDir "$zipBaseName-MANIFEST.json"
$manifest | ConvertTo-Json -Depth 6 | Set-Content $manifestPath -Encoding UTF8
$manifestSha = (Get-FileHash $manifestPath -Algorithm SHA256).Hash.ToLower()

$shaTxt = @(
"# CORVONERO PRE-PHASE-6 CHECKPOINT SHA-256",
"created: $ts",
"archive: $zipSha  $zipBaseName.zip",
"manifest: $manifestSha  $zipBaseName-MANIFEST.json",
"checkpoint_receipt: $receiptSha  CORVONERO-PRE-PHASE-6-CHECKPOINT-v1.json",
"",
"# Critical registries"
)
foreach ($k in $criticalHashes.Keys) { $shaTxt += "$($criticalHashes[$k])  $k" }
$shaPath = Join-Path $ArchiveDir "$zipBaseName-SHA256.txt"
$shaTxt -join "`n" | Set-Content $shaPath -Encoding UTF8

$readme = @(
"# CORVONERO PRE-PHASE-6 CHECKPOINT ARCHIVE",
"",
"Run: corv-semantic-v2-20260626-004",
"Phase 5.2: PASS (partial semantic authority operator approved)",
"Git commit: $commitSha",
"Tag: $tagName",
"",
"Contents: repository Corvonero pilot + reports + ORCA SPPC-05 repair evidence + Run 004 STORAGE state (locks excluded).",
"Phase 6 NOT started.",
"",
"Verify: compare $zipBaseName-SHA256.txt hashes before restore."
) -join "`n"
$readmePath = Join-Path $ArchiveDir "$zipBaseName-README.md"
$readme | Set-Content $readmePath -Encoding UTF8

# Archive verification
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$zipCount = $zip.Entries.Count
$requiredInZip = @(
  'repository/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json',
  'repository/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json',
  'repository/git-metadata/checkpoint-git-metadata-v1.json'
)
$missing = @()
foreach ($r in $requiredInZip) {
  if (-not ($zip.Entries.FullName -replace '\\','/' | Where-Object { $_ -like "*$($r -replace '/','*')*" })) {
    $found = $false
    foreach ($e in $zip.Entries) {
      if ($e.FullName.Replace('\','/') -like "*$(Split-Path $r -Leaf)") { $found = $true; break }
    }
    if (-not $found) { $missing += $r }
  }
}
$zip.Dispose()

$verifyZipSha = (Get-FileHash $zipPath -Algorithm SHA256).Hash.ToLower()
$verifyOk = ($verifyZipSha -eq $zipSha) -and ($missing.Count -eq 0)

Write-Output "ARCHIVE_DIR=$ArchiveDir"
Write-Output "ZIP_PATH=$zipPath"
Write-Output "ZIP_SIZE=$zipSize"
Write-Output "ZIP_SHA=$zipSha"
Write-Output "FILE_COUNT=$($fileEntries.Count)"
Write-Output "ZIP_ENTRY_COUNT=$zipCount"
Write-Output "VERIFY_OK=$verifyOk"
Write-Output "MISSING=$($missing -join ',')"
Write-Output "MANIFEST_SHA=$manifestSha"
Write-Output "COMMIT_SHA=$commitSha"
