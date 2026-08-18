# iseoblog glossary package

Local source of truth for the i-seo.su glossary foundation deployed into theme `iseoblog`.

## Files

| Path | Role |
|------|------|
| `functions.php` | Patched theme functions (baseline + glossary bootstrap require) |
| `archive-glossary.php` | Alphabetical archive |
| `single-glossary.php` | Term single |
| `template-parts/content-glossary-page-scene.php` | Shared services-style hero |
| `template-parts/content-topbar.php` | Shared header topbar incl. **Глоссарий** menu link |
| `inc/glossary-bootstrap.php` | Requires |
| `inc/glossary-cpt.php` | CPT + exposure/indexation + archive title filters |
| `inc/glossary-acf.php` | ACF field group |
| `inc/glossary-helpers.php` | Letter grouping + related links + CTA scroll |
| `inc/glossary-import-admin.php` | Gated admin import (disabled after intake) |
| `inc/data/glossary-terms-inventory-v1.json` | Sanitized intake inventory |

## Shared CSS authority

Operator manual glossary CSS tuning is **not** in this theme package. Canonical copy:

`projects/iseo-su-site-ops/production-source/css/main.css`

Promote runtime→source before overwriting production `css/main.css` from automation.

## Gates

- `ISEO_GLOSSARY_PUBLIC_EXPOSURE` default `true` (public launch complete)
- `ISEO_GLOSSARY_IMPORT_ENABLED` default `false` after successful import

## Deploy

Use programme SFTP deploy helpers under `_glossary-scratch/` (local evidence only). Do not commit secrets.

Final integration deploy (2026-08-18): `content-topbar.php`, `glossary-cpt.php` — see closeout REPORT.
