# FP-0002 V9-06E4 Future E5 Repair Plan

**Date:** 2026-07-06  
**Status:** PLAN ONLY — no repair in E4

## Wave order

1. **CSS path repair** — fix 4 `/assets/` rules in `v9-style.css` (low risk, high visual impact on shared bands)
2. **Services hub hero** — `services-inner-hero-v2` + `services-hero.webp`
3. **Services hub layout** — body/main classes, section-v2 stack, services-program-v2, missing sections
4. **Subdivision hero** — theme fallback or ACF seed for #73
5. **Subdivision stack** — add missing V9 partials; fix stages variant
6. **Validation** — screenshot parity + route smoke

## Safety

- Bounded theme source edits + manifested runtime delivery
- DB writes only if operator charters `hero_media` seed
- No menu/legal/reviews regression scope in E5 charter without explicit add

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/future-e5-repair-plan.json`
