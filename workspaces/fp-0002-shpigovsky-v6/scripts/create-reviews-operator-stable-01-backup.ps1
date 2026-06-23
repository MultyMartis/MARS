# FP-0002 V6 REVIEWS OPERATOR STABLE 01 — backup, checksums, verify, restore test
$ErrorActionPreference = 'Stop'

$Workspace = 'C:\AI MARS\workspaces\fp-0002-shpigovsky-v6'
$ReleaseId = 'FP-0002-V6-REVIEWS-OPERATOR-STABLE-01'
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

Get-ChildItem (Join-Path $StagingRoot 'src\img\content\pre-reviews') -Filter '_*' -File -ErrorAction SilentlyContinue | Remove-Item -Force

$nextPartial = Join-Path $StagingRoot 'src\partials\sections\home-rehabilitation-requirements.html'
if (Test-Path $nextPartial) { Remove-Item $nextPartial -Force }

$indexPath = Join-Path $StagingRoot 'src\pages\index.html'
if (Test-Path $indexPath) {
    $indexHtml = Get-Content $indexPath -Raw
    $indexHtml = $indexHtml -replace '(?s)\s*@@include\(''partials/sections/home-rehabilitation-requirements.html''\)\r?\n', ''
    [System.IO.File]::WriteAllText($indexPath, $indexHtml, (New-Object System.Text.UTF8Encoding $false))
}

$scssPath = Join-Path $StagingRoot 'src\scss\style.scss'
if (Test-Path $scssPath) {
    $scss = Get-Content $scssPath -Raw
    $scss = $scss -replace '(?s)/\* =+\s*\r?\n\s*10j\. Home rehabilitation requirements.*?(?=\/\* =+\s*\r?\n\s*11\. Footer)', ''
    [System.IO.File]::WriteAllText($scssPath, $scss, (New-Object System.Text.UTF8Encoding $false))
}

$fileCount = Write-ChecksumFile -Root $StagingRoot -OutPath (Join-Path $StagingRoot 'CHECKSUMS-SHA256.txt') -IncludeManifestFiles
Copy-Item (Join-Path $StagingRoot 'CHECKSUMS-SHA256.txt') $RepoChecksumPath -Force

if (Test-Path $ArchivePath) { Remove-Item $ArchivePath -Force }
Compress-Archive -Path $StagingRoot -DestinationPath $ArchivePath -CompressionLevel Optimal

$archiveHash = (Get-FileHash -Algorithm SHA256 -Path $ArchivePath).Hash.ToLower()
[System.IO.File]::WriteAllText($ChecksumSidecar, "$archiveHash  $ArchiveName`n", (New-Object System.Text.UTF8Encoding $false))

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

$RestoreTestDir = Join-Path 'C:\AI MARS\workspaces' ('fp-0002-shpigovsky-v6-reviews-restore-test-' + (Get-Date -Format 'yyyyMMddHHmmss'))
New-Item -ItemType Directory -Path $RestoreTestDir -Force | Out-Null
$ExpandRoot = Join-Path $env:TEMP 'fp0002-reviews-restore-expand'
if (Test-Path $ExpandRoot) { Remove-Item $ExpandRoot -Recurse -Force }
Expand-Archive -Path $ArchivePath -DestinationPath $ExpandRoot -Force
Get-ChildItem -Path (Join-Path $ExpandRoot $ReleaseId) | Copy-Item -Destination $RestoreTestDir -Recurse -Force
Push-Location $RestoreTestDir
$prevEap = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
cmd /c "npm ci >nul 2>nul"
if ($LASTEXITCODE -ne 0) { $ErrorActionPreference = $prevEap; Pop-Location; throw 'npm ci failed in restore test' }
cmd /c "npm run build >nul 2>nul"
$ErrorActionPreference = $prevEap
if (-not (Test-Path 'dist\index.html')) { Pop-Location; throw 'Restore test: dist/index.html missing after build' }
$distHtml = Get-Content 'dist\index.html' -Raw
if ($distHtml -notmatch 'home-reviews') { Pop-Location; throw 'Restore test: Reviews must be present' }
if ($distHtml -notmatch 'home-gallery') { Pop-Location; throw 'Restore test: Gallery missing' }
if ($distHtml -match 'home-rehabilitation-requirements') { Pop-Location; throw 'Restore test: next section must be absent' }
if ($distHtml -match 'fonts\.googleapis\.com') { Pop-Location; throw 'Restore test: Google Fonts must be 0' }
$scssFiles = Get-ChildItem 'src\scss' -Filter '*.scss' -File
if ($scssFiles.Count -ne 1) { Pop-Location; throw "Restore test: SCSS entry count must be 1, got $($scssFiles.Count)" }
Pop-Location

Write-Output "ARCHIVE_PATH=$ArchivePath"
Write-Output "ARCHIVE_SHA256=$archiveHash"
Write-Output "ARCHIVE_VERIFICATION=$(if ($verifyPass) { 'PASS' } else { 'FAIL' })"
Write-Output "RESTORE_TEST=PASS"
Write-Output "FILE_COUNT=$fileCount"
