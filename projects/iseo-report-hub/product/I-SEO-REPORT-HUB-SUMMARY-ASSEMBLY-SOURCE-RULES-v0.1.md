# I-SEO Report Hub — Summary Assembly Source Rules v0.1

**Status:** CHARTER / RULES — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01

Source table: `monthly_report_work_entries` (joined category/item names via existing repository).  
Target shells: the six `report_blocks.block_key` values. Implementation 01 **renders** these rules; it does **not** write blocks.

---

## 1. Global exclusions (all client blocks)

An entry is **never** placed in a client draft if any of:

| Rule | Field |
|------|--------|
| Cancelled | `status = cancelled` |
| Internal only | `client_visibility = internal` |
| Empty title after trim | `title` blank (should not occur; skip + count as invalid) |

Never copied into client text:

- `internal_note`
- `evidence_note`
- raw catalogue slugs
- user emails / ids

`description` may be used only as a **short fallback** after `client_summary` (see §3).

---

## 2. Exclusive assignment (one primary block)

An included entry is assigned to **at most one** generated block, in this order:

1. **risks_and_blockers** if risk rule matches  
2. **work_completed** if done rule matches  
3. **next_month_plan** if plan rule matches  
4. else **unassigned** (counted, not shown in a draft body)

`key_findings` / `results_summary` / `executive_summary` are **not** primary auto-targets in Implementation 01.

This prevents a `blocked` + leftover `period_role=done` row from appearing as completed work.

---

## 3. Text source priority (generated line)

For each included entry, the visible line is:

1. `client_summary` if non-empty after trim  
2. else `title` + truncated `description` (if description non-empty; max **280** characters, ellipsis)  
3. else `title` only  

Prefix optional category label in the grouped body (see UX / technical charter), not inside the line source itself.

---

## 4. Rules table

| Block key | RU | Included entries | Excluded (beyond global) | Text source | Fallback | Manual override | Risk |
|-----------|----|------------------|---------------------------|-------------|----------|-----------------|------|
| `work_completed` | Что сделали | `period_role = done` **and** `status = done` **and** `client_visibility IN (client_safe, client_facing)` | `in_progress` / `planned` / `blocked` / `deferred` even if role is `done`; anything already taken by risks | §3 | Category group heading + «Нет выполненных работ для клиентского раздела.» | Human edits the **block** later (Option B); preview does not write | Low (strict done) |
| `next_month_plan` | План на следующий месяц | `period_role = planned_next` **and** `status IN (planned, in_progress, deferred)` **and** visibility client_safe/facing | `status = done` (belongs to completed if role were done; here role is plan — still exclude done-plan as completed-looking); `blocked` plan rows go to **risks** first | §3 | «Нет запланированных работ для следующего периода.» | Same | Low |
| `risks_and_blockers` | Риски и блокеры | (`period_role = risk` **or** `status = blocked`) **and** `client_visibility != internal` | Internal risks; cancelled | §3 | «Клиентских рисков и блокеров в работах нет.» | Same | Medium (wording) |
| `key_findings` | Ключевые выводы | **None auto-body in Impl 01** | All auto-inclusion | — | Manual required | Specialist writes block | Low if manual |
| `results_summary` | Результаты | **None** | Do not infer KPI/traffic/positions from work titles | — | Manual required | Specialist writes block | High if faked |
| `executive_summary` | Краткое резюме | **None** in Impl 01 | No concat of other drafts | — | Manual required | Specialist writes block; later may draft from other **block** summaries after apply exists | Medium if auto-prose |

---

## 5. Decisions locked for Implementation 01

### 5.1 Internal risks

**Stay internal.** `client_visibility = internal` never enters `risks_and_blockers` (or any other client draft). Preview **stats** may count `excluded_internal` so the specialist sees they were omitted on purpose.

Do **not** auto-rewrite internal notes into “client-safe” language.

### 5.2 `key_findings`

**Manual first.** Optional preview subsection «Кандидаты в выводы» may list entries with `period_role = note` and visibility client_safe/facing — **not** as the block body, labeled as candidates only. Fixture report 1 currently has **zero** `note` rows.

### 5.3 `results_summary`

**Manual until a metrics model exists.** Work entries are activity, not outcomes. Do not turn “мониторинг выполнен” into a ranking/traffic result.

### 5.4 `executive_summary`

**Manual in Implementation 01.** Even preview-only must **not** generate a synthetic paragraph from work titles. Show the block as «заполняется вручную» and optionally show a **read-only** current `report_blocks` summary/body for comparison (SELECT existing block, no write).

A later wave may draft executive text from the other five **assembled or human** summaries — still with preview-before-apply.

---

## 6. Other statuses / roles

| Combination | Destination |
|-------------|-------------|
| `status=in_progress`, `period_role=done` | Unassigned (incomplete); not completed |
| `status=deferred`, `period_role=planned_next` | `next_month_plan` |
| `status=deferred`, `period_role=done` | Unassigned (not completed) |
| `status=blocked`, any role | `risks_and_blockers` if not internal |
| `period_role=note`, client-safe/facing | Candidate list only (`key_findings` sidebar) |
| `period_role=note`, internal | excluded_internal |
| `client_visibility=client_facing` | Same inclusion as `client_safe` for Impl 01 (both are client-usable). Facing may later sort first; not required now |

---

## 7. Expected fixture mapping (report id 1, 7 seed rows)

From `tools/seed-nikita-catalogue.php` monthly fixtures (all `client_safe`; none `internal` / `cancelled`):

| Count | Seed shape | Generated block |
|------:|------------|-----------------|
| 4 | `done` + `done` + client_safe | `work_completed` |
| 2 | `planned` + `planned_next` + client_safe | `next_month_plan` |
| 1 | `blocked` + `risk` + client_safe | `risks_and_blockers` |
| 0 | — | `key_findings` auto-body |
| 0 | — | excluded_internal / cancelled |

Acceptance for Implementation 01 preview: those three drafts non-empty; two manual blocks flagged; totals 7/7 included in one of the three (or stats: included 7, excluded 0).

If the operator edited seeds after the editor wave, counts may differ — preview must follow **live** rows, not this table. This table is the **design fixture expectation**.

---

## 8. Manual override policy (future Option B)

Preview-only does not override anything.

When apply exists:

- generated text is a **proposal**;
- existing non-empty `body`/`summary` is treated as **manual content** unless the operator ticks that block and confirms;
- empty body may be filled without treating it as a conflict (still require explicit block selection).

---

## 9. SAFE UNKNOWN

- Whether `client_facing` should later get a stronger “must show” sort than `client_safe`.  
- Whether a single entry should ever appear in **two** client sections (rejected for Impl 01).  
- Operator preference for bullet vs numbered lists (UX charter defaults to bullets grouped by category).
