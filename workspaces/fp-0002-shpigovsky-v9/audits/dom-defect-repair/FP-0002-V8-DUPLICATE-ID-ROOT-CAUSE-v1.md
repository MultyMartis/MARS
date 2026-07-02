# FP-0002 V8 — Duplicate ID Root Cause v1

**Date:** 2026-06-28
**Defect ID:** `home-treatment-prevention-panel-1`
**Page:** `index.html` (Home)
**Owner family:** `home-treatment-prevention`

## Occurrences before repair

| # | Source | Element | Role |
|---|--------|---------|------|
| 1 | `src/partials/sections/home-treatment-prevention.html` L31 | `#home-treatment-prevention-panel-1` | Accordion panel for item 1 (canonical) |
| 2 | `src/partials/sections/home-why-us.html` L13 | `#home-treatment-prevention-panel-1` | Static service list panel (copy-paste) |

**Page-wide count in `dist/index.html`:** 2

## Related references

| Reference | File | Value |
|-----------|------|-------|
| `aria-controls` | `home-treatment-prevention.html` L21 | `home-treatment-prevention-panel-1` |
| `aria-labelledby` | `home-treatment-prevention.html` L33 | `home-treatment-prevention-trigger-1` |
| Trigger ID | `home-treatment-prevention.html` L22 | `home-treatment-prevention-trigger-1` |
| `aria-labelledby` (orphan) | `home-why-us.html` L15 | `home-treatment-prevention-trigger-1` (no trigger on page in why-us block) |

## Root cause

**Duplicate hardcoded ID inside a second partial on the same page.**

`home-why-us.html` contains a block of markup copied from the treatment-prevention accordion panel (same BEM classes and the same panel ID). Both partials are included on `index.html`:

```html
@@include('partials/sections/home-treatment-prevention.html')
@@include('partials/sections/home-why-us.html', {"class": "no-top-padding--30"})
```

This predates CF-008/CF-009; not introduced by those waves.

## Affected files

- **Primary defect:** `src/partials/sections/home-why-us.html`
- **Canonical owner (unchanged):** `src/partials/sections/home-treatment-prevention.html`
- **Consumer page:** `src/pages/index.html` (includes both partials)

## Repair policy

Change only the conflicting ID and its `aria-labelledby` in `home-why-us.html`. Do not rename the `home-treatment-prevention` family or alter accordion behavior.

**Verdict:** ROOT CAUSE CONFIRMED
