# database/seeds/

Reserved for sanitized seed data notes.

Executable seed tooling lives under `tools/` (CLI only), consistent with other local DB helpers.

## Nikita catalogue seed (DB-11+)

- Script: `tools/seed-nikita-catalogue.php`
- Source attribution: `nikita_catalogue_v1`
- Targets: `seo_work_categories`, `seo_work_items`, optional `monthly_report_work_entries` for monthly report id 1
- Idempotent upsert by slug / (monthly_report_id + title)
- Excludes access/credentials taxonomy
- Local DB only: `iseo_report_hub_dev` @ `127.0.0.1`

```text
php tools/db-migrate.php apply
php tools/seed-nikita-catalogue.php
```
