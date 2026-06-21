# REPORT — SITE-002 PRODUCT RESET BEFORE FRESH 1C IMPORT PLAN

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Environment:** https://zpm.new-site.space/  
**Plan date:** 2026-06-19  
**Mode:** PLAN ONLY — no DELETE, no SQL mutation, no deploy, no commit, no push  

**Evidence bundle (read-only probes):**  
`projects/ocpilot/sites/site-002/reports/product-reset-plan-work/`  
- `probe-results.json` — table counts, branch counts, image samples  
- `probe-supplement.json` — `SHOW TABLES`, SEO breakdown, manual vs 1C split  
- `probe-ancillary.json` — cart, wishlist, googleshopping counts  

**Prior context:** M9.8.9-06I (filter forensic), 06J (numeric attr hotfix), 06F (offers price-index hook), 06C (1C/cron chain)

---

## 1. Current problem

### Operator symptom

Filters on TEST still fail or behave inconsistently after the M9.8.9-06J numeric-attribute hotfix (`attr[51]` / `attr[47]` SQL branch). Operator hypothesis: **catalog data is mixed** — not a single clean 1C snapshot.

### Confirmed data-layer signals (live DB, read-only 2026-06-19)

| Signal | Value | Interpretation |
|--------|------:|----------------|
| Total products | **3134** | Large inactive bulk + active subset |
| Active products (`status=1`, `date_available <= NOW()`) | **609** | Storefront-visible SKU pool |
| Products with `xml_id` (1C link) | **3079** | Most rows tied to 1C |
| Active **without** `xml_id` | **55** | Likely manual / SQL / admin inserts |
| Inactive **with** `xml_id` | **2525** | Stale 1C catalog rows not cleaned |
| Distinct products in `oc_product_attribute` | **1106** | **2028 products have no attribute rows** |
| Active in subtree 301 (Столы) | **420** | All active in branch |
| `oc_product_price_index` rows (all groups) | **1977** | Partial / historical index |
| Distinct products indexed (group 2) | **659** | Index includes inactive SKUs; incomplete vs 609 active |
| Products with main image | **553** / 3134 | Many products image-empty |
| Cron `lastrun` vs XML mtime | 2026-06-02 vs 2026-06-08 (06C) | Possible import not run after last file upload |

### Code vs data

- **06J fixed** numeric-key SQL for attrs **47/51** when `filter_name` is empty (verified in 06J QA).
- Remaining filter/price issues may still come from **mixed attributes**, **partial price index**, **zero-price SKUs**, **branch mis-assignment**, and **inactive/xml_id drift** — not fully fixable by code-only patches on dirty data.

### Goal of reset

Controlled **product-only** wipe on TEST → fresh `import0_1.xml` + `offers0_1.xml` → single coherent catalog baseline. **Categories, attribute definitions, filter profiles, theme, settings stay.**

---

## 2. Product-owned tables

### 2.1 Core OpenCart product tables (DELETE all rows)

Discovered via live `SHOW TABLES` + row counts. Prefix `oc_`.

| Table | Rows (live) | Distinct `product_id` | Role |
|-------|------------:|----------------------:|------|
| `oc_product` | 3134 | 3134 | Master product row (**delete last**) |
| `oc_product_description` | 3134 | 3134 | Names, meta, descriptions |
| `oc_product_attribute` | 10175 | 1106 | Filter / PDP specs (**major gap: 2028 products missing attrs**) |
| `oc_product_to_category` | 3134 | 3134 | Category assignment |
| `oc_product_to_store` | 3134 | 3134 | Store visibility |
| `oc_product_image` | 6 | 5 | Gallery images |
| `oc_product_discount` | 1 | 1 | Quantity discounts |
| `oc_product_special` | 2 | 1 | Special prices |
| `oc_product_reward` | 0 | 0 | Reward points |
| `oc_product_filter` | 0 | 0 | OC filter module links |
| `oc_product_option` | 0 | 0 | Options |
| `oc_product_option_value` | 0 | 0 | Option values |
| `oc_product_related` | 0 | 0 | Related products (both directions) |
| `oc_product_to_download` | 0 | 0 | Download links |
| `oc_product_to_layout` | 57 | 57 | Per-product layout overrides |
| `oc_product_recurring` | 0 | 0 | Recurring profiles |
| `oc_review` | 0 | 0 | Product reviews |

### 2.2 ZPM / SITE-002 custom product table

| Table | Rows | Distinct `product_id` | Role |
|-------|-----:|----------------------:|------|
| `oc_product_price_index` | 1977 | 659 | **Custom** — PLP price filter, slider, `only_with_price` (not in core OC `deleteProduct()`) |

### 2.3 SEO URLs (partial delete)

| Table | Total rows | Product rows | Action |
|-------|----------:|-------------:|--------|
| `oc_seo_url` | 3381 | **3134** (`query LIKE 'product_id=%'`) | Delete **product rows only** |

SEO breakdown (non-product — **keep**):

| Kind | Count |
|------|------:|
| category | 189 |
| information | 11 |
| manufacturer | 1 |
| other | 46 |
| product | 3134 |

### 2.4 Extension / session tables with `product_id` (DELETE product refs)

| Table | Rows | Notes |
|-------|-----:|-------|
| `oc_coupon_product` | 0 | Safe to clear |
| `oc_customer_wishlist` | 27 (18 products) | Orphan refs after reset — **delete all** |
| `oc_cart` | 16 | Active carts — **delete all** (TEST) |
| `oc_googleshopping_product` | 1 | Google Shopping feed mapping — **delete all** |
| `oc_googleshopping_product_status` | 0 | Delete all (empty) |
| `oc_googleshopping_product_target` | SAFE UNKNOWN | Include in plan if rows exist at execution time |

### 2.5 NOT product-owned — no dedicated product doc table

**Product “documents” on PDP** come from **category-level** tables via join:

- `oc_category_docs` (4 rows) — **DO NOT DELETE**
- `oc_category_doc_description` — **DO NOT DELETE**

Physical files: `Product_DOCs/` on host — category certificates; **not** tied to `product_id`. Keep unless operator confirms product-only files inside.

### 2.6 Migration / backup artifact (leave alone)

| Table | Rows | Notes |
|-------|-----:|-------|
| `oc_backup_move_polka_to_83` | 0 | One-off migration backup — **DO NOT DELETE** |

---

## 3. Tables not to touch

### Catalog structure & filters (keep)

- `oc_category`, `oc_category_description`, `oc_category_path`, `oc_category_filter`
- `oc_category_to_store`, `oc_category_to_layout`
- `oc_attribute`, `oc_attribute_description`, `oc_attribute_group`, `oc_attribute_group_description`
- `oc_filter`, `oc_filter_description`, `oc_filter_group`, `oc_filter_group_description`
- M9 filter profile PHP (`system/library/zpm/filter_profiles/*`) — filesystem, not DB

### Documents & certificates (keep)

- `oc_category_docs`, `oc_category_doc_description`
- `Product_DOCs/` files (category-level)

### Site / theme / config (keep)

- `oc_setting`, `oc_store`, `oc_layout*`, `oc_theme`, `oc_module`, `oc_banner*`
- All template/theme files on FTP
- `cron` table rows (only toggle `active` during import)

### Customer & order history (keep — explicit charter)

| Table | Rows | Policy |
|-------|-----:|--------|
| `oc_order` | SAFE UNKNOWN | **Keep** |
| `oc_order_product` | 27 (9 distinct `product_id`) | **Keep** — historical orders; will reference deleted product IDs (orphan) |
| `oc_order_option` | 0 | Keep |
| `oc_order_*` (other) | — | Keep |
| `oc_customer*` (except wishlist) | — | Keep |

**Note:** After product reset, old order lines will point to non-existent `product_id`. Acceptable for TEST if operator agrees; restore from Beget backup if order integrity required.

### Manufacturers, information, blog (keep)

- `oc_manufacturer*`, `oc_information*`, `oc_blog_*`

---

## 4. Current counts

**Snapshot UTC:** 2026-06-19T07:55:33Z (`probe-results.json`)

### Products

| Metric | Count |
|--------|------:|
| Total products | 3134 |
| Active products | 609 |
| With `xml_id` | 3079 |
| Active without `xml_id` (manual) | 55 |
| Inactive with `xml_id` | 2525 |
| Product SEO URLs | 3134 |
| Main image set | 553 |
| Gallery rows (`oc_product_image`) | 6 |

### Branch counts (subtree via `oc_category_path`, store 0)

| category_id | Branch | Total SKUs | Active SKUs |
|------------:|--------|----------:|------------:|
| 79 | Нейтральное оборудование (root) | 3134 | 609 |
| 80 | Моечные ванны | 2677 | 152 |
| 207 | Зонты вытяжные | 23 | 23 |
| 301 | Столы | 420 | 420 |
| 322 | Подтоварники и подставки | 11 | 11 |
| 326 | Тележки сервировочные | 3 | 3 |

### Price index

| Metric | Count |
|--------|------:|
| Total index rows (all customer groups) | 1977 |
| Distinct products in index | 659 |
| Distinct products in index (group 2) | 659 |
| Active products (609) not guaranteed indexed | gap likely |

### Attribute coverage anomaly

| Metric | Count |
|--------|------:|
| `oc_product_attribute` rows | 10175 |
| Products with ≥1 attribute row | 1106 |
| Products with **zero** attribute rows | **2028** |

This alone can cause filter PLPs to show options but return 0 for many SKUs after partial manual/1C history.

---

## 5. Image/file impact

### Path pattern (live DB)

| Location | Count | Pattern |
|----------|------:|---------|
| Main image `oc_product.image` | 552 | `catalog/1c_import/{1c-uuid-hash}.jpg` (typical) |
| Main image (other) | 1 | `catalog/b151225.jpg` — verify before any file delete |
| Gallery `oc_product_image` | 6 | `catalog/1c_import/...` |

**Filesystem root (OpenCart):** `{site_root}/image/`  
**Product image folder:** `{site_root}/image/catalog/1c_import/`

Category/menu/banner images typically live under other `image/catalog/...` paths — **not referenced** in product rows above.

### 1C import behaviour (from live code / 06C–06E audits)

| Stage | File | Image behaviour |
|-------|------|-----------------|
| Catalog import | `import0_1.xml` → `import_1C.php` / `import_1C_process.php` | Updates `oc_product.image`, attributes, categories, dimensions |
| Offers import | `offers0_1.xml` → `import_1C_offers.php` | **Price/qty only** — no image changes |

**Conclusion:** Fresh catalog import **re-downloads / re-assigns** product images into `catalog/1c_import/`. Offers pass does not touch files.

### Physical delete recommendation (plan only — do not execute in this task)

| Action | When | Risk |
|--------|------|------|
| **Archive** `image/catalog/1c_import/` to Beget backup / zip | After DB product wipe, **before** catalog import | Low if only product images use this folder |
| **Do not delete** other `image/catalog/*` | Always | Category thumbs, favicon, banners |
| **Do not delete** `Product_DOCs/` | Always | Category certificates (4 DB rows) |
| **Optional keep** old `1c_import` until import succeeds | Safer rollback | Disk only; stale files harmless |

**Shared category image risk:** Low for `1c_import/` (552/553 product paths). Confirm `catalog/b151225.jpg` is not used as category image before any broad `catalog/` delete.

---

## 6. Proposed SQL delete order

**NOT EXECUTED.** Operator runs manually after Beget DB backup, on TEST only.

**Prefer `DELETE` over `TRUNCATE`:** easier to abort inside transaction; no implicit FK surprises; full restore via Beget backup remains primary rollback.

**Recommended:** wrap in transaction; `COMMIT` only after row-count verification.

```sql
-- ============================================================
-- SITE-002 TEST — PRODUCT-ONLY RESET (PLAN — DO NOT RUN HERE)
-- Database: polygonws_zpm
-- Pre-requisite: Beget full DB backup confirmed
-- ============================================================

START TRANSACTION;

-- Phase A: satellite / extension product refs
DELETE FROM oc_coupon_product;
DELETE FROM oc_customer_wishlist;
DELETE FROM oc_cart;
DELETE FROM oc_googleshopping_product;
DELETE FROM oc_googleshopping_product_status;
DELETE FROM oc_googleshopping_product_target;  -- if table exists and has rows

-- Phase B: custom price index (ZPM — not in core deleteProduct)
DELETE FROM oc_product_price_index;

-- Phase C: product child tables (OpenCart order)
DELETE FROM oc_product_attribute;
DELETE FROM oc_product_description;
DELETE FROM oc_product_discount;
DELETE FROM oc_product_filter;
DELETE FROM oc_product_image;
DELETE FROM oc_product_option_value;
DELETE FROM oc_product_option;
DELETE FROM oc_product_related;
DELETE FROM oc_product_reward;
DELETE FROM oc_product_special;
DELETE FROM oc_product_to_category;
DELETE FROM oc_product_to_download;
DELETE FROM oc_product_to_layout;
DELETE FROM oc_product_to_store;
DELETE FROM oc_product_recurring;
DELETE FROM oc_review;

-- Phase D: product SEO only (preserve category/information/manufacturer URLs)
DELETE FROM oc_seo_url WHERE query LIKE 'product_id=%';

-- Phase E: master product table LAST
DELETE FROM oc_product;

-- Phase F: verification (must be zero before COMMIT)
-- SELECT COUNT(*) FROM oc_product;                    -- expect 0
-- SELECT COUNT(*) FROM oc_product_attribute;        -- expect 0
-- SELECT COUNT(*) FROM oc_product_price_index;        -- expect 0
-- SELECT COUNT(*) FROM oc_seo_url WHERE query LIKE 'product_id=%';  -- expect 0
-- SELECT COUNT(*) FROM oc_category;                   -- unchanged
-- SELECT COUNT(*) FROM oc_attribute;                  -- unchanged

COMMIT;
```

### Explicitly excluded from DELETE

```sql
-- DO NOT RUN:
-- DELETE FROM oc_order_product;
-- DELETE FROM oc_category*;
-- DELETE FROM oc_attribute*;
-- DELETE FROM oc_category_docs;
-- DELETE FROM oc_filter*;
-- DELETE FROM cron;
```

### Post-delete cache (operator, after COMMIT)

- Clear OpenCart cache: `system/storage/cache/*` (especially `cache.category.attributes.*`, template cache)
- No code deploy required for reset itself

### Optional: AUTO_INCREMENT reset

Only if operator wants `product_id` to restart from 1 after clean import:

```sql
-- OPTIONAL — only after empty verification; breaks order_product orphan mapping clarity
ALTER TABLE oc_product AUTO_INCREMENT = 1;
```

**Recommendation:** skip AUTO_INCREMENT reset on TEST if historical `oc_order_product` rows must remain interpretable.

---

## 7. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Irreversible product loss | **High** | Beget DB backup before any DELETE; TEST only |
| Orphan `product_id` in `oc_order_product` (27 rows) | Medium | Expected; document; do not delete order tables |
| Orphan wishlist/cart | Low | Deleted in plan (TEST carts/wishlists) |
| Category tree damaged | **High if mis-scoped** | Delete only tables listed in §6; verify counts |
| Attribute/filter defs lost | **High if mis-scoped** | Do not touch `oc_attribute*` / `oc_filter*` |
| SEO 404 for old product URLs | Medium | Expected until re-import recreates `oc_seo_url` |
| Stale image files on disk | Low | Optional archive of `image/catalog/1c_import/` |
| Import overwrites wrong XML | Medium | Upload to `1c_incoming/webdata/`; verify filenames `import0_1.xml`, `offers0_1.xml` |
| Cron runs unintended task | Medium | Only one `active=1` row at a time; both currently inactive (06C) |
| Partial import / timeout | Medium | `max_execution_time=300` on cron; monitor HTTP output |
| Price index incomplete after import | Medium | 06F hook in live `import_1C_offers.php` should refresh index post-offers — verify after import |
| `filter_name` empty on attrs 47/51 | Low | 06J code handles numeric keys; fresh import should still populate attrs consistently |

---

## 8. Rollback

### Primary rollback

**Beget full database restore** to snapshot taken immediately before DELETE phase.

Includes all product rows, SEO URLs, price index, attributes, and order integrity.

### Secondary rollback (code-only issues)

If import succeeds but code regressions appear — restore PHP from authority baseline:

`SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` / stable baseline manifests under  
`projects/ocpilot/sites/site-002/backups/stable-baselines/`

### File rollback

- Restore `image/catalog/1c_import/` from archive if physical delete was performed
- Re-upload previous `import0_1.xml` / `offers0_1.xml` from backup if needed

---

## 9. Operator import sequence

**Preconditions:** Product DELETE committed; fresh 1C XML uploaded to host; Beget backup confirmed.

### Step 0 — Upload files

Upload to server path (live code uses):

```
{site_root}/1c_incoming/webdata/import0_1.xml
{site_root}/1c_incoming/webdata/offers0_1.xml
```

Legacy path `1c_exchange/` exists but is **commented out** in import handlers — do not rely on it.

### Step 1 — Catalog import (`import0_1.xml`)

```sql
UPDATE cron SET active = 0;                          -- safety: all off
UPDATE cron SET active = 1 WHERE command = '1c';     -- row id=1, import0_*.xml
```

Run cron (browser or curl):

```
https://zpm.new-site.space/index.php?route=common/cronjob
```

Wait for success output (product create/update messages). Then:

```sql
UPDATE cron SET active = 0 WHERE command = '1c';
```

### Step 2 — Offers import (`offers0_1.xml`)

```sql
UPDATE cron SET active = 1 WHERE command = '1c_offers';   -- row id=2, offers0_*.xml
```

Run same cron URL again:

```
https://zpm.new-site.space/index.php?route=common/cronjob
```

Wait for price/qty update messages. Post-06F live code should call `refreshPriceIndex()` for updated IDs.

Then:

```sql
UPDATE cron SET active = 0 WHERE command = '1c_offers';
```

### Step 3 — Post-import verification (quick SQL)

| Check | Expected |
|-------|----------|
| `SELECT COUNT(*) FROM oc_product` | > 0; matches 1C assortment |
| `SELECT COUNT(*) FROM oc_product WHERE xml_id <> ''` | ≈ total (1C-linked) |
| `SELECT COUNT(*) FROM oc_product_attribute` | >> 0; coverage ≈ active SKUs |
| `SELECT COUNT(DISTINCT product_id) FROM oc_product_price_index WHERE customer_group_id=2` | ≈ active priced SKUs after offers |
| `SELECT COUNT(*) FROM oc_seo_url WHERE query LIKE 'product_id=%'` | ≈ product count |

### Cron reference (from M9.8.9-06C live audit)

| id | name | command | active (normal) |
|----|------|---------|-----------------|
| 1 | Импорт 1C | `1c` | 0 except during step 1 |
| 2 | Импорт 1C - цены и остатки | `1c_offers` | 0 except during step 2 |

**SAFE UNKNOWN:** exact `lastrun` at execution time — re-query before import.

---

## 10. Post-import QA checklist

### A. Counts & index

| # | Check | Method | Pass criteria |
|---|-------|--------|---------------|
| A1 | Total active products | SQL / admin | Matches expected 1C assortment |
| A2 | Products with attributes | SQL | No large gap (target: active ≈ attr-covered) |
| A3 | Price index coverage (group 2) | SQL | Distinct indexed ≈ active SKUs with offers pass |
| A4 | Product SEO URLs | SQL | One URL per active product |

### B. PLP baselines (card count > 0)

| # | Branch | URL | Baseline expectation |
|---|--------|-----|---------------------|
| B1 | Столы | `/katalog/nejtralnoe-oborudovanie/stoly/` | Cards > 0 |
| B2 | Подтоварники | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | Cards > 0 |
| B3 | Моечные ванны | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | Cards > 0 |
| B4 | Зонты | `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/` | Cards > 0 |
| B5 | Тележки | `/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/` | Cards > 0 |

### C. Filter probes (must return > 0 when filter applicable)

| # | Branch | Filter param | Example |
|---|--------|--------------|---------|
| C1 | Столы | `attr[51][]` | `Без полки` |
| C2 | Столы | `attr[table-top-material][]` | slug value from sidebar |
| C3 | Подтоварники | `attr[51][]` | dimension value from sidebar |
| C4 | Подтоварники | `attr[max-load][]` | `200` |
| C5 | Моечные ванны | `attr[shell-size][]` | e.g. `1100х500х400` |
| C6 | Зонты | `attr[construction][]` | e.g. `угловая, купольная` |
| C7 | Столы | `only_with_price=1` | ≥1 if priced SKUs exist |
| C8 | Столы | price range | min–max from slider, not collapsed single point |

URL format: `?filters={param}` (semicolon-separated inside `filters`).

### D. PDP samples

| # | Check | Pass criteria |
|---|-------|---------------|
| D1 | Price display | Numeric price **or** «По запросу» for zero-price SKU |
| D2 | Main image | Present for sampled SKU |
| D3 | SEO URL | Clean URL resolves 200 |
| D4 | Specs block | Attributes visible |
| D5 | Reference SKU | e.g. СПКБ-18/7-ВЛ5 or equivalent from new import — 200, no PHP errors |

### E. Regression guards

| # | Check | Pass criteria |
|---|-------|---------------|
| E1 | Category pages | Hub `/katalog/nejtralnoe-oborudovanie/` → 200 |
| E2 | Category SEO URLs | Unchanged (189 category SEO rows) |
| E3 | Certificates block | Category docs still on PDP if configured |
| E4 | PHP errors | None on PLP/PDP/cron output |

---

## Execution checklist (operator summary)

1. Confirm Beget **full DB backup**
2. Optional: archive `image/catalog/1c_import/`
3. Execute §6 DELETE script in transaction; verify zero product counts
4. Clear OC cache
5. Upload fresh `import0_1.xml` + `offers0_1.xml`
6. Run import sequence §9 (catalog → offers)
7. Run QA §10
8. If fail → Beget DB restore (§8)

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Exact product count in incoming fresh 1C XML (not parsed in this plan pass) |
| **UNKNOWN** | Whether operator still sees filter failures on attrs **other than** 47/51 after 06J |
| **UNKNOWN** | `oc_googleshopping_product_target` row count at execution time |
| **UNKNOWN** | Whether physical delete of `1c_import/` is desired vs leave stale files |
| **SECURITY** | DB credentials used only in local read-only probe scripts; not stored in this report |

---

**Plan status:** COMPLETE  
**Mutations performed in this task:** NONE  
**Git:** no commit, no push
