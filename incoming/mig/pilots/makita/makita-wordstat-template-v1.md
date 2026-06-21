# Makita Wordstat Template v1 — Operator Helper

**Status:** operator Excel template — manual Wordstat input
**Date:** 2026-06-07
**Pilot:** Makita Snab
**Source:** incoming/mig/pilots/makita/wordstat-collection-sheet-v1.md

---

## File Path

`incoming/mig/pilots/makita/makita-wordstat-template-v1.xlsx`

---

## Operator Instructions

1. Open the Excel file above.
2. For each row, copy `wordstat_query` into [Yandex Wordstat](https://wordstat.yandex.ru/).
3. Set region to **Москва и Московская область** (pre-filled in column `region`).
4. Record the observed monthly query frequency in `wordstat_frequency`.
5. Use `operator_notes` only for collection anomalies (e.g. zero results, ambiguous Wordstat UI, query not found).
6. Do **not** estimate, infer, or rank demand — record only what Wordstat shows.

### What to fill

| Column | Operator action |
|--------|-----------------|
| `wordstat_frequency` | **Fill** — observed Wordstat frequency (integer or exact UI value) |
| `operator_notes` | **Optional** — brief note if collection was unusual |

### What not to change

| Column | Rule |
|--------|------|
| `sku` | Do not edit |
| `product_title` | Do not edit |
| `landing_url` | Do not edit |
| `wordstat_query` | Do not edit — fixed as `makita {sku}` (lowercase SKU) |
| `region` | Do not edit — fixed to **Москва и Московская область** |
| `safe_unknown` | Do not edit — preserved source caveats |

### Query scope (this pass)

- **One query per SKU:** `makita {sku}` only.
- **No** related_query_candidates.
- **No** product-type variants (`пылесос makita …`, `макита …`, etc.).
- **70 rows** — one row per approved SKU.

---

## Columns

| Column | Description |
|--------|-------------|
| `sku` | Product SKU (as listed on makita-snab.ru) |
| `product_title` | Retail product title |
| `landing_url` | Product page URL |
| `wordstat_query` | Primary Wordstat query: `makita ` + lowercase SKU |
| `region` | Wordstat region: Москва и Московская область |
| `wordstat_frequency` | **Operator input** — empty until collected |
| `operator_notes` | **Operator input** — optional collection notes |
| `safe_unknown` | Source caveats; empty unless noted below |

---

## SAFE UNKNOWN

Preserved from source (`demand-surface-seed-list-v1.md` → `safe_unknown` column):

| SKU | safe_unknown |
|-----|--------------|
| DVC265ZXU | product_type inferred from title modifier «ранцевый»; not in canonical short-type list |
| DK0116 | bundle composition not resolved from title alone |
| DK0117 | bundle composition not resolved from title alone |
| DK0167 | bundle composition not resolved from title alone |
| DTD172Z | promo bundle page lists DDF485Z + DTD172Z; seed phrase anchored to listed SKU DTD172Z only |
| KT001GZ | product category outside core power-tool taxonomy; demand_class assigned by rarity |
| TD003GA201 | title lists винтоверт synonym; seed uses шуруповерт as primary retail type |
| SD100DZ | niche saw type retained in product_type per title |

---

## Evidence Pointers

| Ref | Path |
|-----|------|
| Collection sheet source | incoming/mig/pilots/makita/wordstat-collection-sheet-v1.md |
| Seed / safe_unknown source | incoming/mig/pilots/makita/demand-surface-seed-list-v1.md |
| Excel template | incoming/mig/pilots/makita/makita-wordstat-template-v1.xlsx |

---

*Makita Wordstat Template v1 — operator helper · documentation only*
