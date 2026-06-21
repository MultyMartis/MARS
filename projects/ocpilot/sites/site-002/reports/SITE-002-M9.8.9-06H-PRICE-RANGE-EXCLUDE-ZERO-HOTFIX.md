# REPORT — M9.8.9-06H PRICE RANGE EXCLUDE ZERO HOTFIX

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Date:** 2026-06-19  
**Mode:** Minimal hotfix + deploy + QA  
**Basis:** `SITE-002-M9.8.9-06G-PRICE-FILTER-ZERO-PRICE-FORENSIC`

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06h-work/`  
**Deploy runner:** `m9.8.9-06h-deploy-run.py`  
**QA runner:** `m9.8.9-06h-qa-run.py`

---

## 1. Root Cause

После M9.8.9-06F (`refreshPriceIndex()` после offers) товары с `price = 0` («Цена по запросу») корректно попадают в `oc_product_price_index`, но **`getCategoryPriceRange()`** агрегировал `MIN()` / `MAX()` по **всем** строкам index без исключения `effective_price <= 0`.

`effective_price` в этом методе уже определён как:

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

Нулевые SKU (144, 145, 1057, 1058, 3071) сдвигали `min_price` sidebar-фильтра на **0** в категориях **301 (Столы)** и **80 (Моечные ванны)**.

**Не затронуто (по scope):** `import_1C_offers.php`, cron, `category.php`, PDP/PLP карточки, schema `product_price_index`, `refreshPriceIndex()`.

---

## 2. Backup

| Item | Path |
|------|------|
| Pre-deploy backup | `projects/ocpilot/sites/site-002/backups/product.php.pre-m9.8.9-06h-price-range-exclude-zero.bak` |
| Live capture (pre-deploy) | `projects/ocpilot/sites/site-002/reports/m9.8.9-06h-work/live-capture/catalog__model__catalog__product.php` |
| Patched local copy | `projects/ocpilot/sites/site-002/reports/m9.8.9-06h-work/catalog__model__catalog__product.php.patched` |
| Manifest | `projects/ocpilot/sites/site-002/reports/m9.8.9-06h-work/manifest-20260619-064138.json` |

FTP RETR выполнен до STOR. Backup byte-identical к live capture.

---

## 3. Changed SQL

**File:** `catalog/model/catalog/product.php`  
**Method:** `getCategoryPriceRange()`  
**Diff:** одна строка в `$sql .=` блоке WHERE.

**Было:**

```php
$sql .= " AND ppi.customer_group_id = '" . (int)$customer_group_id . "'
          AND p.status = '1'
          AND p.date_available <= NOW()
          AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'";
```

**Стало:**

```php
$sql .= " AND ppi.customer_group_id = '" . (int)$customer_group_id . "'
          AND p.status = '1'
          AND p.date_available <= NOW()
          AND p2s.store_id = '" . (int)$this->config->get('config_store_id') . "'
          AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0";
```

**SQL-эквивалент (фрагмент WHERE после fix):**

```sql
AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0
```

Товары с `effective_price = 0` остаются в каталоге и index; исключаются **только** из расчёта `min_price` / `max_price` фильтра.

---

## 4. Before / After

| Категория | До (PLP `placeholder_from`) | После (PLP + SQL) |
|-----------|------------------------------|-------------------|
| **301 Столы** | **0** → 72630 | **5405** → 72630 |
| **80 Моечные ванны** | **0** → 75071 | **5553** → 75071 |

Pre-deploy PLP (2026-06-19 ~06:40 UTC): `placeholder_from = 0` на обеих ветках.  
Post-deploy PLP (2026-06-19 ~06:42 UTC): `5405` / `5553`.

---

## 5. QA

**Runner:** `qa-results.json` — **`all_pass: true`**

| # | Check | Result |
|---|-------|--------|
| 1 | Столы (301): диапазон не начинается с 0 | **PASS** — SQL min 5405; PLP `placeholder_from` 5405 |
| 2 | Моечные ванны (80): диапазон не начинается с 0 | **PASS** — SQL min 5553; PLP `placeholder_from` 5553 |
| 3 | PDP 3071 — «По запросу» | **PASS** |
| 4 | PDP 144, 145, 1057, 1058 — «По запросу» | **PASS** |
| 5 | Zero-price SKU остаются в каталоге | **PASS** — `oc_product.price = 0`, `status = 1`, index rows сохранены; 3071 active в поддереве 301 |
| 6 | `only_with_price` | **PASS** — `/stoly/?only_with_price=1` отрабатывает, «По запросу» в листинге не показывается |

**Deploy verify:** `deploy_ok: true` — post-deploy FTP SHA совпадает с patched local.

---

## 6. Rollback

1. FTP STOR `catalog/model/catalog/product.php` from backup:  
   `backups/product.php.pre-m9.8.9-06h-price-range-exclude-zero.bak`
2. Verify SHA256 = `4dea62375e261bfb2fea986511405f34b28b5c3d4a98c1bbda8520bc31094659`
3. Ожидаемый регресс: PLP min снова **0** на ветках с zero-price SKU

Alternative rollback source: `reports/m9.8.9-06h-work/live-capture/catalog__model__catalog__product.php` (identical pre-deploy SHA).

---

## 7. SHA256

| Artifact | SHA256 | Size (bytes) |
|----------|--------|--------------|
| **Pre-deploy (live FTP)** | `4dea62375e261bfb2fea986511405f34b28b5c3d4a98c1bbda8520bc31094659` | 58556 |
| **Patched (local + live post-deploy)** | `f53f6b3f0aad776baa28490e340471beb871e55673b0377faf0c2c5c066a844c` | 58650 |
| **Post-deploy verify (live FTP)** | `f53f6b3f0aad776baa28490e340471beb871e55673b0377faf0c2c5c066a844c` | 58650 |

---

## Git / Changes

| Item | Status |
|------|--------|
| Live deploy | **YES** — `catalog/model/catalog/product.php` |
| Git commit | **NO** |
| Git push | **NO** |

**Created artifacts (workspace):**

- `reports/SITE-002-M9.8.9-06H-PRICE-RANGE-EXCLUDE-ZERO-HOTFIX.md` (this file)
- `reports/m9.8.9-06h-work/` (manifest, capture, patched copy, deploy/QA scripts, `deploy-result.json`, `qa-results.json`)
- `backups/product.php.pre-m9.8.9-06h-price-range-exclude-zero.bak`

**SECURITY NOTE:** deploy/QA runners contain FTP/DB credentials by pattern of prior M9.8.9 tasks — do not commit to public repo without redaction.
