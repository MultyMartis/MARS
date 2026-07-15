# FP-0002 — Admin UX: ACF thematic section styling (v1)

**Status:** Active (V9-06E53)  
**Scope:** WordPress admin only — ACF edit screens for FP-0002 page/service models  
**Not:** public frontend CSS, content model changes, field key renames

## Purpose

Make ACF admin screens easier to scan for operators (notably Olga):

- Major thematic blocks stay visually distinct (`1. Hero`, `2. Навигация…`, `Макет страницы`, postboxes such as `Содержимое страницы`).
- Inside a thematic block, remove noisy grey horizontal divider lines between sibling ACF fields.
- Keep input/textarea/select chrome and usable controls (toggles, layout mode, etc.).

## Canonical assets

| Asset | Role |
|---|---|
| `WORDPRESS/theme/shpigovsky/assets/css/admin-fp02-acf.css` | Unified FP-0002 ACF admin stylesheet |
| `WORDPRESS/theme/shpigovsky/assets/css/admin-home-acf.css` | Compatibility alias (`@import` of unified file) |
| `WORDPRESS/theme/shpigovsky/inc/admin-editor.php` | Scoped enqueue + `body.fp02-acf-admin` |

## When styles load

Enqueued only in `wp-admin` when:

- editing `page` or `service` (`post.php` / `post-new.php`); or
- FP02 Site Settings options screens (hook contains `fp02-site-settings`).

Body class: `fp02-acf-admin`.

## Visual rules (E53)

1. **Remove** default ACF sibling `border-top` on `.acf-fields > .acf-field` inside `.acf-postbox` (top-level and nested field lists).
2. **Restore** a single stronger separator on `.acf-field.fp02-acf-section-title` (background `#f6f7f7`, top border `#c3c4c7`, margin).
3. Keep ~20px section title labels (E41/E43).
4. Preserve E44/E45 layout help + technical-hide rules.

## Field markers

Thematic starts use existing ACF wrapper class:

- `fp02-acf-section-title` (already present on Home / hub / services / sections / layout selectors).

Generic pages:

- `Макет страницы` uses `fp02-acf-section-title` on `page_layout_mode`.
- `Содержимое страницы` is a separate ACF postbox; internal lead/body dividers are muted by the same CSS.

No field keys/names were renamed for E53. ACF JSON was not mutated.

## Screens covered

- Home (#4)
- Services hub (#5)
- Service CPT (sections + Услуга pages)
- Generic Content pages (`page-templates/generic.php`)
- Other `page` edit screens with ACF (e.g. О центре, Контакты) — quieter field list + postbox spacing
- FP02 Site Settings options pages

## Non-goals / freeze guardrails

- Do not change Home / Services hub / service / generic **frontend** visuals for this style pass.
- Do not mutate service roles/layouts (`#315` / `#78` remain `Услуга` / `service_general`).
- Do not edit operator runtime `v9-style.css` drift.
- Do not globally restyle all of WordPress admin outside FP-0002 selectors/screens.

## Related reports

- `REPORTS/REPORT-FP-0002-V9-06E53-admin-ux-section-styling.md`
- Evidence: `REPORTS/evidence/v9-06e53-*.csv`
