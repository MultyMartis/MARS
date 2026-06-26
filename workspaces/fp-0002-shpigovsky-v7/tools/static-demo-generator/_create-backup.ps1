# FP-0002 PASS 2 pre-implementation backup
$ErrorActionPreference = "Stop"
$repoRoot = "C:\MARS Phenix\AI MARS"
$ws = Join-Path $repoRoot "workspaces\fp-0002-shpigovsky-v7"
$storageRoot = "C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints"
$zipPath = Join-Path $storageRoot "FP-0002-V7-STATIC-DEMO-BEFORE-PASS-2.zip"
$staging = Join-Path $env:TEMP "fp0002-pass2-backup-staging"

if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Path $staging -Force | Out-Null
New-Item -ItemType Directory -Path $storageRoot -Force | Out-Null

Push-Location $repoRoot
git status --short | Out-File (Join-Path $staging "GIT-STATUS-BEFORE-PASS-2.txt") -Encoding utf8
git diff | Out-File (Join-Path $staging "GIT-DIFF-BEFORE-PASS-2.patch") -Encoding utf8
Pop-Location

$items = @(
    @{ Src = Join-Path $ws "src"; Dst = "src" },
    @{ Src = Join-Path $ws "package.json"; Dst = "package.json" },
    @{ Src = Join-Path $ws "package-lock.json"; Dst = "package-lock.json" },
    @{ Src = Join-Path $ws "gulpfile.js"; Dst = "gulpfile.js" },
    @{ Src = Join-Path $ws "plans\static-client-demo"; Dst = "plans/static-client-demo" },
    @{ Src = Join-Path $ws "foundation"; Dst = "foundation" }
)

foreach ($item in $items) {
    if (Test-Path $item.Src) {
        $dest = Join-Path $staging $item.Dst
        $parent = Split-Path $dest -Parent
        if (-not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
        Copy-Item $item.Src $dest -Recurse -Force
    }
}

$statusDoc = Join-Path $repoRoot "workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\PROJECT-STATUS.md"
if (Test-Path $statusDoc) {
    Copy-Item $statusDoc (Join-Path $staging "PROJECT-STATUS.md") -Force
}

$head = (git -C $repoRoot rev-parse --short HEAD).Trim()
$manifest = @"
# FP-0002 V7 Static Demo PASS 2 — Backup Manifest

FP-0002 STATIC DEMO PASS 2 PRE-IMPLEMENTATION STATE PRESERVED

| Field | Value |
| --- | --- |
| Repository | C:\MARS Phenix\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | $head |
| Stable baseline | 3c48a4b9 |
| Planning commit | 797dab58 |
| Dirty state | ORCA WIP + package-lock drift (excluded from scope) |
| Intended use | Restore pre-PASS-2 workspace before static demo generator |

## Operator decisions (PASS 2)
- Blog duplicates → /stati/statya-1..3/
- Reserved «Название» → neutral client_demo_name, HIDDEN_FROM_PRIMARY_NAV
- Footer legal placeholders (4)
- URL typos normalized for demo (specyalisty→specialisty, pilzovatelyu→polzovatelyu)

## Included paths
- src/
- package.json, package-lock.json, gulpfile.js
- plans/static-client-demo/
- foundation/
- GIT-STATUS-BEFORE-PASS-2.txt, GIT-DIFF-BEFORE-PASS-2.patch

## Excluded paths
- node_modules, dist, Figma, INCOMING, screenshots, .git, ORCA, unrelated workspaces
"@
$manifest | Out-File (Join-Path $staging "BACKUP-MANIFEST.md") -Encoding utf8

$restore = @"
# Restore instructions — FP-0002 PASS 2 pre-implementation backup

1. Extract ``FP-0002-V7-STATIC-DEMO-BEFORE-PASS-2.zip`` to a temporary folder.
2. Copy ``src/`` → ``workspaces/fp-0002-shpigovsky-v7/src/``
3. Copy ``package.json``, ``package-lock.json``, ``gulpfile.js`` → workspace root.
4. Copy ``plans/static-client-demo/`` and ``foundation/`` if needed.
5. Run ``npm run build`` from workspace (not ``build:demo``).
6. Verify canonical four template pages unchanged via SHA-256 hashes in evidence file.

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
