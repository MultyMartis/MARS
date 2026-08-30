# I-SEO Report Hub — Browser Demo UX Fix Implementation Result v0.1

**Date:** 2026-08-24  
**Wave:** Browser Demo UX Fix Implementation 01  
**Status:** BROWSER DEMO UX FIX PASS  
**Scope:** local app-source + runtime sync only (no host, no PDF/export/share, no DB seed)

## Implemented fixes

1. **Stale file/share navigation** — removed hardcoded sidebar links to `/report-snapshots/1/exports` and `/report-exports/4/shares`; replaced with parked copy (`PDF ещё не создан` / `Публичная ссылка ещё не создана`). Monthly detail and dashboard only link when a ready PDF / active share exists.
2. **Finalized July read-only for specialist** — hide «Добавить работу» and work-entry «Изменить»; show clear read-only notice; preview kept.
3. **Narrowed `seo_specialist`** — cannot create/edit reporting periods, monthly report form, or raw report blocks (403). Can still view periods/reports, preview, and mutate work entries on non-finalized reports.
4. **August detail simplification** — specialist primary CTAs: add work + client draft preview; admin/diagnostics/finalization collapsed behind privileged-only UI; delivery section honest parked state.
5. **Block edit access** — specialist denied on `/report-blocks/{id}/edit`; no raw `block_key` / `data_json` form.
6. **Copy polish** — login flash `Вход выполнен.`; health not a specialist primary CTA; period helper no longer promises files/PDF/share.

## Role / route behavior after fix

| Route | Specialist | Admin/lead |
|-------|------------|------------|
| `/`, periods list, monthly show/preview | allow | allow |
| work-entry create/edit (in_progress) | allow | allow |
| work-entry mutate on finalized | deny | allow |
| `/reporting-periods/create` | 403 | allow |
| `/monthly-reports/{id}/edit` | 403 | allow (if canEdit) |
| `/report-blocks/{id}/edit` | 403 | allow (if canEdit) |
| `/health` primary CTA | hidden | visible |

## Remaining backlog

- P2: denser work-entry field help redesign; catalogue-first vs manual-first layout.
- Future: `Specialist Report Block Editorial UI 01` (non-technical block editing).
- Parked: PDF / export / share generation and real delivery links.
- Optional: Production Config Normalization 01 (hosting paused).

## Not touched

- Host / production
- DB seed/cleanup, finalization state, passwords
- PDF/export/share/snapshot generation
- Foreign WIP outside i-SEO scope
