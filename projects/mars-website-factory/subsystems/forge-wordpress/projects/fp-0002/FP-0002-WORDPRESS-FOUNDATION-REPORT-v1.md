# FP-0002 — WordPress Foundation Report v1

**Version:** v1 | **Date:** 2026-06-23 | **Stage:** FW-06A / FW-06A.1

## Overall status

```text
READY
```

WordPress foundation closed and checkpointed (FW-06A.1). Approved frontend intake remains **PENDING**.

---

## Foundation readiness matrix

| Area | Result | Evidence | Blocking before integration |
|------|--------|----------|------------------------------|
| Runtime | **PASS** | `D:\MARS-Localhost\sites\wordpress\projects\shpigovsky` | No |
| Domain | **PASS** | Direct `shpigovsky.test` → 127.0.0.1 (FW-06A.1 closure) | No |
| Database | **PASS** | `mars_wp_fp0002` + `mli_shpigovsky_app` | No |
| WordPress | **PASS** | 7.0 ru_RU installed | No |
| Base config | **PASS** | [baseline doc](FP-0002-WORDPRESS-BASELINE-CONFIGURATION-v1.md) | No |
| Theme skeleton | **PASS** | `WORDPRESS/theme-source/shpigovsky/` — foundation only | No |
| Functionality plugin | **PASS** | `shpigovsky-core` 0.1.0 active | No |
| ACF | **PASS** (Free) | 6.8.4 — Pro pending | No for foundation |
| WPilot | **HOLD** | [WPilot doc](FP-0002-WPILOT-LOCAL-INSTALLATION-v1.md) — canonical package required | No for foundation |
| Plugins | **PASS** | [register](FP-0002-WORDPRESS-PLUGIN-REGISTER-v1.md) | No |
| Pages | **PASS** | [page registry](FP-0002-WORDPRESS-PAGE-REGISTRY-v1.md) | No |
| Menus | **PASS** | [menu map](FP-0002-WORDPRESS-MENU-MAP-v1.md) | No |
| Mail safety | **PASS** | MU suppress | No |
| Media policy | **PASS** | Documented | No |
| Roles | **PASS** | Local admin only | No |
| Backup/reset | **PASS** | `foundation-001` + scripts | No |
| Frontend acceptance | **PASS** | [acceptance slot](FP-0002-APPROVED-FRONTEND-ACCEPTANCE-SLOT-v1.md) | **YES** — integration locked |

---

## Forge project status

```text
WordPress foundation: READY
Theme integration: LOCKED
Approved frontend intake: PENDING
Production readiness: NOT ASSESSED
Client implementation: NOT STARTED
Production: NONE
```

---

## Validation summary

| Check | Result |
|-------|--------|
| `wp core is-installed` | PASS |
| `wp core verify-checksums` | PASS |
| HTTP front 200 | PASS (direct domain) |
| REST `/wp-json/` | PASS |
| Placeholder heading visible | PASS |
| `blog_public` = 0 | PASS |
| No production URL | PASS |
| FP-0002 `src/` unchanged | PASS |
| `mysqlcheck` on PATH (MLI session) | PASS — MySQL 8.4.3 |
| `wp db check` | PASS — all `fp02_` tables OK |
| Playwright foundation smoke | PASS — [report](FP-0002-WORDPRESS-FOUNDATION-PLAYWRIGHT-SMOKE-v1.md) |

---

## FW-06A.1 closure — direct domain

```text
Direct domain:
PASS

Evidence:
Operator browser verification + automated DNS/HTTP verification

Closure date:
2026-06-23
```

Historical note (FW-06A point-in-time): Host-header validation used before operator hosts elevation (Kaspersky block resolved 2026-06-23).

---

## FW-06A.1 closure — MySQL client and DB check

```text
mysql / mysqldump / mysqlcheck:
PASS — MySQL 8.4.3 (MLI session via activate-mli.ps1)

wp db check:
PASS — mars_wp_fp0002 all tables OK

Closure date:
2026-06-23
```

---

## MLI-03R.1 post-reboot qualification (2026-06-24)

```text
FW-06A.1 initial runtime validation:
PASS at original checkpoint (2026-06-23) — preserved above.

Post-reboot persistence incident:
DETECTED — MySQL datadir/config drift after Windows reboot.

MLI-03R.1 remediation:
PASS — datadir restored to mysql-8.4.3; loopback + mysqlx=0; wp db check PASS;
HTTP 200; Playwright 5/5; controlled MySQL restart PASS.

FP-0002 WordPress foundation:
READY — POST-REBOOT VALIDATED
```

Report: [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](../../../../mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)

### MLI-03R.3 reconciliation (2026-06-24)

```text
Post-Windows-reboot datadir drift (mysql-8.4):
REPRODUCED

Laragon cold-start persistence after MLI-03R.3:
PROVEN (2 consecutive cold starts)

FP-0002 WordPress foundation:
READY — CURRENT SESSION RESTORED

Full Windows reboot after MLI-03R.3:
PENDING OPERATOR RETEST
```

Report: [MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md](../../../../mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md)

FW-06B: **NOT EXECUTED**

---

## Next authorized action

```text
WAIT FOR FP-0002 FRONTEND PRODUCTION PASS
THEN RUN FW-06B — APPROVED FRONTEND INTAKE
```

See [FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md](FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md).

---

*FP-0002 WordPress foundation report — FW-06A / FW-06A.1 complete.*
