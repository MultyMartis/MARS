# I-SEO Report Hub — Report Blocks CRUD Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый управляемый CRUD/editor-слой** для `report_blocks` на локальном MVP после:

- DB-backed auth baseline;
- Reporting Period CRUD Implementation 01;
- Weekly Checkpoints CRUD Implementation 01;
- Monthly Report Content CRUD Implementation 01;
- DB-06 `report_blocks` migration apply + 5 local fixture blocks under monthly report content id **1** / period `2026-07`.

Цель charter:

1. Зафиксировать текущий baseline после DB-06 apply.
2. Спроектировать MVP internal CRUD/editor для `report_blocks` (без drag/drop).
3. Определить routes / controller / service / repository / views / nav.
4. Определить relation с `monthly_report_contents`, `reporting_periods`, `weekly_checkpoints`.
5. Определить lifecycle, field locks, validation, role access.
6. Подготовить smoke/validation plan для следующей implementation wave.
7. Явно исключить drag/drop, PDF/export, Topvisor, client portal, public share, DELETE.
8. Не менять app-source / runtime / DB в этой волне.

Эта волна — **documentation / policy only**. CRUD **не** кодируется здесь.

---

## 2. Current Baseline

### Auth implementation

| Item | Value |
|------|-------|
| Primary commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Hash-record | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` |
| Users / roles | **1** / **6** |
| Local admin | `admin@iseo-report-hub.test` / `admin_owner` (password/hash **not** recorded) |

### Reporting Period CRUD

| Item | Value |
|------|-------|
| Primary commit | `392258fc572ac17b479618ba888b6b2ffe0feb68` — `feat(iseo-report-hub): add reporting period crud` |
| Hash-record | `f1d8a17e52fd7eb401b34cb3d044a061ebb6f5e7` |
| Periods | `2026-07` id **1** draft fixture; `2026-08` id **3** archived smoke |

### Weekly Checkpoints CRUD

| Item | Value |
|------|-------|
| Primary commit | `911db07d8ca51bb1778c53ca570ef3b8950234a0` — `feat(iseo-report-hub): add weekly checkpoints crud` |
| Hash-record | `64c42cbe6616be19b6d8ea3340466e7bab1f7bf9` |
| Clarify | `6f968ed2` / `865cd4b5` |
| Checkpoints | W1 id **1** completed; W2 id **2** reviewed; W3 id **3** draft; W4 id **7** skipped — all `LOCAL_FIXTURE_ONLY` |

### Monthly Report Content CRUD

| Item | Value |
|------|-------|
| Primary commit | `65f6412443c7236f17cbf54db3b259a59eccb288` — `feat(iseo-report-hub): add monthly report content crud` |
| Hash-record | `17553a555948120fa3b84184a6610668a0ced2e5` |
| Clarify | `eb00b3f409649069bd47c187885af126a7f96863` |
| Demo monthly | id **1**; period `2026-07`; status `in_progress`; sources `[1,2,3,7]` |

### DB-06 Report Blocks migration apply

| Item | Value |
|------|-------|
| Primary commit | `1b71a0213c61844258a87afb68f9b796bd35443f` — `feat(iseo-report-hub): add report blocks migration` |
| Hash-record | `7393d7c1d287bb8d180e41be26d37f738e330821` |
| Clarify | `86338d666f08146b6feff06536ae6d7b50eb332c` |
| Migration | `2026_07_26_000005_create_report_blocks_table.sql` |
| Checksum (SHA-256) | `951bc88826a6155a624377b43851f1d6f7eadb8fdf7d229cb5bffe952eee3236` |
| Batch | **5** |
| Validation | FK / unique / CHECK / JSON expected failures + rollback; Reporting Period + Weekly Checkpoint + Monthly Report Content CRUD regression PASS |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations | **5** |
| Tables | **13** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **5** |

### Parent monthly report content

| Field | Value |
|-------|-------|
| Id | **1** |
| Parent period | id **1** / `2026-07` / draft |
| Status | `in_progress` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` (W1–W4) |
| created_by / updated_by | **1** / **1** |

### Fixture report blocks

Parent: monthly report content id **1** / period `2026-07`. All status `draft`. Sources `[1,2,3,7]`. Content markers `LOCAL_FIXTURE_ONLY`.

| block_key | sort_order | status |
|-----------|------------|--------|
| `executive_summary` | 10 | `draft` |
| `work_completed` | 20 | `draft` |
| `results_summary` | 30 | `draft` |
| `key_findings` | 40 | `draft` |
| `next_month_plan` | 50 | `draft` |

### Current limitation

- **No** report block CRUD / UI / routes / controller / service / repository.
- **No** block editor.
- **No** block reorder UI (manual `sort_order` field planned for next wave; **no** drag/drop).
- **No** PDF / export.
- **No** Topvisor / API integration / metric tables.
- **No** client portal / public share.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- Internal report block **list / detail / create / edit / status lifecycle**
- Monthly-report-scoped entry: `/monthly-reports/{monthly_report_id}/blocks`
- Flat block detail/edit: `/report-blocks/{id}` (+ `/edit`)
- Auth required on all CRUD routes; CSRF on all POST
- Source weekly checkpoint selection/reference (`source_weekly_checkpoint_ids`)
- Manual `sort_order` input (no drag/drop)
- Role-aware create/edit/status boundaries (MVP matrix)
- Validation for parent monthly, uniqueness `(parent, block_key)`, status transitions, JSON, source ids, lengths
- Optional audit events for create/update/status/reviewed/approved/archived/reordered
- Navigation: monthly report detail → report blocks section (ordered table + create link)
- Local fixture smoke using monthly id **1** + existing 5 blocks + optional additional `risks_and_blockers`
- Design + implementation + validation plans for next wave

### Out of scope

- Drag / drop reorder UI
- Rich text / Markdown editor
- PDF / export / public share
- Topvisor / API imports / n8n reminders / evidence uploads / metric tables
- Client portal / `client_viewer` access
- Hard DELETE / bulk actions
- Schema / migration changes
- Real client data
- Production deployment
- Mutations to `monthly_report_contents`, `weekly_checkpoints`, or `reporting_periods` rows (except reading parent context)

---

## 4. Product Rules

1. A report block is a **child** of one `monthly_report_contents` row (`ON DELETE RESTRICT`); unique `(monthly_report_content_id, block_key)`.
2. UX is a **simple internal block editor**, not a drag/drop page builder: list under monthly report; open/edit/archive individual blocks.
3. Status lifecycle follows [REPORT-BLOCKS-LIFECYCLE-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md).
4. Soft retire via `archived` only — **no DELETE** route/UI in MVP. Archiving does **not** free the unique `(parent, block_key)` slot.
5. Parent monthly `finalized` locks block editing except privileged roles; parent monthly `archived` blocks create/edit for non-`admin_owner`.
6. Field locks: `monthly_report_content_id` immutable; `block_key` / `block_type` editable only while `draft` unless `admin_owner`; content editable until `approved` or parent finalized unless privileged.
7. `source_weekly_checkpoint_ids` must reference checkpoints that exist and belong to the **same reporting period** as the parent monthly report; empty array allowed with warning.
8. Manual `sort_order` (≥0 integer); non-unique at DB; list order by `sort_order`, tie-break `id`. **No** drag/drop in MVP.
9. Smoke / demo rows must carry `LOCAL_FIXTURE_ONLY` markers; no real client data.
10. Reuse existing i-SEO Report Hub internal UI patterns (Monthly Report / Weekly Checkpoint / Reporting Period CRUD style); no CDN.
11. MVP does **not** auto-rollup parent monthly status from block statuses; does **not** mutate weekly or period rows from block edits.

---

## 5. Access Model

| Role | List / detail | Create / edit draft–in_progress | ready_for_review | reviewed / approved | archived | Reopen approved | Reorder (`sort_order`) |
|------|---------------|----------------------------------|------------------|---------------------|----------|-----------------|------------------------|
| `admin_owner` | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| `seo_lead_reviewer` | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| `seo_specialist` | Yes | Yes | Yes (submit) | No | No | No | Limited (own draft/in_progress until parent lock) |
| `account_client_manager` | Read-only | No | No | No | No | No | No |
| `internal_viewer` | Read-only | No | No | No | No | No | No |
| `client_viewer` | **No** | No | No | No | No | No | No |

Unauthenticated → redirect `/login`.

Current smoke may only have `admin_owner`. Multi-role HTTP denial paths may be **policy covered / not multi-user smoked**.

---

## 6. Data Policy

| Rule | Policy |
|------|--------|
| Parent monthly for smoke | id **1** / period `2026-07` / status `in_progress` |
| Existing fixture blocks | Prefer edit `executive_summary`; create optional `risks_and_blockers` with `LOCAL_FIXTURE_ONLY` |
| Source checkpoints | Prefer resolve by key `2026-07-W1`…`W4`; known ids `[1,2,3,7]` |
| Parent monthly / weekly / period rows | **Read only** from block CRUD wave (no UPDATE/DELETE) |
| Real client data | **Forbidden** |
| Schema changes | **Forbidden** in CRUD implementation wave |
| Credentials in docs | **Forbidden** |

---

## 7. Implementation Boundary

This charter wave:

- **May** create/update Active Brain product docs + OPERATIONAL-INDEX + closeout REPORT.
- **Must not** edit `app-source/**`, Localhost runtime, SQL/migrations, fixtures, env, users/passwords.
- **Must not** mutate `report_blocks`, `monthly_report_contents`, `weekly_checkpoints`, or `reporting_periods` rows.
- **Must not** push / fetch / pull / reset / clean / stash / broad git add.

Next wave implements CRUD per design + implementation plan under a separate operator charter.

---

## 8. Validation Gates

Before declaring next-wave implementation complete (summary; detail in validation plan):

1. Preflight: root / volume / branch / DB target / DB-06 baseline intact (migrations **5**, report_blocks **5**+).
2. Route smoke: monthly-scoped block list/create; flat detail/edit; unauth redirect; **no DELETE**.
3. Form/CSRF smoke: POST rejected without valid CSRF.
4. DB edit/create/status smoke: edit `executive_summary`; create `risks_and_blockers`; status → `in_progress`; manual `sort_order`.
5. Duplicate `block_key` refused; invalid JSON refused; invalid/cross-period source weekly ids refused.
6. Monthly report detail shows report blocks section ordered by `sort_order`.
7. Audit events present if implemented.
8. Regression: reporting period CRUD, weekly checkpoint CRUD, monthly report CRUD, `/login`, `/health`, `/not-existing`.
9. No drag/drop UI; no real client data; no schema change; parent monthly/weekly/period counts unchanged except intended `report_blocks` inserts/updates.

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Nested monthly `/blocks` + flat `/report-blocks/{id}` confuse Router exact-match | Mirror Monthly/Weekly pattern: static segments before dynamic id; request-time exact-path registration |
| Duplicate `(parent, block_key)` | Service uniqueness guard + friendly error on errno 1062 |
| Editing approved / parent-finalized content by non-privileged | Field/status locks in service; reopen only `admin_owner` / `seo_lead_reviewer` |
| Cross-period source weekly ids | Validate checkpoint belongs to parent monthly’s `reporting_period_id` |
| Invalid JSON in `data_json` / `source_metric_refs` / source ids | Normalize + validate; catch MySQL 3140; friendly form errors |
| Multi-role matrix untested (one admin user) | Document SAFE SIMPLIFICATION / deferred multi-user smoke |
| Status transition graph only app-enforced | Align service with lifecycle doc; DB CHECK only values |
| Scope creep into drag/drop / PDF / portal / Topvisor | Hard out-of-scope list; STOP if charter expands |
| Accidental mutation of monthly/weekly/period rows | Explicit data policy: block CRUD mutates `report_blocks` (+ optional audit) only |

---

## 10. Next Implementation Wave

**`I-SEO Report Hub — Report Blocks CRUD Implementation 01`**

Implement internal report block CRUD/editor over existing DB-06 table using Model A source → runtime sync, local fixture monthly id **1** / period `2026-07`, and the 5 fixture blocks (+ optional `risks_and_blockers`) — without drag/drop, PDF/export, client portal, schema changes, or hard delete.

See:

- [DESIGN-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md)
- [IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md)
- [VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-VALIDATION-PLAN-v0.1.md)
