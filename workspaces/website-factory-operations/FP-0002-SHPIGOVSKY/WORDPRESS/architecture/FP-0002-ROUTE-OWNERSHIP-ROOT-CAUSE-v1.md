# FP-0002 Route Ownership Root Cause v1

**Date:** 2026-07-04  
**Phase:** ROUTE-OWNERSHIP-INVESTIGATION  
**Runtime mutations:** 0

## Primary cause

**B. POST_TYPE_LINK_REWRITE_MISMATCH**

## Secondary causes

- **A. PAGE_SERVICE_PATH_COLLISION** — Page ID 6 and Service ID 73 both generate `/uslugi/zavisimosti/` (ownership debt; not the direct Service 74 404 mechanism).

## Failing URL

`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` — Service ID 74

## Evidence

| Check | Result |
|---|---|
| Service 74 object state | publish; parent Service 73 publish; slug `lechenie-alkogolnoy-zavisimosti` |
| Generated permalink (`post_type_link`) | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` — MATCH |
| HTTP | **404** |
| Depth-2 rewrite rule present | `^uslugi/([^/]+)/([^/]+)/?$` |
| Matched query | `index.php?post_type=service&service=$matches[2]` → `service=lechenie-alkogolnoy-zavisimosti` |
| `get_page_by_path(leaf, service)` | **null** |
| `get_page_by_path(zavisimosti/lechenie-alkogolnoy-zavisimosti, service)` | **74** |
| WP_Query leaf service var | `found_posts=0` |
| WP_Query full-path service var | `found_posts=1` |
| Controls 77 / 84 | HTTP 200 |

## Why generated permalink is correct but HTTP is 404

1. `ServicePermalinks::filter_service_permalink` walks `post_parent` and emits the full public path.
2. `ServicePermalinks::register_rewrite_rules` registers a depth-2 top rule that injects **only the leaf slug** into the hierarchical `service` query var.
3. WordPress hierarchical CPT resolution resolves the `service` query var like a path (`get_page_by_path` style). Leaf-only lookup looks for a **root** service named `lechenie-alkogolnoy-zavisimosti`, which does not exist.
4. Query finds no object → front controller returns HTTP 404.
5. Template loader and `redirect_canonical` never participate for this URL.

## Why controls work

Services 77 and 84 are root-level (`post_parent = 0`). Depth-1 rule sets `service={slug}`, which equals their full hierarchy path, so lookup succeeds.

## Page ID 6 / Service ID 73

| Object | Path | Status |
|---|---|---|
| Page ID 6 | `/uslugi/zavisimosti/` | publish (legacy source page) |
| Service ID 73 | `/uslugi/zavisimosti/` | publish |

Winning rewrite for the shared path is the custom top depth-1 service rule (`service=zavisimosti` → Service 73). Collision is real for generated ownership but **not** the Service 74 404 root cause.

## Repair layer

| Layer | Role |
|---|---|
| **rewrite rules** (primary) | Correct depth-2 query mapping to `service=$matches[1]/$matches[2]` |
| permalink generator | Already correct — no change required for this failure |
| request resolver | Optional alternative; not required if rewrite mapping is fixed |
| template loader | Not involved |
| path ownership policy | Later cleanup for Page 6; separate task |
| redirect/canonical | Reject as primary fix |

## Source locus

`plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php` — `register_rewrite_rules()` depth-2 query string.

Contract note: `FP-0002-SERVICE-PERMALINK-REWRITE-CONTRACT-v1.md` currently documents the same leaf-only mapping and must be corrected with the repair.

## Result

Root cause **IDENTIFIED**. Service 74 route **STILL_404**. No runtime mutations in this investigation.
