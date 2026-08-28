# PATCH-DESIGN-v1

## Target

Admin.dev `wLrLp4WQHm1VJmxz` only. Operational.dev unchanged.

## Changes

1. **Handle Callback Action** — `queue_open`: call shared `buildFinalCard`; pending keyboard; `answer_text: 'Карточка'`.
2. **Recent Leads** — lifecycle-aware header (`📋 Лид` vs archive); attach pending action keyboard when status pending.

## Deploy

- **When:** 2026-08-28T11:09:44Z
- **PRE backup:** `backups/Admin.dev.pre-2026-08-28T11-09-44-262Z.json`
- **POST backup:** `backups/Admin.dev.post-2026-08-28T11-09-44-262Z.json`
- **ops_nodes_unchanged:** true

## Repo patches

- `implementation/patches/HandleCallbackAction.canonical-card-unification.js`
- `implementation/patches/RecentLeads.canonical-card-unification.js`
