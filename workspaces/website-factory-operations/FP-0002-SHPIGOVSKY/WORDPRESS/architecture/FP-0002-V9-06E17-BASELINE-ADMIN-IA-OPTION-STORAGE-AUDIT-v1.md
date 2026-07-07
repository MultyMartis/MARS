# FP-0002 V9-06E17 — Baseline Admin IA and Option Storage Audit

**Evidence:** `validation/v9-06e17-site-settings-ia-skeleton/baseline-admin-ia-option-storage-audit.json`

## Before E17

- Parent **Настройки сайта** (`fp02-site-settings`) held contacts + modal/CTA field groups directly.
- Top-level **Отзывы** (`fp02-reviews`) separate from Site Settings.
- Site options stored under ACF `option` post_id (`options_*` keys).
- Reviews stored under `fp02-reviews` post_id.

## Compatibility proof

Relocating field groups to `fp02-site-settings-general` is safe when the subpage registers `post_id => option`. Frontend `shpigovsky_get_site_option()` continues reading `get_field($name, 'option')` unchanged.

Reviews relocation deferred — top-level menu remains active in E17.
