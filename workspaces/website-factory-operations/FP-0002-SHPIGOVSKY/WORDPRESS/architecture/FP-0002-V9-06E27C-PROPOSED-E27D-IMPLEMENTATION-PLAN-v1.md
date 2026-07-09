# FP-0002 V9-06E27C — Proposed E27D Implementation Plan

**Planned task:** V9-06E27D Page Service Ownership Implementation  
**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/proposed-e27d-implementation-plan.json`  
**Status:** Plan only — **do not execute in E27C**

## Steps

| Step | Action | Object IDs | Safety | Validation |
|---:|---|---|---|---|
| 1 | Fresh DB checkpoint | — | Mandatory mysqldump + SHA256 | `db-checkpoint.json` |
| 2 | Retarget Primary menu item | `#301` → service `#73` | Single menu meta update | Menu + route probe |
| 3 | Pre-trash validation | `#301`, `#73` | Read-only HTTP | menu_route_alignment PASS |
| 4 | Trash legacy pages | `#6`, `#7`, `#8` | `wp_trash_post` only | Status = trash |
| 5 | Post-cleanup route probe | `#73`, `#74`, `#75`, `#77`, `#84` | HTTP 200 expected | route validation JSON |

## Stop conditions

- Menu retarget fails or route owner flips unexpectedly
- Protected objects change status
- Permalink or rewrite flush becomes necessary

## Rollback

1. Restore pages `#6–#8` from Trash, or  
2. Revert menu item `#301` to page `#6`, or  
3. Full DB checkpoint restore

## Explicitly out of E27D scope

- Redirects (not needed — same URLs)
- Rewrite flush
- Creating missing `/uslugi/zavisimosti/specialistam/` service object
- Production migration
