# REPORT — SITE-002 PDP FULL ROLLBACK

**Site ID:** SITE-002  
**Environment:** TEST — https://zpm.new-site.space/  
**Date:** 2026-06-09  
**Action:** Full PDP rollback to pre-W1A baseline  
**Git commit:** NO  
**Git push:** NO

---

## Restored files (live FTP)

| Remote path | Size | Status |
|-------------|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | 8 562 B | Restored |
| `catalog/view/theme/default/template/product/producttabs.twig` | 3 305 B | Restored |
| `assets/css/style.css` | 252 353 B | Restored |

**Byte-for-byte verification:** all three live files **MATCH** local rollback sources (MD5 confirmed).

**Template cache:** `system/storage/cache/template/` — 0 files cleared (directory empty or already flushed).

---

## Exact backup files used

| Target | Backup source |
|--------|---------------|
| `producthero.twig` | `projects/ocpilot/sites/site-002/backups/producthero.twig.pre-w1a.bak` |
| `producttabs.twig` | `projects/ocpilot/sites/site-002/backups/producttabs.twig.pre-w1b.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-w1a.bak` |

**Selection rationale:**

- `pre-w1a` backups = earliest baseline before Hero redesign / Product Context / compactness CSS.
- `producttabs.pre-w1b.bak` = last snapshot with original tab UI (`js-tabs`: Описание / Характеристики / Документы) before W1B scroll-section conversion.

**Pre-rollback safety copies (W1B.2 state):**

- `backups/producthero.20260609-033251.pre-rollback.bak` (9 815 B — W1A/W1B.2 hero with `product-hero__layout`, context block)
- `backups/producttabs.20260609-033251.pre-rollback.bak` (3 126 B — scroll sections `product-pdp-sections`)
- `backups/style.20260609-033251.pre-rollback.bak` (263 409 B — W1B.2 CSS)

**Manifest:** `backups/rollback-pre-w1a-manifest-20260609-033251.json`

---

## Verification checklist

Test URL:  
`https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850`

| # | Check | Result |
|---|-------|--------|
| 1 | Hero returned to original layout (`product-hero__grid`, no `product-hero__layout`) | **PASS** |
| 2 | Assum brand as original (`product-hero__brand` + Assum logo) | **PASS** |
| 3 | Original subtitle behavior restored (`product-hero__subtitle`) | **PASS** |
| 4 | Original tabs restored: Описание / Характеристики / Документы | **PASS** (tab switch verified) |
| 5 | Related products unchanged (`rel-products` block «Похожие товары») | **PASS** |
| 6 | Cart works (`data-cart-add` → qty visible) | **PASS** |
| 7 | Qty works (`data-qty-plus` increments) | **PASS** |
| 8 | Wishlist works (`data-fav-toggle` → `active`) | **PASS** |
| 9 | Compare works (`data-compare-toggle` → `active`) | **PASS** |
| 10 | Gallery / Fancybox works (`data-fancybox="product"`) | **PASS** |

**Reverted W1A/W1B markers absent on live HTML:**

- `product-hero__layout`, `product-hero__context`, `product-hero__fit-grid`
- `product-pdp-sections`, `product-pdp-section--*`

---

## Screenshots

Saved to `projects/ocpilot/sites/site-002/qa/rollback-pre-w1a/`:

| File | Viewport |
|------|----------|
| `desktop-full-page.png` | 1440×900, full page |
| `desktop-hero.png` | 1440×900, hero crop |
| `mobile-full-page.png` | 390×844, full page |
| `mobile-hero.png` | 390×844, hero crop |

---

## Remaining differences (if any)

| Item | Status |
|------|--------|
| Controllers / models / DB | **Unchanged** (per scope) |
| JS bundles | **Unchanged** (per scope) |
| OCMOD | **Unchanged** (per scope) |
| `relproducts.twig` | **Unchanged** — not in rollback scope |
| `assets/css/style.min.css` | **Not restored** — storefront loads `style.css` (min variant commented out in header) |
| Subtitle placeholder text | **Present** — content from DB/controller (`heading_subtitle`), not a W1A artifact |

No unintended PDP template/CSS differences detected beyond pre-W1A baseline.

---

## Rollback confidence

**HIGH**

Evidence:

1. Live FTP files byte-identical to designated rollback backups.
2. Static HTML markers for W1A hero redesign and W1B scroll sections removed.
3. All 10 functional/visual checks passed on TEST.
4. Pre-rollback W1B.2 state preserved locally for re-reference.

---

## Local artifacts (this run)

**New/changed under repo (not committed):**

- `projects/ocpilot/sites/site-002/rollback-work/` — deploy, verify, screenshot helpers
- `projects/ocpilot/sites/site-002/backups/rollback-pre-w1a-manifest-20260609-033251.json`
- `projects/ocpilot/sites/site-002/backups/*.20260609-033251.pre-rollback.bak`
- `projects/ocpilot/sites/site-002/qa/rollback-pre-w1a/*.png`

**SECURITY:** FTP credentials used from existing operator deploy scripts only; not committed to repo in this report.
