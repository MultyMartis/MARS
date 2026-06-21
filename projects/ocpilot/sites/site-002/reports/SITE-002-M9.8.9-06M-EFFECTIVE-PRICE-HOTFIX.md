# REPORT — M9.8.9-06M EFFECTIVE PRICE HOTFIX

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Deploy date:** 2026-06-19  
**Basis:** M9.8.9-06K (filter forensic), M9.8.9-06L (safety audit)

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06m-work/`  
**Manifest:** `manifest-20260619-100258.json`  
**QA:** `qa-results.json`

---

## 1. Changes Applied

### Root cause

`IFNULL(ppi.special, ppi.price)` трактует `special = 0` (типично после offers-импорта 1C) как эффективную цену **0**. Условия `price_from >= N` и `only_with_price` (принудительный `price_from = 1`) отсекали товары с ненулевой базовой ценой.

### File changed (live FTP only)

| Location | Action |
|----------|--------|
| **Live FTP** `catalog/model/catalog/product.php` | **PATCHED** — 3 замены `IFNULL` → `IF(special > 0, …)` |
| `backups/product.php.pre-m9.8.9-06m-effective-price.bak` | pre-deploy backup |
| `reports/m9.8.9-06m-work/live-capture/catalog__model__catalog__product.php` | FTP capture before patch |
| `reports/m9.8.9-06m-work/catalog__model__catalog__product.php.patched` | local patched artifact |

### SQL expression (3 точки)

**Было:**

```sql
IFNULL(ppi.special, ppi.price)
```

**Стало:**

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

| # | Method | Location | Purpose |
|---|--------|----------|---------|
| 1 | `getProducts()` | `$effective_price` (~219) | `price_from` / `price_to` / `only_with_price` WHERE |
| 2 | `getProducts()` | `ORDER BY` (~286) | сортировка `sort=p.price` |
| 3 | `getTotalProducts()` | `$effective_price` (~641) | тот же price-filter для счётчика |

### Не затронуто (подтверждено)

- `refreshPriceIndex()` — без изменений  
- `getProduct()` — без изменений  
- `getCategoryPriceRange()` — уже использовал корректную `IF(...)` с M9.8.9-06H  
- PDP price logic, cart, checkout, import 1C, customer groups, `discount1c`, `price2`, `price3`  
- M9.8.9-06J numeric attribute filter branch — сохранён

---

## 2. Deploy Verification

| Step | Status |
|------|--------|
| FTP capture (pre-deploy) | ✓ |
| Backup `product.php.pre-m9.8.9-06m-effective-price.bak` | ✓ |
| Manifest `manifest-pre-20260619-100258.json` + `manifest-20260619-100258.json` | ✓ |
| Upload only `catalog/model/catalog/product.php` | ✓ |
| SHA256 verify on live | ✓ `deploy_ok: true` |

| Artifact | SHA256 |
|----------|--------|
| Pre-deploy (M9.8.9-06J baseline) | `2e3faeed496d9b48dcce7c7d13ba4659536a7ac732ca88504cfe24b162584d9f` |
| Post-deploy (patched) | `66ad19e4e0211973214d72dcb8aef6af3cd4a9be2e343b5e5e9ecd27e7168d00` |
| FTP verify after deploy | `66ad19e4e0211973214d72dcb8aef6af3cd4a9be2e343b5e5e9ecd27e7168d00` ✓ |

**Replacements:** 3 (exactly as audited in M9.8.9-06L)

---

## 3. QA Results

Live HTTP QA (`2026-06-19T10:05:27Z`). Источник: `qa-results.json`.

### Price-hotfix scope (primary)

| Category | `only_with_price` | sort ASC | sort DESC | Hotfix pass |
|----------|-------------------|----------|-----------|-------------|
| Столы (301) | 15 ✓ | 14 ✓ monotonic | 15 ✓ monotonic | ✓ |
| Подтоварники (322) | 11 ✓ | 11 ✓ | 11 ✓ | ✓ |
| Тележки (326) | 3 ✓ | 3 ✓ | 3 ✓ | ✓ |
| Моечные ванны (80) | 15 ✓ | 11 ✓ | 15 ✓ | ✓ |
| Зонты (207) | 1 ✓ | 1 ✓ | 1 ✓ | ✓ |

### Attribute filter probes

| Category | Filter | Cards | Pass | Note |
|----------|--------|-------|------|------|
| Столы | `attr[51][]=Без полки` | 15 | ✓ | |
| Подтоварники | `attr[51][]=600х400х300` | 1 | ✓ | |
| Тележки | baseline (нет attr sidebar) | 3 | ✓ | per M9.8.9-06L |
| Моечные ванны | `attr[shell-size][]=1100х500х400` | 2 | ✓ | |
| Зонты | `attr[construction][]=разборная` | 0 | ✗ | **pre-existing data gap** — 1 SKU, `attribute_data_db` пуст в 06K forensic; не регрессия 06M |

### Key combined probe (primary fix validation)

| Probe | Before (06K) | After (06M) |
|-------|--------------|-------------|
| Столы `attr[51][]=Без полки;only_with_price=1` | **0** cards | **15** cards ✓ |
| Столы `price_from=5405` | **0** cards | *(not re-probed; same root cause fixed)* |

### QA verdict

- **Hotfix objective (effective price in filter/sort/count): PASS** — все 5 категорий, `only_with_price` и сортировка по цене работают.  
- **Full checklist `all_pass`:** `false` из‑за зонтов attr=0 — **вне scope hotfix** (каталожные данные / отсутствие attr на единственном SKU).

---

## 4. Before / After

### Expression alignment

| Area | Before (06J live) | After (06M) |
|------|-------------------|-------------|
| `getProducts` price filter | `IFNULL(special, price)` | `IF(special > 0, special, price)` |
| `getProducts` ORDER BY `p.price` | `IFNULL(special, price)` | `IF(special > 0, special, price)` |
| `getTotalProducts` price filter | `IFNULL(special, price)` | `IF(special > 0, special, price)` |
| `getCategoryPriceRange` | уже `IF(special > 0, …)` | без изменений |
| `getProduct()` / PDP | `getProduct()` chain | без изменений |

### Observable behaviour (representative)

| Scenario | Before | After |
|----------|--------|-------|
| Столы `only_with_price=1` | 0 (06K) | 15 |
| Столы attr + `only_with_price` | 0 (06K) | 15 |
| Зонты `only_with_price=1` | 0 (06K) | 1 |
| Тележки `only_with_price=1` | 0 (06K) | 3 |
| Сортировка «сначала дешевле» (столы) | special=0 → неверный порядок / обнуление | монотонный ASC по реальной цене |

---

## 5. Rollback

1. Восстановить из backup:
   - Local: `projects/ocpilot/sites/site-002/backups/product.php.pre-m9.8.9-06m-effective-price.bak`
   - SHA256 rollback: `2e3faeed496d9b48dcce7c7d13ba4659536a7ac732ca88504cfe24b162584d9f`
2. Загрузить на FTP: `catalog/model/catalog/product.php`
3. Проверить SHA256 на live = rollback hash
4. Перепроверить `only_with_price` на столах (ожидается регрессия к 0)

**Runner:** `reports/m9.8.9-06m-work/m9.8.9-06m-deploy-run.py` (invert: upload backup bytes)

---

## Artifacts

| File | Purpose |
|------|---------|
| `m9.8.9-06m-deploy-run.py` | capture → backup → patch → deploy → SHA verify |
| `m9.8.9-06m-qa-run.py` | live QA probes |
| `deploy-result.json` | deploy outcome |
| `qa-results.json` | QA outcome |
| `manifest-20260619-100258.json` | full deploy manifest |

**Git:** NO commit, NO push (per task charter).

**UNKNOWN:** точное значение атрибута «Конструкция» у единственного SKU в категории «Зонты» на live — требует DB probe для восстановления attr-фильтра (не блокер hotfix).
