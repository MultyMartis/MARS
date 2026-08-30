# I-SEO Report Hub — Specialist Report Content Workflow Charter v0.1

**Status:** CHARTER / PRODUCT+TECHNICAL DECISION — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-26  
**Wave:** Specialist Report Content Workflow Charter 01  
**Code/DB/host mutation in this wave:** none

---

## 1. Purpose

Define how an SEO specialist works with **client-facing report text** after work entries are filled, without exposing the raw report-block editor (`block_key`, `data_json`, `source_metric_refs`).

This charter is the decision basis for:

`I-SEO Report Hub — Specialist Report Content Workflow Implementation 01`

---

## 2. Current content flow audit (source + DB)

### 2.1 What feeds client preview

| Layer | Path / type | Role |
|-------|-------------|------|
| Route | `GET /monthly-reports/{id}/preview` | Specialist-allowed preview |
| Controller | `ReportPreviewController` | Auth + assemble |
| Service | `ReportPreviewService::assemble()` | SELECT-only composition |
| Document DTO | `ClientReportDocument::fromAssemble()` | Client document sections |
| Primary content | `report_blocks` (`body` / `summary`) when non-archived blocks exist → `render_mode = blocks_primary` |
| Fallback | Flat columns on `monthly_report_contents` → `flat_fallback` |
| Optional overlay | Local demo show-ready for report id **1** only (not 7/8) | Preview-only; no DB write |

Client preview section order (`ClientReportDocument::SECTION_ORDER`):

1. `executive_summary` — Краткое резюме  
2. `results_summary` — Результаты  
3. `work_completed` — Что сделали  
4. `key_findings` — Ключевые выводы  
5. `risks_and_blockers` — Риски и блокеры  
6. `next_month_plan` — План на следующий месяц  

`client_notes` / `internal_notes` exist as flat fields (and optional block keys) but are **not** currently rendered in `ClientReportDocument`.

### 2.2 Where monthly content lives

| Store | Table | Keys / fields |
|-------|-------|----------------|
| Flat monthly row | `monthly_report_contents` | `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `risks_and_blockers`, `next_month_plan`, `client_notes`, `internal_notes` + lifecycle columns |
| Structured blocks | `report_blocks` | `block_key`, `block_type`, `title`, `body`, `summary`, `data_json`, `source_metric_refs`, … |
| Work log | `monthly_report_work_entries` | FK `monthly_report_id`; catalogue + narrative fields |

Services/controllers/views (read-only inventory):

- `MonthlyReportContentController` / `MonthlyReportContentService` / `Views/pages/monthly-reports/show.php` (+ edit forms for privileged roles)
- `ReportBlockController` / `ReportBlockService` / `Views/pages/report-blocks/form.php`
- `MonthlyReportWorkEntryController` / `MonthlyReportWorkEntryService` / work-entry form
- `MonthlyReportAssemblyController` / `MonthlyReportSummaryAssemblyService` / `MonthlyReportSummaryApplyService` / `assembly-preview.php`

### 2.3 Work entries → report sections

`MonthlyReportSummaryAssemblyService` classifies entries into:

| Kind | Keys | Behavior |
|------|------|----------|
| Auto / writable | `work_completed`, `next_month_plan`, `risks_and_blockers` | Draft text from work entries; apply may write `report_blocks.body` |
| Manual-only | `executive_summary`, `results_summary`, `key_findings` | Not auto-applied; human text |
| Candidates | `key_findings` hints | Preview-only candidates |

Apply (`POST /monthly-reports/{id}/assembly-apply`):

- Roles: `admin_owner`, `seo_lead_reviewer` only  
- Writes: `report_blocks.body` for selected auto keys  
- Refuses: finalized / archived / active share  
- Does **not** mutate work entries, snapshots, exports, shares, PDF

### 2.4 Role access today (specialist)

| Capability | `seo_specialist` today |
|------------|------------------------|
| List/view periods & monthly detail | yes |
| Work entries create/edit (non-finalized) | yes |
| Client preview / print | yes |
| Raw block create/edit (`/report-blocks/{id}/edit`) | **denied** (`ReportBlockService::SPECIALIST_EDIT_ROLES = []`) |
| Monthly metadata / flat content edit via monthly canEdit | **denied** (`MonthlyReportContentService::SPECIALIST_EDIT_ROLES = []`) |
| Assembly preview CTA on show | **hidden** in `isSpecialistFlow` |
| Assembly apply | **no** (`APPLY_ROLES` privileged only) |
| Finalize / reopen / snapshot / PDF / share | **no** (admin zone / parked) |

`AuthService::isSpecialistFlow()` = has `seo_specialist` and **not** privileged editor.

### 2.5 Demo DB reality (local `iseo_report_hub_dev`, read-only 2026-08-26)

| Object | State |
|--------|-------|
| Monthly **7** | `finalized` — July — 6 blocks — 12 work entries — flat texts filled |
| Monthly **8** | `in_progress` — August — 6 blocks — 11 work entries — flat texts filled |
| Snapshots / exports / shares | `0 / 0 / 0` |
| Canonical block keys on 7 & 8 | `executive_summary`, `results_summary`, `work_completed`, `key_findings`, `risks_and_blockers`, `next_month_plan` |

Because blocks exist, preview for 7/8 is **`blocks_primary`**. Editing only flat columns would **not** change client preview until blocks are empty.

---

## 3. Role boundary decision

### 3.1 `seo_specialist` **may**

- View reporting periods and monthly detail  
- Create/edit work entries on **in-progress** (and non-finalized) reports  
- Open client draft preview  
- Open **Specialist Content Workflow** page for in-progress reports  
- Edit **allowed client-facing section texts** via friendly UI  
- Optionally trigger **section-scoped assembly suggestions** (review/apply-to-draft for auto sections only, if Implementation 01 includes it)  
- Never see raw `block_key` / `data_json` / `source_metric_refs` inputs  

### 3.2 `seo_specialist` **must not**

- Create reporting periods  
- Edit monthly metadata / status transitions (submit-review / mark-reviewed / finalize / reopen)  
- Open raw report-block form  
- Generate PDF / export / share / snapshot  
- Access admin diagnostics  

### 3.3 `admin_owner` / `seo_lead_reviewer` **may**

- Everything specialist can, plus:  
- Raw block editor  
- Assembly apply (existing)  
- Full monthly edit / finalization / reopen  
- Broader repair of technical fields when needed  

---

## 4. Options compared

### Option A — Work entries only

Specialist fills work entries; manager/reviewer owns all report text.

| Pros | Cons |
|------|------|
| Minimal new UI | Specialist cannot finish client-facing narrative |
| Lowest risk | Bottleneck on lead; weak demo for specialist ownership |

### Option B — Specialist-friendly text editor only

New `/monthly-reports/{id}/content-workflow` with section cards; no assembly UX.

| Pros | Cons |
|------|------|
| Clear UX; no technical fields | Duplicates assembly value for auto sections |
| Fits blocks_primary write path | Specialist may rewrite “Что сделали” from scratch |

### Option C — Assembly preview/apply refinement only

Expose/refine assembly for specialist; limited free-text editing.

| Pros | Cons |
|------|------|
| Reuses existing classify/format | Manual sections still need an editor |
| Good for auto bullets | Current apply is lead-only; UX still operator-shaped |

### Option D — Hybrid MVP (**recommended**)

1. Specialist keeps filling work entries.  
2. Content workflow page shows section cards + **assembly draft hints** for auto keys.  
3. Specialist edits/saves **allowed** section texts in friendly UI (writes safe block text fields).  
4. Lead/admin retain raw editor + finalize.  

| Pros | Cons |
|------|------|
| Matches product question and existing dual model | Slightly larger Implementation 01 than B alone |
| No migration required for MVP | Must keep flat + block text in sync (see §6) |
| Preserves denied raw editor | Must not invent metrics |

---

## 5. Recommended MVP UX

### 5.1 Entry path

1. Specialist opens August: `/monthly-reports/8`  
2. Primary actions (Russian labels):

| Label | Target |
|-------|--------|
| **Добавить работу** | existing create work entry |
| **Посмотреть черновик для клиента** | existing preview |
| **Тексты отчета** | **new** content workflow |

July (`/monthly-reports/7`): **Тексты отчета** opens read-only (or 403 with branded deny) — finalized lock.

### 5.2 Route

**Canonical MVP route:**

`GET|POST /monthly-reports/{id}/content-workflow`

Alternatives considered and rejected for MVP naming: `content-edit`, `editorial` (less clear in RU product language).

Visibility:

- Authenticated internal roles that can list monthly reports  
- Specialist: in-progress (and draft / ready_for_review if present) — editable; finalized — read-only or deny mutation  
- Privileged: editable per existing parent locks  

### 5.3 Page layout (Russian)

**Заголовок:** `Тексты отчета`  
**Подзаголовок:** client / period / status summary  

Blocks:

1. **Статус периода** — status badge; work-entry count; short hint  
2. **Работы за месяц** — compact summary + link to `#work-entries` / create  
3. **Разделы отчета** — cards in client preview order  

Per section card:

- Russian heading (via `UiLabels`)  
- Current client text (from block `body`, fallback summary)  
- For auto keys: collapsed **Черновик из работ** (assembly format text, SELECT-only) + button **Подставить черновик в поле** (client-side or POST-less fill into textarea; save is separate)  
- Textarea for allowed editable sections  
- **Сохранить раздел** (MVP: per-section save preferred for safer partial writes)  

Footer:

- **Посмотреть черновик для клиента**  
- **К отчету** → monthly show  

### 5.4 Explicit non-goals on this page

- No `block_key` / `block_type` / `sort_order` controls  
- No JSON editors  
- No PDF / share / snapshot actions  
- No finalize  

---

## 6. Section policy

| Section key | RU label | Specialist edit (in-progress) | From work entries | Reviewer/admin override | Client preview | MVP |
|-------------|----------|-------------------------------|-------------------|-------------------------|----------------|-----|
| `executive_summary` | Краткое резюме | yes | no (manual) | yes | yes | yes |
| `results_summary` | Результаты | yes (caution: no fake metrics) | no | yes | yes | yes |
| `work_completed` | Что сделали | yes (review/edit) | yes (assembly) | yes | yes | yes |
| `key_findings` | Ключевые выводы | yes | candidates only | yes | yes | yes |
| `risks_and_blockers` | Риски и блокеры | yes | yes (assembly) | yes | yes | yes |
| `next_month_plan` | План на следующий месяц | yes | yes (assembly) | yes | yes | yes |
| `client_notes` | Заметки для клиента | optional flat-only | no | yes | **not in ClientReportDocument today** | defer UI or flat-only later |
| `internal_notes` | Внутренние заметки | optional internal | no | yes | **no** | defer from specialist MVP page |

---

## 7. Data / write model decision

### Recommended: Approach 2+ (friendly writes to `report_blocks` + mirror flat columns)

**Why not Approach 1 alone (flat only):**  
August/July already have blocks → preview is `blocks_primary`. Flat-only saves would not update client preview.

**Why not Approach 3 (new draft table):**  
Unnecessary migration for MVP; dual storage already exists.

**MVP write contract per allowed section:**

1. Resolve existing `report_blocks` row by `(monthly_report_content_id, block_key)`.  
2. UPDATE only safe fields: `body` (required), optionally `summary`/`title` if product keeps them in sync — **do not** change `block_key`, `data_json`, `source_metric_refs`, ownership JSON ids unless privileged path.  
3. Mirror the same body text into the matching `monthly_report_contents` column so detail “Тексты разделов” stays consistent.  
4. Refuse writes when parent status is `finalized` / `archived` (specialist); privileged rules follow existing reopen policy.  

**Migration:** not required for MVP.  
**Backup:** required before first implementation write wave (mysqldump of `iseo_report_hub_dev` or at least `monthly_report_contents` + `report_blocks`).  
**Implementation shape:** code-only (controllers/services/views/routes) after backup.

---

## 8. Status / locking policy

| Parent status | Work entries | Content workflow | Preview | Finalize |
|---------------|--------------|------------------|---------|----------|
| `in_progress` / `draft` / `ready_for_review` | specialist mutate yes | specialist edit yes | yes | privileged only |
| `finalized` | specialist read-only | read-only or mutation denied | yes | reopen = admin |
| `archived` | locked | locked | as existing | — |

Privileged editors may edit broader content and use raw block form subject to existing locks (`locksForBlock`, finalized parent rules).

---

## 9. Implementation sequence

1. **Backup** local DB tables used by content.  
2. Add route + controller action + specialist-friendly view.  
3. Wire auth: list OK; mutate only allowed roles + non-finalized for specialist.  
4. Section load from blocks (fallback flat).  
5. Per-section save → block body + flat mirror.  
6. Optional: assembly hint panel for auto keys (reuse `MonthlyReportSummaryAssemblyService::preview` / `formatBlockBody`).  
7. Show page CTA **Тексты отчета**.  
8. Keep `/report-blocks/{id}/edit` denied for specialist.  
9. Local validation on monthly **8** + read-only **7** + screenshots.  
10. No PDF/export/share/host.

---

## 10. Acceptance criteria (for Implementation 01)

See companion plan doc. Summary:

- Specialist sees **Тексты отчета** on August detail.  
- Opens friendly workflow; **no** technical JSON/key fields.  
- Can save at least one allowed section on August; preview reflects it.  
- July finalized remains non-mutable for specialist.  
- Raw block edit remains denied.  
- Backup before mutation; no host; no PDF/export/share rows.

---

## 11. Risks / deferred

- PDF / export / share parked  
- Production config normalization paused  
- Work-entry help density optional Polish 02  
- Full reviewer approval UX beyond existing status actions  
- AI-generated summaries **out of scope** unless separately chartered  
- Real metrics integrity policy before real clients  
- Demo content may contain invented metrics — local/demo only  
- `client_notes` not in client document yet — do not promise preview visibility in MVP  
- Dual write (block + flat) must stay transactional or clearly ordered to avoid drift  

---

## 12. Decision record

| Decision | Choice |
|----------|--------|
| MVP option | **D — Hybrid** |
| Write model | **report_blocks safe text + flat mirror** |
| Next wave | **Specialist Report Content Workflow Implementation 01** |
| Separate Data Audit wave | **Not required** (schema/roles/preview path verified) |
