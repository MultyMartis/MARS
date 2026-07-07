# FP-0002 V9-06E21 Frontend Renderer Migration

Evidence: `validation/v9-06e21-reusable-blocks-batch-2-fields/frontend-renderer-migration-result.json`

| Consumer | Change |
|----------|--------|
| `template-parts/layout/header.php` | `shpigovsky_get_header_logo_url()`, `shpigovsky_get_header_callback_label()` |
| `template-parts/layout/footer.php` | footer logo, copyright suffix, credit, CTA labels from block helpers |
| `inc/hero-helpers.php` | `shpigovsky_get_block_hero_fallback_image()` before theme registry fallback |
| `template-parts/home/comfort.php` | dynamic gallery from block repeater |
| `template-parts/home/rehabilitation-requirements.php` | block-driven steps, CTA, support, photo |

Frontend regression: 9/9 routes HTTP 200 PASS.
