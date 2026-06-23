# FP-0002 V6 PRE-REVIEWS OPERATOR STABLE 01 — create backup, checksums, verify, restore test
$ErrorActionPreference = 'Stop'

$Workspace = 'C:\AI MARS\workspaces\fp-0002-shpigovsky-v6'
$ReleaseId = 'FP-0002-V6-PRE-REVIEWS-OPERATOR-STABLE-01'
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
Copy-Item (Join-Path $Workspace "releases\$ReleaseId\BACKUP-MANIFEST.md") $StagingRoot -Force

$reviewsPartial = Join-Path $StagingRoot 'src\partials\sections\home-reviews.html'
if (Test-Path $reviewsPartial) { Remove-Item $reviewsPartial -Force }

$indexPath = Join-Path $StagingRoot 'src\pages\index.html'
if (Test-Path $indexPath) {
    $indexHtml = Get-Content $indexPath -Raw
    $indexHtml = $indexHtml -replace '(?s)\s*@@include\(''partials/sections/home-reviews.html''\)\r?\n', ''
    [System.IO.File]::WriteAllText($indexPath, $indexHtml, (New-Object System.Text.UTF8Encoding $false))
}

$mainJsPath = Join-Path $StagingRoot 'src\js\main.js'
if (Test-Path $mainJsPath) {
    $mainJs = Get-Content $mainJsPath -Raw
    $mainJs = $mainJs -replace '(?s)\r?\n// FP-0002 v6 — home reviews swiper.*?\}\)\(\);\r?\n', "`n"
    [System.IO.File]::WriteAllText($mainJsPath, $mainJs, (New-Object System.Text.UTF8Encoding $false))
}

$scssPath = Join-Path $StagingRoot 'src\scss\style.scss'
if (Test-Path $scssPath) {
    $scss = Get-Content $scssPath -Raw
    $scss = $scss -replace '(?s)/\* =+\s*\r?\n\s*10i\. Home reviews.*?(?=\/\* =+\s*\r?\n\s*11\. Footer)', ''
    [System.IO.File]::WriteAllText($scssPath, $scss, (New-Object System.Text.UTF8Encoding $false))
}

Get-ChildItem (Join-Path $StagingRoot 'src\img\content\pre-reviews') -Filter '_*' -File | Remove-Item -Force

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
}

$RestoreTestDir = Join-Path 'C:\AI MARS\workspaces' ('fp-0002-shpigovsky-v6-pre-reviews-restore-test-' + (Get-Date -Format 'yyyyMMddHHmmss'))
New-Item -ItemType Directory -Path $RestoreTestDir -Force | Out-Null
$ExpandRoot = Join-Path $env:TEMP 'fp0002-pre-reviews-restore-expand'
if (Test-Path $ExpandRoot) { Remove-Item $ExpandRoot -Recurse -Force }
Expand-Archive -Path $ArchivePath -DestinationPath $ExpandRoot -Force
Get-ChildItem -Path (Join-Path $ExpandRoot $ReleaseId) | Copy-Item -Destination $RestoreTestDir -Recurse -Force
Push-Location $RestoreTestDir
npm ci 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) { Pop-Location; throw 'npm ci failed in restore test' }
npm run build 2>&1 | Out-Null
if (-not (Test-Path 'dist\index.html')) { Pop-Location; throw 'Restore test: dist/index.html missing after build' }
$distHtml = Get-Content 'dist\index.html' -Raw
if ($distHtml -match 'home-reviews') { Pop-Location; throw 'Restore test: Reviews must be absent in pre-reviews freeze' }
if ($distHtml -notmatch 'home-gallery') { Pop-Location; throw 'Restore test: Gallery missing in pre-reviews freeze' }
if ($distHtml -notmatch 'home-clinic-landscape') { Pop-Location; throw 'Restore test: Clinic landscape missing' }
$scssFiles = Get-ChildItem 'src\scss' -Filter '*.scss' -File
if ($scssFiles.Count -ne 1) { Pop-Location; throw "Restore test: SCSS entry count must be 1, got $($scssFiles.Count)" }
Pop-Location

Write-Output "ARCHIVE_PATH=$ArchivePath"
Write-Output "ARCHIVE_SHA256=$archiveHash"
Write-Output "ARCHIVE_VERIFICATION=$(if ($verifyPass) { 'PASS' } else { 'FAIL' })"
Write-Output "RESTORE_TEST=PASS"
