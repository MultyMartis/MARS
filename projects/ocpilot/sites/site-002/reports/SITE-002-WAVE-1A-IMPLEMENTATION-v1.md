# REPORT — WAVE 1A IMPLEMENTATION

**Site ID:** SITE-002 (ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Wave:** 1A — PDP Hero (live implementation)  
**Date:** 2026-06-09  
**Scope:** Hero only — `producthero.twig` + `assets/css/style.css`

**Technical source:** [SITE-002-WAVE-1A-IMPLEMENTATION-MAP-v1.md](SITE-002-WAVE-1A-IMPLEMENTATION-MAP-v1.md)

**Pilot SKU (QA):** Стол производственный СП-П-18/6 —  
https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850

---

## 1. Backup paths

FTP backup выполнен **до** загрузки изменений.

| Artifact | Local backup path | Remote original |
|----------|-------------------|-----------------|
| `producthero.twig` (timestamped) | `projects/ocpilot/sites/site-002/backups/producthero.twig.20260608-202723.bak` | `catalog/view/theme/default/template/product/producthero.twig` |
| `style.css` (timestamped) | `projects/ocpilot/sites/site-002/backups/style.css.20260608-202723.bak` | `assets/css/style.css` |
| `producthero.twig` (rollback alias) | `projects/ocpilot/sites/site-002/backups/producthero.twig.pre-w1a.bak` | same |
| `style.css` (rollback alias) | `projects/ocpilot/sites/site-002/backups/style.css.pre-w1a.bak` | same |
| Deploy manifest | `projects/ocpilot/sites/site-002/backups/w1a-deploy-manifest-20260608-202723.json` | — |

**Server-side (pre-existing, not modified):** `producthero -backUp.twig` on FTP.

---

## 2. Changed files

| File | Action |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | **Deployed** — hero markup restructure |
| `assets/css/style.css` | **Deployed** — hero layout, buy box, fit grid, mobile order |

**Local working copies (not on server):**

- `projects/ocpilot/sites/site-002/w1a-work/producthero.twig`
- `projects/ocpilot/sites/site-002/w1a-work/style.css`
- `projects/ocpilot/sites/site-002/w1a-work/w1a-deploy.py` *(operator tooling — contains FTP credentials; do not commit)*

**Untouched (scope lock respected):** `product.twig`, `producttabs.twig`, `relproducts.twig`, controllers, models, DB, SEO URLs, OCMOD, cart/compare/wishlist JS.

---

## 3. Before / After

### A — Removed demo noise

| Element | Before | After |
|---------|--------|-------|
| AssuM demo logo | `.product-hero__brand` + `/assets/img/demo/assum_logo.png` | **Removed** |
| Placeholder subtitle | `{{ heading_subtitle }}` visible | **Removed** from hero |
| Article copy | `data-copy=""` (broken) | `data-copy="{{ model }}"` |

### B — Hero layout 30% / 70%

| Aspect | Before | After |
|--------|--------|-------|
| Grid | `1fr 1fr` (50/50) | `3fr 7fr` (~30/70) via `.product-hero__layout` |
| Gallery height | Fixed 520px | `aspect-ratio: 4/3`, `max-height: 420px` |
| Structure | Two `<span>` stacks in `.product-hero__info` | Named grid areas: media / identity / buybox / actions |

### C — Product Context Block

| Aspect | Before | After |
|--------|--------|-------|
| Series visibility | Breadcrumb only (header) | **Context band** from `breadcrumbs[length-2]` when `href` + `text` valid |
| Fallback | — | Block **hidden** if heuristic fails (`--has-context` modifier absent) |
| Pilot value | — | «Столы ПРЕМИУМ-600» → category link |

### D — Fit attributes grid

| Aspect | Before | After |
|--------|--------|-------|
| Presentation | Vertical `.product-hero__props` list | **4-column compact grid** `.product-hero__fit-grid` |
| Data source | `super_atts[]` only | Same — no new DB queries |
| Pilot SKU | 4 rows (L/W/H/mass) | 4 cells in grid (2×2 on tablet, 1 col on narrow mobile) |

### E — Commercial Card

| Aspect | Before | After |
|--------|--------|-------|
| Status + price + CTA + qty | Scattered in identity column | Unified **`.product-hero__buybox`** card (border, shadow, padding) |
| JS hooks | `data-cart-pdp`, `data-cart-add`, `data-cart-qty` | **Preserved** on same elements |

### F — Compare / Wishlist

| Aspect | Before | After |
|--------|--------|-------|
| Position | Below props, icon-only in `.product-hero__actions-wrap` | **`.product-hero__actions-row`** beside B2B preview |
| Handlers | `data-fav-toggle`, `data-compare-toggle` | **Unchanged** |
| Labels | Icon-only | Icon + text label (accessibility / wireframe P2) |

### Mobile commercial-first (P1)

| Order | Block |
|-------|-------|
| 1 | Buy box |
| 2 | Context band (if present) |
| 3 | Identity + fit grid |
| 4 | Actions row |
| 5 | Gallery (deprioritized) |

---

## 4. Rollback procedure

1. Upload rollback backups via FTP:
   - `projects/ocpilot/sites/site-002/backups/producthero.twig.pre-w1a.bak` → `catalog/view/theme/default/template/product/producthero.twig`
   - `projects/ocpilot/sites/site-002/backups/style.css.pre-w1a.bak` → `assets/css/style.css`
2. Clear OpenCart Twig cache: `system/storage/cache/template/` (directory was empty at deploy; clear after restore if populated).
3. Hard-refresh storefront (Ctrl+F5) and verify hero reverts to 50/50 layout with brand/subtitle.

**Blast radius:** PDP hero presentation only. Tabs, related products, cart/compare/wishlist endpoints unchanged.

**Operator script:** `py projects/ocpilot/sites/site-002/w1a-work/w1a-deploy.py backup-only` re-downloads live files without deploying.

---

## 5. Screenshots

**Location:** `projects/ocpilot/sites/site-002/qa/w1a-screenshots/`

| File | Viewport | Description |
|------|----------|-------------|
| `desktop-hero-full.png` | 1440×900 | Full hero — context band, 30/70 grid, buy box, fit grid |
| `desktop-hero-fold.png` | 1366×768 | First-screen fold |
| `mobile-hero-full.png` | 390×844 | Commercial-first mobile stack |
| `mobile-hero-fold.png` | 375×667 | Mobile fold |

**Before screenshots:** not captured live (backup-only). Visual baseline documented in [SITE-002-BASELINE-v1.md](SITE-002-BASELINE-v1.md) and `.recovery-temp/site-002-w1a-prep/`.

---

## 6. Post-deploy verification

Automated probe (`w1a-verify.py`) on pilot SKU:

| Check | Result |
|-------|--------|
| `.product-hero__layout` | OK |
| `.product-hero__buybox` | OK |
| `.product-hero__fit-grid` | OK |
| `.product-hero__context` | OK |
| `.product-hero__actions-row` | OK |
| Brand / subtitle absent | OK |
| `data-cart-pdp` / fav / compare hooks | OK |
| Fit cells | 4 |

**Alternate pilot URL** (ВМЦ-П3-2/500 from map): **404** on TEST — URL needs confirmation before Wave 1B attribute-rich QA.

**Twig cache:** `system/storage/cache/template/` — 0 files cleared (directory empty at deploy time).

---

## 7. Limitations (found in W1A)

| ID | Limitation | Severity |
|----|------------|----------|
| L-01 | **Context band = `breadcrumbs[n-2]`** — on deep taxonomies this is leaf category, not always marketing «series» name | High |
| L-02 | **Fit grid ≤4 cells** on pilot стол — `SUPER_ATTS` IDs 12/13/15 often empty; no 8-cell shell with placeholders shipped | High |
| L-03 | **No series descriptor, sibling count, adjacent series links** — deferred by scope | Expected |
| L-04 | **`deliveryText` sparse** — B2B preview row shows dealer link; delivery line often empty in-stock | Medium |
| L-05 | **Sink pilot URL 404** — PREMIUM-3 SKU path from prep doc not reachable | Medium |
| L-06 | **Context block hidden** on products without category path in URL (manufacturer/search-only routes) | Medium |
| L-07 | **Fold density on 1366×768** — band + identity + grid + buy box may exceed first screen; acceptable for Alpha, needs UX QA | Low |

---

## 8. Recommendations for Wave 1B

1. **Controller series DTO** — pass explicit `series_name`, `series_href`, `series_descriptor`, `sibling_count` instead of breadcrumb heuristic (resolves L-01, L-03).
2. **Expand `SUPER_ATTS`** — add category-critical attribute IDs per taxonomy; populate CMS on pilot series (resolves L-02).
3. **Confirm PREMIUM-3 pilot URL** on TEST and re-run QA with 8-attribute SKU (map suggestion: ВМЦ-П3-2/500).
4. **Min spec summary (USR-PDP-09)** — surface key rows from `attribute_groups` below hero or in tabs wave; out of W1A scope.
5. **Delivery copy tuning** — controller/content ops for consistent `deliveryText` on под-заказ SKUs.
6. **Visual polish** — series band tint/typography alignment with Hi-Fi Alpha tokens once design system pass starts.
7. **Manual QA checklist** — cart add/qty, wishlist toggle, compare toggle, Fancybox gallery, «Запросить цену» branch on `showrequest` SKU.

---

## 9. Git status

**Git commit:** not performed (per operator instruction).  
**Git push:** not performed.

**New / modified repo paths (uncommitted):**

- `projects/ocpilot/sites/site-002/backups/*`
- `projects/ocpilot/sites/site-002/w1a-work/*`
- `projects/ocpilot/sites/site-002/qa/w1a-screenshots/*`
- `projects/ocpilot/sites/site-002/reports/SITE-002-WAVE-1A-IMPLEMENTATION-v1.md` *(this file)*

---

## SECURITY NOTE

FTP credentials used from operator recovery tooling (external to repo). **`w1a-deploy.py` must not be committed** without credential removal. No secrets added to tracked documentation.

---

*Implementation complete on TEST. Rollback paths verified via pre-deploy FTP backup.*
