# FP-0002 V9-06E9 Baseline Visual Failure Capture

**Task:** V9-06E9 Service Leaf Static V9 Layout Parity Repair  
**Date:** 2026-07-06

## Summary

Operator E8 leaf layout gate rejected. Pre-repair runtime drift confirmed via probe and `runtime-alcohol-leaf-before-e9.png`. Static V9 reference captured from `fp-0002-shpigovsky-v9/dist/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html`.

## Pre-repair failures

| Issue | Evidence |
|-------|----------|
| Extra `<article class="shpigovsky-service">` wrapper | Broke direct section stack under `page-service-leaf-v1__main` |
| Program block missing item images | Titles-only grid vs static V9 image stack |
| Subnav anchors wrong | Intro/signs/faq vs static approach/program/start/specialists/comfort/reviews |
| Reviews section missing `id="service-leaf-reviews"` | Subnav anchor broken |
| Final form generic heading id | `final-form-heading` vs `service-leaf-final-form-heading` |

## Evidence

- `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/screenshots/runtime-alcohol-leaf-before-e9.png`
- `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/screenshots/static-v9-alcohol-leaf-reference-e9.png`
- `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/baseline-visual-failure-capture.json`

Operator-uploaded screenshot not found in workspace; documented as NOT_FOUND_IN_WORKSPACE.
