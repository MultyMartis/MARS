# REPORT — CATEGORY V2.1 LIST CARD LAYOUT FIX

**Site:** SITE-002 (BZPM / ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline:** CATEGORY V2.1 LIST CARD COMMERCE PASS  
**Deployed at (UTC):** 2026-06-09T21:32:48Z

---

## 1. Backup paths

Pre-change live captures (FTP):

| File | Backup path |
|------|-------------|
| `productcard.twig` | `projects/ocpilot/sites/site-002/backups/productcard.twig.pre-list-card-layout-fix.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-list-card-layout-fix.bak` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/category-v2.1-list-card-layout-fix-deploy-manifest-20260609-213248.json`

---

## 2. Changed files

| Local work copy | Remote path |
|-----------------|-------------|
| `category-v2.1-list-card-commerce-work/productcard.twig` | `catalog/view/theme/default/template/product/productcard.twig` |
| `category-v2.1-list-card-commerce-work/style.css` | `assets/css/style.css` |

Supporting (not deployed): `category-v2.1-list-card-layout-fix-work/` (deploy + QA scripts).

---

## 3. productcard.twig changes

Inside `.p-card__primary-spec` loop:

- Added `{% set spec_name = spec.name|lower %}`
- Added `.p-card__primary-spec-icon` with FA Pro icons (same mapping as PDP):
  - длина → `fad fa-arrows-alt-h`
  - ширина → `fad fa-arrows-alt-v`
  - высота → `fad fa-arrow-to-top`
  - масса → `far fa-weight-hanging`
  - fallback → `fal fa-info-circle`
- Wrapped `dt`/`dd` in `.p-card__primary-spec-content`
- Data, names, values — unchanged

---

## 4. style.css changes

**Scope:** `@media (min-width: 1025px) { .page--category .category--view-list ... }` only.

**Fix 1 — commerce column:**

- Grid col 3: `minmax(180px, auto)` stable width
- `.p-card__top`: absolute top/right, `z-index: 3`, status hidden (actions only)
- `.p-card__prices`: `margin-top: calc(40px + var(--pad-gap-mini))` — clears wishlist/compare
- `.p-card__footer`: column layout, fixed 180px width, row 2 / col 3
- `.product-card__actions`: column stack inside footer

**Fix 2 — primary specs simplify:**

- Removed background, border, border-radius, padding from `.p-card__primary-specs`
- Compact 4-col grid with gap only

**Fix 3 — icon layout (list scope only):**

- `.p-card__primary-spec`: flex row + gap
- `.p-card__primary-spec-icon`: 24×24 flex container
- `.p-card__primary-spec-content`: column stack for dt/dd

---

## 5. PHP confirmation

`product_results.php` — **NOT touched**. No PHP, JS, DB, OCMOD, category.twig, main.js changes.

---

## 6. QA — grid / list / mobile

| Context | Viewports | Result |
|---------|-----------|--------|
| Grid | 1920, 1440, 1366, 1280 | PASS — specs hidden |
| List | 1920, 1440, 1366, 1280 | PASS — specs visible (4 icons), media 200px, no overlap, no overflow |
| Mobile grid | 768, 576, 390, 375, 360 | PASS — specs hidden, switcher hidden |

QA JSON: `projects/ocpilot/sites/site-002/qa/category-v2.1-list-card-layout-fix/category-v2.1-list-card-layout-fix-qa-result.json`

---

## 7. Regression

| Context | Result |
|---------|--------|
| PDP V4 | PASS — hero 3 cols, commerce, content intact |
| Search | PASS — 0 visible specs blocks |
| Wishlist | PASS — 0 visible specs blocks |
| Compare | PASS — 0 visible specs blocks |
| Related on PDP | PASS — 0 card specs in related |

---

## 8. Screenshot paths

`projects/ocpilot/sites/site-002/qa/category-v2.1-list-card-layout-fix/`

- `category-list-1920.png`, `category-list-1440.png`, `category-list-1366.png`, `category-list-1280.png`
- `category-grid-1920.png`, `category-grid-1440.png`, `category-grid-1366.png`, `category-grid-1280.png`
- `category-mobile-grid-768.png`, `576`, `390`, `375`, `360`
- `pdp-v4-regression-1920.png`

---

## 9. Rollback procedure

1. FTP restore from backups:
   - `productcard.twig.pre-list-card-layout-fix.bak` → `catalog/view/theme/default/template/product/productcard.twig`
   - `style.css.pre-list-card-layout-fix.bak` → `assets/css/style.css`
2. Clear `system/storage/cache/template/*`
3. Hard-refresh browser (CSS cache)

Or run deploy script pointed at backup files.

---

## 10. Git status

New/untracked under `projects/ocpilot/sites/site-002/`:

- `backups/productcard.twig.pre-list-card-layout-fix.bak`
- `backups/style.css.pre-list-card-layout-fix.bak`
- `backups/category-v2.1-list-card-layout-fix-deploy-manifest-*.json`
- `category-v2.1-list-card-commerce-work/productcard.twig` (modified)
- `category-v2.1-list-card-commerce-work/style.css` (modified)
- `category-v2.1-list-card-layout-fix-work/`
- `qa/category-v2.1-list-card-layout-fix/`
- `reports/SITE-002-CATEGORY-V2.1-LIST-CARD-LAYOUT-FIX.md`

**Commit:** NO  
**Push:** NO
