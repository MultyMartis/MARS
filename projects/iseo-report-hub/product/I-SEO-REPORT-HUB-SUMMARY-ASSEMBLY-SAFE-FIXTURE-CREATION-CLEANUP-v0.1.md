# I-SEO Report Hub — Summary Assembly Safe Fixture Creation / Cleanup v0.1

**Status:** CHARTER / TOOLING — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01

Scripts are **not** written in this wave. Implementation 01 must add them under `app-source/tools/` and commit the tools (not dumps).

---

## 1. Tool shape

**One CLI script**, two modes:

`projects/iseo-report-hub/app-source/tools/summary-assembly-safe-fixture.php`

```
php tools/summary-assembly-safe-fixture.php --create  --confirm-local-fixture
php tools/summary-assembly-safe-fixture.php --cleanup --confirm-local-fixture
php tools/summary-assembly-safe-fixture.php --status
```

`--status` is read-only (optional). `--create` / `--cleanup` **refuse** without `--confirm-local-fixture`.

Do **not** add a second unguarded seed into `seed-nikita-catalogue.php` (that tool still targets monthly id 1 for catalogue fixtures).

---

## 2. Guards (all mutating modes)

Refuse and exit non-zero unless **all** hold:

| Guard | Rule |
|-------|------|
| SAPI | CLI only |
| Confirm flag | `--confirm-local-fixture` present |
| `APP_ENV` | exactly `local` |
| `DB_DATABASE` / `SELECT DATABASE()` | exactly `iseo_report_hub_dev` |
| `DB_HOST` | exactly `127.0.0.1` |
| Report id 1 | never in the created-id list; never in DELETE/UPDATE allowlist |
| Report id 5 | never in allowlist |
| Production hostnames | refuse if `APP_URL` is not local (`iseo-report-hub.test` / localhost / 127.0.0.1) |

Never print `.env` values, passwords, hashes, or share tokens.

Follow existing tool patterns in `create-local-fixture.php` and `seed-nikita-catalogue.php` (`assertLocalDevDatabase`, CLI-only).

---

## 3. Backup (before `--create`)

**Mandatory** full `mysqldump` of `iseo_report_hub_dev` **before** the first INSERT.

Suggested STORAGE path (not git):

`X:\AI MARS STORAGE\incoming\iseo-report-hub\summary-assembly-safe-fixture-implementation-01\`

Files:

- `iseo_report_hub_dev-pre-create.sql` (or timestamped equivalent)
- optional table dumps: `report_blocks`, `monthly_report_contents`, `monthly_report_work_entries`

If dump fails → **STOP**. No fixture INSERT.

Backup is emergency rollback, not the planned happy-path cleanup.

---

## 4. `--create` algorithm

1. Run guards + dump.  
2. Capture baseline counts (see §8).  
3. Generate marker `MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS` (UTC).  
4. Resolve reused parents (client/project/site 1, catalogue slugs, user ids). **STOP** if missing.  
5. Choose unused `period_key`.  
6. INSERT period → monthly → 6 blocks → 7 entries (one transaction).  
7. SELECT: snapshots/exports/shares for new monthly id must be **0**. Else rollback + STOP.  
8. SELECT: id 1 block `updated_at` max still `2026-07-27 01:46:07` (or the captured pre-create value).  
9. Write `fixture-ids.json` to STORAGE (not git).  
10. Print only: marker, new monthly id, period id, block keys/ids, entry count. No secrets.

`--create` is **not** idempotent across runs. A second create without cleanup **STOP**s if `fixture-ids.json` exists and those ids still have the marker (operator must cleanup first). If JSON is missing but a marked period/monthly exists, **STOP** and report ids (do not guess).

---

## 5. `fixture-ids.json` (STORAGE)

Suggested path:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\summary-assembly-safe-fixture-implementation-01\fixture-ids.json`

Must include:

- marker
- created_at (UTC)
- reused: client_id, project_id, site_id, user_ids
- created: period_id, monthly_id, block_ids by key, entry_ids
- baseline_counts (pre-create)
- dump filename
- `report_id_1_protected: true`

No tokens, no passwords, no full PDF paths that embed secrets.

---

## 6. `--cleanup` algorithm

1. Guards.  
2. Load `fixture-ids.json`. If missing → **STOP**.  
3. For each owned id, SELECT and verify marker (title / internal_note / `data_json.mars_fixture_marker` as applicable). Mismatch → **STOP**, keep backup, print exact ids.  
4. Refuse if any owned id is `1` or `5` for monthly, or a report-1 block/entry id.  
5. SELECT snapshots/exports/shares for fixture monthly:  
   - if **0**: continue;  
   - if **not 0**: **STOP** (do not DELETE unknown publication rows).  
6. DELETE in this order (exact ids only):

   1. `report_blocks` (fixture block ids)
   2. `monthly_report_work_entries` (fixture entry ids)
   3. `monthly_report_contents` (fixture monthly id)
   4. `reporting_periods` **only if** `created.period_id` was created by this fixture
   5. `sites` / `projects` / `clients` **only if** created by this fixture (expected: skip)

7. Do **not** DELETE `audit_log`, catalogue, users, weekly_checkpoints, report 1/5 rows.  
8. Re-read baseline counts (except `audit_log`). Mismatch → **STOP**.  
9. Rename or keep `fixture-ids.json` as `fixture-ids.cleaned.json` in STORAGE (operator evidence). Do not commit.

Physical DELETE is allowed **only** in this guarded CLI tool. App CRUD stays no-hard-delete.

---

## 7. Cleanup refusals

| Condition | Action |
|-----------|--------|
| Marker mismatch | STOP |
| JSON ids vs live row mismatch | STOP |
| Broad title/date match without JSON | Forbidden |
| Fixture monthly has snapshot/export/share | STOP |
| Would touch id 1 or 5 | STOP |
| Dump missing and operator asks restore | Separate restore charter; do not invent |

---

## 8. Baseline counts (probe 2026-08-17)

Implementation must recapture immediately before create. Expected if DB unchanged:

| Table / metric | Count |
|----------------|--------|
| `clients` | 1 |
| `projects` | 1 |
| `sites` | 1 |
| `reporting_periods` | 2 |
| `monthly_report_contents` | 2 |
| `report_blocks` | 6 (all monthly 1) |
| `monthly_report_work_entries` | 7 (all monthly 1) |
| `weekly_checkpoints` | 4 |
| `report_snapshots` | 1 |
| `report_exports` | 4 |
| `report_export_shares` | 7 (active 1 / revoked 6) |
| `seo_work_categories` | 13 |
| `seo_work_items` | 31 |
| `users` | 2 |

`audit_log` was **54** at probe; **may increase** and need not return.

After successful cleanup, the table counts above (except `audit_log`) must match the **pre-create baseline**, not necessarily this historic snapshot if the operator changed the DB in between.

---

## 9. Should the script be committed?

**Yes**, in Safe Fixture Implementation 01:

- local-dev tool with the guards in §2
- no evidence / dumps / `fixture-ids.json` in git
- no runtime-only copy without source→runtime sync of that one tool file if the operator runs it from runtime `tools/`

This charter wave commits **docs only**.

---

## 10. Runtime sync

Implementation 01 may sync **only** `app-source/tools/summary-assembly-safe-fixture.php` (and docs are git-only). No `.env`, no export storage, no PDF.

---

## 11. SAFE UNKNOWN

- Whether `mysqldump` is on PATH vs Laragon `mysql\bin` — implementation should use the same dump method as the latest i-SEO STORAGE incoming dumps.  
- Exact `audit_log` growth per create/apply (record counts, do not prune).
