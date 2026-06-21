# REPORT — M9.8.9-06C LIVE PRICE INDEX ROOT CAUSE CONFIRMATION

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Audit date:** 2026-06-19  
**Mode:** READ ONLY — no SQL mutations, no cron URL, no deploy, no commit

**Evidence sources:** live phpMyAdmin (SELECT only), live FTP (RETR/LIST only), prior M9.8.9-06 forensic audit cross-check.

**Supporting artefacts (local, not committed):**
- `reports/m9.8.9-06c-audit-data/` — FTP captures, SQL payloads, variant-C list
- `reports/m9.8.9-06c-audit-data/variant-c-301-clean.json` — 419 unique products for subtree 301

---

## 1. Cron table findings

**Table name:** `cron` (no `oc_` prefix; queried directly by `ModelCatalogCronjob`).

**Schema (read-only `SHOW FULL COLUMNS FROM cron`):**

| Field | Type | Notes |
|-------|------|-------|
| `id` | int(11) PK auto_increment | Task id |
| `name` | varchar(250) | Human label |
| `command` | varchar(80) | Switch key in `ControllerCommonCronjob` |
| `duration` | int(11) | Cooldown seconds added to `lastrun` |
| `lastrun` | timestamp | Last successful completion timestamp |
| `active` | tinyint(4) | **1 = eligible to run** |

**No separate columns** for file name, route, action, or error log. File association is **implicit** via `command` → included PHP script → `glob()` on `1c_incoming/webdata/`.

**All rows (live DB, 2026-06-19):**

| id | name | command | duration (sec) | lastrun | active |
|----|------|---------|----------------|---------|--------|
| 1 | Импорт 1C | `1c` | 1 | **2026-06-02 12:43:23** | **0** |
| 2 | Импорт 1C - цены и остатки | `1c_offers` | 1 | **2026-06-02 10:23:15** | **0** |

**Active task selection (not manual `Active=1` alone):**

```php
// catalog/model/catalog/cronjob.php
SELECT * FROM `cron`
WHERE DATE_ADD(`lastrun`, INTERVAL `duration` SECOND) < NOW()
  AND active = 1;
```

Operator workflow (activate `import0_1` task, run cron, deactivate; then activate `offers0_1` task, run cron, deactivate) maps to:

1. Set `active=1` on row id=1 (`command=1c`) → processes `import0_*.xml`
2. Cron hit sets `lastrun=NOW()` via `setDone($id)` on success
3. Set `active=0` on row 1, set `active=1` on row id=2 (`command=1c_offers`) → processes `offers0_*.xml`

**Current state:** both tasks **inactive** (`active=0`). No error column; failures would surface only in HTTP output of cron URL (not invoked in this audit).

**File locations on server (FTP LIST, read-only):**

| Path | Contents | mtime |
|------|----------|-------|
| `1c_incoming/webdata/import0_1.xml` | Catalog import (live path) | 2026-06-08 |
| `1c_incoming/webdata/offers0_1.xml` | Prices/stock (live path) | 2026-06-08 |
| `1c_exchange/import0_1.xml` | Legacy/stale copy | 2026-06-08 |

Live code uses **`1c_incoming/webdata/`** (`1c_exchange/` is commented out in import handlers).

**SAFE UNKNOWN:** whether operator re-ran cron after 2026-06-08 file upload — `lastrun` timestamps (2026-06-02) predate XML mtimes (2026-06-08), suggesting **either** post-upload import not executed **or** files were replaced without re-import.

---

## 2. Cronjob controller chain

**Entry:** `index.php?route=common/cronjob`  
**File:** `catalog/controller/common/cronjob.php` (live FTP, 215 lines)

**Execution chain:**

```
ControllerCommonCronjob::index()
  → load model catalog/cronjob
  → ModelCatalogCronjob::getTasks()     // active=1 AND cooldown elapsed
  → foreach task by command:
       case '1c':       parse1C()        → include import_1C.php
       case '1c_offers': parse1COffers() → include import_1C_offers.php
  → if $itsOK: ModelCatalogCronjob::setDone($id)  // UPDATE lastrun=NOW()
  → break after first successful task
```

**Key behaviours:**
- Processes **one** eligible task per HTTP hit, then `break`
- `$itsOK` is set inside included files (`import_1C.php` / `import_1C_offers.php`)
- **No** call to `refreshPriceIndex` anywhere in `cronjob.php`
- Helper methods: `processProduct1C()`, `processImage1C()`, `translit()`, logging

---

## 3. 1C import0_1.xml handler

**File:** `catalog/controller/common/import_1C.php` (included by `parse1C()`)

| Aspect | Detail |
|--------|--------|
| Input glob | `$import_directory . 'import0_*.xml'` |
| Directory | `DIR_ROOT . '1c_incoming/webdata/'` |
| Product logic | `processProduct1C()` via `import_1C_process.php` |
| Updates | xml_id, model, image, manufacturer, status, descriptions, categories, attributes |
| Price fields | **Does not set** `price`, `price2`, `price3`, `discount1c` in import path |
| End state | Clears SeoPro / product cache; `$itsOK = true` |
| refreshPriceIndex | **NOT called** |

**Conclusion:** catalog import creates/updates product metadata but **does not populate price index**. Prices for display on PLP depend on a separate offers pass + index rebuild.

---

## 4. 1C offers0_1.xml handler

**File:** `catalog/controller/common/import_1C_offers.php` (included by `parse1COffers()`)

| Aspect | Detail |
|--------|--------|
| Input glob | `$offers_directory . 'offers0_*.xml'` |
| Directory | `DIR_ROOT . '1c_incoming/webdata/'` |
| Match key | `xml_id` → `product_id` |
| Per-offer UPDATE | `oc_product.quantity`, `oc_product.price` only |
| price2 / price3 / discount1c | **Not updated** by offers import |
| End state | `$itsOK = true` |
| refreshPriceIndex | **NOT called** |

**Critical gap:** offers import **mutates live card base price** in `oc_product` but **never rebuilds** `oc_product_price_index`. Filter PLP reads index, not raw `oc_product.price` (see §6 linkage).

---

## 5. refreshPriceIndex callers

**Method definitions (live FTP):**
- `catalog/model/catalog/product.php` — `refreshPriceIndex($product_id = 0)` (full rebuild helper)
- `admin/model/catalog/product.php` — `refreshPriceIndex($product_id)` (single-product)

**Live callers of `refreshPriceIndex` (FTP grep):**

| Location | When invoked |
|----------|--------------|
| `admin/controller/catalog/product.php` | After **manual** admin add (line 24) and edit (line 78) POST |
| `reindex_prices.php` | Standalone CLI/browser script — loops all products, calls admin model method |
| `catalog/controller/common/cronjob.php` | **No** |
| `import_1C.php` | **No** |
| `import_1C_offers.php` | **No** |
| `import_1C_process.php` | **No** |

**`reindex_prices.php`** exists at site root as an **manual maintenance** entry point; it is **not** wired into cron or 1C pipeline.

**Index logic:** `refreshPriceIndex` deletes + reinserts rows in `oc_product_price_index` per customer group, using `getProductForIndex()` with `price` / `price2` / `price3` / `discount1c` / specials / category discounts.

---

## 6. Price index coverage 301 (Столы)

**Query:** active products in subtree `category_id = 301`, guest-normalized group **2** (`customer_group_id = 2`).

| Metric | Value |
|--------|-------|
| Active products in subtree 301 | **419** |
| With `oc_product_price_index` row (group 2) | **1** |
| Coverage | **0.24%** |
| Missing index rows | **418** |

**Only indexed product (live DB):**

| product_id | model | name | oc_product.price | index price | index special |
|------------|-------|------|------------------|-------------|---------------|
| 3213 | СПКБ-18/7-ВЛ5 | Стол-тумба СПКБ-18/7-ВЛ5 (1800×700×850) | 60330 | 60330 | **51280.5** |

This matches M9.8.9-06 forensic finding: price slider on «Столы» collapsed to **51280–51281** because `getCategoryPriceRange()` aggregates **only** `oc_product_price_index` — with one row, min≈max≈51280.

---

## 7. Price index coverage 80 (Моечные ванны)

| Metric | Value |
|--------|-------|
| Active products in subtree 80 | **152** |
| With index (group 2) | **37** |
| Coverage | **24.34%** |

Partial coverage explains why «Моечные ванны» price slider works better (8500–40375 in M9.8.9-06) but filters can still be inconsistent for non-indexed SKUs.

---

## 8. Price index coverage global

| Metric | Value |
|--------|-------|
| Active products (store 0, status=1) | **608** |
| Distinct products indexed (group 2) | **110** |
| Global group-2 coverage | **~18.1%** |
| Total rows in `oc_product_price_index` | **330** |

330 rows vs 110 products ⇒ multiple customer groups indexed for a subset of catalog (admin/manual rebuild path indexes all groups per product).

**Interpretation:** index is **systemically stale/incomplete** site-wide, not limited to category 301. Category 301 is the **worst** branch (0.24%), likely because almost no post-import rebuild ever ran for those SKUs.

---

## 9. Variant C readiness

**Goal:** point rebuild list for subtree 301 without executing rebuild.

| Item | Value |
|------|-------|
| Unique product_ids prepared | **419** |
| Missing `has_price_index_group_2` | **418** |
| Already indexed | **1** (product_id **3213**) |
| Full list file | `reports/m9.8.9-06c-audit-data/variant-c-301-clean.json` |

**Sample (first rows, all `has_index: no`):**

| product_id | model | name | card price (oc_product.price) |
|------------|-------|------|-------------------------------|
| 2786 | СПК-18/6 | Стол-тумба СПК-18/6 (1800×600×850) | 50810 |
| 2787 | СПК-18/7 | Стол-тумба СПК-18/7 (1800×700×850) | 54819 |
| 2788 | СПКБ-18/7 | Стол-тумба СПКБ-18/7 (1800×700×850) | 55311 |
| 2789 | СК-П-12/6 | Стол кондитерский СК-П-12/6 (1200×600×850) | 22967 |

**Rebuild volume:** 418 `refreshPriceIndex(product_id)` calls (or filtered batch) for subtree 301; 1 product can be skipped.

**Card price source:** `oc_product.price` (updated by offers import). Index rebuild will recompute effective guest price including `discount1c` / specials per model logic.

---

## 10. Root cause confidence

### Q1. Почему для «Столов» индекс почти пустой?

**Answer (confidence: HIGH):**  
`oc_product_price_index` for subtree 301 has **1/419** rows (0.24%). PLP price filter uses `getCategoryPriceRange()` which **JOINs only** `product_price_index` — not live `oc_product.price`. After 1C offers updated hundreds of table SKUs in `oc_product`, **no index rebuild ran**, leaving 418 products invisible to price aggregation.

### Q2. Связано ли с тем, что offers0_1 обновляет цены, но не вызывает refreshPriceIndex?

**Answer (confidence: HIGH — confirmed in live code):**  
Yes. `import_1C_offers.php` executes:

```php
UPDATE oc_product SET quantity = ..., price = ... WHERE product_id = ...
```

No subsequent `refreshPriceIndex()`. This is a **direct causal chain** for index/card price divergence.

### Q3. Есть ли вызов refreshPriceIndex в текущем cron/1C-коде?

**Answer (confidence: HIGH — confirmed negative):**  
**No.** Cron pipeline and both 1C import includes do not call it. Only admin product save and manual `reindex_prices.php`.

### Q4. Где должен быть вызов?

| Hook point | Recommendation | Rationale |
|------------|----------------|-----------|
| After each product in offers loop | Optional (per-product) | Correct but N queries; acceptable for ~600 SKUs |
| **After entire offers file** | **Primary fix** | Matches batch import semantics; call `refreshPriceIndex($product_id)` for each updated id collected in loop |
| After import0_1 file | Secondary | New products still need prices from offers first; index rebuild more critical **after offers** |
| After each import0_1 product | Low priority | No price change at import stage |

**Best placement:** end of `import_1C_offers.php` (after successful UPDATE loop), optionally also at end of `import_1C.php` for newly inserted products once offers have run.

### Q5. Можно ли безопасно чинить через Variant C?

**Answer (confidence: HIGH for operational safety, MEDIUM for scope):**

| Factor | Assessment |
|--------|------------|
| Safety | **Yes** — `refreshPriceIndex` is idempotent delete+insert per product; read-only audit confirms method exists in both catalog and admin models |
| Scope | Variant C fixes **301 only** (418 products); global gap is **498** missing group-2 rows site-wide — full fix needs global rebuild or cron hook |
| Risk | Low if run off-peak; uses same logic as admin save hook |
| Not in this audit | Execution of rebuild (explicitly forbidden) |

---

## 11. Recommended next action

**Immediate (HITL, outside this audit):**

1. **Variant C execution charter** — rebuild index for 418 product_ids in subtree 301 via controlled `refreshPriceIndex` batch (operator script or adapted `reindex_prices.php` with WHERE filter). Verify price slider on `/katalog/nejtralnoe-oborudovanie/stoly/` returns wide min/max.

2. **Structural fix (separate change task)** — add `refreshPriceIndex($product_id)` call in `import_1C_offers.php` after each price UPDATE (or batch at file end) so future 1C runs keep index in sync.

3. **Global catch-up** — plan full-catalog reindex (608 products) or post-offers hook; current 18% global coverage affects other branches too.

4. **Operator sync check** — reconcile cron `lastrun` (2026-06-02) vs XML mtimes (2026-06-08); confirm whether post-upload 1C sequence was completed.

**Do NOT (per authority):** run cron URL, flip `active`, SQL UPDATE/INSERT/DELETE, deploy, or commit in this audit pass.

---

## Cross-reference

Prior audit: `SITE-002-M9.8.9-06-FILTER-BUG-FORENSIC-AUDIT.md` — hypothesized index/card price split for category 301; **this audit confirms with live DB + live code.**

---

**Changed files (this task):**
- `projects/ocpilot/sites/site-002/reports/SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md` (created)
- `projects/ocpilot/sites/site-002/reports/m9.8.9-06c-*.py` (audit helpers, local)
- `projects/ocpilot/sites/site-002/reports/m9.8.9-06c-audit-data/*` (evidence captures, local)

**Git:** no commit (per task).

**UNKNOWN:** exact operator run history after 2026-06-08 XML drop; cron HTTP logs not inspected.

**SECURITY RISK:** audit scripts contain live DB/FTP credentials copied from existing operator tooling — do not commit helper scripts without credential scrubbing.
