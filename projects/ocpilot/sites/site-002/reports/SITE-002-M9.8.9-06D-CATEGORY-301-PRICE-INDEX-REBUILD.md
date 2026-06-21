# REPORT — M9.8.9-06D CATEGORY 301 PRICE INDEX REBUILD

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Execution date:** 2026-06-19  
**Basis:** `SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md`

**Scope:** Rebuild `oc_product_price_index` for subtree **category_id = 301** (Столы) only.  
**Out of scope (not touched):** 1C import code, cron, `import_1C_offers.php`, global architecture.

---

## 1. Backup

Live FTP capture (read-only RETR) before any mutation:

| Remote path | Local capture | SHA-256 |
|-------------|---------------|---------|
| `catalog/model/catalog/product.php` | `reports/m9.8.9-06d-work/live-capture/catalog__model__catalog__product.php` | `4dea6237…94659` |
| `catalog/controller/common/import_1C_offers.php` | `reports/m9.8.9-06d-work/live-capture/catalog__controller__common__import_1C_offers.php` | `403c813e…6586d` |
| `admin/model/catalog/product.php` | `reports/m9.8.9-06d-work/live-capture/admin__model__catalog__product.php` | `1b8aecca…ca9e3a` |
| `reindex_prices.php` | `reports/m9.8.9-06d-work/live-capture/reindex_prices.php` | `e3d4ea12…87850` |

**Manifest:** `reports/m9.8.9-06d-work/manifest-20260619-123127.json`

**Baseline snapshot (category 301, before rebuild):**

| Metric | Value |
|--------|-------|
| Active products | **419** |
| Indexed (group 2) | **1** |
| Coverage | **0.24%** |
| DB min_price (group 2) | **51280.50** |
| DB max_price (group 2) | **51280.50** |

---

## 2. Rebuild method

| Item | Value |
|------|-------|
| Source list | `reports/m9.8.9-06c-audit-data/variant-c-301-clean.json` |
| SKUs without index | **418** (`has_index: no`) |
| Already indexed (skipped) | **1** (product_id **3213**) |
| Mechanism | **`refreshPriceIndex(product_id)`** via `admin/model/catalog/product.php` |
| Pattern | Adapted from live `reindex_prices.php` — **no direct SQL INSERT** into `oc_product_price_index` |
| Deploy | Temporary script `reindex_prices_301_m98906d.php` uploaded → HTTP run (token-gated) → **removed from server** |
| Site code changed | **No** — only DB index rows updated through model logic |

**Runner (local):** `reports/m9.8.9-06d-category-301-reindex-run.py`  
**Run log:** `reports/m9.8.9-06d-work/reindex-run-output.txt`

---

## 3. Products processed

| Result | Count |
|--------|-------|
| **OK** | **418** |
| **FAIL** | **0** |

Sample processed IDs: 2786, 2787, 2788, 2789, 2790 … 3216 (full list in variant-C JSON).

---

## 4. Coverage before

| Metric | Value |
|--------|-------|
| Active products | 419 |
| Indexed products (group 2) | 1 |
| Coverage | **0.24%** |

---

## 5. Coverage after

| Metric | Value |
|--------|-------|
| Active products | 419 |
| Indexed products (group 2) | 419 |
| Coverage | **100.00%** |

**Verified via phpMyAdmin SELECT** (same query as M9.8.9-06C audit).

---

## 6. PLP min/max before

**URL:** https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/

**Evidence:** `reports/m9.8.9-06d-work/plp-stoly-before.html`

| Source | min | max |
|--------|-----|-----|
| Price slider (`data-range-min` / `data-range-max`) | **51280** | **51281** |
| DB index aggregate (group 2) | **51280.50** | **51280.50** |

**Diagnosis:** Degenerate range (span = 1 ₽) — one indexed SKU drove entire price filter.

---

## 7. PLP min/max after

**Evidence:** `reports/m9.8.9-06d-work/plp-stoly-after.html`

| Source | min | max |
|--------|-----|-----|
| Price slider (`data-range-min` / `data-range-max`) | **5405** | **72630** |
| DB index aggregate (group 2) | **5405.00** | **72630.00** |

**Span:** 67 225 ₽ (was 1 ₽). Matches real catalog price spread for Столы.

---

## 8. Slider verification

| Check | Before | After |
|-------|--------|-------|
| Range span vs step (1000) | 1 ₽ — **degenerate** | 67 225 ₽ — **normal** |
| Both thumbs same track position | **Yes** (51280 ≈ 51281) | **No** — distinct min/max |
| Right thumb drags left thumb | **Yes** (M9.8.9-06 bug) | **No** — independent range |
| `price_from` placeholder | 51280 | 5405 |

**Result:** Price slider on Столы PLP is **no longer collapsed**.

**Note (out of scope):** Height filter still shows 850–850 (attribute range, not price index) — unchanged, expected.

---

## 9. Filter verification

| Check | Status |
|-------|--------|
| Price range reflects indexed catalog | **PASS** — 5405–72630 |
| Filter no longer single-price band | **PASS** |
| Index coverage supports price aggregation | **PASS** — 419/419 |
| Structural 1C/cron fix | **Not done** (separate task per charter) |

Price filter on `/katalog/nejtralnoe-oborudovanie/stoly/` is **operationally restored** for guest group 2.

---

## 10. Rollback

| Layer | Rollback path |
|-------|---------------|
| **Site files** | Not modified — no file rollback needed |
| **Temporary script** | `reindex_prices_301_m98906d.php` **deleted** from live root after run |
| **DB index (301 subtree)** | Restore from **Beget full backup** or re-run offers import + manual reindex; no automated rollback script executed |
| **Evidence** | Pre-capture manifest + PLP HTML before/after in `reports/m9.8.9-06d-work/` |

To revert index data only: restore `oc_product_price_index` rows for product_ids in `variant-c-301-clean.json` from DB backup taken before this run (if operator created one). Live site PHP remains at pre-task state.

---

## Git / deploy summary

| Action | Status |
|--------|--------|
| Git commit | **NO** |
| Git push | **NO** |
| Live deploy (site code) | **NO** — only ephemeral reindex script |
| Live data fix | **YES** — 418 × `refreshPriceIndex` executed |

---

## Changed / created files (local repo)

| Path | Role |
|------|------|
| `reports/SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md` | This report |
| `reports/m9.8.9-06d-category-301-reindex-run.py` | Execution helper |
| `reports/m9.8.9-06d-work/` | Manifest, live captures, run log, PLP HTML before/after |

---

## Recommended follow-up (separate tasks)

1. Add `refreshPriceIndex($product_id)` hook at end of `import_1C_offers.php` so future 1C runs keep index in sync.
2. Plan global index catch-up (~18% site-wide coverage per M9.8.9-06C) if other branches show similar filter gaps.

---

## Cross-reference

- Root cause: `SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md`
- Forensic filter audit: `SITE-002-M9.8.9-06-FILTER-BUG-FORENSIC-AUDIT.md`
