# CF-005 Implementation Receipt — Specialists Universalization

**Date:** 2026-06-28
**Wave:** CF-005
**Verdict:** COMPLETE — pending operator visual review

## Naming decision

| Field | Value |
| ----- | ----- |
| Selected name | `specialists` |
| Partial | `src/partials/sections/specialists.html` |
| Root class | `.specialists` |
| Slider hooks | `data-specialists-slider`, `data-specialists-pagination` |
| Alternative considered | `specialists-section` — not needed |
| Reason | No selector/path conflict with `.specialists`; matches approved neutral family pattern |

## Migration summary

- Old partial removed: `home-specialists.html`
- New partial: `specialists.html`
- Consumers migrated: 3 (`index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`)
- Home heading id neutralized: `specialists-heading` (was `home-specialists-heading`)
- Old class references in active `src/` (excluding asset folder paths): 0
- CSS declaration values: unchanged (selector rename only)
- JS config: unchanged; init renamed to `initSpecialists`
- Asset paths: unchanged (`assets/img/content/home-specialists/`)

## Validation

| Check | Result |
| ----- | ------ |
| Baseline build | PASS |
| Post-change build | PASS |
| DOM validation | PASS |
| Selector validation | PASS |
| Protected source | PASS (0 changes) |
| Before browser QA | PASS (6 captures) |
| After browser QA | PASS (6 captures) |
| Visual parity | PASS |
| Slider functional QA | PASS |

## Evidence

- Backup: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-CF-005-SPECIALISTS-UNIVERSALIZATION.zip`
- Before screenshots: `...\cf-005-evidence\before\`
- After screenshots: `...\cf-005-evidence\after\`
- Manifests: `audits/cf-005-specialists/CF-005-*-SCREENSHOT-MANIFEST.json`
- DOM: `audits/cf-005-specialists/data/CF-005-DOM-VALIDATION.json`
- Selectors: `audits/cf-005-specialists/data/CF-005-SELECTOR-HOOK-VALIDATION.json`
- Visual parity: `audits/cf-005-specialists/CF-005-VISUAL-PARITY-MATRIX.json`
- Slider QA: `audits/cf-005-specialists/CF-005-SLIDER-FUNCTIONAL-QA.json`

## Next wave

CF-006 `home-comfort` — **NOT AUTHORIZED**
