# FP-0002 Route Ownership Recommended Repair v1

**Date:** 2026-07-04  
**Phase:** ROUTE-OWNERSHIP-INVESTIGATION  
**Status:** APPLIED — PASS (REWRITE-RULE-REPAIR 2026-07-04)

## Recommended option

**Option 2 — Rewrite rule repair**

## Exact next micro-task

`CREATE_REWRITE_RULE_REPAIR_MICRO_TASK`

## Expected changes

### Source (Git)

In `WORDPRESS/plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php`:

```php
// BEFORE (broken for depth-2 hierarchical lookup)
add_rewrite_rule(
    '^uslugi/([^/]+)/([^/]+)/?$',
    'index.php?post_type=service&service=$matches[2]',
    'top'
);

// AFTER (full hierarchy path in service query var)
add_rewrite_rule(
    '^uslugi/([^/]+)/([^/]+)/?$',
    'index.php?post_type=service&service=$matches[1]/$matches[2]',
    'top'
);
```

Update `FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md` §4.2 to document full-path mapping.

### Runtime (later authorized apply)

1. Deliver updated `shpigovsky-core` source to local runtime.
2. DB checkpoint.
3. Soft rewrite flush only (`rewrite_rules` option).
4. No content/ACF/menu/redirect/object writes.

## Required checkpoint

Database checkpoint before soft flush (same pattern as REWRITE-FLUSH-MICRO-GATE).

## Required validation

| Check | Expected |
|---|---|
| Service 74 generated permalink | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` unchanged |
| Service 74 HTTP | 200 |
| Queried object | Service ID 74 |
| `/uslugi/` | Page ID 5, HTTP 200 |
| `/uslugi/zavisimosti/` | HTTP 200 (Service 73 via depth-1 rule) |
| Controls 77 / 84 | HTTP 200 |
| Content/ACF/menus/redirects | Unchanged |
| Object counts | Unchanged |

## Rollback

1. Restore prior `ServicePermalinks.php` in source and runtime.
2. Restore `rewrite_rules` from checkpoint or re-flush prior plugin version.
3. Re-validate Service 74 returns to known 404 baseline only if rollback required.

## Why not Option 1 first

Contract model is `CPT_REWRITE_PLUS_POST_TYPE_LINK_FILTER`. Permalink generation is already correct; only rewrite query mapping is wrong. A custom request resolver is reserved for cases where rewrite + filter fail after correct mapping.

## Why not Option 3 first

Page ID 6 cleanup is real ownership debt but does not fix leaf-only depth-2 mapping. Schedule after Service 74 route passes.

## Result

Recommended repair **applied** in REWRITE-RULE-REPAIR micro-task (2026-07-04): source + runtime delivery + soft flush. Service 74 HTTP 200. See `FP-0002-REWRITE-RULE-REPAIR-REPORT-v1.md`.
