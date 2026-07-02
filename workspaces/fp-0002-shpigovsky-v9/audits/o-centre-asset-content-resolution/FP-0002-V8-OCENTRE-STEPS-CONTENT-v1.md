# FP-0002 V8 O-Centre Steps Content v1

**Charter block:** OC-B05  
**Inventory:** BLK-018 «Этапы процедуры» / rehabilitation requirements steps  
**Figma frame name:** «Этапы процедуры» (`1:2310`)

## Critical finding

The frame named «Этапы процедуры» on Spig_v1.2 O-Centre **does not contain** BLK-018 step content. Extracted texts are **who-we-treat** copy:

| Step | Number | Title | Description | Source | Status |
|---:|---|---|---|---|
| — | — | — | — | — | **MISSING** |

## Actual content in mislabeled frame

| Item | Text | Source | Status |
|---|---|---|---|
| Heading | Разные люди, разные истории — одно общее: что-то пошло не так | `1:2323` | CONFIRMED (OC-B04) |
| Lead | К нам приходят люди, которые устали… | `1:2321` | CONFIRMED |
| Body | Зависимости и пристрастия — алкогольная… | `1:2319` | CONFIRMED |
| Callout | Нас не беспокоит социальный статус… | `1:2316` | CONFIRMED |
| Link | Подробнее | `1:2314` | CONFIRMED |

## BLK-018 search result

No nodes in O-Centre desktop/mobile extract contain:

- «Что нужно для прохождения реабилитации»
- Numbered rehabilitation steps 01–04 (requirements)
- «Связаться с нами» CTA tied to steps block

The strings «01 — Генотипирование» etc. appear in **Программа центра** (program directions), not steps.

## Comparison with existing partial

`home-rehabilitation-requirements.html` copy was **not** proven as an exact match — **do not reuse** without canonical source.

## Result

| Field | Value |
|---|---|
| Heading | **MISSING** |
| CTA | **MISSING** |
| Order | N/A |
| Status | **BLOCKED_MISSING_CANONICAL_SOURCE** |

**Recommendation:** Remove OC-B05 / BLK-018 from O-Centre implementation scope unless operator supplies approved copy or a different Spig_v1.2 frame is identified.
