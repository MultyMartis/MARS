# FP-0002 Path Ownership Note — Services v1

**Date:** 2026-07-04  
**Context:** Post REWRITE-FLUSH-MICRO-GATE observation (read-only)

## Path under review

`/uslugi/zavisimosti/`

## Current generators

| Object | Type | Status | Generated path |
|---|---|---|---|
| Page ID 6 | `page` | publish | `/uslugi/zavisimosti/` |
| Service ID 73 | `service` | publish | `/uslugi/zavisimosti/` |

Both objects currently generate the same public path.

## HTTP after soft rewrite flush

| Path | HTTP | Notes |
|---|---:|---|
| `/uslugi/zavisimosti/` | 200 | Resolves; title “Зависимости” |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 404 | Service ID 74; generated permalink MATCH |

## Service ID 74

| Field | Value |
|---|---|
| Parent | Service ID 73 |
| Slug | `lechenie-alkogolnoy-zavisimosti` |
| Generated permalink | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| HTTP after flush | 404 |

Depth-2 service rewrite rules are present after flush. Soft flush alone is **not sufficient**.

## Blocking for D.5 visual QA

- Shared path Page 6 / Service 73: **not** an immediate hard blocker while HTTP 200.
- Service 74 depth-2 404: **active blocker** for alcohol-service visual route QA.

## Mutations in this note

None. Page ID 6 was not changed, deleted, or redirected.

## Recommended later action

`CREATE_ROUTE_OWNERSHIP_INVESTIGATION_TASK`

Investigate:

1. Whether Page ID 6 should remain published under `/uslugi/zavisimosti/`.
2. Whether hierarchical CPT rewrite + `post_type_link` filter correctly resolve depth-2 services when a Page shares the parent segment.
3. Whether custom rewrite / query resolution is required (planning only until authorized).
