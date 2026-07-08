# FP-0002 V9-06E25A — Corrective Plan

**Wave:** V9-06E25A  
**Generated:** 2026-07-09

## Plan

| Component | Decision | Reason | Safety |
|---|---|---|---|
| List table | Hook `page_row_actions` + keep `post_row_actions` | hierarchical CPT compatibility | service-only guard |
| Capability | `user_can_duplicate()` via CPT `cap->create_posts` | fixes hidden actions for admins | no handler rewrite |
| Edit screen | Side meta box `Дублирование` | obvious second entry point | existing posts only |
| Copy logic | Preserve `duplicate_service()` | E25 PASS on copy semantics | no publish |
| Runtime | Deliver 2 plugin files | bounded delivery | checksum match |
| Validation | PHP hook eval + admin screenshots | prove UI without new duplicate | 0 DB writes preferred |

## Out of scope

- Blog/other pages porting
- Obsolete page cleanup
- Global hero settings
- New duplicate creation (use existing 746)

## Evidence

`validation/v9-06e25a-service-duplicate-action-visibility-repair/corrective-plan.json`

**Result:** PASS
