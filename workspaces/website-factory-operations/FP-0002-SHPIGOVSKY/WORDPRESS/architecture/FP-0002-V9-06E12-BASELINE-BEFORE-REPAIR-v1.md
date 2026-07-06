# FP-0002 V9-06E12 Baseline Before Repair

**Task:** V9-06E12 Direct Static V9 Port Repair — Alcohol Leaf  
**Date:** 2026-07-07

## Route

`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` — Service CPT #74 (alcohol-special variant)

## Static authority

`workspaces/fp-0002-shpigovsky-v9/src/pages/usluga-konechnaya-v1.html`

## Pre-repair failure mode

Semantic reconstruction via `alcohol-stack.php` orchestrating ACF-driven partials:

- `approach.php` pulled programme_items from ACF (wrong cards, no staff image/highlight/intro)
- `stages.php` returned early without ACF stages (missing lead, support block)
- `faq.php` used ACF faq_items (wrong questions vs static V9)

## Baseline evidence

- `validation/v9-06e12-direct-static-v9-port-repair-alcohol-leaf/baseline-before-repair.json`
- Screenshots: `runtime-alcohol-leaf-before-e12.png`, `static-v9-alcohol-leaf-reference-e12-before.png`

## Pre-repair DOM gaps

| Check | Before |
|---|---|
| staff-image | false |
| stages-lead | false |
| stages-support | false |
| section_count | 16 |
