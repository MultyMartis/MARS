# FP-0002 V9-06E9 Service Leaf Layout Repair

## Files changed (7)

1. `template-parts/service/alcohol-stack.php` — direct partial stack (no article)
2. `template-parts/service/leaf-stack.php` — direct partial stack (no article)
3. `inc/service-helpers.php` — alcohol-specific subnav
4. `template-parts/service/program.php` — image fallback for alcohol-special
5. `template-parts/home/reviews.php` — pass args to slider
6. `template-parts/shared/reviews-slider.php` — section_id support
7. `template-parts/components/final-form.php` — heading_id / lead_source args

## Results

| Area | Before | After | Result |
|------|--------|-------|--------|
| Main wrapper | article wrapper | direct sections | PASS |
| Program grid | titles only | 4 image cards | PASS |
| Subnav | wrong anchors | static V9 anchors | PASS |
| Reviews id | missing | service-leaf-reviews | PASS |
| Final form id | generic | service-leaf-final-form-heading | PASS |

Runtime delivered to `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\`.

JSON: `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/service-leaf-layout-repair-result.json`
