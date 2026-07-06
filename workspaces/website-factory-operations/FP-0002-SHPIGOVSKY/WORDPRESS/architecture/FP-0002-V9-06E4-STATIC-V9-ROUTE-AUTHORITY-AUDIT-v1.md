# FP-0002 V9-06E4 Static V9 Route Authority Audit

**Date:** 2026-07-06  
**Authority:** `workspaces/fp-0002-shpigovsky-v9/`

## Route map

| Route | Source | Dist | Template family |
|-------|--------|------|-----------------|
| `/uslugi/` | `src/pages/uslugi-v2.html` | `dist/uslugi/index.html` | TPL-SERVICES-HUB |
| `/uslugi/zavisimosti/` | `src/pages/usluga-podrazdel-v1.html` | `dist/uslugi/zavisimosti/index.html` | TPL-SERVICE-SUBDIVISION |

## Expected heroes

- **Hub:** `services-inner-hero-v2` + `services-hero.webp`
- **Subdivision:** `services-inner-hero-v2` + `service-subdivision-hero.webp`

## Expected shared backgrounds

Static SCSS uses relative `../img/content/home-final-form/home-final-form-background.webp` for:

- `.final-form__band::before`
- `.home-rehabilitation-requirements__cta-band::before`
- `.program-cta-band::before` (CF-011)

Dist resolves these as root-relative `/assets/img/...` — valid on static host only.

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/static-v9-route-authority-audit.json`
