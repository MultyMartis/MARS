# FINAL WORKFLOW STATE v1

**As of:** post activate-monitor 2026-08-04 ~13:26 UTC

| Workflow | ID | Active |
|---|---|---|
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | **YES** |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | **YES** |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | **NO** |
| Sales-Manager-v1 | `cJGoQUqIIHull4p7` | **NO** |

| Metric | Value |
|---|---|
| Active Gmail intake count | **1** (Operational.dev only) |
| Workflows created this phase | **0** |
| Operational node count | **45** (was 42; +Prepare Claims, Upsert Claim, Restore Claimed Items) |
| OpenRouter AI | **disabled** |
| Graph cycles | **0** |
| Telegram Skip Pass → Send | **none** |

## Patch highlights (same Ops ID)

- Stamp Delivery Result → `runOnceForAllItems` (hash `674C84E16D7F3FB4`)
- Expand claim-aware (hash `B890B3D24C339FE7`)
- Aggregate admin-anchor finalize (hash `3D1A8133C1228850`)
- Update Last Success prefers Aggregate Delivery Finalizer
- Claim-before-send serialized Sheets upsert by `delivery_key`
