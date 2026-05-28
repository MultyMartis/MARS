# Campaign Structure v1.1

**Document ID:** `triumph-manipulator-krd-search-full-cycle-v1` (unchanged)  
**Campaign:** `camp_triumph_search_full_cycle_v1` — «Триумф — Поиск — Full Cycle v1»

## Intent groups (12)

| # | Group | Slug | Display path | Ads | Keywords |
|---|--------|------|--------------|-----|----------|
| 01 | Манипулятор 5 тонн | `/manipulyator-5-tonn/` | `manip-5-tonn` | 2 | 6 |
| 02 | Перевозка бытовок | `/perevozka-bytovok/` | `bytovki` | 2 | 5 |
| 03 | Доставка стройматериалов | `/dostavka-stroymaterialov/` | `stroymaterialy` | 1 | 5 |
| 04 | Манипулятор для юрлиц | `/manipulyator-dlya-yurlic/` | `dlya-yurlic` | 2 | 4 |
| 05 | Манипулятор-вездеход 6x6 | `/manipulyator-vezdehod/` | `vezdehod-6x6` | 1 | 5 |
| 06 | Перевозка оборудования | `/perevozka-oborudovaniya/` | `oborudovanie` | 2 | 5 |
| 07 | Перевозка контейнеров | `/perevozka-konteynerov/` | `konteynery` | 1 | 5 |
| 08 | Перевозка арматуры | `/perevozka-armatury/` | `armatura` | 2 | 5 |
| 09 | Доставка кирпича и блоков | `/dostavka-kirpicha-blokov/` | `kirpich-bloki` | 1 | 5 |
| 10 | ФБС и ЖБИ | `/perevozka-fbs-zhbi/` | `fbs-zhbi` | 2 | 6 |
| **11** | **Манипулятор по Краснодарскому краю** | `/manipulyator-krasnodarskiy-kray/` | `kray` | 2 | 6 |
| **12** | **Заказать манипулятор** | `/` (master hot) | `zakaz-manip` | 2 | 7 |

**Totals:** 20 ads · 64 keywords · Commander fill rows **108** (keyword×ad matrix).

## New intent coverage

| Group | Intent signals | Landing blueprint |
|-------|----------------|-------------------|
| 11 | по краю, межгород, район, выезд, доставка по краю | `08-intercity-krai` |
| 12 | заказать, вызвать, цена, аренда, манипулятор Краснодар | `01-master-hot-general` |

## Copy discipline (new groups)

- **11:** Краснодарский край and межгород in copy; no fake fleet; no cities outside service policy (group negatives: москва, спб).
- **12:** Commercial CTA (звонок, расчёт); capability facts 5 т / 3 т only; phrase match; group negatives block employment and asset-purchase junk.

## SAFE UNKNOWN slugs

| Slug | Notes |
|------|--------|
| `/perevozka-oborudovaniya/` | Carried from v1 — blueprint exists; live URL not verified in this pass. |
| `/manipulyator-krasnodarskiy-kray/` | Blueprint `08-intercity-krai.md` — **live URL not verified** in this pass. |
| `/` (homepage) | Master hot blueprint — **live homepage PPC fit not verified** in this pass. |
