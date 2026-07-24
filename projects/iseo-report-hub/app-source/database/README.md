# database/

## Purpose

Versioned SQL migrations and human-readable schema notes for i-SEO Report Hub.

## Layout

- `migrations/` — timestamped SQL migration files (source of truth)
- `schema-draft-not-migration.md` — conceptual reminder; **not** executable SQL
- `seeds/` — reserved for future sanitized seeds (not used by first migration)

## First migration

`migrations/2026_07_24_000001_create_core_tables.sql`

Creates DB-01 + minimal DB-02 tables:

- `schema_migrations`
- `users`
- `roles`
- `user_roles`
- `audit_log`
- `clients`
- `projects`
- `sites`
- `project_type_profiles`

Role catalog seed rows only (no users, no passwords, no client data).

## Apply (local only)

Target DB must be exactly `iseo_report_hub_dev`.

From app root (source or runtime after sync):

```text
php tools/db-migrate.php status
php tools/db-migrate.php apply
```

Requires local `.env.local` (runtime recommended) or equivalent environment variables.
The migration tool inserts the ledger row after successful SQL execution.
