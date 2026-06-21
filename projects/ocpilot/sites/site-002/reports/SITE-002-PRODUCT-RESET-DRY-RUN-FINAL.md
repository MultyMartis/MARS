# REPORT — SITE-002 PRODUCT RESET DRY RUN FINAL

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Environment:** https://zpm.new-site.space/  
**Database:** `polygonws_zpm` (Beget phpMyAdmin, read-only probe)  
**Dry-run date:** 2026-06-19  
**Probe UTC:** 2026-06-19T08:08:41Z (+ final supplement 2026-06-19T08:10Z)  

**Mode:** DRY RUN ONLY — **no DELETE, no UPDATE, no deploy, no commit, no push**

**Operator note:** свежая выгрузка 1С загружена на сервер; **импорт ещё не выполнялся** — счётчики БД отражают текущий каталог до reset.

**Evidence bundle (read-only):**  
`projects/ocpilot/sites/site-002/reports/product-reset-plan-work/`  
- `probe-results.json`  
- `probe-supplement.json`  
- `probe-ancillary.json`  
- `probe-final.json`  

---

## 1. Tables To Be Cleared

По каждой таблице: текущее количество строк → **будет удалено** при execution (если оператор подтвердит).

### 1.1 Core OpenCart — product tables (DELETE ALL rows)

| Table | Rows now | Will delete | Notes |
|-------|--------:|------------:|-------|
| `oc_product` | **3134** | **3134** | Master table — **удалять последней** |
| `oc_product_description` | 3134 | 3134 | Названия, meta, описания |
| `oc_product_attribute` | 10175 | 10175 | Атрибуты / фильтры PDP (1106 distinct `product_id`) |
| `oc_product_to_category` | 3134 | 3134 | Привязка к категориям |
| `oc_product_to_store` | 3134 | 3134 | Видимость в store |
| `oc_product_image` | 6 | 6 | Галерея (5 distinct `product_id`) |
| `oc_product_discount` | 1 | 1 | Скидки по количеству |
| `oc_product_special` | 2 | 2 | Special price |
| `oc_product_reward` | 0 | 0 | Баллы |
| `oc_product_filter` | 0 | 0 | OC filter module links |
| `oc_product_option` | 0 | 0 | Опции |
| `oc_product_option_value` | 0 | 0 | Значения опций |
| `oc_product_related` | 0 | 0 | Связанные товары |
| `oc_product_to_download` | 0 | 0 | *(alias в задаче: `oc_product_download`)* |
| `oc_product_to_layout` | 57 | 57 | *(alias в задаче: `oc_product_layout`)* |
| `oc_product_recurring` | 0 | 0 | Recurring profiles |
| `oc_review` | 0 | 0 | Отзывы |

### 1.2 ZPM custom — product table (DELETE ALL rows)

| Table | Rows now | Will delete | Notes |
|-------|--------:|------------:|-------|
| `oc_product_price_index` | **1977** | **1977** | Custom PLP price filter / slider / `only_with_price` (659 distinct `product_id`; **не входит** в core `deleteProduct()`) |

### 1.3 SEO URLs — partial delete

| Table | Rows now | Will delete | Will keep |
|-------|--------:|------------:|----------:|
| `oc_seo_url` | 3381 | **3134** (`query LIKE 'product_id=%'`) | **247** (category / information / manufacturer / other) |

SEO breakdown (non-product — **не удаляются**):

| Kind | Count |
|------|------:|
| category | 189 |
| information | 11 |
| manufacturer | 1 |
| other | 46 |
| **product** | **3134** ← delete |

### 1.4 Extension / session tables (DELETE ALL rows)

| Table | Rows now | Will delete | Notes |
|-------|--------:|------------:|-------|
| `oc_coupon_product` | 0 | 0 | Купоны ↔ товары |
| `oc_customer_wishlist` | 27 | 27 | *(alias: `wishlist`)*; 18 distinct `product_id` |
| `oc_cart` | 16 | 16 | *(alias: `cart`)*; активные корзины TEST |
| `oc_googleshopping_product` | 1 | 1 | *(alias: `googleshopping`)* |
| `oc_googleshopping_product_status` | 0 | 0 | |
| `oc_googleshopping_product_target` | 0 | 0 | Подтверждено final probe |

### 1.5 Summary — rows to be deleted

| Phase | Tables | Rows deleted |
|-------|--------|-------------:|
| A — satellites | coupon_product, wishlist, cart, googleshopping* | **44** |
| B — price index | `oc_product_price_index` | **1977** |
| C — product children | 16 OC product child tables | **19 643** |
| D — SEO (partial) | `oc_seo_url` product rows | **3134** |
| E — master | `oc_product` | **3134** |
| **Total approximate** | | **~27 932 rows** |

---

## 2. Tables Not Touched

Подтверждение: **не будут затронуты** DELETE-скриптом product reset.

### 2.1 Category tree & structure

| Table / area | Rows now | Action |
|--------------|--------:|--------|
| `oc_category` | 190 | **NOT touched** |
| `oc_category_description` | 190 | **NOT touched** |
| `oc_category_path` | 522 | **NOT touched** |
| `oc_category_filter` | 0 | **NOT touched** |
| `oc_category_to_store` | — | **NOT touched** |
| `oc_category_to_layout` | — | **NOT touched** |
| Category SEO URLs (`oc_seo_url` category) | 189 | **NOT touched** |
| Category images (filesystem) | — | **NOT touched** |

### 2.2 Attribute & filter definitions

| Table / area | Rows now | Action |
|--------------|--------:|--------|
| `oc_attribute` | 59 | **NOT touched** |
| `oc_attribute_description` | 59 | **NOT touched** |
| `oc_attribute_group` | 6 | **NOT touched** |
| `oc_attribute_group_description` | 6 | **NOT touched** |
| `oc_filter` / `oc_filter_group` / descriptions | 0 each | **NOT touched** |
| Filter profiles PHP (`system/library/zpm/filter_profiles/*`) | filesystem | **NOT touched** |

### 2.3 Category documents

| Table / area | Rows now | Action |
|--------------|--------:|--------|
| `oc_category_docs` | 4 | **NOT touched** |
| `oc_category_doc_description` | 4 | **NOT touched** |
| `Product_DOCs/` (host filesystem) | — | **NOT touched** |

### 2.4 Site config, theme, code

| Table / area | Rows now | Action |
|--------------|--------:|--------|
| `oc_setting` | 201 | **NOT touched** |
| `oc_theme` | 0 | **NOT touched** |
| `oc_layout*`, `oc_module`, `oc_banner*` | — | **NOT touched** |
| Twig templates | filesystem | **NOT touched** |
| CSS / JS | filesystem | **NOT touched** |

### 2.5 Cron & 1C exchange

| Table / area | Rows now | Action |
|--------------|--------:|--------|
| `cron` | **2 rows** | **NOT deleted** — только `UPDATE active` при импорте (после reset) |
| `1c_exchange/` (legacy path) | filesystem | **NOT touched** |
| `1c_incoming/webdata/` + uploaded XML | filesystem | **NOT touched** — свежие `import0_1.xml` / `offers0_1.xml` остаются для post-reset import |

### 2.6 Orders & customers (explicit keep)

| Table | Rows now | Action |
|-------|--------:|--------|
| `oc_order` | 16 | **NOT touched** |
| `oc_order_product` | 27 (9 distinct `product_id`) | **NOT touched** — станут orphan refs после reset |
| `oc_order_option` | 0 | **NOT touched** |
| `oc_customer*` (кроме wishlist) | — | **NOT touched** |

### 2.7 Other preserved

| Table | Rows now | Action |
|-------|--------:|--------|
| `oc_manufacturer*` | — | **NOT touched** |
| `oc_information*` | — | **NOT touched** |
| `oc_blog_*` | — | **NOT touched** |
| `oc_backup_move_polka_to_83` | 0 | **NOT touched** (migration artifact) |

---

## 3. Product Counts

**Snapshot:** live DB read-only, 2026-06-19T08:08:41Z

### 3.1 Catalog totals

| Metric | Count |
|--------|------:|
| Total products (`oc_product`) | **3134** |
| Active (`status=1`, `date_available <= NOW()`) | **609** |
| With `xml_id` (1C link) | **3079** |
| Active **without** `xml_id` (manual) | **55** |
| Inactive **with** `xml_id` | **2525** |
| Products with **zero** attribute rows | **2028** |
| Products with ≥1 attribute row | **1106** |
| Product SEO URLs | **3134** |

### 3.2 Branch counts (subtree via `oc_category_path`, store 0)

| category_id | Branch | Total SKUs | Active SKUs |
|------------:|--------|----------:|------------:|
| 79 | Нейтральное оборудование | 3134 | 609 |
| 80 | Моечные ванны | 2677 | 152 |
| 207 | Зонты вытяжные | 23 | 23 |
| 301 | Столы | 420 | 420 |
| 322 | Подтоварники и подставки | 11 | 11 |
| 326 | Тележки сервировочные | 3 | 3 |

### 3.3 Price index

| Metric | Count |
|--------|------:|
| `oc_product_price_index` rows (all groups) | **1977** |
| Distinct products in index | **659** |
| Distinct products in index (customer_group_id=2) | **659** |
| Active products (609) fully indexed | **gap likely** |

### 3.4 Post-reset expectation

После DELETE + fresh 1C import (catalog → offers) ожидается **новый** согласованный каталог из загруженного XML. Точное количество SKU в incoming XML — **SAFE UNKNOWN** (не парсилось в этом dry run).

---

## 4. Image Impact

### 4.1 DB references (product images)

| Source | Row count | Distinct paths | Path pattern |
|--------|----------:|---------------:|--------------|
| `oc_product.image` (main) | 553 products | **553** | `catalog/1c_import/*` — **552**; `catalog/b151225.jpg` — **1** |
| `oc_product_image` (gallery) | 6 rows | **6** | `catalog/1c_import/*` — all 6 |
| **Union distinct paths** (main ∪ gallery) | — | **559** | Overlap possible between main and gallery |

### 4.2 Filesystem locations

| Location | Role |
|----------|------|
| `{site_root}/image/catalog/1c_import/` | Primary product image folder (1C import) |
| `{site_root}/image/catalog/b151225.jpg` | Single non-1c_import main image (verify not used as category image) |
| `{site_root}/image/catalog/*` (other) | Category thumbs, banners, favicon — **NOT referenced** in product rows |
| `{site_root}/Product_DOCs/` | Category certificates — **NOT product-owned** |

**OpenCart image root:** `{site_root}/image/`  
**Site root (TEST):** Beget host for `zpm.new-site.space`

### 4.3 Physical file deletion policy (default)

| Action | Default at execution |
|--------|---------------------|
| Delete DB image references | **YES** (via product table DELETE) |
| Delete physical files in `image/catalog/1c_import/` | **NO** — без отдельного подтверждения оператора |
| Delete other `image/catalog/*` | **NO** |
| Delete `Product_DOCs/` | **NO** |

**Rationale:** stale files on disk harmless; fresh catalog import re-downloads into `1c_import/`. Optional archive before import — см. §7 Rollback.

**SAFE UNKNOWN:** exact count of `.jpg`/`.png` files on disk in `image/catalog/1c_import/` (may exceed 559 due to orphan files from past imports). DB probe counts paths only.

---

## 5. SQL Execution Order

**NOT EXECUTED in this task.** Operator runs manually after Beget full DB backup.

**Prefer `DELETE` over `TRUNCATE`:** abort inside transaction; Beget backup = primary rollback.

```sql
-- ============================================================
-- SITE-002 TEST — PRODUCT-ONLY RESET
-- Database: polygonws_zpm
-- Pre-requisite: Beget full DB backup confirmed by operator
-- DRY RUN COMPLETE — execute only after operator approval
-- ============================================================

START TRANSACTION;

-- Phase A: satellite / extension product refs
DELETE FROM oc_coupon_product;              -- 0 rows
DELETE FROM oc_customer_wishlist;           -- 27 rows
DELETE FROM oc_cart;                        -- 16 rows
DELETE FROM oc_googleshopping_product;      -- 1 row
DELETE FROM oc_googleshopping_product_status; -- 0 rows
DELETE FROM oc_googleshopping_product_target; -- 0 rows

-- Phase B: custom price index (ZPM)
DELETE FROM oc_product_price_index;         -- 1977 rows

-- Phase C: product child tables
DELETE FROM oc_product_attribute;           -- 10175 rows
DELETE FROM oc_product_description;         -- 3134 rows
DELETE FROM oc_product_discount;            -- 1 row
DELETE FROM oc_product_filter;              -- 0 rows
DELETE FROM oc_product_image;               -- 6 rows
DELETE FROM oc_product_option_value;        -- 0 rows
DELETE FROM oc_product_option;              -- 0 rows
DELETE FROM oc_product_related;             -- 0 rows
DELETE FROM oc_product_reward;              -- 0 rows
DELETE FROM oc_product_special;             -- 2 rows
DELETE FROM oc_product_to_category;         -- 3134 rows
DELETE FROM oc_product_to_download;         -- 0 rows
DELETE FROM oc_product_to_layout;           -- 57 rows
DELETE FROM oc_product_to_store;            -- 3134 rows
DELETE FROM oc_product_recurring;           -- 0 rows
DELETE FROM oc_review;                      -- 0 rows

-- Phase D: product SEO only
DELETE FROM oc_seo_url WHERE query LIKE 'product_id=%';  -- 3134 rows

-- Phase E: master LAST
DELETE FROM oc_product;                     -- 3134 rows

-- Phase F: verification (must pass before COMMIT)
-- SELECT COUNT(*) FROM oc_product;                                         -- expect 0
-- SELECT COUNT(*) FROM oc_product_attribute;                               -- expect 0
-- SELECT COUNT(*) FROM oc_product_price_index;                             -- expect 0
-- SELECT COUNT(*) FROM oc_seo_url WHERE query LIKE 'product_id=%';       -- expect 0
-- SELECT COUNT(*) FROM oc_seo_url WHERE query NOT LIKE 'product_id=%';   -- expect 247
-- SELECT COUNT(*) FROM oc_category;                                        -- expect 190 (unchanged)
-- SELECT COUNT(*) FROM oc_attribute;                                       -- expect 59 (unchanged)
-- SELECT COUNT(*) FROM oc_category_docs;                                   -- expect 4 (unchanged)
-- SELECT COUNT(*) FROM cron;                                               -- expect 2 (unchanged)

COMMIT;
```

### Explicitly excluded

```sql
-- DO NOT RUN during product reset:
-- DELETE FROM oc_order_product;
-- DELETE FROM oc_order;
-- DELETE FROM oc_category*;
-- DELETE FROM oc_attribute*;
-- DELETE FROM oc_category_docs;
-- DELETE FROM oc_filter*;
-- DELETE FROM cron;
-- DELETE FROM oc_setting;
```

### Post-DELETE (operator, after COMMIT — not part of DELETE script)

1. Clear OpenCart cache: `system/storage/cache/*`
2. **Do not** delete physical image files (default)
3. Run 1C import sequence (catalog `import0_1.xml` → offers `offers0_1.xml`) via cron toggle — see `SITE-002-PRODUCT-RESET-BEFORE-FRESH-1C-IMPORT-PLAN.md` §9

---

## 6. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Irreversible product loss | **High** | Beget full DB backup **before** any DELETE; TEST only |
| Wrong scope (category/attribute wipe) | **High** | Use exact table list §1; verify post-DELETE counts §5 Phase F |
| Orphan `product_id` in `oc_order_product` (27 rows) | Medium | Expected; do **not** delete order tables |
| Orphan wishlist/cart cleared | Low | Planned (TEST session data) |
| SEO 404 for old product URLs | Medium | Expected until re-import recreates product SEO rows |
| Stale image files on disk | Low | Default: keep files; optional archive |
| Import wrong/stale XML | Medium | Confirm `1c_incoming/webdata/import0_1.xml` + `offers0_1.xml` are fresh upload |
| Cron unintended run | Medium | Keep all cron `active=0` until deliberate import steps |
| Partial import / timeout | Medium | Monitor cron HTTP output; `max_execution_time=300` |
| Price index gap after import | Medium | Verify 06F `refreshPriceIndex()` post-offers |
| Physical file delete without approval | Medium | **Default NO** — §4.3 |

---

## 7. Rollback

### Primary

**Beget full database restore** to snapshot taken immediately before DELETE.

Restores: all products, attributes, SEO URLs, price index, order integrity.

### Secondary (code regressions after import)

Restore PHP from authority baseline:  
`SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` / `projects/ocpilot/sites/site-002/backups/stable-baselines/`

### Files

| Scenario | Action |
|----------|--------|
| Physical delete of `1c_import/` was performed | Restore folder from archive |
| Need previous XML | Re-upload from backup |
| Default (no physical delete) | No file rollback needed |

---

## 8. Ready For Execution (YES/NO)

| Gate | Status |
|------|--------|
| Dry-run table inventory complete | **YES** |
| Live row counts captured (2026-06-19) | **YES** |
| SQL order documented | **YES** |
| Protected tables confirmed | **YES** |
| Image policy documented (no physical delete default) | **YES** |
| Mutations performed in this task | **NONE** |
| Operator approval for DELETE | **NO — awaiting confirmation** |
| Beget DB backup confirmed | **UNKNOWN — operator must confirm before execution** |

### Verdict

**Ready For Execution: YES** (dry run complete; plan validated)

**Execution authorized: NO** — ждём явного подтверждения оператора после review этого отчёта.

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Exact SKU count in fresh uploaded 1C XML |
| **UNKNOWN** | On-disk file count in `image/catalog/1c_import/` (orphans vs DB 559 paths) |
| **UNKNOWN** | Whether operator wants physical archive/delete of `1c_import/` after DB wipe |
| **UNKNOWN** | Beget backup timestamp at moment of execution |
| **SECURITY** | DB credentials used only in local read-only probe scripts under `product-reset-plan-work/`; not stored in this report |

---

**Dry-run status:** COMPLETE  
**Next step:** operator review → confirm Beget backup → explicit **GO** for execution task
