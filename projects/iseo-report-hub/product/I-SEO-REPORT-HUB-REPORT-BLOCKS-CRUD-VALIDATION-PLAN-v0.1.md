# I-SEO Report Hub — Report Blocks CRUD Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — execute in implementation wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight

Before implementation smoke:

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged index | Empty (or only intentional allowlist mid-wave) |
| DB name / host | `iseo_report_hub_dev` / `127.0.0.1` |
| Migrations / tables | **5** / **13** |
| users / roles | **1** / **6** |
| clients / projects / sites / reporting_periods | **1** / **1** / **1** / **2** |
| weekly_checkpoints | **4** (W1/W2/W3/W4) |
| monthly_report_contents | **1** (id **1**, period `2026-07`, status `in_progress`) |
| report_blocks before create smoke | **5** under monthly id **1** |
| Fixture keys / sort | `executive_summary`…`next_month_plan` at 10/20/30/40/50; all `draft` |
| Auth | Local admin can authenticate (password never printed) |
| Migration file present | `2026_07_26_000005_create_report_blocks_table.sql` |

STOP if DB-06 baseline missing or DB target wrong.

---

## 2. Route smoke

| Step | Request | Expect |
|------|---------|--------|
| Unauth block list | GET `/monthly-reports/1/blocks` | Redirect `/login` |
| Auth block list | GET `/monthly-reports/1/blocks` | **200**; 5 fixture blocks sorted 10–50 |
| Auth create form | GET `/monthly-reports/1/blocks/create` | **200** when capability allows |
| Auth detail | GET `/report-blocks/{id}` for `executive_summary` | **200**; parent monthly/period context; source links |
| Auth edit form | GET `/report-blocks/{id}/edit` | **200** when capability allows |
| Missing id | GET `/report-blocks/999999` | **404** or safe not-found |
| No DELETE | Any DELETE method / UI | Absent |
| No drag/drop controls | Block list/edit | Absent |

---

## 3. Form / CSRF smoke

| Step | Expect |
|------|--------|
| Create/edit forms include `_csrf` | Present |
| POST create/update without CSRF / bad token | Rejected; no mutation |
| POST update with valid CSRF | Accepted when payload valid |
| Validation errors re-render form | Safe messages; old input preserved where practical |
| No stack traces / SQL errors in HTML | Confirmed |

---

## 4. DB create / edit / status smoke

| Step | Expect |
|------|--------|
| Edit existing `executive_summary` title/body | Updated; markers remain `LOCAL_FIXTURE_ONLY` |
| POST status → `in_progress` | Persisted; `updated_by` set |
| Create additional `risks_and_blockers` | Inserted under monthly id **1**; `LOCAL_FIXTURE_ONLY`; status default `draft` (or documented) |
| Manual `sort_order` update | Persisted; list order reflects change |
| Optional archive of additional block | Via status only if exercised; document |
| Counts | monthly_report_contents **1**; reporting_periods **2**; weekly_checkpoints **4** unchanged; report_blocks **5** or **6** depending create |
| Prefer not mutate weekly / period / monthly rows | Intact |
| Document final block statuses / count | In implementation result |

---

## 5. Uniqueness / validation errors

| Case | Expect |
|------|--------|
| Duplicate `block_key` under monthly id **1** | Refused; friendly error; count unchanged |
| Invalid status / illegal transition | Refused |
| Invalid `block_type` | Refused |
| Non-existent parent monthly | Refused / 404 |
| Create/edit while parent monthly finalized/archived as non-privileged | Refused |
| Edit content while `approved` as non-privileged | Refused / field locked |
| `block_key` empty / invalid slug / >64 | Refused |
| Title empty or >255 | Refused |
| Body/summary over soft length cap | Refused |
| `sort_order` negative / non-integer | Refused |

---

## 6. Source weekly checkpoint validation

| Case | Expect |
|------|--------|
| Valid sources from period `2026-07` (ids resolved from W1–W4 keys) | Accepted |
| Empty sources | Allowed with warning / “no sources” marker |
| Non-existent checkpoint id | Refused |
| Checkpoint id from another period | Refused |
| Invalid JSON / non-array payload | Refused |
| Detail page source links | Show selected set with links to weekly detail |

---

## 7. JSON validation

| Case | Expect |
|------|--------|
| Valid `data_json` object/array | Accepted |
| Valid `source_metric_refs` object/array | Accepted |
| Invalid JSON text | Refused (friendly); no MySQL errno in HTML |
| Oversized JSON | Refused per safe-size policy |
| Metric FK validation | **Not required** (metric tables absent) |

---

## 8. Access-role smoke

Practical MVP (one local admin):

| Step | Expect |
|------|--------|
| Admin (`admin_owner`) | Full create/edit/status/archive/reopen/reorder path PASS |
| Unauthenticated | All block routes denied/redirect |
| `client_viewer` | N/A until such user exists — document as deferred |
| Specialist denial of reviewed/approved/archive | If only admin user exists: **policy covered / not multi-user smoked** |

Do **not** create extra users/passwords in CRUD wave unless a separate bootstrap charter authorizes it.

---

## 9. Audit smoke

If audit implemented:

| Event | When |
|-------|------|
| `report_block.created` | After create `risks_and_blockers` (or other create) |
| `report_block.updated` | After title/field edit |
| `report_block.status_changed` | After status change |
| `report_block.reviewed` / `.approved` / `.archived` | Only if those statuses are entered in smoke |
| `report_block.reordered` | If sort_order change emits reorder event |

No secrets in audit payload. If audit deferred, document as SAFE SIMPLIFICATION in implementation result.

---

## 10. Regression smoke

| Check | Expect |
|-------|--------|
| GET `/reporting-periods` (auth) | **200**; `2026-07` / `2026-08` still listed |
| GET `/reporting-periods/1` | **200**; monthly report section intact |
| GET `/reporting-periods/1/weekly-checkpoints` | **200**; W1–W4 still listed |
| GET `/weekly-checkpoints/7` | **200**; W4 still `skipped` (or documented) |
| GET `/monthly-reports/1` | **200**; includes report blocks section |
| GET `/monthly-reports/1/edit` | **200** |
| GET `/login` | **200** |
| GET `/health` | **200** (no secrets) |
| GET `/not-existing` | **404** |
| Auth services / password bootstrap | Untouched |
| Fixture client/project/site | Counts **1/1/1** unchanged |
| monthly_report_contents / weekly_checkpoints / reporting_periods | Counts **1** / **4** / **2** unchanged |

---

## 11. Data policy

| Rule | Expect |
|------|--------|
| Smoke markers | `LOCAL_FIXTURE_ONLY` retained on fixture/smoke blocks |
| Real client data | None |
| Schema | Unchanged |
| reporting_periods rows | Unchanged by block CRUD |
| weekly_checkpoints rows | Unchanged by block CRUD |
| monthly_report_contents rows | Unchanged by block CRUD |
| Duplicate `block_key` under monthly id **1** | Never persists |
| Credentials | Never printed / committed |
| Drag/drop / DELETE | Absent |

---

## 12. STOP conditions

STOP implementation smoke / commit if:

- Preflight fails (root/volume/branch/DB target)
- DB-06 baseline destroyed unexpectedly
- DELETE route/UI introduced
- Drag/drop UI / sortable CDN introduced
- PDF / portal / Topvisor creep in
- Real client data would be written
- Schema/migration mutated
- monthly_report_contents / weekly_checkpoints / reporting_periods mutated unexpectedly
- Non-allowlist paths staged
- Push without charter

Token:

`STOP — I-SEO REPORT BLOCKS CRUD VALIDATION SAFETY CONDITION FAILED`

---

## 13. Recommended smoke sequence (next wave)

1. Monthly report id **1** block list shows 5 fixture blocks sorted 10–50
2. Detail shows `executive_summary`
3. Edit existing `executive_summary` title/body/status to `in_progress`
4. Create additional `risks_and_blockers` block with `LOCAL_FIXTURE_ONLY`
5. Duplicate `block_key` refused safely
6. Invalid `source_weekly_checkpoint_ids` refused safely
7. Invalid JSON refused safely
8. Manual `sort_order` update works
9. Source weekly checkpoint links shown
10. Monthly report detail shows report blocks section
11. Confirm no DELETE route/UI and no drag/drop
12. Regression: reporting periods / weekly checkpoints / monthly reports / login / health / 404
