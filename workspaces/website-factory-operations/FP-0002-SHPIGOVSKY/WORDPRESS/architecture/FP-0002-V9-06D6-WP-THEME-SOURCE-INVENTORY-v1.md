# FP-0002 V9-06D.6 WordPress Theme Source Inventory v1

**Date:** 2026-07-04
**Theme:** `theme/shpigovsky` `0.2.0-skeleton`

## Templates

- `front-page.php` — home orchestration (inert partials)
- `page-templates/services-hub.php` — H1 + placeholder
- `single-service.php` — loads stack via `shpigovsky_load_service_template()`
- `page-templates/contacts.php` — H1 + contacts partials
- Also: institutional, reviews, legal, home.php, page.php, single.php, index.php, search.php, 404.php

## Service stacks

- Variants: `subdivision`, `leaf`, `alcohol-special`
- Loader default: `leaf` (ACF not wired)
- Stacks and section partials exist as inert comment markers

## Assets

- Enqueues only `assets/css/foundation.css`
- Hook `shpigovsky_enqueue_theme_assets` reserved for V9 assets

## Plugin

- Mode: `content_model`
- Enabled: service CPT, permalinks (depth-2 repaired), ACF groups, options page, validation
- Disabled: forms consultation, migrations

## Result

COMPLETE — planning inventory only.
