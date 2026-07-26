# I-SEO Report Hub — DB-06 Report Blocks Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no SQL created; no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md)

---

## 1. Purpose

Define the **DB-06 Report Blocks** data-model layer so the next implementation wave can add an ordered `report_blocks` table under `monthly_report_contents` in local `iseo_report_hub_dev` without building a block editor, export pipeline, or client portal.

DB-06 is the **structured composition layer** inside one monthly report working document. It sits under:

- `reporting_periods` (month/period shell);
- `weekly_checkpoints` (weekly internal progress snapshots);
- `monthly_report_contents` (monthly working document; DB-05 TEXT fields remain fallback).

This charter is **documentation / policy only**. It does **not** authorize migration SQL, app edits, runtime sync, fixture mutation, or DB mutation in this wave.

---

## 2. Current Baseline

### Monthly Report Content CRUD (primary dependency)

| Item | Value |
|------|-------|
| Primary commit | `65f6412443c7236f17cbf54db3b259a59eccb288` — `feat(iseo-report-hub): add monthly report content crud` |
| Hash-record | `17553a555948120fa3b84184a6610668a0ced2e5` — `docs(iseo-report-hub): record monthly report content crud commit hash` |
| Clarify | `eb00b3f409649069bd47c187885af126a7f96863` — `docs(iseo-report-hub): clarify monthly report content crud commit hash record` |
| Expected HEAD at charter start | `eb00b3f409649069bd47c187885af126a7f96863` |
| Surface | Period-scoped monthly detail/create/edit; archive-by-status; CSRF; source weekly checkpoint validation; **no DELETE** |
| Smoke | monthly id **1** → `in_progress`; sources `[1,2,3,7]`; `LOCAL_FIXTURE_ONLY` |

### DB-05 Monthly Report Content migration apply

| Item | Value |
|------|-------|
| Primary commit | `aac9c18ef49fc3b715106882893e18e280176800` — `feat(iseo-report-hub): add monthly report content migration` |
| Hash-record | `32674ea911ce9fd8740b329db114b87eb65a9389` |
| Migration | `2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Checksum (SHA-256) | `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |
| Batch | **4** |

### Supporting baseline commits (context)

| Wave | Primary | Hash-record |
|------|---------|-------------|
| Auth persistence | `d4b3b2e2…` | `0cd2cfb7…` |
| Reporting Period CRUD | `392258fc…` | `f1d8a17e…` |
| Weekly Checkpoints CRUD | `911db07d…` | `64c42cbe…` (+ clarify `6f968ed2` / `865cd4b5`) |

### DB baseline (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **4** |
| Tables count | **12** |
| Users / roles | **1** / **6** |
| Clients / projects / sites | **1** / **1** / **1** |
| Reporting periods | **2** (`2026-07` draft id **1**; `2026-08` archived id **3**) |
| Weekly checkpoints | **4** |
| Monthly report contents | **1** (id **1**, `in_progress`, period `2026-07`) |
| `report_blocks` | **Absent** (expected) |

### Current monthly report content row (id 1)

| Field | Value |
|-------|-------|
| `reporting_period_id` | **1** / period `2026-07` |
| `status` | `in_progress` |
| `title` | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| Content markers | `LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` |
| `created_by` / `updated_by` | **1** / **1** (local admin) |

### Current weekly checkpoint data (under period `2026-07`)

| Id | Key | Status | Marker |
|----|-----|--------|--------|
| 1 | `2026-07-W1` | `completed` | `LOCAL_FIXTURE_ONLY` |
| 2 | `2026-07-W2` | `reviewed` | `LOCAL_FIXTURE_ONLY` |
| 3 | `2026-07-W3` | `draft` | `LOCAL_FIXTURE_ONLY` |
| 7 | `2026-07-W4` | `skipped` | `LOCAL_FIXTURE_ONLY` |

### Current limitation

- Period shell CRUD exists.
- Weekly checkpoint CRUD exists.
- Monthly report content CRUD exists (flat structured TEXT fields).
- **No** report block DB model / table / rows.
- **No** block editor / ordering UI.
- **No** block-level source refs (beyond parent monthly JSON hint).
- **No** Topvisor / API metrics tables.
- **No** export / public share / client portal.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Problem

Monthly report content exists, but content is still **flat structured text fields**. There is no block-level composition model.

Without DB-06:

1. Ordered sections cannot be stored as first-class rows.
2. Block types / per-section lifecycle cannot be modeled independently of the parent monthly document.
3. Future block editor / reorder UX has nothing to bind to.
4. Block-level source weekly checkpoint and metric placeholders cannot be recorded.
5. Composition remains limited to DB-05 TEXT columns until a structured layer exists.

DB-06 closes the schema gap for **ordered structured content blocks inside one monthly report**. It does **not** deliver the editor, PDF/export, or client portal.

---

## 4. Scope

### In scope

- `report_blocks` table design (fields, block types, statuses, FKs, indexes, uniqueness, JSON policy)
- Relation to `monthly_report_contents` (N:1)
- Soft relation to `weekly_checkpoints` (JSON snapshot ids per block)
- Metric ref placeholder JSON (no Topvisor/import tables yet)
- Ordered internal content sections (`sort_order` + `block_key`)
- Block lifecycle (independent, with parent finalize lock policy)
- Constraints / validation / apply / smoke plan for the next migration wave
- OPERATIONAL-INDEX status update

### Out of scope

- Migration SQL authoring (deferred to apply wave)
- App-source / runtime / DB mutation in this charter wave
- Report block CRUD UI / routes / controllers / views
- Drag/drop editor / Markdown / rich text editor
- PDF / export / public share
- Client portal
- Topvisor / API integration / import tables
- Evidence / uploads
- n8n reminder automation
- Real client data / production
- Replacing or dropping DB-05 TEXT fields

**Programme numbering after DB-05:**

- DB-03 = `reporting_periods` (**done**)
- DB-04 = `weekly_checkpoints` (**done**)
- DB-05 = `monthly_report_contents` (**done** + CRUD)
- **DB-06 = `report_blocks` only** (this charter)
- Evidence / publish snapshots remain later phases

---

## 5. Product Model

1. A **reporting period** is the monthly shell for one project.
2. **Weekly checkpoints** are internal weekly progress snapshots under that period.
3. **Monthly report content** is the final/monthly working document for that period (at most one row per period).
4. **Report blocks** are ordered structured sections **inside** one monthly report content row.
5. MVP: **one row per section** (e.g. executive summary, work completed), identified by `block_key` + typed by `block_type`.
6. DB-05 TEXT fields remain the **canonical fallback / summary layer** until a block editor is implemented and accepted. Blocks are **additive**, not a replacement in this wave.
7. `source_weekly_checkpoint_ids` on a block is an optional **JSON array of checkpoint ids** as a soft snapshot hint; join table deferred.
8. `source_metric_refs` / `data_json` are **JSON placeholders** only — Topvisor/import tables do not exist yet.
9. Ownership chain: `report_block` → `monthly_report_content` → `reporting_period` → `project` → `client`.
10. Block status is **independent** of parent monthly status at DB level, except future app policy: parent `finalized` locks block editing.
11. Blocks are **internal-only** in MVP — no public/client view now.
12. No hard DELETE in MVP — archive instead.

### Design resolutions

| Question | Decision |
|----------|----------|
| Replace DB-05 TEXT fields? | **No** — additive structured layer; DB-05 remains fallback |
| One row per section? | **Yes** for MVP |
| Strict unique `sort_order`? | **No** — non-unique index; service-level reorder later |
| Weekly sources: JSON or join? | **JSON** in MVP; join table deferred |
| Metric refs normalized? | **No** — JSON placeholder only |
| Independent block lifecycle? | **Yes**, but parent finalized locks editing (app policy) |
| Hard delete? | **No** — archive |
| CRUD immediately after migration? | **No** — charter CRUD/editor separately after apply |

---

## 6. Safety Boundary

| Boundary | Rule |
|----------|------|
| This wave | Docs only under allowlisted Active Brain paths |
| App-source | **No** edits |
| Runtime | **No** edits / **no** sync |
| DB | **No** mutation; optional read-only status only |
| SQL / migration files | **Not** created in this wave |
| Report block / monthly / weekly / period rows | **Unchanged** |
| Admin / password / hash | **Unchanged** |
| `.env` / `.env.local` | **Unchanged** |
| Real client data | **Forbidden** |
| Production | **Forbidden** |
| Foreign WIP | **Preserve** |
| Push | **No** |

---

## 7. Migration Boundary

Next apply wave (not this charter) may:

- Author **one** migration SQL file for `report_blocks`
- Sync that migration file only to Localhost runtime
- Run `db-migrate.php apply` against `iseo_report_hub_dev` @ `127.0.0.1`
- Optionally insert **local fixture blocks** under monthly report content for period `2026-07`
- Update result docs / OPERATIONAL-INDEX if chartered

Next apply wave must **not**:

- Add report block CRUD controllers/views/editor
- Edit prior migrations (`000001`–`000004`)
- Mutate auth users/roles/passwords
- Mutate monthly/weekly/period rows except by inserting child block smoke rows
- Insert real client data
- Create evidence / publish / Topvisor schema unless separately chartered

Planned migration filename:

`2026_07_26_000005_create_report_blocks_table.sql`

(Sequence `_000005` is authoritative; date prefix follows project convention / charter day.)

---

## 8. Validation Gates

Charter wave gates (this wave):

1. Preflight: root / `AI WS` / branch / empty staged / clean i-SEO WIP.
2. Docs created on allowlist only.
3. No app-source / runtime / DB / SQL changes.
4. Scoped docs commit; no push.

Future apply-wave gates (summary; detail in validation plan):

1. Migration count **4 → 5**; table count **12 → 13**.
2. Columns / indexes / FKs / CHECKs present.
3. Idempotent re-apply.
4. Fixture blocks for monthly content of period `2026-07` (if smoke chartered).
5. Duplicate `(monthly_report_content_id, block_key)` rejected.
6. Invalid parent FK rejected.
7. Invalid status / block_type rejected (if DB CHECK used).
8. JSON validity verified via MySQL JSON type.
9. Parent monthly / weekly / period rows unchanged except new child block rows.
10. Health/app regression (period + weekly + monthly CRUD still work; no secrets printed).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Overbuilding into block editor / publish stack | Schema + lifecycle only; defer CRUD/editor/export/portal |
| Premature replacement of DB-05 TEXT | Explicit additive policy; TEXT remains fallback |
| Strict unique sort_order blocking reorder drafts | Non-unique index; service reorder later |
| Treating JSON weekly/metric ids as hard FK | Document as soft hints; no cascade; resolve dynamically in smoke |
| Cascading monthly deletes wiping block history | FK `ON DELETE RESTRICT` |
| Hard DELETE of blocks | No DELETE in MVP; archive instead |
| Seeding real-looking client narrative | `LOCAL_FIXTURE_ONLY` markers; no production |
| Coupling block status to weekly/period status in DDL | Forbid DB triggers; app policy later |

---

## 10. Next Implementation Wave

**One next action only:**

`I-SEO Report Hub — Report Blocks DB-06 Migration Apply 01`

That wave authors/applies migration `_000005`, validates structure, and may insert local fixture blocks under monthly report content for period `2026-07`. It does **not** implement report block CRUD UI or editor.
