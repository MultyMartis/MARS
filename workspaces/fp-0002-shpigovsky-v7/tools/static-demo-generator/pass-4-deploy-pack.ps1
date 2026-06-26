# FP-0002 PASS 4 — deploy pack creation and validation
param(
    [string]$StableCommit = "HEAD",
    [switch]$ValidateOnly
)
$ErrorActionPreference = "Stop"
$ws = "C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7"
$dist = Join-Path $ws "dist"
$deployDir = "C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\client-demo-deploy"
$zipName = "FP-0002-SHPIGOVSKY-STATIC-CLIENT-DEMO-v1.zip"
$zipPath = Join-Path $deployDir $zipName
$validationDir = Join-Path $deployDir "_validation-extract-pass4"
$repoRoot = "C:\MARS Phenix\AI MARS"
$node = Join-Path $repoRoot ".tools\node-portable\node.exe"
$registryPath = Join-Path $ws "src\direction\static-demo\demo-page-registry.json"

# fix path typo
$registryPath = Join-Path $ws "src\data\static-demo\demo-page-registry.json"
$registry = Get-Content $registryPath | ConvertFrom-Json
$pageCount = $registry.meta.page_count
$commit = (git -C $repoRoot rev-parse $StableCommit).Trim()
$commitShort = (git -C $repoRoot rev-parse --short $StableCommit).Trim()

New-Item -ItemType Directory -Path $deployDir -Force | Out-Null

if (-not $ValidateOnly) {
    if (-not (Test-Path (Join-Path $dist "index.html"))) {
        throw "dist/index.html missing — run npm run build:demo first"
    }
    if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
    Compress-Archive -Path (Join-Path $dist '*') -DestinationPath $zipPath -CompressionLevel Optimal -Force
}

if (-not (Test-Path $zipPath)) { throw "Deploy ZIP missing: $zipPath" }

$zipHash = (Get-FileHash $zipPath -Algorithm SHA256).Hash.ToLower()
$zipSize = (Get-Item $zipPath).Length

# Validate ZIP structure
Add-Type -AssemblyName System.IO.Compression.FileSystem
$archive = [System.IO.Compression.ZipFile]::OpenRead($zipPath)
$entries = @($archive.Entries | ForEach-Object { $_.FullName })
$archive.Dispose()

$hasRootIndex = $entries -contains "index.html"
$hasAssets = ($entries | Where-Object { $_ -like "assets/*" }).Count -gt 0
$htmlPages = ($entries | Where-Object { $_ -like "*/index.html" -or $_ -eq "index.html" }).Count

# Extract for HTTP validation
if (Test-Path $validationDir) { Remove-Item $validationDir -Recurse -Force }
New-Item -ItemType Directory -Path $validationDir -Force | Out-Null
Expand-Archive -Path $zipPath -DestinationPath $validationDir -Force

$port = 4188
$server = Start-Process -FilePath "python" -ArgumentList @("-m", "http.server", "$port", "--directory", $validationDir) -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 2

$criticalUrls = @("/", "/uslugi/", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "/assets/js/main.js")
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

$validation = @{
    timestamp = (Get-Date).ToUniversalTime().ToString("o")
    zip = $zipPath
    zip_sha256 = $zipHash
    zip_size = $zipSize
    root_index = $hasRootIndex
    assets_present = $hasAssets
    html_page_entries = $htmlPages
    expected_pages = $pageCount
    critical_http = $httpResults
    result = ($hasRootIndex -and $hasAssets -and ($httpResults | Where-Object { -not $_.ok }).Count -eq 0)
}
$validationJson = Join-Path $deployDir "PASS-4-DEPLOY-PACK-VALIDATION.json"
$validation | ConvertTo-Json -Depth 6 | Out-File $validationJson -Encoding utf8

$manifest = @"
# FP-0002 Static Client Demo v1 — Manifest

| Field | Value |
| --- | --- |
| Project | FP-0002 Shpigovsky V7 |
| Purpose | Static client demo for ordinary static hosting |
| Generation commit | $commitShort ($commit) |
| Stable tag | fp-0002-v7-static-client-demo-stable-01 |
| Build command | npm run build:demo |
| Registry page count | $pageCount |
| Package file count | $($entries.Count) |
| ZIP size | $zipSize bytes |
| ZIP SHA-256 | ``$zipHash`` |
| Root structure | index.html + assets/ + section folders at ZIP root |
| Deployment | NOT YET PERFORMED |
| CMS/backend | NONE |
| Forms | demo-only, no backend submission |

## Excluded material
- source, node_modules, generator, registries, Git, Excel, Figma, screenshots, reports

## Limitations
- Demo copy and placeholder pages
- noindex on demo pages
- no production SEO/legal finalization
"@
$manifest | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v1-MANIFEST.md") -Encoding utf8

"$zipHash  $zipName" | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v1-CHECKSUMS-SHA256.txt") -Encoding utf8

$deployInstructions = @"
# FP-0002 Static Client Demo v1 — Deploy Instructions

1. Create an empty document root on static hosting.
2. Backup current hosting contents.
3. Extract ``$zipName`` contents directly into document root (``index.html`` at root).
4. Verify ``/``, ``/uslugi/``, one deep service URL, and ``/assets/``.
5. Run smoke checks (navigation, mobile menu, assets load).
6. Rollback using hosting backup if issues appear.

**Do not** purge hosting with destructive mirror commands without explicit operator confirmation.
"@
$deployInstructions | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v1-DEPLOY-INSTRUCTIONS.md") -Encoding utf8

$rollback = @"
# FP-0002 Static Client Demo v1 — Rollback

1. Confirm target paths with operator.
2. Remove only files introduced by this demo package if explicitly approved.
3. Restore pre-deploy hosting backup.
4. Re-verify site root after rollback.
"@
$rollback | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v1-ROLLBACK.md") -Encoding utf8

@"
FP-0002 static client demo deploy pack
Commit: $commit
Branch: mars/canonical-post-recovery
Built: $(Get-Date -Format o)
ZIP: $zipName
SHA256: $zipHash
"@ | Out-File (Join-Path $deployDir "FP-0002-STATIC-CLIENT-DEMO-v1-GIT-RECEIPT.txt") -Encoding utf8

Write-Output "ZIP=$zipPath"
Write-Output "ZIP_SHA256=$zipHash"
Write-Output "VALIDATION=$validationJson"
Write-Output "RESULT=$($validation.result)"
