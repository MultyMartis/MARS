# SITE-002 TECHNICAL KNOWLEDGE MAP

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`  
**Created:** 2026-06-19  
**Purpose:** Persistent technical reference for operators and agents working on SITE-002.

**Evidence cutoff:** M9.8.9 filter recovery wave (06C–06M), product reset, fresh 1C import.

---

## 1. Authority Rules

### Source of truth (priority order)

| # | Source | Rule |
|---|--------|------|
| 1 | **Live TEST** (`zpm.new-site.space`) | Authoritative runtime state |
| 2 | **Beget full backup** | Operator-controlled disaster recovery |
| 3 | **Manual UI / CSS / Twig / JS refinements** | **CANONICAL** — operator edits on live override older deploy snapshots |
| 4 | **This Knowledge Map** | Architecture and discovered behaviour — update when new forensic evidence appears |
| 5 | **Latest Stable Checkpoint** | [SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) |

### Current stable state

- **Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`
- **Supersedes:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`
- **Post-recovery:** clean product reset → fresh 1C import → price index recovery → filter hotfixes (06H, 06J, 06M)

### Manual UI refinements are canonical

Operator manual CSS, Twig, JS, and UX edits on live TEST are the **visual and behavioural authority**. Repo work copies (`*-work/`), prior STABLE folders, and `.pre-*.bak` from earlier passes are **historical** unless refreshed by live FTP capture.

See also **§10 Operator Manual JS Refinements** (post M9.8.9-04A operator polish).

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

## 7. Overlay System

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

## 8. PDP Architecture

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

## 9. Catalog Architecture

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

## 10. Operator Manual JS Refinements

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

## 11. Operational Rules

### PRE-TASK RULE (mandatory)

Before **any** SITE-002 task:

1. **Read** this Technical Knowledge Map
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md)
3. **Verify Authority State** matches checkpoint name
4. **Check Active Roadmap Stage** — [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)
5. **Only then** perform audit or changes

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

## Document maintenance

| When | Action |
|------|--------|
| New stable checkpoint | Update §1 authority reference |
| New forensic pass | Add row to relevant § + evidence link |
| Live code change | Update affected §; note SHA in pass report |
| SAFE UNKNOWN resolved | Replace with evidence; remove UNKNOWN label |

---

*Documentation only — no runtime claimed. Last updated: 2026-06-19 (M9.8.9-04B operator manual JS refinements).*
