# MARS Localhost MLI-01 — Service Control Verification v1

**Document type:** Service control verification report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01

---

## Summary

| Check | Result |
|-------|--------|
| Laragon executable launches | **PASS** |
| Apache starts | **PASS** |
| MySQL starts | **PASS** (after MLI-01 data dir initialization) |
| Apache stops | **PASS WITH LIMITATION** — `httpd -k stop` fails (no Windows service); process stop works |
| MySQL stops | **PASS** — `mysqladmin -u root shutdown` |
| Orphan processes after stop | **PASS** — none observed after forced httpd stop + mysqladmin |
| Windows autostart disabled | **PASS** — `RunAtStartup=0` |
| Port 80 available when running | **PASS** |
| Port 3306 available when running | **PASS** |
| localhost HTTP | **PASS** — HTTP 200 |
| Laragon UI required continuously | **PASS** — not required |
| Cursor can observe processes/ports | **PASS** |

---

## Detail

### Apache

- Started via `httpd.exe` and confirmed listening on `:80`.
- Smoke site returned HTTP 200 with `Host: mli-smoke-001.test` header.
- Stop via `httpd -k stop` returned error (no installed Windows service `Apache2.4`).
- Stop via `Stop-Process -Name httpd` succeeded; port 80 released.

### MySQL

- Data directory initialized at `laragon\data\mysql-8.4.3` with `my.ini`.
- `mysqld` started; `SELECT VERSION()` → 8.4.3.
- `mysqladmin -u root shutdown` stopped server cleanly.

### Autostart

- `laragon.ini` updated: `RunAtStartup=0`.

---

## Classification legend

- **PASS** — verified in session
- **PASS WITH LIMITATION** — works with documented workaround
- **FAIL** — not met
- **NOT EXECUTED** — not attempted

---

*Service control verification v1 — MLI-01.*
