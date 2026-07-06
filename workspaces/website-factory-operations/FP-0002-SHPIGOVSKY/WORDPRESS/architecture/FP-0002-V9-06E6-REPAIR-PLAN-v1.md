# FP-0002 V9-06E6 — Repair Plan

## Scope

`/uslugi/zavisimosti/` main layout only. Preserve E5 hero and shared backgrounds.

## Planned changes

| Component | Planned repair | Safety |
|-----------|----------------|--------|
| Body class | Add `page-service-subdivision-v1` on subdivision singles | Template-only |
| Stack | Remove article wrapper | Low risk |
| Dependencies | V9 header marker, heading, lead/footer fallbacks | No DB |
| Program | Subdivision modifiers, intros, images, foot link | Theme assets only |
| Nature / team-stats | Static V9 lorem fallbacks | No DB |
| Mid-cta | Correct modal source id | Low risk |

## Files (7)

- `inc/service-helpers.php`
- `template-parts/service/subdivision-stack.php`
- `template-parts/service/children.php`
- `template-parts/service/program.php`
- `template-parts/service/nature.php`
- `template-parts/service/mid-cta.php`
- `template-parts/service/team-stats.php`

JSON: `validation/v9-06e6-service-subdivision-main-layout-repair/repair-plan.json`
