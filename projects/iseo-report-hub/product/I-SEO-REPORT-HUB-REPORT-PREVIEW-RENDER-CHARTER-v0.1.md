# I-SEO Report Hub — Report Preview / Render Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-BLOCKS-CRUD-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый internal preview / render слой** monthly report после:

- DB-backed auth;
- Reporting Period CRUD;
- Weekly Checkpoints CRUD;
- Monthly Report Content CRUD (DB-05 flat fields);
- Report Blocks migration (DB-06) + Report Blocks CRUD.

Цель charter:

1. Описать, как собрать **один** internal report view из period context + monthly row + ordered blocks.
2. Зафиксировать canonical render order, inclusion/exclusion, DB-05 fallback.
3. Спроектировать routes / controller / service / views для следующей implementation wave.
4. Определить safe text rendering, auth/access, diagnostics, optional print-friendly route.
5. Подготовить validation/smoke gates (read-only preview; DB unchanged).
6. Явно исключить public share, PDF/export, client portal, Markdown/rich text, immutable snapshots.
7. Не менять app-source / runtime / DB в этой волне.

Эта волна — **documentation / policy only**. Preview **не** кодируется здесь.

---

## 2. Current Baseline

### Report Blocks CRUD implementation

| Item | Value |
|------|-------|
| Primary commit | `135da2137cef401e16225b8f1e653dfbe3e18699` — `feat(iseo-report-hub): add report blocks crud` |
| Hash-record | `5c65ac8817e94ad146c7aee80d876b2290e65ef5` — `docs(iseo-report-hub): record report blocks crud commit hash` |
| Push | **no** |
| Smoke | **42/42 PASS** (per implementation closeout) |

### Upstream baselines (unchanged authority)

| Layer | Primary / hash-record |
|-------|------------------------|
| Auth | `d4b3b2e2…` / `0cd2cfb7…` |
| Reporting Period CRUD | `392258fc…` / `f1d8a17e…` |
| Weekly Checkpoints CRUD | `911db07d…` / `64c42cbe…` |
| Monthly Report Content CRUD | `65f64124…` / `17553a55…` (+ clarify `eb00b3f4…`) |
| DB-06 Report Blocks migration | `1b71a021…` / `7393d7c1…` (+ clarify `86338d66…`) |

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
| report_blocks | **6** |

### Parent monthly report content

| Field | Value |
|-------|-------|
| Id | **1** |
| Parent period | id **1** / `2026-07` / draft |
| Status | `in_progress` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` (W1–W4) |
| Flat DB-05 fields | still contain `LOCAL_FIXTURE_ONLY` |
| created_by / updated_by | **1** / **1** |

### Current report blocks (ordered)

| id | block_key | status | sort_order |
|----|-----------|--------|------------|
| 1 | `executive_summary` | `in_progress` | 15 |
| 2 | `work_completed` | `draft` | 20 |
| 3 | `results_summary` | `draft` | 30 |
| 9 | `risks_and_blockers` | `draft` | 35 |
| 4 | `key_findings` | `draft` | 40 |
| 5 | `next_month_plan` | `draft` | 50 |

All retain `LOCAL_FIXTURE_ONLY` markers / sources as applicable. No archived blocks in current fixture set.

### Current limitation

- **No** assembled monthly report preview;
- **No** preview route / controller / service / view;
- **No** documented canonical render composition beyond block `sort_order` in list UI;
- **No** DB-05 → DB-06 fallback policy in runtime;
- **No** print view; **no** PDF/export; **no** public share; **no** client portal.

---

## 3. Problem

Система умеет хранить и редактировать:

- reporting period context;
- weekly checkpoints;
- monthly report content (DB-05 flat fields);
- report blocks (DB-06 rows + CRUD).

Но **нет** read-only слоя, который собирает **итоговый internal monthly report** для оператора: один экран с period header, source weekly links, ordered blocks, status labels, safe body text, и diagnostics (включая legacy flat fields). Без preview нельзя проверить «как будет выглядеть отчёт» до publish/export waves.

---

## 4. Scope

### In scope (this charter + next implementation wave design)

- Internal monthly report preview (authenticated, read-only);
- Composition from period + monthly row + report_blocks;
- Canonical block order (`sort_order` ASC, then `id` ASC);
- Archived block exclusion (default);
- Empty-block empty-state rules;
- DB-05 flat field fallback / diagnostics behavior;
- Source weekly checkpoint references;
- Optional print-friendly internal route design;
- Validation / smoke plan for next implementation wave;
- Docs-only deliverables in this wave.

### Out of scope

- Public / client-facing report;
- Share tokens / public URLs;
- PDF generation / email / export packages;
- Client portal;
- Metric charts / Topvisor imports / screenshots;
- Markdown parser / rich text / raw HTML;
- Immutable published snapshots;
- Approval/finalization workflow changes;
- Drag/drop;
- Production deployment;
- Any app-source / runtime / DB mutation in **this** charter wave.

---

## 5. Product Rules

1. Preview is **internal-only**; always show an **Internal only** label.
2. Preview is **read-only** — no mutations, no CSRF write surface on preview routes.
3. Auth required; same read access model as monthly report detail (internal roles); `client_viewer` **denied** in MVP unless a later charter explicitly opens it.
4. **DB-06 blocks preferred** when any non-archived blocks exist for the monthly report.
5. **DB-05 flat fields** are fallback if zero non-archived blocks; otherwise appear only in an **internal diagnostics / legacy** section.
6. Canonical block order: `sort_order ASC`, then `id ASC`.
7. Archived blocks **excluded by default**; no MVP debug-include flag required.
8. Include draft / in_progress / reviewed / approved (and other non-archived statuses) in internal preview; show status labels.
9. Safe text: escape HTML; preserve newlines; **no** raw HTML, Markdown, or external assets/CDN.
10. No public token, share link, PDF route, or client portal in MVP preview.
11. Optional `/preview/print` uses the same data + print-friendly CSS; browser print only.
12. Missing parent/context fails safely (404 / friendly error); missing source checkpoints are surfaced as warnings without inventing data.
13. Preview must leave DB counts and row content unchanged.

---

## 6. Render Data Sources

| Source | Role in preview |
|--------|-----------------|
| `reporting_periods` (+ client/project/site joins) | Header context: period key, dates, status, org labels |
| `monthly_report_contents` | Title, monthly status, source weekly ids, DB-05 flat fields |
| `report_blocks` | Primary body sections (non-archived), ordered |
| `weekly_checkpoints` | Source summary links / compact labels for W1–W4 |
| Auth session | Gate + identity; no secrets in HTML |

Composition is a **read model** assembled by a preview service (future implementation). Not a new DB table. Not a snapshot.

---

## 7. Safety Boundary

| Boundary | Rule |
|----------|------|
| This wave writes | Active Brain docs only (allowlisted paths) |
| App-source | **No** edits |
| Runtime | **No** edits / sync |
| DB | **No** mutation; optional read-only verify only |
| Secrets | Never print passwords/hashes/env secrets |
| Foreign WIP | Preserve; do not stage/clean |
| Git | Exact-path docs commit; **no** push |
| Real client data | Forbidden; fixture/`LOCAL_FIXTURE_ONLY` only |

---

## 8. Validation Gates

For the **next** implementation wave (documented here; not executed in this charter):

- Unauth `/monthly-reports/1/preview` → login redirect;
- Auth preview **200** with title, period `2026-07`, status `in_progress`, 6 blocks, ordered keys including `executive_summary` and `risks_and_blockers`, source W1–W4 links, Internal only label;
- Render order matches `sort_order`/`id`;
- DB unchanged before/after;
- Regression on monthly/blocks/weekly/periods/health/login/404;
- Optional print route **200** if implemented;
- No public/PDF routes introduced.

Full matrix: [VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Operators confuse preview with published client report | Strong Internal only label; no public URLs |
| Dual content (blocks vs flat) misread as client output | Blocks primary; flat fields diagnostics-only when blocks exist |
| Missing weekly sources | Warn / mark broken refs; do not invent checkpoints |
| Empty blocks look broken | Explicit empty-state note under title |
| Scope creep into PDF/share | Hard out-of-scope + smoke “no export/public” |
| Accidental DB writes | Preview service SELECT-only; validation counts before/after |

---

## 10. Next Implementation Wave

**`I-SEO Report Hub — Report Preview / Render Implementation 01`**

Deliver (future wave only):

- `ReportPreviewController` + `ReportPreviewService` (+ optional composition repository);
- `GET /monthly-reports/{id}/preview` (required);
- optional `GET /monthly-reports/{id}/preview/print`;
- views under `pages/report-preview/`;
- Preview link on monthly report detail;
- Model A source → runtime allowlist sync;
- Smoke per validation plan;
- Result docs + OPERATIONAL-INDEX update.

**Not** in next wave: schema, PDF, public share, client portal, Markdown, Topvisor, snapshots.

See [IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-PLAN-v0.1.md).
