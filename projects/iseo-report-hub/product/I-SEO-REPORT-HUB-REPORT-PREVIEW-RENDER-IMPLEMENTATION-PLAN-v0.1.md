# I-SEO Report Hub — Report Preview / Render Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Preview / Render Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Report Preview / Render Implementation 01`**

Purpose: implement the first **internal, authenticated, read-only** monthly report preview/render layer on local MVP (Model A source → runtime), composing period context + monthly report content + ordered non-archived `report_blocks`, without schema changes, DB mutations, PDF/export, public share, or client portal.

Baseline dependency:

- Report Blocks CRUD Implementation 01 — primary `135da2137cef401e16225b8f1e653dfbe3e18699`, hash-record `5c65ac8817e94ad146c7aee80d876b2290e65ef5`;
- Current local fixture: monthly id **1** / period `2026-07` / report_blocks **6**.

---

## 2. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/app/routes.php` | Register `/monthly-reports/{id}/preview` (+ optional `/preview/print`) before bare `{id}` |
| `app-source/app/bootstrap.php` | Require new classes if needed |
| `app-source/app/Controllers/ReportPreviewController.php` | New controller |
| `app-source/app/Services/ReportPreviewService.php` | Composition + access + diagnostics (SELECT-only) |
| `app-source/app/Repositories/ReportPreviewRepository.php` | Optional composition queries |
| `app-source/app/Views/pages/report-preview/show.php` | Preview view |
| `app-source/app/Views/pages/report-preview/print.php` | Optional print view |
| `app-source/app/Views/pages/monthly-reports/show.php` | Add Preview link |
| `app-source/app/Views/pages/reporting-periods/show.php` | Optional Preview link |
| `app-source/app/Views/partials/header.php` | Only if needed |
| `app-source/app/Controllers/DashboardController.php` | Card/link only if needed |
| `app-source/app/Views/pages/dashboard.php` | Only if needed |
| `app-source/public/assets/css/app.css` (or existing css) | Preview / print styles |
| `app-source/README.md` | Routes note |
| `product/` result doc(s) | Implementation result |
| `reports/` closeout | Implementation REPORT |
| `OPERATIONAL-INDEX.md` | Status update |

Reuse (read-only from preview wave perspective):

- `MonthlyReportContentRepository` / `ReportBlockRepository` / period & weekly repositories as needed.

**Not allowed without separate charter:**

- New migrations / SQL schema edits;
- Mutations to `report_blocks`, `monthly_report_contents`, `weekly_checkpoints`, `reporting_periods`;
- Auth core rewrite / password/hash changes;
- PDF/export / share tokens / client portal;
- Markdown / rich text / CDN assets;
- Topvisor / metric charts / n8n;
- Fixture tool rewrite;
- `.env` / `.env.local` edits;
- Real client data import;
- DELETE routes;
- Drag/drop.

---

## 3. DB actions next wave

| Allowed | Not allowed |
|---------|-------------|
| **SELECT** only for composition / smoke verification | INSERT / UPDATE / DELETE on any product table |
| Read-only count checks before/after | Schema CREATE/ALTER/DROP |
| | New migration files |
| | TRUNCATE / DROP |
| | User/role/password mutations |
| | Any non-local / production DB |

**DB actions next wave: none (mutation).** Read-only only.

Target: `iseo_report_hub_dev` @ `127.0.0.1` only.

---

## 4. Runtime sync policy

- Model A: after source changes, allowlist sync **source → runtime** for touched app files only.
- Runtime root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- No wipe; no unrelated runtime edits; no Composer/npm; no tools/migrations sync.
- `.env.local` untouched.

---

## 5. Smoke list (summary)

Full matrix in [VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-VALIDATION-PLAN-v0.1.md).

Minimum:

1. Unauth GET `/monthly-reports/1/preview` → redirect `/login`.
2. Auth GET `/monthly-reports/1/preview` → **200**.
3. Content: title; period `2026-07`; monthly status `in_progress`; block count **6**; order by sort_order/id; includes `executive_summary` + `risks_and_blockers`; source W1–W4 links; Internal only label.
4. Optional `/preview/print` → **200** if implemented.
5. DB counts unchanged before/after.
6. Regression: monthly detail; blocks list/detail/edit; weekly; periods; health; login; 404.
7. No public/PDF routes.

Archived exclusion: document as design-validated; live archive mutation **not** required for smoke if operator forbids archive mutation (current fixture has zero archived blocks).

---

## 6. Commit policy

- Exact-path `git add` for allowlisted implementation + docs paths only;
- Never `git add .` / `-A` / `commit -a`;
- Preserve foreign WIP;
- Commit and push are **separate** waves; push only if operator charter says so;
- Default: implementation result + closeout docs after code smoke.

Suggested primary message (implementation wave):

`feat(iseo-report-hub): add report preview render`

(Exact message subject to operator implementation charter.)

---

## 7. STOP conditions

STOP implementation wave if:

- Repo root / volume / branch unsafe;
- Staged index non-empty unexpectedly;
- DB target ≠ `iseo_report_hub_dev` @ `127.0.0.1`;
- Report Blocks CRUD baseline missing;
- Scope expands into PDF/public/share/schema;
- Preview path would require DB writes;
- Foreign WIP would need remediation;
- Exact-path stage cannot be guaranteed.

Output token example:

`STOP — I-SEO REPORT PREVIEW RENDER IMPLEMENTATION SAFETY CONDITION FAILED`
