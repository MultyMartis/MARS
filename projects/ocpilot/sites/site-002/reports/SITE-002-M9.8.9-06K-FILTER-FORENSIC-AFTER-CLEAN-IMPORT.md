# REPORT — M9.8.9-06K FILTER FORENSIC AFTER CLEAN IMPORT

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Environment:** https://zpm.new-site.space/  
**Database:** `polygonws_zpm`  
**Context:** После product reset + `import0_1.xml` + `offers0_1.xml` (2026-06-19)  
**Mode:** Read-only forensic — **no deploy, no SQL UPDATE/DELETE, no fixes**  
**Run UTC:** 2026-06-19T09:05:00Z → 2026-06-19T09:15:00Z  

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06k-work/`  
- `forensic-results.json` — основной прогон  
- `supplement-probes.json` — price/UI combo  
- `combo-probe-results.txt` — attr-only vs attr+price  
- `stoly-filter-form.html` — live HTML формы (301)  
- `m9.8.9-06k-filter-forensic-run.py` — runner (read-only)

---

## Executive summary

После чистого импорта **атрибуты товаров присутствуют**; гипотеза «импорт не записал `oc_product_attribute`» **не подтверждается**.

Главная причина «нулевой выдачи» при использовании фильтров sidebar — **регрессия в SQL ценового фильтра**: `IFNULL(ppi.special, ppi.price)` трактует `special = 0` (типично после offers-импорта) как эффективную цену **0**, из‑за чего условие `price_from >= min` отсекает **все** товары с ненулевой базовой ценой.

JS на PLP при инициализации **записывает** `price_from` / `price_to` в поля формы (`syncFromRanges()`), поэтому **любой** клик по чекбоксу атрибута или свитчу отправляет ценовой диапазон вместе с фильтром → UI воспроизводит 0 карточек, хотя **изолированный** attr-фильтр по URL работает.

Патч **M9.8.9-06J** (numeric `attr[47]` / `attr[51]`) на live **активен** — numeric-атрибуты резолвятся корректно при запросе без price-параметров.

---

## 1. Category Statistics

### Global (post-import)

| Metric | Value |
|--------|------:|
| `oc_product` (active) | **594** |
| `oc_product_attribute` rows | **9 877** (591 distinct products) |
| `oc_product_price_index` (cg=2, active) | **594 / 594** (100%) |

### Per branch (path_id = branch root)

| Категория | category_id | profile | operator | total | with attrs | without attrs | PPI cg=2 indexed | PPI price > 0 |
|-----------|------------:|---------|----------|------:|-----------:|--------------:|-----------------:|--------------:|
| **Столы** | 301 | `301_stoly` | broken | **460** | **460** | **0** | 460 | 459 |
| **Подтоварники** | 322 | `322_podtovarniki` | broken | **11** | **11** | **0** | 11 | 11 |
| **Тележки** | 326 | `326_telezhki` | broken | **3** | **3** | **0** | 3 | 3 |
| **Моечные ванны** | 80 | `80_moechnye_vanny` | working | **119** | **116** | **3** | 119 | 115 |
| **Зонты** | 207 | `207_zonty` | working | **1** | SAFE UNKNOWN | SAFE UNKNOWN | 1 | 1 |

*Подсчёт without attrs для 207: на странице 1 карточка; детальная SQL-агрегация не приоритетна при N=1.*

### Атрибуты 47 / 51 (`filter_name` пустой)

| attribute_id | name | filter_name | effective sidebar key |
|-------------:|------|-------------|----------------------|
| 47 | Конструкция борта | **EMPTY** | `47` (numeric) |
| 51 | Конструкция полки | **EMPTY** | `51` (numeric) |

Данные в `oc_product_attribute` **есть** (пример: attr 51 «Без полки» — 57 SKU в ветке 301 по SQL-probe).

---

## 2. Sidebar Filter Inventory

Источник: live HTML `stoly-filter-form.html` + filter profiles PHP.  
Разметка: `<section class="flt__group">` (не `<fieldset>`).

### Столы (301) — ключевые группы

| filter key | filter_name (legend) | attribute_id | key type |
|------------|----------------------|-------------:|----------|
| `price_from` / `price_to` | Цена (₽) | — | range |
| `in_stock` | Только в наличии | — | switch |
| `preorder_only` | Только под заказ | — | switch |
| `only_with_price` | Только с ценой | — | switch |
| `only_discount` | Со скидкой | — | switch |
| `len_from` / `len_to` | Длина (мм) | — | range |
| `w_from` / `w_to` | Ширина (мм) | — | range |
| `h_from` / `h_to` | Высота (мм) | — | range |
| `table-top-material` | Материал столешницы | 22 | slug |
| `51` | Конструкция полки | 51 | **numeric** |
| `type-support` | Тип опоры | 33 | slug |
| `max-load` | Макс. нагрузка (до, кг) | 20 | slug |
| `available-board` | Наличие борта | 25 | slug |
| `construction` | Конструкция (secondary) | 21 | slug |
| `material-polki` | Материал полки | 112 | slug |
| `eq-legs` | Ножки | 26 | slug |
| `height-adjustment` | Регулируемость опоры | 31 | slug |
| `usilenie` | Усиление | 115 | slug |
| `side-height` | Высота борта (мм) | 18 | slug |
| `47` | Конструкция борта | 47 | **numeric** |
| `s[]` | Подкатегории | — | subcategory |

### Подтоварники (322)

PRIMARY: `51` (numeric), `max-load` (20).  
SECONDARY: `table-top-material`, `type-support`, `construction`, `qty`, `eq-legs`, `height-adjustment`, `usilenie`, `section-size`, `section-assignment`, `number-guide-levels` + dims/price/switches — та же схема имён.

### Тележки (326)

Profile: **primary/secondary attrs = пусто**.  
Sidebar: только **price**, **dims** (len/w/h), **commerce switches**. Атрибутных чекбоксов нет.

### Моечные ванны (80)

PRIMARY slugs: `shell-size` (29), `washing` (23), `available-board` (25).  
SECONDARY: `hole-for-mixer`, `47` (numeric), `side-height`, `type-support`, `eq-legs`, `construction`, `height-adjustment`, `table-top-material`, `equipmentpack`.

### Зонты (207)

Profile: PRIMARY `construction` (21).  
**Live HTML (2026-06-19):** attr-чекбоксы **не рендерятся** (1 SKU; sidebar минимален). Baseline PLP = 1 карточка.

---

## 3. HTML Filter Keys

Реальные `name` в форме `[data-filters-form]` (пример 301):

```
price_from, price_to
in_stock, preorder_only, only_with_price, only_discount
len_from, len_to, w_from, w_to, h_from, h_to
attr[table-top-material][], attr[51][], attr[type-support][], attr[max-load][],
attr[available-board][], attr[construction][], attr[material-polki][],
attr[eq-legs][], attr[height-adjustment][], attr[usilenie][],
attr[side-height][], attr[47][], s[]
```

**Поведение JS (`main.js`):**

- `bindOneRange()` → `syncFromRanges()` **на init** пишет min/max слайдера в `price_from` / `price_to`.
- `collectFormState()` включает все непустые поля → при клике по attr-checkbox URL получает и attr, и price.
- Пустые поля пропускаются; **после init price-поля не пустые**.

---

## 4. SQL Behaviour

### 4.1 Ценовой фильтр (root cause)

**Код live** (`catalog/model/catalog/product.php`, `getProducts` / `getTotalProducts`):

```php
$effective_price = "IFNULL(ppi.special, ppi.price)";
// ...
if (isset($f['price_from']) && $f['price_from'] !== '') {
    $sql .= " AND " . $effective_price . " >= '" . (float)$f['price_from'] . "'";
}
```

**После offers-импорта:** у большинства SKU `ppi.special = 0` (не NULL) при `ppi.price > 0`.

| Логика | Выражение для special=0, price=5405 | Результат |
|--------|--------------------------------------|-----------|
| **Текущая (filter)** | `IFNULL(0, 5405)` | **0** |
| **Корректная (range/sort)** | `IF(special > 0, special, price)` | **5405** |

**SQL-simulation cat 301 (path_id=301, cg=2):**

| Query | matching products |
|-------|------------------:|
| `IFNULL(special, price) BETWEEN 5405 AND 79010` | **0** |
| `IF(special > 0, special, price) BETWEEN 5405 AND 79010` | **459** |
| Products with `special=0 AND price>0` in branch | **459** |
| Products with `price=0` in branch | **1** |

**Cat 80 (моечные ванны):** из 119 active — **0** проходят `IFNULL` при `price_from=5553`; **115** проходят корректную логику.

### 4.2 Построенный SQL при UI-клике (Столы, attr + price)

Пользователь отмечает «Конструкция полки = Без полки». JS отправляет:

```
filters=attr[51][]=Без полки;price_from=5405;price_to=79010
```

Фрагмент SQL (упрощённо):

```sql
... AND EXISTS (
      SELECT 1 FROM oc_product_attribute pa
      WHERE pa.product_id = p.product_id
        AND pa.attribute_id = 51
        AND pa.text = 'Без полки'
        AND pa.language_id = 1
    )
AND IFNULL(ppi.special, ppi.price) >= 5405
AND IFNULL(ppi.special, ppi.price) <= 79010
```

**Почему 0:** EXISTS по атрибуту находит товары, но **оба** price-условия ложны при `IFNULL → 0`.

**Live probe:** attr-only → **15** карточек; attr+price → **0** карточек (`combo-probe-results.txt`).

### 4.3 Атрибутный фильтр (numeric key, 06J)

Для `attr[51][]=Без полки` (без price):

```sql
AND EXISTS (
  SELECT 1 FROM oc_product_attribute pa
  WHERE pa.product_id = p.product_id
    AND pa.attribute_id = 51
    AND (pa.text = 'Без полки')
    AND pa.language_id = 1
)
```

| Resolution | DB count (301) | Live cards |
|------------|---------------:|-----------:|
| `pa.attribute_id = 51` (06J) | 57 | **15** (paginated) |
| `ad.filter_name = '51'` (pre-06J) | **0** | would be 0 |

**06J signal:** `attr[51][]=Без полки` на 301 → 15 cards → patch **LIVE**.

### 4.4 `only_with_price`

Код выставляет `price_from = 1` при `only_with_price=1`. С `IFNULL(special, price) = 0` → **0 товаров** на всех ветках (probe: stoly/podtovarniki/telezhki/moechnye → 0 cards).

### 4.5 Тележки (326)

Любое применение фильтра через UI включает price (init sync).  
Probe: `price_from=12416;price_to=500000` → **0** cards при 3 SKU с PPI price > 0.

---

## 5. Root Cause Candidates

| # | Candidate | Status | Evidence |
|---|-----------|--------|----------|
| 1 | **`IFNULL(ppi.special, ppi.price)` в price filter** | **CONFIRMED — primary** | 459/460 stoly fail price SQL; attr+price live = 0 |
| 2 | **JS syncFromRanges on init bundles price into every filter submit** | **CONFIRMED — amplifier** | `main.js:4509`; combo probes |
| 3 | Missing attributes after import | **REJECTED** | 460/460 stoly with attrs; 9877 attr rows |
| 4 | Filter options without matching products (orphans) | **REJECTED** | `orphan_filter_values: []` all branches |
| 5 | 06J not deployed (numeric 47/51) | **REJECTED** | attr[51] live = 15 cards; DB match 57 |
| 6 | Price index not rebuilt after import | **REJECTED** | 594/594 indexed |
| 7 | `filter_name` empty on 47/51 | **Known, mitigated by 06J** | Not root of current UI symptom when price bundled |

### Гипотеза оператора (импорт / несовпадение значений)

**Не подтверждается.** `attribute_data` (значения из `oc_product_attribute` по ветке) согласованы с опциями sidebar; orphan-значений нет. Проблема в **ценовом слое SQL + UI**, не в отсутствии атрибутов.

---

## 6. Difference Between Working And Broken Categories

### Столы vs Моечные ванны

| Аспект | Столы (301) «broken» | Моечные ванны (80) «working» |
|--------|----------------------|------------------------------|
| Attr data after import | 460/460 with attrs | 116/119 with attrs |
| Attr filter **без price** | **Works** (e.g. attr[51], slugs) | **Works** (e.g. shell-size) |
| Attr filter **с price** (UI path) | **0 cards** | **0 cards** |
| Numeric keys 47/51 in UI | Yes (PRIMARY/SECONDARY) | 47 in SECONDARY |
| PPI `special=0, price>0` | 459 SKUs | 115 SKUs |

**Главное отличие восприятия, не механики:** обе ветки ломаются одинаково при price в запросе. Оператор, вероятно, тестировал **slug-primary** фильтры на ваннах (без осознанного price-слоя) или не использовал price-slider / «Только с ценой» на 80. На столах больше групп фильтров и заметнее numeric keys — симптом заметен чаще.

### Подтоварники vs Зонты

| Аспект | Подтоварники (322) | Зонты (207) |
|--------|-------------------|-------------|
| SKU count | 11 | 1 |
| Attr sidebar | Полный (51 numeric + slugs) | **Нет attr-чекбоксов** в live HTML |
| Attr-only filter | **Works** (e.g. attr[51]) | N/A (нет UI) |
| Price filter | **0** (IFNULL bug) | **0** (тот же bug) |
| Operator «works» | — | Baseline 1 card; фильтры фактически не используются |

**Главное отличие:** зонты — **дегенеративная** ветка (1 SKU, нет attr UI); подтоварники — полноценный фильтр, но UI path с price → 0.

### Тележки (326) — особый случай

Profile **без атрибутов** → единственный путь фильтрации = price/dims/switches → **всегда** попадает в price SQL → sidebar «полностью мёртв» в UI.

---

## 7. Recommended Fix

**Только рекомендации — в рамках задачи не выполнялись.**

1. **Hotfix SQL (приоритет P0):** в `getProducts()` и `getTotalProducts()` заменить  
   `IFNULL(ppi.special, ppi.price)` на  
   `IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)`  
   — зеркало уже используемой логики в `getCategoryPriceRange()` / sort (после 06G/06H).

2. **Проверить `only_with_price`:** после (1) перепроверить switch; при необходимости align с 06H semantics.

3. **JS (опционально P1):** не писать price в text inputs до user interaction, или не включать price в `collectFormState` пока пользователь не менял price-block — снижает coupling.

4. **Post-import QA:** после каждого offers-импорта — probe `price_from={min};price_to={max}` + один attr+price combo на 301 и 80.

5. **06J:** оставить; numeric attrs корректны при изолированном attr-запросе.

6. **Price index:** rebuild не требуется (100% coverage); проблема не в index absence, а в filter expression.

---

## 8. Confidence Level

| Finding | Confidence |
|---------|------------|
| Price filter broken via `IFNULL(special, price)` after fresh offers import | **Very high** — SQL simulation + live URL probes |
| UI bundles price on every checkbox via `syncFromRanges()` init | **High** — code trace + attr+price combo 0 vs attr-only 15 |
| Attributes present after import; orphan hypothesis rejected | **High** — DB counts + empty orphan list |
| 06J numeric attr path live and working (isolated) | **High** — live probe + SQL 57 vs 0 |
| Exact operator click path on each category | **Medium** — inferred from UI/JS; не записан HITL trace |
| Zonty «works» = baseline-only usage | **Medium** — no attr UI rendered; N=1 |

---

## Git / Deploy

| Action | Status |
|--------|--------|
| Git commit | **NO** (per task) |
| Deploy | **NO** (per task) |
| Files changed | Report + evidence scripts only |

---

## UNKNOWN

- Точный HITL сценарий оператора по каждой ветке (какие именно чекбоксы / слайдеры нажимались).
- Полный охват остальных веток нейтрального оборудования кроме пяти branch profiles (79 hub не развёрнут в полный probe).
- Совпадение live `product.php` с repo capture `m9.8.9-06j-work` — inferred from behavior, не byte-compare в этом прогоне.

---

*Forensic only. No remediation applied.*
