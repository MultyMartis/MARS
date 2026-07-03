# FP-0002 V9-06D.1 Rerun Readiness v1

**Status:** READY AFTER V9-06C.1 SOURCE FIX

## Previous Blocker

The previous V9-06D.1 attempt was blocked before runtime apply because Shpigovsky Core source used `SHPIGOVSKY_CORE_SKELETON=true`; service CPT, permalink hooks, ACF field groups, Options Page, admin UX, and validation hooks would not register after delivery.

## V9-06C.1 Resolution

V9-06C.1 sets `SHPIGOVSKY_CORE_MODE=content_model` and routes module activation through `ModuleRegistry`.

Enabled in source:

- ContentTypes
- Permalinks
- Fields
- Settings
- Admin
- Validation

Still disabled:

- Migrations
- Forms
- Object creation
- Content migration
- Redirects
- Rewrite flush
- ACF Extended PRO usage

## Rerun Condition

V9-06D.1 may be rerun only as a separate runtime delivery task with explicit operator authorization, package/checkpoint controls, and runtime validation. V9-06C.1 does not perform delivery.
