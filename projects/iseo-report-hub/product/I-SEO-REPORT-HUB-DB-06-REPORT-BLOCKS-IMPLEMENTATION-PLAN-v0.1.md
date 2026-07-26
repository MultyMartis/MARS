# I-SEO Report Hub — DB-06 Report Blocks Implementation Plan v0.1

**Status:** IMPLEMENTATION PLAN for next wave — not an apply authorization by itself  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Report Blocks DB-06 Migration Apply 01`**

Operator must issue an explicit apply charter before execution. This plan is the blueprint for that wave.

---

## 2. Migration filename

`2026_07_26_000005_create_report_blocks_table.sql`

| Part | Rule |
|------|------|
| Date prefix | `2026_07_26` (charter day / project convention) |
| Sequence | **`_000005`** (authoritative next sequence after `_000004`) |
| If system date differs | Keep `_000005`; adjust date prefix only if project convention requires the apply-day date — do **not** renumber sequence |

---

## 3. Allowed app-source writes (next wave)

| Path / class | Allowed |
|--------------|---------|
| `app-source/database/migrations/2026_07_26_000005_create_report_blocks_table.sql` | **Yes** (create) |
| Optional product result doc | **Yes** if apply charter lists it |
| Optional reports closeout | **Yes** if apply charter lists it |
| `OPERATIONAL-INDEX.md` | **Yes** if apply charter lists it |
| App controllers / services / repositories / views | **No** |
| Prior migrations `000001`–`000004` | **No** edits |
| Fixture tool / auth tools | **No** unless apply charter explicitly adds a local smoke helper |
| `.env` / `.env.local` | **No** |
| Demo workspace / registry | **No** |

---

## 4. Runtime sync (next wave)

| Action | Allowed |
|--------|---------|
| Copy **only** the new migration SQL to Localhost `database/migrations/` | **Yes** |
| Run `tools/db-migrate.php status` / `apply` on runtime | **Yes** |
| Broad source → runtime app sync | **No** |
| Sync CRUD / controllers / views | **No** |
| Restart Apache / MySQL | **No** unless separately approved |

Target DB only: `iseo_report_hub_dev` @ `127.0.0.1`.

---

## 5. DB smoke (next wave)

Expected deltas:

| Metric | Before | After |
|--------|--------|-------|
| Migration count | **4** | **5** |
| Table count | **12** | **13** |
| New table | — | `report_blocks` |

Smoke row plan (local demo only; not in this charter wave):

1. Resolve monthly report content for fixture period `2026-07` dynamically (expected id **1**; do not hard-fail if id differs).
2. Insert **five** local fixture blocks under that parent:
   - `executive_summary` (sort 10)
   - `work_completed` (sort 20)
   - `results_summary` (sort 30)
   - `key_findings` (sort 40)
   - `next_month_plan` (sort 50)
3. All content markers `LOCAL_FIXTURE_ONLY`; status `draft`; titles contain `LOCAL_FIXTURE_ONLY`.
4. `source_weekly_checkpoint_ids` = JSON array of current local fixture weekly checkpoint ids for `2026-07`, resolved dynamically by `checkpoint_key` (`2026-07-W1` … `2026-07-W4` if present).
5. `owner_user_id` / `created_by` / `updated_by` = local admin id if safely resolvable.
6. Reject duplicate `(monthly_report_content_id, block_key)`.
7. Reject invalid `monthly_report_content_id` FK.
8. Reject invalid `status`.
9. Reject invalid `block_type` if DB CHECK used.
10. Verify JSON validity if applicable.
11. Confirm `reporting_periods` / `monthly_report_contents` / `weekly_checkpoints` unchanged except new child block rows.
12. No real client data.

Idempotent re-apply of migration must be a no-op after ledger success.

---

## 6. Commit policy (next wave)

- Exact-path stage of allowlisted migration + docs only.
- No `git add .` / `-A` / `commit -a`.
- Preserve foreign WIP.
- No push unless operator charter explicitly authorizes push (default **no push**).
- Optional hash-record follow-up for closeout report only.

Suggested primary message pattern:

`feat(iseo-report-hub): add db06 report blocks migration`

(Exact message is set by the apply charter.)

---

## 7. STOP conditions (next wave)

Stop before mutation if:

- Wrong root / volume / branch
- Non-empty staged index with foreign paths
- Unexpected i-SEO WIP outside apply allowlist
- DB host ≠ `127.0.0.1` or DB name ≠ `iseo_report_hub_dev`
- Migration `_000005` already applied with different checksum and no repair charter
- Apply charter attempts report block CRUD UI, editor, export, or portal in same wave without explicit expansion

Output token pattern:

`STOP — I-SEO REPORT BLOCKS DB-06 MIGRATION APPLY SAFETY CONDITION FAILED`

---

## 8. Explicit non-goals of next wave

- Report block CRUD UI / editor
- Drag/drop reorder product
- PDF / export / client portal
- Topvisor / API metrics tables
- Production deployment
- Automatic sync of blocks into DB-05 TEXT fields
- Monthly / weekly / period row mutation beyond inserting child block smoke rows
