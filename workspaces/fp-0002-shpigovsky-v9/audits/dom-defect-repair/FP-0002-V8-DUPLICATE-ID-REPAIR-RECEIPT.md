# FP-0002 V8 — Duplicate ID Repair Receipt

**Date:** 2026-06-28
**Commit scope:** narrow DOM/ARIA repair only

## Repair

| Field | Before | After |
|-------|--------|-------|
| Duplicate ID | `home-treatment-prevention-panel-1` × 2 on `index.html` | × 1 (canonical accordion only) |
| Conflicting element | `home-why-us.html` panel | `id="home-why-us-services-panel"` |
| `aria-labelledby` (why-us panel) | `home-treatment-prevention-trigger-1` (broken) | `home-why-us-heading` |

## Unchanged

- `home-treatment-prevention` partial, classes, JS, CSS
- Accordion default state and behavior
- Visual layout (ID/ARIA only)

## Validation

| Check | Result |
|-------|--------|
| Page-wide duplicate IDs | 0 |
| Target ID count | 1 |
| Broken ARIA | 0 |
| Accordion click/Enter/Space | PASS |
| Build | PASS |

## Evidence

- Backup: `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\operator-checkpoints\FP-0002-V8-BEFORE-TREATMENT-PREVENTION-DUPLICATE-ID-REPAIR.zip`
- Before PNG: `...\duplicate-id-repair-evidence\before\`
- After PNG: `...\duplicate-id-repair-evidence\after\`
- JSON: `audits/dom-defect-repair/data/FP-0002-V8-DUPLICATE-ID-REPAIR-VALIDATION.json`

**Verdict:** REPAIR COMPLETE
