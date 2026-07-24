# iseoblog glossary package

Local source of truth for the i-seo.su glossary foundation deployed into theme `iseoblog`.

## Files

| Path | Role |
|------|------|
| `functions.php` | Patched theme functions (baseline + glossary bootstrap require) |
| `archive-glossary.php` | Alphabetical archive |
| `single-glossary.php` | Term single |
| `inc/glossary-bootstrap.php` | Requires |
| `inc/glossary-cpt.php` | CPT + exposure/indexation gates |
| `inc/glossary-acf.php` | ACF field group |
| `inc/glossary-helpers.php` | Letter grouping helpers |
| `inc/glossary-import-admin.php` | Gated admin import (disabled after intake) |
| `inc/data/glossary-terms-inventory-v1.json` | Sanitized intake inventory |

## Gates

- `ISEO_GLOSSARY_PUBLIC_EXPOSURE` default `false`
- `ISEO_GLOSSARY_IMPORT_ENABLED` default `false` after successful import

## Deploy

Use programme SFTP deploy helper under `_glossary-scratch/` (local evidence only). Do not commit secrets.
