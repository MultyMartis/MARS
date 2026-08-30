# i-SEO Report Hub — Monthly Report Detail Target IA v0.1

**Wave:** Monthly Report Detail UX Collapse Charter 01  
**Date:** 2026-08-21  
**Route:** keep `GET /monthly-reports/{id}`  
**Goal:** manager-friendly workspace without removing existing logic

---

## Design principle

One page remains the monthly report workspace. Hierarchy:

1. Know state  
2. Do primary workflow  
3. Edit work entries  
4. Scan content / delivery readiness  
5. Open diagnostics only when needed  

No data removal. Presentation and default open/collapsed state change only.

---

## 1. Top summary card

Always visible near the top.

| Element | Notes |
|---------|--------|
| Report title | Human title (sanitized display) |
| Period | `period_key` + date range |
| Client / project / site | From parent period context |
| Status | Existing status badge |
| Finalization state | Finalized / not finalized; short lock warning if finalized |
| Export / share readiness | Compact yes/no indicators (PDF ready, active link) — no token printing |
| Owner / reviewer (optional compact) | One line max; full timestamps stay in collapsed details |

If finalized: keep a **visible** lock/warning banner (never fully hidden).

---

## 2. Primary workflow actions

Prominent GET navigation near the top (above fold when practical):

| Priority | Label (RU) | Target |
|----------|------------|--------|
| Primary | `Работы за месяц` | in-page `#work-entries` (or keep section immediately below) |
| Primary | `Собрать черновик` | `/monthly-reports/{id}/assembly-preview` |
| Primary | `Предпросмотр отчета` | `/monthly-reports/{id}/preview` |
| Primary | `Файлы отчета` | snapshot exports page when snapshot exists; otherwise clear empty-state hint |

Secondary (visible but quieter):

| Label | Target |
|-------|--------|
| `Ежедневные заметки` / weekly notes | period weekly checkpoints |
| `Блоки отчета` | `/monthly-reports/{id}/blocks` |
| `К периоду` | `/reporting-periods/{periodId}` |
| `Изменить` (meta edit) | `/monthly-reports/{id}/edit` when `$canEdit` |

Danger / status-changing actions: **not** in this primary row — see Action Safety UX (`Административные действия` / `Изменение статуса`).

---

## 3. Work entries section

High on the page (immediately after summary + primary actions).

Show:

- counters  
- work cards  
- add work button (when allowed)  
- edit buttons  
- short notices (finalized vs editable)

This is the **main working area**. Duplicate primary workflow buttons inside the work-entries panel may be reduced or demoted to secondary to avoid double yellow-button clusters (implementation choice: prefer one strong primary action strip at top + lean work-entries local actions).

---

## 4. Report content summary

Compact panel.

Show only:

- section / field human name  
- clean status: filled / empty / fallback  

Do **not** show technical field keys unless inside collapsed tech details. Prefer short status line over dumping full body text on the detail page (full bodies remain on edit / preview / assembly routes).

---

## 5. Snapshot / export / share status

Compact card:

- PDF ready: yes/no  
- Active client link: yes/no (no token)  
- Links: open snapshot page, files page, share management page if already linked in product  

Details (checksum, snapshot key, template lineage notes) → collapsed `<details>`.

POST “create snapshot” stays available but **not** primary unless state requires it; place with admin/status zone or secondary within this card.

---

## 6. Technical diagnostics (collapsed by default)

Preserve all existing readiness gates, failed-gate lists, timestamps, source weekly notes, report raw details, and dense blocks table — but default **collapsed**:

- finalization checklist diagnostics  
- snapshot technical details  
- report raw / ID details  
- source daily/weekly notes list  
- report blocks table (if kept on page; list page link remains)  
- catalogue technical summary  
- internal create/update timestamps  

See Collapse Policy for open vs collapsed rules.

---

## Proposed vertical order (target)

1. Top summary card (+ finalized warning if any)  
2. Primary workflow actions  
3. Work entries  
4. Compact content summary  
5. Compact snapshot/export/share status  
6. Collapsed: administrative / status actions  
7. Collapsed: readiness checklist + finalization diagnostics  
8. Collapsed: parent period / details / source notes / blocks table / tech details  

Exact markup may reuse existing panels; order and default open state are the IA change.

---

## Non-goals

- New product features  
- Backend authorization or state-machine changes  
- DB / PDF / export / share mutation  
- Route rename (default keep current URLs)
