# FP-0002 V9-06E4 Reconciliation Matrix

**Date:** 2026-07-06

| ID | Category | Static expected | WP current | Root cause | E5 repair |
|----|----------|-----------------|------------|------------|-----------|
| E4-001 | SERVICES_HUB_HERO_TYPE | services-inner-hero-v2 | hero--inner | TEMPLATE_WRAPPER | Replace hub hero partial |
| E4-002 | SERVICES_HUB_MAIN_LAYOUT | page-uslugi-v2 stack | simplified hub stack | TEMPLATE_WRAPPER | Align sections/classes |
| E4-003 | SERVICES_HUB_HERO_IMAGE | services-hero.webp | no img | TEMPLATE_WRAPPER | Wire default theme image |
| E4-004 | SUBDIVISION_HERO_IMAGE | service-subdivision-hero.webp | ACF empty | fallback missing | Fallback or seed hero_media |
| E4-005 | SUBDIVISION_LAYOUT | 14-section static stack | 7-section WP stack | TEMPLATE_WRAPPER | Extend subdivision-stack |
| E4-006 | FINAL_FORM_BACKGROUND | visible ::before | 404 CSS URL | CSS_PATH | Fix v9-style.css urls |
| E4-007 | CTA_BAND_BACKGROUND | visible ::before | 404 CSS URL | CSS_PATH | Fix v9-style.css urls |

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/reconciliation-matrix.json`
