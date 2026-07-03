# FP-0002 V9-06C.1 Source Activation Model v1

**Status:** SOURCE ACTIVATION GATE RESOLVED — NOT DELIVERED

## Purpose

V9-06C.1 replaces the old coarse Shpigovsky Core skeleton gate with a deterministic source phase model.

## Source Mode

`SHPIGOVSKY_CORE_MODE` is the source authority for plugin activation behavior.

Allowed values:

| Mode | Meaning |
|---|---|
| `skeleton` | Skeleton-only; content-model modules inert |
| `content_model` | V9-06C content-model modules can register hooks after delivery |
| `runtime_delivered` | Runtime-delivered source state; still does not imply migrations/forms/object creation |

Default after V9-06C.1: `content_model`.

`SHPIGOVSKY_CORE_SKELETON` remains only as a compatibility-derived constant and is false unless `SHPIGOVSKY_CORE_MODE === 'skeleton'`.

## Enabled In Content Model

- ContentTypes
- Permalinks
- Fields, with ACF/ACF PRO guards
- Settings, with ACF PRO guard
- Admin
- Validation, with ACF PRO guard

## Deferred Or Rejected

- Migrations: disabled until V9-06D2 or later.
- Forms: disabled until a later authorized phase.
- Taxonomies: rejected.
- Object creation, content migration, redirects, and rewrite flush: disabled.
- ACF Extended PRO: not used.

## Runtime Boundary

V9-06C.1 performs no runtime delivery, database writes, WordPress object mutations, ACF runtime sync, plugin updates, plugin installs, plugin deletes, or rewrite flush.
