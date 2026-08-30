# I-SEO Report Hub — Summary Assembly Apply Implementation Result v0.1

**Status:** IMPLEMENTED (local; limited write proof)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Implementation 01  
**Verdict:** `SUMMARY ASSEMBLY APPLY PASS_WITH_LIMITED_WRITE_PROOF`

Guarded per-block apply of client-facing draft text. Finalized report id **1** cannot be written. No live UPDATE was executed because no safe non-finalized target exists.

---

## 1. What landed

| Piece | Path / detail |
|-------|----------------|
| POST route | `POST /monthly-reports/{id}/assembly-apply` |
| GET preview | still `GET /monthly-reports/{id}/assembly-preview`; POST to preview remains **405** |
| Controller | `MonthlyReportAssemblyController::apply` |
| Apply service | `app/Services/MonthlyReportSummaryApplyService.php` |
| Formatter | `MonthlyReportSummaryAssemblyService::formatBlockBody` / `buildApplyPayload` |
| Repository | `ReportBlockRepository::updateAssemblyApply` (narrow body/status/actor/review timestamps/optional `data_json`) |
| View | apply checkboxes, current vs draft, confirm, disabled finalized panel |
| Auth | internal; apply roles `admin_owner`, `seo_lead_reviewer`; CSRF required |

GET on `/assembly-apply` is **405** (POST-only).

---

## 2. Text contract

Applied body is plain UTF-8 text: intro + blank line + `- ` bullets. Source priority: `client_summary` → title + truncated description → title. No ids, categories, badges, `internal_note`, `evidence_note`, JSON, or HTML.

| Key | Intro / empty |
|-----|----------------|
| `work_completed` | `В течение месяца выполнены основные SEO-работы:` — empty list is **not** writable |
| `next_month_plan` | `В следующем периоде запланированы работы:` — empty list is **not** writable |
| `risks_and_blockers` | `На текущий момент требуют внимания:` — empty selected list writes locked phrase |

Empty risks phrase: `Существенных рисков и блокеров на текущий момент не зафиксировано.`

`summary`, title, key, sort remain unchanged.

---

## 3. Finalized report 1

UI: disabled checkboxes, disabled confirm, disabled submit, **no** working POST form. Copy:

`Отчет финализирован. Чтобы применить черновик, нужен отдельный безопасный процесс reopen/update/finalize/export.`

POST with valid session/CSRF/selection/confirm: **302** back to assembly preview + warn flash. No UPDATE.

---

## 4. Safe report discovery

Read-only probe of `iseo_report_hub_dev`:

| id | status | auto blocks | entries | exports | shares | safe |
|----|--------|-------------|---------|---------|--------|------|
| 1 | finalized | 3 | 7 | 4 | 7 | **no** |
| 5 | draft | 0 | 0 | 0 | 0 | **no** |

No other monthly reports. Write proof **not executed**. Fixture seed / reopen **not** performed.

---

## 5. DB counts (before = after)

| Count | Value |
|-------|--------|
| categories | 13 |
| items | 31 |
| entries_r1 | 7 |
| blocks_r1 | 6 |
| exports | 4 |
| shares | 7 |
| active | 1 |
| revoked | 6 |
| export 4 checksum prefix | `a8c4d61c6216e8d70b19` |
| share 7 | `active` |

Report 1 `updated_at` max on blocks unchanged: `2026-07-27 01:46:07`.

---

## 6. Remaining debt

- Safe fixture seed / one-block write proof  
- Apply UX refinement (simple vs technical toggle)  
- Metrics model for `results_summary`  
- Client PDF / template visual alignment  
- Screenshot QA of all pages when operator sends shots  
- Optional `summary` rewrite checkbox  

---

## 7. SAFE UNKNOWN

- Whether operators will charter a fixture seed immediately. Default: wait for **Summary Assembly Safe Fixture Charter 01**.  
- Live `data_json` merge on a future non-finalized apply (not exercised).
