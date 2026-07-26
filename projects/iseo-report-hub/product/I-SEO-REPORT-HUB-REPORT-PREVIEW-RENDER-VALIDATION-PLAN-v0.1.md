# I-SEO Report Hub — Report Preview / Render Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — execute in implementation wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md)

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
| weekly_checkpoints | **4** (W1–W4) |
| monthly_report_contents | **1** (id **1**, period `2026-07`, status `in_progress`) |
| report_blocks | **6** under monthly id **1** |
| Baseline commits | Report Blocks CRUD primary `135da213…` / hash-record `5c65ac88…` |
| Auth | Local admin can authenticate (password never printed) |

STOP if DB target wrong or Report Blocks CRUD baseline missing.

Capture DB counts **before** smoke.

---

## 2. Route smoke

| Step | Request | Expect |
|------|---------|--------|
| Preview exists | GET `/monthly-reports/1/preview` (auth) | **200** |
| Optional print | GET `/monthly-reports/1/preview/print` (auth) | **200** if implemented; else document skipped |
| Missing monthly | GET `/monthly-reports/999999/preview` | Safe 404 / not-found |
| No PDF route | GET `/monthly-reports/1/pdf` (or similar) | **404** / absent |
| No share route | GET `/share/...` | Absent |
| Preview before bare show | Router registration order | `/preview` not captured by `{id}` only |

---

## 3. Auth smoke

| Step | Expect |
|------|--------|
| Unauth GET `/monthly-reports/1/preview` | Redirect `/login` |
| Auth internal role (admin_owner smoke) | **200** |
| `client_viewer` (if testable later) | Denied / no access in MVP |
| Session injection / password-form | Follow existing project smoke pattern; never print secrets |

---

## 4. Preview content smoke

Auth GET `/monthly-reports/1/preview` must show:

| Element | Expected |
|---------|----------|
| Report title | Contains demo title / `LOCAL_FIXTURE_ONLY` |
| Period | `2026-07` |
| Monthly status | `in_progress` |
| Internal only label | Present |
| Block count | **6** non-archived |
| Blocks present | `executive_summary`, `work_completed`, `results_summary`, `risks_and_blockers`, `key_findings`, `next_month_plan` |
| Status labels | At least `executive_summary` shows `in_progress` |
| Generated-at | Local timestamp present (diagnostics or header) |
| Client/project/site context | Present when joins available |

---

## 5. Render order validation

| Check | Expect |
|-------|--------|
| Order rule | `sort_order ASC`, then `id ASC` |
| Observed order | 15→20→30→35→40→50 (`executive_summary` … `next_month_plan` with `risks_and_blockers` between `results_summary` and `key_findings`) |
| List vs preview | Same order as blocks list UI |

---

## 6. Fallback validation

| Case | Expect |
|------|--------|
| Current fixture (6 blocks) | Render mode **blocks**; flat fields only in diagnostics/legacy if shown |
| Documented empty-blocks case | If no non-archived blocks (future/safe test without permanent mutation): flat fallback used when flat content exists |
| Empty blocks + empty flat | Explicit empty / warning state |
| Live archive mutation | **Not required** for MVP smoke if operator forbids; design rule still documented |

Do **not** mutate rows solely for fallback smoke unless a separate rollback-safe charter allows temporary change.

---

## 7. Source weekly link validation

| Check | Expect |
|-------|--------|
| Monthly sources `[1,2,3,7]` | Links/labels for W1–W4 present |
| Links resolve | Point to existing weekly checkpoint detail routes |
| Missing id warning | If a source id is absent, diagnostics/source section warns (do not invent) |

---

## 8. Internal diagnostics validation

| Check | Expect |
|-------|--------|
| Block count | Matches non-archived count (**6**) |
| Render mode | `blocks` for current fixture |
| Flat field presence | Indicated in diagnostics when flat text exists |
| Metric refs / data_json | Collapsed/debug only if present; not primary body |
| No secrets | No password/hash/env dumps |

---

## 9. DB unchanged validation

Before and after preview smoke:

| Metric | Expected unchanged |
|--------|--------------------|
| migrations | **5** |
| tables | **13** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| users / roles | **1** / **6** |

Spot-check monthly id **1** status/title and block statuses/sort_orders unchanged.

---

## 10. Regression smoke

| Area | Expect |
|------|--------|
| Monthly report detail | Still **200**; Preview link present after implementation |
| Report blocks list/detail/edit | Intact |
| Weekly checkpoints | Intact |
| Reporting periods | Intact |
| Health | Intact |
| Login / logout | Intact |
| Unknown route | Safe 404 |

---

## 11. No-public / no-export validation

| Check | Expect |
|-------|--------|
| Public token URL | Absent |
| PDF endpoint | Absent |
| Share UI | Absent |
| Client portal | Absent |
| Preview labeling | Internal only |

---

## 12. Data policy

- Fixture / `LOCAL_FIXTURE_ONLY` only;
- No real client data;
- No credentials in HTML or reports;
- No `.env` printing.

---

## 13. STOP conditions

STOP validation / implementation if:

- DB host/name mismatch;
- Preview mutates any row;
- Public/PDF/share surfaces appear;
- Auth gate missing on preview;
- Foreign WIP would be staged;
- Counts drift without authorized mutation charter;
- HTML renders unescaped user/content fields (XSS risk).

Output token example:

`STOP — I-SEO REPORT PREVIEW RENDER VALIDATION SAFETY CONDITION FAILED`
