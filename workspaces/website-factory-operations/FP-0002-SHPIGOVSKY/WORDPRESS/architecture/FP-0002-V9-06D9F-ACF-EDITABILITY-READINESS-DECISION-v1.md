# FP-0002 V9-06D9F ACF / Admin Editability Readiness Decision v1

**Date:** 2026-07-05  
**Task:** V9-06D9-F

## Decision

| Field | Value |
|-------|-------|
| Visual parity readiness | PARTIAL |
| Blocking visual issues | none |
| Minor visual issues | FAQ `comfort-heading` typo + duplicate id |
| Footer QA | PASS |
| Slider/vendor QA | PASS |
| Secondary route safety | PASS |
| **ACF wiring recommended now** | **NO** |
| **Recommended next phase** | **CREATE_V9_06D9G_MICRO_VISUAL_REPAIR_TASK** |

## Reason

Home structure, footer, sliders, assets, and routes are production-safe for continued visual work. One documented transplant defect remains in `faq.php`: wrong heading text, wrong `id`/`aria-labelledby`, and duplicate `comfort-heading` with the comfort section.

Wiring ACF field bindings to FAQ before correcting the DOM contract risks encoding the wrong heading key and accessibility references.

## Micro repair scope (follow-up, not performed here)

File: `theme/shpigovsky/template-parts/home/faq.php`

1. `aria-labelledby="comfort-heading"` → `aria-labelledby="faq-heading"`
2. `id="comfort-heading"` → `id="faq-heading"`
3. Heading text `Комфорт, приватность, забота` → `Нас часто спрашивают`

Then bounded runtime delivery + re-run FAQ slice of D9-F or proceed to D9-G ACF wiring.

## Evidence

`validation/v9-06d9f-home-footer-visual-parity-qa/acf-editability-readiness-decision.json`
