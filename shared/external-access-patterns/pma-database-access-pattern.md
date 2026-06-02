# phpMyAdmin / Database Access Pattern

**Scope:** shared pattern for PMA, hosting DB panels, and CLI database supervised access.  
**Applies to:** WPilot, OCPilot, future MODxPilot, CustomSitePilot.

## Purpose

Human-supervised workflow for inspecting or modifying site databases.

## Pre-access gates

| Gate | Operator confirms |
|------|-------------------|
| Target | Correct database name, host, prefix |
| Environment | test / staging / production |
| Backup | DB backup before any mutation |
| Scope | read-only schema inspect vs scoped query vs dump |
| Credentials | Operator holds DB session; not in repo |

## Workflow — read-only first

1. **Read-only first** — `SHOW TABLES`, schema describe, row counts, sample queries without mutation.
2. Prefer **schema metadata** over raw dumps in repo: table list, prefix, column notes, relationship map.
3. Operator may provide sanitized exports externally; repo holds labels and manifests only unless explicitly approved and sanitized.

## Dump / export safety

| Rule | Detail |
|------|--------|
| Full raw dumps | Do not commit unless explicitly approved and sanitized |
| PII | Customer, order, payment data — external only |
| Schema-only | Preferred for baseline compare and audit |
| Prefix note | Record table prefix in passport; do not assume `oc_` or `wp_` |

## Workflow — mutation (requires explicit approval)

1. Backup before any destructive SQL (`DROP`, `TRUNCATE`, bulk `UPDATE`/`DELETE`).
2. Scoped query only — single table or explicit charter scope.
3. Rollback path required — restore from backup or documented reverse SQL.
4. No destructive SQL without explicit operator approval in charter.

## Forbidden in repo

- DB passwords, connection strings with secrets.
- Full production dumps with PII or credentials.
- Live session tokens from PMA.

## OpenCart / ocStore notes (OCPilot)

- Core tables: `product`, `category`, `url_alias` / SEO routes — verify version-specific schema.
- Compare against versioned baseline in `projects/ocpilot/baselines/<version>/`.

## WordPress notes (WPilot)

- Core tables: `posts`, `postmeta`, `options` — prefix varies.
- Do not apply OpenCart catalog import assumptions to WordPress.

## Stop conditions

- Destructive SQL without approval → refuse.
- Dump would contain secrets or unredacted PII → external storage only.
- Version/schema mismatch vs baseline → SAFE UNKNOWN; do not claim clean diff.

## REPORT requirement

Every database access session must produce: `# REPORT — <pilot> database — <site>` with scope, tables inspected, backup status, SAFE UNKNOWN.
