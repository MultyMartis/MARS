# MARS Localhost MLI-03R.1 — Active MySQL Config Audit v1

**Document type:** Post-reboot active MySQL configuration audit  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.1  
**Git baseline (pre-remediation):** `11e9155` on `mars/post-cycle8-live-tests`

---

## Incident context

After Windows reboot, WordPress FP-0002 reported database connection failure. `wp db check` returned MySQL error 1524 (`mysql_native_password` not loaded). Port 3306 was listening on `[::]:3306`.

---

## Running process (pre-remediation)

| Field | Value |
|-------|-------|
| **Binary** | `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysqld.exe` |
| **Process count** | 2 `mysqld.exe` instances observed (abnormal) |
| **Command line** | `--log-error=D:\MARS-Localhost\laragon\data\mysql-8.4\mysqld.log` (no `--defaults-file`) |
| **Version** | 8.4.3 |

---

## Configuration candidates

| Path | `datadir` | `bind-address` | `mysqlx` | Used by `mysqld` |
|------|-----------|----------------|----------|------------------|
| `laragon\bin\mysql\mysql-8.4.3-winx64\my.ini` | `mysql-8.4` | *(absent)* | *(absent)* | **YES** (Windows default search order) |
| `laragon\data\my.ini` | `mysql-8.4.3` | `127.0.0.1` | `0` | **NO** |

---

## Effective variables (pre-remediation)

| Variable | Value |
|----------|-------|
| `basedir` | `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\` |
| `datadir` | `D:\MARS-Localhost\laragon\data\mysql-8.4\` |
| `port` | `3306` |
| `bind_address` | `*` |
| `mysqlx_port` | `33060` (listener active on `[::]:33060`) |
| `default_authentication_plugin` | NOT AVAILABLE (removed in MySQL 8.4) |

---

## Databases visible (pre-remediation)

| Database | Present in active `datadir` |
|----------|----------------------------|
| `mars_wp_fp0002` | **NO** |
| `mars_wp_fws0001` | **NO** |

MLI WordPress data exists on disk under `laragon\data\mysql-8.4.3\` but was **not** mounted by the running server.

---

## Plugins (pre-remediation)

| Plugin | Status |
|--------|--------|
| `caching_sha2_password` | ACTIVE |
| `mysql_native_password` | **DISABLED** |

---

## Root finding

MLI-03 / MLI-03R hardening edited `laragon\data\my.ini`, but Laragon starts `mysqld` without `--defaults-file`. After reboot, the **binary-directory** `my.ini` won, pointing at an **empty** `mysql-8.4` datadir and exposing `bind_address=*` with X Protocol enabled.

---

## Post-remediation authority (2026-06-24)

| Field | Value |
|-------|-------|
| **Authoritative config** | `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini` |
| **Mirror reference** | `D:\MARS-Localhost\laragon\data\my.ini` (synced) |
| **datadir** | `mysql-8.4.3` |
| **bind_address** | `127.0.0.1` |
| **mysqlx** | `0` |

---

## Related

- [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](../MARS-LOCALHOST-DATABASE-STANDARD-v1.md)
- [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)

---

*Active MySQL config audit v1 — MLI-03R.1.*
