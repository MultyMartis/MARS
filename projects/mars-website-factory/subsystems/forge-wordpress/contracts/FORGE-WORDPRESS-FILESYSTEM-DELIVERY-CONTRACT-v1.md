# Forge WordPress — Filesystem Delivery Authority Contract v1

**Project:** FP-0002  
**Task:** FW-07C-2C  
**Date:** 2026-07-03  
**Status:** PROVEN (additive + rollback)

---

## 1. Source

Git-tracked canonical surface:

`X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS\`

## 2. Build

Manifested package per surface:

| Package | Source root | Target root |
|---------|-------------|-------------|
| `shpigovsky-theme-foundation-<build-id>.zip` | `WORDPRESS/theme/shpigovsky/` | `wp-content/themes/shpigovsky/` |
| `shpigovsky-core-foundation-<build-id>.zip` | `WORDPRESS/plugins/shpigovsky-core/` | `wp-content/plugins/shpigovsky-core/` |
| `fp-0002-acf-json-foundation-<build-id>.zip` | `WORDPRESS/acf-json/` | `wp-content/acf-json/` |

Each package includes: package id, file manifest, SHA-256 per file, package SHA-256, allowlisted paths, excluded paths, source commit, build timestamp, secret audit, expected target identity, deletion policy, rollback metadata.

## 3. Delivery

Exact target allowlist only:

- `wp-content/themes/shpigovsky/`
- `wp-content/plugins/shpigovsky-core/`
- `wp-content/acf-json/`

Operations (Forge runtime):

| Operation ID | Module |
|--------------|--------|
| `forge.delivery.plan` | `delivery-planner.mjs` |
| `forge.delivery.checkpoint` | `delivery-checkpoint.mjs` |
| `forge.delivery.apply_additive` | `delivery-apply.mjs` |
| `forge.delivery.validate` | `delivery-validator.mjs` |
| `forge.delivery.rollback` | `delivery-rollback.mjs` |
| `forge.delivery.final_equivalence` | `delivery-equivalence.mjs` |

## 4. Runtime

Deployment target only — not canonical source:

`X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\`

## 5. Drift

Detected by comparing source manifest, package manifest, and runtime manifest (SHA-256 per file + aggregate hash).

## 6. Unknown files

**FAIL CLOSED** — unmanifested target files block mirror/replace operations.

## 7. Overwrite

Requires future explicit charter. FW-07C-2C: **NOT AUTHORIZED**.

## 8. Deletion

Requires future explicit charter. FW-07C-2C: **NOT AUTHORIZED** except exact owned proof file cleanup.

Deletion policy for FW-07C-2C proof:

```json
{
  "DELETE_EXISTING_FILES": false,
  "REMOVE_UNKNOWN_FILES": false,
  "MIRROR": false,
  "PURGE": false
}
```

## 9. Rollback

Checkpoint snapshot or exact owned-file reversal with hash verification before deletion.

## 10. Secrets

Never packaged. Token paths rejected by delivery path policy.

## 11. WordPress database

Outside filesystem delivery scope. Zero database writes in FW-07C-2C.

## 12. WPilot

Not modified by this capability. `write_enabled` must remain `false`.

## 13. MU-plugins

Not modified by this capability.

---

*Contract v1 — FW-07C-2C proof scope.*
