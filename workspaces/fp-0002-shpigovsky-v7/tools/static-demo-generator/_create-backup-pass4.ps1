# FP-0002 PASS 4 pre-final-QA backup
$ErrorActionPreference = "Stop"
$repoRoot = "C:\MARS Phenix\AI MARS"
$ws = Join-Path $repoRoot "workspaces\fp-0002-shpigovsky-v7"
$storageRoot = "C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints"
$zipPath = Join-Path $storageRoot "FP-0002-V7-STATIC-DEMO-BEFORE-PASS-4-FINAL-QA.zip"
$staging = Join-Path $env:TEMP "fp0002-pass4-backup-staging"

if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Path $staging -Force | Out-Null
New-Item -ItemType Directory -Path $storageRoot -Force | Out-Null

Push-Location $repoRoot
git status --short | Out-File (Join-Path $staging "GIT-STATUS-BEFORE-PASS-4.txt") -Encoding utf8
git diff | Out-File (Join-Path $staging "GIT-DIFF-BEFORE-PASS-4.patch") -Encoding utf8
Pop-Location

$items = @(
    @{ Src = Join-Path $ws "src"; Dst = "src" },
    @{ Src = Join-Path $ws "src\data\static-demo"; Dst = "src/data/static-demo" },
    @{ Src = Join-Path $ws "tools\static-demo-generator"; Dst = "tools/static-demo-generator" },
    @{ Src = Join-Path $ws "plans\static-client-demo"; Dst = "plans/static-client-demo" },
    @{ Src = Join-Path $ws "foundation"; Dst = "foundation" },
    @{ Src = Join-Path $ws "package.json"; Dst = "package.json" },
    @{ Src = Join-Path $ws "package-lock.json"; Dst = "package-lock.json" },
    @{ Src = Join-Path $ws "gulpfile.js"; Dst = "gulpfile.js" }
)

foreach ($item in $items) {
    if (Test-Path $item.Src) {
        $dest = Join-Path $staging $item.Dst
        $parent = Split-Path $dest -Parent
        if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
        if ((Get-Item $item.Src).PSIsContainer) {
            Copy-Item $item.Src $dest -Recurse -Force
        } else {
            Copy-Item $item.Src $dest -Force
        }
    }
}

$statusDoc = Join-Path $repoRoot "workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\PROJECT-STATUS.md"
if (Test-Path $statusDoc) {
    Copy-Item $statusDoc (Join-Path $staging "PROJECT-STATUS.md") -Force
}
$opStatus = Join-Path $ws "foundation\FP-0002-V7-OPERATIONAL-STATUS.md"
if (Test-Path $opStatus) {
    Copy-Item $opStatus (Join-Path $staging "FP-0002-V7-OPERATIONAL-STATUS.md") -Force
}

$head = (git -C $repoRoot rev-parse HEAD).Trim()
$headShort = (git -C $repoRoot rev-parse --short HEAD).Trim()
$branch = (git -C $repoRoot rev-parse --abbrev-ref HEAD).Trim()
$pageCount = (Get-Content (Join-Path $ws "src\data\static-demo\demo-page-registry.json") | ConvertFrom-Json).meta.page_count
$dirty = (git -C $repoRoot status --short).Trim()

$manifest = @"
# FP-0002 V7 Static Demo PASS 4 — Pre-Final-QA Backup Manifest

FP-0002 STATIC CLIENT DEMO PRE-FINAL-QA STATE PRESERVED

| Field | Value |
| --- | --- |
| Repository | C:\MARS Phenix\AI MARS |
| Branch | $branch |
| HEAD | $headShort ($head) |
| PASS 3 commit | 93942b56 |
| Stable template tag | fp-0002-v7-four-template-canonical-demo-baseline-01 @ 3c48a4b9 |
| Page count | $pageCount |
| Dirty state | ORCA WIP + package-lock drift + pass evidence timestamps (excluded from PASS 4 commit scope) |
| package-lock status | drift present — excluded from PASS 4 commit |
| ORCA exclusion | confirmed — not included in this archive |
| Intended purpose | Restore pre-PASS-4-final-QA workspace before client demo freeze |

## Included paths
- src/ (full)
- src/data/static-demo/
- tools/static-demo-generator/
- plans/static-client-demo/
- foundation/
- package.json, package-lock.json, gulpfile.js
- PROJECT-STATUS.md, FP-0002-V7-OPERATIONAL-STATUS.md
- GIT-STATUS-BEFORE-PASS-4.txt, GIT-DIFF-BEFORE-PASS-4.patch

## Excluded paths
- node_modules, dist, screenshots, .git, Figma, INCOMING, ORCA, unrelated workspaces, recovery/temp directories
"@
$manifest | Out-File (Join-Path $staging "BACKUP-MANIFEST.md") -Encoding utf8

$restore = @"
# Restore instructions — FP-0002 PASS 4 pre-final-QA backup

1. Extract ``FP-0002-V7-STATIC-DEMO-BEFORE-PASS-4-FINAL-QA.zip`` to a temporary folder.
2. Copy ``src/`` → ``workspaces/fp-0002-shpigovsky-v7/src/``
3. Copy ``tools/static-demo-generator/`` → workspace tools folder.
4. Copy ``plans/static-client-demo/`` and ``foundation/`` if needed.
5. Copy ``package.json``, ``package-lock.json``, ``gulpfile.js`` → workspace root.
6. Run ``npm run build:demo`` from workspace using portable Node.
7. Verify canonical four template pages unchanged via SHA-256 hashes in PASS 4 evidence.

Do not use git checkout/restore for rollback — use this archive.
"@
$restore | Out-File (Join-Path $staging "RESTORE-INSTRUCTIONS.md") -Encoding utf8

$checksums = @()
Get-ChildItem $staging -Recurse -File | ForEach-Object {
    $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
    $rel = $_.FullName.Substring($staging.Length + 1).Replace('\', '/')
    $checksums += "$hash  $rel"
}
$checksums | Out-File (Join-Path $staging "CHECKSUMS-SHA256.txt") -Encoding utf8

if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $staging '*') -DestinationPath $zipPath -Force

$zipHash = (Get-FileHash $zipPath -Algorithm SHA256).Hash.ToLower()
Write-Output "ZIP=$zipPath"
Write-Output "ZIP_SHA256=$zipHash"
Write-Output "STAGING=$staging"
