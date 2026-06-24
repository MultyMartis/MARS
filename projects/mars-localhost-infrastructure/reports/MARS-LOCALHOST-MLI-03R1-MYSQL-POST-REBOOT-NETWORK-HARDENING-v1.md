# MARS Localhost MLI-03R.1 — MySQL Post-Reboot Network Hardening v1

**Document type:** MySQL loopback and X Protocol validation after MLI-03R.1  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.1

---

## Objective

Restore MLI-03 / MLI-03R network posture after full Windows reboot exposed config drift.

---

## Configuration applied

| Setting | Previous (drift) | Target | Post-remediation |
|---------|------------------|--------|------------------|
| `datadir` | `mysql-8.4` | `mysql-8.4.3` | **PROVEN** |
| `bind-address` | `*` / `[::]:3306` | `127.0.0.1` | **PROVEN** |
| `mysqlx` | enabled | `0` | **PROVEN** |

**Active file:** `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini`

---

## Listen state (post-remediation)

| Endpoint | Port | Result |
|----------|------|--------|
| `127.0.0.1` | 3306 | **LISTENING** |
| `0.0.0.0` | 3306 | **NOT listening** |
| `[::]` | 3306 | **NOT listening** |
| All interfaces | 33060 | **NOT listening** |

---

## MySQL variables

| Variable | Value |
|----------|-------|
| `bind_address` | `127.0.0.1` |

---

## Controlled restart test (2026-06-24)

| Step | Result |
|------|--------|
| MySQL shutdown via `mysqladmin` | **PASS** |
| MySQL restart (canonical `mysqld` + log-error) | **PASS** |
| `bind_address` after restart | `127.0.0.1` |
| Port 3306 loopback only | **PASS** |
| Port 33060 absent | **PASS** |
| `wp db check` FP-0002 | **PASS** |
| `wp db check` FWS-0001 | **PASS** |

---

## Assessment

| Check | Status |
|-------|--------|
| Classic protocol loopback-only | **PROVEN** |
| X Protocol disabled | **PROVEN** |
| Survives controlled MySQL restart | **PROVEN** |
| Full Windows reboot re-test | **DEFERRED** — operator observation on next reboot |

---

## Related

- [MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md](MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md) — historical MLI-03 point-in-time
- [MARS-LOCALHOST-MLI-03R-MYSQL-X-PROTOCOL-HARDENING-v1.md](MARS-LOCALHOST-MLI-03R-MYSQL-X-PROTOCOL-HARDENING-v1.md) — historical MLI-03R point-in-time

---

*MySQL post-reboot network hardening v1 — MLI-03R.1.*
