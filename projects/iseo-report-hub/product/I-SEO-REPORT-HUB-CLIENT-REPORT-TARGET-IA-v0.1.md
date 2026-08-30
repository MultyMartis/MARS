# I-SEO Report Hub — Client Report Target IA v0.1

**Status:** CHARTER / TARGET IA — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01  
**Related:** [I-SEO-REPORT-HUB-TARGET-REPORT-INFORMATION-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-TARGET-REPORT-INFORMATION-ARCHITECTURE-v0.1.md) (workspace vs client layers)

This document is the **client-facing monthly report outline**. It does not add KPI/metrics models.

---

## 1. Principle

Клиентский отчёт — **документ**, не админка и не таблица блоков.

Three layers stay separate:

1. Internal manager/admin screens.  
2. Internal assembly/apply preview.  
3. Client-facing report (this IA) — preview / future export HTML / PDF / share delivery.

Content still comes from the six `report_blocks` shells. IA changes **order, visibility, and empty-state behaviour**, not the data model.

---

## 2. Target section order

Render in this order regardless of current `sort_order` / snapshot outline (today: work → results → risks → findings → plan). Do **not** mutate stored `sort_order` in Implementation 01.

| # | Section | `block_key` | Source of truth | Invent metrics? |
|---|---------|-------------|-----------------|-----------------|
| 0 | Cover / header | — | monthly + period + client/project/site | No |
| 1 | Краткое резюме | `executive_summary` | Manual block body (summary if body empty) | No |
| 2 | Результаты | `results_summary` | Manual block only | **No** |
| 3 | Что сделали | `work_completed` | Applied/polished or manual body | No |
| 4 | Ключевые выводы | `key_findings` | Manual block | No |
| 5 | Риски и блокеры | `risks_and_blockers` | Applied/polished or manual; client-safe wording only | No |
| 6 | План на следующий месяц | `next_month_plan` | Applied/polished or manual | No |
| 7 | Footer | — | Brand + local/demo label in local env | No |

Optional specialist/manager line on the cover is allowed if a **non-technical display name** exists. Do not show user ids, emails unless already a public contact convention (today: omit email).

---

## 3. Cover / header

Show:

- i-SEO wordmark / brand line (text MVP; no binary logo required);
- document type: «SEO-отчёт» / «Ежемесячный отчёт»;
- client name, project name, site URL (or label);
- period as human date range + month label (not only `2026-07` code);
- report status as a **calm** badge: «Итоговый отчёт» if finalized, «Черновик» if not;
- report date: `finalized_at` when present, else generated/preview date;
- local env only: small «Локальная демо-среда» (not `LOCAL_FIXTURE_ONLY`).

Hide on cover:

- monthly id, snapshot id/key/checksum, export id, share id;
- `render_mode`, template id/version in the header body;
- weekly checkpoint keys;
- «Internal report export» wording.

---

## 4. Section rules

### 4.1 Executive summary

Human-written narrative. One lead paragraph preferred. No fake KPI row above it.

### 4.2 Results

Qualitative results **only if present** in `results_summary`.  
Until a metrics model exists: **no** invented traffic/position/lead numbers, **no** empty KPI cards, **no** Topvisor widgets.

If empty: see §5 (preview shows a calm gap; client export/PDF later may omit).

### 4.3 Work completed

Polished body from assembly apply or manual edit. Intro + bullets as in the block text contract. No work-entry ids, catalogue codes, or internal notes.

### 4.4 Key findings

Manual. Same body-or-summary rule. No debug JSON.

### 4.5 Risks and blockers

Client-safe risks only. Visual language: **calm attention**, not panic (see visual direction).  
If applied empty-state copy exists («Существенных рисков… не зафиксировано.»), show that as a normal paragraph, not a red alert.

### 4.6 Next month plan

Plan bullets. No sprint/ticket ids.

---

## 5. Empty states

| Context | Empty required section | Empty optional (`risks_and_blockers`) |
|---------|------------------------|----------------------------------------|
| **Internal client preview** (Impl 01) | Show the heading + calm note: «Раздел будет заполнен специалистом.» Manual keys may add: «Требуется ручная редактура.» | Show heading + «Существенных рисков и блокеров на текущий момент не зафиксировано.» if no body; do not use danger styling |
| **Future client export/PDF** | Prefer omit fully empty sections **or** the same calm note — choose omit for a cleaner PDF if the block has no body and no summary | Omit if empty; do not keep a red empty card |
| **Never** | Fake lorem, fake KPI, placeholder charts | Panic empty-state |

Do not hide a section in Impl 01 preview just because it is manual-empty: operators need to see the gap.

---

## 6. Hidden technical metadata

Never in client document body:

- `block_key`, `block_type`, `sort_order`, block id, status machine values;
- snapshot key / version / checksum;
- export key / checksum / storage path;
- weekly checkpoint ids/keys as a source list;
- `source_metric_refs` / `data_json`;
- `render_mode`, DB-05 fallback labels;
- apply/edit/snapshot buttons;
- admin nav/sidebar;
- raw `LOCAL_FIXTURE_ONLY` (strip; do not replace with a large debug badge inside the document);
- assembly source entry ids/categories.

Operator-only strip (preview, `no-print`): one back link to `/monthly-reports/{id}` is allowed. Print/PDF document must not include that strip.

---

## 7. Fixture / local / test markers

| Marker | Client document |
|--------|-----------------|
| `LOCAL_FIXTURE_ONLY` in titles/bodies | Strip entirely |
| `UiLabels::humanizeFixtureMarker` → «Тестовые данные» | Allowed only as a **small local-env footer/cover note**, not in every heading |
| Fixture English block titles | Prefer RU shell titles from `UiLabels::BLOCK_KEYS` for the six keys |
| Demo site `https://demo.example.test` | May remain as site URL (content); not a CDN issue |

Do not rewrite stored DB bodies in this visual wave. Filtering is **render-time**.

---

## 8. Finalized / export metadata display

| Item | Client document | Internal export detail |
|------|-----------------|------------------------|
| Finalized | Calm «Итоговый отчёт» + date | Keep technical finalized/snapshot facts |
| Draft preview | Calm «Черновик» + short note that this is not the issued file | n/a |
| Export checksum | Hidden | Technical details |
| Template id | Hidden in body; optional HTML comment/meta for future artifacts | Technical details |
| Share / download | Not in the document | Handoff UI |

Issued PDF **4** remains the current shareable file until an explicit regeneration proof wave.

---

## 9. Out of client report

- Internal notes, reviewer comments, unapproved AI drafts.
- Credentials / access material.
- Work-entry editor cards.
- Assembly apply controls.
- Weekly source dump.
- KPI invention.

---

## 10. Compatibility

Existing six shells stay. Flat DB-05 fields are fallback only (`flat_fallback`) and should be mapped to the same six headings if preview ever hits that mode. Do not surface «Плоское содержимое (резерв DB-05)» in the client document.
