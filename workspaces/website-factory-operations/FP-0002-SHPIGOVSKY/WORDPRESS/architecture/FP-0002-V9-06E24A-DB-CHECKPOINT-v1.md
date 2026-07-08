# FP-0002 V9-06E24A DB Checkpoint

**Wave:** V9-06E24A Service Structured Sections Required Field Polish  
**Date:** 2026-07-08

## Checkpoint

| Item | Value |
|---|---|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e24a-service-structured-sections-required-field-polish-pre-20260708T173446Z\` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `69F86DE293F4CEB2AB239511B264C0ED4B04E1739CF8E2A5C9C6D7F6293560E5` |

## Snapshots

- `service-structured-sections-postmeta.json` — programme + hero CTA meta for services 73/74
- `service-acf-group-snapshot.json` — `group_fp02_service_structured_sections`
- `programme-field-snapshot.json` — `programme_items` ACF field row
- `e24-hero-cta-preservation.json`
- `reviews-options-preservation.json`

## Restore

```bash
mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e24a-service-structured-sections-required-field-polish-pre-20260708T173446Z\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/db-checkpoint.json`
