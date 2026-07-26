# I-SEO Report Hub — Report Blocks CRUD Design v0.1

**Status:** DESIGN ONLY — no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md)

---

## 1. Routes

| Method | Path | Auth | CSRF | Action |
|--------|------|------|------|--------|
| GET | `/monthly-reports/{monthly_report_id}/blocks` | Required (internal role) | — | Block list for monthly report (ordered by `sort_order`) |
| GET | `/monthly-reports/{monthly_report_id}/blocks/create` | Required + create capability | — | Create form |
| POST | `/monthly-reports/{monthly_report_id}/blocks` | Required + create capability | Required | Store new block |
| GET | `/report-blocks/{id}` | Required (internal role) | — | Detail by id |
| GET | `/report-blocks/{id}/edit` | Required + edit capability | — | Edit form |
| POST | `/report-blocks/{id}` | Required + edit capability | Required | Update (fields + status + sort_order) |

**Optional (not required for MVP):**

| Method | Path | Notes |
|--------|------|-------|
| GET | `/report-blocks` | Admin index only if useful; monthly-report-scoped entry is enough |

**Not routed in MVP:**

- Separate POST status-only routes (status lives in edit form)
- Separate reorder endpoint (manual `sort_order` on edit form is enough)
- `DELETE /report-blocks/{id}`
- Drag/drop / bulk endpoints
- Client-facing / public share URLs

**Routing note:** Existing `Router` is exact-match. Register static `/blocks`, `/blocks/create`, and `/edit` segments before parameterized collisions with `/monthly-reports/{id}` and `/report-blocks/{id}`. Prefer request-time exact-path registration (same pattern as Monthly Report Content + Weekly Checkpoints CRUD).

---

## 2. Controller / service / repository

### Controller

`app-source/app/Controllers/ReportBlockController.php`

Methods (recommended):

- `index(int $monthlyReportId)` — list for parent monthly
- `create(int $monthlyReportId)` — GET form
- `store(int $monthlyReportId)` — POST create
- `show(int $id)` — detail by id
- `edit(int $id)` — GET form
- `update(int $id)` — POST update

Controller responsibilities:

- Auth gate (`isAuthenticated` + internal role / capability)
- CSRF validate on POST
- Map request → service input
- Render views or redirect with flash
- Never echo secrets / stack traces

### Service

`app-source/app/Services/ReportBlockService.php`

Responsibilities:

- Validation rules (parent monthly, uniqueness, status transitions, block_key/type, JSON, source ids, users, lengths, sort_order)
- Status transition matrix + timestamp policy (`reviewed_at` / `approved_at`)
- Field lock enforcement (immutable parent; draft-only key/type; approved / parent-finalized locks)
- Role capability checks for mutations
- Resolve parent monthly → reporting period for source weekly validation
- Audit event emission (recommended)
- Friendly error messages

### Repository

`app-source/app/Repositories/ReportBlockRepository.php`

Responsibilities:

- Find by id (with parent monthly + period join context)
- List by `monthly_report_content_id` ordered by `sort_order`, `id`
- Insert / update
- Exists check for `(monthly_report_content_id, block_key)` uniqueness
- Load parent monthly for context / lock checks
- Load weekly checkpoints for the parent period (source selection + link labels)
- Load internal users for owner/reviewer selects
- Optional count by status for dashboard

Prefer PDO via existing `DatabaseService`; no new ORM. May reuse `MonthlyReportContentRepository` / `WeeklyCheckpointRepository` / `ReportingPeriodRepository` for parent/source loads (read-only from block wave perspective).

Wire in `routes.php` + `bootstrap.php` (require classes) following Monthly Report Content CRUD patterns.

---

## 3. Views

| View path | Purpose |
|-----------|---------|
| `app/Views/pages/report-blocks/index.php` | List under monthly report context |
| `app/Views/pages/report-blocks/show.php` | Detail / preview + parent context + source checkpoint links |
| `app/Views/pages/report-blocks/form.php` | Shared create/edit fields |
| `app/Views/pages/report-blocks/create.php` | Create wrapper |
| `app/Views/pages/report-blocks/edit.php` | Edit wrapper |

Parent integration:

- Update `app/Views/pages/monthly-reports/show.php` with a **report blocks** section:
  - table ordered by `sort_order`;
  - status / type / title / source summary / edit links;
  - create block link;
  - link to full block list if useful.

Reporting period detail may keep current monthly report section only — **no** need to embed all blocks there.

Reuse:

- `layout.php`, `partials/header.php`
- Existing CSS (`public/assets/css/app.css`); extend status/type badges if needed
- No CDN / external assets
- No drag/drop JS libraries

---

## 4. Form fields

### Create (`GET/POST …/blocks`)

| Field | Control | Required | Notes |
|-------|---------|----------|-------|
| `monthly_report_content_id` | from route | Yes | Display only; not editable |
| `block_key` | text | Yes | Slug-like `[a-z0-9_\-]+`; ≤64 |
| `block_type` | select | Yes | Allowlist from DB CHECK |
| `sort_order` | number | Yes | Integer ≥0; default next step (e.g. 60) |
| `status` | select | Yes | Default `draft` |
| `title` | text | Yes | Smoke: keep / include `LOCAL_FIXTURE_ONLY` |
| `body` | textarea | No | Soft ≤50000 |
| `summary` | textarea | No | Soft ≤10000 |
| `data_json` | textarea (JSON) | No | Object/array; smoke marker OK |
| `source_weekly_checkpoint_ids` | checkboxes of period checkpoints | No | Default parent monthly sources or all period checkpoints |
| `source_metric_refs` | textarea (JSON) | No | Object/array; no metric FK yet |
| `owner_user_id` | select users (nullable) | No | Internal users only |
| `reviewer_user_id` | select users (nullable) | No | Internal users only |
| `_csrf` | hidden | Yes | Via `CsrfService::field()` |

Server-set:

- `created_by` = current user id
- `updated_by` = null on create (or same as created_by — pick one; recommend null until first update)
- `reviewed_at` / `approved_at` = null unless status starts as reviewed/approved (discouraged; prefer draft)

### Edit (`GET/POST /report-blocks/{id}`)

| Field | Editable when |
|-------|---------------|
| `monthly_report_content_id` | **Never** (immutable) |
| `block_key` | While `draft`, unless `admin_owner` |
| `block_type` | While `draft`, unless `admin_owner` |
| `sort_order` | Until parent monthly `finalized`, unless privileged |
| `title` / `body` / `summary` / JSON / source refs | Until `approved` or parent finalized, unless privileged |
| `status` | Per transition + role matrix |
| `owner_user_id` / `reviewer_user_id` | `admin_owner` / `seo_lead_reviewer` |

Server-set:

- `updated_by` = current user id
- `reviewed_at` / `approved_at` per timestamp policy

---

## 5. Detail page fields

Show all schema fields relevant to ops:

- Identity: id, block_key, block_type badge, sort_order, status badge, title
- Parent monthly: id / title / status (link to `/monthly-reports/{id}`)
- Parent period: id / period_key / title / status (via monthly; link to `/reporting-periods/{id}`)
- Status timestamps: reviewed_at / approved_at
- body / summary
- `data_json` / `source_metric_refs` (pretty-printed JSON, no secrets)
- Source weekly checkpoints: resolved list with links to `/weekly-checkpoints/{id}`
- Owner / reviewer / created_by / updated_by
- created_at / updated_at

No secrets. No private metrics. No DELETE control. No drag/drop controls.

---

## 6. Relation to monthly report

| Rule | Design |
|------|--------|
| Parent FK | Required; RESTRICT delete |
| Uniqueness | Unique `(monthly_report_content_id, block_key)` |
| Nested list/create | Under `/monthly-reports/{monthly_report_id}/blocks…` |
| Flat detail/edit | `/report-blocks/{id}` (+ `/edit`) |
| Monthly show integration | Report blocks section: ordered table + create link |
| Parent lock | Parent `finalized` → lock block create/edit except privileged; parent `archived` → block create/edit for non-`admin_owner` |
| Rollup | MVP does **not** auto-update parent monthly status from block changes |
| Parent TEXT fields | Remain fallback; no automatic overwrite from blocks in MVP |
| Parent row mutation | Block CRUD must **not** UPDATE/DELETE monthly report content rows |

Current fixture parent status `in_progress` → editable.

---

## 7. Relation to reporting period

| Rule | Design |
|------|--------|
| Direct FK | **None** — period resolved through parent monthly |
| Context | Always show period via monthly parent on list/detail/forms |
| Period show | Keep monthly report section only; do **not** require embedding all blocks |
| Period mutation | Block CRUD must **not** UPDATE/DELETE reporting period rows |

---

## 8. Relation to weekly checkpoints

| Rule | Design |
|------|--------|
| Source hint | JSON array `source_weekly_checkpoint_ids` |
| Validation | Each id exists; belongs to same `reporting_period_id` as parent monthly; valid JSON array |
| Empty sources | Allowed; show warning / “no sources selected” |
| UI | Checkboxes of parent period checkpoints; detail page shows links |
| Coupling | Weekly status changes do **not** auto-change block status |
| Aggregation | No automatic copy of weekly TEXT into block body |
| Mutation | Block CRUD must **not** UPDATE/DELETE weekly checkpoint rows |

Prefer resolving smoke sources by checkpoint_key (`2026-07-W1`…`W4`) rather than hard-coding ids in application logic; fixture docs may still cite known ids `[1,2,3,7]`.

---

## 9. Status workflow

Allowed statuses (DB CHECK + app):

`draft`, `in_progress`, `ready_for_review`, `reviewed`, `approved`, `archived`

Recommended transitions:

| From | To |
|------|----|
| `draft` | `in_progress` |
| `in_progress` | `ready_for_review` |
| `ready_for_review` | `reviewed` |
| `reviewed` | `approved` |
| any non-`approved` | `archived` |
| `ready_for_review` | `in_progress` (revision request; optional if simple) |
| `approved` reopen | `draft` or `in_progress` — **`admin_owner` / `seo_lead_reviewer` only** |
| `archived` reopen | Prefer `admin_owner` / `seo_lead_reviewer` |

Timestamps:

| Event | Policy |
|-------|--------|
| Enter `reviewed` | Set `reviewed_at` if null |
| Enter `approved` | Set `approved_at` if null |
| Leave reviewed/approved (privileged reopen) | **Keep** timestamps as history by default; set `updated_by` + audit |
| Enter `archived` | Do not require `approved_at` |

Approved content locked except `admin_owner` / `seo_lead_reviewer`. Status changes occur via the edit form (no separate status POST routes in MVP).

---

## 10. Validation

| Rule | Expect |
|------|--------|
| `monthly_report_content_id` exists | Required (from route on create) |
| Parent not finalized/archived | Block create/edit unless privileged (`admin_owner`; lead per charter) |
| `block_key` | Required; ≤64; slug-like `[a-z0-9_\-]+` |
| Unique `(parent, block_key)` | Guard + friendly error |
| `block_type` | In allowlist (executive_summary … weekly_summary) |
| `sort_order` | Integer ≥0 |
| Status | In allowlist + transition legal for role |
| `source_weekly_checkpoint_ids` | Valid JSON array; ids exist; same period as parent monthly; empty OK with warn |
| `source_metric_refs` | Valid JSON object/array; no metric FK validation yet; safe size |
| `data_json` | Valid JSON object/array; safe size |
| `title` | Required; ≤255 |
| `body` | Soft ≤50000 chars |
| `summary` | Soft ≤10000 chars |
| Owner/reviewer | Exist; internal users if set |
| Smoke content | No real client data; prefer `LOCAL_FIXTURE_ONLY` |

Surface uniqueness/CHECK/JSON violations as friendly form errors; no SQL errors in HTML.

---

## 11. Audit

Recommended events:

- `report_block.created`
- `report_block.updated`
- `report_block.status_changed`
- `report_block.reviewed`
- `report_block.approved`
- `report_block.archived`
- `report_block.reordered`

Payload: block id, monthly report content id, period id (resolved), old/new status or sort_order when relevant. No secrets / private metrics.

---

## 12. Navigation

| Surface | Change |
|---------|--------|
| Monthly report show | Report blocks section + ordered table + create/edit links |
| Block list | Parent monthly (+ period) context always visible |
| Block detail/edit/create | Parent monthly + period context; source weekly links |
| Reporting period show | Keep monthly section only; no full block embed required |
| Header top-level | Optional; **not required** — workflow is monthly-report-scoped |
| Dashboard | Optional `report_blocks` count if simple |

---

## 13. Error handling

- Unauthenticated → `/login`
- Forbidden role → safe 403 or redirect with flash
- Missing monthly/block row → safe 404
- Duplicate `block_key` → friendly error
- Validation failure → re-render form with errors + old input
- CSRF failure → reject; no mutation
- DB unique/CHECK/JSON → catch and map to friendly message
- Never leak stack traces, SQL, passwords, hashes, session ids

---

## 14. No-delete policy

| Action | MVP |
|--------|-----|
| DELETE route | **Forbidden** |
| DELETE UI button | **Forbidden** |
| Soft path | `archived` via status on edit form |
| Smoke cleanup DELETE | Not in this feature wave (unless separate destructive charter) |
| Monthly delete while blocks exist | Blocked by FK RESTRICT |
| Archive frees unique key | **No** — reopen/edit the same row |

Prefer archive over inventing hard-delete escapes.

---

## 15. No-drag/drop policy

| Action | MVP |
|--------|-----|
| Drag/drop reorder UI | **Forbidden** |
| Sortable JS libraries / CDN | **Forbidden** |
| Manual `sort_order` input | **Allowed** on create/edit |
| Batch reorder endpoint | Deferred; not required for MVP |
| Audit `report_block.reordered` | Optional when sort_order changes |

Ordering is operator-controlled via integer field only in this CRUD wave.
