# FP-0002 Service Subdivision Pass 1 — Anatomy Map v1

| Order | Region | Desktop node | Mobile node | Runtime component | Result |
|------:|--------|--------------|-------------|-------------------|--------|
| 1 | Header | `1:3493` in `1:3492` | `1:7098` in `1:7097` | `partials/layout/header.html` | REUSE_EXACT |
| 2 | Hero | `1:3528`–`1:3540` | `1:7122` area | `services-inner-hero-v2` + params | REUSE_WITH_CONTENT |
| 3 | Breadcrumbs | `1:3544` | `1:7145` | `breadcrumbs` 3-level | IMPLEMENTED |
| 4 | Local subnav | `1:3550` | `1:7137` | `services-page-subnav` + `listHtml` | IMPLEMENTED |
| 5 | Intro | `1:3558` | `1:7151` (partial) | `service-subdivision-intro-v1` | IMPLEMENTED |
| 6 | Primary service info | `1:3654` (excl. nature) | `1:7160` rows | `services-category-section-v2` scoped | IMPLEMENTED |

**Desktop anatomy:** Hero → crumbs/subnav → intro (heading, lead, bullets, 3 cards) → primary (service title, lorem, dependencies list, rows, genotyping link).

**Mobile anatomy:** Combined hero shell → crumbs/subnav → intro stack with CTA context → dependencies heading + rows (distinct order vs desktop).

**Structural differences:** Mobile breadcrumb truncates current label in Figma (`Лечение алко`); runtime uses full desktop label. Mobile rows omit body copy; desktop template duplicates title as body for first row.

**Result:** `PASS_1_ANATOMY_IMPLEMENTED`
