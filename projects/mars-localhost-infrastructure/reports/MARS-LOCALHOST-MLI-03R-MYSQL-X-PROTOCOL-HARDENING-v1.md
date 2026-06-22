# MARS Localhost MLI-03R — MySQL X Protocol Hardening v1

**Document type:** MySQL X Protocol hardening validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03R (FW-05R closure)  
**Git baseline:** commit `4a46267` on `mars/post-cycle8-live-tests`

---

## Objective

Close residual MLI-03 gap: MySQL X Protocol (port 33060) listening on all interfaces. WordPress uses classic MySQL protocol on 3306 only; X Protocol is not required for MLI WordPress consumers.

---

## Configuration applied

| Setting | Value |
|---------|-------|
| `mysqlx` | `0` added to `my.ini` |
| MySQL service | Restarted |

---

## Listen state (post-restart)

| Endpoint | Port | Result |
|----------|------|--------|
| `127.0.0.1` | 3306 | **LISTENING** |
| `0.0.0.0` | 3306 | **NOT listening** |
| All interfaces | 33060 | **NOT listening** |

---

## Assessment

| Check | Status |
|-------|--------|
| Primary SQL port loopback-only (3306) | **PROVEN** (MLI-03) |
| X Protocol disabled (33060) | **PROVEN** (MLI-03R) |
| WordPress / WP-CLI DB connectivity | **PROVEN** — `wp db check` PASS in FW-05R session |

---

## Related

- [MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md](MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md)
- [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md)

---

*MySQL X Protocol hardening v1 — MLI-03R.*
