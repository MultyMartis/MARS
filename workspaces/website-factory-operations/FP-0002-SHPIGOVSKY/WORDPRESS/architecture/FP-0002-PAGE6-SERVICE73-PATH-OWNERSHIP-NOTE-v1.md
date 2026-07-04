# FP-0002 Page 6 / Service 73 Path Ownership Note v1

**Date:** 2026-07-04  
**Phase:** V9-06D.5 (documentation of secondary debt)

## Shared path

`/uslugi/zavisimosti/`

## Objects

| Object | ID | Type | Status | Generated permalink path |
|---|---:|---|---|---|
| Зависимости (page) | 6 | page | publish | `/uslugi/zavisimosti/` |
| Зависимости (service) | 73 | service | publish | `/uslugi/zavisimosti/` |

## Current resolver (D.5)

| Field | Value |
|---|---|
| HTTP | 200 |
| Resolved object | Service ID **73** |
| Resolved type | `service` |
| D.5 blocker | **NO** |

Request resolution prefers the Service CPT rewrite for this path. Page ID 6 remains published and shares the same generated path — ownership debt, not an active 404.

## Later action

`PATH_OWNERSHIP_CLEANUP_AFTER_TEMPLATE_INTEGRATION_PLANNING`

Recommended approach (not performed here):

1. Decide canonical owner for parent “Зависимости” (Service 73 per service IA).
2. Retire, redirect, or re-slug Page ID 6 under an authorized mutation task.
3. Do not mix cleanup with V9 template integration unless operator explicitly expands scope.

## Result

**DOCUMENTED_SECONDARY_DEBT**
