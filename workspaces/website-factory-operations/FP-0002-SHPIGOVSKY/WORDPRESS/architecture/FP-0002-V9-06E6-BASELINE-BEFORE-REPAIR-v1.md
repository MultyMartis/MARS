# FP-0002 V9-06E6 — Baseline Before Repair

**Date:** 2026-07-06  
**Route:** `/uslugi/zavisimosti/` (service #73)

## Summary

After E5, hero type and hero image were acceptable. Main layout below hero remained misaligned with static V9.

## Key defects

1. **Missing `page-service-subdivision-v1` body class** — subdivision CSS in `v9-style.css` is scoped under `.page-service-subdivision-v1`; without it, dependencies/nature/stages/team-stats layout rules did not apply.
2. **Extra `article.shpigovsky-service--subdivision` wrapper** — static V9 places sections directly under `main`.
3. **Dependencies section** — missing marker `01`, static heading, footer text.
4. **Program section** — missing V9 modifier classes, intro paragraphs, item media images, mobile foot link.
5. **Nature / team-stats** — non-V9 fallback copy vs static lorem authority.

## Preserved (E5)

- Hero `services-inner-hero-v2` + `service-subdivision-hero.webp`
- Main wrapper `page-service-subdivision-v1__main`
- Shared background CSS paths
- Section stack order (14 blocks after hero)

Evidence: `validation/v9-06e6-service-subdivision-main-layout-repair/baseline-before-repair.json`
