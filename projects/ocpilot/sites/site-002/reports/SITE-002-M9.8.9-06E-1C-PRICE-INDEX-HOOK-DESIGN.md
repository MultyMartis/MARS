# REPORT — M9.8.9-06E 1C PRICE INDEX HOOK DESIGN

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Basis:** M9.8.9-06C (root cause), M9.8.9-06D (418× `refreshPriceIndex` proof)  
**Audit date:** 2026-06-19  
**Mode:** Forensic design pass only — **no code changes, no deploy, no cron, no import**

**Evidence (read-only, not re-fetched in this task):**
- Live FTP captures: `reports/m9.8.9-06d-work/live-capture/`
- Prior audits: `SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md`, `SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md`
- Baseline SHA-256 for target file: `import_1C_offers.php` → `403c813e…6586d` (manifest `m9.8.9-06d-work/manifest-20260619-123127.json`)

---

## Executive answers (task checklist)

| # | Question | Answer |
|---|----------|--------|
| 1 | **Где правильная точка вызова?** | В `catalog/controller/common/import_1C_offers.php`: **после цикла UPDATE по предложениям**, до `unset($xml)` / перехода к следующему файлу. Рекомендуется **Option B** — накопить `$product_id` в set и вызвать `refreshPriceIndex` batch-блоком (см. §8). |
| 2 | **Сколько раз будет вызван `refreshPriceIndex`?** | **1 раз на каждый уникальный `product_id`, прошедший UPDATE** в offers-цикле. Оценка для полного `offers0_1.xml`: **≤ ~608** (число активных SKU с `xml_id`; точное число `<Предложение>` в XML — **SAFE UNKNOWN**, файл не парсился в этом проходе). Дубликаты `xml_id` в одном файле → **1 вызов** при dedupe. |
| 3 | **Риск сильного замедления?** | **Низкий–умеренный.** M9.8.9-06D: 418 вызовов ≈ **~30–35 с** (~79 ms/товар). Полный каталог (~608) ≈ **~45–55 с** дополнительно к текущему offers-import. Укладывается в `max_execution_time = 300` cronjob, если offers-файл один. |
| 4 | **Нужен ли batch rebuild после цикла?** | **Нет**, если hook вызывает `refreshPriceIndex` для всех затронутых ID. Отдельный post-import rebuild — дублирование и лишняя нагрузка. |
| 5 | **Option A vs B?** | **Option B (recommended):** собирать ID → refresh после файла (или после всех файлов glob). Тот же итог по количеству вызовов, dedupe, меньше interleaving UPDATE/index, проще логирование ошибок. Option A допустим, но хуже при partial failure и duplicate offers. |

---

## 1. Current import chain

```
HTTP index.php?route=common/cronjob
  └─ ControllerCommonCronjob::index()
       └─ ModelCatalogCronjob::getTasks()          // active=1 AND cooldown elapsed
       └─ switch command:
            case '1c':
              parse1C() → include import_1C.php     // import0_*.xml
            case '1c_offers':
              parse1COffers() → include import_1C_offers.php   // offers0_*.xml  ← TARGET
       └─ if $itsOK → setDone(cron_id)             // UPDATE cron.lastrun
       └─ break after first successful task
```

**Operator sequence (documented in 06C):**
1. Activate cron row `command=1c` → `import0_1.xml`
2. Deactivate `1c`, activate `command=1c_offers` → `offers0_1.xml`

**Key facts:**
- `$this` inside `import_1C_offers.php` = `ControllerCommonCronjob` instance (include scope).
- `$this->db`, `$this->load->model(...)`, `$this->config` доступны.
- **`refreshPriceIndex` сейчас не вызывается** ни в cronjob, ни в import_1C, ни в import_1C_offers.
- Единственные production-callers до фикса: admin product add/edit, manual `reindex_prices.php`.

**Related path (out of offers scope, for completeness):**

```
import_1C.php
  └─ foreach Товар → processProduct1C() → include import_1C_process.php
       └─ updates: xml_id, model, image, status, categories, attributes, dimensions
       └─ does NOT set price / price2 / price3 / discount1c
       └─ does NOT call refreshPriceIndex
```

---

## 2. Price update location

**File:** `catalog/controller/common/import_1C_offers.php` (live capture, 65 lines)

| Step | Lines | Action |
|------|-------|--------|
| Resolve directory | 5–6 | `glob(DIR_ROOT . '1c_incoming/webdata/offers0_*.xml')` |
| Build xml_id map | 15–19 | `SELECT product_id, xml_id FROM oc_product` → `$existing_products` |
| Per offer loop | 30–53 | Match `Ид` → `$product_id`; read `Количество`, `Цены/Цена/ЦенаЗаЕдиницу` |
| **Price UPDATE** | **47–50** | `UPDATE oc_product SET quantity=..., price=... WHERE product_id=...` |
| Success flag | 65 | `$itsOK = true` (unconditional after all files) |

**Quantity update:** same UPDATE at lines 47–50 (`quantity` + `price` in one statement).

**Not updated by offers import (confirmed in live code):**
- `price2`, `price3`, `discount1c`, `status`, categories, specials, product_discount

**Root cause (confirmed 06C + 06D):** PLP price filter, `only_with_price`, price slider, `getCategoryPriceRange()` читают **`oc_product_price_index`**, не `oc_product.price`. Offers меняет только `oc_product.price` → index drift.

---

## 3. Product ID availability

**In-loop availability (confirmed safe):**

```php
// Line 34-38: skip unknown xml_id
if (!isset($existing_products[$xml_id])) continue;
$product_id = $existing_products[$xml_id];  // int, always defined here
```

**Which products enter the loop:**
- Every `<Предложение>` in `ПакетПредложений/Предложения`
- **Only if** `Ид` matches a non-empty `oc_product.xml_id`
- Offers for unknown/new SKUs (not yet in catalog import) are **silently skipped** (`continue`)

**Processed ID set characteristics:**
- No separate `$processed_product_ids` array today — only implicit per-iteration `$product_id`
- Full catalog map preloaded once (all products with `xml_id`)
- Multiple files via `offers0_*.xml` glob: IDs may repeat across files → **dedupe recommended**

**Can `refreshPriceIndex($product_id)` run inside the current loop?**

| Check | Result |
|-------|--------|
| Method exists | **Yes** — `catalog/model/catalog/product.php` and `admin/model/catalog/product.php` |
| Proven on live | **Yes** — 418/418 OK in M9.8.9-06D via admin model |
| Idempotent | **Yes** — DELETE + INSERT per product per customer group |
| `$this->load->model('catalog/product')` in include context | **Yes** — standard OpenCart controller pattern |
| Needs `$product_id > 0` | **Yes** — always satisfied after map lookup |
| Transaction coupling | **No** — each UPDATE and refresh is independent; partial index refresh on crash is acceptable (same as partial import today) |

**Verdict:** **Safe to call inside or immediately after the offer loop.**

---

## 4. Option A analysis

**Pattern:** call `refreshPriceIndex($product_id)` immediately after each UPDATE (line 50).

| Pros | Cons |
|------|------|
| Minimal code delta | UPDATE and index rebuild interleaved → harder to profile |
| Index fresh during long import (edge case) | Duplicate XML rows → duplicate refresh (waste) |
| Matches admin edit hook mentally | On failure mid-loop: some products indexed, some not — harder to retry block |
| Same call count as B if no duplicates | Slightly more DB round-trips between consecutive products |

**Call count:** 1 × per matched offer row (no dedupe) = **N offers processed**.

---

## 5. Option B analysis

**Pattern:** accumulate unique IDs during loop; run refresh block after inner loop (per file) or after all files.

```php
// Pseudocode — NOT implemented in this task
$price_index_refresh_ids = [];

// inside offer loop, after UPDATE:
$price_index_refresh_ids[(int)$product_id] = true;

// after inner foreach, before unset($xml):
$this->load->model('catalog/product');
foreach (array_keys($price_index_refresh_ids) as $pid) {
    $this->model_catalog_product->refreshPriceIndex($pid);
}
$price_index_refresh_ids = []; // reset per file
```

| Pros | Cons |
|------|------|
| Dedupe within file | Index stale until block runs (seconds — acceptable) |
| Clear separation: import phase → index phase | Slightly more code |
| Easier to log `refreshed N products` once per file | If refresh block throws, all UPDATEs done but index batch failed |
| Same semantics as 06C recommendation | |
| Can extend with try/catch per ID without stopping UPDATE loop | |

**Recommended variant:** dedupe **per file** (reset array each file iteration). If multiple `offers0_*.xml` exist, optionally merge into one global set before final refresh — **SAFE UNKNOWN** how many files operator uses (glob allows N).

**Call count:** 1 × per **unique** `product_id` updated in file(s).

---

## 6. Performance impact

**Baseline from M9.8.9-06D (measured):**

| Metric | Value |
|--------|-------|
| Products refreshed | 418 |
| Failures | 0 |
| Wall time (approx.) | ~30–35 s (run start → post-rebuild PLP fetch) |
| Per-product (approx.) | ~79 ms |
| Extrapolated 608 SKUs | ~48 s |

**Per `refreshPriceIndex($product_id)` cost (admin model, live code):**
1. SELECT customer groups
2. SELECT product + discount subquery
3. DELETE FROM `oc_product_price_index` WHERE product_id
4. For each customer group (~3 groups → ~330 index rows / 110 products in 06C): category discount query + INSERT

**Offers import baseline (without index):** lightweight — 1 UPDATE + echo per offer. Adding refresh dominates runtime but remains **≪ 300 s** cron limit for ~600 SKUs.

**Memory:** cronjob already `memory_limit = 512M`. ID set of ~600 ints negligible. Catalog model refresh uses session override briefly — cleared at method end.

**Risk of "strong slowdown":** **Low** for current catalog size (~608 active). **Monitor** if catalog grows 5×+ or customer groups increase.

**Separate batch rebuild after cycle:** **Not required** when hook covers all updated IDs.

---

## 7. Recommended implementation

**Primary fix (M9.8.9-06F scope):** Option B in `import_1C_offers.php`.

**Model choice:**

| Model | Recommendation |
|-------|----------------|
| `$this->load->model('catalog/product')` | **Preferred** — uses `getProductForIndex()`; same logic as storefront PLP |
| Admin `ModelCatalogProduct` | Proven in 06D; lighter registry; acceptable fallback |

**Trigger scope for offers import:**

| Field changed by offers | Must refresh index? | Rationale |
|-------------------------|---------------------|-----------|
| `price` | **YES** | Direct input to index `price` column |
| `quantity` | **Optional (skip in optimized build)** | Index stores price/special only; `in_stock` / `preorder_only` filters use `p.quantity` |
| `discount1c` | N/A in offers | Not written by offers; if changed elsewhere → separate hook |
| `status` | N/A in offers | Set by `import_1C_process.php`; affects PLP via `p.status`, not index values |
| `price2` / `price3` | N/A in offers | Not written by offers |

**Pragmatic rule for 06F:** refresh **every product that received offers UPDATE** (price + quantity together). Quantity-only refresh is redundant but harmless (idempotent). Optional 06F optimization: refresh only when `(float)$price` changed (requires pre-SELECT or compare `$existing_products` cache extended with current price).

**Secondary hook (separate charter, not blocking offers fix):**

After `import_1C.php` product loop — refresh when `import_1C_process.php` changes **category assignment** (affects category discount in index) or **status** (does not change index row values but new products need index after first offers pass). New products: index should run **after offers**, not after catalog import (price still 0 until offers).

**Do NOT in 06F:**
- Mass rebuild / cron changes / global `reindex_prices.php` automation
- Modify `oc_product` data paths
- Change filter or slider code

---

## 8. Exact insertion point

**Target file:** `catalog/controller/common/import_1C_offers.php`

**Anchor A — initialize set (before file loop, line ~21):**

```php
$price_index_refresh_ids = [];
```

**Anchor B — register ID (inside offer loop, after line 50 UPDATE):**

```php
$price_index_refresh_ids[(int)$product_id] = true;
```

**Anchor C — refresh block (after inner `foreach`, before line 57 `unset($xml)`):**

```php
if (!empty($price_index_refresh_ids)) {
    $this->load->model('catalog/product');
    foreach (array_keys($price_index_refresh_ids) as $pid) {
        $this->model_catalog_product->refreshPriceIndex((int)$pid);
    }
    echo 'Price index refreshed for ' . count($price_index_refresh_ids) . ' products<br>';
}
$price_index_refresh_ids = [];
```

**Do not place after `$itsOK = true` only** — that misses per-file error visibility and runs even when `$xml` parse failed mid-file (if partial processing occurred).

**Alternative (Option A):** replace Anchor B+C with single call immediately after line 50 — acceptable but not recommended.

---

## 9. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Cron timeout on very large offers file | Medium (future scale) | Option B + per-file logging; raise `max_execution_time` only if measured breach |
| Catalog vs admin model divergence | Low | Use catalog model; spot-check 3 SKUs post-import (price vs index group 2) |
| Partial failure in refresh block | Low | try/catch per ID in 06F; log failures; do not rollback product UPDATE |
| Session override leak (catalog model) | Low | Method already `unset`s override; verify in 06F smoke test |
| Duplicate refresh if operator also runs manual reindex | None | Idempotent |
| New SKU: offers before catalog import | Existing | Skipped by design (`continue` on unknown xml_id) |
| `discount1c` stale in index when changed outside offers | Medium (pre-existing) | Out of scope; admin edit already refreshes |
| Index refreshed for quantity-only delta | None functional | Wasted ~79 ms/SKU — optional price-change gate in 06F |

**SECURITY RISK:** none introduced by design; no new HTTP surface.

**UNKNOWN:**
- Exact `<Предложение>` count in live `offers0_1.xml`
- Whether operator uses multiple `offers0_*.xml` files per run
- Whether `discount1c` is ever fed from 1C outside admin (no capture of such path in repo)

---

## 10. Rollback strategy

| Layer | Action |
|-------|--------|
| **Code** | Restore `catalog/controller/common/import_1C_offers.php` from M9.8.9-06D backup: SHA `403c813e4eb8142e4280b222d0d464c9f2336868fff3ccf52a17b9cc80f6586d` (local: `m9.8.9-06d-work/live-capture/catalog__controller__common__import_1C_offers.php`) |
| **Data** | Hook only rebuilds index rows — rollback data via DB backup of `oc_product_price_index` if bad values (same as 06D §10) |
| **Verify rollback** | Re-run offers import without hook → index drift returns (expected); PLP filters may degrade again for unindexed SKUs |

**Pre-deploy checklist for 06F:**
1. FTP backup current live `import_1C_offers.php`
2. Deploy hook (Option B)
3. Run offers import on test/staging or single-SKU probe
4. SQL: verify `oc_product_price_index` row exists for updated `product_id` / group 2
5. PLP: price slider min/max widens on affected category

---

## Cross-reference

| Prior work | Link |
|------------|------|
| Root cause | `SITE-002-M9.8.9-06C-LIVE-PRICE-INDEX-ROOT-CAUSE.md` |
| Index rebuild proof | `SITE-002-M9.8.9-06D-CATEGORY-301-PRICE-INDEX-REBUILD.md` |
| Filter forensic | `SITE-002-M9.8.9-06-FILTER-BUG-FORENSIC-AUDIT.md` |
| Next step | **M9.8.9-06F IMPLEMENTATION PASS** |

---

**Changed files (this task):**
- `projects/ocpilot/sites/site-002/reports/SITE-002-M9.8.9-06E-1C-PRICE-INDEX-HOOK-DESIGN.md` (created)

**Git:** no commit (per task).

**UNKNOWN:** live `offers0_1.xml` offer count; multi-file offers glob usage; post-2026-06-08 operator import history.
