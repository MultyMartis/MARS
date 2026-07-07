# FP-0002 V9-06E19 Baseline Admin Visibility Audit v1

**Wave:** V9-06E19  
**Date:** 2026-07-08

## Root cause

E18 registered Batch 1 reusable block option subpages with `parent_slug = fp02-site-settings-blocks`. In WordPress admin, `add_submenu_page()` only supports two visible levels under a top-level menu. Pages whose parent is itself a submenu item (`fp02-site-settings-blocks`) are registered but **not shown** in the sidebar.

## Operator symptom

- **Повторяемые блоки** visible but empty: `С этой страницей настроек не связаны группы полей.`
- Expected Batch 1 children not visible in sidebar.

## Contributing factors

| Factor | Present |
|--------|---------|
| 3rd-level menu registration | YES |
| Field group slug mismatch | NO |
| Runtime delivery incomplete | NO |
| ACF JSON not loaded | NO |
| Reviews dual location missing in DB | YES (fixed in E19 sync) |

## ACF redirect behavior

Top-level `fp02-site-settings` uses `redirect => true`. ACF rewrites direct children to parent slug `fp02-site-settings-general` for WordPress menu registration. Batch 1 pages must register with `parent_slug = fp02-site-settings` to become visible siblings of **Общие настройки** and **Повторяемые блоки**.
