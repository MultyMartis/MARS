# I-SEO Report Hub — Report Finalization Design v0.1

**Status:** DESIGN / PLANNING ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Finalization Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md)

---

## 1. Lifecycle

Finalization is the internal close of a monthly report for a reporting period.

Meaning:

- Content is considered complete for internal operational use;
- Monthly row is locked for normal editing;
- Child report blocks are locked for normal create/edit;
- Preview/print remain available to internal readers;
- **Not** public publish, **not** PDF, **not** client approval, **not** immutable snapshot.

Existing schema columns are sufficient:

- `monthly_report_contents.status`, `finalized_at`
- `report_blocks.status`, `approved_at`
- audit log

No MVP migration.

---

## 2. Status Transitions

Monthly allowlist (DB-05):

`draft` | `in_progress` | `ready_for_review` | `reviewed` | `finalized` | `archived`

### Recommended staged graph

| From | To | Action | Notes |
|------|----|--------|-------|
| `draft` | `in_progress` | edit / start work | existing CRUD may already support |
| `in_progress` | `ready_for_review` | `submit-review` | specialist+ |
| `ready_for_review` | `reviewed` | `mark-reviewed` | lead+ |
| `reviewed` | `finalized` | `finalize` | readiness gates required |
| any ≠ `finalized` | `archived` | archive-by-status | existing archive pattern |
| `finalized` | `reviewed` | `reopen` | admin_owner only; preferred target |
| `finalized` | `in_progress` | `reopen` | admin_owner only; alternate target |
| `archived` | (reopen later) | out of MVP unless admin charter | read-only for now |

**MVP policy:** prefer staged path; do **not** implement casual direct jump `in_progress` → `finalized`. If an admin override is ever added, it must be explicit, warned, and audited — **not** default.

Current fixture monthly id **1** is `in_progress` → Implementation smoke should walk submit → review → finalize after readiness prep.

---

## 3. Readiness Checklist

Compute readiness before allowing `finalize` (also display on monthly show / preview).

| Key | Pass condition |
|-----|----------------|
| `monthly_exists` | Row found |
| `period_exists` | Parent reporting period found |
| `title_present` | Title non-empty after trim |
| `preview_ok` | Preview service can compose without hard failure |
| `render_mode_valid` | Mode is `blocks_primary` or valid `flat_fallback` (not `empty` for finalize) |
| `has_non_archived_block` | ≥1 non-archived block |
| `required_blocks_present` | All canonical required keys present (non-archived) |
| `block_statuses_ready` | No non-archived block in `draft` / `in_progress`; required blocks ≥ `reviewed` |
| `source_weekly_resolved` | All monthly source weekly ids resolve; missing list empty |

Failed gate keys returned to UI and audit (`finalization_failed` / `readiness_checked`).

**Current fixture:** readiness **FAIL** (`executive_summary`=`in_progress`; required blocks mostly `draft`; optional `risks_and_blockers`=`draft`).

---

## 4. Canonical Required Blocks

### Required (MVP)

- `executive_summary`
- `work_completed`
- `results_summary`
- `key_findings`
- `next_month_plan`

### Optional (if present, still must not be draft/in_progress when finalizing)

- `risks_and_blockers`
- `client_notes`
- `internal_notes`
- `custom_text`
- `metric_snapshot`
- `weekly_summary`

Archived blocks ignored.

---

## 5. Parent / Child Lock Model

Parent: `monthly_report_contents`  
Children: `report_blocks` where `monthly_report_content_id = parent.id`

When parent.status = `finalized`:

| Actor / action | Allowed? |
|----------------|----------|
| Preview / print GET | Yes (internal roles) |
| Monthly show GET | Yes |
| Monthly content edit POST | No (except after reopen) |
| Block create / edit / status update | No for normal users |
| Block list / show GET | Yes (read-only notices) |
| Reopen POST | admin_owner only |

Implementation: app-level checks in services (status of parent), not DB triggers.

Existing Monthly Report Content CRUD already has partial finalized content locks; Implementation 01 must **extend** lock to blocks via parent status and centralize readiness/finalize in `ReportFinalizationService`.

---

## 6. Routes

Explicit endpoints (preferred over generic status POST for auditability):

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/monthly-reports/{id}/submit-review` | `in_progress` → `ready_for_review` |
| POST | `/monthly-reports/{id}/mark-reviewed` | `ready_for_review` → `reviewed` |
| POST | `/monthly-reports/{id}/finalize` | `reviewed` → `finalized` (+ readiness) |
| POST | `/monthly-reports/{id}/reopen` | `finalized` → `reviewed`/`in_progress` |

Rules:

- Auth required; CSRF required;
- No GET mutation;
- No DELETE;
- No public route;
- No `/pdf`, `/share`, `/export`.

Optional later: generic `POST /monthly-reports/{id}/status` — **not** MVP preferred.

Existing monthly edit form status changes may remain for non-finalization transitions, but finalize/reopen should use explicit routes.

---

## 7. Controller / Service / Repository Design

### Recommended new service

`ReportFinalizationService`

Responsibilities:

- compute readiness checklist;
- enforce transition graph for submit/review/finalize/reopen;
- set `finalized_at` on first finalize (if null);
- preserve `finalized_at` on reopen;
- write audit events;
- return structured errors with failed gate keys.

### Existing touchpoints

| Component | Change intent |
|-----------|---------------|
| `MonthlyReportContentController` | Wire transition actions + readiness display data |
| `MonthlyReportContentService` | Delegate finalize/reopen; keep CRUD; cooperate on locks |
| `MonthlyReportContentRepository` | Status/`finalized_at` updates; audit insert (reuse) |
| `ReportBlockService` | Reject mutations when parent finalized |
| `ReportPreviewService` / views | Read-only status/finalized cues |
| `routes.php` / `bootstrap.php` | Register routes + DI |
| Views: monthly show, preview, blocks index/show/edit | Status card, checklist, locked notices, buttons |
| `app.css` | Finalization / locked / readiness styles |
| README / docs index | Document routes + policy |

Avoid bloating MonthlyReportContentService with all readiness rules — isolate in `ReportFinalizationService`.

---

## 8. UI Integration

### Monthly report detail

- Finalization status card (`status`, `finalized_at`, actor from audit if available);
- Readiness checklist with pass/fail per gate;
- Action buttons by role/status:
  - Submit for review
  - Mark reviewed
  - Finalize
  - Reopen
- Disabled buttons show concrete reason (role, wrong status, failed gates).

### Preview page

- Finalization state badge;
- `finalized_at` when finalized;
- Warning when not finalized;
- Link/summary to readiness on monthly detail.

### Block list / detail / edit

- If parent finalized: locked notice;
- Hide/disable create/edit controls for non-privileged users;
- Read remains available.

---

## 9. Preview Integration

Preview remains read-only composition:

- Does not mutate DB;
- Continues to render draft/in_progress blocks before finalization;
- After finalization, same render path; show finalized metadata;
- Print twin unchanged (browser print only).

Finalize does **not** require print success; preview composition + render mode gate is enough.

---

## 10. Block Editor Integration

`ReportBlockService` (and controller guards):

- On create/update: load parent monthly; if `finalized` → reject with clear message;
- After reopen: edits allowed again under normal block status rules;
- Reopen does not auto-approve/reset blocks.

---

## 11. Access Model

| Role | Submit review | Mark reviewed | Finalize | Reopen | Edit before finalize |
|------|---------------|---------------|----------|--------|----------------------|
| `admin_owner` | Yes | Yes | Yes (gates) | **Yes** | Yes |
| `seo_lead_reviewer` | Yes | Yes | Yes (gates) | **No** (MVP) | Yes |
| `seo_specialist` | Yes | No | No | No | Yes |
| `account_client_manager` | No | No | No | No | Read-only MVP |
| `internal_viewer` | No | No | No | No | Read-only |
| `client_viewer` | No access | No | No | No | No |

Local smoke may only have `admin_owner`. Multi-role HTTP smoke **deferred** / optional hardening — document as SAFE UNKNOWN / deferred.

Admin readiness override: **out of MVP default**. If added later: warning + audit mandatory.

---

## 12. Audit Events

Recommended product event names:

| Event | When |
|-------|------|
| `monthly_report.readiness_checked` | Checklist computed (optional on show / required on finalize attempt) |
| `monthly_report.submitted_for_review` | submit-review success |
| `monthly_report.reviewed` | mark-reviewed success |
| `monthly_report.finalized` | finalize success |
| `monthly_report.reopened` | reopen success |
| `monthly_report.finalization_failed` | finalize refused (gates / role / transition) |

Payload (no secrets):

- `monthly_report_content_id`
- `reporting_period_id`
- `old_status` / `new_status`
- `readiness_result` (pass/fail)
- `failed_gate_keys` (if any)
- `actor_user_id`

**Note:** Monthly Report Content CRUD already emits some `monthly_report_content.*` events (e.g. status_changed / finalized). Implementation 01 should **prefer** the `monthly_report.*` names above for new transition endpoints, and avoid duplicate contradictory events for the same action. Mapping/alias of legacy names is an implementation detail — document in result if both appear.

Block lock refusal events: optional later; not required for MVP.

---

## 13. Data Policy

- Use existing local fixture only (`LOCAL_FIXTURE_ONLY`).
- No real client data.
- Implementation smoke may mutate:
  - monthly id **1** status / `finalized_at`;
  - report_blocks statuses under monthly id **1** only as readiness preparation via existing CRUD/service;
  - audit inserts.
- Prefer CRUD/service paths over raw SQL for prep.
- No schema changes.

Recommended Implementation 01 sequence:

1. Readiness failure smoke on current fixture (no finalize);
2. Controlled prep: advance **required** blocks to `reviewed`/`approved` (LOCAL_FIXTURE_ONLY);
3. Optional block `risks_and_blockers` also advanced or remains gated — if present, must leave draft/in_progress;
4. submit → mark-reviewed → finalize;
5. lock smoke; reopen smoke; leave **finalized** as preferred final state.

---

## 14. Error Handling

| Case | Behavior |
|------|----------|
| Wrong transition | 4xx + message; audit `finalization_failed` when finalize attempted |
| Failed readiness | Finalize blocked; list failed gates |
| Parent finalized + block edit | Reject with lock message |
| Unauthorized role | Reject; no status change |
| Missing monthly / period | 404 |
| CSRF / unauth | Existing auth/CSRF patterns |

No silent partial finalize.

---

## 15. No-public / No-PDF Policy

Finalization **must not** introduce:

- public token URLs;
- client portal routes;
- PDF generation;
- export packages;
- email delivery;
- immutable snapshot tables;
- e-signature.

Preview/print remain internal authenticated browser surfaces only.
