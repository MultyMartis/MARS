# V9-06E52 pre-write backup - STOP if DB dump fails
$ErrorActionPreference = "Stop"
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$backupRoot = "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e52-generic-pages-demo-acf-sot-placeholder-before-$ts"
$siteRoot = "X:\MARS-Localhost\sites\wordpress\projects\shpigovsky"
$rtTheme = Join-Path $siteRoot "wp-content\themes\shpigovsky"
$rtPlugin = Join-Path $siteRoot "wp-content\plugins\shpigovsky-core"
$rtAcf = Join-Path $siteRoot "wp-content\acf-json"
$mysqldump = "X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysqldump.exe"
$php = "X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe"
$evidence = "X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence"
$exportPhp = "X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\validation\v9-06e52-generic-pages-demo-acf-sot-placeholder\_e52_backup_exports.php"

New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
@("db","theme","plugin","acf-json","meta","frontend","hashes") | ForEach-Object {
  New-Item -ItemType Directory -Force -Path (Join-Path $backupRoot $_) | Out-Null
}

Write-Output "BACKUP_ROOT=$backupRoot"

$dbFile = Join-Path $backupRoot "db\mars_wp_fp0002.sql"
$stderr = Join-Path $backupRoot "db\mysqldump-stderr.txt"
$prevEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"
cmd /c "`"$mysqldump`" --host=127.0.0.1 --user=mli_shpigovsky_app --password=9st4UPjdkc5MXyuNKEGTQaS0V7AD1ClR --no-tablespaces --single-transaction --routines --triggers mars_wp_fp0002 1>`"$dbFile`" 2>`"$stderr`""
$dumpExit = $LASTEXITCODE
$ErrorActionPreference = $prevEap
$dbSize = 0
if (Test-Path $dbFile) { $dbSize = (Get-Item $dbFile).Length }
if ($dumpExit -ne 0 -or $dbSize -lt 100000) {
  Write-Output "STOP - DB backup failed exit=$dumpExit size=$dbSize"
  exit 2
}
$dbHash = (Get-FileHash $dbFile -Algorithm SHA256).Hash
Write-Output "DB_OK size=$dbSize sha256=$dbHash"

robocopy $rtTheme (Join-Path $backupRoot "theme\shpigovsky") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $rtPlugin (Join-Path $backupRoot "plugin\shpigovsky-core") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $rtAcf (Join-Path $backupRoot "acf-json") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null

function Get-TreeHash([string]$dir) {
  $files = Get-ChildItem -Path $dir -Recurse -File | Sort-Object FullName
  $sha = [System.Security.Cryptography.SHA256]::Create()
  $ms = New-Object System.IO.MemoryStream
  foreach ($f in $files) {
    $rel = $f.FullName.Substring($dir.Length).TrimStart('\')
    $hash = (Get-FileHash $f.FullName -Algorithm SHA256).Hash
    $line = "$rel|$hash`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($line)
    $ms.Write($bytes, 0, $bytes.Length)
  }
  $ms.Position = 0
  $hashBytes = $sha.ComputeHash($ms)
  return ([System.BitConverter]::ToString($hashBytes) -replace '-','').ToLowerInvariant()
}

$themeHash = Get-TreeHash (Join-Path $backupRoot "theme\shpigovsky")
$pluginHash = Get-TreeHash (Join-Path $backupRoot "plugin\shpigovsky-core")
$acfHash = Get-TreeHash (Join-Path $backupRoot "acf-json")
Set-Content (Join-Path $backupRoot "hashes\theme-tree.sha256") $themeHash
Set-Content (Join-Path $backupRoot "hashes\plugin-tree.sha256") $pluginHash
Set-Content (Join-Path $backupRoot "hashes\acf-json-tree.sha256") $acfHash
$manifest = @"
DB=$dbHash
THEME=$themeHash
PLUGIN=$pluginHash
ACF=$acfHash
"@
Set-Content (Join-Path $backupRoot "hashes\source-hash-manifest.txt") $manifest

$css = Join-Path $rtTheme "assets\css\v9-style.css"
if (Test-Path $css) {
  $cssHash = (Get-FileHash $css -Algorithm SHA256).Hash
  Set-Content (Join-Path $backupRoot "hashes\operator-css.sha256") "v9-style.css=$cssHash"
}

$env:E52_BACKUP_ROOT = $backupRoot
& $php $exportPhp
if ($LASTEXITCODE -ne 0) {
  Write-Output "STOP - meta/frontend export failed"
  exit 2
}

Set-Content -Path (Join-Path $evidence "v9-06e52-backup-path.txt") -Value $backupRoot -Encoding UTF8
Set-Content -Path (Join-Path $backupRoot "BACKUP-OK.txt") -Value "OK $ts DB=$dbHash THEME=$themeHash PLUGIN=$pluginHash ACF=$acfHash" -Encoding UTF8

Write-Output "BACKUP_COMPLETE=$backupRoot"
Write-Output "DB_SHA256=$dbHash"
Write-Output "THEME_SHA256=$themeHash"
Write-Output "PLUGIN_SHA256=$pluginHash"
Write-Output "ACF_SHA256=$acfHash"
