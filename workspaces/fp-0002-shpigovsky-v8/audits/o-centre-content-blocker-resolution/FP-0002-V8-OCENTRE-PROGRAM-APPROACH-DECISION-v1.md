# FP-0002 V8 O-Centre Program Approach Decision v1

**Gap:** OC-G11 / OC-B06 / BLK-020
**Date:** 2026-06-29

## Field classification

| Field | Figma node | Figma text (summary) | Candidate source | Authority | Decision | Status |
|---|---|---|---|---|---|---|
| Subnav label | `1:2243` | Наш подход к лечению | Spig_v1.2 subnav | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Approach H2 (visible) | `1:2343` | Наш подход к лечению **алкогольной зависимости** | — | Figma | PLACEHOLDER_REMOVE_FIELD (service-template leak) | RESOLVED |
| Approach H2 (reconciled) | `1:2243` | Наш подход к лечению | Subnav O-Centre label | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Approach lead 1 | `1:2355` | Мы используем мультидисциплинарный подход… | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Approach lead 2 | `1:2357` | Лечение в нашем реабилитационном центре… | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Card title 1 | `1:2366` | диагностические инструменты | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Card body 1 | `1:2367` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Card title 2 | `1:2369` | Психиатрия | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Card body 2 | `1:2370` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Card title 3 | `1:2384` | Функциональная терапия | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Card body 3 | `1:2385` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Card title 4 | `1:2387` | комплиментарная терапия | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Card body 4 | `1:2388` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Program intro 1 | `1:2406` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Program intro 2 | `1:2408` | Lorem ipsum… | — | — | PLACEHOLDER_OMIT_FIELD | RESOLVED |
| Program heading | `1:2433` | Наша программа включает 4 направления | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Direction 01 | `1:2412` | 01 — Генотипирование | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Direction 02 | `1:2417` | 02 — Нейропсихологическая коррекция | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Direction 03 | `1:2423` | 03 — Психокоррекция | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Direction 04 | `1:2428` | 04 — Кинезиотерапия | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| Foot link | `1:2435` | подробнее | Spig_v1.2 | Canonical Figma | CONFIRMED_OCENTRE_TEXT | RESOLVED |
| CTA band copy | `1:2511` etc. | Запишитесь на гостевой визит | Spig_v1.2 | Canonical Figma | CONFIRMED_REUSE_EXISTING (CF-011) | RESOLVED |

## Summary

| Category | Count |
|---|---:|
| Confirmed O-Centre fields | 14 |
| Reused component fields | 1 (CTA band) |
| Placeholder omitted fields | 6 |
| Required unknown fields | 0 |

## Implementation note

Implement program/approach using `services-program-v2.html` + CF-012 modifiers with **confirmed headings, leads, card titles, and four directions only**. Omit Lorem card bodies and program intro paragraphs. Use subnav label `1:2243` for approach H2 — not service-leak text `1:2343`.

## Status

**RESOLVED_BY_PLACEHOLDER_OMISSION** (section remains; optional Lorem fields excluded)
