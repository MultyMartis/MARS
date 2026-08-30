# I-SEO Report Hub — Summary Assembly Current Block Baseline v0.1

**Status:** CHARTER / BASELINE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01  
**Depends on:** DB-06 `report_blocks`; Report Preview / Finalization / Snapshot / Export implementations; Work Entry model (DB-11)

This wave does **not** implement assembly. No app-source, runtime, DB, share, or PDF mutation.

---

## 1. Naming

Operator charter language sometimes says `monthly_report_blocks`. The **actual table** is:

| Informal name | Canonical entity |
|---------------|------------------|
| monthly report blocks / client blocks | `report_blocks` |
| monthly report row | `monthly_report_contents` |
| specialist work log | `monthly_report_work_entries` |

Do **not** invent a second blocks table. Assembly later writes (Option B) target `report_blocks` rows keyed by `block_key` under `monthly_report_content_id`.

---

## 2. Dual content path (current MVP)

Client-facing six sections exist in **two** places:

| Layer | Storage | Role today |
|-------|---------|------------|
| Flat columns | `monthly_report_contents.executive_summary` … `next_month_plan` (+ `client_notes`, `internal_notes`) | Legacy free-text; still edited on monthly report form; shown on `/monthly-reports/{id}` as «Содержимое» |
| Block rows | `report_blocks` (one row per `block_key` per monthly report) | **Primary** preview/snapshot/export source when any non-archived block exists |

`ReportPreviewService::assemble()`:

- if non-archived blocks exist → `render_mode = blocks_primary`;
- else if any flat field is non-empty → `flat_fallback`;
- else → `empty` (not finalizable).

Local report id **1** uses `blocks_primary` (6 rows). Flat columns remain for compatibility and must **not** be auto-overwritten by Implementation 01.

---

## 3. `report_blocks` fields

From DB-06 / `ReportBlockRepository`:

| Column | Purpose for assembly |
|--------|----------------------|
| `id` | Stable row id; copied into snapshot `source_block_ids` |
| `monthly_report_content_id` | Parent monthly report |
| `block_key` | Machine key; unique per parent (`uniq_report_blocks_parent_key`) |
| `block_type` | Usually equals key for the six shells; CHECK includes extra types (`client_notes`, `custom_text`, …) |
| `sort_order` | Preview/PDF outline order |
| `status` | `draft` / `in_progress` / `ready_for_review` / `reviewed` / `approved` / `archived` |
| `title` | Human heading (often fixture English + `LOCAL_FIXTURE_ONLY`) |
| `summary` | Short text |
| `body` | Main client text |
| `data_json` | Optional JSON object/array; unused by work-entry assembly today |
| `source_weekly_checkpoint_ids` | JSON list of weekly ids |
| `source_metric_refs` | JSON; unused for work-entry assembly |
| owner / reviewer / audit timestamps | Workflow only |

**No** column today means “assembled draft vs human final”. `summary` + `body` are the only text surfaces. `data_json` can later hold provenance (`assembled_from_entry_ids`, `assembled_at`) **without** a migration.

---

## 4. The six client-facing keys

UI labels (`UiLabels::BLOCK_KEYS`):

| `block_key` | RU | Required for finalize? |
|-------------|----|-------------------------|
| `executive_summary` | Краткое резюме | **Yes** |
| `work_completed` | Что сделали | **Yes** |
| `results_summary` | Результаты | **Yes** |
| `key_findings` | Ключевые выводы | **Yes** |
| `next_month_plan` | План на следующий месяц | **Yes** |
| `risks_and_blockers` | Риски и блокеры | **No** (present locally as 6th fixture row) |

`ReportFinalizationService::REQUIRED_BLOCK_KEYS` = the five **Yes** rows. `risks_and_blockers` may be absent and still finalize. Do **not** change this set in assembly Implementation 01.

---

## 5. Lifecycle and locks

### 5.1 Block CRUD

`ReportBlockService::canMutateAgainstParent()`: parent status `finalized` or `archived` → **no** create/edit, including `admin_owner`. Controller redirects with “Reopen before editing blocks.”

Specialist may edit blocks only while status is `draft` / `in_progress` / `ready_for_review` **and** parent is not finalized.

Approved block content: only `admin_owner` / `seo_lead_reviewer`.

### 5.2 Monthly report finalize

`finalize` requires readiness gates, including:

- preview assemble OK;
- render mode `blocks_primary` or `flat_fallback`;
- required five keys present (non-archived);
- those five in `reviewed` or `approved`;
- no active `draft` / `in_progress` blocks;
- weekly source ids resolve.

Finalize does **not** copy work entries into blocks. It only locks the monthly row (`status=finalized`, `finalized_at` set once).

### 5.3 Work entries vs finalized

Work entry editor **remains allowed** on a finalized report, with a UI warning that PDF/snapshots do not auto-rebuild. That is a product split: specialist log can move; client shells stay frozen until reopen + explicit block edit / future apply.

### 5.4 Reopen

`admin_owner` only: `finalized` → `reviewed`; `finalized_at` preserved. After reopen, block CRUD is allowed again. Existing snapshot/export/share rows are **not** deleted or regenerated.

---

## 6. Preview, snapshot, export, PDF

| Consumer | Reads | Auto-updates if blocks change? |
|----------|-------|--------------------------------|
| `/monthly-reports/{id}/preview` | Live `assemble()` | Yes (live read) |
| Print preview | Same | Yes |
| `report_snapshots` | Payload frozen at create time from `assemble()` | **No** |
| `report_exports` HTML/PDF | Snapshot / export artifact | **No** |
| Public share token | Existing export file | **No** |

Checksum of export id **4** is independent of live `report_blocks` until a **new** export wave. Implementation 01 must not create snapshots or exports.

---

## 7. Protection of existing manual text

| Mechanism | Protects? |
|-----------|-----------|
| Finalized parent lock | Yes — blocks cannot be written without reopen |
| No assembly writer today | Yes — nothing overwrites shells from entries |
| Snapshot immutability | Yes — published client PDF stays as exported |
| Flat columns vs blocks | Partial — two texts can diverge; preview prefers blocks |
| `data_json` provenance | **Not used** |
| Backup-before-overwrite | **Not implemented** |

There is **no** “manual lock” or “do not overwrite” flag on a block. Option B must add **process** protection (select + confirm + backup), not a schema flag, for the first apply wave.

---

## 8. Answers required by this charter

### If we auto-update blocks after finalized, what breaks?

1. `ReportBlockService` / controller would **reject** writes until reopen — a naive writer is a failed POST, not a silent update.  
2. If reopen + overwrite succeeded: live preview would show new text; **active snapshot, export 4, share `test-first-link` would still show old PDF**. Operators would think the client report changed when it did not.  
3. Required-block statuses (`reviewed`/`approved`) would become stale vs new body unless also reset — readiness/re-finalize confusion.  
4. Audit would show `report_block.updated` without a matching new snapshot.

### Do snapshot / export / PDF update automatically?

**No.** Confirmed in current services. Preview is live; publication chain is explicit.

### Do current blocks have enough fields for assembled draft vs manual final?

**Enough for Option A (preview-only):** generated text lives only in the HTTP response.  
**Enough for a cautious Option B MVP:** write generated markdown/plain text into `body` (and optional short `summary`); stash provenance in `data_json`.  
**Not enough for a first-class draft/final split:** no `draft_body`, no `manual_override`, no version table. That is Option C / later apply charter.

### Is schema enough for MVP assembly without migration?

**Yes** for Implementation 01 (preview-only, SELECT work entries + existing blocks for side-by-side display).  
**Yes** for a later apply that overwrites `body`/`summary` with operator consent.  
**No new table or CHECK change** is required to start.

---

## 9. Local fixture (report id 1) — context only

Documented after Work Entry UI / Editor waves (not re-probed in this charter unless needed):

- `report_blocks` for monthly id 1: **6**
- `monthly_report_work_entries` for id 1: **7**
- monthly status: **finalized**
- exports **4** / shares **7** (active **1**, likely id 7 / `test-first-link`)
- PDF unchanged by work-entry waves

---

## 10. SAFE UNKNOWN

- Exact current `body`/`summary` strings of the six fixture blocks (not required to design preview-only assembly).  
- Whether operators will later want assembly to update **flat** columns in lockstep with blocks (default: **no**, blocks remain SoT for client render).  
- Whether `risks_and_blockers` will join `REQUIRED_BLOCK_KEYS` (unchanged in this wave).
