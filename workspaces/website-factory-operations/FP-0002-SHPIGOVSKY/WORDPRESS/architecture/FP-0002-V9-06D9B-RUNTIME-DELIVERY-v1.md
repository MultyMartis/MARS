# FP-0002 V9-06D9-B Runtime Delivery

**Date:** 2026-07-05

## Mode

Bounded copy — 10 files, no mirror/purge/delete.

## Targets

| Target | Role | Files |
|--------|------|------:|
| `wp-content/themes/shpigovsky/` | **Active WP ABSPATH** | 10 |
| `app/public/wp-content/themes/shpigovsky/` | Charter-authorized path | 10 |

## Verification

SHA256 source ↔ target match on all delivered files.

## Infrastructure note

Task charter listed `app/public/...` as runtime target. Live WordPress installation uses project-root `ABSPATH` (`shpigovsky/` not `shpigovsky/app/public/`). Delivery applied to both paths; validation used active root.

Evidence: `validation/v9-06d9b-header-font-asset-messenger-repair/runtime-delivery-result.json`
