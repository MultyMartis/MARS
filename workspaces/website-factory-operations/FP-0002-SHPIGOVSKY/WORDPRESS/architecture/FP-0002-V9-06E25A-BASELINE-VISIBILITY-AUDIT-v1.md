# FP-0002 V9-06E25A — Baseline Visibility Audit

**Wave:** V9-06E25A  
**Generated:** 2026-07-09

## Operator symptom

E25 created draft duplicate **746** (`Зависимости — копия`) but operator saw no `Дублировать` control in wp-admin.

## Findings

| Area | Finding | Root cause |
|---|---|---|
| Module load | PASS | `admin.service-duplicate` registered in `ModuleRegistry`; runtime file delivered |
| Plugin active | PASS | Hooks register on `plugins_loaded` |
| List table hook | FAIL (E25) | E25 used only `post_row_actions` |
| Hierarchical CPT | CONFIRMED | `service` has `hierarchical => true` → WP uses `page_row_actions` |
| Capability gate | FAIL (E25) | `current_user_can('create_posts')` is false; CPT maps create to `edit_posts` |
| Edit screen UI | FAIL (E25) | No meta box / visible button on edit screen |
| Copy logic | PASS | `duplicate_service()` works; draft 746 proves handler |

## Dual root cause

1. **Wrong list-table filter** — hierarchical posts never receive `post_row_actions`.
2. **Wrong capability literal** — `create_posts` check blocks all users including administrators for default-mapped service CPT.

## Evidence

`validation/v9-06e25a-service-duplicate-action-visibility-repair/baseline-visibility-audit.json`

**Result:** PASS (root cause identified)
