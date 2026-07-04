# FP-0002 V9-06D8D Rollback Ready v1

**Checkpoint:** `v9-06d8d-services-hub-content-seed-pre-20260704-210430`  
**Root:** `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8d-services-hub-content-seed-pre-20260704-210430`

## Changed fields

- `services_hub_intro`
- `services_hub_faq_items`

## Procedures

- **Per-field:** restore from `services-hub-page-5-pre-values.json` via `update_field` on page 5
- **Full DB:** `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8d-services-hub-content-seed-pre-20260704-210430/mars_wp_fp0002.sql`

Rollback tested: NO — seed succeeded; not required.
