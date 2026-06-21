# REPORT — M9.8.9-06G PRICE FILTER ZERO-PRICE FORENSIC

**Project:** SITE-002 (ZPM TEST)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`  
**Date:** 2026-06-19  
**Mode:** Read-only forensic audit — **no deploy, no cron, no import, no DB/code changes**

**Evidence bundle:** `projects/ocpilot/sites/site-002/reports/m9.8.9-06g-work/audit-data.json`  
**Audit runner (read-only):** `projects/ocpilot/sites/site-002/reports/m9.8.9-06g-zero-price-forensic-run.py`

---

## Root Cause

**Гипотеза подтверждена.**

После импорта `offers0_1.xml` (M9.8.9-06F hook активен) товары с `price = 0` из 1С:

1. Записываются в `oc_product.price` импортом `import_1C_offers.php`.
2. Попадают в `oc_product_price_index` через `refreshPriceIndex()` (батч после offers).
3. Участвуют в `MIN()` внутри `getCategoryPriceRange()` **без исключения нулевых цен**.
4. Сдвигают `min_price` sidebar-фильтра с коммерческого минимума на **0**.

### Цепочка (подтверждена)

```
offers0_1.xml (ЦенаЗаЕдиницу = 0)
  → UPDATE oc_product.price = 0
  → refreshPriceIndex() [M9.8.9-06F]
  → INSERT oc_product_price_index.price = 0
  → getCategoryPriceRange() MIN(effective_price) = 0
  → category.php: $data['min_price'] = floor(0) = 0
  → filterssidebar.twig: placeholder="{{ min_price }}" → "0"
```

### Код — источник диапазона

`getCategoryPriceRange()` агрегирует **только** `oc_product_price_index`, без фильтра `> 0`:

```sql
MIN(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS min_price
```

Условия: `status = 1`, `date_available <= NOW()`, `store_id`, `customer_group_id = 2` (guest).  
**Нет** `AND effective_price > 0`.

### Сопоставление с M9.8.9-06D

После rebuild 301 (06D) диапазон был **5405 – 72630** (`run-results.json`).  
Сейчас SQL-эквивалент `getCategoryPriceRange()` для 301:

| Метрика | С нулевыми | Без нулевых (`effective_price > 0`) |
|---------|------------|--------------------------------------|
| min | **0** | **5405** |
| max | 72630 | 72630 |

Регрессия вызвана **появлением нулевых цен в index после import**, а не повторным index drift.

### Live PLP (2026-06-19)

| Категория | URL | `placeholder_from` (факт) |
|-----------|-----|---------------------------|
| Столы (301) | `/katalog/nejtralnoe-oborudovanie/stoly/` | **0** |
| Моечные ванны (80) | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | **0** |

---

## Affected Categories

Все **5** активных товаров с `oc_product.price = 0` лежат в ветке **Нейтральное оборудование (79)**.

| Root / branch | category_id | Название | Товаров с price=0 |
|---------------|-------------|----------|-------------------|
| 79 | 79 | Нейтральное оборудование | 5 |
| 80 | 80 | **Моечные ванны** | **4** |
| 80 | 270 | Ванны цельнотянутые ЛЮКС | 4 |
| 301 | 301 | **Столы** | **1** |
| 301 | 305 | Столы серии СТАНДАРТ | 1 |
| 301 | 306 | Столы СТАНДАРТ-600 с полкой-решеткой | 1 |

### Товары с price=0 (полный список)

| product_id | model | Ветка | Подкатегория |
|------------|-------|-------|--------------|
| 144 | ВМЦ-Л-1/500 | Моечные ванны (80) | 270 |
| 145 | ВМЦ-Л-2/400 | Моечные ванны (80) | 270 |
| 1057 | ВМЦ-Л-2/500 | Моечные ванны (80) | 270 |
| 1058 | ВМЦ-Л-1/400 | Моечные ванны (80) | 270 |
| 3071 | СПБ-С-10/6 | Столы (301) | 306 |

Все перечисленные в задании ID (144, 145, 1057, 1058, 3071) подтверждены: `oc_product.price = 0`, `ppi.price = 0`, `effective_price = 0`.

### Диапазоны фильтра по затронутым веткам

| Ветка | min (текущий) | max | min без нулевых |
|-------|---------------|-----|-----------------|
| 301 Столы | **0** | 72630 | 5405 |
| 80 Моечные ванны | **0** | 75071 | 5553 |

Index coverage 301: **420/420** (100%) — проблема не в отсутствии строк, а в нулевых значениях.

---

## Zero Price Product Count

| Метрика | Значение |
|---------|----------|
| Активных товаров с `oc_product.price = 0` | **5** |
| Из них с записью в `oc_product_price_index` (group 2), `ppi.price = 0` | **5** |
| С `effective_price = 0` в index (group 2) | **5** |
| В поддереве **301** (Столы) | **1** |
| В поддереве **80** (Моечные ванны) | **4** |

---

## Current Business Logic

### Отображение цены (PLP / PDP) — «По запросу»

**PLP** — `catalog/controller/product/product_results.php` (live pattern):

- `$pricecalc` берётся из `$result['price']` / special.
- При `$pricecalc == 0`:
  - `$price = 'По запросу'`
  - `$canCart = false`
  - `$classstatus = 'order'`

**PDP** — `catalog/controller/product/product.php`:

- При `$pricecalc == 0`:
  - `$data['price'] = 'По запросу'`
  - `$data['showrequest'] = true`
  - `$canCart = false`

Строка **«Цена по запросу»** задаётся как начальный `$statusText`, но при `quantity > 0` перезаписывается на «В наличии: N шт.» — на PDP/PLP **цена** показывается как **«По запросу»**, не как число.

Live check: PDP product_id **3071** и **144** содержат текст **«По запросу»**.

### Фильтр «Только с ценой» (`only_with_price`)

В `getProducts()` / `getTotalProducts()` при `only_with_price`:

- если `price_from` не задан или равен 0 → принудительно `price_from = 1`
- фильтрация по `IFNULL(ppi.special, ppi.price) >= price_from`

То есть **осознанная** бизнес-логика уже трактует `0` как «без коммерческой цены» для **выборки товаров**, но **не** для расчёта границ слайдера.

### Импорт 1С

`import_1C_offers.php` (post-06F): при отсутствии цены в XML `$price = 0`, UPDATE без валидации. После файла — `refreshPriceIndex()` для всех обновлённых ID, включая нулевые.

`refreshPriceIndex()` (admin/catalog model): пишет `price = (float)$final_price` без пропуска нуля; при `$final_special === 0` в БД может попасть `special = 0.0000` (не NULL).

### Расхождение семантики

| Слой | Поведение для price=0 |
|------|------------------------|
| Карточка / PDP | «По запросу», корзина отключена |
| Фильтр `only_with_price` | Исключает из выдачи (from ≥ 1) |
| `getCategoryPriceRange()` | **Включает в MIN** → min = 0 |

---

## Recommended Fix Strategy

### Вариант A — Оставить как есть

- **Суть:** не менять код/данные; 0 в слайдере = «есть товары без цены».
- **Минусы:** UX-конфликт с «По запросу»; пользователь может отфильтровать диапазон 0–X и получить товары без цены вперемешку с дешёвыми; повторяет баг после каждого offers с нулевыми позициями.
- **Оценка:** не рекомендуется.

### Вариант B — Исключать price=0 из расчёта диапазона (рекомендуется)

- **Суть:** в `getCategoryPriceRange()` добавить  
  `AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0`
- **Плюсы:** минимальный diff; согласовано с `only_with_price`; восстанавливает 5405/5553 без трогания index; безопасно при будущих imports.
- **Минусы:** товары «По запросу» не отражаются в нижней границе (ожидаемо).
- **Оценка:** **предпочтительный** — один метод, одна семантика.

### Вариант C — Не писать / удалять строки в `product_price_index` для price=0

- **Суть:** в `refreshPriceIndex()` при `final_price == 0` не INSERT (или DELETE без replace); либо разовая чистка нулевых строк.
- **Плюсы:** index = только «товары с коммерческой ценой»; `getCategoryPriceRange` с INNER JOIN автоматически исключит их.
- **Минусы:** `LEFT JOIN ppi` в листинге может дать NULL для фильтра по цене; нужна проверка всех путей (`only_with_price`, сортировка по цене); риск регрессии шире, чем у B.
- **Оценка:** допустим как **дополнение** к B, не как единственная мера.

### Вариант D — Источник данных 1С + NULL-semantics

- **Суть:** (1) в offers не затирать цену нулём, если в 1С «цена по запросу» — хранить NULL/отдельный флаг; (2) в index хранить `NULL` вместо `0` для non-priced SKU.
- **Плюсы:** корректная предметная модель.
- **Минусы:** требует согласования с 1С и миграции схемы/импорта; больше scope.
- **Оценка:** стратегический backlog; для hotfix — B.

**Итоговая рекомендация:** **Вариант B** (быстрый, согласованный fix) + опционально **D** на уровне 1С-контракта; **C** только после regression pass по всем `ppi` consumers.

---

## Risk Assessment

| Риск | Уровень | Комментарий |
|------|---------|-------------|
| Неверный min в фильтре на всех ветках с zero-price SKU | **Высокий (активен)** | Подтверждено live на 301 и 80 |
| Повтор после каждого offers с price=0 | **Высокий** | 06F hook **усиливает** проблему: index синхронизируется с нулём |
| Слайдер 0–max, degenerate thumb coupling (06) | **Средний** | При min=0 span больше, но UX «от 0» вводит в заблуждение |
| Скрытие товаров «По запросу» при fix B | **Низкий** | Они остаются в листинге; меняется только нижняя граница виджета |
| Fix C без аудита JOIN-путей | **Средний** | Возможны пустые ppi в сортировке/фильтрах |
| Изменение 1С (вариант D) | **Средний / долгий** | Зависит от бизнес-правил учёта |

### UNKNOWN

- Точное бизнес-правило 1С для ID 144/145/1057/1058/3071 (сняты с продажи / нет прайса / ошибка выгрузки) — **не верифицировано** вне БД; требует сверки с оператором 1С.
- Полный список веток каталога с `min_price = 0` beyond 80/301 — не сканировался; при 5 zero-SKU затронуты минимум ветки 79→80 и 79→301.

---

## Verification Checklist (для оператора после будущего fix)

1. SQL: `getCategoryPriceRange` equivalent для 301 → min **5405**, не 0.
2. PLP Столы: `placeholder` поля «Цена от» = **5405** (или floor актуального min).
3. PLP Моечные ванны: min **5553** (или актуальный).
4. PDP 3071 / 144: по-прежнему **«По запросу»**.
5. Чекбокс «Только с ценой» — без регрессии.

---

## Git / Changes

| Item | Status |
|------|--------|
| Live site PHP/DB | **Не изменялись** |
| Созданы артефакты аудита | `reports/m9.8.9-06g-work/audit-data.json`, `reports/m9.8.9-06g-zero-price-forensic-run.py`, этот отчёт |

**SECURITY NOTE:** audit runner содержит read-only DB credentials по образцу 06C/06D — не коммитить в публичный репозиторий без redaction.
