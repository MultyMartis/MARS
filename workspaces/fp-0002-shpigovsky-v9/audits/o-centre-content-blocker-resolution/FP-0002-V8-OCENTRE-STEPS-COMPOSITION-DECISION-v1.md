# FP-0002 V8 O-Centre Steps Composition Decision v1

**Gap:** OC-G06 / OC-B05 / BLK-018
**Date:** 2026-06-29
**Authority:** Spig_v1.2.fig desktop `1:2185`, mobile `1:5519`

## Previous assumption

Preliminary anatomy (charter `62d24fa7`) and early design evidence mapped desktop section «Этапы процедуры» (`1:2310`) to BLK-018 rehabilitation steps (numbered 01–04 + CTA). PG-005 composition row in `FP-0002-BLOCK-INVENTORY-v1.md` line 135 incorrectly lists BLK-018 among About page blocks.

## Canonical Figma evidence (fresh parse 2026-06-29)

| Evidence | Result |
|---|---|
| Desktop section `1:2310` name | «Этапы процедуры» |
| Actual text in `1:2310` | OC-B04 who-we-treat copy (`1:2323`, `1:2321`, `1:2319`, `1:2316`, `1:2314`) |
| BLK-018 strings («Что нужно для прохождения реабилитации», step requirements 01–04) | **Absent** from O-Centre desktop and mobile extracts |
| Numbered strings «01 — Генотипирование» etc. | Present in **Программа центра** (`1:2341`/`1:2401`), not steps block |
| Infrastructure decorative step labels `/04` in `1:2440` | Visual decoration only — not BLK-018 content |

## Inventory evidence

| Source | BLK-018 on PG-005? |
|---|---|
| `FP-0002-BLK-018` row (line 80) | **No** — pages: PG-001…004, PG-006, PG-007 |
| BLK-018 usage matrix (line 292) | **No** checkmark for PG-005 |
| PG-005 composition row (line 135) | Lists `018` — **contradicts BLK-018 row** |
| O-Centre node map `OC-B05` | `desktop_node: null`, confidence UNRESOLVED |

## Classification

**`INVENTORY_LABEL_ERROR`** (composition consequence: **`NOT_PRESENT_IN_CANONICAL_COMPOSITION`**)

The frame name «Этапы процедуры» was misread as BLK-018. Canonical O-Centre composition contains **who-we-treat** at that scroll position, not rehabilitation steps.

## Composition consequence

- Remove OC-B05 / BLK-018 from O-Centre reconciled composition.
- Retire phantom steps fields from content pack and implementation JSON.
- Do **not** invent steps copy or reuse `home-rehabilitation-requirements.html` without canonical proof.

## Inventory correction

Correct PG-005 About composition row: remove `018` from block list (align with BLK-018 row and usage matrix). Historical PG-005 row preserved in charter correction notes.

## Status

**RESOLVED_BY_COMPOSITION_CORRECTION**
