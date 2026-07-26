# I-SEO Report Hub — Report Snapshot Schema Plan v0.1

**Status:** SCHEMA PLANNING ONLY — no SQL migration created/edited in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-DESIGN-v0.1.md)

---

## 1. Table name

**`report_snapshots`**

Migration batch expected: **DB-07** (next migration after DB-06 `report_blocks`).

Parent relationships:

- `monthly_report_content_id` → `monthly_report_contents(id)`
- `reporting_period_id` → `reporting_periods(id)`

---

## 2. Columns

| Column | Type | Null | Default | Notes |
|--------|------|------|---------|-------|
| `id` | BIGINT UNSIGNED | NO | AUTO_INCREMENT | PK |
| `monthly_report_content_id` | BIGINT UNSIGNED | NO | — | Parent monthly |
| `reporting_period_id` | BIGINT UNSIGNED | NO | — | Denormalized period FK |
| `snapshot_key` | VARCHAR(96) | NO | — | Unique slug-safe key |
| `version` | INT UNSIGNED | NO | 1 | Per-monthly version |
| `status` | VARCHAR(32) | NO | `'active'` | active / superseded / archived |
| `title` | VARCHAR(255) | NO | — | Snapshot title (copy from monthly at create) |
| `render_mode` | VARCHAR(32) | NO | — | e.g. blocks_primary / flat_fallback |
| `payload_json` | JSON | NO | — | Canonical frozen payload |
| `rendered_text` | MEDIUMTEXT | YES | NULL | Optional plain text |
| `rendered_html` | MEDIUMTEXT | YES | NULL | Optional; prefer null MVP |
| `checksum_sha256` | CHAR(64) | NO | — | Hex SHA-256 |
| `source_block_ids` | JSON | YES | NULL | Ordered block ids |
| `source_weekly_checkpoint_ids` | JSON | YES | NULL | Weekly refs |
| `created_by` | BIGINT UNSIGNED | YES | NULL | Actor |
| `created_at` | DATETIME | NO | CURRENT_TIMESTAMP | Snapshot created |
| `archived_at` | DATETIME | YES | NULL | When archived |

No `updated_at` for content mutation — rows are immutable except status/archived_at transitions.

---

## 3. Indexes

| Name / type | Columns |
|-------------|---------|
| PRIMARY KEY | `id` |
| UNIQUE | `(monthly_report_content_id, version)` |
| UNIQUE | `snapshot_key` |
| INDEX | `(monthly_report_content_id, status)` |
| INDEX | `(reporting_period_id, status)` |
| INDEX (optional) | `(checksum_sha256)` — for idempotency lookups if useful |

---

## 4. Constraints

- `CHECK (status IN ('active', 'superseded', 'archived'))` — if MySQL version/policy allows CHECKs as used in prior migrations; otherwise enforce in app + document.
- `CHECK (version >= 1)`
- MySQL JSON types for `payload_json`, `source_block_ids`, `source_weekly_checkpoint_ids` — **no** extra JSON CHECK unless portable across prior migrations’ style.

**One active per monthly:** not enforced by unique partial index (awkward in MySQL without generated column tricks). **Enforce in application/service** when creating new active versions.

---

## 5. FK policy

| FK | References | ON DELETE | ON UPDATE |
|----|------------|-----------|-----------|
| `monthly_report_content_id` | `monthly_report_contents(id)` | **RESTRICT** | CASCADE or RESTRICT (match prior style; prefer RESTRICT) |
| `reporting_period_id` | `reporting_periods(id)` | **RESTRICT** | same |
| `created_by` | `users(id)` | **SET NULL** | same |

Rationale: snapshots must not disappear if parent mistakenly targeted; hard parent delete blocked while snapshots exist.

---

## 6. Status CHECK

Allowed values:

- `active` — current frozen version for the monthly report;
- `superseded` — replaced by a newer version;
- `archived` — admin soft-retire (still readable, not active).

---

## 7. JSON policy

- `payload_json` is source of truth for frozen content structure.
- `source_block_ids` / `source_weekly_checkpoint_ids` are convenience indexes of ids also present inside payload.
- Store UTF-8; no secrets; LOCAL_FIXTURE_ONLY markers may appear in fixture payloads.
- Do not put credentials, env, or session tokens in JSON.

---

## 8. Versioning policy

- First snapshot: `version = 1`, `snapshot_key = monthly-{id}-v1`.
- Next after re-finalize cycle: increment version; new `snapshot_key`; mark previous `active` as `superseded`.
- Unique `(monthly_report_content_id, version)` prevents duplicate version numbers.
- Do not reuse version numbers.

---

## 9. Idempotency policy

App-level (not DB unique on checksum alone — same checksum could theoretically appear across superseded history):

1. Compute checksum for candidate payload.
2. If current `active` row for monthly has same checksum → return existing (no insert).
3. Else insert new version (after superseding prior active when checksum differs and create is authorized).

Optional helper index on checksum is fine; uniqueness of checksum is **not** required globally.

---

## 10. Migration apply validation plan

For **DB-07 Migration Apply 01** (future wave):

| Check | Expect |
|-------|--------|
| Preflight DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Pre: schema_migrations | **5** |
| Pre: tables | **13**; no `report_snapshots` |
| Post: schema_migrations | **6** |
| Post: tables | **14** including `report_snapshots` |
| DESCRIBE / SHOW CREATE | columns/indexes/FKs match this plan |
| Row count | `report_snapshots` = **0** after apply (no seed unless separate fixture charter) |
| Existing counts unchanged | periods **2**; weekly **4**; monthly **1**; blocks **6**; users **1** |
| Monthly id 1 | still `finalized`; no row mutation |
| No DROP unrelated tables | |
| No real client data | |

---

## 11. Rollback expectation

| Scenario | Policy |
|----------|--------|
| Migration fail mid-apply | STOP; do not leave partial undocumented state; restore from migration transaction if used, or document manual DROP of `report_snapshots` + schema_migrations row only if explicitly chartered |
| After successful apply, before app code | Safe to leave empty table; app without snapshot routes continues working |
| Destructive rollback after data exists | Requires separate destructive charter (exact path / dry-run / approval) |

This charter wave creates **no** SQL file and applies **nothing**.

---

## 12. Explicit non-creation this wave

- No file under `app-source/database/migrations/**`
- No ALTER on existing tables required for MVP snapshot (new table only)
- No seed/fixture insert of snapshots in DB-07 apply unless a later implementation smoke charter adds controlled LOCAL_FIXTURE_ONLY create via app
