# DUPLICATE ADS MATRIX v1

**Label:** `orca-commander-duplicate-ads-matrix-v1`  
**Date:** 2026-05-29  
**Instance:** `triumph-s-tier-draft-v1.json`  
**Transport analyzed:** `mapTemplateFillRows()` → Commander sheet **Тексты** (sheet1 patch)

**Duplicate criterion:** `headline_1` + `headline_2` + `description` + `landing_url` match within the same group.

**Source key:** `C` = exporter-cli `mapTemplateFillRows` · `A` = would be JSON (none found) · `D` = XLSX 1:1 transport of C.

---

## Summary counts

| Metric | Value |
|--------|-------|
| Groups audited | 12 |
| Unique ads (JSON) | 20 |
| Template-fill rows | 108 |
| Duplicate signatures | 20 |
| Extra ad copies (transport) | 88 |
| Affected groups | 12 |

---

## Matrix

| Group | Ad headline | Expected count | Actual count | Duplicate count | Source | Severity |
|-------|-------------|----------------|--------------|-----------------|--------|----------|
| 01 — Манипулятор 5 тонн | Манипулятор 5 тонн в Краснодаре | 1 | 6 | 5 | C (+D) | Critical |
| 01 — Манипулятор 5 тонн | Манипулятор 5т - подача на объект | 1 | 6 | 5 | C (+D) | Critical |
| 02 — Перевозка бытовок | Перевозка бытовок в Краснодаре | 1 | 5 | 4 | C (+D) | High |
| 02 — Перевозка бытовок | Манипулятор для бытовки | 1 | 5 | 4 | C (+D) | High |
| 03 — Доставка стройматериалов | Доставка стройматериалов манипулятором | 1 | 5 | 4 | C (+D) | High |
| 04 — Манипулятор для юрлиц | Манипулятор для юрлиц | 1 | 4 | 3 | C (+D) | Medium |
| 04 — Манипулятор для юрлиц | Манипулятор безнал краснодар | 1 | 4 | 3 | C (+D) | Medium |
| 05 — Манипулятор-вездеход 6x6 | Манипулятор-вездеход 6x6 | 1 | 5 | 4 | C (+D) | High |
| 06 — Перевозка оборудования | Перевозка оборудования | 1 | 5 | 4 | C (+D) | High |
| 06 — Перевозка оборудования | Манипулятор для оборудования | 1 | 5 | 4 | C (+D) | High |
| 07 — Перевозка контейнеров | Перевозка контейнера | 1 | 5 | 4 | C (+D) | High |
| 08 — Перевозка арматуры | Перевозка арматуры | 1 | 5 | 4 | C (+D) | High |
| 08 — Перевозка арматуры | Доставка арматуры краснодар | 1 | 5 | 4 | C (+D) | High |
| 09 — Доставка кирпича и блоков | Доставка кирпича манипулятором | 1 | 5 | 4 | C (+D) | High |
| 10 — ФБС и ЖБИ | Перевозка ФБС манипулятором | 1 | 6 | 5 | C (+D) | Critical |
| 10 — ФБС и ЖБИ | Манипулятор для ЖБИ | 1 | 6 | 5 | C (+D) | Critical |
| 11 — Манипулятор по Краснодарскому краю | Манипулятор по Краснодарскому краю | 1 | 6 | 5 | C (+D) | Critical |
| 11 — Манипулятор по Краснодарскому краю | Манипулятор межгород по краю | 1 | 6 | 5 | C (+D) | Critical |
| 12 — Заказать манипулятор | Заказать манипулятор в Краснодаре | 1 | 7 | 6 | C (+D) | Critical |
| 12 — Заказать манипулятор | Аренда манипулятора Краснодар | 1 | 7 | 6 | C (+D) | Critical |

---

## Phase 1 reference (group roll-up)

| group_id | group_name | ads | keywords | fill rows |
|----------|------------|-----|----------|-----------|
| grp_fc01_5ton | 01 — Манипулятор 5 тонн | 2 | 6 | 12 |
| grp_fc02_bytovka | 02 — Перевозка бытовок | 2 | 5 | 10 |
| grp_fc03_stroymaterialy | 03 — Доставка стройматериалов | 1 | 5 | 5 |
| grp_fc04_yurlica | 04 — Манипулятор для юрлиц | 2 | 4 | 8 |
| grp_fc05_6x6 | 05 — Манипулятор-вездеход 6x6 | 1 | 5 | 5 |
| grp_fc06_oborudovanie | 06 — Перевозка оборудования | 2 | 5 | 10 |
| grp_fc07_konteynery | 07 — Перевозка контейнеров | 1 | 5 | 5 |
| grp_fc08_armatura | 08 — Перевозка арматуры | 2 | 5 | 10 |
| grp_fc09_kirpich | 09 — Доставка кирпича и блоков | 1 | 5 | 5 |
| grp_fc10_fbs | 10 — ФБС и ЖБИ | 2 | 6 | 12 |
| grp_fc11_kray | 11 — Манипулятор по Краснодарскому краю | 2 | 6 | 12 |
| grp_fc12_zakaz | 12 — Заказать манипулятор | 2 | 7 | 14 |

---

## Formula check

For each row in the matrix:

`Actual count` = `keywords_count` for that group (when `ads_count ≥ 1`).

`Duplicate count` = `Actual count − 1` = `keywords_count − 1`.

Example **01 — Манипулятор 5 тонн** / «Манипулятор 5т - подача на объект»: 6 keywords → 6 Commander-visible copies → **5 duplicates**.

---

## Source attribution (per row)

| Source | Present in matrix? |
|--------|-------------------|
| A — JSON instance | No duplicate rows (Expected = Actual = 1 in JSON) |
| B — `_build-full-cycle-draft.js` | Same as A |
| C — `mapTemplateFillRows` | **Yes — all 20 rows** |
| D — sheet1 XLSX patch | Propagates C 1:1; no extra dedupe |

---

## ad_id cross-reference

| Group | Headline (short) | ad_id |
|-------|------------------|-------|
| 01 | Манипулятор 5 тонн в Краснодаре | ad_fc01_a1 |
| 01 | Манипулятор 5т - подача на объект | ad_fc01_a2 |
| 02 | Перевозка бытовок в Краснодаре | ad_fc02_a1 |
| 02 | Манипулятор для бытовки | ad_fc02_a2 |
| 03 | Доставка стройматериалов манипулятором | ad_fc03_a1 |
| 04 | Манипулятор для юрлиц | ad_fc04_a1 |
| 04 | Манипулятор безнал краснодар | ad_fc04_a2 |
| 05 | Манипулятор-вездеход 6x6 | ad_fc05_a1 |
| 06 | Перевозка оборудования | ad_fc06_a1 |
| 06 | Манипулятор для оборудования | ad_fc06_a2 |
| 07 | Перевозка контейнера | ad_fc07_a1 |
| 08 | Перевозка арматуры | ad_fc08_a1 |
| 08 | Доставка арматуры краснодар | ad_fc08_a2 |
| 09 | Доставка кирпича манипулятором | ad_fc09_a1 |
| 10 | Перевозка ФБС манипулятором | ad_fc10_a1 |
| 10 | Манипулятор для ЖБИ | ad_fc10_a2 |
| 11 | Манипулятор по Краснодарскому краю | ad_fc11_a1 |
| 11 | Манипулятор межгород по краю | ad_fc11_a2 |
| 12 | Заказать манипулятор в Краснодаре | ad_fc12_a1 |
| 12 | Аренда манипулятора Краснодар | ad_fc12_a2 |
