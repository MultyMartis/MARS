# CF-008 Implementation Receipt — FAQ / Accordion Universalization

**Date:** 2026-06-28
**Wave:** CF-008
**Verdict:** COMPLETE — pending operator visual review

## Naming decision

| Field | Value |
| ----- | ----- |
| Selected name | `faq` |
| Partial | `src/partials/sections/faq.html` |
| Root class | `.faq` |
| Accordion hooks | `data-accordion`, `data-accordion-button`, `data-accordion-panel` (unchanged) |
| Init function | global `[data-accordion]` in `main.js` (unchanged — not name-scoped) |
| Alternative considered | `faq-section` — not needed |
| Reason | No `.faq` selector/path conflict in active V8 source |

## Migration summary

- Old partial removed: `home-faq.html`
- New partial: `faq.html`
- Consumers migrated: 5 (`index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`)
- Old class references in active `src/`: 0
- CSS declaration values: unchanged (selector rename only)
- JS accordion behavior: unchanged
- ID prefix: `home-faq-*` → `faq-*` (component-internal); `home-faq-heading` → `faq-heading` on hub pages

## Validation

| Check | Result |
| ----- | ------ |
| Baseline build | PASS |
| Post-change build | PASS |
| DOM/ARIA validation | PASS |
| Selector validation | PASS |
| Protected source | PASS (0 changes) |
| Before browser QA | PASS (20 captures) |
| After browser QA | PASS (20 captures) |
| Visual parity (crop + context) | PASS (40/40 exact) |
| Accordion functional QA | PASS (10/10) |

## Evidence

- Backup: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-CF-008-FAQ-UNIVERSALIZATION.zip`
- Before screenshots: `...\cf-008-evidence\before\`
- After screenshots: `...\cf-008-evidence\after\`
- Manifests: `audits/cf-008-faq/CF-008-*-SCREENSHOT-MANIFEST.json`
- DOM: `audits/cf-008-faq/data/CF-008-DOM-ARIA-VALIDATION.json`
- Selectors: `audits/cf-008-faq/data/CF-008-SELECTOR-HOOK-VALIDATION.json`
- Visual parity: `audits/cf-008-faq/CF-008-VISUAL-PARITY-MATRIX.json`
- Accordion QA: `audits/cf-008-faq/data/CF-008-ACCORDION-FUNCTIONAL-QA.json`

## Next wave

CF-009 `home-final-form` — **COMPLETE** (see `audits/cf-009-final-form/`)
