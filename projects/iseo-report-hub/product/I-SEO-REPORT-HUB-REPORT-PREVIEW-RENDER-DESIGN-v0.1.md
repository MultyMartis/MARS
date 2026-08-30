# I-SEO Report Hub — Report Preview / Render Design v0.1

**Status:** DESIGN ONLY — no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md)

---

## 1. Routes

| Method | Path | Auth | CSRF | Action |
|--------|------|------|------|--------|
| GET | `/monthly-reports/{id}/preview` | Required (internal read roles) | — | Assemble and render internal preview |
| GET | `/monthly-reports/{id}/preview/print` | Required (same as preview) | — | Optional print-friendly view (same data) |

**Routing notes:**

- Register `/preview` and `/preview/print` **before** the bare `/monthly-reports/{id}` matcher (same exact-path / preg_match discipline as blocks CRUD).
- No POST on preview routes.
- No public token query params.
- No `/export`, `/pdf`, `/share` routes in MVP.

---

## 2. Controller / service / repository

### Controller

`app-source/app/Controllers/ReportPreviewController.php`

Recommended methods:

- `show(int $monthlyReportId)` — HTML preview
- `print(int $monthlyReportId)` — optional print view

Responsibilities:

- Auth gate (authenticated + internal read role);
- Call `ReportPreviewService` for composition;
- Render view or safe 404 / error page;
- Never mutate DB; never echo secrets / stack traces.

### Service

`app-source/app/Services/ReportPreviewService.php`

Responsibilities:

- Load monthly report by id;
- Load parent reporting period + client/project/site context;
- Load non-archived blocks ordered by `sort_order`, `id`;
- Resolve source weekly checkpoints for monthly `source_weekly_checkpoint_ids` (and optionally per-block sources);
- Decide primary render mode: **blocks** vs **flat-fallback**;
- Build diagnostics payload (counts, fallback presence, missing source ids, render mode);
- Apply access capability check (read);
- **No** INSERT/UPDATE/DELETE.

### Repository

Prefer reuse:

- `MonthlyReportContentRepository`
- `ReportBlockRepository` (list by monthly id; filter archived in service or repo helper)
- Existing period / weekly / org loaders already used by CRUD

Optional:

- `ReportPreviewRepository` — only if a single composition query is cleaner than multi-repo assembly.

Wire in `routes.php` + `bootstrap.php` following Monthly Report / Report Block patterns.

---

## 3. Views

| View path | Purpose |
|-----------|---------|
| `app/Views/pages/report-preview/show.php` | Internal assembled preview |
| `app/Views/pages/report-preview/print.php` | Optional print-friendly twin |

Reuse:

- `layout.php`, `partials/header.php` (print may use a minimal layout without nav chrome);
- Extend `public/assets/css/app.css` with preview + print classes;
- **No** CDN / external assets.

---

## 4. Monthly report integration

On `app/Views/pages/monthly-reports/show.php`:

- Add **Preview** link/button → `/monthly-reports/{id}/preview`;
- Place near existing title/actions / report blocks section;
- Do not remove existing CRUD links.

Optional dashboard/nav: not required for MVP if monthly detail entry is enough.

---

## 5. Reporting period integration (optional)

On reporting period detail monthly section:

- Optional secondary **Preview** link when a monthly report exists for the period;
- Not required for Implementation 01 if monthly show already links.

---

## 6. Render order

Canonical order for blocks in preview:

1. `sort_order` **ASC**
2. `id` **ASC**

Expected smoke order for monthly id **1** (current fixture):

1. `executive_summary` (15 / id 1)
2. `work_completed` (20 / id 2)
3. `results_summary` (30 / id 3)
4. `risks_and_blockers` (35 / id 9)
5. `key_findings` (40 / id 4)
6. `next_month_plan` (50 / id 5)

---

## 7. Block inclusion / exclusion

| Status / condition | In MVP preview? |
|--------------------|-----------------|
| `draft` | Yes (with status label) |
| `in_progress` | Yes |
| `ready_for_review` / `reviewed` / `approved` (and other non-archived allowlisted statuses) | Yes |
| `archived` | **No** (excluded by default) |
| Debug “include archived” flag | **Not** in MVP |

Empty blocks:

- If title present and body/summary empty → show title + empty-state note;
- If body present → render escaped body with newline preservation;
- Summary: render separately only if product chooses; default MVP — show summary under title when non-empty, before or after body as a labeled sub-section;
- `data_json` / `source_metric_refs` → collapsed / diagnostics-like section only; do not dominate main reading flow.

---

## 8. DB-05 fallback behavior

| Situation | Preview behavior |
|-----------|------------------|
| ≥1 non-archived block | **Blocks primary**; DB-05 flat fields in **diagnostics / legacy** collapsible only |
| 0 non-archived blocks, flat fields non-empty | **Flat fallback** as main body (map known flat keys to labeled sections) |
| 0 non-archived blocks and empty flat content | Safe empty report state / validation warning (see error handling) |

MVP preference: blocks primary; flat fields diagnostics-only when blocks exist.

---

## 9. Weekly source links

- Resolve monthly `source_weekly_checkpoint_ids` to checkpoint rows in the same reporting period;
- Show compact source summary (W1–W4 labels + status + link to weekly detail);
- Missing ids → warn in diagnostics / source section; do not invent rows;
- Per-block `source_weekly_checkpoint_ids` may show as secondary chips under each block when present.

---

## 10. Metric refs placeholder

- If `source_metric_refs` or block `data_json` present: show JSON in a collapsed “debug / metric refs” panel;
- No charts, no Topvisor fetch, no metric table rendering in MVP.

---

## 11. Internal diagnostics

Recommended diagnostics block (internal only):

- Non-archived block count;
- Whether flat fallback is active;
- Presence of non-empty DB-05 flat fields;
- Missing source weekly ids (if any);
- Render mode: `blocks` | `flat_fallback` | `empty`;
- Generated-at local timestamp;
- Optional: archived block count excluded (if cheap to compute).

---

## 12. Safe text rendering

| Rule | MVP |
|------|-----|
| HTML escape | Default for all text fields |
| Newlines | `<br>` or paragraph split after escape |
| Raw HTML | Forbidden |
| Markdown | Forbidden |
| Rich text | Forbidden |
| External assets / CDN | Forbidden |

---

## 13. Print route

If implemented:

- Same composition as `/preview`;
- Body/layout class for print (hide nav/actions; widen content);
- Browser **Print** only;
- No server-side PDF;
- No external print CSS frameworks.

---

## 14. Auth / access

| Role | Preview read (MVP) |
|------|--------------------|
| `admin_owner` | Yes |
| `seo_lead_reviewer` | Yes |
| `seo_specialist` | Yes |
| `account_client_manager` | Yes |
| `internal_viewer` | Yes |
| `client_viewer` | **No** (unless later charter) |
| Unauthenticated | Redirect `/login` |

Align with monthly report **read** internal-role gate (`requireInternalUser` pattern).

---

## 15. Error handling

| Condition | Behavior |
|-----------|----------|
| Monthly id missing / not found | 404 safe page |
| Parent reporting period missing | 404 / error; do not render orphan preview |
| Project/client context missing | Fail safely with friendly message |
| No blocks and no flat fallback content | Empty-state page with warning; still 200 **or** documented soft-fail — prefer **200** with explicit empty diagnostics for operator UX |
| Source weekly ids missing | Preview still renders; mark broken refs |
| Auth fail | Redirect login / deny |
| Any write attempted | Not applicable — no write endpoints |

Preview **must not** mutate DB on any path.

---

## 16. No-public / no-PDF policy

- No public token URLs;
- No share links;
- No client portal routes;
- No PDF generation endpoints;
- No email delivery;
- Preview pages must carry **Internal only** labeling;
- Future publish/snapshot waves remain separate charters.
