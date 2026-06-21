# BZPM M8.2 — Cleanup Specification v1

**Program:** BZPM Product Roadmap  
**Milestone:** M8.2 Cleanup Specification  
**Environment:** https://zpm.new-site.space/ (TEST)  
**Audit UTC:** 2026-06-14T18:09:33Z (M8.1 baseline)  
**Specification UTC:** 2026-06-15  
**Mode:** Planning only — no DB, admin, code, or deploy changes  
**Authority:** `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md` · `BZPM-PRODUCT-ROADMAP-v1.md` (ROAD-002) · M7.1 Launch Mode artifacts · `.recovery-temp/bzpm-m8.1-audit.json`

---

# REPORT — BZPM M8.2 Cleanup Specification

## Executive Summary

M8.1 зафиксировал **609** активных SKU в scope Launch Mode (Нейтральное оборудование, `category_id` 79), **56** атрибутов в реестре (DB сообщает **60** — 4 ID не экспортированы), **0** native OpenCart filters, и **подтверждённое TEST-загрязнение**: 1 активный товар (**3071**), 6 TEST-атрибутов с данными (IDs **105–109**, **111**), 1 пустой placeholder (**16**).

**Цель M8.2:** превратить сырой каталог в коммерческий **без потери данных** — для каждой сущности явно задано **DELETE**, **HIDE** или **KEEP**. Удаление из фильтров ≠ удаление из БД.

**Ключевые выводы:**

| Область | Объём | Доминирующее действие |
| --- | --- | --- |
| TEST contamination | 1 product, 7 attr defs, 6 attr values | HIDE сразу; DELETE defs/values после миграции SKU 3071 |
| Packaging cluster | 10 attr IDs (44–46, 52–57) + `oc_product.weight` | HIDE из фильтров; STORE_ONLY (логистика) |
| SERVICE attrs | 4 IDs (43, 48, 58, 102) | HIDE из фильтров; STORE_ONLY на PDP |
| Dead attrs | 9 IDs (13–16, 32, 55, 102–104) | DELETE defs после admin-проверки inactive SKU |
| Commercial core | 18 SHOW + 7 REVIEW + 4 `oc_product` dims | KEEP; профили M9 |
| Category noise | Packaging/SERVICE/TEST в PLP всех веток | HIDE via M9 profiles после M8.3 wave 1 |

**M9 readiness:** M9 Filter Profile System **не может** стартовать сразу после M8.2 (это только спецификация). Требуется **M8.3 Cleanup Implementation** — минимум **Wave 1** (SKU 3071 + TEST attrs off surface) — до валидации профилей на TEST storefront. M9 design/spec может идти параллельно; **deploy/verify** — только после M8.3 Wave 1.

**SAFE UNKNOWN:** 4 attribute IDs (60 DB count vs 56 registry); видимость SKU 3071 на PLP/search post-M7.1; полный inactive-SKU assignment check для dead attrs.

---

## TEST Cleanup Matrix

Принцип: **никогда не предполагать DELETE** для данных с коммерческой ценностью. TEST-значения на SKU 3071 дублируют реальные измерения (шир/выс/дл/сталь/толщины) — перед DELETE перенести в канонические поля/атрибуты.

### Confirmed TEST entities

| Entity | Type | Location | Action | Reason |
| --- | --- | --- | --- | --- |
| Product **3071** | TEST Product | `oc_product` · active `status=1` · category subtree incl. Столы | **HIDE** → затем **KEEP** (после очистки) или **DELETE** (только если дубликат/мусор подтверждён) | Единственный активный SKU с `%тест%` в имени и всеми ТЕСТ-атрибутами; сейчас загрязняет filter panel. Деактивировать или переименовать + перенести значения до удаления attrs. |
| Attribute def **16** | TEST Attribute | `oc_attribute` · группа «Общие» · `filter_name=param` | **DELETE** | Пустой placeholder «Параметр»; 0 товаров; 0 категорий; не в фильтре, но мусорная дефиниция. |
| Attribute def **105** | TEST Attribute | `oc_attribute` · «шир ТЕСТ» | **HIDE** → **DELETE** | QA-атрибут; 1 товар; **в фильтре сегодня**. Сначала снять с поверхности, затем удалить def после strip SKU 3071. |
| Attribute def **106** | TEST Attribute | `oc_attribute` · «выс ТЕСТ» | **HIDE** → **DELETE** | Аналогично 105. |
| Attribute def **107** | TEST Attribute | `oc_attribute` · «дл ТЕСТ» | **HIDE** → **DELETE** | Аналогично 105. |
| Attribute def **108** | TEST Attribute | `oc_attribute` · «марка стали ТЕСТ» | **HIDE** → **DELETE** | Аналогично 105. |
| Attribute def **109** | TEST Attribute | `oc_attribute` · «толщина столешницы ТЕСТ» | **HIDE** → **DELETE** | Аналогично 105. |
| Attribute def **111** | TEST Attribute | `oc_attribute` · «толщина материала ног ТЕСТ» | **HIDE** → **DELETE** | Аналогично 105. |
| Attr value 3071×**105** | TEST Value | `oc_product_attribute` · `0,6` | **DELETE** (после migrate) | Дублирует `oc_product.width` или коммерческий attr; перенести, затем удалить value. |
| Attr value 3071×**106** | TEST Value | `oc_product_attribute` · `0,85` | **DELETE** (после migrate) | Дублирует `oc_product.height`. |
| Attr value 3071×**107** | TEST Value | `oc_product_attribute` · `1` | **DELETE** (после migrate) | Дублирует `oc_product.length`. |
| Attr value 3071×**108** | TEST Value | `oc_product_attribute` · `430` | **DELETE** (после migrate) | Нет канонического «марка стали» в inventory — **REVIEW** migrate target (возможно STORE_ONLY note или новый commercial attr позже). |
| Attr value 3071×**109** | TEST Value | `oc_product_attribute` · `0,7` | **DELETE** (после migrate) | Нет прямого commercial twin; ближайшее — материал столешницы (22), не толщина. **REVIEW** при migrate. |
| Attr value 3071×**111** | TEST Value | `oc_product_attribute` · `1,5` | **DELETE** (после migrate) | Нет канонического attr для толщины ног. **REVIEW** при migrate. |

### Explicit non-targets (false positives)

| Entity | Type | Location | Action | Reason |
| --- | --- | --- | --- | --- |
| Category **189** «Тестомесы» | Category | Thermal subtree · not Neutral 79 | **KEEP** | Legitimate «тесто-*» equipment name; substring false positive. |
| Category **193** «Тестораскатки, тестозакатки» | Category | Thermal subtree | **KEEP** | Legitimate product category. |
| Category **194** «Тестоделители и тестоокруглители» | Category | Thermal subtree | **KEEP** | Legitimate product category. |
| `oc_filter` / `oc_filter_group` | Native filter | OpenCart filter tables | **KEEP** (empty) | 0 rows; no TEST names; no action. |
| Option values | Option | `oc_option_value` | **KEEP** | 0 TEST matches per M8.1. |
| Manufacturers | Manufacturer | `oc_manufacturer` | **KEEP** | 1 manufacturer; no TEST name. |

### TEST cleanup sequence (implementation order for M8.3)

1. **HIDE** product 3071 from PLP/search OR deactivate until cleaned.
2. **Migrate** dimensional TEST values → `oc_product` L/W/H (if empty) + review steel/thickness targets.
3. **DELETE** `oc_product_attribute` rows for IDs 105–111 on product 3071.
4. **HIDE** TEST attrs from filter surface (M9 profile rule or interim code flag).
5. **DELETE** attribute defs 105–111, then **16**.
6. **Verify** TEST storefront — no «ТЕСТ» in filter sidebar on any Neutral PLP.

---

## Attribute Visibility Matrix

Классификация из M8.1. Действия: **SHOW_IN_FILTER** · **SHOW_IN_PDP** · **STORE_ONLY** · **DELETE** · **REVIEW**.

Поле `oc_product` (не attribute):

| ID / Field | Attribute Name | Class | Action | Reason |
| --- | --- | --- | --- | --- |
| `length` | Длина (`oc_product`) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 586/609 fill; primary commercial dimension via `getCategoryPhysicalLimits()`. |
| `width` | Ширина (`oc_product`) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 586/609 fill; primary filter. |
| `height` | Высота (`oc_product`) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 586/609 fill; primary filter. |
| `weight` | Масса (`oc_product`) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 531/609 fill; buyer-relevant load/logistics hint; not packaging attr duplicate. |

### Full attribute registry (56 captured IDs)

| Attribute ID | Attribute Name | Class | Action | Reason |
| ---: | --- | --- | --- | --- |
| 12 | Габариты нетто (мм) | TECHNICAL | **STORE_ONLY** | Дублирует `oc_product` L/W/H; 54 SKU; logistics/specs only. |
| 13 | Габариты брутто (мм) | TECHNICAL | **DELETE** | 0 товаров; dead def; дубль 12/упаковки. |
| 14 | Борт | COMMERCIAL | **DELETE** | 0 товаров; superseded by 25/18/47 bort cluster. |
| 15 | Гарантия | COMMERCIAL | **DELETE** | 0 товаров; dead def; восстановить при наполнении warranty program. |
| 16 | Параметр | TEST | **DELETE** | TEST placeholder; 0 товаров. |
| 17 | В комплекте | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 45 SKU; meaningful kit info. |
| 18 | Высота борта (мм) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 380 SKU; sink/table buyer decision. |
| 19 | Количество уровней направляющих | COMMERCIAL | **REVIEW** | 3 SKU; category-specific (подтоварники); profile when N grows. |
| 20 | Макс. нагрузка (до, кг) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 427 SKU; core commercial. |
| 21 | Конструкция | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 599 SKU; universal neutral filter. |
| 22 | Материал столешницы | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 535 SKU; tables/sinks. |
| 23 | Мойка | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 192 SKU; sink branch primary. |
| 24 | Назначение секции | COMMERCIAL | **REVIEW** | 4 SKU; подтоварники only. |
| 25 | Наличие борта | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 569 SKU; commercial yes/no. |
| 26 | Ножки | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 579 SKU; construction filter. |
| 27 | Обвязка | TECHNICAL | **STORE_ONLY** | 7 SKU; engineering; not buyer filter. |
| 28 | Отверстие под смеситель | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 192 SKU; sink branch. |
| 29 | Размер раковины (ДхШхВ, мм) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 190 SKU; sink primary dimension. |
| 30 | Размер секции | COMMERCIAL | **REVIEW** | 3 SKU; подтоварники. |
| 31 | Регулируемость опоры по высоте (max мм) | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 545 SKU; commercial adjustability. |
| 32 | Тип крепления | COMMERCIAL | **DELETE** | 0 товаров; dead def (NE group). |
| 33 | Тип опоры | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 580 SKU; universal. |
| 34 | Страна производства | TECHNICAL | **STORE_ONLY** | 55 SKU; origin; PDP specs; hide filter except зонты secondary. |
| 36 | Обвязка | TECHNICAL | **STORE_ONLY** | 17 SKU; duplicate name 27; engineering. |
| 38 | Количество | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 30 SKU; multi-unit sets. |
| 42 | Стандарт | TECHNICAL | **STORE_ONLY** | 367 SKU; GOST/ref; not primary buyer filter (secondary зонты/тележки). |
| 43 | Дополнительные сведения | SERVICE | **STORE_ONLY** | 974 SKU; ops/junk text risk; never filter. |
| 44 | Длина в упаковке (мм) | TECHNICAL | **STORE_ONLY** | 531 SKU; logistics; см. Packaging Audit. |
| 45 | Ширина в упаковке (мм) | TECHNICAL | **STORE_ONLY** | 531 SKU; logistics. |
| 46 | Высота в упаковке (мм) | TECHNICAL | **STORE_ONLY** | 531 SKU; logistics. |
| 47 | Конструкция борта | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 152 SKU; sink/table bort detail. |
| 48 | Комплект поставки | SERVICE | **STORE_ONLY** | 111 SKU; overlaps 17; logistics/docs. |
| 49 | Производитель | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 18 SKU; low fill but valid commercial. |
| 50 | Тип крепления | COMMERCIAL | **REVIEW** | 1 SKU; duplicate concept of 32; defer. |
| 51 | Конструкция полки | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 435 SKU; shelves/tables. |
| 52 | Упаковка (Длина, мм) | TECHNICAL | **STORE_ONLY** | 29 SKU; duplicate plane of 44. |
| 53 | Упаковка (Ширина, мм) | TECHNICAL | **STORE_ONLY** | 29 SKU; duplicate plane of 45. |
| 54 | Упаковка (Высота, мм) | TECHNICAL | **STORE_ONLY** | 29 SKU; duplicate plane of 46. |
| 55 | Упаковка (вес брутто, кг) | TECHNICAL | **DELETE** | 0 товаров; dead def. |
| 56 | Упаковка (Объем, м. куб.) | TECHNICAL | **STORE_ONLY** | 535 SKU; freight calc; not buyer filter. |
| 57 | Вес (нетто, кг) | TECHNICAL | **STORE_ONLY** | 28 SKU; differs from `oc_product.weight`; logistics. |
| 58 | Комплект отгрузки | SERVICE | **STORE_ONLY** | 47 SKU; shipping logistics. |
| 102 | Выгрузка | SERVICE | **DELETE** | 0 товаров; dead def. |
| 103 | 08 Количество уровней направляющих | COMMERCIAL | **DELETE** | 0 товаров; mis-import duplicate of 19. |
| 104 | 35 Размер секции | COMMERCIAL | **DELETE** | 0 товаров; mis-import duplicate of 30. |
| 105 | шир ТЕСТ | TEST | **DELETE** | TEST; in filter today. |
| 106 | выс ТЕСТ | TEST | **DELETE** | TEST. |
| 107 | дл ТЕСТ | TEST | **DELETE** | TEST. |
| 108 | марка стали ТЕСТ | TEST | **DELETE** | TEST. |
| 109 | толщина столешницы ТЕСТ | TEST | **DELETE** | TEST. |
| 110 | Тип покрытия | COMMERCIAL | **REVIEW** | 1 SKU; potential commercial when assortment grows. |
| 111 | толщина материала ног ТЕСТ | TEST | **DELETE** | TEST. |
| 112 | Материал полки | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 377 SKU; tables/shelves. |
| 113 | Шаг регулировки полки (мм) | COMMERCIAL | **REVIEW** | 1 SKU. |
| 114 | Количество полок (шт) | COMMERCIAL | **REVIEW** | 1 SKU; future полки/стеллажи profile. |
| 115 | Усиление | COMMERCIAL | **SHOW_IN_FILTER** + **SHOW_IN_PDP** | 385 SKU; load-bearing tables. |

### SAFE UNKNOWN — missing attribute IDs

DB count **60** vs **56** exported rows. До любого DELETE-wave: verify in admin which 4 IDs exist and classify. **Action default: REVIEW** until identified.

---

## Packaging Data Audit

Коммерческая логика: покупатель фильтрует по **габаритам изделия** и **рабочим характеристикам**, не по транспортной упаковке. Инженерные поля сохраняем для отгрузки/склада.

### Packaging-related attributes

| Attribute ID | Name | Filled (active) | SHOW_IN_FILTER | SHOW_IN_PDP | STORE_ONLY | Commercial rationale |
| ---: | --- | ---: | --- | --- | --- | --- |
| 44 | Длина в упаковке (мм) | 531 | **No** | **No** | **Yes** | Carton dimension; duplicates freight plane; clutters PLP (420/420 on Столы). |
| 45 | Ширина в упаковке (мм) | 531 | **No** | **No** | **Yes** | Same. |
| 46 | Высота в упаковке (мм) | 531 | **No** | **No** | **Yes** | Same. |
| 52 | Упаковка (Длина, мм) | 29 | **No** | **No** | **Yes** | Alternate import schema; subset of 44. |
| 53 | Упаковка (Ширина, мм) | 29 | **No** | **No** | **Yes** | Alternate import schema. |
| 54 | Упаковка (Высота, мм) | 29 | **No** | **No** | **Yes** | Alternate import schema. |
| 55 | Упаковка (вес брутто, кг) | 0 | **No** | **No** | **DELETE** | Dead; no data. |
| 56 | Упаковка (Объем, м. куб.) | 535 | **No** | **No** | **Yes** | Freight volume; internal/logistics. |
| 57 | Вес (нетто, кг) | 28 | **No** | **Optional** | **Yes** | Net weight attr ≠ `oc_product.weight`; show on PDP only if ops confirms accuracy. |
| 12 | Габариты нетто (мм) | 54 | **No** | **No** | **Yes** | Text blob dims; superseded by `oc_product` L/W/H for buyers. |
| 13 | Габариты брутто (мм) | 0 | **No** | **No** | **DELETE** | Dead. |
| `weight` | Масса (`oc_product`) | 531 | **Yes** | **Yes** | — | **Commercial** product weight — not packaging cluster. |

### Duplication strategy (M8.3+ / long-term CMS)

| Cluster | IDs | M8.2 action | Long-term |
| --- | --- | --- | --- |
| Primary carton L/W/H | 44, 45, 46 | HIDE filter; STORE_ONLY | Consolidate to single logistics group |
| Legacy import L/W/H | 52, 53, 54 | HIDE filter; STORE_ONLY | Merge into 44–46 on data migration |
| Volume + gross | 56, 55 | HIDE filter; DELETE 55 | Keep 56 STORE_ONLY |
| Product vs net weight | `oc_product.weight` vs 57 | Commercial vs STORE_ONLY | Document semantic difference in admin |

**Сегодня на TEST:** все packaging attrs с fill **появляются в sidebar** через `getAttributesByCategory()` — это главный источник «неkomмерческого» шума на Столы (6 packaging attrs в top-15).

---

## Core Commercial Attribute Set

Канонический набор для **Нейтральное оборудование** (buyer-facing). Источник: M8.1 fill rates + category matrix + M9 prep notes.

### Tier 1 — Universal primary (все ветки Neutral)

| Source | Name | Role |
| --- | --- | --- |
| `oc_product` | **Длина** | Physical range filter + PDP hero |
| `oc_product` | **Ширина** | Physical range filter + PDP hero |
| `oc_product` | **Высота** | Physical range filter + PDP hero |
| `oc_product` | **Масса** | Physical range filter + PDP |
| — | **Цена** | Existing commerce filter (non-attribute) |
| — | **Наличие** | Existing availability filter |

### Tier 2 — Universal commercial attributes (cross-category, high fill)

| ID | Name | Typical filter tier |
| ---: | --- | --- |
| 21 | **Конструкция** | Primary |
| 33 | **Тип опоры** | Primary |
| 26 | **Ножки** | Secondary |
| 25 | **Наличие борта** | Secondary |
| 31 | **Регулируемость опоры по высоте (max мм)** | Secondary |
| 20 | **Макс. нагрузка (до, кг)** | Primary (tables, подтоварники) |

### Tier 3 — Branch-specific commercial (profile assignment)

| ID | Name | Primary branches |
| ---: | --- | --- |
| 22 | **Материал столешницы** | Столы, Моечные ванны, Подтоварники |
| 51 | **Конструкция полки** | Столы, Полки*, Стеллажи*, Подтоварники |
| 112 | **Материал полки** | Столы, Полки*, Стеллажи* |
| 115 | **Усиление** | Столы, Подтоварники |
| 18 | **Высота борта (мм)** | Моечные ванны, Столы (subset) |
| 47 | **Конструкция борта** | Моечные ванны |
| 23 | **Мойка** | Моечные ванны |
| 28 | **Отверстие под смеситель** | Моечные ванны |
| 29 | **Размер раковины (ДхШхВ, мм)** | Моечные ванны |
| 38 | **Количество** | Подтоварники, комплекты |
| 17 | **В комплекте** | Моечные ванны, комплекты |
| 49 | **Производитель** | Low-fill global secondary |
| 114 | **Количество полок (шт)** | Полки*, Стеллажи* (REVIEW until assortment) |
| 113 | **Шаг регулировки полки (мм)** | Полки*, Стеллажи* (REVIEW) |

\*Полки (`83`) и Стеллажи (`86`): **0 active SKU** — attrs included as **planned profile** from Столы/Подтоварники pattern.

### Explicitly NOT in core commercial set

- All packaging IDs 44–46, 52–57, 56  
- SERVICE 43, 48, 58, 102  
- TECHNICAL 12, 27, 34, 36, 42 (except secondary where noted)  
- TEST 16, 105–111  
- Dead/duplicate 13, 14, 15, 32, 55, 103, 104  

---

## Hidden Attribute Set

Атрибуты, которые **исчезают из filter layer** (M9 profile / M8.3 hide rules). Данные **сохраняются** в БД unless marked DELETE.

### Technical — hide from filters

| ID | Name | PDP | DB |
| ---: | --- | --- | --- |
| 12 | Габариты нетто (мм) | STORE_ONLY | KEEP |
| 27 | Обвязка | STORE_ONLY | KEEP |
| 34 | Страна производства | STORE_ONLY | KEEP |
| 36 | Обвязка | STORE_ONLY | KEEP |
| 42 | Стандарт | STORE_ONLY | KEEP |
| 44 | Длина в упаковке (мм) | STORE_ONLY | KEEP |
| 45 | Ширина в упаковке (мм) | STORE_ONLY | KEEP |
| 46 | Высота в упаковке (мм) | STORE_ONLY | KEEP |
| 52 | Упаковка (Длина, мм) | STORE_ONLY | KEEP |
| 53 | Упаковка (Ширина, мм) | STORE_ONLY | KEEP |
| 54 | Упаковка (Высота, мм) | STORE_ONLY | KEEP |
| 56 | Упаковка (Объем, м. куб.) | STORE_ONLY | KEEP |
| 57 | Вес (нетто, кг) | STORE_ONLY | KEEP |
| 13 | Габариты брутто (мм) | — | DELETE |
| 55 | Упаковка (вес брутто, кг) | — | DELETE |

### Service — hide from filters

| ID | Name | PDP | DB |
| ---: | --- | --- | --- |
| 43 | Дополнительные сведения | STORE_ONLY | KEEP (audit junk in M8.3 wave 2) |
| 48 | Комплект поставки | STORE_ONLY | KEEP |
| 58 | Комплект отгрузки | STORE_ONLY | KEEP |
| 102 | Выгрузка | — | DELETE |

### Logistics / packaging global hide rule

**All branches:** IDs **44–46, 52–57, 56** + SERVICE **43, 58** + TEST **16, 105–111** — never appear in `filter_groups` after M9 profile enforcement.

### TEST — hide then delete

| ID | Name | Filter | DB |
| ---: | --- | --- | --- |
| 105–111 | *ТЕСТ attrs* | HIDE immediately | DELETE after SKU 3071 strip |
| 16 | Параметр | N/A (not in filter) | DELETE |

---

## Category Cleanup Matrix

Для каждой major category: mapping атрибутов с fill **≥3 active SKU** в ветке (M8.1) + universal `oc_product` dims.  
**KEEP** = commercial filter/PDP · **HIDE** = STORE_ONLY, не в фильтре · **REVIEW** = мало данных или branch-specific decision.

### Моечные ванны (`category_id` **80**, **152** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Primary physical filters |
| Размер раковины (ДхШхВ, мм) | 29 | **KEEP** | Primary sink filter |
| Мойка | 23 | **KEEP** | Primary |
| Отверстие под смеситель | 28 | **KEEP** | Primary |
| Наличие борта | 25 | **KEEP** | Primary |
| Конструкция борта | 47 | **KEEP** | Secondary |
| Высота борта (мм) | 18 | **KEEP** | Secondary |
| Тип опоры | 33 | **KEEP** | Secondary |
| Конструкция | 21 | **KEEP** | Secondary |
| Ножки | 26 | **KEEP** | Secondary |
| Регулируемость опоры по высоте | 31 | **KEEP** | Secondary |
| Материал столешницы | 22 | **KEEP** | Secondary (104 SKU) |
| В комплекте | 17 | **KEEP** | Secondary |
| Стандарт | 42 | **HIDE** | STORE_ONLY |
| Страна производства | 34 | **HIDE** | STORE_ONLY |
| Габариты нетто (мм) | 12 | **HIDE** | STORE_ONLY |
| Производитель | 49 | **REVIEW** | Low branch fill (18) |
| Длина/Ширина/Высота в упаковке | 44–46 | **HIDE** | Packaging noise (111 SKU each) |
| Упаковка (Объем) | 56 | **HIDE** | 113 SKU |
| Дополнительные сведения | 43 | **HIDE** | SERVICE |
| Комплект поставки | 48 | **HIDE** | SERVICE |
| Упаковка (Высота/Ширина, мм) | 54, 53 | **HIDE** | Subset packaging |

### Столы (`category_id` **301**, **420** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Primary |
| Материал столешницы | 22 | **KEEP** | Primary |
| Конструкция полки | 51 | **KEEP** | Primary |
| Макс. нагрузка (до, кг) | 20 | **KEEP** | Primary |
| Материал полки | 112 | **KEEP** | Secondary |
| Усиление | 115 | **KEEP** | Secondary |
| Конструкция | 21 | **KEEP** | Secondary |
| Тип опоры | 33 | **KEEP** | Secondary |
| Наличие борта | 25 | **KEEP** | Secondary |
| Ножки | 26 | **KEEP** | Secondary |
| Регулируемость опоры | 31 | **KEEP** | Secondary |
| Высота борта (мм) | 18 | **REVIEW** | 240 SKU — tables subset with bort |
| Конструкция борта | 47 | **REVIEW** | 44 SKU |
| Мойка / Размер раковины / Отверстие | 23, 29, 28 | **REVIEW** | 43 SKU — combined table+sink SKUs |
| Стандарт | 42 | **HIDE** | 234 SKU but technical |
| Комплект отгрузки | 58 | **HIDE** | SERVICE |
| Дополнительные сведения | 43 | **HIDE** | 419 SKU — highest noise |
| Длина/Ширина/Высота в упаковке | 44–46 | **HIDE** | **420 SKU each — critical hide** |
| Упаковка (Объем) | 56 | **HIDE** | 420 SKU |
| TEST attrs (if 3071 in branch) | 105–111 | **HIDE** → **DELETE** | Contamination |

### Тележки (`category_id` **85**, **0** SKU) + Тележки сервировочные (`326`, **3** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Only reliable filters at N=3 |
| Стандарт | 42 | **REVIEW** | 3 SKU on 326 — secondary if kept |
| All other attrs | * | **HIDE** | Insufficient assortment (N<20); defer until population |

**Parent «Тележки» (85):** empty — **REVIEW** entire branch visibility in Launch Mode.

### Подтоварники и подставки (`category_id` **322**, **11** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Primary |
| Конструкция полки | 51 | **KEEP** | Primary |
| Макс. нагрузка (до, кг) | 20 | **KEEP** | Primary |
| Материал столешницы | 22 | **KEEP** | Secondary |
| Тип опоры | 33 | **KEEP** | Secondary |
| Конструкция | 21 | **KEEP** | Secondary |
| Количество | 38 | **KEEP** | Secondary |
| Усиление | 115 | **REVIEW** | 8 SKU |
| Размер секции | 30 | **REVIEW** | 3 SKU |
| Количество уровней направляющих | 19 | **REVIEW** | 3 SKU |
| Назначение секции | 24 | **REVIEW** | 3 SKU |
| Стандарт | 42 | **HIDE** | Technical |
| Вес (нетто, кг) | 57 | **HIDE** | Packaging |
| Упаковка (Длина/Ширина/Высота) | 52–54 | **HIDE** | All 11 SKU — packaging |

### Полки (`category_id` **83**, **0** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Planned primary when populated |
| Материал полки | 112 | **KEEP** | From Столы pattern (377 global fill) |
| Конструкция полки | 51 | **KEEP** | Planned primary |
| Количество полок (шт) | 114 | **REVIEW** | 1 SKU global — activate when branch fills |
| Шаг регулировки полки (мм) | 113 | **REVIEW** | 1 SKU global |
| Макс. нагрузка | 20 | **REVIEW** | Apply when SKUs added |
| All packaging / SERVICE / TEST | 43–58, 105–111 | **HIDE** | Default until assortment |

**Branch status:** empty — category tile visible in Launch Mode but no products; profile is **spec-only**.

### Стеллажи (`category_id` **86**, **0** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Planned primary |
| Конструкция полки | 51 | **KEEP** | Planned |
| Материал полки | 112 | **KEEP** | Planned |
| Макс. нагрузка | 20 | **KEEP** | Planned — load-critical for shelving |
| Количество полок (шт) | 114 | **REVIEW** | Future |
| Усиление | 115 | **REVIEW** | Future |
| All packaging / SERVICE / TEST | * | **HIDE** | Default |

### Зонты вытяжные (`category_id` **207**, **23** SKU)

| Attribute | ID | Mapping | Notes |
| --- | ---: | --- | --- |
| Длина / Ширина / Высота / Масса (`oc_product`) | — | **KEEP** | Primary |
| Конструкция | 21 | **KEEP** | Primary (19 SKU) |
| Страна производства | 34 | **REVIEW** | Secondary (22 SKU) — only branch where origin may surface |
| Габариты нетто (мм) | 12 | **HIDE** | Duplicates product dims (22 SKU) |
| All packaging / SERVICE / TEST | * | **HIDE** | Not in branch matrix |

---

## M9 Readiness Assessment

### Question

Can **M9 Filter Profile System** start immediately after M8.2?

### Answer

**No** — not for implementation deploy and TEST verification. **M8.3 Cleanup Implementation is required first** (at minimum Wave 1).

### Justification

| Factor | Evidence | Impact on M9 |
| --- | --- | --- |
| Dynamic filter surfacing | `getAttributesByCategory()` exposes **all filled attrs** | M9 profiles cannot be validated while TEST/packaging attrs still appear |
| Active TEST on surface | Product **3071** + attrs **105–111** in filter today | ROAD-002 violation until M8.3 Wave 1 |
| Packaging noise | 6 packaging attrs on **100%** of Столы PLP | Profile "hide" rules need code + clean baseline to QA |
| Dead defs | 9 zero-fill attrs still in `oc_attribute` | Profile engine must handle/exclude; cleaner after M8.3 Wave 3 |
| M8.2 scope | This document = planning only | No surface change until M8.3 |
| M7.1 dependency | Launch Mode scopes Neutral 79 only | M9 profiles target this tree — prerequisite met |

### Recommended split

| Phase | Milestone | Work | M9 relationship |
| --- | --- | --- | --- |
| **M8.2** | Now | Specification (this doc) | Input to M9 profile design |
| **M8.3 Wave 1** | Next | SKU 3071 + TEST hide/delete + verify storefront | **Gate** — M9 deploy/QA starts after PASS |
| **M8.3 Wave 2** | After Wave 1 | SERVICE hygiene (43 audit), packaging hide via interim or M9 | M9 profiles absorb hide rules |
| **M8.3 Wave 3** | After Wave 2 | Dead attr DELETE (13–16, 32, 55, 102–104) | Cleaner attribute ID space |
| **M9** | After Wave 1 min. | Category + subcategory filter profiles (ROAD-003/004) | Implementation |

**Parallel allowed:** M9 **design document** and profile JSON/schema drafting using this spec — **in parallel** with M8.3. **Not allowed:** M9 TEST deploy claiming "done" before Wave 1 verification.

---

## Recommended Cleanup Order

Aligned with M8.1 §Recommended Cleanup Order; refined with DELETE/HIDE/KEEP discipline.

| Wave | Step | Entities | Action type | Verification |
| ---: | --- | --- | --- | --- |
| **1** | 1.1 | Product **3071** | HIDE/deactivate → migrate → reactivate | No «ТЕСТ» in name on active PLP |
| **1** | 1.2 | Attr values 3071 × 105–111 | DELETE after migrate | `oc_product_attribute` clean |
| **1** | 1.3 | Attr defs **105–111** | DELETE | Admin attr count −6 |
| **1** | 1.4 | Attr def **16** | DELETE | Placeholder gone |
| **1** | 1.5 | TEST storefront PLP | Visual QA | No TEST attrs in sidebar |
| **2** | 2.1 | Attr **43** values | KEEP data; audit junk samples | Spot-check 20 SKUs |
| **2** | 2.2 | SERVICE **43, 48, 58** | HIDE from filter (M9 or interim) | PLP sidebar clean |
| **2** | 2.3 | Packaging **44–46, 52–57, 56** | HIDE from filter | Столы PLP: no packaging attrs |
| **2** | 2.4 | TECHNICAL **12, 27, 34, 36, 42** | HIDE from filter | зонты/столы QA |
| **3** | 3.1 | Dead defs **13, 14, 15, 32, 55, 102, 103, 104** | DELETE after inactive-SKU check | Admin cleanup |
| **3** | 3.2 | Duplicate **27 vs 36** «Обвязка» | REVIEW merge | Long-term CMS |
| **3** | 3.3 | Packaging consolidation | REVIEW data migration | Deferred CMS project |
| **4** | 4.1 | **M9** filter profiles per category matrix | IMPLEMENT | ROAD-003/004 |
| **4** | 4.2 | REVIEW attrs 19, 24, 30, 50, 110, 113, 114 | Operator decision | Promote or DELETE |

**No action:** Categories 189, 193, 194 (false positives). Native `oc_filter` (empty).

---

## Risks

| ID | Risk | Severity | Mitigation |
| --- | --- | --- | --- |
| RSK-M82-01 | **Data loss on SKU 3071** if TEST values deleted before migrate | High | Migrate to `oc_product` L/W/H first; REVIEW steel/thickness targets |
| RSK-M82-02 | **4 unknown attribute IDs** (60 vs 56) | Medium | Admin verify before Wave 3 DELETE |
| RSK-M82-03 | **Packaging attrs mistaken for product dims** by buyers | High | M8.3 Wave 2 hide + M9 profile; comms in PDP template |
| RSK-M82-04 | **SERVICE 43 junk text** pollutes PDP if shown | Medium | STORE_ONLY + spot audit; no mass DELETE in M8 |
| RSK-M82-05 | **M9 started before TEST removal** — ROAD-002 breach | High | Enforce M8.3 Wave 1 gate |
| RSK-M82-06 | **Empty branches** (Полки, Стеллажи, Тележки 85) — profile without SKUs | Low | Spec-only profiles; REVIEW when assortment arrives |
| RSK-M82-07 | **Duplicate attrs** (Обвязка 27/36; упаковка 44–54; борт 14/25/18/47) | Medium | Wave 3 REVIEW; no rushed DELETE |
| RSK-M82-08 | **Inactive SKU assignments** on dead attrs | Medium | Admin query inactive products before DELETE |
| RSK-M82-09 | **Filter mechanism is dynamic** — hide requires code (M9), not admin-only | High | M8.3 must include storefront layer, not только DB |

---

## Evidence & limitations

| Item | Source |
| --- | --- |
| Attribute registry (56 rows) | `BZPM-M8.1-ATTRIBUTE-INVENTORY-v1.md` |
| Category matrix + TEST values | `.recovery-temp/bzpm-m8.1-audit.json` |
| Filter mechanism | `getAttributesByCategory()` per M8.1 / SITE-002 trace |
| Launch Mode state | `SITE-002-M7.1-TEST-DEPLOYMENT.md` — 609 active under cat 79 |
| Strategic mandate | `BZPM-PRODUCT-ROADMAP-v1.md` ROAD-002 (M8), ROAD-003/004 (M9) |

## UNKNOWN / SECURITY RISK

- **UNKNOWN:** 4 attribute definition IDs not in M8.1 export — classify before DELETE waves.
- **UNKNOWN:** Whether product 3071 appears on visible PLP/search paths post-M7.1.
- **UNKNOWN:** Inactive product assignments on dead attribute defs (13–16, 32, 55, 102–104).
- **UNKNOWN:** Canonical migrate target for TEST values 108–111 (no direct commercial attr twins).
- **SECURITY RISK:** None introduced by this specification (read-only planning).

---

*M8.2 Cleanup Specification v1 — documentation only. No cleanup performed. No implementation authorized.*
