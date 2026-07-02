# CF-006 Implementation Receipt — Comfort / Facility Gallery Universalization

**Date:** 2026-06-28
**Wave:** CF-006
**Verdict:** COMPLETE — pending operator visual review

## Naming decision

| Field | Value |
| ----- | ----- |
| Selected name | `comfort` |
| Partial | `src/partials/sections/comfort.html` |
| Root class | `.comfort` |
| Gallery hook | `data-fancybox="comfort"` |
| Alternative considered | `clinic-comfort` — not needed |
| Reason | No selector/path conflict with `.comfort`; matches facility comfort gallery function |

## Migration summary

- Old partial removed: `home-comfort.html`
- New partial: `comfort.html`
- Consumers migrated: 5 (`index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`)
- Home heading id neutralized: `comfort-heading` (was `home-comfort-heading`)
- Old class references in active `src/` (excluding asset folder paths): 0
- CSS declaration values: unchanged (selector rename only)
- JS config: unchanged; init renamed to `initComfortFancybox`
- Asset paths: unchanged (`assets/img/content/home-comfort/` — HISTORICAL_ASSET_PATH_PRESERVED)

## Validation

| Check | Result |
| ----- | ------ |
| Baseline build | PASS |
| Post-change build | PASS |
| DOM validation | PASS |
| Selector validation | PASS |
| Protected source | PASS (0 changes) |
| Before browser QA | PASS (10 captures) |
| After browser QA | PASS (10 captures) |
| Visual parity (context crops) | PASS (10/10 exact) |
| Gallery functional QA | PASS (10/10) |

## Evidence

- Backup: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-CF-006-COMFORT-UNIVERSALIZATION.zip`
- Before screenshots: `...\cf-006-evidence\before\`
- After screenshots: `...\cf-006-evidence\after\`
- Manifests: `audits/cf-006-comfort/CF-006-*-SCREENSHOT-MANIFEST.json`
- DOM: `audits/cf-006-comfort/data/CF-006-DOM-VALIDATION.json`
- Selectors: `audits/cf-006-comfort/data/CF-006-SELECTOR-HOOK-VALIDATION.json`
- Visual parity: `audits/cf-006-comfort/CF-006-VISUAL-PARITY-MATRIX.json`
- Gallery QA: `audits/cf-006-comfort/data/CF-006-GALLERY-FUNCTIONAL-QA.json`

## Next wave

CF-008 `home-faq` — **NOT AUTHORIZED**
