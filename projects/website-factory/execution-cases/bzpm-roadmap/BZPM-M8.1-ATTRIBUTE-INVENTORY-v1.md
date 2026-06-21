# BZPM M8.1 — TEST + Attribute Inventory v1

**Program:** BZPM Product Roadmap  
**Milestone:** M8.1 Catalog Data Audit  
**Environment:** https://zpm.new-site.space/ (TEST)  
**Audit UTC:** 2026-06-14T18:09:33Z  
**Mode:** Read-only — no DB, storefront, or admin changes  
**Authority:** Live TEST DB `polygonws_zpm` + M7.1 Launch Mode baseline + W1B attribute discovery

---

# REPORT — BZPM M8.1 TEST + Attribute Inventory

## Executive summary

| Metric | Value |
| --- | ---: |
| Active products (`status=1`) | **609** |
| Total products | 3134 |
| Attribute definitions (`oc_attribute`) | **60** |
| Attributes in registry (this audit) | **56** |
| OpenCart native filters (`oc_filter`) | **0** |
| Manufacturers | 1 |

**Filter architecture (documented, verified):** Category PLP builds `filter_groups` dynamically from `getAttributesByCategory()` — any attribute with non-empty text on active SKUs in the category subtree appears in the sidebar. Physical ranges (Длина/Ширина/Высота/Масса) come from `oc_product` fields via `getCategoryPhysicalLimits()`. Native `oc_filter` tables are **empty** on TEST.

**Post M7.1 context:** Launch Mode active — catalog scope = Neutral Equipment (`category_id` 79); 609 active SKUs under this root.

## TEST Inventory

### Method

Substring search: `TEST`, `test`, `ТЕСТ`, `тест` across categories, products, attributes, attribute values, OpenCart filters, option values, manufacturers.

**Important:** Substring `тест` produces **false positives** in legitimate Russian category names (тесто-* equipment under Тепловое). These are **not** QA contamination.

### Confirmed TEST contamination

| Surface | ID / count | Detail | M8 action |
| --- | --- | --- | --- |
| **Attributes** | 7 defs | IDs **16**, **105–109**, **111** — names contain `ТЕСТ` or placeholder «Параметр» | Remove from filter surface + delete/archive defs |
| **Attribute values** | 1 SKU × 6 attrs | Product **3071** — all ТЕСТ attrs filled (шир/выс/дл/марка стали/толщина столешницы/толщина ног) | Clean SKU or deactivate |
| **Products (active)** | **1** | **3071** — «Стол производственный СПБ-С-10/6 … **ТЕ…**» (name truncated in DB export; matches `%тест%`) | Rename/deactivate/remove |
| **Products (name search list)** | 0 other rows | No additional rows in top-200 name/model search beyond 3071 | — |
| **OpenCart filters** | 0 | `oc_filter` / groups — no TEST names | — |
| **Option values** | 0 | — | — |
| **Manufacturers** | 0 | 1 manufacturer total; no TEST name | — |

### TEST attribute detail

| ID | Название | filter_name | Товаров | В фильтре сегодня |
| --- | --- | --- | --- | --- |
| 16 | Параметр | param | 0 | Нет |
| 105 | шир ТЕСТ | shir-test | 1 | Да |
| 106 | выс ТЕСТ | vys-test | 1 | Да |
| 107 | дл ТЕСТ | dl-test | 1 | Да |
| 108 | марка стали ТЕСТ | marka-stali-test | 1 | Да |
| 109 | толщина столешницы ТЕСТ | tolschina-stoleshnicy-test | 1 | Да |
| 111 | толщина материала ног ТЕСТ | tolschina-materiala-nog-test | 1 | Да |

### Product 3071 — TEST attribute values

| attribute_id | name | value |
| ---: | --- | --- |
| 105 | шир ТЕСТ | 0,6 |
| 106 | выс ТЕСТ | 0,85 |
| 107 | дл ТЕСТ | 1 |
| 108 | марка стали ТЕСТ | 430 |
| 109 | толщина столешницы ТЕСТ | 0,7 |
| 111 | толщина материала ног ТЕСТ | 1,5 |

### False positives (NOT cleanup targets)

| category_id | name | reason |
| ---: | --- | --- |
| 189 | Тестомесы | Legitimate «тесто-*» product category name — not QA artifact |
| 193 | Тестораскатки, тестозакатки | Legitimate «тесто-*» product category name — not QA artifact |
| 194 | Тестоделители и тестоокруглители | Legitimate «тесто-*» product category name — not QA artifact |

## Attribute Registry Summary

| Classification | Count |
| --- | ---: |
| COMMERCIAL | 30 |
| TECHNICAL | 15 |
| SERVICE | 4 |
| TEST | 7 |

| Filter relevance | Count |
| --- | ---: |
| SHOW TO CUSTOMER | 18 |
| REVIEW | 7 |
| HIDE FROM CUSTOMER | 31 |

### Universal dimension fields (`oc_product`, not attributes)

| Field | Filled (active SKUs) |
| --- | ---: |
| length | 586 / 609 |
| width | 586 / 609 |
| height | 586 / 609 |
| weight | 531 / 609 |

These fields power Hero + physical range filters on PLP and should be treated as **primary commercial filters** in M9 profiles.

### Full registry (56 rows captured)

| ID | Название | Группа | Класс | Товаров | Кат. | Фильтр | Релевантность |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | Габариты нетто (мм) | Габариты | TECHNICAL | 54 | 4 | Yes | HIDE FROM CUSTOMER |
| 13 | Габариты брутто (мм) | Габариты | TECHNICAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 14 | Борт | Нейтральное оборудование | COMMERCIAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 15 | Гарантия | Общие | COMMERCIAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 16 | Параметр | Общие | TEST | 0 | 0 | No | HIDE FROM CUSTOMER |
| 17 | В комплекте | Общие | COMMERCIAL | 45 | 10 | Yes | SHOW TO CUSTOMER |
| 18 | Высота борта (мм) | Общие | COMMERCIAL | 380 | 28 | Yes | SHOW TO CUSTOMER |
| 19 | Количество уровней направляющих | Нейтральное оборудование | COMMERCIAL | 3 | 1 | Yes | REVIEW |
| 20 | Макс. нагрузка (до, кг) | Общие | COMMERCIAL | 427 | 18 | Yes | SHOW TO CUSTOMER |
| 21 | Конструкция | Общие | COMMERCIAL | 599 | 36 | Yes | SHOW TO CUSTOMER |
| 22 | Материал столешницы | Нейтральное оборудование | COMMERCIAL | 535 | 30 | Yes | SHOW TO CUSTOMER |
| 23 | Мойка | Нейтральное оборудование | COMMERCIAL | 192 | 18 | Yes | SHOW TO CUSTOMER |
| 24 | Назначение секции | Нейтральное оборудование | COMMERCIAL | 4 | 2 | Yes | REVIEW |
| 25 | Наличие борта | Нейтральное оборудование | COMMERCIAL | 569 | 32 | Yes | SHOW TO CUSTOMER |
| 26 | Ножки | Общие | COMMERCIAL | 579 | 35 | Yes | SHOW TO CUSTOMER |
| 27 | Обвязка | Нейтральное оборудование | TECHNICAL | 7 | 2 | Yes | HIDE FROM CUSTOMER |
| 28 | Отверстие под смеситель | Нейтральное оборудование | COMMERCIAL | 192 | 18 | Yes | SHOW TO CUSTOMER |
| 29 | Размер раковины (ДхШхВ, мм) | Нейтральное оборудование | COMMERCIAL | 190 | 17 | Yes | SHOW TO CUSTOMER |
| 30 | Размер секции | Нейтральное оборудование | COMMERCIAL | 3 | 1 | Yes | REVIEW |
| 31 | Регулируемость опоры по высоте (max мм) | Нейтральное оборудование | COMMERCIAL | 545 | 31 | Yes | SHOW TO CUSTOMER |
| 32 | Тип крепления | Нейтральное оборудование | COMMERCIAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 33 | Тип опоры | Нейтральное оборудование | COMMERCIAL | 580 | 35 | Yes | SHOW TO CUSTOMER |
| 34 | Страна производства | Общие | TECHNICAL | 55 | 4 | Yes | HIDE FROM CUSTOMER |
| 36 | Обвязка | Другое | TECHNICAL | 17 | 4 | Yes | HIDE FROM CUSTOMER |
| 38 | Количество | Другое | COMMERCIAL | 30 | 9 | Yes | SHOW TO CUSTOMER |
| 42 | Стандарт | Другое | TECHNICAL | 367 | 0 | Yes | HIDE FROM CUSTOMER |
| 43 | Дополнительные сведения | Другое | SERVICE | 974 | 0 | Yes | HIDE FROM CUSTOMER |
| 44 | Длина в упаковке (мм) | Другое | TECHNICAL | 531 | 0 | Yes | HIDE FROM CUSTOMER |
| 45 | Ширина в упаковке (мм) | Другое | TECHNICAL | 531 | 0 | Yes | HIDE FROM CUSTOMER |
| 46 | Высота в упаковке (мм) | Другое | TECHNICAL | 531 | 0 | Yes | HIDE FROM CUSTOMER |
| 47 | Конструкция борта | Другое | COMMERCIAL | 152 | 0 | Yes | SHOW TO CUSTOMER |
| 48 | Комплект поставки | Другое | SERVICE | 111 | 0 | Yes | HIDE FROM CUSTOMER |
| 49 | Производитель | Другое | COMMERCIAL | 18 | 6 | Yes | SHOW TO CUSTOMER |
| 50 | Тип крепления | Другое | COMMERCIAL | 1 | 1 | Yes | REVIEW |
| 51 | Конструкция полки | Другое | COMMERCIAL | 435 | 0 | Yes | SHOW TO CUSTOMER |
| 52 | Упаковка (Длина, мм) | Другое | TECHNICAL | 29 | 8 | Yes | HIDE FROM CUSTOMER |
| 53 | Упаковка (Ширина, мм) | Другое | TECHNICAL | 29 | 8 | Yes | HIDE FROM CUSTOMER |
| 54 | Упаковка (Высота, мм) | Другое | TECHNICAL | 29 | 8 | Yes | HIDE FROM CUSTOMER |
| 55 | Упаковка (вес брутто, кг) | Другое | TECHNICAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 56 | Упаковка (Объем, м. куб.) | Другое | TECHNICAL | 535 | 0 | Yes | HIDE FROM CUSTOMER |
| 57 | Вес (нетто, кг) | Другое | TECHNICAL | 28 | 7 | Yes | HIDE FROM CUSTOMER |
| 58 | Комплект отгрузки | Другое | SERVICE | 47 | 14 | Yes | HIDE FROM CUSTOMER |
| 102 | Выгрузка | Другое | SERVICE | 0 | 0 | No | HIDE FROM CUSTOMER |
| 103 | 08 Количество уровней направляющих | Другое | COMMERCIAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 104 | 35 Размер секции | Другое | COMMERCIAL | 0 | 0 | No | HIDE FROM CUSTOMER |
| 105 | шир ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 106 | выс ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 107 | дл ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 108 | марка стали ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 109 | толщина столешницы ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 110 | Тип покрытия | Другое | COMMERCIAL | 1 | 1 | Yes | REVIEW |
| 111 | толщина материала ног ТЕСТ | Другое | TEST | 1 | 1 | Yes | HIDE FROM CUSTOMER |
| 112 | Материал полки | Другое | COMMERCIAL | 377 | 14 | Yes | SHOW TO CUSTOMER |
| 113 | Шаг регулировки полки (мм) | Другое | COMMERCIAL | 1 | 1 | Yes | REVIEW |
| 114 | Количество полок (шт) | Другое | COMMERCIAL | 1 | 1 | Yes | REVIEW |
| 115 | Усиление | Другое | COMMERCIAL | 385 | 16 | Yes | SHOW TO CUSTOMER |

**SAFE UNKNOWN:** DB reports **60** attribute definitions; PMA export captured **56** IDs (12–115). Four definitions not present in this export — verify in admin before M8 deletion waves.

## Commercial Attributes

| ID | Название | Группа | Товаров | Категорий | В фильтре | filter_name |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | Конструкция | Общие | 599 | 36 | Yes | construction |
| 33 | Тип опоры | Нейтральное оборудование | 580 | 35 | Yes | type-support |
| 26 | Ножки | Общие | 579 | 35 | Yes | eq-legs |
| 25 | Наличие борта | Нейтральное оборудование | 569 | 32 | Yes | available-board |
| 31 | Регулируемость опоры по высоте (max мм) | Нейтральное оборудование | 545 | 31 | Yes | height-adjustment |
| 22 | Материал столешницы | Нейтральное оборудование | 535 | 30 | Yes | table-top-material |
| 51 | Конструкция полки | Другое | 435 | 0 | Yes | — |
| 20 | Макс. нагрузка (до, кг) | Общие | 427 | 18 | Yes | max-load |
| 115 | Усиление | Другое | 385 | 16 | Yes | usilenie |
| 18 | Высота борта (мм) | Общие | 380 | 28 | Yes | side-height |
| 112 | Материал полки | Другое | 377 | 14 | Yes | material-polki |
| 23 | Мойка | Нейтральное оборудование | 192 | 18 | Yes | washing |
| 28 | Отверстие под смеситель | Нейтральное оборудование | 192 | 18 | Yes | hole-for-mixer |
| 29 | Размер раковины (ДхШхВ, мм) | Нейтральное оборудование | 190 | 17 | Yes | shell-size |
| 47 | Конструкция борта | Другое | 152 | 0 | Yes | — |
| 17 | В комплекте | Общие | 45 | 10 | Yes | equipmentpack |
| 38 | Количество | Другое | 30 | 9 | Yes | qty |
| 49 | Производитель | Другое | 18 | 6 | Yes | manuf |
| 24 | Назначение секции | Нейтральное оборудование | 4 | 2 | Yes | section-assignment |
| 19 | Количество уровней направляющих | Нейтральное оборудование | 3 | 1 | Yes | number-guide-levels |
| 30 | Размер секции | Нейтральное оборудование | 3 | 1 | Yes | section-size |
| 50 | Тип крепления | Другое | 1 | 1 | Yes | typefast |
| 110 | Тип покрытия | Другое | 1 | 1 | Yes | tip-pokrytiya |
| 113 | Шаг регулировки полки (мм) | Другое | 1 | 1 | Yes | shag-regulirovki-polki-mm |
| 114 | Количество полок (шт) | Другое | 1 | 1 | Yes | kolichestvo-polok-sht |
| 14 | Борт | Нейтральное оборудование | 0 | 0 | No | bort |
| 15 | Гарантия | Общие | 0 | 0 | No | wty |
| 32 | Тип крепления | Нейтральное оборудование | 0 | 0 | No | mounting-type |
| 103 | 08 Количество уровней направляющих | Другое | 0 | 0 | No | 08-kolichestvo-urovney-napravlyayuschih |
| 104 | 35 Размер секции | Другое | 0 | 0 | No | 35-razmer-sekcii |

**Notes:** Includes sink/table-specific attrs (23–29), load/construction/shelf family (20–22, 51, 112–115). IDs **103–104** are mis-imported duplicates (prefixed «08» / «35») — zero fill; treat as dead.

## Technical Attributes

| ID | Название | Группа | Товаров | Категорий | В фильтре | filter_name |
| --- | --- | --- | --- | --- | --- | --- |
| 56 | Упаковка (Объем, м. куб.) | Другое | 535 | 0 | Yes | — |
| 44 | Длина в упаковке (мм) | Другое | 531 | 0 | Yes | — |
| 45 | Ширина в упаковке (мм) | Другое | 531 | 0 | Yes | — |
| 46 | Высота в упаковке (мм) | Другое | 531 | 0 | Yes | — |
| 42 | Стандарт | Другое | 367 | 0 | Yes | — |
| 34 | Страна производства | Общие | 55 | 4 | Yes | country-origin |
| 12 | Габариты нетто (мм) | Габариты | 54 | 4 | Yes | gn |
| 52 | Упаковка (Длина, мм) | Другое | 29 | 8 | Yes | u_l |
| 53 | Упаковка (Ширина, мм) | Другое | 29 | 8 | Yes | u_s |
| 54 | Упаковка (Высота, мм) | Другое | 29 | 8 | Yes | u_v |
| 57 | Вес (нетто, кг) | Другое | 28 | 7 | Yes | mass_netto |
| 36 | Обвязка | Другое | 17 | 4 | Yes | bind |
| 27 | Обвязка | Нейтральное оборудование | 7 | 2 | Yes | strapping |
| 13 | Габариты брутто (мм) | Габариты | 0 | 0 | No | gb |
| 55 | Упаковка (вес брутто, кг) | Другое | 0 | 0 | No | u_mass |

**Notes:** Packaging cluster **44–46, 52–57, 56** duplicates logistics data. **12** «Габариты нетто» overlaps `oc_product` L/W/H. Hide from customer filters; keep on PDP/specs if filled.

## Service Attributes

| ID | Название | Группа | Товаров | Категорий | В фильтре | filter_name |
| --- | --- | --- | --- | --- | --- | --- |
| 43 | Дополнительные сведения | Другое | 974 | 0 | Yes | — |
| 48 | Комплект поставки | Другое | 111 | 0 | Yes | — |
| 58 | Комплект отгрузки | Другое | 47 | 14 | Yes | deliv_compl |
| 102 | Выгрузка | Другое | 0 | 0 | No | vygruzka |

**Notes:** **43** «Дополнительные сведения» — high fill but ops/junk text (e.g. `!!"№;%ЕПАВЫУ%ЕП` in W1B sample); **58** «Комплект отгрузки» — logistics. Not buyer filter material.

## TEST Attributes

| ID | Название | Группа | Товаров | Категорий | В фильтре | filter_name |
| --- | --- | --- | --- | --- | --- | --- |
| 105 | шир ТЕСТ | Другое | 1 | 1 | Yes | shir-test |
| 106 | выс ТЕСТ | Другое | 1 | 1 | Yes | vys-test |
| 107 | дл ТЕСТ | Другое | 1 | 1 | Yes | dl-test |
| 108 | марка стали ТЕСТ | Другое | 1 | 1 | Yes | marka-stali-test |
| 109 | толщина столешницы ТЕСТ | Другое | 1 | 1 | Yes | tolschina-stoleshnicy-test |
| 111 | толщина материала ног ТЕСТ | Другое | 1 | 1 | Yes | tolschina-materiala-nog-test |
| 16 | Параметр | Общие | 0 | 0 | No | param |

**Notes:** **16** «Параметр» — empty placeholder with filter slug `param`. **105–111** — explicit ТЕСТ naming; appear on product **3071** filter panel today.

## Category Attribute Matrix

Branches under **Нейтральное оборудование** (`parent_id=79`). Attributes listed = used on **≥3 active SKUs** in branch (non-empty text).

### Моечные ванны (category_id **80**, **152** active SKUs)

- **Тип опоры** (ID 33, 149 SKU, COMMERCIAL)
- **Наличие борта** (ID 25, 149 SKU, COMMERCIAL)
- **Мойка** (ID 23, 149 SKU, COMMERCIAL)
- **Отверстие под смеситель** (ID 28, 149 SKU, COMMERCIAL)
- **Конструкция** (ID 21, 149 SKU, COMMERCIAL)
- **Ножки** (ID 26, 148 SKU, COMMERCIAL)
- **Размер раковины (ДхШхВ, мм)** (ID 29, 147 SKU, COMMERCIAL)
- **Высота борта (мм)** (ID 18, 140 SKU, COMMERCIAL)
- **Регулируемость опоры по высоте (max мм)** (ID 31, 114 SKU, COMMERCIAL)
- **Упаковка (Объем, м. куб.)** (ID 56, 113 SKU, TECHNICAL)
- **Длина в упаковке (мм)** (ID 44, 111 SKU, TECHNICAL)
- **Дополнительные сведения** (ID 43, 111 SKU, SERVICE)
- **Комплект поставки** (ID 48, 111 SKU, SERVICE)
- **Высота в упаковке (мм)** (ID 46, 111 SKU, TECHNICAL)
- **Ширина в упаковке (мм)** (ID 45, 111 SKU, TECHNICAL)

### Столы (category_id **301**, **420** active SKUs)

- **Высота в упаковке (мм)** (ID 46, 420 SKU, TECHNICAL)
- **Регулируемость опоры по высоте (max мм)** (ID 31, 420 SKU, COMMERCIAL)
- **Ширина в упаковке (мм)** (ID 45, 420 SKU, TECHNICAL)
- **Материал столешницы** (ID 22, 420 SKU, COMMERCIAL)
- **Длина в упаковке (мм)** (ID 44, 420 SKU, TECHNICAL)
- **Конструкция** (ID 21, 420 SKU, COMMERCIAL)
- **Упаковка (Объем, м. куб.)** (ID 56, 420 SKU, TECHNICAL)
- **Конструкция полки** (ID 51, 420 SKU, COMMERCIAL)
- **Ножки** (ID 26, 420 SKU, COMMERCIAL)
- **Наличие борта** (ID 25, 420 SKU, COMMERCIAL)
- **Тип опоры** (ID 33, 420 SKU, COMMERCIAL)
- **Дополнительные сведения** (ID 43, 419 SKU, SERVICE)
- **Макс. нагрузка (до, кг)** (ID 20, 419 SKU, COMMERCIAL)
- **Усиление** (ID 115, 377 SKU, COMMERCIAL)
- **Материал полки** (ID 112, 377 SKU, COMMERCIAL)

### Столы производственные (category_id **87**, **0** active SKUs)

_No attributes with ≥3 filled SKUs._

### Тележки (category_id **85**, **0** active SKUs)

_No attributes with ≥3 filled SKUs._

### Тележки сервировочные (category_id **326**, **3** active SKUs)

- **Стандарт** (ID 42, 3 SKU, TECHNICAL)

### Зонты вытяжные (category_id **207**, **23** active SKUs)

- **Страна производства** (ID 34, 22 SKU, TECHNICAL)
- **Габариты нетто (мм)** (ID 12, 22 SKU, TECHNICAL)
- **Конструкция** (ID 21, 19 SKU, COMMERCIAL)

### Подтоварники и подставки (category_id **322**, **11** active SKUs)

- **Упаковка (Высота, мм)** (ID 54, 11 SKU, TECHNICAL)
- **Материал столешницы** (ID 22, 11 SKU, COMMERCIAL)
- **Тип опоры** (ID 33, 11 SKU, COMMERCIAL)
- **Упаковка (Ширина, мм)** (ID 53, 11 SKU, TECHNICAL)
- **Конструкция** (ID 21, 11 SKU, COMMERCIAL)
- **Регулируемость опоры по высоте (max мм)** (ID 31, 11 SKU, COMMERCIAL)
- **Упаковка (Длина, мм)** (ID 52, 11 SKU, TECHNICAL)
- **Конструкция полки** (ID 51, 11 SKU, COMMERCIAL)
- **Вес (нетто, кг)** (ID 57, 11 SKU, TECHNICAL)
- **Ножки** (ID 26, 11 SKU, COMMERCIAL)
- **Стандарт** (ID 42, 11 SKU, TECHNICAL)
- **Количество** (ID 38, 11 SKU, COMMERCIAL)
- **Макс. нагрузка (до, кг)** (ID 20, 8 SKU, COMMERCIAL)
- **Усиление** (ID 115, 8 SKU, COMMERCIAL)
- **Размер секции** (ID 30, 3 SKU, COMMERCIAL)

### Summary matrix (commercial attrs only, top 8 per branch)

| Category | SKUs | Key commercial attributes |
| --- | ---: | --- |
| Моечные ванны | 152 | Размер раковины (29), Мойка (23), Отверстие под смеситель (28), Наличие борта (25), Конструкция (21), Высота борта (18), Конструкция борта (47) |
| Столы | 420 | Материал столешницы (22), Конструкция полки (51), Макс. нагрузка (20), Конструкция (21), Тип опоры (33), Наличие борта (25), Материал полки (112), Усиление (115) + L/W/H из oc_product |
| Тележки сервировочные | 3 | Стандарт (42) only — **3 SKU**; insufficient data for rich profile |
| Зонты вытяжные | 23 | Страна производства (34), Конструкция (21) + L/W/H |
| Подтоварники и подставки | 11 | Конструкция полки (51), Макс. нагрузка (20), Материал столешницы (22) |

## Filter Relevance Audit

Per-attribute recommendation for M9 filter profiles. Today **all filled attributes surface dynamically** — M8/M9 must **exclude** SERVICE/TECHNICAL/TEST by profile rules.

### SHOW TO CUSTOMER

| ID | Название | Товаров | Причина |
| --- | --- | --- | --- |
| 21 | Конструкция | 599 | Commercial attribute with meaningful catalog fill |
| 33 | Тип опоры | 580 | Commercial attribute with meaningful catalog fill |
| 26 | Ножки | 579 | Commercial attribute with meaningful catalog fill |
| 25 | Наличие борта | 569 | Commercial attribute with meaningful catalog fill |
| 31 | Регулируемость опоры по высоте (max мм) | 545 | Commercial attribute with meaningful catalog fill |
| 22 | Материал столешницы | 535 | Commercial attribute with meaningful catalog fill |
| 51 | Конструкция полки | 435 | W1B baseline fill — category_count not re-queried |
| 20 | Макс. нагрузка (до, кг) | 427 | Commercial attribute with meaningful catalog fill |
| 115 | Усиление | 385 | supplement merge |
| 18 | Высота борта (мм) | 380 | Commercial attribute with meaningful catalog fill |
| 112 | Материал полки | 377 | supplement merge |
| 23 | Мойка | 192 | Commercial attribute with meaningful catalog fill |
| 28 | Отверстие под смеситель | 192 | Commercial attribute with meaningful catalog fill |
| 29 | Размер раковины (ДхШхВ, мм) | 190 | Commercial attribute with meaningful catalog fill |
| 47 | Конструкция борта | 152 | W1B baseline fill — category_count not re-queried |
| 17 | В комплекте | 45 | Commercial attribute with meaningful catalog fill |
| 38 | Количество | 30 | supplement merge |
| 49 | Производитель | 18 | supplement merge |

### REVIEW

| ID | Название | Товаров | Причина |
| --- | --- | --- | --- |
| 24 | Назначение секции | 4 | Low fill (4 products) — category-specific relevance |
| 19 | Количество уровней направляющих | 3 | Low fill (3 products) — category-specific relevance |
| 30 | Размер секции | 3 | Low fill (3 products) — category-specific relevance |
| 50 | Тип крепления | 1 | supplement merge |
| 110 | Тип покрытия | 1 | supplement merge |
| 113 | Шаг регулировки полки (мм) | 1 | supplement merge |
| 114 | Количество полок (шт) | 1 | supplement merge |

### HIDE FROM CUSTOMER

| ID | Название | Товаров | Причина |
| --- | --- | --- | --- |
| 43 | Дополнительные сведения | 974 | W1B baseline fill — category_count not re-queried |
| 56 | Упаковка (Объем, м. куб.) | 535 | W1B baseline fill — category_count not re-queried |
| 44 | Длина в упаковке (мм) | 531 | W1B baseline fill — category_count not re-queried |
| 45 | Ширина в упаковке (мм) | 531 | W1B baseline fill — category_count not re-queried |
| 46 | Высота в упаковке (мм) | 531 | W1B baseline fill — category_count not re-queried |
| 42 | Стандарт | 367 | W1B baseline fill — category_count not re-queried |
| 48 | Комплект поставки | 111 | W1B baseline fill — category_count not re-queried |
| 34 | Страна производства | 55 | Logistics/packaging — PDP specs only |
| 12 | Габариты нетто (мм) | 54 | Logistics/packaging — PDP specs only |
| 58 | Комплект отгрузки | 47 | supplement merge |
| 52 | Упаковка (Длина, мм) | 29 | supplement merge |
| 53 | Упаковка (Ширина, мм) | 29 | supplement merge |
| 54 | Упаковка (Высота, мм) | 29 | supplement merge |
| 57 | Вес (нетто, кг) | 28 | supplement merge |
| 36 | Обвязка | 17 | Logistics/packaging — PDP specs only |
| 27 | Обвязка | 7 | Logistics/packaging — PDP specs only |
| 105 | шир ТЕСТ | 1 | supplement merge |
| 106 | выс ТЕСТ | 1 | supplement merge |
| 107 | дл ТЕСТ | 1 | supplement merge |
| 108 | марка стали ТЕСТ | 1 | supplement merge |
| 109 | толщина столешницы ТЕСТ | 1 | supplement merge |
| 111 | толщина материала ног ТЕСТ | 1 | supplement merge |
| 13 | Габариты брутто (мм) | 0 | Zero products — dead attribute |
| 14 | Борт | 0 | Zero products — dead attribute |
| 15 | Гарантия | 0 | Zero products — dead attribute |
| 16 | Параметр | 0 | TEST attribute — M8 cleanup target |
| 32 | Тип крепления | 0 | Zero products — dead attribute |
| 55 | Упаковка (вес брутто, кг) | 0 | supplement merge |
| 102 | Выгрузка | 0 | supplement merge |
| 103 | 08 Количество уровней направляющих | 0 | supplement merge |
| 104 | 35 Размер секции | 0 | supplement merge |

## Dead Attributes

Zero active products with non-empty value.

| ID | Название | Группа | Товаров | Категорий | В фильтре | filter_name |
| --- | --- | --- | --- | --- | --- | --- |
| 13 | Габариты брутто (мм) | Габариты | 0 | 0 | No | gb |
| 14 | Борт | Нейтральное оборудование | 0 | 0 | No | bort |
| 15 | Гарантия | Общие | 0 | 0 | No | wty |
| 16 | Параметр | Общие | 0 | 0 | No | param |
| 32 | Тип крепления | Нейтральное оборудование | 0 | 0 | No | mounting-type |
| 55 | Упаковка (вес брутто, кг) | Другое | 0 | 0 | No | u_mass |
| 102 | Выгрузка | Другое | 0 | 0 | No | vygruzka |
| 103 | 08 Количество уровней направляющих | Другое | 0 | 0 | No | 08-kolichestvo-urovney-napravlyayuschih |
| 104 | 35 Размер секции | Другое | 0 | 0 | No | 35-razmer-sekcii |

### Duplicate / import garbage

| id1 | name1 | id2 | name2 |
| --- | --- | --- | --- |
| 12 | Габариты нетто (мм) | 13 | Габариты брутто (мм) |
| 14 | Борт | 18 | Высота борта (мм) |
| 14 | Борт | 25 | Наличие борта |
| 14 | Борт | 47 | Конструкция борта |
| 17 | В комплекте | 48 | Комплект поставки |
| 17 | В комплекте | 58 | Комплект отгрузки |
| 18 | Высота борта (мм) | 25 | Наличие борта |
| 18 | Высота борта (мм) | 47 | Конструкция борта |
| 25 | Наличие борта | 47 | Конструкция борта |
| 44 | Длина в упаковке (мм) | 45 | Ширина в упаковке (мм) |
| 44 | Длина в упаковке (мм) | 46 | Высота в упаковке (мм) |
| 44 | Длина в упаковке (мм) | 52 | Упаковка (Длина, мм) |
| 44 | Длина в упаковке (мм) | 53 | Упаковка (Ширина, мм) |
| 44 | Длина в упаковке (мм) | 54 | Упаковка (Высота, мм) |
| 44 | Длина в упаковке (мм) | 55 | Упаковка (вес брутто, кг) |
| 44 | Длина в упаковке (мм) | 56 | Упаковка (Объем, м. куб.) |
| 45 | Ширина в упаковке (мм) | 46 | Высота в упаковке (мм) |
| 45 | Ширина в упаковке (мм) | 52 | Упаковка (Длина, мм) |
| 45 | Ширина в упаковке (мм) | 53 | Упаковка (Ширина, мм) |
| 45 | Ширина в упаковке (мм) | 54 | Упаковка (Высота, мм) |

**Packaging duplication:** IDs **44–46** vs **52–54** vs **56** — same logistics plane; consolidate in CMS long-term.

**Bort cluster:** ID **14** «Борт» empty; **25** «Наличие борта» + **18** «Высота борта» + **47** «Конструкция борта» — use 25/18/47; retire 14.

**Mis-import:** **103** «08 Количество уровней…», **104** «35 Размер секции» — duplicate naming of **19** / **30** with zero fill.

## M9 Preparation Notes

Preliminary filter profile inputs per major neutral-equipment branch. **Not implementation** — input for ROAD-003/004 profile design.

| Category | Primary filters | Secondary filters | Hidden filters |
| --- | --- | --- | --- |
| Моечные ванны | L/W/H/weight (product), Размер раковины (29), Мойка (23), Наличие борта (25) | Отверстие под смеситель (28), Конструкция (21), Высота борта (18), Конструкция борта (47) | All packaging (44–46, 52–57), TEST, 43, 58, 12 |
| Столы | L/W/H/weight, Материал столешницы (22), Конструкция полки (51), Макс. нагрузка (20) | Тип опоры (33), Наличие борта (25), Материал полки (112), Усиление (115), Конструкция (21) | Packaging cluster, TEST, 43, 58, 12, Страна (34) |
| Тележки / сервировочные | L/W/H/weight only (3 SKU — profile minimal until assortment grows) | Стандарт (42) if still filled | All attrs until N≥20 SKUs |
| Зонты вытяжные | L/W/H/weight, Конструкция (21) | Страна производства (34) | Packaging, 43, TEST |
| Подтоварники и подставки | L/W/H/weight, Конструкция полки (51), Макс. нагрузка (20) | Материал столешницы (22), Тип опоры (33) | Packaging, TEST, 43 |

**Global hidden (all neutral profiles):** TEST attrs 16, 105–111; SERVICE 43, 58, 102; empty defs 13–16, 32, 35, 55, 103–104; native `oc_filter` (unused).

**Global primary (all neutral profiles):** Price, availability toggles (existing), L/W/H/weight ranges.

## Recommended Cleanup Order

1. **Product 3071** — deactivate or strip TEST attrs / rename SKU (only active product with TEST in name + all ТЕСТ attrs).

2. **TEST attribute definitions** — IDs 105–111, then placeholder **16** «Параметр» (verify no new assignments).

3. **Dead attribute defs** — 13, 14, 15, 32, 35, 55, 102–104 (after admin confirms zero assignments on inactive SKUs).

4. **SERVICE field hygiene** — audit **43** «Дополнительные сведения» for junk; stop filter surfacing via M9 profile (do not mass-delete values in M8).

5. **Packaging filter noise** — hide 44–46, 52–57 from PLP filters via M9; CMS consolidation deferred.

6. **False-positive category names** — **no action** on «Тестомесы» etc. (thermal dough equipment).

7. **M9 filter profiles** — after M8 TEST removal verified on TEST storefront.


---

## Evidence & limitations

| Item | Source |
| --- | --- |
| Live counts | TEST DB `polygonws_zpm` read-only SQL via phpMyAdmin, 2026-06-14 UTC |
| Filter mechanism | `getAttributesByCategory()` in `product_model.php` (SITE-002 trace) |
| W1B cross-check | `.recovery-temp/site-002-w1b-db-final.json` (2026-06-09) — fill rates consistent (609 active) |
| M7.1 state | `SITE-002-M7.1-TEST-DEPLOYMENT.md` — Launch Mode deployed 2026-06-14 |
| M6 formal report | **SAFE UNKNOWN in-repo** — roadmap lists M6 as Planned; this M8.1 audit subsumes attribute/filter inventory scope |

## UNKNOWN / SECURITY RISK

- **UNKNOWN:** 4 attribute IDs not exported in this PMA run (60 DB count vs 56 registry rows).
- **UNKNOWN:** Whether product 3071 is linked on visible PLP/search after M7.1 (active status=1).
- **SECURITY RISK:** DB credentials used read-only from existing OCPilot recovery scripts — not committed in this document.

*Documentation only. No cleanup performed. No implementation authorized.*
