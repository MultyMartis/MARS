# Schema draft — NOT a migration

**Status:** documentation only  
**Executable SQL:** **NO**  
**Migrations executed:** **NO**  
**Database created:** **NO** (`iseo_report_hub_dev` is a candidate name only)

This file is a human-readable reminder of the MVP conceptual schema draft from:

`X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md`

It is **not** a `.sql` file, **not** a migration runner input, and **must not** be executed against MySQL.

Migrations and DDL belong to a **later phase** under an explicit charter.

## Candidate tables (conceptual)

- users
- roles
- user_roles
- clients
- projects
- sites
- project_type_profiles
- reporting_periods
- weekly_checkpoints
- monthly_reports
- report_blocks
- report_block_values
- work_item_categories
- work_items
- kpi_definitions
- kpi_values
- evidence_items
- evidence_files
- evidence_links
- reviewer_comments
- published_snapshots
- audit_log
