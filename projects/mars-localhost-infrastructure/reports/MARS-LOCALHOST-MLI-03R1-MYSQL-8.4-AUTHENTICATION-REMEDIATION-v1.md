# MARS Localhost MLI-03R.1 — MySQL 8.4 Authentication Remediation v1

**Document type:** Master incident and remediation report  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.1  
**Prior HEAD:** `11e9155f017e256c9a57810fba5d0f835b3ea721`

---

## 1. Result

```text
MLI MySQL current state: PROVEN (current session + controlled restart)
Controlled MySQL restart: PASS
Full Windows reboot: DEFERRED OPERATOR GATE
FP-0002 WordPress foundation: READY — CURRENT SESSION VALIDATED
FWS-0001 synthetic runtime: ACTIVE — HTTPS VALIDATED (current session)
FW-06B: WAITING FOR FP-0002 FRONTEND PRODUCTION PASS
```

---

## 2. Incident evidence

| Signal | Observation |
|--------|-------------|
| `http://shpigovsky.test` | Database connection error (operator) |
| `wp db check` | Error 1524 — `mysql_native_password` not loaded |
| Port 3306 | `[::]:3306` LISTEN (pre-remediation) |
| Port 33060 | LISTEN (pre-remediation) |
| `mysqladmin ping` (no creds) | Access denied for `ODBC` — not project-account test |

---

## 3. Preflight and backups

| Item | Location |
|------|----------|
| Backup root | `D:\MARS-Localhost\backups\runtime\mysql\MLI-03R1-POST-REBOOT-20260624-122632\` |
| Config copies | `my.ini.binary-default`, `my.ini.laragon-data` |
| Process evidence | `mysqld-processes.json` |
| Account inventory | `account-inventory-sanitized.txt` |
| Logical dumps | `mars_wp_fp0002.sql`, `mars_wp_fws0001.sql` |
| Datadir file copy | `datadir-mysql-8.4.3-filecopy\` |
| `wp-config.php` (both) | backed up (sanitized filenames) |
| `runtime.env` (both) | backed up outside Git |

No passwords recorded in this report.

---

## 4. Root cause

**Primary:** After reboot, `mysqld` used the **binary-directory** `my.ini` with `datadir=mysql-8.4` (empty system DBs only). MLI WordPress databases and users live in `mysql-8.4.3`. WordPress could not reach its schema.

**Contributing:** MLI-03 loopback and MLI-03R X Protocol hardening were applied to `laragon\data\my.ini`, which is **not** the file Windows MySQL loads when Laragon omits `--defaults-file`.

**Authentication:** In the correct `mysql-8.4.3` datadir, application accounts already used `caching_sha2_password`. Error 1524 likely reflected client/server mismatch during wrong-datadir or transitional state. **No `mysql_native_password` re-enablement.** No `ALTER USER` required after datadir restoration.

---

## 5. Remediation performed

1. Stopped duplicate/abnormal `mysqld` processes.
2. Updated authoritative `laragon\bin\mysql\mysql-8.4.3-winx64\my.ini`:
   - `datadir` → `mysql-8.4.3`
   - `bind-address` → `127.0.0.1`
   - `mysqlx` → `0`
3. Synced `laragon\data\my.ini` as operator mirror.
4. Restarted MySQL; validated listeners, variables, databases, WordPress, Playwright.
5. Controlled second MySQL restart — configuration and auth persisted.
6. Added [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](../MARS-LOCALHOST-DATABASE-STANDARD-v1.md) and [provision-mli-wordpress-db.ps1](../scripts/provision-mli-wordpress-db.ps1).

**Not performed:** WordPress reinstall, database recreate, dump restore, `mysql_native_password` enable, password rotation, production access.

---

## 6. Sanitized account inventory (post-remediation)

| Runtime | User | Host | Plugin | Action |
|---------|------|------|--------|--------|
| FP-0002 | `mli_shpigovsky_app` | `127.0.0.1` | `caching_sha2_password` | None — already compliant |
| FP-0002 | `mli_shpigovsky_app` | `localhost` | `caching_sha2_password` | Retained (redundant; `DB_HOST=127.0.0.1`) |
| FWS-0001 | `mli_fws0001_app` | `127.0.0.1` | `caching_sha2_password` | None — already compliant |
| FWS-0001 | `mli_fws0001_app` | `localhost` | `caching_sha2_password` | Retained (redundant) |

---

## 7. Grants (127.0.0.1)

| User | Grants |
|------|--------|
| `mli_shpigovsky_app` | `mars_wp_fp0002.*` only |
| `mli_fws0001_app` | `mars_wp_fws0001.*` only |

No `GRANT OPTION`, `FILE`, `PROCESS`, `SUPER`, or `SYSTEM_USER`.

---

## 8. Validation summary

| Check | Result |
|-------|--------|
| `wp db check` FP-0002 | **PASS** |
| `wp db check` FWS-0001 | **PASS** |
| HTTP 200 (both runtimes, 3 URLs each) | **PASS** |
| Playwright FP-0002 foundation (5 tests) | **PASS** |
| `wp core verify-checksums` (both) | **PASS** |
| Controlled MySQL restart | **PASS** |
| Data loss | **NONE** |

---

## 9. FW-06A.1 reconciliation

| Phase | Status |
|-------|--------|
| FW-06A.1 initial validation (2026-06-23) | **PASS** — preserved |
| Post-reboot persistence incident | **DETECTED** |
| MLI-03R.1 remediation | **PASS** |
| FP-0002 foundation | **READY — POST-REBOOT VALIDATED** |
| FW-06B | **NOT EXECUTED** |

---

## 10. Deferred

| Item | Note |
|------|------|
| Full Windows reboot re-test | **DEFERRED BY OPERATOR** — use [MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md) on next natural reboot |
| Drop redundant `localhost` account variants | Low priority; `DB_HOST` uses `127.0.0.1` |
| Empty `mysql-8.4` datadir | **QUARANTINE CANDIDATE / DO NOT USE** — deletion deferred until successful full Windows reboot validation |

---

## Post-report Git and runtime reconciliation

**Reconciliation date:** 2026-06-24 (MLI-03R.1 final pass)

### Git state

| Item | Value |
|------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| Remediation commit | `f003fe8d` — `fix(mli): migrate local WordPress DB users for MySQL 8.4` |
| Local HEAD (reconciliation) | `8ccda4da` — includes `f003fe8d` in ancestry |
| Origin HEAD (reconciliation) | `8ccda4da` — matches local |
| Branch ahead/behind | **NO** — synced with `origin/mars/post-cycle8-live-tests` |
| `f003fe8d` on origin | **YES** (`git branch -r --contains f003fe8d`) |

### Push result (contradiction closure)

| Phase | Status |
|-------|--------|
| Initial report session (§28 agent closeout) | Push **NOT COMPLETED** / branch reported ahead by 1 at `f003fe8d` |
| Subsequent reconciliation | **PUSH CONFIRMED COMPLETE** — `f003fe8d` and later commits present on origin; local/origin HEAD aligned at `8ccda4da` |

No duplicate push required during reconciliation. No force push performed.

### Current MySQL runtime (no Windows reboot this session)

| Check | Result |
|-------|--------|
| Process binary | `mysql-8.4.3-winx64\bin\mysqld.exe` (two PIDs observed — Laragon parent/child pattern) |
| `VERSION()` | `8.4.3` |
| `datadir` | `D:\MARS-Localhost\laragon\data\mysql-8.4.3\` |
| `bind_address` | `127.0.0.1` |
| `127.0.0.1:3306` | **LISTENING** |
| `33060` | **NOT listening** |

### FP-0002 current state

| Check | Result |
|-------|--------|
| `wp db check` | **PASS** |
| `wp core verify-checksums` | **PASS** |
| `blog_public` | `0` |
| `http://shpigovsky.test/` | HTTP **200** — no database error |
| `wp-login.php`, `wp-json/` | HTTP **200** |

### FWS-0001 current state

| Check | Result |
|-------|--------|
| `wp db check` | **PASS** |
| `wp core verify-checksums` | **PASS** |
| Active theme | `fws-synthetic` |
| Active plugins | `advanced-custom-fields`, `fws-synthetic-core` (+ MU `mars-local-runtime`) |
| Demo content | **Present** — `MARS Forge WordPress Synthetic Runtime` marker in HTML |
| Database error | **None** |

### HTTPS / redirect state

| Probe | Result |
|-------|--------|
| `http://fws-0001.test/` (CLI, no redirect follow) | HTTP **200** direct (no `Location` header in automation session) |
| `https://fws-0001.test/` (PHP curl, local cert) | HTTP **200** — synthetic runtime renders |
| Operator browser session | HTTP → HTTPS redirect **confirmed by operator** after Laragon start |

Apache vhosts expose both `:80` and `:443` for `fws-0001.test`; WordPress `siteurl`/`home` remain `http://`. HTTPS availability is proven; HTTP→HTTPS may be operator-browser or HSTS behaviour — not required to block current runtime status.

### Windows reboot validation

```text
Full Windows reboot persistence test: DEFERRED BY OPERATOR
Reason: Operator actively working; reboot not authorized this session.
Blocking current work: NO
Controlled MySQL restart: PASS (unchanged from remediation)
```

Post-reboot operator command: `& "D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1"` — see [MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md).

### Empty `mysql-8.4` datadir policy

```text
Path: D:\MARS-Localhost\laragon\data\mysql-8.4
Status: QUARANTINE CANDIDATE / DO NOT USE
Deletion: DEFERRED UNTIL SUCCESSFUL FULL WINDOWS REBOOT VALIDATION
```

Directory left untouched (28 entries observed — not authoritative MLI data).

---

## Related

- [MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md](MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md)
- [MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md](MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md)

---

*MySQL 8.4 authentication remediation master report v1 — MLI-03R.1.*
