# REPORT — M9.8.9-06J NUMERIC ATTRIBUTE FILTER HOTFIX

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Live URL:** https://zpm.new-site.space/  
**Deploy date:** 2026-06-19  
**Prior forensic:** M9.8.9-06I FILTER ZERO RESULTS FORENSIC  

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06j-work/`  
**Manifest:** `manifest-20260619-071701.json`  
**QA:** `qa-results.json` (`all_pass: true`)

---

## 1. Root Cause

Часть фильтров в sidebar рендерится с **numeric key** в HTML (`attr[51][]`, `attr[47][]`), когда у атрибута в `oc_attribute_description` пустой `filter_name`.

SQL в `getProducts()` и `getTotalProducts()` всегда сопоставлял ключ с `ad.filter_name`:

```sql
AND ad.filter_name = '51'
```

Для attrs **47** и **51** `filter_name` в БД **пустой** → условие никогда не выполняется → **0 товаров**.

Slug-фильтры (`shell-size`, `construction`, `table-top-material` и т.д.) имеют заполненный `filter_name` и работали корректно.

---

## 2. Files Changed

| Location | Action |
|----------|--------|
| **Live FTP** `catalog/model/catalog/product.php` | **PATCHED** — numeric/slug branch в двух местах |
| `backups/product.php.pre-m9.8.9-06j-numeric-attr-filter.bak` | pre-deploy backup |
| `reports/m9.8.9-06j-work/live-capture/catalog__model__catalog__product.php` | live FTP capture |
| `reports/m9.8.9-06j-work/catalog__model__catalog__product.php.patched` | local patched artifact |
| `reports/m9.8.9-06j-work/m9.8.9-06j-deploy-run.py` | deploy runner |
| `reports/m9.8.9-06j-work/m9.8.9-06j-qa-run.py` | QA runner |

**SHA256:**

| Artifact | SHA256 |
|----------|--------|
| Pre-deploy (live) | `f53f6b3f0aad776baa28490e340471beb871e55673b0377faf0c2c5c066a844c` |
| Post-deploy (patched) | `2e3faeed496d9b48dcce7c7d13ba4659536a7ac732ca88504cfe24b162584d9f` |
| FTP verify after deploy | `2e3faeed496d9b48dcce7c7d13ba4659536a7ac732ca88504cfe24b162584d9f` ✓ |

**Не затронуто:** price index, 06F, 06H, cron, 1C, PDP, category layout, filter UI.

---

## 3. SQL Before

Единая ветка для всех ключей (`getProducts` и `getTotalProducts`):

```sql
AND EXISTS (
    SELECT 1 FROM oc_product_attribute pa
    LEFT JOIN oc_attribute_description ad ON (pa.attribute_id = ad.attribute_id)
    WHERE pa.product_id = p.product_id
    AND ad.filter_name = '51'
    AND (pa.text = 'Без полки')
    AND ad.language_id = '1'
)
```

При `attr[51][]` ключ `'51'` искался как `filter_name` → **0 rows** (в БД `filter_name` пустой).

---

## 4. SQL After

Точечная ветка по типу ключа:

```php
if (is_numeric($attr_slug)) {
    // pa.attribute_id = (int)$attr_slug
} else {
    // ad.filter_name = $attr_slug  (без изменений для slug)
}
```

**Numeric key** (`attr[51][]`):

```sql
AND EXISTS (
    SELECT 1 FROM oc_product_attribute pa
    WHERE pa.product_id = p.product_id
    AND pa.attribute_id = '51'
    AND (pa.text = 'Без полки')
    AND pa.language_id = '1'
)
```

**Slug key** (`attr[construction][]`) — **без изменений**:

```sql
AND EXISTS (
    SELECT 1 FROM oc_product_attribute pa
    LEFT JOIN oc_attribute_description ad ON (pa.attribute_id = ad.attribute_id)
    WHERE pa.product_id = p.product_id
    AND ad.filter_name = 'construction'
    AND (pa.text = 'сварная (неразборная)')
    AND ad.language_id = '1'
)
```

---

## 5. QA

Live HTTP QA после деплоя (`2026-06-19T07:17:58Z`):

| Probe | Category | Filter | Cards (before 06J) | Cards (after 06J) | Pass |
|-------|----------|--------|--------------------|-------------------|------|
| `stoly_baseline` | Столы 301 | — | 15 | **15** | ✓ |
| **`stoly_attr51`** | **Столы 301** | **`attr[51][]=Без полки`** | **0** | **15** | ✓ |
| `podtovarniki_baseline` | Подтоварники 322 | — | 11 | **11** | ✓ |
| **`podtovarniki_attr51`** | **Подтоварники 322** | **`attr[51][]=600х400х300`** | **0** | **1** | ✓ |

**PRIMARY fix подтверждён:** numeric `attr[51]` на Столах и Подтоварниках возвращает товары.

---

## 6. Regression

| Probe | Category | Slug filter | Cards (after 06J) | Pass |
|-------|----------|-------------|-------------------|------|
| `stoly_construction_slug` | Столы | `attr[construction][]` | 15 | ✓ |
| `sinks_shell_size` | Моечные ванны | `attr[shell-size][]` | 2 | ✓ |
| `zonty_construction` | Зонты вытяжные | `attr[construction][]` | 1 | ✓ |

Slug-фильтры **не регрессировали**.

---

## 7. Rollback

1. Восстановить файл на FTP из backup:
   - `projects/ocpilot/sites/site-002/backups/product.php.pre-m9.8.9-06j-numeric-attr-filter.bak`
   - → `catalog/model/catalog/product.php`
2. Ожидаемый SHA256 после rollback: `f53f6b3f0aad776baa28490e340471beb871e55673b0377faf0c2c5c066a844c`
3. Повторить QA: `attr[51][]` на Столах снова даст **0** карточек (подтверждение отката).

**Deploy runner** (повторный upload backup): адаптировать `m9.8.9-06j-deploy-run.py`, указав backup как источник вместо patched.

---

**Deploy status:** `deploy_ok: true`  
**QA status:** `all_pass: true`
