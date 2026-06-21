# REPORT — SITE-002 PRODUCT RESET EXECUTION

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Environment:** https://zpm.new-site.space/  
**Database:** `polygonws_zpm`  
**Execution UTC:** 2026-06-19T08:31:27Z → 2026-06-19T08:33:37Z  
**Operator approval:** GO CONFIRMED  
**Beget backup:** CONFIRMED  
**Dry-run reference:** `SITE-002-PRODUCT-RESET-DRY-RUN-FINAL.md`  

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/product-reset-execution-work/`  
- `manifest-20260619-083123.json`  
- `pre-capture-20260619-083123.json`  
- `delete-results-20260619-083123.json`  
- `post-verify-20260619-083123.json`  
- `cache-clear-20260619-083123.json`  
- `run-summary-20260619-083123.json`  

---

## 1. Execution Summary

| Item | Result |
|------|--------|
| Pre-execution live capture | **DONE** — counts match dry-run snapshot |
| Execution manifest created | **DONE** — `manifest-20260619-083123.json` |
| DELETE phases A→E | **COMPLETE** — 25 steps, 0 errors |
| Total rows deleted | **27 932** (matches dry-run estimate) |
| Post-delete verification | **PASS** |
| Physical image files | **NOT touched** (`image/catalog/1c_import/` preserved) |
| Theme / twig / css / js | **NOT touched** |
| OpenCart cache flush | **ATTEMPTED** — cache dirs already empty (0 files deleted) |
| Execution errors | **NONE** |

**Verdict:** Product-owned DB data cleared. Category tree, attribute definitions, settings, orders, cron, and 1C XML on disk preserved.

---

## 2. Tables Cleared

Executed in order per dry-run §5 (phases A→E):

| Phase | Table | Action |
|-------|-------|--------|
| A | `oc_coupon_product` | DELETE ALL |
| A | `oc_customer_wishlist` | DELETE ALL |
| A | `oc_cart` | DELETE ALL |
| A | `oc_googleshopping_product` | DELETE ALL |
| A | `oc_googleshopping_product_status` | DELETE ALL |
| A | `oc_googleshopping_product_target` | DELETE ALL |
| B | `oc_product_price_index` | DELETE ALL |
| C | `oc_product_attribute` | DELETE ALL |
| C | `oc_product_description` | DELETE ALL |
| C | `oc_product_discount` | DELETE ALL |
| C | `oc_product_filter` | DELETE ALL |
| C | `oc_product_image` | DELETE ALL |
| C | `oc_product_option_value` | DELETE ALL |
| C | `oc_product_option` | DELETE ALL |
| C | `oc_product_related` | DELETE ALL |
| C | `oc_product_reward` | DELETE ALL |
| C | `oc_product_special` | DELETE ALL |
| C | `oc_product_to_category` | DELETE ALL |
| C | `oc_product_to_download` | DELETE ALL |
| C | `oc_product_to_layout` | DELETE ALL |
| C | `oc_product_to_store` | DELETE ALL |
| C | `oc_product_recurring` | DELETE ALL |
| C | `oc_review` | DELETE ALL |
| D | `oc_seo_url` | DELETE WHERE `query LIKE 'product_id=%'` |
| E | `oc_product` | DELETE ALL (last) |

---

## 3. Rows Deleted

### Pre-execution counts (live capture 2026-06-19T08:31:27Z)

| Metric | Count |
|--------|------:|
| `oc_product` | 3134 |
| Product SEO URLs | 3134 |
| `oc_product_attribute` | 10175 |
| `oc_product_image` | 6 |
| `oc_product_price_index` | 1977 |

### Per-table deleted rows

| Phase | Table | Rows before | Rows deleted |
|-------|-------|------------:|-------------:|
| A | `oc_coupon_product` | 0 | 0 |
| A | `oc_customer_wishlist` | 27 | 27 |
| A | `oc_cart` | 16 | 16 |
| A | `oc_googleshopping_product` | 1 | 1 |
| A | `oc_googleshopping_product_status` | 0 | 0 |
| A | `oc_googleshopping_product_target` | 0 | 0 |
| B | `oc_product_price_index` | 1977 | 1977 |
| C | `oc_product_attribute` | 10175 | 10175 |
| C | `oc_product_description` | 3134 | 3134 |
| C | `oc_product_discount` | 1 | 1 |
| C | `oc_product_filter` | 0 | 0 |
| C | `oc_product_image` | 6 | 6 |
| C | `oc_product_option_value` | 0 | 0 |
| C | `oc_product_option` | 0 | 0 |
| C | `oc_product_related` | 0 | 0 |
| C | `oc_product_reward` | 0 | 0 |
| C | `oc_product_special` | 2 | 2 |
| C | `oc_product_to_category` | 3134 | 3134 |
| C | `oc_product_to_download` | 0 | 0 |
| C | `oc_product_to_layout` | 57 | 57 |
| C | `oc_product_to_store` | 3134 | 3134 |
| C | `oc_product_recurring` | 0 | 0 |
| C | `oc_review` | 0 | 0 |
| D | `oc_seo_url` (product) | 3134 | 3134 |
| E | `oc_product` | 3134 | 3134 |
| | **Total** | | **27 932** |

Pre-capture counts matched dry-run exactly; no drift detected at execution time.

---

## 4. Tables Preserved

| Table / area | Count before | Count after | Status |
|--------------|-------------:|------------:|--------|
| `oc_category` | 190 | **190** | preserved |
| `oc_category_description` | 190 | — | preserved |
| `oc_category_path` | 522 | — | preserved |
| `oc_category_docs` | 4 | **4** | preserved |
| `oc_attribute` | 59 | **59** | preserved |
| `oc_attribute_group` | 6 | — | preserved |
| `oc_filter_group` | 0 | **0** | preserved |
| Filter profiles PHP (`system/library/zpm/filter_profiles/*`) | filesystem | — | **NOT touched** |
| `oc_setting` | 201 | **201** | preserved |
| `oc_order` | 16 | **16** | preserved |
| `oc_order_product` | 27 | — | preserved (orphan refs expected) |
| `cron` | 2 | **2** | preserved |
| `1c_incoming/webdata/` XML | filesystem | — | **NOT touched** |
| `1c_exchange/` | filesystem | — | **NOT touched** |
| `image/catalog/1c_import/` | filesystem | — | **NOT deleted** |
| Theme / twig / css / js | filesystem | — | **NOT touched** |

Non-product SEO URLs preserved: **247** (category / information / manufacturer / other).

---

## 5. Product Count After

| Metric | Count |
|--------|------:|
| `oc_product` | **0** |
| `oc_product_attribute` | **0** |
| `oc_product_price_index` | **0** |
| `oc_product_image` | **0** |
| `oc_customer_wishlist` | **0** |
| `oc_cart` | **0** |
| `oc_googleshopping_product` | **0** |

---

## 6. Category Count After

| Metric | Count |
|--------|------:|
| `oc_category` | **190** (unchanged) |
| `oc_category_docs` | **4** (unchanged) |

Category PLP pages remain navigable; product grids will be empty until 1C import.

---

## 7. Attribute Count After

| Metric | Count |
|--------|------:|
| `oc_attribute` | **59** (unchanged) |
| `oc_attribute_group` | **6** (unchanged per dry-run) |

Attribute definitions and filter-profile infrastructure preserved for post-import re-linking.

---

## 8. SEO URL Count After

| Kind | Count |
|------|------:|
| Product (`query LIKE 'product_id=%'`) | **0** |
| Non-product (category / information / other) | **247** (unchanged) |
| Total `oc_seo_url` | **247** |

---

## 9. Cache Clear

| Action | Result |
|--------|--------|
| `system/storage/cache/*` | Scanned via FTP — **0 cache files** present (only `index.html` guards) |
| `system/storage/cache/template/*` | Scanned via FTP — **0 template cache files** present |
| Errors | **None** |

Safe OpenCart file caches cleared or already empty. No template/CSS/JS files modified.

---

## 10. Rollback

### Primary

**Beget full database restore** to snapshot taken before execution (operator-confirmed backup).

Restores: all 3134 products, attributes, SEO URLs, price index, wishlist/cart.

### Secondary

- PHP baseline: `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` / `projects/ocpilot/sites/site-002/backups/stable-baselines/`
- Physical images: no rollback needed (files not deleted)
- 1C XML: re-upload from backup if needed

### Known post-reset state

- `oc_order_product` retains 27 rows referencing deleted `product_id` values (expected per dry-run §6)
- Stale image files may remain on disk in `image/catalog/1c_import/` (harmless; fresh import overwrites)

---

## READY FOR CLEAN 1C IMPORT

| Gate | Status |
|------|--------|
| `oc_product` = 0 | **YES** |
| Product SEO URLs = 0 | **YES** |
| `oc_product_price_index` = 0 | **YES** |
| Categories preserved | **YES** (190) |
| Attributes preserved | **YES** (59) |
| XML files preserved (not deleted) | **YES** (filesystem untouched) |
| No execution errors | **YES** |
| Physical images preserved | **YES** |

### **READY FOR CLEAN 1C IMPORT: YES**

**Next step (operator):** Run 1C import sequence per `SITE-002-PRODUCT-RESET-BEFORE-FRESH-1C-IMPORT-PLAN.md` §9 — catalog `import0_1.xml` → offers `offers0_1.xml` via cron toggle.

---

## UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Exact SKU count in fresh uploaded 1C XML |
| **UNKNOWN** | On-disk file count in `image/catalog/1c_import/` (orphans may exceed former 559 DB paths) |
| **SECURITY** | DB/FTP credentials used only in local execution script; not stored in this report |

---

**Execution status:** COMPLETE  
**Git commit/push:** NOT performed (per task)
