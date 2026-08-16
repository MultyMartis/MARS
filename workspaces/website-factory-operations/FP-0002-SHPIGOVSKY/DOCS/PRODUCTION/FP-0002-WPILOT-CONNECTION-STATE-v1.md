# FP-0002 — WPilot Connection State v1

**Wave:** PROD-P05-FU01 (**PASS**)  
**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Companion:** [FP-0002-WPILOT-INSTALL-READINESS.md](FP-0002-WPILOT-INSTALL-READINESS.md)  
**Rule:** No token values.

---

## Current state

| Field | Value |
|-------|-------|
| Install origin | Migrated with the site; **upgraded by MARS** in P05-FU01 |
| Public ping | **200** `/wp-json/wpilot/v1/ping` |
| Plugin | `metacode-wpilot` **active** |
| Plugin Version | **`0.3.2`** |
| RELEASE_LABEL | **`0.3.2-RC1`** |
| Schema | **`0.2.0`** |
| REST namespace | **`wpilot/v1`** |
| vs current global baseline `0.3.2 / 0.3.2-RC1` | **CURRENT** |
| `bridge_enabled` | **true** |
| `dev_confirmed` | **true** |
| Server-side token | **generated** — hash only in DB |
| Client token | **STORED LOCALLY** at `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` |
| `write_enabled` | **false** |
| `emergency_disabled` | **false** |
| Authenticated READ | **PROVEN** |
| P05 upgrade | **PERFORMED** (native Upload Plugin replace) |
| Historical local DEV token | `wpilot-local-shpigovsky.token` — **not** production authority |

---

## This wave (PROD-P05-FU01)

| Action | Done? |
|--------|-------|
| Reconfirm 0.3.2-RC1 package SHA | **YES — MATCH** |
| WP Admin HTTP login | **PASS** |
| Layer A post-reimport backup | **OPERATOR CONFIRMED** |
| Upgrade plugin | **YES** — 0.3.0 → 0.3.2-RC1 |
| Token reissue | **YES** — count **1** |
| Enable write | **NO** |
| Authenticated REST GET | **YES — PROVEN** |

---

## Remaining (deferred)

1. Migration tail cleanup / environment normalization (**PROD-P06** — not started).  
2. DNS cutover.  
3. Any WPilot **write** proof — separate charter only.

---

*WPilot Connection State v1 · PROD-P05-FU01 PASS · write remains disabled.*
