# V9-06E59 exact-file source to runtime delivery
$ErrorActionPreference = "Stop"
$srcRoot = "X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS"
$rtTheme = "X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\themes\shpigovsky"
$rtPlugin = "X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\plugins\shpigovsky-core"
$rtAcf = "X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\acf-json"
$evidence = "X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\v9-06e59-layout-polish-maps-footer-comfort-admin"
New-Item -ItemType Directory -Force -Path $evidence | Out-Null

$files = @(
    @{ Src = "$srcRoot\theme\shpigovsky\functions.php"; Dst = "$rtTheme\functions.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\front-page.php"; Dst = "$rtTheme\front-page.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\inc\yandex-map-embed.php"; Dst = "$rtTheme\inc\yandex-map-embed.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\inc\contacts-helpers.php"; Dst = "$rtTheme\inc\contacts-helpers.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\assets\css\v9-style.css"; Dst = "$rtTheme\assets\css\v9-style.css" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\home\staff-photo.php"; Dst = "$rtTheme\template-parts\home\staff-photo.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\home\feature-grid.php"; Dst = "$rtTheme\template-parts\home\feature-grid.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\home\why-us.php"; Dst = "$rtTheme\template-parts\home\why-us.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\home\rehabilitation-requirements.php"; Dst = "$rtTheme\template-parts\home\rehabilitation-requirements.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\layout\footer.php"; Dst = "$rtTheme\template-parts\layout\footer.php" },
    @{ Src = "$srcRoot\theme\shpigovsky\template-parts\contacts\location-card.php"; Dst = "$rtTheme\template-parts\contacts\location-card.php" },
    @{ Src = "$srcRoot\plugins\shpigovsky-core\src\Fields\FieldGroups.php"; Dst = "$rtPlugin\src\Fields\FieldGroups.php" },
    @{ Src = "$srcRoot\plugins\shpigovsky-core\src\Fields\RepeaterValidation.php"; Dst = "$rtPlugin\src\Fields\RepeaterValidation.php" },
    @{ Src = "$srcRoot\acf-json\group_fp02_page_contacts.json"; Dst = "$rtAcf\group_fp02_page_contacts.json" },
    @{ Src = "$srcRoot\acf-json\group_fp02_block_comfort_requirements.json"; Dst = "$rtAcf\group_fp02_block_comfort_requirements.json" }
)

$rows = @("file,source_sha256,runtime_after_sha256,match")
foreach ($f in $files) {
    if (-not (Test-Path $f.Src)) { throw "Missing source: $($f.Src)" }
    Copy-Item $f.Src $f.Dst -Force
    $srcHash = (Get-FileHash $f.Src -Algorithm SHA256).Hash
    $rtHash = (Get-FileHash $f.Dst -Algorithm SHA256).Hash
    $match = if ($srcHash -eq $rtHash) { "YES" } else { "NO" }
    $rows += "$($f.Dst),$srcHash,$rtHash,$match"
}
Set-Content (Join-Path $evidence "delivery-hashes.csv") ($rows -join "`n") -Encoding UTF8
Write-Output "DELIVERED=$($files.Count)"
