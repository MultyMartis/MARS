# LEADS-COMMAND-FORENSIC-v1

## Root cause (proven)

**Recent Leads** node always emitted `📁 Архивная карточка` and omitted pending action keyboard regardless of `manager_status === 'pending'`.

## Post-patch behavior (acceptance @ 2026-08-28T12:04:51Z)

- `/leads 3`: 3 pending cards
- All headers: `📋 Лид` (not archival)
- `incorrectly_archival`: **0**
- All cards: `telegram_has_buttons: true`
- **pass:** true

## Fix artifact

`implementation/patches/RecentLeads.canonical-card-unification.js` — deployed Admin.dev @ 2026-08-28T11:09:44Z.
