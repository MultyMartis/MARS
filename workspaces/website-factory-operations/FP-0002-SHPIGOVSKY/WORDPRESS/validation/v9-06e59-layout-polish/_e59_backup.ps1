# V9-06E59 pre-change backup — STOP if DB dump fails
$ErrorActionPreference = "Stop"
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$backupRoot = "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e59-before-layout-polish-maps-footer-comfort-admin-$ts"
$siteRoot = "X:\MARS-Localhost\sites\wordpress\projects\shpigovsky"
$srcRoot = "X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS"
$rtTheme = Join-Path $siteRoot "wp-content\themes\shpigovsky"
$rtPlugin = Join-Path $siteRoot "wp-content\plugins\shpigovsky-core"
$rtAcf = Join-Path $siteRoot "wp-content\acf-json"
$srcTheme = Join-Path $srcRoot "theme\shpigovsky"
$srcPlugin = Join-Path $srcRoot "plugins\shpigovsky-core"
$srcAcf = Join-Path $srcRoot "acf-json"
$mysqldump = "X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysqldump.exe"

New-Item -ItemType Directory -Force -Path $backupRoot | Out-Null
@("db", "theme-runtime", "theme-source", "plugin-runtime", "plugin-source", "acf-json-runtime", "acf-json-source", "hashes", "runtime-snapshot") | ForEach-Object {
    New-Item -ItemType Directory -Force -Path (Join-Path $backupRoot $_) | Out-Null
}

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
    if (Test-Path $stderr) { Get-Content $stderr }
    exit 2
}
$dbHash = (Get-FileHash $dbFile -Algorithm SHA256).Hash

robocopy $rtTheme (Join-Path $backupRoot "theme-runtime\shpigovsky") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $srcTheme (Join-Path $backupRoot "theme-source\shpigovsky") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $rtPlugin (Join-Path $backupRoot "plugin-runtime\shpigovsky-core") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $srcPlugin (Join-Path $backupRoot "plugin-source\shpigovsky-core") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $rtAcf (Join-Path $backupRoot "acf-json-runtime") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
robocopy $srcAcf (Join-Path $backupRoot "acf-json-source") /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null

$hashRows = @("path,scope,sha256")
$hashTargets = @(
    @{ Scope = "runtime"; Path = Join-Path $rtTheme "assets\css\v9-style.css" },
    @{ Scope = "source"; Path = Join-Path $srcTheme "assets\css\v9-style.css" },
    @{ Scope = "runtime"; Path = Join-Path $rtTheme "template-parts\home\rehabilitation-requirements.php" },
    @{ Scope = "source"; Path = Join-Path $srcTheme "template-parts\home\rehabilitation-requirements.php" },
    @{ Scope = "runtime"; Path = Join-Path $rtTheme "template-parts\layout\footer.php" },
    @{ Scope = "source"; Path = Join-Path $srcTheme "template-parts\layout\footer.php" },
    @{ Scope = "runtime"; Path = Join-Path $rtTheme "inc\contacts-helpers.php" },
    @{ Scope = "source"; Path = Join-Path $srcTheme "inc\contacts-helpers.php" },
    @{ Scope = "runtime"; Path = Join-Path $rtTheme "template-parts\contacts\location-card.php" },
    @{ Scope = "source"; Path = Join-Path $srcTheme "template-parts\contacts\location-card.php" },
    @{ Scope = "runtime"; Path = Join-Path $rtAcf "group_fp02_page_contacts.json" },
    @{ Scope = "source"; Path = Join-Path $srcAcf "group_fp02_page_contacts.json" },
    @{ Scope = "runtime"; Path = Join-Path $rtAcf "group_fp02_block_comfort_requirements.json" },
    @{ Scope = "source"; Path = Join-Path $srcAcf "group_fp02_block_comfort_requirements.json" }
)
foreach ($t in $hashTargets) {
    if (Test-Path $t.Path) {
        $h = (Get-FileHash $t.Path -Algorithm SHA256).Hash
        $rel = $t.Path -replace '^[A-Z]:\\',''
        $hashRows += "$rel,$($t.Scope),$h"
    }
}
Set-Content (Join-Path $backupRoot "hashes.csv") ($hashRows -join "`n") -Encoding UTF8

$opManifest = @"
classification,file,source_hash_prefix,runtime_hash_prefix,action
operator_css,assets/css/v9-style.css,307A111E,106D5BEB,promote_runtime_to_source_before_wave
operator_html,template-parts/home/rehabilitation-requirements.php,D6C8B02D,68BE0867,promote_runtime_to_source_before_wave
"@
Set-Content (Join-Path $backupRoot "operator-change-manifest.csv") $opManifest -Encoding UTF8

Push-Location "X:\AI MARS"
$gitBranch = git branch --show-current 2>$null
$gitHead = git rev-parse HEAD 2>$null
Pop-Location

$backupInfo = @"
# BACKUP-INFO — V9-06E59 Layout Polish, Contacts Maps, Footer Links and Comfort CTA Admin Parity

- **Wave:** V9-06E59
- **Timestamp:** $ts
- **Path:** $backupRoot
- **Latest operator CSS and HTML are canon**
- **Scope:** Contacts maps + repeatable ACF; Footer heading links; Comfort CTA lead admin parity; confirmed E58-VA-001 correction
- **DB changes allowed:** safe ACF data migration/default seeding only
- **No commit / push / freeze**
- **Runtime URL:** http://shpigovsky.test/
- **Database:** mars_wp_fp0002
- **DB dump:** db/mars_wp_fp0002.sql ($dbSize bytes, SHA256 $dbHash)
- **Git branch:** $gitBranch
- **Git HEAD:** $gitHead
"@
Set-Content (Join-Path $backupRoot "BACKUP-INFO.md") $backupInfo -Encoding UTF8
Set-Content (Join-Path $backupRoot "BACKUP-OK.txt") "OK $ts DB=$dbHash" -Encoding UTF8

Write-Output "BACKUP_ROOT=$backupRoot"
Write-Output "DB_SHA256=$dbHash"
Write-Output "DB_SIZE=$dbSize"
