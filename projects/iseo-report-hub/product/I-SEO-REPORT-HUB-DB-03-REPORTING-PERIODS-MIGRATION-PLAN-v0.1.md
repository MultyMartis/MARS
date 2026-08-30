# I-SEO Report Hub — DB-03 Reporting Periods Migration Plan v0.1

**Status:** MIGRATION PLAN ONLY — no SQL authored; no DB mutation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md), [I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Planned migration file name

```text
2026_07_25_000002_create_reporting_periods_table.sql
```

| Role | Path |
|------|------|
| SoT | `projects/iseo-report-hub/app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql` |
| Runtime after sync | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\database\migrations\2026_07_25_000002_create_reporting_periods_table.sql` |

**Not created in this charter wave.**

---

## 2. Ledger behavior

| Rule | Statement |
|------|-----------|
| Authority | `schema_migrations` |
| Apply tool | `tools/db-migrate.php apply` |
| Status tool | `tools/db-migrate.php status` |
| On success | Insert ledger row: `migration` = filename, `checksum` = SHA-256 of file, `batch` incremented |
| Already applied | Re-run is **no-op** (idempotent) |
| Checksum mismatch | **STOP** — do not re-apply; investigate file drift |
| Allowed DB name | `iseo_report_hub_dev` only |

Current ledger baseline: one row for `2026_07_24_000001_create_core_tables.sql` with checksum `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4`.

---

## 3. Preflight (apply wave)

Before authoring/applying DB-03 SQL:

1. Confirm repo root `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`.
2. Confirm staged area empty (or only allowlisted apply-wave paths).
3. Confirm auth baseline present (local admin / users≥1 / roles=6) unless operator waives.
4. Confirm first migration still applied and checksum OK.
5. Confirm `reporting_periods` does **not** already exist (or decide STOP if unexpected).
6. Confirm target is **local** `iseo_report_hub_dev` only.
7. No production credentials; never print DB password.

---

## 4. Apply steps (future wave)

1. Author SQL in `app-source/database/migrations/` per schema plan (CREATE TABLE `reporting_periods` only).
2. Sync migration file source → runtime (Model A allowlist; no broad wipe).
3. Run `php tools/db-migrate.php status` — expect pending `000002`.
4. Run `php tools/db-migrate.php apply`.
5. Re-run `status` — expect `[applied]` + `checksum_ok`.
6. Run structural validation (see §5).
7. Optional: safe fixture project + one period insert **only if** implementation charter approves; otherwise structure-only.
8. Re-run apply — expect idempotent no-op.
9. Record result docs / OPERATIONAL-INDEX update as chartered.
10. Scoped commit of allowlisted paths; **no push** unless separately authorized.

---

## 5. Validation SQL categories (no destructive SQL)

Categories for apply-wave checks (describe intent; do **not** run DROP/TRUNCATE):

| Category | Intent |
|----------|--------|
| Table exists | `reporting_periods` present in information_schema / SHOW TABLES |
| Columns exist | Required columns listed in schema plan are present with expected nullability |
| Indexes / unique | Unique `(project_id, period_key)` and required indexes exist |
| FK presence | FKs to `projects` and `users` recorded |
| Unique refusal | Controlled duplicate insert attempt fails (only if a safe project exists) |
| Ledger | Second migration row present; checksum matches file |
| Idempotency | Second `apply` does not alter schema / does not duplicate ledger |
| Counts | Migration count increments by 1; table count increments by 1 |

**Forbidden in automated task without explicit approval:** `DROP TABLE`, `TRUNCATE`, `DELETE` of non-smoke rows, `DROP DATABASE`, broad restore.

---

## 6. Rollback notes

| Policy | Statement |
|--------|-----------|
| Environment | Local `iseo_report_hub_dev` only |
| Default | **Forward-only** — prefer fix-forward migration |
| Automated destructive rollback | **Not allowed** unless table is empty **and** operator gives explicit approval |
| Manual rollback notes | If approved and table empty: drop `reporting_periods`, remove ledger row for `000002` under HITL — document in apply result |
| Non-empty table | Backup / export first; no agent `DROP` without charter |
| Production | No rollback/apply |

---

## 7. Idempotency

1. `schema_migrations` ledger is authority.
2. Migration file checksum must remain stable after apply.
3. Re-run apply → no-op if already applied with matching checksum.
4. Checksum mismatch → **STOP**.
5. `CREATE TABLE IF NOT EXISTS` may appear in SQL style consistent with first migration, but ledger still prevents double-ledger inserts.

---

## 8. STOP conditions

STOP the apply wave (and do not mutate further) if:

- wrong volume / branch / repo root;
- staged area contains foreign paths;
- DB name ≠ `iseo_report_hub_dev`;
- first migration missing or checksum failed;
- unexpected pre-existing `reporting_periods` with unknown provenance;
- checksum mismatch on re-apply;
- FK/unique smoke fails unexpectedly;
- operator withholds approval for fixture or rollback.

---

## 9. No DB mutation in charter wave

This document does **not** authorize:

- creating the SQL file;
- editing existing migrations;
- applying migrations;
- inserting periods;
- changing users/roles/passwords;
- editing `.env` / `.env.local`;
- source → runtime sync.

Charter wave = docs only.
