# FP-0002 — Services General Geometry & Responsive Map v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Baseline:** `audits/home-style-baseline-01/FP-0002-RESPONSIVE-RULES-REALITY-MAP-v1.md`

---

## Global baseline (retain)

| Token / rule | Value | Classification |
|--------------|-------|----------------|
| Container max-width | 1230px | USE_EXISTING_RULE |
| Desktop gutter | 30px (`--pad-x`) | USE_EXISTING_RULE |
| ≤1024 gutter | 15px | USE_EXISTING_RULE |
| Primary breakpoint | 1024 / 1025 | USE_EXISTING_RULE |
| Section rhythm Y | 50px (`--pad-y`) | USE_EXISTING_RULE |
| Hero max-width | 1400px | USE_EXISTING_RULE |
| Button radius | `--radius-main`, `--radius-full` | USE_EXISTING_RULE |

---

## Section geometry

| Section | Desktop | ≤1024 | Mobile | Small mobile | Classification | Risk |
| ------- | ------- | ----- | ------ | ------------ | -------------- | ---- |
| Inner hero | 628px height `.hero--inner`; panel overlay | height auto; min readable | Title scale @930px pattern | Same | USE_EXISTING_RULE | Low |
| Category hub head | Container-aligned; H2 + optional link | Full width | Stack | Stack | USE_EXISTING_RULE | Low |
| Category service list | Full width rows; dotted leader desktop | Hide leader ≤1024 | Full width | Full width | USE_EXISTING_RULE | Low |
| Category gallery | 3-col image row (~370px cards in Figma) | 1-col stack | 1-col | 1-col | SECTION_SPECIFIC_MEASURED_VALUE | Medium — measure from Figma export |
| Program directions | Row cards + image (existing flex) | Existing responsive | May wrap tight | Same | USE_EXISTING_RULE | Low |
| Founder quote | 2-col grid | 1-col @1024 | variant A stack | Same | USE_EXISTING_RULE | Low |
| Comfort gallery | 3-col + wide span | 1-col proven | 1-col | 1-col | USE_EXISTING_RULE | None |
| FAQ | Full width accordion | Same | Same | Same | USE_EXISTING_RULE | None |
| Final form | 2-col band | 1-col stack | 1-col | 1-col | USE_EXISTING_RULE | None |

---

## New measured values (implementation only)

| Element | Desktop evidence | Mobile evidence | Status |
|---------|------------------|-----------------|--------|
| Category hub gallery gap | Figma ~400px column gap in «Нас выбирают»-like rows | Full-width images | SECTION_SPECIFIC_MEASURED_VALUE |
| Category block vertical rhythm | ~50px between sub-blocks | Larger gaps in mobile PNG | USE_EXISTING_RULE first |
| Hero bottom radius | PNG large corner on hero panel | Rounded panel persists | USE_EXISTING_RULE (`--radius-main`) |
| Watermark position | Absolute decorative | Scale/hide TBD | SAFE_UNKNOWN |

---

## Mobile order

Mobile PNG authority — order preserved vs desktop (no reorder of major sections). Category internal order: heading → lead → list → gallery → CTA.

---

## Responsive verdict

**Implement with existing container/gutter/hero/accordion/form rules first.** Only category hub 3-col gallery requires new SCSS block in `style.scss` under `.services-category-hub` (or scoped `.page-uslugi` rules).

---

*End of geometry & responsive map v1.*
