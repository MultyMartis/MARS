# SITE-002 TECHNICAL KNOWLEDGE MAP

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`  
**Created:** 2026-06-19  
**Purpose:** Persistent technical reference for operators and agents working on SITE-002.

**Evidence cutoff:** M9.8.9 filter recovery (06D–06M) + filter UX polish (04–08A) + tooltips (01) + Commercial Trust (03B/03C) + catalog state persistence (09A–09C) + hub cleanup (10) + operator manual polish (2026-06-21 live state) + M9.13 About Company redesign/polish/rejection/restoration (2026-06-23) + BZPM recovery closeout (2026-06-28).

---

## 0. BZPM UX Redesign — project lifecycle

| Field | Value |
|-------|--------|
| **Recovery status** | **CLOSED** (2026-06-28) |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Current phase** | **PRODUCTION PREPARATION** |
| **Next phase** | **Production Development** — Corporate Pages implementation after operator gates |
| **Closeout** | [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](../reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |

**Lifecycle:** Research → Corporate Pages Program → Recovery (**CLOSED**) → Production Development

**M9.13 About redesign:** **ARCHIVED** · **NOT ACTIVE** — live authority = restored pre-redesign only (`SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`). See **§17**.

**Operator implementation order (remaining pages):** M9.14 Delivery **IMPLEMENTED** · M9.15 Payment **IMPLEMENTED** · M9.17 Warranty **IMPLEMENTED** · M9.16 Dealers **IMPLEMENTED** · M9.18 Custom Manufacturing **IMPLEMENTED** — Corporate Pages Program implementation phase **COMPLETE on TEST** (pending operator B6/B8).

---

## 1. Authority Rules

### Source of truth (priority order)

| # | Source | Rule |
|---|--------|------|
| 1 | **Live TEST** (`zpm.new-site.space`) | Authoritative runtime state |
| 2 | **Beget full backup** | Operator-controlled disaster recovery |
| 3 | **Manual UI / CSS / Twig / JS refinements** | **CANONICAL** — operator edits on live override older deploy snapshots |
| 4 | **This Knowledge Map** | Architecture and discovered behaviour — update when new forensic evidence appears |
| 5 | **Latest Stable Checkpoint** | [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) |

### Current stable state

- **Authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`
- **Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`
- **Catalog UX cluster:** filter recovery (06D–06M) → filter UX (04–08A) → tooltips (01) → Commercial Trust (03B/03C + operator polish) → catalog state persistence (09A–09C) → hub cleanup (10)
- **About page:** M9.13 redesign **rejected by operator** — live `/about` **restored** to pre-redesign version (operator-approved restoration, not rollback failure)

### Manual UI refinements are canonical

Operator manual CSS, Twig, JS, and UX edits on live TEST are the **visual and behavioural authority**. Repo work copies (`*-work/`), prior STABLE folders, and `.pre-*.bak` from earlier passes are **historical** unless refreshed by live FTP capture.

See also **§12 Operator Manual JS Refinements** (post M9.8.9-04A/04B operator polish).

### Conflict resolution

If documentation contradicts current TEST behaviour → **live TEST wins**. Update this map and checkpoint docs after verified forensic pass.

---

## 2. 1C Architecture

### Overview

1C exchange uses two XML files and a two-step cron sequence. Live path: `1c_incoming/webdata/` (legacy `1c_exchange/` is commented out in import handlers).

| File | Cron command | Handler | Purpose |
|------|--------------|---------|---------|
| `import0_1.xml` | `1c` | `import_1C.php` | Catalog: products, categories, attributes, images, SEO |
| `offers0_1.xml` | `1c_offers` | `import_1C_offers.php` | Prices and stock: `oc_product.price`, `oc_product.quantity` |

### Cron table (`cron` — no `oc_` prefix)

| id | name | command | Purpose |
|----|------|---------|---------|
| 1 | Импорт 1C | `1c` | `import0_*.xml` |
| 2 | Импорт 1C - цены и остатки | `1c_offers` | `offers0_*.xml` |

**Task selection** (`catalog/model/catalog/cronjob.php`):

```sql
SELECT * FROM `cron`
WHERE DATE_ADD(`lastrun`, INTERVAL `duration` SECOND) < NOW()
  AND active = 1;
```

Only **one** eligible task runs per HTTP hit; on success `lastrun` is updated and loop breaks.

### Entry point

```
https://zpm.new-site.space/index.php?route=common/cronjob
```

**Controller:** `catalog/controller/common/cronjob.php`

```
ControllerCommonCronjob::index()
  → ModelCatalogCronjob::getTasks()
  → switch command:
       '1c'        → parse1C()        → include import_1C.php
       '1c_offers' → parse1COffers() → include import_1C_offers.php
  → if $itsOK → setDone(cron_id)
```

### Operator import sequence (mandatory order)

1. Upload XML to `{site_root}/1c_incoming/webdata/`
2. **Step 1 — Catalog:**
   ```sql
   UPDATE cron SET active = 0;
   UPDATE cron SET active = 1 WHERE command = '1c';
   ```
   Hit cron URL → wait for product messages → `UPDATE cron SET active = 0 WHERE command = '1c';`
3. **Step 2 — Offers:**
   ```sql
   UPDATE cron SET active = 1 WHERE command = '1c_offers';
   ```
   Hit cron URL → wait for price/qty messages → `UPDATE cron SET active = 0 WHERE command = '1c_offers';`

Post-**M9.8.9-06F** live code: offers import calls `refreshPriceIndex()` for each updated `product_id`.

### import0_1.xml — what is imported

**File:** `catalog/controller/common/import_1C.php` → `processProduct1C()` → `import_1C_process.php`

| Imported | Not imported by this stage |
|----------|---------------------------|
| `xml_id`, model, image, manufacturer | `price`, `price2`, `price3`, `discount1c` |
| status, descriptions | `oc_product_price_index` |
| categories, attributes | specials / product_discount |
| dimensions (weight, width, height, length) | |

**Does NOT call** `refreshPriceIndex()`.

### offers0_1.xml — what is imported

**File:** `catalog/controller/common/import_1C_offers.php`

| Imported | Not imported |
|----------|--------------|
| `oc_product.quantity` | `price2`, `price3`, `discount1c` |
| `oc_product.price` (base retail) | categories, attributes, status |
| `refreshPriceIndex()` per updated ID (**since 06F**) | specials |

Match key: `xml_id` → `product_id`. Unknown `xml_id` offers are silently skipped.

### SAFE UNKNOWN

- Exact ocStore/OpenCart version line
- Whether cron was re-run after every XML upload (check `cron.lastrun` vs file mtime)
- Exact `<Предложение>` count in live `offers0_1.xml` at next import

---

## 3. Product Lifecycle

```
1C export
  │
  ├─ import0_1.xml ──► cron command '1c'
  │                      └─ import_1C.php
  │                           └─ processProduct1C()
  │                                └─ oc_product (insert/update)
  │                                └─ oc_product_description
  │                                └─ oc_product_attribute
  │                                └─ oc_product_to_category
  │                                └─ oc_product_image
  │                                └─ oc_seo_url (product_id=*)
  │
  └─ offers0_1.xml ──► cron command '1c_offers'
                         └─ import_1C_offers.php
                              └─ UPDATE oc_product.price, quantity
                              └─ refreshPriceIndex(product_id)  [since 06F]
                                   └─ oc_product_price_index

Storefront read paths:
  PLP filter/sort/range ──► oc_product_price_index (via getProducts/getCategoryPriceRange)
  PDP card price        ──► getProduct() — oc_product + price2/3/discount1c/special chain
  Cart / Checkout       ──► standard OC cart (not price index)
```

### SEO

Product SEO URLs created during catalog import (`oc_seo_url` where `query LIKE 'product_id=%'`). Category SEO preserved across product reset.

### Images

Physical files: `image/catalog/1c_import/`. Product reset does **not** delete image files; fresh import re-links paths.

---

## 4. Pricing System

### Fields on `oc_product`

| Field | Known role | Updated by 1C offers? |
|-------|------------|----------------------|
| `price` | Base retail price | **Yes** (`offers0_1.xml`) |
| `price2` | Dealer price (customer group mapping in `getProduct`) | **No** — not in offers import |
| `price3` | Wholesale price | **No** |
| `discount1c` | Percent discount from 1C | **No** in offers path |
| `quantity` | Stock | **Yes** |

### OpenCart standard tables

| Table | Role |
|-------|------|
| `oc_product_special` | Time-bound special prices per customer group |
| `oc_product_discount` | Quantity discounts per customer group |

### `getProduct()` price chain (PDP / cards)

Documented in live `catalog/model/catalog/product.php` captures:

1. Select base by customer group: default `price`, dealer → `price2`, wholesale → `price3`
2. Apply `discount1c` percent if > 0
3. Apply `product_discount` / `product_special` if active

**PLP filter does NOT use this chain directly** — it uses `oc_product_price_index` (see §5).

### Customer groups

- Guest / default storefront group used in filter forensic: **customer_group_id = 2**
- Index rows exist per customer group; full rebuild indexes all groups

### SAFE UNKNOWN

- Who populates `price2`, `price3`, `discount1c` in production (manual admin? separate 1C pass? legacy data?)
- Whether dealer/wholesale groups are actively used on TEST storefront
- Exact mapping of OC customer group IDs to B2B roles beyond group 2

---

## 5. Price Index System

### Table: `oc_product_price_index`

Denormalized effective prices per `product_id` × `customer_group_id`.

**Populated by:** `ModelCatalogProduct::refreshPriceIndex($product_id)` — DELETE + INSERT using `getProductForIndex()` logic (price / price2 / price3 / discount1c / specials).

### Used by (PLP / catalog filter layer)

| Feature | Method | Notes |
|---------|--------|-------|
| Price range slider min/max | `getCategoryPriceRange()` | Aggregates index; excludes `effective_price <= 0` since **06H** |
| `price_from` / `price_to` filter | `getProducts()`, `getTotalProducts()` | Uses effective price expression |
| `only_with_price` | `getProducts()` | Forces `price_from >= 1` on effective price |
| `only_discount` | `getProducts()` | Index `special` column |
| Sort `sort=p.price` | `getProducts()` ORDER BY | Effective price since **06M** |

### NOT used by

| Surface | Price source |
|---------|--------------|
| **PDP** | `getProduct()` |
| **Cart** | Cart session / OC cart model |
| **Checkout** | Cart + order totals |

### Effective price expression (current live — post 06M)

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

**Critical discovery:** `IFNULL(ppi.special, ppi.price)` treats `special = 0` (common after offers import) as effective price **0**, breaking filters. Fixed in **M9.8.9-06M**.

### M9.8.9 discoveries (preserved)

| Task | Finding | Resolution |
|------|---------|------------|
| **06D** | Category 301 had **1/419** index rows (0.24%); slider collapsed to 51280–51281 | Targeted `refreshPriceIndex` × 418 → 100% coverage; range 5405–72630 |
| **06F** | Offers import never called `refreshPriceIndex` | Hook in `import_1C_offers.php` — batch refresh after each file |
| **06H** | Zero-price SKUs («По запросу») pulled `min_price` to 0 in sidebar | `getCategoryPriceRange()` excludes `effective_price <= 0` |
| **06M** | `IFNULL(special, price)` broke `only_with_price`, price sort, combined attr+price filters | Align filter/sort/count with `IF(special > 0, …)` |

### Manual maintenance

`reindex_prices.php` at site root — loops all products via admin model. **Not** wired to cron. Use for bulk catch-up if hook missed.

---

## 6. Filter System

### Filter profiles

**Location (live):** `system/library/zpm/filter_profiles/`

**Resolver:** `system/library/zpm/filter_profile_resolver.php` — `resolveForCategory($category_id)` → profile PHP array.

| Profile file | Branch root | category_id |
|--------------|-------------|-------------|
| `301_stoly.php` | Столы | 301 |
| `322_podtovarniki.php` | Подтоварники | 322 |
| `326_telezhki.php` | Тележки | 326 |
| `80_moechnye_vanny.php` | Моечные ванны | 80 |
| `207_zonty.php` | Зонты вытяжные | 207 |
| `global_hidden.php` | Global hide list | — |

Profile schema: `primary_attribute_ids`, `secondary_attribute_ids`, `hidden_attribute_ids`, sort weights.

Controller applies profile in `getCategory()` path via `applyProfileToAttributes()`.

### Filter UI

- Form: `[data-filters-form]` inside `[data-filters]`
- Sidebar mobile: `[data-filter-sidebar]` + `[data-filter-open]` / `[data-filter-close]`
- Groups: `<section class="flt__group">`
- JS: `syncFromRanges()` writes `price_from`/`price_to` into form on init — **any attribute click submits price range too**

### Numeric attributes (M9.8.9-06J)

**Bug:** attrs **47**, **51** have **empty** `filter_name` in `oc_attribute_description` → sidebar renders `attr[51][]` (numeric key).

**Old SQL:** `ad.filter_name = '51'` → 0 rows.

**Fix (06J):** if `is_numeric($attr_slug)` → `pa.attribute_id = (int)$attr_slug`; else slug branch unchanged.

### Slug attributes

Attributes with populated `filter_name` (e.g. `construction`, `shell-size`, `table-top-material`) use:

```sql
AND ad.filter_name = '{slug}'
```

### Combined filter behaviour (06K)

Isolated `attr[51][]` URL works. Sidebar form also sends price params → before **06M** caused 0 cards. After **06M**: combined attr + `only_with_price` works on Столы (15 cards).

### SAFE UNKNOWN

- Full list of attributes with empty `filter_name` beyond 47 and 51
- Whether `len_from`/`w_from`/`h_from` dimension filters use separate SQL path (not attribute_id branch)

---

## 7. Filter Architecture

End-to-end PLP filter behaviour on live TEST (post M9.8.9 filter recovery + UX wave).

### Filter sidebar

| Layer | Location | Role |
|-------|----------|------|
| **Template** | `catalog/view/theme/default/template/sections/filterssidebar.twig` | Renders `[data-filters]` / `[data-filters-form]`; attribute groups `.flt__group`; price/LWH ranges; switches; global reset footer |
| **Mobile shell** | Same twig + `style.css` | `[data-filter-sidebar]`, open/close hooks, `.category__sidebar__overlay` |
| **Controller data** | `catalog/controller/product/category.php` | Builds `filter_groups`, `filter_subcategories`, price range, `filter_custom` from query |
| **Profiles** | `system/library/zpm/filter_profiles/*.php` | Per-branch attribute visibility and sort weights |

**Hidden subcategories policy (M9.8.9-07):** Sidebar block `<!-- SUBCATEGORIES -->` gated by `{% if false and filter_subcategories %}` — **UI only**. Controller, `filter_custom['s']`, and SQL `product_to_category` IN clause remain intact for restore.

### AJAX flow

```
User change (checkbox / range / switch / group reset / global reset)
  → syncChoiceClasses(root)          — visual .active on labels; group-reset disabled state (08A)
  → updateBrowserUrl(form)           — serialize form → query param `filters` (+ preserve sort/limit)
  → debounced updateProducts(root)   — fetch full category URL
  → parse HTML → replace .category__grid + .pagination
  → scrollToCategorySection()        — offset 0 (04B canonical)
```

Filter state is **not** a separate API — vanilla JS fetches the full PLP page and swaps grid fragments.

### `syncChoiceClasses(root)`

- Scoped to filter root `[data-filters]`
- Toggles `.active` on `.flt__check` labels from `:checked` on `.flt__check-input`
- Calls `updateGroupResetVisibility(root)` (08/08A) — `disabled` + `.is-active` on `[data-filter-group-reset]` per attribute group
- Invoked on init, checkbox change, group reset, global reset

### `updateBrowserUrl(form)`

- Reads `[data-filters-form]` fields into semicolon-separated `filters` payload (PHP `parse_str` compatible)
- Updates `history.replaceState` / URL without full navigation
- Preserves non-filter query params (`sort`, `order`, `limit`, `page`)
- Triggers debounced `updateProducts` via change handlers on checks and ranges

### `updateProducts(root)`

- `fetch(location.href)` — full category page
- Replaces `.category__grid` and `.pagination` from response
- Calls `scrollToCategorySection()` — targets category section anchor, **not** `grid.scrollIntoView` (04)
- Re-inits pagination AJAX handlers on new DOM

### Group reset (08 / 08A)

| Item | Behaviour |
|------|-----------|
| Scope | Attribute checkbox groups only (not price, LWH, switches, subcategories) |
| Trigger | `[data-filter-group-reset]` inside `.flt__group-body` (08A position) |
| Action | Uncheck panel inputs; remove `.active`; `syncChoiceClasses` → `updateBrowserUrl` |
| Visibility | Button always rendered; `disabled` when no selection; `.is-active` when group has checks |

### Global reset

- Footer control clears all checks, ranges to min/max, switches, search inputs
- Resets URL to pathname; calls `updateProducts(root)`

### Numeric attributes

Attributes with **empty** `filter_name` render as `attr[47][]`, `attr[51][]` (numeric keys). SQL branch (06J): `pa.attribute_id = (int)$slug` instead of `ad.filter_name = '{slug}'`.

### Effective price logic

PLP filter/sort/count uses `oc_product_price_index` with expression:

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

**Not** `IFNULL(special, price)` — special=0 after offers import must fall back to base price (06M).

### Price index dependency

| Operation | Index touch |
|-----------|-------------|
| Catalog import (`1c`) | **No** automatic refresh |
| Offers import (`1c_offers`) | `refreshPriceIndex(product_id)` per updated SKU (06F) |
| `getCategoryPriceRange()` | Reads index; excludes `effective_price <= 0` (06H) |
| `getProducts()` price filter/sort | Reads index effective price (06M) |

Bulk catch-up: `reindex_prices.php` at site root (manual, not cron).

**Evidence:** [SITE-002-M9.8.9-08-FILTER-GROUP-RESET-FORENSIC.md](../reports/SITE-002-M9.8.9-08-FILTER-GROUP-RESET-FORENSIC.md) · [SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md](../reports/SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md)

---

## 8. Live Files With Business Logic

Canonical live paths on TEST — capture before any deploy in these areas.

| File | Why it matters |
|------|----------------|
| `catalog/model/catalog/product.php` | **Filter SQL core** — `getProducts()`, `getTotalProducts()`, `getCategoryPriceRange()`; numeric attribute branch (06J); effective price expression (06M); zero-price exclusion (06H); `refreshPriceIndex()` / `getProductForIndex()` |
| `catalog/controller/common/import_1C_offers.php` | **1C offers pipeline** — updates `oc_product.price` + `quantity`; calls `refreshPriceIndex()` after each product (06F); price index stays in sync with offers XML |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | **Filter sidebar markup** — form structure, attribute groups, group-reset buttons (08/08A), subcategories hide gate (07), price/LWH ranges, global reset |
| `assets/js/main.js` | **Filter client orchestration** — `syncChoiceClasses`, `updateBrowserUrl`, `updateProducts`, `scrollToCategorySection` (04/04B), `initGroupReset` (08/08A), wishlist/compare tooltips (01), global filter reset |
| `assets/css/style.css` | **Filter + PLP + Commercial Trust presentation** — sidebar layout, `.flt__group-reset` states (08A), mobile filter shell, category grid density (operator polish), `.zpm-commercial-trust*` block (03C + operator polish), overlay coordination |
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | **Commercial Trust block markup** — category PLP CTA: header, cert podium, OEM benefits, lead form, FAQ grid (operator polish canonical) |
| `catalog/controller/product/category.php` | **Commercial Trust dynamic H2** — `$data['commercial_trust_heading']` map + `blockcommercialtrust` view load |

**Rule:** Repo `*-work/` copies and `backups/*.pre-*` are deploy artefacts — **live TEST** is authority unless freshly captured.

---

## 9. Overlay System

### Global page overlay

| Element | Hook | CSS |
|---------|------|-----|
| `.page_overlay` | `[data-overlay]` | `body.has-overlay` toggles visibility |
| Themes | `body.overlay--light` / `body.overlay--dark` | blur + rgba background |
| Scroll lock | `body.is-scroll-locked` | `position: fixed` on body |

Used as shared backdrop for multiple popups (catalog mega menu, etc.).

### Desktop catalog mega menu

| Element | Hook / class |
|---------|--------------|
| Container | `.zpm-catalog`, `.zpm-catalog__megamenu` |
| Open state | `html.is-catalog-open` |
| Data prep | `prepareMegamenuCategories()` — hides zero-count branches |

Animation: fade + `translateY(100px → 0)` per `style.css` overlay section.

### Mobile menu

| Element | Hook |
|---------|------|
| Panel | `#zpmMobileMenu`, `[data-mobile-menu]` |
| Overlay | `.zpm-mmenu__overlay`, `[data-menu-close]` |
| Trigger | `aria-controls="zpmMobileMenu"` |

### Search

| Surface | Hook |
|---------|------|
| Mobile search overlay | `.zpm-qsearch-mobile__overlay`, `[data-qsearch-mobile-close]` |

**SAFE UNKNOWN:** desktop search overlay mechanism — not fully traced in repo evidence.

### Cart dropdown

**SAFE UNKNOWN:** exact DOM hooks and JS init path for header cart dropdown — not captured in M9.8.9 forensic bundle. Likely standard theme header partial.

### Catalog filter (mobile sidebar)

| Element | Hook |
|---------|------|
| Sidebar | `[data-filter-sidebar]` |
| Open | `[data-filter-open]` |
| Close | `[data-filter-close]` |
| Inner overlay | `.category__sidebar__overlay` |

Sidebar is `aria-hidden="true"` until opened; uses popup close button pattern (`.zpm-popup_close`).

### Overlay coordination

**SAFE UNKNOWN:** whether a single `has-overlay` class coordinates all subsystems or each popup manages its own overlay layer. PLP HTML shows **two** `.page_overlay` nodes — stacking behaviour not fully documented.

---

## 10. PDP Architecture

### Gallery (M9.8.1 — PDP Gallery Compact)

- Side-rail vertical thumbs on desktop (≥1025px); horizontal reinit on smaller viewports
- Single-image SKUs: no thumbs rail
- Fancybox hooks preserved (`data-fancybox`)
- Evidence: [m9.8.1-pdp-gallery-compact-qa-result.json](../qa/m9.8.1-pdp-gallery-compact/m9.8.1-pdp-gallery-compact-qa-result.json)

### Lightbox (M9.8.2 — PDP Lightbox Constraints)

- Fancybox with constrained viewport: desktop **80vw / 80vh**; mobile **95vw / 90vh**
- `object-fit: contain` — no crop/stretch
- Class: `is_product_fancybox` on panzoom content
- Evidence: [m9.8.2-pdp-lightbox-constraints-qa-result.json](../qa/m9.8.2-pdp-lightbox-constraints/m9.8.2-pdp-lightbox-constraints-qa-result.json)

### Specifications Collapse (PDP V5.1)

- Collapsible specs block in lower PDP content
- Evidence: [SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md](../reports/SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md)

### Scroll Offset (Wave 1B)

- Anchor scroll offset for PDP section navigation
- Evidence: [SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md](../reports/SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md)

### PDP price display

Uses `getProduct()` — **not** `oc_product_price_index`. Zero price → «По запросу» display.

---

## 11. Catalog Architecture

### Products Per Page (M9.8.5)

- Selector: 10 / 20 / 50 / 100 on PLP
- Query param: `limit`
- Evidence: [m9.8.5-products-per-page-qa-result.json](../qa/m9.8.5-products-per-page/m9.8.5-products-per-page-qa-result.json)

### Filter Profiles

See §6. Per-category PHP profiles control which attributes appear in sidebar and in what order.

### Category Images (M9.7)

- Hub mode category cards with WebP images
- Evidence: M9.7 image deploy reports

### Megamenu (M9.7)

- `prepareMegamenuCategories()` filters empty branches
- Template: `catalog/view/theme/default/template/common/megamenu.twig`
- Evidence: [REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md](../reports/REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md)

### PLP Layout (Category V2.x)

- Grid / list view switcher (desktop ≥1025)
- List card compactness passes V2.1–V2.3
- Scoped CSS: `.page--category`, `.category--view-list`
- Operator manual PLP polish (canonical)

### Hub Mode (M9.5)

- Parent categories show subcategory hub instead of flat product grid where configured

---

## 12. Operator Manual JS Refinements

**Registered:** M9.8.9-04B (2026-06-19) — operator manual edits on live TEST **after** M9.8.9-04A deploy pass.

**Policy:** Manual JS refinements on live TEST are **canonical**. Repo work copies, pass reports (including 04A), and deploy snapshots describe **historical** deploy state unless refreshed by live capture.

### Filter scroll offset

| Item | M9.8.9-04A report | Live canonical (post operator edit) |
|------|-------------------|-------------------------------------|
| `scrollToCategorySection()` offset | `15px` (fixed) | **`0`** |
| Location | `assets/js/main.js` | same |

Operator set offset to **0** on live. Treat **0** as authoritative for filter/AJAX scroll-to-category behaviour.

**Prior pass evidence (historical):** [SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md](../reports/SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md)

### Sticky header trigger

Operator manually adjusted the sticky header appearance threshold in `assets/js/main.js` on live TEST.

| Item | Status |
|------|--------|
| File | `assets/js/main.js` |
| Change type | Manual threshold tweak (sticky header show/hide) |
| Exact value | **SAFE UNKNOWN** — not captured in repo at registration time |
| Canonical | Live TEST behaviour |

### Pre-task rule (header / filter JS)

Before **any** JS task touching header sticky behaviour or catalog filter scroll:

1. **Verify live** `assets/js/main.js` on TEST (FTP capture or operator confirmation) — do not assume 04A report values.
2. Confirm current `scrollToCategorySection()` offset (canonical: **0**).
3. Confirm sticky header trigger matches live UX; document exact threshold if captured.
4. Treat operator manual JS as override over pass reports and work copies.

**Registration report:** [SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](../reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md)

---

## 13. Operational Rules

### PRE-TASK RULE (mandatory — all SITE-002 tasks)

Before **any** SITE-002 task:

1. **Read** this Technical Knowledge Map
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Verify Authority State** matches checkpoint name
4. **Check Active Roadmap Stage** — [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)
5. **Only then** perform audit or changes

### PRE-TASK RULE UPDATE (domain-specific — filters / sort / pagination / limit / only_with_price)

Before **any** task touching **filters**, **sort**, **pagination**, **limit**, or **only_with_price**:

1. **Read** this Technical Knowledge Map — **§16 Catalog State Persistence** (mandatory)
2. **Read** pass reports **M9.8.9-09A**, **M9.8.9-09B**, **M9.8.9-09C** as mandatory context
3. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
4. Test **interaction paths** — filter AJAX → limit click; limit → filter; full combo with sort + page — not only full-page URL loads

### PRE-TASK RULE UPDATE (domain-specific — About page)

Before **any** task touching the **About page** (`/about`, `information/about`) or planning a **new About redesign**:

1. **Read** this Technical Knowledge Map — **§17 About Page History** (mandatory)
2. **Read** [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md)
3. **Read** [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md)
4. **Read** [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md)
5. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
6. Treat **restored version** on live TEST as **source of truth** — M9.13 work copies are historical reference only

### PRE-TASK RULE UPDATE (domain-specific — filters / catalog / 1C / price / PLP)

Before **any** task touching **filters**, **catalog**, **1C import**, **price**, or **PLP**:

1. **Read** this Technical Knowledge Map — especially **§5 Price Index**, **§6 Filter System**, **§7 Filter Architecture**, **§8 Live Files With Business Logic**, **§16 Catalog State Persistence**
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** the specific business-logic files in scope (`product.php`, `import_1C_offers.php`, `filterssidebar.twig`, `main.js`, `style.css`, `category.php`) before deploy
4. Test isolated URL params **and** sidebar form submit; test `only_with_price` + attribute combos; verify price range min ≠ 0 when zero-price SKUs exist

### PRE-TASK RULE UPDATE (domain-specific — Commercial Trust / CTA)

Before **any** task touching **trust block**, **certificates**, **dealers form**, or **category CTA**:

1. **Read** this Technical Knowledge Map — **§14 Commercial Trust Block**
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** `blockcommercialtrust.twig`, `style.css`, `category.php` before deploy — do not trust 03C work copies or pass reports alone
4. Verify dynamic H2 on at least one mapped category + fallback category
5. Treat operator manual CSS/Twig on live as **canonical** over repo work copies

### Deploy rules (summary)

- Live FTP capture + SHA256 before any write
- Backup to `backups/*.pre-<pass>.bak`
- Clear Twig cache after deploy
- Document rollback in report
- See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md)

### 1C import rules

- Always: catalog (`1c`) **before** offers (`1c_offers`)
- Deactivate cron tasks after each step
- Post-import verify: product count, index coverage, sample PLP price range
- Never assume index is current without checking `oc_product_price_index` row count

### Filter change rules

- Test both isolated URL params and sidebar form submit
- Test `only_with_price` + attribute combo
- Test numeric (`attr[51][]`) and slug (`attr[construction][]`) keys
- Verify `getCategoryPriceRange` min ≠ 0 when zero-price SKUs exist

---

## 14. Commercial Trust Block

Category PLP decision-stage block — after product grid, before footer. **Live TEST is canonical**; M9.8.9-03C deploy + operator manual polish registered in `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` (catalog UX carried forward from Commercial Trust 01 / Catalog UX Complete 01).

### Purpose

Convert post-catalog evaluation into trust + lead capture: manufacturer proof (OEM, certs, «Сделано в России»), procurement reassurance, and price-list request form (`dialog=7`).

**Scope:** category PLP only. Homepage `certificates.twig`, `/katalog`, PDP, filters — **out of scope**.

### Structure (live canonical — 2026-06-21 capture)

```
section.zpm-commercial-trust[data-commercial-trust]
└── .container → .zpm-commercial-trust__card
    └── .zpm-commercial-trust__wrap (flex row)
        ├── .zpm-commercial-trust__info
        │   ├── .zpm-commercial-trust__header — label + H2 + lead
        │   └── .zpm-commercial-trust__main
        │       ├── .zpm-commercial-trust__cert-col — cert on podium (sert-base.jpg)
        │       └── .zpm-commercial-trust__benefits — 3 OEM benefit rows
        └── .zpm-commercial-trust__form-wrap
            ├── .zpm-decoration-with-logo — decor-logo.svg background contours
            └── .zpm-commercial-trust__form-col → form card (dialog=7)

section.zpm-catalog-faq
└── .zpm-commercial-trust__services--like-FAQ
    ├── «Частые вопросы» heading
    └── .zpm-commercial-trust__services — 8 FAQ cards (4-col grid desktop)
```

**Mobile stack:** header → cert → benefits → form → FAQ grid (2 columns ≤1024px).

### Files

| File | Role |
|------|------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | Markup — trust card + FAQ section |
| `catalog/controller/product/category.php` | Loads view; sets `commercial_trust_heading` |
| `assets/css/style.css` | Block `M9.8.9-03C` CSS + operator polish (podium, cert size, form, FAQ grid, logo decor) |
| `assets/img/certificates/thumb_00.png` | Visible certificate thumb |
| `assets/img/certificates/certificat_00.jpg` | Fancybox full-size target |
| `assets/img/sert-base.jpg` | Certificate podium base |
| `assets/img/decor-logo.svg` | Background logo contours in form wrap |

**Not used on live block:** `main.js` changes for Commercial Trust — form uses existing `zpm-form` / mask / validation patterns.

### Dynamic headings

`category.php` maps category name → H2:

| Category name | H2 |
|---------------|-----|
| Столы | Нужна помощь с выбором столов? |
| Моечные ванны | Нужна помощь с выбором моечных ванн? |
| Подтоварники и подставки | Нужна помощь с выбором подтоварников и подставок? |
| Тележки сервировочные | Нужна помощь с выбором тележек? |
| Зонты вытяжные | Нужна помощь с выбором зонтов? |
| **Fallback** | Подберём оборудование под вашу задачу |

Twig: `{{ commercial_trust_heading|default('Подберём оборудование под вашу задачу') }}`

### Certificate

| Item | Live behaviour |
|------|----------------|
| Visible count | **1** slide in `.swiper.js-commercial-trust-certs` |
| Display | Enlarged on podium (`__cert-card--base` + `sert-base.jpg`); `max-width: 250px` on cert card |
| Interaction | Fancybox `data-fancybox="certificates-plp"` on cert link |
| «Все сертификаты» | **Not present** on live twig (removed in operator polish) |

**SAFE UNKNOWN:** whether hidden `certificat_01` should return for multi-doc tenders.

### Form

| Item | Value |
|------|-------|
| Endpoint | `POST` `dialog=7` (existing dealers/lead handler) |
| Title | «Получить прайс-лист» |
| Fields | name, phone (`data-mask="phone"`), email, message (Комментарий), agree checkbox |
| Submit | «Отправить заявку» |
| Visual | Backdrop-blur card; decor logo behind form wrap |

**Preserved:** field IDs/names, privacy links, `zpm-form` classes — backend-safe.

### FAQ grid

8 service cards with `fad` icons — catalog gaps, full price list, custom sizes, lead times, dealers, documentation, project fit, nationwide delivery.

CSS: `.zpm-commercial-trust__services` — `grid-template-columns: repeat(4, 1fr)` desktop; `repeat(2, 1fr)` ≤1024px.

### Change rules

Before **any** edit to trust block, certificates strip, dealers form, or category CTA:

1. Read **§14** (this section)
2. Read latest stable checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** `blockcommercialtrust.twig`, `style.css`, `category.php` — do not trust 03C work copies or pass reports alone
4. Operator manual CSS/Twig on live **override** repo work copies
5. Clear Twig cache after twig deploy
6. Test at least one mapped category + fallback category PLP

**Evidence:** [SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md](../reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md) · [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](../reports/SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) · [live-capture 2026-06-21](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/)

---

## 15. Page Intro Block (`page-intro`)

Shared H1 strip rendered **above `<main>`** via header partial — not inside `category.twig`.

### Render chain

| Step | File | Role |
|------|------|------|
| 1 | Controller sets `Pageintro` | `$pageintro->title`, `$pageintro->description` |
| 2 | `Pageintro::render()` | Emits `<section class="page-intro">` HTML (incl. optional `.page-intro__description`) |
| 3 | `$this->document->setPageintro(...)` | Stores rendered HTML on document |
| 4 | `catalog/controller/common/header.php` | `$data['pageintro'] = $this->document->getPageintro()` |
| 5 | `catalog/view/theme/default/template/common/header.twig` | `{% if pageintro %}{{ pageintro }}{% endif %}` after breadcrumbs |

**Important:** `$data['description']` in `category.php` (from `oc_category_description`) is the **SEO/category body block below the grid** — **not** the same as `$pageintro->description`.

### Data sources by route

| Route / page | Controller | `$pageintro->description` source | Live (post M9.8.9-10) |
|--------------|------------|--------------------------------|------------------------|
| `/katalog` | `catalog/controller/product/katalog.php` | Hardcoded string | **Present** — «Для предприятий общественного питания…» |
| Category PLP (branch) | `catalog/controller/product/category.php` | Always `''` | **Absent** |
| Neutral hub `/katalog/nejtralnoe-oborudovanie` | `category.php` + `$is_hub` | Was hardcoded M9.5 hub copy; **removed M9.8.9-10** | **Absent** |
| PDP | `product.php` | **SAFE UNKNOWN** — no forensic in this pass | **Absent** on sampled PLPs |
| Wishlist / compare / account | respective controllers | Usually `''` | **Absent** when empty |

Hub intro text was **controller logic**, not CMS category description, not language file, not twig override per category.

### M9.8.9-10 change

Removed hub-only hardcoded string from `category.php`; all category routes now set `$pageintro->description = ''`. **`katalog.php` unchanged** — catalog root keeps its intro line.

**Evidence:** [SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md](../reports/SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md)

---

## 16. Catalog State Persistence

PLP query-state model on live TEST (post M9.8.9-09A / 09B / 09C). **Joint behaviour:** `filter` + `limit` + `sort` + `pagination` + `only_with_price` work together when combined via sidebar AJAX, limit menu, sort buttons, and pagination.

### State model

| Param | Role | Set by |
|-------|------|--------|
| `filters` | Semicolon-separated filter payload (`only_with_price=1`, `attr[51][]=…`, `price_from`/`price_to`, etc.) | Sidebar form → JS `updateBrowserUrl()` |
| `limit` | Products per page (15 / 25 / 50 / 100 on live) | Limit menu `<a href>` or preserved in URL |
| `sort` | Sort field (e.g. `p.price`) | Sort button `data-sort` → JS URL merge |
| `order` | Sort direction (`ASC` / `DESC`) | Sort button `data-sort` → JS URL merge |
| `page` | Pagination page index | Pagination links or `initPaginationAJAX` merge |

**Fetch model:** filter changes do **not** call a separate filter API — `updateProducts()` fetches the **full category page** at current `location.href` and swaps DOM fragments.

### `updateBrowserUrl(form)`

**File:** `assets/js/main.js`

- Reads `[data-filters-form]` fields into semicolon-separated `filters` string
- Merges into existing `URLSearchParams(window.location.search)` — **preserves** `limit`, `sort`, `order`, `page`, and other query keys
- Updates `filters` only (set or delete)
- Applies `history.replaceState` without full navigation
- Triggers debounced `updateProducts(root)`

**Since 09A:** replaced naive `pathname + "?filters=" + stateText` rebuild that dropped non-filter params.

### `updateProducts(root)`

**File:** `assets/js/main.js`

```
fetch(location.href) — full category page
  → parse HTML response
  → replace .category__grid innerHTML
  → replace .pagination outerHTML (or insert/remove)
  → replace .category__limit outerHTML + initCategoryLimitMenu()  [since 09C]
  → scrollToCategorySection()
  → initPaginationAJAX(root)
```

**Since 09C:** limit toolbar refresh closes the 09B gap — after filter AJAX, limit hrefs match server-rendered filtered URLs.

### `category__limit` refresh

| Layer | Role |
|-------|------|
| **PHP** | `category.php` builds `$data['limits'][]['href']` — appends `&filters=` when request carries `filters` (09A) |
| **Twig** | `category.twig` — `.category__limit` menu with `<a href="{{ l.href }}">` |
| **JS (09C)** | After AJAX, swap `.category__limit` from fetched HTML; call `initCategoryLimitMenu()` to re-bind dropdown toggle |

**09B discovery:** pagination was already refreshed after filter AJAX; limit menu was **not** — operator path filter→limit click used stale plain-page hrefs.

### Pagination refresh

| Layer | Role |
|-------|------|
| **PHP** | `category.php` pagination `$url` includes `filters` when present (09A) |
| **JS** | `updateProducts()` replaces `.pagination` from response; `initPaginationAJAX` merges `page` into current browser URL on click |

Post-filter AJAX, pagination links in fetched HTML include `filters` — consistent with full-page filtered load.

### Sort behaviour

Sort toolbar uses `<button data-sort="sort=…&order=…">` — **not** server-rendered hrefs.

JS click handler merges sort params into `window.location.href` (which already contains `filters` after sidebar toggle). Sort path was unaffected by 09A/09C limit bug.

### PHP URL generation (09A)

**File:** `catalog/controller/product/category.php`

In sort, limit, and pagination `$url` assembly blocks:

```php
if (isset($this->request->get['filters'])) {
    $url .= '&filters=' . $this->request->get['filters'];
}
```

Ensures full-page navigation links (limit menu, pagination) carry active filter state when request URL includes `filters`.

### Interaction matrix (registered behaviour)

| Scenario | Expected | Mechanism |
|----------|----------|-----------|
| Toggle filter at `?limit=50` | Both params in URL | `updateBrowserUrl()` merge (09A) |
| Filter AJAX → click limit 50 | Filter persists | Limit href refreshed from response (09C) |
| Set limit → toggle filter | Limit persists | `updateBrowserUrl()` merge (09A) |
| Filter + sort + page combo | All params coexist | Sort JS merge + PHP pagination URLs + 09C limit refresh |
| `only_with_price` + attribute + limit | Combined `filters` + `limit` | Full stack |

### Change rules

Before **any** edit to catalog URL state, limit menu, pagination AJAX, or filter sidebar submit chain:

1. Read **§16** (this section) and **§7 Filter Architecture**
2. Read **09A / 09B / 09C** pass reports
3. Live-capture `assets/js/main.js` and `catalog/controller/product/category.php`
4. QA **interaction paths** — not only direct URL loads

**Evidence:** [SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md](../reports/SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md) · [SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md](../reports/SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md) · [SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md](../reports/SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md)

**SAFE UNKNOWN:** M9.8.9-09C browser QA Q1–Q6 — automated probe PASS; operator interaction HITL **PENDING**. Mobile filter shell separate limit control — not probed in 09C.

---

## 17. About Page History

Corporate page `/about` — route `information/about`. **Current canonical state = restored pre-M9.13 version** on live TEST.

### 1. Original page (pre-M9.13)

| Item | Value |
|------|--------|
| **Route** | `information/about` |
| **Controller** | `catalog/controller/information/about.php` |
| **Twig** | `catalog/view/theme/default/template/information/about.twig` |
| **Structure** | Legacy layout — `about-page--main-wrap`, video hero (`about-page-video`), metrics, certificate Swiper, dealer form, geo block (`geo-web.png`) |
| **Hero image** | `assets/img/about-page-img.jpg` |
| **CSS** | Scoped rules in `assets/css/style.css` (no `zpm-about-*` namespace) |

This structure was live before M9.13 redesign (2026-06-23).

### 2. M9.13 redesign

| Item | Value |
|------|--------|
| **Status** | **IMPLEMENTED** · **QA PASSED** · **REJECTED BY OPERATOR** |
| **Scope** | 6-section compact concept — `zpm-about-hero`, company, advantages, certs, geo, CTA |
| **Files changed** | `about.twig`, `about.php`, `style.css` (`zpm-about-page*` block) |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md) |
| **Work copies** | `reports/m9.13-work/` |
| **Backups** | `backups/*.pre-m9.13-about-redesign.bak` |

Removed legacy blocks: video hero, metrics cards, cert slider, dealer section, advantage partials.

### 3. M9.13 polish

| Item | Value |
|------|--------|
| **Status** | **IMPLEMENTED** · **QA PASSED** · **REJECTED WITH REDESIGN** |
| **Scope** | Hero trust row, spacing, cert column sizing, hero + logistics image upgrades |
| **Files changed** | `about.twig`, `style.css`, `about-page-img.jpg`; **new** `about-logistics.jpg` |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md) |
| **Work copies** | `reports/m9.13-polish-work/` |
| **Backups** | `backups/*.pre-m9.13-about-polish-v1.bak` |

Structure unchanged from redesign — polish only.

### 4. Operator review

| Item | Value |
|------|--------|
| **Decision** | **REJECTED** — M9.13 redesign/polish not accepted for production |
| **Classification** | Operator visual evaluation — not a technical deploy failure |
| **Implication** | Redesign work copies remain **historical reference**; live must return to pre-redesign |

### 5. Restoration

| Item | Value |
|------|--------|
| **Status** | **RESTORED** · **QA PASSED** |
| **Type** | **Operator-approved restoration** — **not** rollback failure |
| **Date** | 2026-06-23 |
| **Script** | `reports/m9.13-restore-work/m913-about-restore-to-pre-redesign.py` |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) |

**Restored from:** `backups/*.pre-m9.13-about-redesign.bak` (+ `about-page-img.jpg` from polish backup — same pre-redesign bytes).

**Removed:** `assets/img/about-logistics.jpg` (polish-only asset).

**SHA verified** against redesign pre-deploy manifest — restored files match pre-M9.13 state.

### 6. Current canonical state

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/about |
| **Structure** | **Restored original** — pre-M9.13 legacy layout |
| **M9.13 namespaces** | **Absent** on live — no `zpm-about-*` |
| **Source of truth** | Live TEST restored version |
| **Authority** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |

### Change rules

Before **any** edit to About page or new About redesign:

1. Read **§17** (this section)
2. Read restoration, redesign, and polish reports (listed above)
3. **Live-capture** `about.twig`, `about.php`, `style.css` before deploy
4. Treat restored live version as canonical — do not assume M9.13 work copies reflect production intent
5. New redesign requires **operator charter** — M9.13 pass is closed as rejected/restored

**Evidence:** [SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md](../reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md) · [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)

**SAFE UNKNOWN:** Twig cache clear after restore returned empty listing — operator manual clear on Beget if stale render appears.

---

## 18. Delivery Page (M9.14)

Corporate page `/delivery` — route `information/delivery`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/delivery |
| **Route** | `information/delivery` |
| **SEO** | `oc_seo_url` keyword `delivery` → `information/delivery` |
| **Controller** | `catalog/controller/information/delivery.php` |
| **Twig** | `catalog/view/theme/default/template/information/delivery.twig` |
| **CSS namespace** | `zpm-delivery-page`, `zpm-delivery-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — scoped `[data-delivery-faq]` |
| **Copy** | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → shipment points → organization (summary row) → methods → 7-step timeline → packaging → Russia coverage → outcomes → TK table → FAQ (8) → Commercial Trust CTA + form (region required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Forbidden on page:** map · calculator · TK logos · Басовская · mid-page primary submit

### Change rules

1. Read [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) and **§18**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md) · `reports/m9.14-work/`

---

## 19. Payment Page (M9.15)

Corporate page `/payment-methods` — route `information/payment`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/payment-methods |
| **Route** | `information/payment` |
| **SEO** | `oc_seo_url` keyword `payment-methods` → `information/payment` |
| **Controller** | `catalog/controller/information/payment.php` |
| **Twig** | `catalog/view/theme/default/template/information/payment.twig` |
| **CSS namespace** | `zpm-payment-page`, `zpm-payment-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq]` |
| **Copy** | [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → 6-step payment timeline (step 6 = Подготовка к отгрузке + Delivery handoff) → payment methods + summary table → document proof cards (5) → legal entity strip → FAQ (8) → Commercial Trust CTA + form (company required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` + company field — **not** contact card grid or map
- **Delivery:** one-line / step-6 handoff only — **not** TK tables, shipment points, or logistics timeline
- **Forbidden on page:** bank widgets · payment logos · QR · Moscow warehouse detail · freight/logistics bodies

### Change rules

1. Read [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) and **§19**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Delivery, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](../reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md](../baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md) · `reports/m9.15-work/`

---

## 20. Warranty Page (M9.17)

Corporate page `/guarantee` — route `information/guarantee`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/guarantee |
| **Route** | `information/guarantee` |
| **SEO** | `oc_seo_url` keyword `guarantee` → `information/guarantee` (id 1048; prior `information_id=11`) |
| **Controller** | `catalog/controller/information/guarantee.php` |
| **Twig** | `catalog/view/theme/default/template/information/guarantee.twig` |
| **CSS namespace** | `zpm-warranty-page`, `zpm-warranty-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq], [data-warranty-faq]` |
| **Copy** | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → warranty principles + coverage (BLOCK 01) → document checklist (BLOCK 02) → 5-step claim timeline (BLOCK 03) → verification cases (BLOCK 04) → service outcomes (BLOCK 05) → FAQ (8) → Commercial Trust CTA + service form (equipment_model required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Delivery:** outbound/RMA pointers only — **not** TK tables or shipment points
- **Payment:** deal-docs pointer only — **not** methods matrix or bank detail
- **Forbidden on page:** term badge without OQ-W01 · ASC map · fear exclusion walls · warranty certificate hero · photo upload MVP

### Change rules

1. Read [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md) and **§20**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Delivery, Payment, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md) · `reports/m9.17-work/`

---

## 21. Dealers Page (M9.16)

Corporate page `/dealers` — route `information/dealers`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/dealers |
| **Route** | `information/dealers` |
| **SEO** | `oc_seo_url` keyword `dealers` → `information/dealers` (id 1049; prior `information_id=10`) |
| **Controller** | `catalog/controller/information/dealers.php` |
| **Twig** | `catalog/view/theme/default/template/information/dealers.twig` |
| **CSS namespace** | `zpm-dealers-page`, `zpm-dealers-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq], [data-warranty-faq], [data-dealers-faq]` |
| **Copy** | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` (page domain only) |

### Structure (target)

Pageintro (H1 + Lead) → optional trust strip → partner matrix (SC-13) → OEM proof (BLOCK 02) → partner outcomes → 5-step timeline → supply chain + cross-links → FAQ (8) → Commercial Trust CTA + qualification form (company + city required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap on corp page — **not** full PLP trust block; **do not** edit PLP `blockdealersform.twig` in M9.16 scope
- **Delivery / Payment / Warranty:** one-line summaries + links only — **not** embedded sibling bodies
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Forbidden on page:** form-as-hero · discount map · franchise aesthetics · territory map · partner logo wall · СНГ geography

### Governance (B3)

Standalone `/dealers` corp page = **primary qualification surface** per charter. PLP dealer form reconciliation = **separate future task** — operator blocker **B3** is governance-only for M9.16 implementation start.

### Change rules

1. Read [SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md) and **§21**
2. Live-capture remote files before deploy
3. Do not bleed scope into PLP dealer form unless operator opens dedicated B3 task

**Evidence:** [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md](../baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md) · `reports/m9.16-work/`

---

## 22. Custom Manufacturing Page (M9.18)

Corporate page `/custom-equipment` — route `information/custom_equipment`. **IMPLEMENTED** on live TEST (2026-06-28). Checkpoint **`SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`**.

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/custom-equipment |
| **Route** | `information/custom_equipment` |
| **SEO** | `oc_seo_url` keyword `custom-equipment` → `information/custom_equipment` (id 1042; prior `information_id=14`) |
| **Legacy CMS** | Information id **14** — orphaned, not deleted |
| **Controller** | `catalog/controller/information/custom_equipment.php` |
| **Twig** | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| **CSS namespace** | `zpm-custom-page`, `zpm-custom-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-custom-faq]` in selector list |
| **Copy** | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) |
| **Charter** | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md) |
| **Implementation** | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md) |
| **Checkpoint** | [SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md](../baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md) |

### Structure (target)

Pageintro (H1 + Lead) → when custom needed (BLOCK 01 + BLOCK 02) → scope + OEM proof (BLOCK 03 + BLOCK 04) → **8-step process timeline** (BLOCK 05 — dominant) → requirements + materials (BLOCK 06 + BLOCK 07) → project outcomes (BLOCK 08 — second emphasis) → FAQ (8) → Commercial Trust CTA + custom form (company, contact, phone, email, project_description required; **no upload MVP**).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Delivery / Payment / Warranty / Dealers:** one-line summaries + links only — **not** embedded sibling bodies
- **Catalog:** text links and scope bridge — **not** PLP grid or prices
- **Forbidden on page:** calculator/configurator · file upload MVP · price/lead badges · tender portal UX · fake case gallery · universal AISI table hero

### Program note

M9.18 is the **terminal** Corporate Pages Program implementation milestone. After stable checkpoint, corp implementation phase for M9.14–M9.18 (About restoration separate) is **complete on TEST** — pending operator gates B6/B8 for formal sign-off.

### Change rules

1. Read [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md) and **§22**
2. Live-capture remote files before deploy
3. Do not bleed scope into sibling corp pages or catalog templates

**Evidence:** [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [reports/m9.18-work/deploy-manifest.json](../reports/m9.18-work/deploy-manifest.json) · [qa/m9.18-custom-screenshots/](../qa/m9.18-custom-screenshots/)

---

## Document maintenance

| When | Action |
|------|--------|
| New stable checkpoint | Update §1 authority reference |
| New forensic pass | Add row to relevant § + evidence link |
| Live code change | Update affected §; note SHA in pass report |
| SAFE UNKNOWN resolved | Replace with evidence; remove UNKNOWN label |

---

*Documentation only — live TEST evidence in deploy manifest. Last updated: 2026-06-28 (§22 M9.18 Custom Manufacturing IMPLEMENTED — terminal corp page).*
