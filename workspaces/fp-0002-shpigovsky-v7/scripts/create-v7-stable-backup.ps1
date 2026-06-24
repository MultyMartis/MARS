# FP-0002 V7 pre-final-polish stable source backup
$ErrorActionPreference = "Stop"
$WorkspaceRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$ReleaseId = "FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01"
$Staging = Join-Path $env:TEMP "fp-0002-v7-backup-staging"
$ZipDir = "C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\releases"
$ZipPath = Join-Path $ZipDir "$ReleaseId-SOURCE.zip"

if (Test-Path $Staging) { Remove-Item $Staging -Recurse -Force }
New-Item -ItemType Directory -Path $Staging -Force | Out-Null
New-Item -ItemType Directory -Path $ZipDir -Force | Out-Null

# Copy source tree
Copy-Item (Join-Path $WorkspaceRoot "src") (Join-Path $Staging "src") -Recurse
Copy-Item (Join-Path $WorkspaceRoot "foundation") (Join-Path $Staging "foundation") -Recurse
Copy-Item (Join-Path $WorkspaceRoot "gulpfile.js") $Staging
Copy-Item (Join-Path $WorkspaceRoot "package.json") $Staging
Copy-Item (Join-Path $WorkspaceRoot "package-lock.json") $Staging
Copy-Item (Join-Path $WorkspaceRoot "README.md") $Staging -ErrorAction SilentlyContinue

# Release docs into staging root
$ReleaseDir = Join-Path $WorkspaceRoot "releases\$ReleaseId"
Copy-Item (Join-Path $ReleaseDir "RESTORE-INSTRUCTIONS.md") $Staging
$BackupManifest = @"
# BACKUP-MANIFEST — $ReleaseId

**Release ID:** ``$ReleaseId``  
**Scope:** Operator-canonical V7 source before Package #001 final visual polish.

## Included

- ``src/`` (operator-canonical HTML/SCSS/JS/assets)
- ``foundation/`` (project-owned docs)
- ``gulpfile.js``
- ``package.json``
- ``package-lock.json``
- ``README.md``
- ``BACKUP-MANIFEST.md``
- ``CHECKSUMS-SHA256.txt``
- ``RESTORE-INSTRUCTIONS.md``

## Excluded

- ``node_modules/``, ``dist/``, ``.git/``, ``reviews/``, ``releases/``, temp, Figma source, ``_fig_extract_temp``, secrets, unrelated workspaces

## Archive

``$ZipPath``

## Frozen state

- Current ``src`` — **OPERATOR_CANONICAL**
- Gallery caption placement — **OVERLAY (known defect)**
- Global visual polish — **NOT_STARTED**
"@
Set-Content -Path (Join-Path $Staging "BACKUP-MANIFEST.md") -Value $BackupManifest -Encoding UTF8

# Checksums for all staged files
$checksumLines = @()
Get-ChildItem $Staging -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($Staging.Length + 1).Replace("\", "/")
    $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower()
    $checksumLines += "$hash  $rel"
}
$checksumPath = Join-Path $Staging "CHECKSUMS-SHA256.txt"
Set-Content -Path $checksumPath -Value ($checksumLines -join "`n") -Encoding UTF8

# Also write checksums to release dir (without zip self-reference)
$releaseChecksumPath = Join-Path $ReleaseDir "CHECKSUMS-SHA256.txt"
Set-Content -Path $releaseChecksumPath -Value ($checksumLines -join "`n") -Encoding UTF8

# Create ZIP
if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
Compress-Archive -Path (Join-Path $Staging "*") -DestinationPath $ZipPath -CompressionLevel Optimal

$zipHash = (Get-FileHash $ZipPath -Algorithm SHA256).Hash.ToLower()
$fileCount = (Get-ChildItem $Staging -Recurse -File).Count

Write-Output "ZIP_PATH=$ZipPath"
Write-Output "ZIP_SHA256=$zipHash"
Write-Output "FILE_COUNT=$fileCount"
Write-Output "STAGING=$Staging"
