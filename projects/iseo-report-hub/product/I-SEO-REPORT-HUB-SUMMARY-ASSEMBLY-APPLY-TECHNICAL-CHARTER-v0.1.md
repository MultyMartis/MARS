# I-SEO Report Hub — Summary Assembly Apply Technical Charter v0.1

**Status:** CHARTER FOR FUTURE IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01  
**Recommended next impl wave:** `I-SEO Report Hub — Summary Assembly Apply Implementation 01`

Source of truth: `projects/iseo-report-hub/app-source/`  
Runtime sync: **not** in this charter wave.

---

## 1. Goal

POST apply of **selected** auto `report_blocks` using client-facing text from Block Text Contract. Refuse finalized/archived parents. No migration. No PDF/export/share/work-entry writes.

---

## 2. Schema

| Change | Decision |
|--------|----------|
| New migration | **No** |
| ALTER / CHECK | **No** |
| New table | **No** |
| Writes | UPDATE existing `report_blocks` rows only |

Provenance may be merged into existing JSON column `data_json` **without** migration (object keys below). If current `data_json` is not a JSON object, do **not** overwrite it; skip provenance merge and still write `body`.

---

## 3. Table and columns

Table: **`report_blocks`**.

| Column | Apply Implementation 01 |
|--------|-------------------------|
| `body` | Set to generated plain text |
| `summary` | **Leave as-is** |
| `status` | Set to `in_progress` **only if** `body` actually changes |
| `updated_by` | Actor user id |
| `updated_at` | Auto `ON UPDATE CURRENT_TIMESTAMP` |
| `reviewed_at` / `approved_at` | Set **NULL** if `body` changes (review of old text is stale) |
| `data_json` | Optional merge: `assembly_applied_at`, `assembly_source_entry_ids`, `assembly_previous_body_sha256` |
| `title`, `block_key`, `block_type`, `sort_order`, owner/reviewer, weekly source ids | **Unchanged** |

There is no `updated_by_user_id` column; the column is **`updated_by`**.

Do **not** INSERT missing shells. Do **not** UPDATE `monthly_report_contents` flat text columns.

---

## 4. Status and readiness

Changing client prose invalidates `reviewed` / `approved`.

After a real body change: `status = in_progress`. Finalize gates will then fail until a human reviews the five required keys again. That is intended.

If generated body equals current body (newline-normalized): **skip** that row (no status change, no `updated_at` bump required).

Archived block: skip / refuse that key.

---

## 5. Files (planned)

| Piece | Path |
|-------|------|
| Format helper | extend `MonthlyReportSummaryAssemblyService` with `formatApplyBody(string $blockKey, array $draft): string` (and empty-risk phrase) |
| Apply service | `app/Services/MonthlyReportSummaryApplyService.php` |
| Controller action | `MonthlyReportAssemblyController::apply` |
| Route | `POST /monthly-reports/{id}/assembly-apply` next to existing GET preview |
| View | update `assembly-preview.php` + CSS in `public/assets/css/app.css` |
| Repository | add `ReportBlockRepository::updateAssemblyApply(int $id, array $data)` **or** a narrow UPDATE in the apply service via existing `update()` while preserving unchanged fields |

Prefer a **narrow** UPDATE (body, status, updated_by, reviewed_at, approved_at, optional data_json) so apply cannot accidentally retitle or reorder.

Do **not** route apply through the HTML block edit form.

---

## 6. Apply service algorithm

Input: monthly id, actor user, POST `block_keys[]`, `confirm_overwrite`, CSRF already validated by controller.

1. `assertLocalDevDatabase()`.
2. Load monthly row; 404 if missing.
3. If status `finalized` or `archived` → refuse (no writes).
4. If actor lacks `admin_owner` / `seo_lead_reviewer` → 403.
5. If confirm not `1` → refuse.
6. Normalize selected keys; allowlist `{work_completed, next_month_plan, risks_and_blockers}` only; unique.
7. If none selected → refuse.
8. Build preview/classify payload (reuse `MonthlyReportSummaryAssemblyService::preview`).
9. Load existing blocks keyed by `block_key`.
10. For each selected key, decide skip vs write (empty completed/plan; missing row; archived; identical body; risks empty-state phrase).
11. If zero writes remain → refuse or success-with-skips (no DB write). Prefer **no UPDATE** if nothing to write.
12. Transaction: for each write, capture old values, UPDATE, `insertAudit`.
13. Commit. Return `{ok, updated: [...], skipped: [...]}`.

Audit event type: `report_block.assembly_applied` plus existing `report_block.updated` / `report_block.status_changed` if those helpers stay consistent. Metadata: `monthly_report_content_id`, `block_key`, `from_status`, `to_status`, `old_body_sha256`, `new_body_sha256`, `old_body_len`, `new_body_len`, `source_entry_ids`. No passwords. Avoid putting full body in `audit_log` if longer than ~500 characters; evidence files hold full text.

---

## 7. Controller / HTTP

| Rule | Detail |
|------|--------|
| GET preview | Unchanged success path; adds disabled or live form |
| POST apply | `guard` POST-only; CSRF; auth |
| Success | Redirect `/monthly-reports/{id}` + flash |
| Failure | Redirect back to preview + flash |
| POST to preview URL | Keep **405** (preview stays GET-only) |

Register POST **before** the generic `/monthly-reports/{id}` route, beside the GET preview matcher.

---

## 8. Idempotence

Applying the same draft twice:

- first apply writes body + status `in_progress`;
- second apply sees identical body → skip all selected keys → no content change.

`updated_at` should not move on skip.

---

## 9. Backup (implementation wave only)

**Mandatory** `mysqldump` of `iseo_report_hub_dev` **before the first POST apply smoke**. Also dump `report_blocks` for the target monthly id.

This charter wave: **no dump required** (no writes).

If dump fails in Implementation 01 → **STOP** before POST.

---

## 10. Out of scope

- Reopen / finalize
- INSERT new `report_blocks`
- Dual-write flat monthly columns
- PDF / snapshot / export / share
- Migration
- Specialist apply role expansion

---

## 11. SAFE UNKNOWN

- Whether `data_json` on fixture blocks is already a non-object (probe at implementation time; skip merge if unsafe).  
- Exact audit event string if a later naming convention prefers `monthly_report.assembly_applied` on the parent entity instead of per-block.
