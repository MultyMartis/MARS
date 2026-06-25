# MARS Localhost MLI-03R.2 — MySQL Process Identity Audit v1

**Document type:** Runtime process identity audit  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.2

---

## 1. Purpose

Explain why two `mysqld.exe` processes were observed after MLI-03R.1 and classify each PID before any termination action.

---

## 2. Pre-investigation observation (MLI-03R.1 closeout)

| PID | PPID | Notes |
|-----|------|-------|
| 18436 | 12944 | Parent/supervisor `mysqld` |
| 18108 | 18436 | Child `mysqld`; owned `127.0.0.1:3306` |

Both referenced:

```text
D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysqld.exe
--log-error=D:\MARS-Localhost\laragon\data\mysql-8.4.3\mysqld.log
```

---

## 3. Process inventory (2026-06-24 session)

| PID | PPID | Parent | Datadir (inferred) | Port | Listener | Role | Action |
|-----|------|--------|-------------------|------|----------|------|--------|
| 18436 | 12944 | exited launcher | `mysql-8.4.3` | — | none | Parent/supervisor | none |
| 18108 | 18436 | mysqld 18436 | `mysql-8.4.3` | 3306 | `127.0.0.1:3306` | Active server worker | none |

After controlled restart (`mysqladmin shutdown` + canonical `mysqld --log-error=...`):

| PID | PPID | Port | Listener | Role |
|-----|------|------|----------|------|
| 7968 | 30752 (exited) | — | none | Parent/supervisor |
| 26532 | 7968 | 3306 | `127.0.0.1:3306` | Active server worker |

---

## 4. Port ownership

| Endpoint | State | Owning PID |
|----------|-------|------------|
| `127.0.0.1:3306` | LISTEN | child mysqld (18108 pre-restart; 26532 post-restart) |
| `33060` | absent | — |

Only one TCP listener for classic protocol. No second server endpoint.

---

## 5. Windows service and launch source audit

| Source | Result |
|--------|--------|
| Windows MySQL/MariaDB services | none registered |
| Task Scheduler (mysql/maria/laragon) | none matched |
| Laragon GUI | `laragon.exe` PID 1432 running |
| Duplicate Laragon instances | none |
| Manual second server | not evidenced |

---

## 6. MySQL server identity (administrative probe)

| Variable | Value |
|----------|-------|
| `@@version` | 8.4.3 |
| `@@port` | 3306 |
| `@@datadir` | `D:\MARS-Localhost\laragon\data\mysql-8.4.3\` |
| `@@basedir` | `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\` |
| `@@hostname` | WSP-ONE |
| `@@server_uuid` | `bbb926c1-6e4e-11f1-9bca-6045cb844e2e` |
| `@@server_id` | 1 |
| `bind_address` | 127.0.0.1 |
| `named_pipe` | OFF |
| `mysqlx_port` | not listening |

Single server identity; no second endpoint to probe.

---

## 7. Classification

```text
Duplicate server: NO

Two-process observation: BENIGN — VERIFIED MULTI-PROCESS INTERNAL MODEL (Windows mysqld parent + worker child)

CASE: A — NORMAL TRANSIENT/PERSISTENT PARENT-CHILD (not a second server instance)
```

Rationale:

- Parent and child share the same binary and `--log-error` path (same datadir).
- Only the child PID binds `127.0.0.1:3306`.
- Parent has negligible CPU/working set; child carries server workload.
- Pattern reproduced identically after controlled canonical restart.
- No Windows service or second launch source.

---

## 8. Actions taken

| Action | Result |
|--------|--------|
| Terminate secondary PID | **not performed** — child is the active server |
| Controlled `mysqladmin -u root shutdown` | **PASS** |
| Canonical `mysqld --log-error=...` restart | **PASS** |
| Post-restart process model | parent + child; child owns 3306 |

---

*MySQL process identity audit v1 — MLI-03R.2.*
