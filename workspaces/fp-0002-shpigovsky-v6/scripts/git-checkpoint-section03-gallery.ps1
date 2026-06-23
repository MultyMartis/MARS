# FP-0002 selective git checkpoints
$ErrorActionPreference = 'Stop'
$Root = 'C:\AI MARS'
$Ws = Join-Path $Root 'workspaces\fp-0002-shpigovsky-v6'
Set-Location $Root

function Stage-Fp0002 {
    param([string[]]$Paths)
    foreach ($p in $Paths) {
        if (Test-Path (Join-Path $Root $p)) {
            git add -f $p
        }
    }
}

function Show-Staged {
    git diff --cached --stat
    git diff --cached --name-status
}

$styleFull = Get-Content (Join-Path $Ws 'src\scss\style.scss') -Raw
$indexFull = Get-Content (Join-Path $Ws 'src\pages\index.html') -Raw
$mainFull = Get-Content (Join-Path $Ws 'src\js\main.js') -Raw

$styleS03 = $styleFull -replace '(?s)\r?\n/\* =+\r?\n   10d\. Home gallery.*?(?=/\* =+\r?\n   11\. Footer)', "`r`n"
$styleS03 = $styleS03 -replace '(?s)\r?\n\t\.home-gallery__image \{.*?\r?\n\t\}', ''
Set-Content (Join-Path $Ws 'src\scss\style.scss') -Value $styleS03 -NoNewline

$indexS03 = $indexFull -replace "\r?\n\s*@@include\('partials/sections/home-gallery\.html'\)", '' `
    -replace "\r?\n\s*@@include\('partials/sections/home-why-us\.html'\)", '' `
    -replace "\r?\n\s*<script src=`"assets/vendor/swiper/swiper-bundle\.min\.js`" defer></script>", ''
$mainMarker = '(?s)\r?\n// FP-0002 v6 . home gallery swiper.*\z'
$mainS03 = [regex]::Replace($mainFull, $mainMarker, "`r`n").TrimEnd() + "`r`n"
Set-Content (Join-Path $Ws 'src\pages\index.html') -Value $indexS03 -NoNewline
Set-Content (Join-Path $Ws 'src\js\main.js') -Value $mainS03 -NoNewline

Stage-Fp0002 @(
    'workspaces/fp-0002-shpigovsky-v6/src/partials/sections/home-treatment-prevention.html',
    'workspaces/fp-0002-shpigovsky-v6/src/partials/sections/home-founder-quote.html',
    'workspaces/fp-0002-shpigovsky-v6/src/scss/style.scss',
    'workspaces/fp-0002-shpigovsky-v6/src/pages/index.html',
    'workspaces/fp-0002-shpigovsky-v6/src/js/main.js'
)
Show-Staged
git commit -m "fix(fp-0002): add treatment service links and arrow icons"
Write-Host "COMMIT 1 done: $(git rev-parse --short HEAD)"

Stage-Fp0002 @(
    'workspaces/fp-0002-shpigovsky-v6/scripts/create-section-03-operator-stable-01-backup.ps1',
    'workspaces/fp-0002-shpigovsky-v6/scripts/git-checkpoint-section03-gallery.ps1',
    'workspaces/fp-0002-shpigovsky-v6/releases/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01/RESTORE-INSTRUCTIONS.md',
    'workspaces/fp-0002-shpigovsky-v6/releases/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01-MANIFEST.md',
    'workspaces/fp-0002-shpigovsky-v6/releases/FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01/CHECKSUMS-SHA256.txt',
    'workspaces/fp-0002-shpigovsky-v6/foundation/FP-0002-V6-OPERATIONAL-STATUS.md',
    'workspaces/fp-0002-shpigovsky-v6/logs/v6-actions.log',
    'workspaces/fp-0002-shpigovsky-v6/logs/v6-decisions.log',
    'workspaces/fp-0002-shpigovsky-v6/logs/v6-safe-unknown.log',
    'workspaces/fp-0002-shpigovsky-v6/logs/v6-source-access.log'
)
Show-Staged
git commit -m "chore(fp-0002): freeze operator-approved section 03"
Write-Host "COMMIT 2 done: $(git rev-parse --short HEAD)"
git tag -a fp-0002-v6-section-03-operator-stable-01 -m "FP-0002 V6 stable baseline through Section 03 with operator-canonical source and clickable treatment service links."

$styleGalleryOnly = $styleFull -replace '(?s)\r?\n/\* =+\r?\n   10e\. Home why us \(pre-reviews\).*?(?=/\* =+\r?\n   11\. Footer)', "`r`n"
Set-Content (Join-Path $Ws 'src\scss\style.scss') -Value $styleGalleryOnly -NoNewline
$indexGallery = $indexFull -replace "\r?\n\s*@@include\('partials/sections/home-why-us\.html'\)", ''
Set-Content (Join-Path $Ws 'src\pages\index.html') -Value $indexGallery -NoNewline
Set-Content (Join-Path $Ws 'src\js\main.js') -Value $mainFull -NoNewline

Stage-Fp0002 @(
    'workspaces/fp-0002-shpigovsky-v6/src/scss/style.scss',
    'workspaces/fp-0002-shpigovsky-v6/src/pages/index.html',
    'workspaces/fp-0002-shpigovsky-v6/src/js/main.js',
    'workspaces/fp-0002-shpigovsky-v6/src/partials/sections/home-gallery.html',
    'workspaces/fp-0002-shpigovsky-v6/src/img/content/gallery/shpigovsky-gallery-01.webp',
    'workspaces/fp-0002-shpigovsky-v6/src/img/content/gallery/shpigovsky-gallery-02.webp',
    'workspaces/fp-0002-shpigovsky-v6/src/img/content/gallery/shpigovsky-gallery-03.webp',
    'workspaces/fp-0002-shpigovsky-v6/src/img/content/gallery/shpigovsky-gallery-04.webp',
    'workspaces/fp-0002-shpigovsky-v6/src/img/content/gallery/GALLERY-ASSET-PROVENANCE.md',
    'workspaces/fp-0002-shpigovsky-v6/gulpfile.js',
    'workspaces/fp-0002-shpigovsky-v6/package.json',
    'workspaces/fp-0002-shpigovsky-v6/package-lock.json',
    'workspaces/fp-0002-shpigovsky-v6/scripts/extract-gallery-fig.mjs',
    'workspaces/fp-0002-shpigovsky-v6/scripts/probe-gallery-fig.mjs',
    'workspaces/fp-0002-shpigovsky-v6/reviews/main-content/gallery-audit',
    'workspaces/fp-0002-shpigovsky-v6/reviews/main-content/gallery-implementation',
    'workspaces/fp-0002-shpigovsky-v6/reviews/main-content/FP-0002-V6-SECTION-03-LINKS-AND-GALLERY-REVIEW.md'
)
Show-Staged
git commit -m "feat(fp-0002): add Figma gallery with Swiper"
Write-Host "COMMIT 3 done: $(git rev-parse --short HEAD)"

Set-Content (Join-Path $Ws 'src\scss\style.scss') -Value $styleFull -NoNewline
Set-Content (Join-Path $Ws 'src\pages\index.html') -Value $indexFull -NoNewline
Stage-Fp0002 @(
    'workspaces/fp-0002-shpigovsky-v6/src/scss/style.scss',
    'workspaces/fp-0002-shpigovsky-v6/src/pages/index.html',
    'workspaces/fp-0002-shpigovsky-v6/src/partials/sections/home-why-us.html',
    'workspaces/fp-0002-shpigovsky-v6/reviews/main-content/FP-0002-V6-PRE-REVIEWS-BLOCK-MAP.md'
)
Show-Staged
git commit -m "feat(fp-0002): integrate pre-reviews home blocks"
Write-Host "COMMIT 4 done: $(git rev-parse --short HEAD)"
