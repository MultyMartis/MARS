# I-SEO Report Hub — Report Finalization Validation Plan v0.1

**Status:** PLANNING ONLY — for next implementation wave; this charter wave does not run finalize smoke  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Finalization Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight

Before Implementation 01 mutations:

| Check | Expect |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged index | empty (unless charter expects staged) |
| i-SEO scoped WIP | only allowlisted implementation files |
| Foreign WIP | preserved |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Baseline counts | migrations **5**; tables **13**; monthly **1**; blocks **6**; weekly **4**; periods **2** |
| Monthly id 1 | status `in_progress`; `finalized_at` null; `LOCAL_FIXTURE_ONLY` |
| Preview | `/monthly-reports/1/preview` and `/preview/print` auth 200 |

---

## 2. Readiness Failure Smoke

On **current fixture** (no block prep yet):

1. Open monthly id **1** show — readiness checklist visible;
2. Attempt `POST .../finalize` (or UI Finalize) while status still not `reviewed` / blocks not ready;
3. Expect **failure**:
   - `executive_summary` = `in_progress` fails block status gate;
   - required blocks in `draft` fail;
   - present optional `risks_and_blockers` = `draft` fails if gate applies to all non-archived;
4. Status remains unchanged;
5. Audit may record `monthly_report.finalization_failed` and/or `monthly_report.readiness_checked` with failed gate keys;
6. No lock applied.

---

## 3. Readiness Success Smoke

Preparation (LOCAL_FIXTURE_ONLY only):

1. Via existing Report Blocks CRUD/service, advance **required** blocks to at least `reviewed` (or `approved` if used):
   - `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `next_month_plan`
2. Advance present optional `risks_and_blockers` out of `draft`/`in_progress` (same rule), **or** archive it if product allows ignore — preferred: set to `reviewed` to keep fixture representative;
3. Recompute readiness → **PASS**;
4. Do not finalize yet until status path walked.

---

## 4. Status Transition Smoke

Starting from monthly id **1** `in_progress` (after readiness PASS):

| Step | Action | Expect |
|------|--------|--------|
| 1 | `POST /monthly-reports/1/submit-review` | status `ready_for_review`; audit submitted |
| 2 | `POST /monthly-reports/1/mark-reviewed` | status `reviewed`; audit reviewed |
| 3 | `POST /monthly-reports/1/finalize` | status `finalized`; `finalized_at` set; audit finalized |

Reject wrong-order transitions (e.g. finalize from `in_progress`) with clear error.

---

## 5. Finalized Lock Smoke

While status = `finalized`:

| Action | Expect |
|--------|--------|
| Monthly content edit POST | Blocked for normal flow |
| Block create POST | Blocked |
| Block edit/update POST | Blocked |
| Monthly show / blocks list/show GET | 200 + locked notices |
| Period show link to report | Still works |

---

## 6. Reopen Smoke

| Step | Expect |
|------|--------|
| `POST /monthly-reports/1/reopen` as `admin_owner` | status → `reviewed` (preferred) or `in_progress` |
| `finalized_at` | **preserved** (historical) |
| Audit | `monthly_report.reopened` |
| Block statuses | Unchanged by reopen |
| Monthly/block edits | Allowed again under normal rules |
| Non-admin reopen | Denied (if multi-role available; else document deferred) |

After reopen validation, **re-finalize** (or finalize again after returning to `reviewed`) so preferred end state is **`finalized`**.

---

## 7. Audit Validation

Confirm events present with payload fields (ids, old/new status, readiness, failed gates, actor):

- `monthly_report.readiness_checked` (at least on finalize attempt)
- `monthly_report.submitted_for_review`
- `monthly_report.reviewed`
- `monthly_report.finalized`
- `monthly_report.reopened`
- `monthly_report.finalization_failed` (from failure smoke)

No secrets in payloads.

If legacy `monthly_report_content.*` events also appear, document mapping in implementation result — do not leave unexplained duplicates for the same button action.

---

## 8. Role / Access Smoke

| Role | Expect (MVP) |
|------|----------------|
| `admin_owner` | All transitions + reopen |
| `seo_lead_reviewer` | mark-reviewed + finalize; **no** reopen |
| `seo_specialist` | submit-review only among transition actions |
| `account_client_manager` / `internal_viewer` | read-only |
| `client_viewer` | no access |

Local fixture may only have `admin_owner` — multi-role HTTP smoke **optional/deferred**; if skipped, record SAFE UNKNOWN / deferred in closeout.

---

## 9. Preview Read-After-Finalize Smoke

| Check | Expect |
|-------|--------|
| `GET /monthly-reports/1/preview` | auth 200 |
| `GET /monthly-reports/1/preview/print` | auth 200 |
| Render mode | still valid (`blocks_primary` preferred) |
| UI | shows finalized state / `finalized_at` |
| DB mutation by GET preview | **none** |

---

## 10. DB Mutation Boundaries

Allowed:

- monthly id **1** status / `finalized_at`;
- report_blocks statuses for monthly **1** prep;
- audit inserts.

Forbidden:

- schema changes;
- other monthly/period/weekly/client rows;
- user/password/hash changes;
- non-local DB hosts;
- real client content.

Capture before/after counts; business row counts for periods/weekly/monthly/blocks should remain **2/4/1/6** unless a charter explicitly adds a block (prefer **not** adding blocks in finalization wave).

---

## 11. Regression Smoke

| Area | Expect |
|------|--------|
| Reporting periods list/show | OK |
| Weekly checkpoints list/show | OK |
| Monthly show + Preview links | OK |
| Report blocks list/show (when not locked / after reopen) | OK |
| Health | OK |
| Unauth → login redirect | OK |
| 404 unknown ids | OK |

---

## 12. No-public / No-export Validation

Confirm absence of:

- `/pdf`, `/share`, `/export`, public token routes;
- client portal approval UI;
- snapshot table creation.

Print route remains browser-print only.

---

## 13. Data Policy

- `LOCAL_FIXTURE_ONLY` markers retained in titles/content where present;
- No production data;
- Preferred final state after full smoke: monthly id **1** = **`finalized`** (lock baseline for next export/snapshot phase).

---

## 14. STOP Conditions

STOP Implementation 01 if:

- preflight fails;
- finalize succeeds while readiness should fail;
- locks not enforced after finalize;
- reopen available to non-admin without charter change;
- schema migration introduced;
- public/PDF/export added;
- DB host/name wrong;
- real client data introduced;
- broad git ops / unexpected staged foreign paths.

Token:

`STOP — I-SEO REPORT HUB REPORT FINALIZATION VALIDATION SAFETY CONDITION FAILED`
