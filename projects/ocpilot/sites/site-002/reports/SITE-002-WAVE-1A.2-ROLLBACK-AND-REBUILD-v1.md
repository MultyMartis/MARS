# REPORT — WAVE 1A.2 ROLLBACK AND REBUILD

**Site ID:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Wave:** 1A.2 — PDP Hero rollback + rebuild  
**Date:** 2026-06-09  
**Scope:** Hero only — `producthero.twig` + `assets/css/style.css`

**Pilot SKU (QA):** Стол производственный СП-П-18/6 —  
https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850

---

## 1. Rollback confirmation

| Step | Result |
|------|--------|
| Live failed W1A saved before restore | **OK** |
| `producthero.twig.pre-w1a.bak` uploaded | **OK** (8562 B) |
| `style.css.pre-w1a.bak` uploaded | **OK** (252353 B) |
| Twig template cache cleared | **OK** (0 files — directory empty) |
| Storefront reverted to pre-W1A markup | **OK** — `.product-hero__grid` restored, `.product-hero__layout` absent |
| Rollback screenshots | **OK** — `qa/w1a-screenshots/rollback-*.png` |

**Rollback manifest:** `projects/ocpilot/sites/site-002/backups/w1a-rollback-manifest-20260608-205755.json`

**Failed W1A archive (for audit):**

| File | Path |
|------|------|
| Twig | `projects/ocpilot/sites/site-002/backups/producthero.twig.failed-w1a.20260608-205755.bak` (9638 B) |
| CSS | `projects/ocpilot/sites/site-002/backups/style.css.failed-w1a.20260608-205755.bak` (255407 B) |

---

## 2. Restored files (rollback target)

| Remote path | Local source |
|-------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `backups/producthero.twig.pre-w1a.bak` |
| `assets/css/style.css` | `backups/style.css.pre-w1a.bak` |

Original pre-W1A backups from first W1A run remain unchanged (`20260608-202723` timestamped copies).

---

## 3. New backup paths (before W1A.2 deploy)

FTP backup taken **after rollback**, immediately **before** W1A.2 upload:

| Artifact | Path |
|----------|------|
| Twig (timestamped) | `backups/producthero.twig.20260608-205835.bak` |
| CSS (timestamped) | `backups/style.css.20260608-205835.bak` |
| Twig (W1A.2 rollback alias) | `backups/producthero.twig.pre-w1a2.bak` |
| CSS (W1A.2 rollback alias) | `backups/style.css.pre-w1a2.bak` |
| Deploy manifest | `backups/w1a-deploy-manifest-20260608-205835.json` |

---

## 4. Changed files (W1A.2)

| File | Action |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | **Deployed** — 3-column hero, brand kept, controls preserved |
| `assets/css/style.css` | **Deployed** — layout 30/45/25, buy box card, fit grid, gallery compact |

**Local working copies:**

- `projects/ocpilot/sites/site-002/w1a-work/producthero.twig`
- `projects/ocpilot/sites/site-002/w1a-work/style.css`

**Scope lock respected:** no changes to `product.twig`, tabs, related, controllers, models, DB, JS, OCMOD.

---

## 5. What changed vs failed W1A

| Topic | Failed W1A | W1A.2 |
|-------|------------|-------|
| Assum brand | Removed | **Kept** — compact 96×32 block in identity column |
| Subtitle | Removed entirely | **Conditional** — hidden only for placeholder string; mechanism kept |
| Article copy | Fixed `data-copy` | **Kept** fix |
| Buy box position | Second grid row under media (~detached) | **Same row** as media + identity (3-col desktop; 2-col tablet) |
| Wishlist / compare | Text buttons (`.product-hero__action-btn` + labels) | **Restored** round `.btn-no-text` icon buttons + tooltips |
| Dealer CTA | «Купить как дилер» in hero | **Removed** |
| B2B preview row | Present | **Removed** |
| Product Context | Series band | **Minimal** — label «Серия» + link only; hidden if heuristic fails |
| Mobile order | Commercial first, gallery last | **Image first** → context → identity → buy box |
| Fit attributes | 4-col grid | **Kept** grid; same `super_atts` source |
| Gallery | 4:3 compact | **Kept**; max-height 420px desktop |

---

## 6. Screenshots

**Location:** `projects/ocpilot/sites/site-002/qa/w1a-screenshots/`

| File | Description |
|------|-------------|
| `rollback-desktop-hero-full.png` | Pre-W1A baseline after rollback (50/50 grid, brand + placeholder subtitle) |
| `rollback-mobile-hero-full.png` | Pre-W1A mobile |
| `w1a2-desktop-hero-full.png` | W1A.2 — 3-column: media / identity+band / buy box |
| `w1a2-desktop-hero-fold.png` | W1A.2 first-screen fold |
| `w1a2-mobile-hero-full.png` | W1A.2 — image early, buy box after identity + fit grid |
| `w1a2-mobile-hero-fold.png` | W1A.2 mobile fold |

---

## 7. QA results

### Automated HTML probe (`w1a2-verify.py`)

| Check | Result |
|-------|--------|
| Layout / buy box / fit grid / context | OK |
| Assum brand present | OK |
| Placeholder subtitle absent | OK |
| `data-cart-pdp`, fav, compare hooks | OK |
| Round `btn-no-text` wishlist | OK |
| No dealer / no B2B row / no failed-W1A action buttons | OK |
| Fancybox hook | OK |
| Fit cells | 4 |
| Context | «Столы ПРЕМИУМ-600» |

### Interactive smoke (`w1a2-qa.py`, desktop 1440×900)

| # | Requirement | Result | Notes |
|---|-------------|--------|-------|
| 1 | Add to cart works | **OK** | Qty updates after click |
| 2 | Qty stepper works | **OK** | `+` increments |
| 3 | Wishlist round + feedback | **OK** | `btn-no-text`, toggle/tooltip |
| 4 | Compare round + feedback | **OK** | `btn-no-text`, toggle/tooltip |
| 5 | Product gallery works | **OK** | Main swiper slide present |
| 6 | Fancybox works | **OK** | Lightbox opens on image click |
| 7 | Assum brand visible | **OK** | Logo in hero |
| 8 | Placeholder subtitle hidden | **OK** | No `.product-hero__subtitle` on pilot SKU |
| 9 | Buy box near title/price | **OK** | Same row as title on desktop; not under image column |
| 10 | Mobile image early | **OK** | Gallery first in mobile stack |

**Gallery thumbs:** N/A on pilot SKU — only one image; Twig renders thumbs block only when `images[]` is non-empty (pre-existing rule, not W1A.2 regression).

**Manual follow-up recommended:** re-test on multi-image SKU; confirm PREMIUM-3 sink URL when available on TEST.

---

## 8. Remaining risks

| ID | Risk | Severity |
|----|------|----------|
| R-01 | Series context still from `breadcrumbs[n-2]` — may not match marketing «серия» on deep taxonomies | High |
| R-02 | Fit grid often &lt; 8 cells — only populated `super_atts` shown | Medium |
| R-03 | Mobile buy box follows fit grid (after specs) — commercial block not immediately under title on narrow view | Low |
| R-04 | Tablet breakpoint (≤1200px) uses 2-col with buy box beside media lower cell — verify on real tablets | Low |
| R-05 | PREMIUM-3 pilot URL still unconfirmed on TEST for sink-series QA | Medium |

---

## 9. Rollback procedure

### Roll back W1A.2 → pre-W1A.2 (restored baseline)

1. FTP upload:
   - `backups/producthero.twig.pre-w1a2.bak` → `catalog/view/theme/default/template/product/producthero.twig`
   - `backups/style.css.pre-w1a2.bak` → `assets/css/style.css`
2. Clear `system/storage/cache/template/`
3. Hard-refresh PDP

### Roll back to original pre-W1A (full revert)

1. FTP upload:
   - `backups/producthero.twig.pre-w1a.bak` → `catalog/view/theme/default/template/product/producthero.twig`
   - `backups/style.css.pre-w1a.bak` → `assets/css/style.css`
2. Clear template cache

### Roll back failed W1A (reference only)

- `backups/producthero.twig.failed-w1a.20260608-205755.bak`
- `backups/style.css.failed-w1a.20260608-205755.bak`

**Operator scripts (local, not for commit):**

- Rollback: `py projects/ocpilot/sites/site-002/w1a-work/w1a-rollback.py`
- Deploy: `py projects/ocpilot/sites/site-002/w1a-work/w1a-deploy.py`
- Verify: `py projects/ocpilot/sites/site-002/w1a-work/w1a2-verify.py`
- QA smoke: `py projects/ocpilot/sites/site-002/w1a-work/w1a2-qa.py`
- Screenshots: `py projects/ocpilot/sites/site-002/w1a-work/w1a-screenshot.py [rollback|w1a2]`

**Blast radius:** PDP hero presentation only.

---

## 10. Git status

**Git commit:** not performed.  
**Git push:** not performed.

**New / modified repo paths (uncommitted):**

- `projects/ocpilot/sites/site-002/backups/*` (rollback + W1A.2 manifests)
- `projects/ocpilot/sites/site-002/w1a-work/*`
- `projects/ocpilot/sites/site-002/qa/w1a-screenshots/*`
- `projects/ocpilot/sites/site-002/reports/SITE-002-WAVE-1A.2-ROLLBACK-AND-REBUILD-v1.md`

---

## SECURITY NOTE

FTP credentials remain in local operator scripts only (`w1a-deploy.py`, `w1a-rollback.py`, `w1a-cache-probe.py`). **Do not commit** those files without credential removal. No secrets added to tracked documentation.

---

*W1A.2 live on TEST. Failed W1A archived; pre-W1A and pre-W1A.2 rollback paths verified.*
