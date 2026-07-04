# FP-0002 REWRITE-RULE-REPAIR REPORT v1

**Phase:** REWRITE-RULE-REPAIR  
**Date:** 2026-07-04  
**Verdict:** PASS  
**Classification:** POST_TYPE_LINK_REWRITE_MISMATCH_REPAIRED

---

## Summary

Depth-2 service rewrite query mapping repaired from leaf-only `service=$matches[2]` to full hierarchical path `service=$matches[1]/$matches[2]`. Source updated, delivered to local runtime, soft rewrite flush performed under DB/plugin checkpoint. Service ID 74 route now HTTP **200** with queried path resolving to Service 74.

## Root cause addressed

`POST_TYPE_LINK_REWRITE_MISMATCH` — custom top rule `^uslugi/([^/]+)/([^/]+)/?$` previously injected only the leaf slug into the hierarchical `service` query var. WordPress `get_page_by_path` for hierarchical CPT requires `parent/child`. Leaf-only lookup failed for Service 74 (`post_parent=73`).

## Safety preflight

| Check | Value |
|---|---|
| Volume | X / AI WS |
| Branch | `mars/canonical-post-recovery` |
| Prior investigation | ROUTE-OWNERSHIP-INVESTIGATION PASS |
| Recommended repair | Option 2 — rewrite rule repair |

## Authorized mutations

1. Git source: `ServicePermalinks.php` depth-2 query mapping + contract doc §4.2.
2. Runtime plugin file: same `ServicePermalinks.php` delivery.
3. WordPress `rewrite_rules` option via soft rewrite flush (`wp rewrite flush`, no `--hard`).

No content, ACF/meta, menu, redirect, object, theme, or V9 source/dist writes.

## Checkpoint

| Field | Value |
|---|---|
| Name | `rewrite-rule-repair-pre-20260704-190040` |
| Root | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\rewrite-rule-repair-pre-20260704-190040\` |
| DB dump | `database\mars_wp_fp0002-rewrite-rule-repair-pre.sql` (1,075,415 bytes) |
| Plugin before | `plugin-source\ServicePermalinks.php.before` |
| Plugin after | `plugin-source\ServicePermalinks.php.after` |
| Secrets copied | 0 |
| Result | PASS |

## Source change

`WORDPRESS/plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php` — `register_rewrite_rules()`:

```php
// BEFORE
'index.php?post_type=service&service=$matches[2]'

// AFTER
'index.php?post_type=service&service=$matches[1]/$matches[2]'
```

Contract updated: `architecture/FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md` §4.2.

## Runtime apply

| Field | Value |
|---|---|
| Runtime | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| Plugin delivery | PASS |
| Soft flush | PASS (`wp rewrite flush`, no `--hard`) |
| `.htaccess` changed | NO |
| Rewrite hash before | `bf3926c71b7b134708fa052f782c911dcc931dd61b1964a49b034d5b546c3a12` |
| Rewrite hash after | `a0e11d66d4759f7628d3a0f86c740267c29bd656e86745505e35187e31bc1bfe` |
| Count before / after | 108 / 108 |
| Depth-2 query after | `index.php?post_type=service&service=$matches[1]/$matches[2]` |

## Post-repair route QA

| URL | Expected | HTTP | Permalink match | Resolved ID | Result |
|---|---|---:|---|---:|---|
| `/` | Page 4 | 200 | YES | 4 | PASS |
| `/uslugi/` | Page 5 | 200 | YES | 5 | PASS |
| `/uslugi/zavisimosti/` | Service 73 | 200 | YES | 73 | PASS |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service 74 | **200** | YES | **74** | **PASS** |
| `/uslugi/psihicheskoe-zdorovie/` | Service 77 | 200 | YES | 77 | PASS |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | Service 84 | 200 | YES | 84 | PASS |
| `/kontakty/` | Page 20 | 200 | YES | 20 | PASS |

Service 74 rewrite match:

- Matched rule: `^uslugi/([^/]+)/([^/]+)/?$`
- Query var: `service=zavisimosti/lechenie-alkogolnoy-zavisimosti`
- Resolved object: Service ID 74
- Response title: Лечение алкогольной зависимости

## Immutability

- Content changes: 0
- ACF/meta changes: 0
- Menus: UNCHANGED (3)
- Redirects: NOT CREATED
- Object counts: Pages 23 / Services 15 / Menus 3 (unchanged)
- Options changed: `rewrite_rules` only (plus runtime plugin file delivery)

## Secondary debt (unchanged)

Page ID 6 / Service ID 73 still share generated path `/uslugi/zavisimosti/`. Depth-1 currently resolves Service 73 (HTTP 200). Not a D.5 primary blocker after Service 74 repair. Schedule ownership cleanup later.

## Classification

`POST_TYPE_LINK_REWRITE_MISMATCH_REPAIRED` — depth-2 full-path query mapping restores hierarchical CPT lookup for Service 74.

## V9-06D.5 readiness

Service 74 route blocker cleared. V9-06D.5 visual route QA is **unblocked** for authorized routes (Pages 4/5/20, Services 73/74/77/84).

## Recommended next action

**V9-06D.5 visual route QA**

## Evidence

`WORDPRESS/validation/rewrite-rule-repair/`
