# I-SEO Report Hub — DB-04 Weekly Checkpoints Implementation Plan v0.1

**Status:** IMPLEMENTATION PLAN for next wave — not an apply authorization by itself  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Weekly Checkpoints DB-04 Migration Apply 01`**

Operator must issue an explicit apply charter before execution. This plan is the blueprint for that wave.

---

## 2. Migration filename

`2026_07_26_000003_create_weekly_checkpoints_table.sql`

| Part | Rule |
|------|------|
| Date prefix | `2026_07_26` (charter day / project convention) |
| Sequence | **`_000003`** (authoritative next sequence after `_000002`) |
| If system date differs | Keep `_000003`; adjust date prefix only if project convention requires the apply-day date — do **not** renumber sequence |

---

## 3. Allowed app-source writes (next wave)

| Path / class | Allowed |
|--------------|---------|
| `app-source/database/migrations/2026_07_26_000003_create_weekly_checkpoints_table.sql` | **Yes** (create) |
| Optional product result doc | **Yes** if apply charter lists it |
| Optional reports closeout | **Yes** if apply charter lists it |
| `OPERATIONAL-INDEX.md` | **Yes** if apply charter lists it |
| App controllers / services / repositories / views | **No** |
| Prior migrations `000001` / `000002` | **No** edits |
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
| Migration count | **2** | **3** |
| Table count | **10** | **11** |
| New table | — | `weekly_checkpoints` |

Smoke row plan (local demo only; not in this charter wave):

1. Resolve fixture reporting period `2026-07` dynamically by `period_key` (expected id **1**, do not hard-fail if id differs).
2. Insert **3** demo weekly checkpoints:
   - W1 — `checkpoint_key=2026-07-W1`, status `completed`, summary marked `LOCAL_FIXTURE_ONLY`
   - W2 — `checkpoint_key=2026-07-W2`, status `reviewed`
   - W3 — `checkpoint_key=2026-07-W3`, status `draft`
3. Date ranges: first/second/third week windows **inside** parent period dates.
4. Reject duplicate `week_index`.
5. Reject duplicate `checkpoint_key`.
6. Reject invalid `reporting_period_id` FK.
7. No real client data.

Idempotent re-apply of migration must be a no-op after ledger success.

---

## 6. Commit policy (next wave)

- Exact-path stage of allowlisted migration + docs only.
- No `git add .` / `-A` / `commit -a`.
- Preserve foreign WIP.
- No push unless operator charter explicitly authorizes push (default **no push**).
- Optional hash-record follow-up for closeout report only.

Suggested primary message pattern:

`feat(iseo-report-hub): add db04 weekly checkpoints migration`

(Exact message is set by the apply charter.)

---

## 7. STOP conditions (next wave)

Stop before mutation if:

- Wrong root / volume / branch
- Non-empty staged index with foreign paths
- Unexpected i-SEO WIP outside apply allowlist
- DB host ≠ `127.0.0.1` or DB name ≠ `iseo_report_hub_dev`
- Migration `_000003` already applied with different checksum and no repair charter
- Apply charter attempts CRUD UI or monthly content schema in same wave without explicit expansion

Output token pattern:

`STOP — I-SEO WEEKLY CHECKPOINTS DB-04 MIGRATION APPLY SAFETY CONDITION FAILED`

---

## 8. Explicit non-goals of next wave

- Weekly checkpoint CRUD UI
- Monthly report editor / content table
- Report blocks
- Production deployment
- Auto week-generation product tool (beyond optional demo insert)
