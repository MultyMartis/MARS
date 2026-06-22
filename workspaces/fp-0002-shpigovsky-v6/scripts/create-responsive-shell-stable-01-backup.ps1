# FP-0002 V6 RESPONSIVE SHELL STABLE 01 — source backup, checksums, verify, restore test
$ErrorActionPreference = 'Stop'

$Workspace = 'C:\AI MARS\workspaces\fp-0002-shpigovsky-v6'
$ReleaseId = 'FP-0002-V6-RESPONSIVE-SHELL-STABLE-01'
$ArchiveName = "$ReleaseId-SOURCE.zip"
$StorageDir = 'C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases'
$ArchivePath = Join-Path $StorageDir $ArchiveName
$ChecksumSidecar = Join-Path $StorageDir "$ReleaseId-SOURCE.sha256"
$TempRoot = Join-Path $env:TEMP "fp0002-backup-$ReleaseId"
$StagingRoot = Join-Path $TempRoot $ReleaseId
$RepoChecksumPath = Join-Path $Workspace "releases\$ReleaseId\CHECKSUMS-SHA256.txt"

function Get-StableRelativeFiles {
    param([string]$Root)
    $files = @()
    $files += Get-ChildItem (Join-Path $Root 'src') -Recurse -File | ForEach-Object {
        [PSCustomObject]@{ Rel = ($_.FullName.Substring($Root.Length + 1) -replace '\\','/'); Full = $_.FullName }
    }
    foreach ($name in @('gulpfile.js','package.json','package-lock.json')) {
        $p = Join-Path $Root $name
        if (Test-Path $p) { $files += [PSCustomObject]@{ Rel = $name; Full = $p } }
    }
    foreach ($name in @('BACKUP-MANIFEST.md','RESTORE-INSTRUCTIONS.md')) {
        $p = Join-Path $StagingRoot $name
        if (Test-Path $p) { $files += [PSCustomObject]@{ Rel = $name; Full = $p } }
    }
    return $files | Sort-Object Rel -Unique
}

function Write-ChecksumFile {
    param([string]$Root, [string]$OutPath, [switch]$IncludeManifestFiles)
    $lines = New-Object System.Collections.Generic.List[string]
    $items = Get-StableRelativeFiles -Root $Root
    if ($IncludeManifestFiles) {
        foreach ($extra in @('BACKUP-MANIFEST.md','RESTORE-INSTRUCTIONS.md','CHECKSUMS-SHA256.txt')) {
            $p = Join-Path $StagingRoot $extra
            if ((Test-Path $p) -and -not ($items.Rel -contains $extra)) {
                $items += [PSCustomObject]@{ Rel = $extra; Full = $p }
            }
        }
        $items = $items | Sort-Object Rel -Unique
    }
    foreach ($item in $items) {
        $hash = (Get-FileHash -Algorithm SHA256 -Path $item.Full).Hash.ToLower()
        $lines.Add("$hash  $($item.Rel)")
    }
    $content = ($lines -join "`n") + "`n"
    [System.IO.File]::WriteAllText($OutPath, $content, (New-Object System.Text.UTF8Encoding $false))
    return $items.Count
}

if (Test-Path $TempRoot) { Remove-Item $TempRoot -Recurse -Force }
New-Item -ItemType Directory -Path $StagingRoot -Force | Out-Null
New-Item -ItemType Directory -Path $StorageDir -Force | Out-Null

Copy-Item (Join-Path $Workspace 'src') (Join-Path $StagingRoot 'src') -Recurse -Force
Copy-Item (Join-Path $Workspace 'gulpfile.js') $StagingRoot -Force
Copy-Item (Join-Path $Workspace 'package.json') $StagingRoot -Force
Copy-Item (Join-Path $Workspace 'package-lock.json') $StagingRoot -Force
Copy-Item (Join-Path $Workspace "releases\$ReleaseId\RESTORE-INSTRUCTIONS.md") $StagingRoot -Force

$backupManifest = @"
# FP-0002 V6 RESPONSIVE SHELL STABLE 01 — Backup Manifest

**Release ID:** $ReleaseId
**Created:** $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK')
**Scope:** Operator-canonical responsive shell snapshot (Header, Hero, left off-canvas, Footer, local Inter, foundation)
**NOT CANONICAL:** dist/ — regenerate via npm run build
**NOT IN SCOPE:** main content sections

## Contents

- src/ (pages, partials, scss, js, fonts, images)
- gulpfile.js
- package.json
- package-lock.json
- RESTORE-INSTRUCTIONS.md
- CHECKSUMS-SHA256.txt

## Excluded

node_modules/, dist/, .git/, reviews/, archive/, unrelated workspaces
"@
[System.IO.File]::WriteAllText((Join-Path $StagingRoot 'BACKUP-MANIFEST.md'), $backupManifest, (New-Object System.Text.UTF8Encoding $false))

$fileCount = Write-ChecksumFile -Root $StagingRoot -OutPath (Join-Path $StagingRoot 'CHECKSUMS-SHA256.txt') -IncludeManifestFiles
Copy-Item (Join-Path $StagingRoot 'CHECKSUMS-SHA256.txt') $RepoChecksumPath -Force

if (Test-Path $ArchivePath) { Remove-Item $ArchivePath -Force }
Compress-Archive -Path $StagingRoot -DestinationPath $ArchivePath -CompressionLevel Optimal

$archiveHash = (Get-FileHash -Algorithm SHA256 -Path $ArchivePath).Hash.ToLower()
[System.IO.File]::WriteAllText($ChecksumSidecar, "$archiveHash  $ArchiveName`n", (New-Object System.Text.UTF8Encoding $false))

Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead($ArchivePath)
$zipEntries = $zip.Entries.Count
$zip.Dispose()

$ExtractRoot = Join-Path $TempRoot 'verify-extract'
if (Test-Path $ExtractRoot) { Remove-Item $ExtractRoot -Recurse -Force }
Expand-Archive -Path $ArchivePath -DestinationPath $ExtractRoot -Force
$extractedRoot = Join-Path $ExtractRoot $ReleaseId
$checksumLines = Get-Content (Join-Path $extractedRoot 'CHECKSUMS-SHA256.txt')
$verifyPass = $true
$verifyCount = 0
foreach ($line in $checksumLines) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $parts = $line -split '  ', 2
    if ($parts.Count -lt 2) { continue }
    $expected = $parts[0].Trim().ToLower()
    $rel = $parts[1].Trim()
    $target = Join-Path $extractedRoot ($rel -replace '/','\')
    if (-not (Test-Path $target)) { $verifyPass = $false; Write-Output "MISSING: $rel"; continue }
    $actual = (Get-FileHash -Algorithm SHA256 -Path $target).Hash.ToLower()
    if ($actual -ne $expected) { $verifyPass = $false; Write-Output "MISMATCH: $rel" }
    $verifyCount++
}

$RestoreTestDir = Join-Path 'C:\AI MARS\workspaces' 'fp-0002-shpigovsky-v6-responsive-shell-restore-test'
if (Test-Path $RestoreTestDir) {
  try { Remove-Item $RestoreTestDir -Recurse -Force -ErrorAction Stop } catch {
    $RestoreTestDir = Join-Path 'C:\AI MARS\workspaces' ('fp-0002-shpigovsky-v6-responsive-shell-restore-test-' + (Get-Date -Format 'yyyyMMddHHmmss'))
  }
}
New-Item -ItemType Directory -Path $RestoreTestDir -Force | Out-Null
$ExpandRoot = Join-Path $env:TEMP 'fp0002-responsive-shell-restore-expand'
if (Test-Path $ExpandRoot) { Remove-Item $ExpandRoot -Recurse -Force }
Expand-Archive -Path $ArchivePath -DestinationPath $ExpandRoot -Force
Get-ChildItem -Path (Join-Path $ExpandRoot $ReleaseId) | Copy-Item -Destination $RestoreTestDir -Recurse -Force
Push-Location $RestoreTestDir
cmd /c "npm ci >nul 2>&1"
if ($LASTEXITCODE -ne 0) { Pop-Location; throw 'npm ci failed in restore test' }
cmd /c "npm run build >nul 2>&1"
if ($LASTEXITCODE -ne 0) { Pop-Location; throw 'npm run build failed in restore test' }
$restoreChecks = @(
    'dist\index.html',
    'dist\assets\css\style.css',
    'dist\assets\js\main.js',
    'dist\assets\fonts\inter\inter-400.woff2'
)
foreach ($c in $restoreChecks) {
    if (-not (Test-Path $c)) { throw "Restore test missing: $c" }
}
$distHtml = Get-Content 'dist\index.html' -Raw
if ($distHtml -match 'fonts\.googleapis|fonts\.gstatic') { throw 'Restore test: Google Fonts reference in dist HTML' }
$distJs = Get-Content 'dist\assets\js\main.js' -Raw
if ($distJs -notmatch 'data-offcanvas') { throw 'Restore test: off-canvas JS missing' }
Pop-Location

$archiveSize = (Get-Item $ArchivePath).Length

Write-Output "ARCHIVE_PATH=$ArchivePath"
Write-Output "ARCHIVE_SIZE=$archiveSize"
Write-Output "ARCHIVE_SHA256=$archiveHash"
Write-Output "ZIP_ENTRY_COUNT=$zipEntries"
Write-Output "CHECKSUM_FILE_COUNT=$fileCount"
Write-Output "CHECKSUM_VERIFY_COUNT=$verifyCount"
Write-Output "ARCHIVE_VERIFICATION=$(if ($verifyPass) { 'PASS' } else { 'FAIL' })"
Write-Output "CHECKSUM_VERIFICATION=$(if ($verifyPass) { 'PASS' } else { 'FAIL' })"
Write-Output "RESTORE_TEST_DIR=$RestoreTestDir"
Write-Output "RESTORE_TEST=PASS"
