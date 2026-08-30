# I-SEO Report Hub — Summary Assembly Technical Charter v0.1

**Status:** CHARTER FOR FUTURE IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01  
**Recommended next impl wave:** `I-SEO Report Hub — Summary Assembly Preview Implementation 01`

Source of truth: `projects/iseo-report-hub/app-source/`  
Runtime sync: **not** in this charter wave; Implementation 01 may sync an exact allowlist after code lands.

---

## 1. Goal

Option A: internal GET page that classifies `monthly_report_work_entries` into client-section drafts using Source Rules v0.1. **No INSERT/UPDATE/DELETE.** **No migration.**

---

## 2. Schema

| Change | Decision |
|--------|----------|
| New migration | **No** |
| ALTER / CHECK | **No** |
| Writes to `report_blocks` | **No** |
| Writes to work entries | **No** |
| Writes to snapshots / exports / shares | **No** |

Read:

- `MonthlyReportWorkEntryRepository::listByMonthlyReportId`
- Monthly report row (id, title, status, period_key) via existing monthly repository/service
- Optional: `ReportBlockRepository::listByMonthlyReportId` for read-only «Сейчас в отчете»

---

## 3. New files (planned)

| Piece | Path |
|-------|------|
| Service | `app/Services/MonthlyReportSummaryAssemblyService.php` |
| Controller | `app/Controllers/MonthlyReportAssemblyController.php` |
| View | `app/Views/pages/monthly-reports/assembly-preview.php` |
| Partial (optional) | `app/Views/partials/assembly-draft-block.php` |

Prefer a **dedicated GET-only controller** so POST apply cannot be accidentally added to monthly content CRUD in the same file. If Implementation 01 is extremely thin, `MonthlyReportContentController::assemblyPreview` is acceptable **only if** the method is GET, has no `guardMethod(['POST'])` sibling, and does not call block `update()`.

---

## 4. Wiring

### 4.1 `app/bootstrap.php`

`require_once` the new service and controller (same explicit style as work entries).

### 4.2 `app/routes.php`

More specific than `/monthly-reports/(\d+)$`:

```
GET /monthly-reports/{id}/assembly-preview
```

Place near other `/monthly-reports/{id}/...` GET routes (preview/blocks/work-entries).

### 4.3 Show page CTA

Edit `app/Views/partials/monthly-work-entries.php` (and only that partial plus CSS if a button class is missing): add **Собрать черновик из работ**.

Do **not** change work-entry editor forms.

### 4.4 Labels

Reuse `ui_block_label()`. Add assembly-specific strings in the view (Russian copy from UX Flow). Optional `UiLabels` keys only if the same phrases would otherwise duplicate; not required.

---

## 5. Service algorithm

Input: `int $monthlyReportId`  
Output: array (DTO-as-array is enough; no new class required).

Steps:

1. Assert DB configured + local-dev database (same as other services).  
2. Load monthly report; return `null` if missing (controller → 404).  
3. `$entries = listByMonthlyReportId($id)`.  
4. Initialize buckets and counters.  
5. For each entry, in list order (already `sort_order, id`):  
   - Classify exclusion vs exclusive block per Source Rules.  
   - Build `line_text` via client_summary → title+description → title.  
   - Never include `internal_note` / `evidence_note`.  
6. Group each auto-block’s items by category name.  
7. Optionally load existing blocks keyed by `block_key` for comparison (read-only).  
8. Return structure:

```
monthly: {id,status,title,period_key,...}
stats: {total, included, excluded_internal, excluded_cancelled, unassigned}
drafts: {
  work_completed: {key, title_ru, items: [...], groups: [...], empty: bool},
  next_month_plan: {...},
  risks_and_blockers: {...}
}
manual: {executive_summary, results_summary, key_findings}
candidates_key_findings: [...]
existing_blocks: {block_key: {summary, body, status, title}}  // optional
```

**No** persistence. **No** preview `assemble()` rewrite. Do not call `ReportSnapshotService::createForMonthly`.

---

## 6. Escaping and formatting

- View: `e()` on all entry-derived strings.  
- Multiline: `nl2br(e($text), false)` only if a field contains newlines; default one bullet = one line.  
- Do not emit raw HTML from `client_summary`.  
- Description truncation: `mb_substr` at 280; append `…` if truncated.

---

## 7. Auth / HTTP

| Rule | Detail |
|------|--------|
| Method | GET only |
| Auth | `requireInternalUser()` / same read roles as monthly show |
| CSRF | Not applicable (no POST) |
| 404 | Unknown monthly id |
| 403 | No internal role |

---

## 8. Tests / smoke (Implementation 01)

GET-only. Suggested checks:

1. PHP lint new PHP files.  
2. `/health` 200.  
3. `/monthly-reports/1/assembly-preview` 200 (session).  
4. HTML contains warning «не меняет отчет, PDF».  
5. HTML contains «Что сделали», «План на следующий месяц», «Риски и блокеры».  
6. Fixture expectation: 4 / 2 / 1 source counts if seeds unchanged.  
7. No «Сохранить» / apply form.  
8. `/monthly-reports/1` 200; CTA present.  
9. DB counts unchanged: entries_r1 **7**, blocks **6**, exports **4**, shares **7**, active **1**.  
10. Export 4 checksum prefix unchanged if re-read (`a8c4d61c6216e8d70b19`).  
11. No POST to assembly URL (if probed: 405 or 404, not 200 write).

Do **not** reopen, finalize, create share, or regenerate PDF.

---

## 9. Acceptance (Implementation 01)

- Route 200 for report 1.  
- Drafts follow Source Rules on live entries.  
- Manual blocks labeled, not auto-prose.  
- Zero DB mutation vs preflight counts.  
- Foreign WIP / production / WordPress untouched.

---

## 10. Out of scope

- Apply/overwrite  
- Migration  
- PDF/template alignment  
- Screenshot QA of all pages  
- Metrics model  
- AI-generated executive summary  

---

## 11. SAFE UNKNOWN

- Whether Implementation 01 adds a tiny CSS class or reuses `panel` only.  
- Exact HTML structure of groups (ul vs nested sections) — keep simple.
