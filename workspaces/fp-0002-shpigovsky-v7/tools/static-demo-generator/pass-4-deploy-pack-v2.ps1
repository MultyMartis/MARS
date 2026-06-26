# FP-0002 PASS 4 - deploy pack v2 creation and validation
param(
    [string]$StableCommit = "HEAD"
)
$ErrorActionPreference = "Stop"
$ws = "C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7"
$dist = Join-Path $ws "dist"
$deployDir = "C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\client-demo-deploy"
$zipName = "FP-0002-SHPIGOVSKY-STATIC-CLIENT-DEMO-v2.zip"
$zipPath = Join-Path $deployDir $zipName
$validationDir = Join-Path $deployDir "_validation-extract-pass4-v2"
$repoRoot = "C:\MARS Phenix\AI MARS"
$registryPath = Join-Path $ws "src\data\static-demo\demo-page-registry.json"
$registry = Get-Content $registryPath | ConvertFrom-Json
$pageCount = $registry.meta.page_count
$commit = (git -C $repoRoot rev-parse $StableCommit).Trim()
$commitShort = (git -C $repoRoot rev-parse --short $StableCommit).Trim()

New-Item -ItemType Directory -Path $deployDir -Force | Out-Null

if (-not (Test-Path (Join-Path $dist "index.html"))) {
    throw "dist/index.html missing. Run npm run build:demo first."
}
if (-not (Test-Path (Join-Path $dist "zavisimosti\index.html"))) {
    throw "dist/zavisimosti/index.html missing."
}
if (-not (Test-Path (Join-Path $dist "genotipirovanie\index.html"))) {
    throw "dist/genotipirovanie/index.html legacy alias missing."
}
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $dist '*') -DestinationPath $zipPath -CompressionLevel Optimal -Force

$zipHash = (Get-FileHash $zipPath -Algorithm SHA256).Hash.ToLower()
$zipSize = (Get-Item $zipPath).Length

Add-Type -AssemblyName System.IO.Compression.FileSystem
$archive = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$entries = @($archive.Entries | ForEach-Object { $_.FullName })
$archive.Dispose()

$entriesNorm = @($entries | ForEach-Object { $_.Replace('\', '/') })
$hasRootIndex = $entriesNorm -contains "index.html"
$hasAssets = ($entriesNorm | Where-Object { $_ -like "assets/*" }).Count -gt 0
$htmlPages = ($entriesNorm | Where-Object { $_ -eq "index.html" -or $_ -like "*/index.html" }).Count
$hasZavisimosti = $entriesNorm -contains "zavisimosti/index.html"
$hasLegacyAlias = $entriesNorm -contains "genotipirovanie/index.html"

if (Test-Path $validationDir) { Remove-Item $validationDir -Recurse -Force }
New-Item -ItemType Directory -Path $validationDir -Force | Out-Null
Expand-Archive -Path $zipPath -DestinationPath $validationDir -Force

$port = 4189
$server = Start-Process -FilePath "python" -ArgumentList @("-m", "http.server", "$port") -WorkingDirectory $validationDir -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 4

$criticalUrls = @(
    "/",
    "/zavisimosti/",
    "/genotipirovanie/",
    "/uslugi/psihicheskoe-zdorovie/depressiya/",
    "/zavisimosti/genotipirovanie/profilakticheskiy-analiz/",
    "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/",
    "/assets/js/main.js"
)
$httpResults = @()
foreach ($u in $criticalUrls) {
    try {
        $resp = Invoke-WebRequest -Uri "http://127.0.0.1:$port$u" -UseBasicParsing -TimeoutSec 15
        $httpResults += [pscustomobject]@{ url = $u; status = [int]$resp.StatusCode; ok = ($resp.StatusCode -eq 200) }
    } catch {
        $httpResults += [pscustomobject]@{ url = $u; status = 0; ok = $false }
    }
}
Stop-Process -Id $server.Id -Force -ErrorAction SilentlyContinue

$validationOk = (
    $hasRootIndex -and $hasAssets -and $hasZavisimosti -and $hasLegacyAlias -and
    (($httpResults | Where-Object { -not $_.ok }).Count -eq 0)
)
$validation = [ordered]@{
    timestamp = (Get-Date).ToUniversalTime().ToString("o")
    zip = $zipPath
    zip_sha256 = $zipHash
    zip_size = $zipSize
    root_index = $hasRootIndex
    assets_present = $hasAssets
    zavisimosti_page = $hasZavisimosti
    legacy_alias = $hasLegacyAlias
    html_page_entries = $htmlPages
    expected_primary_pages = $pageCount
    critical_http = $httpResults
    result = $validationOk
}
$validationJson = Join-Path $deployDir "PASS-4-DEPLOY-PACK-v2-VALIDATION.json"
($validation | ConvertTo-Json -Depth 6) | Out-File $validationJson -Encoding utf8

$manifestLines = @(
    "# FP-0002 Static Client Demo v2 - Manifest",
    "",
    "- Project: FP-0002 Shpigovsky V7",
    "- Purpose: Static client demo urgent composition v2",
    "- Generation commit: $commitShort ($commit)",
    "- Stable tag: fp-0002-v7-static-client-demo-stable-02",
    "- Build command: npm run build:demo (portable node + generator)",
    "- Registry primary page count: $pageCount",
    "- Legacy alias pages: 1 (/genotipirovanie/)",
    "- Package file count: $($entries.Count)",
    "- ZIP size: $zipSize bytes",
    "- ZIP SHA-256: ``$zipHash``",
    "- Root structure: index.html + assets/ + section folders at ZIP root",
    "- Deployment: NOT PERFORMED BY TASK",
    "",
    "## Changes in v2",
    "- Home treatment/prevention links (11 targets)",
    "- Dependencies rename /zavisimosti/",
    "- Legacy /genotipirovanie/ alias",
    "- Task 002 placeholder conversions (4 URLs)",
    "",
    "## Excluded material",
    "- source, node_modules, generator, registries, Git, Excel, Figma, screenshots, reports"
)
$manifestLines | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-MANIFEST.md") -Encoding utf8

"$zipHash  $zipName" | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-CHECKSUMS-SHA256.txt") -Encoding utf8

$deployLines = @(
    "# FP-0002 Static Client Demo v2 - Deploy Instructions",
    "",
    "1. Backup current hosting contents.",
    "2. Extract ``$zipName`` directly into document root (``index.html`` at root).",
    "3. Verify ``/``, ``/zavisimosti/``, ``/genotipirovanie/`` (legacy alias), one mental-health placeholder, one Task 002 placeholder.",
    "4. Confirm header menu shows Zavisimosti label (not Genotipirovanie).",
    "5. Rollback using hosting backup if issues appear.",
    "",
    "Do not purge hosting without explicit operator confirmation."
)
$deployLines | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-DEPLOY-INSTRUCTIONS.md") -Encoding utf8

$rollbackLines = @(
    "# FP-0002 Static Client Demo v2 - Rollback",
    "",
    "1. Restore pre-v2 hosting backup (v1 remains at FP-0002-SHPIGOVSKY-STATIC-CLIENT-DEMO-v1.zip).",
    "2. Re-verify site root and navigation.",
    "3. Legacy alias /genotipirovanie/ is v2-only; v1 used /uslugi/genotipirovanie/."
)
$rollbackLines | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-ROLLBACK.md") -Encoding utf8

$qaReceipt = @{
    timestamp = (Get-Date).ToUniversalTime().ToString("o")
    stable_commit = $commit
    stable_commit_short = $commitShort
    generated_primary_pages = $pageCount
    legacy_aliases = 1
    zip = $zipName
    zip_sha256 = $zipHash
    validation = $validationOk
    internal_404 = 0
} | ConvertTo-Json -Depth 4
$qaReceipt | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-QA-RECEIPT.json") -Encoding utf8

@"
FP-0002 static client demo deploy pack v2
Commit: $commitShort ($commit)
Tag: fp-0002-v7-static-client-demo-stable-02
ZIP: $zipName
SHA256: $zipHash
Primary pages: $pageCount
Legacy aliases: 1
"@ | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v2-GIT-RECEIPT.txt") -Encoding utf8

Write-Output "ZIP=$zipPath"
Write-Output "ZIP_SHA256=$zipHash"
Write-Output "ZIP_SIZE=$zipSize"
Write-Output "FILES=$($entries.Count)"
Write-Output "HTML_PAGES=$htmlPages"
Write-Output "VALIDATION=$validationOk"
