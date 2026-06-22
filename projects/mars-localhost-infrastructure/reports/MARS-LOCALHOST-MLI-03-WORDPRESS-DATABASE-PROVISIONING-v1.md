# MARS Localhost MLI-03 — WordPress Database Provisioning v1

**Document type:** WordPress database provisioning validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Target runtime

| Field | Value |
|-------|-------|
| Site slug | `fws-0001` |
| Classification | WordPress synthetic |
| Physical path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| Local domain | `fws-0001.test` |
| Database name (standard) | `fws0001` per [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](../MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |

---

## Provisioning results

| Check | Result |
|-------|--------|
| Database created for synthetic runtime | **PROVEN** — WordPress 7.0 core install completed |
| Per-runtime least-privilege user | **WITH LIMITATIONS** — credentials stored outside Git; policy applied per MLI standard (not re-audited in this report) |
| MySQL reachable on loopback | **PROVEN** — `127.0.0.1:3306` LISTENING |
| WP-CLI `core install` | **PROVEN** — site operational |
| WP-CLI `db check` | **WITH LIMITATIONS** — **PARTIAL**; `mysqlcheck` not on PATH (see WP-CLI validation report) |

---

## Connectivity evidence

WordPress front-end, admin login, and REST endpoints return **HTTP 200** via Host-header routing to `fws-0001.test` (after `mod_rewrite` enabled). This implies successful database schema creation and runtime DB connectivity.

---

## Secrets

Database credentials are **not** recorded in this report. Secrets location per manifest contract: `C:\AI MARS\local\mli\fws-0001\` (outside Git).

---

## Related

- [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](../MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md)
- [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](../MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md)
- [MARS-LOCALHOST-MLI-03-WPCLI-RUNTIME-VALIDATION-v1.md](MARS-LOCALHOST-MLI-03-WPCLI-RUNTIME-VALIDATION-v1.md)

---

*WordPress database provisioning report v1 — MLI-03.*
