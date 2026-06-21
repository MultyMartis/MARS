# REPORT — M9.8.9-06L PRICE EFFECTIVE LOGIC SAFETY AUDIT

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Date:** 2026-06-19  
**Mode:** Read-only safety audit — **no deploy, no SQL UPDATE, no code changes, no commit/push**  
**Basis:** M9.8.9-06K (filter forensic after clean import), live captures in `reports/m9.8.9-06j-work/live-capture/`

**Evidence sources (in-repo):**

- `catalog/model/catalog/product.php` — live capture: `reports/m9.8.9-06j-work/live-capture/catalog__model__catalog__product.php`
- `admin/model/catalog/product.php` — live capture: `reports/m9.8.9-06d-work/live-capture/admin__model__catalog__product.php`
- `catalog/controller/common/import_1C_offers.php` — patched reference: `reports/m9.8.9-06f-work/import_1C_offers.php.patched`
- PLP card commerce: `category-v2.1-list-card-commerce-work/product_results.php`
- PDP price pattern: `backups/stable-baseline-2026-06-09/catalog/controller/product/product.php`
- DB probes: `reports/m9.8.9-06k-work/db-price-probe.py`, `forensic-results.json`

---

## Executive answers (for hotfix charter)

| # | Question | Answer |
|---|----------|--------|
| 1 | Безопасна ли замена в `getProducts` / `getTotalProducts`? | **ДА** — выравнивает SQL с уже принятой семантикой `getCategoryPriceRange()`, `getProduct()` и UI |
| 2 | Менять только price-filter WHERE? | **НЕТ** — тот же `$effective_price` используется и для `only_with_price`; отдельный ORDER BY тоже на `IFNULL` |
| 3 | Менять сортировку по цене? | **ДА** — `ORDER BY IFNULL(ppi.special, ppi.price)` имеет тот же баг |
| 4 | Менять `only_with_price`? | **Отдельный код не нужен** — switch только выставляет `price_from = 1`; фильтрация идёт через тот же `$effective_price` |
| 5 | Трогать корзину / PDP / карточки? | **НЕТ** — они не читают `product_price_index` для отображения цены |
| 6 | Минимальный безопасный hotfix? | Один файл: `catalog/model/catalog/product.php` — унифицировать `effective_price` + `ORDER BY` под формулу `getCategoryPriceRange()` |

---

## 1. IFNULL usage inventory

### 1.1 Единственный live-файл с `IFNULL(ppi.special, ppi.price)`

**Файл:** `catalog/model/catalog/product.php` (live capture, authority M9.8.9-06J)

| Location | Method | Usage | Lines (capture) |
|----------|--------|-------|-----------------|
| A | `getProducts()` | `$effective_price = "IFNULL(ppi.special, ppi.price)"` → `price_from` / `price_to` WHERE | ~219–235 |
| B | `getProducts()` | `ORDER BY IFNULL(ppi.special, ppi.price)` при `sort=p.price` | ~286 |
| C | `getTotalProducts()` | `$effective_price` — дубликат блока A | ~641–657 |

**Итого:** 3 SQL-точки в **одном** файле. Других вхождений `IFNULL(ppi.special, ppi.price)` в SITE-002 captures **нет**.

### 1.2 Соседняя логика в том же файле — уже «правильная»

| Location | Method | Expression |
|----------|--------|------------|
| `getCategoryPriceRange()` | MIN/MAX агрегаты | `IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)` |
| `getCategoryPriceRange()` | WHERE (после M9.8.9-06H) | `... AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0` |
| `getProducts()` / `getTotalProducts()` | `only_discount` | `AND ppi.special > 0` |

**Вывод:** программист **уже** закодировал корректную effective-price семантику для слайдера (06G/06H), но **не перенёс** её в фильтр и сортировку. Это выглядит как **незавершённый рефакторинг / oversight**, а не осознанная бизнес-логика «special=0 = бесплатно».

### 1.3 Другие упоминания `ppi.special` / `ppi.price` / `product_price_index`

| Symbol | Where | Role |
|--------|-------|------|
| `LEFT JOIN oc_product_price_index ppi` | `getProducts`, `getTotalProducts` | JOIN по `customer_group_id` (guest → 2) |
| `ppi.special > 0` | filter `only_discount` | Явно: скидка есть только если special > 0 |
| `ppi.price`, `ppi.special` | `refreshPriceIndex` INSERT | Денормализованный кэш для PLP SQL |
| `product_price_index` | `getCategoryPriceRange` | Агрегация min/max для sidebar |

**Корзина, checkout, PDP, карточки:** `product_price_index` **не используют** (см. §2–3).

### 1.4 История появления `IFNULL`

Паттерн присутствует с введения `product_price_index` (m8.3-wave2 captures, июнь 2026). С тех пор `getCategoryPriceRange` писался с `IF(special > 0, ...)`, а filter/sort — с `IFNULL`. **Нет** комментариев или docs, объясняющих намеренное различие.

---

## 2. Price display logic

### 2.1 Источник истины для отображения

**PLP и PDP** берут цену из `ModelCatalogProduct::getProduct($product_id)` — **не** из `ppi`.

Цепочка PLP:

```
getProducts() SQL → product_id list
  → foreach: getProduct(product_id)   // полный PHP-расчёт
  → product_results.php → карточка
```

### 2.2 Алгоритм `getProduct()` (live capture)

**Базовая цена (`price` в массиве результата):**

| `customer_group_id` | Источник |
|--------------------|----------|
| 3 | `p.price2` (дилер) |
| 4 | `p.price3` (опт) |
| иначе | `p.price` |
| override | `product_discount` qty=1, если есть |

**Спеццена (`special` в массиве):**

1. `discount1c > 0` → процент от `final_price`
2. иначе `product_special.price > 0`
3. иначе `MAX(category.discount) > 0` → процент
4. иначе **`$final_special = false`** (не 0)

Ключевая проверка в PHP (и PDP, и index helper):

```php
elseif (isset($query->row['special']) && (float)$query->row['special'] > 0) {
    $final_special = (float)$query->row['special'];
}
```

**«Нет скидки» = `false`, не `0`.**

### 2.3 PLP карточка (`product_results.php`)

```php
if ($result['special'] !== false && (float)$result['special'] > 0) {
    // показать зачёркнутую цену + скидку
} else {
    $special = false;
}
if ($pricecalc == 0) {
    $canCart = false;
    $price = 'По запросу';
}
```

### 2.4 PDP (`product.php` pattern, stable capture)

```php
if ($product_info['special'] !== false && (float)$product_info['special'] > 0) {
    // special price display
}
if ($pricecalc == 0) {
    $data['price'] = 'По запросу';
    $canCart = false;
}
```

### 2.5 Расхождение display vs filter SQL

| Слой | «Нет скидки» | Effective price при base=5405 |
|------|--------------|-------------------------------|
| `getProduct()` / UI | `special === false` | **5405** |
| `getCategoryPriceRange()` | `special` NULL или ≤0 | **5405** |
| Filter/sort `IFNULL` | `special = 0` в index | **0** ← баг |

**Вывод:** замена в фильтре **согласует** SQL с тем, что пользователь уже видит на карточке.

---

## 3. Cart / checkout logic

### 3.1 Что проверено

В SITE-002 repo **нет** live-capture `system/library/cart/cart.php`. Анализ по:

- OpenCart standard pattern (cart loads products via catalog model)
- PLP/PDP commerce flags (`$canCart`, `$pricecalc`)
- Отсутствие `product_price_index` вне `catalog/model/catalog/product.php`

### 3.2 Поведение корзины (documented + standard OC)

| Аспект | Механизм | Зависит от `IFNULL(ppi...)`? |
|--------|----------|------------------------------|
| Цена в корзине | `getProduct()` / cart product array | **НЕТ** |
| «По запросу» | `$pricecalc == 0` → `$canCart = false` | **НЕТ** |
| Группа покупателя | `$this->customer->getGroupId()` в `getProduct()` | **НЕТ** (отдельно от PPI JOIN в листинге) |
| Checkout totals | Cart session + tax/currency | **НЕТ** |

### 3.3 Customer groups в корзине vs PLP filter

- **Отображение / корзина:** реальная группа клиента (2/3/4) через `getProduct()`.
- **PLP SQL filter:** `getProducts()` нормализует гостя к `customer_group_id = 2` (если не 3/4). Дилеры/оптовики на PLP фильтруются по **своей** PPI-строке.

Hotfix `effective_price` **не меняет** эту схему — только формулу внутри уже существующего JOIN.

**Вывод:** корзину и checkout **не трогать**.

---

## 4. Price index logic

### 4.1 Таблица `oc_product_price_index`

Кастомная денормализация для быстрого PLP SQL (фильтр, сортировка, slider).  
**Не** участвует в PDP/cart price rendering.

### 4.2 `refreshPriceIndex()` — два пути

| Path | Caller | INSERT `special` |
|------|--------|------------------|
| **Catalog model** | `import_1C_offers.php` (06F): `$this->load->model('catalog/product')` | `special = '" . (... ? float : "NULL") . "'` → при отсутствии скидки буквально **`special = 'NULL'`** (строка в кавычках) |
| **Admin model** | Admin product save | `special = " . (... ? float : NULL)` → корректный SQL `NULL` |

**Риск данных (SAFE UNKNOWN точная доля без live SQL):** строка `'NULL'` в DECIMAL-колонке MySQL может стать **`0.0000`**, что усиливает баг `IFNULL(special, price) → 0`.

Подтверждённый факт из 06K: после clean import + offers, в ветке 301 (cg=2) **459/460** SKU имеют `ppi.special = 0` при `ppi.price > 0`.

### 4.3 Расчёт при refresh (catalog `getProductForIndex`)

Идентичен `getProduct()`:

- `price2` / `price3` / `price` по группе
- `discount1c`, `product_special`, category discount
- `final_special = false` когда скидки нет

**Запись в index:**

```php
price = (float)$product_info['price'],
special = '" . ($product_info['special'] !== false ? (float)$product_info['special'] : "NULL") . "'
```

| Сценарий | `final_special` | В index (catalog path) |
|----------|-----------------|------------------------|
| Нет скидки | `false` | `'NULL'` string → вероятно **0** в DB |
| Скидка 15% | число > 0 | корректное число |
| Скидка 100% / clamp | `0` | **`0`** (`0 !== false` в PHP) |
| Base price 0 | `price=0` | `price=0`, special по логике выше |

### 4.4 Когда `special = 0` — штатное значение?

| Контекст | `special = 0` штатно? |
|----------|----------------------|
| `getProduct()` return | **НЕТ** — используется `false` |
| UI «нет скидки» | **НЕТ** — проверка `> 0` |
| `only_discount` filter | **НЕТ** — требует `special > 0` |
| `getCategoryPriceRange` | **НЕТ** — `special > 0` для выбора special |
| `product_price_index` после offers | **де-факто да** (данные), но это **артефакт записи**, не бизнес-смысл |

**Вывод:** `special = 0` в index = **«скидки нет»** по смыслу домена, но **не** «эффективная цена = 0». `IFNULL` ошибочно трактует 0 как валидную special-цену.

---

## 5. Customer group logic

### 5.1 Группы в фильтрации / index

```php
$customer_group_id = (int)$this->config->get('config_customer_group_id');
if (!in_array($customer_group_id, [3, 4])) {
    $customer_group_id = 2;  // guest / default retail
}
```

| Group | Назначение (по коду) | PPI `price` source |
|-------|----------------------|-------------------|
| 2 | Розница / гость | `oc_product.price` (+ discounts) |
| 3 | Дилер | `oc_product.price2` |
| 4 | Оптовик | `oc_product.price3` |

`discount1c`, category discount, `product_special` применяются поверх base в `getProductForIndex`.

### 5.2 Влияние hotfix на группы

Формула `IF(ppi.special > 0, ppi.special, ppi.price)` **группо-нейтральна** — работает на строке PPI для текущего `customer_group_id`.  
Менять логику групп **не требуется**.

### 5.3 `price2`, `price3`, `discount1c`

Уже **вшиты** в `ppi.price` / `ppi.special` при `refreshPriceIndex()`.  
Фильтр читает **index**, не сырые колонки `oc_product`. Hotfix не затрагивает импорт 1С и расчёт index.

---

## 6. Risk analysis

### 6.1 Риски замены `IFNULL` → `IF(special > 0, ...)`

| Risk | Severity | Assessment |
|------|----------|------------|
| Сломать отображение цен | **None** | Display не использует эту формулу |
| Сломать корзину / checkout | **None** | Не зависят от PPI SQL |
| Исключить товары со скидкой | **Low** | При `special > 0` формулы эквивалентны |
| Исключить «По запросу» (price=0) | **Low / desired** | `IF(0>0,0,0)=0`; `only_with_price` уже требует `>=1` |
| Регрессия для `special IS NULL` | **None** | `NULL > 0` → false → fallback to `price` (как `IFNULL`) |
| Регрессия для реальной special=0 (100% off) | **Edge** | Оба варианта дают 0; товар и так «бесплатный» — **редкий кейс** |

### 6.2 Риски **не** делать hotfix

| Symptom | Impact |
|---------|--------|
| Любой UI-фильтр с price (JS init sync) | **0 карточек** при attr+price (06K confirmed) |
| `only_with_price` | **0 карточек** на всех ветках |
| Тележки (326) | Sidebar **полностью мёртв** (только price/dims) |
| Сортировка «дешевле» | Товары с `special=0` всплывают **первыми** (effective=0) |

### 6.3 Был ли `IFNULL` намеренным?

**Аргументы против намеренности:**

1. Тот же автор/файл использует **правильную** формулу в `getCategoryPriceRange`.
2. `only_discount` уже трактует скидку как `special > 0`.
3. `getProduct()` трактует отсутствие скидки как `false`, не `0`.
4. M9.8.9-06H **намеренно не трогал** filter/sort (scope = slider only) — баг остался **известным хвостом**, не продуктовым решением.

**Аргументы «за» намеренность:** **не найдены** в коде, комментариях или docs.

**Вердикт:** `IFNULL` — **ошибка программиста** (классическая путаница NULL vs 0), усугублённая записью `special='NULL'` в catalog `refreshPriceIndex`.

### 6.4 Эквивалентность предлагаемых формул

Для filter/sort достаточно:

```sql
IF(ppi.special > 0, ppi.special, ppi.price)
```

Расширенная форма из `getCategoryPriceRange` (рекомендуется для **единообразия**):

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

Для DECIMAL-полей с `0` вместо NULL обе формы **эквивалентны**.

---

## 7. Safe hotfix recommendation

### 7.1 Минимальный scope (P0)

**Файл:** `catalog/model/catalog/product.php` only.

**Change 1 — `$effective_price` (2 места):**

```php
// было
$effective_price = "IFNULL(ppi.special, ppi.price)";

// стало (зеркало getCategoryPriceRange)
$effective_price = "IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)";
```

Применить в:

- `getProducts()` → блок `filter_custom` (~219)
- `getTotalProducts()` → блок `filter_custom` (~641)

Затрагивает автоматически:

- `price_from` / `price_to`
- `only_with_price` (через принудительный `price_from = 1`)

**Change 2 — сортировка по цене:**

```php
// было
$sql .= " ORDER BY IFNULL(ppi.special, ppi.price)";

// стало
$sql .= " ORDER BY IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)";
```

### 7.2 Что **не** входит в минимальный hotfix

| Item | Why defer |
|------|-----------|
| `refreshPriceIndex()` catalog INSERT | Data-quality; filter fix работает **без** reindex |
| `import_1C_offers.php` | Не связан с filter expression |
| `getCategoryPriceRange()` | Уже исправлен в 06H |
| PDP / PLP templates / `product_results.php` | Не затронуты |
| Cart / checkout | Не затронуты |
| JS `syncFromRanges()` | Улучшение UX (P1), не blocker после SQL fix |

### 7.3 Post-hotfix QA (read-only probes)

1. Cat 301: `filters=price_from=5405;price_to=79010` → expect **~459** cards (06K SQL baseline).
2. Cat 301: `attr[51][]=Без полки` + price range → expect **>0** (не 0).
3. `only_with_price=1` → expect **>0** priced SKUs.
4. Sort `p.price ASC` → первый товар не должен иметь commercial price = 0 при наличии priced SKU.
5. PDP spot-check: цена на карточке **не изменилась** (regression guard).

### 7.4 Опциональный follow-up (отдельная задача)

1. **Catalog `refreshPriceIndex`:** писать SQL `NULL` без кавычек (как admin model); не писать `special=0` когда `final_special === false`.
2. **Reindex** после fix INSERT — опционально, для чистоты данных, **не обязателен** для filter hotfix.

---

## 8. Do-not-touch areas

| Area | Reason |
|------|--------|
| `catalog/controller/product/product.php` (PDP) | Цена из `getProduct()`, не PPI |
| `catalog/controller/product/product_results.php` / card partials | То же |
| `system/library/cart/*` | Стандартный OC cart path; нет PPI |
| `catalog/controller/checkout/*` | Totals из cart session |
| `admin/model/catalog/product.php` | Admin save path; не в filter chain |
| `catalog/controller/common/import_1C_offers.php` | Price update OK; index rebuild отдельная тема |
| `getCategoryPriceRange()` | Уже на правильной формуле + `> 0` (06H) |
| `oc_product`, `oc_product_special`, `discount1c` schema | Hotfix — только SQL expression в model |
| DB `UPDATE` / mass reindex | Вне scope; filter fix code-only |

---

## Appendix A — Dependency map

```
                    ┌─────────────────────┐
                    │  oc_product (+      │
                    │  price2/3,          │
                    │  discount1c)        │
                    └──────────┬──────────┘
                               │ refreshPriceIndex()
                               ▼
                    ┌─────────────────────┐
                    │ oc_product_price_   │
                    │ index (ppi)         │
                    └──────────┬──────────┘
           ┌───────────────────┼───────────────────┐
           │                   │                   │
           ▼                   ▼                   ▼
 getCategoryPriceRange   getProducts filter   ORDER BY p.price
 IF(special>0,...) ✅   IFNULL ❌            IFNULL ❌
           │
           ▼
    sidebar min/max

 getProduct() ──────────────────────────────► PLP card / PDP / cart
 (PHP: special===false, special>0) ✅
```

---

## Appendix B — UNKNOWN / limits

| Item | Status |
|------|--------|
| Live `system/library/cart/cart.php` byte-exact | **SAFE UNKNOWN** — не в repo; вывод по OC pattern + PLP flags |
| Точный % `special=0` vs `special IS NULL` в production DB | **SAFE UNKNOWN** в этом проходе; 06K подтвердил массовый `special=0` |
| Частота реальных SKU с `final_special === 0` (100% discount) | **SAFE UNKNOWN** — edge case |

---

## Changed files (this audit task)

| Action | Path |
|--------|------|
| **Created** | `projects/ocpilot/sites/site-002/reports/SITE-002-M9.8.9-06L-PRICE-EFFECTIVE-LOGIC-SAFETY-AUDIT.md` |

**Git:** no commit, no push (audit-only).

**SECURITY RISK:** none identified in recommended hotfix scope.
