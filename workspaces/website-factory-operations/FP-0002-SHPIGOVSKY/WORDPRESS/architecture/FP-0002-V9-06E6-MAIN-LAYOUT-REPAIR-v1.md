# FP-0002 V9-06E6 — Main Layout Repair

## Root cause

Subdivision layout CSS in `v9-style.css` requires `body.page-service-subdivision-v1`. WordPress service singles only had generic `single-service` classes, so main-content layout rules never activated.

## Changes applied

| Area | Before | After |
|------|--------|-------|
| Body class | `single-service postid-73` | + `page-service-subdivision-v1` |
| Stack wrapper | `<article class="shpigovsky-service--subdivision">` | Direct partials in `main` |
| Dependencies | Plain h2 | V9 header + marker `01` + footer text |
| Program | Text-only items | V9 modifiers + images + intros + foot link |
| Hero | `services-inner-hero-v2` + image | **unchanged** |
| Shared BG | E5 relative paths | **unchanged** |

## Validation

All 9 subdivision anchor IDs present. `program-genotyping.webp` renders. Regression routes HTTP 200.

JSON: `validation/v9-06e6-service-subdivision-main-layout-repair/main-layout-repair-result.json`
