# i-SEO Report Hub — Monthly Report Detail Action Safety UX v0.1

**Wave:** Monthly Report Detail UX Collapse Charter 01  
**Date:** 2026-08-21  
**Scope:** presentation grouping only — **no** backend authorization / state-machine changes

---

## Principle

Separate **safe navigation (GET)** from **state-changing (POST)** actions. Keep existing allow/deny logic from readiness `$actions` and role flags. UX must make accidental finalize/reopen/snapshot-create less likely without removing capabilities.

---

## GET navigation actions — safe and prominent

These are primary or secondary workflow links:

| Action | Typical path | Placement |
|--------|--------------|-----------|
| Работы за месяц | `#work-entries` | Primary strip |
| Собрать черновик | `/monthly-reports/{id}/assembly-preview` | Primary strip |
| Предпросмотр отчета | `/monthly-reports/{id}/preview` | Primary strip |
| Файлы отчета | `/report-snapshots/{snapshotId}/exports` | Primary strip (when snapshot exists) |
| Блоки отчета | `/monthly-reports/{id}/blocks` | Secondary |
| Еженедельные заметки | period weekly list | Secondary |
| К периоду | `/reporting-periods/{periodId}` | Secondary |
| Изменить (meta) | `/monthly-reports/{id}/edit` | Secondary when `$canEdit` |
| Открыть снимок | `/report-snapshots/{id}` | Within compact snapshot card |
| Добавить / изменить работу | work-entry create/edit | Inside work entries |

Styling: primary strip uses clear hierarchy (one primary visual style for the main next step; others secondary). Avoid three competing yellow CTAs with equal weight.

---

## POST / state-changing actions — separated

Group under a clearly labeled zone, preferred labels:

- `Административные действия`  
- or `Изменение статуса`

Include:

| Action | Notes |
|--------|--------|
| Отправить на проверку | Existing `submit_review` |
| Отметить проверенным | Existing `mark_reviewed` |
| Финализировать | Existing `finalize` — highest caution |
| Открыть снова | Existing `reopen` |
| Создать снимок | Existing snapshot POST when `$canCreateSnapshot` |

Rules:

1. Visually separated from primary GET workflow (bordered panel, different heading, or collapsed `<details>` per Collapse Policy).  
2. Disabled when not allowed — keep button + reason (`$meta['reason']` via `ui_message`).  
3. Do not promote finalize / reopen / snapshot create into the primary yellow workflow row unless product state makes that the only sensible next step (rare; default: keep secondary/admin).  
4. Clear warnings near finalize/reopen (lock implications already documented in locked-notice).  
5. CSRF fields remain as today.

---

## Accidental-click reduction

| Risk | UX mitigation |
|------|----------------|
| Finalize | Not in primary strip; require admin zone; keep existing disabled reasons |
| Reopen | Same separation; emphasize unlock consequence |
| Create snapshot | Not primary CTA; secondary in snapshot card or admin zone |
| Export / share generation | **Out of scope for this wave** — do not add new generate-PDF/share primary buttons on detail page; do not mutate export 4 |
| Assembly apply | Remains on assembly-preview route (not introduced as primary POST on detail) |

This implementation wave must **not** click or auto-trigger dangerous actions in validation. Validation = GET + visual inspection + DB/export/share immutability checks.

---

## Backend boundary (hard)

Allowed in next implementation wave:

- Reorder markup  
- Collapse wrappers  
- CSS for zones  
- Button class / placement changes  

Not allowed without a separate charter:

- Changing who can finalize/reopen  
- Changing readiness gate logic  
- New POST endpoints  
- Auto-submit forms  
- DB / export / share / PDF mutation  

Presentation may hide prominence; it must not silently remove a previously available allowed action without an expand path to the same control.

---

## Relationship to P0 residuals

Edit-form `internal_note` / `evidence_note` textareas may still show fixture markers — out of scope for action safety UX. Collapsed tech details may retain raw markers — accepted residual.
