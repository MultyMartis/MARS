# MARS Localhost MLI-03R.3 — Laragon Reboot Datadir Persistence v1

**Document type:** Master incident and remediation report  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.3  
**Prior HEAD:** `d0dfc20f` on `mars/post-cycle8-live-tests` (MLI-03R.2 at `a5a7de09`)

---

## 1. Result

```text
MLI Laragon cold-start persistence:
PROVEN

Controlled MySQL restart:
PASS

Full Windows reboot after durable remediation:
PENDING OPERATOR RETEST

FP-0002 WordPress foundation:
READY — CURRENT SESSION RESTORED

FWS-0001 synthetic runtime:
ACTIVE — CURRENT SESSION RESTORED

FW-06B:
WAITING FOR FP-0002 FRONTEND PRODUCTION PASS
```

---

## 2. Reproduced reboot failure evidence

| Signal | Observation |
|--------|-------------|
| Operator checker after Windows reboot | **FAIL** — effective datadir `mysql-8.4` |
| FP-0002 / FWS-0001 `wp db check` | **FAIL** |
| HTTP / HTTPS | **500** |
| VPN (v2rayN) | **Excluded** — both `.test` resolve `127.0.0.1`; Apache responds; MySQL on `127.0.0.1:3306` |
| Hosts | **Excluded** — resolution PASS in checker |

Evidence directory: `D:\MARS-Localhost\backups\runtime\mysql\MLI-03R3-REBOOT-DATADIR-DRIFT-20260624-161018\`

---

## 3. Preflight and backups

| Field | Value |
|-------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| Local HEAD at start | `d0dfc20f45aa038473ce12ad34120efa53cb9153` |
| Origin HEAD at start | `d0dfc20f45aa038473ce12ad34120efa53cb9153` |
| Expected MLI checkpoint | `a5a7de09` (ancestor; superseded by FP-0002 commits) |
| Staged at start | none |
| Unrelated WIP | preserved (not staged) |

---

## 4. Failed-state MySQL process and variables

| Field | Value |
|-------|-------|
| Binary | `mysql-8.4.3-winx64\bin\mysqld.exe` |
| Process model | parent + child (normal) |
| Listener | `127.0.0.1:3306` (child) |
| Command line | `--log-error=...\data\mysql-8.4\mysqld.log` (no `--defaults-file`) |
| Effective `datadir` | `D:\MARS-Localhost\laragon\data\mysql-8.4\` |
| Effective `bind_address` | `127.0.0.1` |
| Databases visible | `information_schema`, `mysql`, `performance_schema`, `sys` only |
| MLI DBs | **absent** (`mars_wp_fp0002`, `mars_wp_fws0001` on disk under `mysql-8.4.3` only) |

---

## 5. Laragon configuration authority inventory

| File / source | datadir | mysql-8.4 | mysql-8.4.3 | Modified at boot | Effective role |
|---------------|--------:|----------:|------------:|-----------------:|----------------|
| `bin\mysql\mysql-8.4.3-winx64\my.ini` | **mysql-8.4** | yes | no | **15:59:17** (MySQL start) | **LOADED by mysqld** (Windows default search order) |
| `data\my.ini` | mysql-8.4.3 | no | yes | 15:56:37 (Laragon start) | Operator mirror; **not loaded** |
| `usr\tpl\MySQL.my.ini.tpl` | *(absent pre-fix)* | — | — | 2026-06-22 | User merge input for Laragon generator |
| `bin\laragon\tpl\MySQL.my.ini.manifest.tpl` | *(absent)* | — | — | install baseline | Laragon generator base |
| `usr\profile\default.ini` | — | — | `mysql-8.4.3-winx64` | 2026-06-22 | Selected binary package |
| `usr\packages.conf` | — | **key `mysql-8.4`** | — | 2026-06-22 | Package family registry |
| `usr\laragon.ini` | — | — | — | 15:56:36 | Laragon preferences (no datadir) |

---

## 6. Startup command generation

```text
LARAGON STARTUP AUTHORITY:
laragon.exe MySQL service starter — regenerates
  D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini
at each MySQL start by merging:
  bin\laragon\tpl\MySQL.my.ini.manifest.tpl
  + usr\tpl\MySQL.my.ini.tpl
then programmatically injecting basedir + datadir.

WHY mysql-8.4 IS SELECTED:
Laragon derives the data directory name from the MySQL **package family**
(matching usr\packages.conf key mysql-8.4), not the full folder
mysql-8.4.3-winx64. It writes datadir=.../data/mysql-8.4 and starts
mysqld with --log-error=.../data/mysql-8.4/mysqld.log.
mysqld loads my.ini from the binary directory (no --defaults-file).
```

Timestamp proof: `data\my.ini` (correct `mysql-8.4.3`) written at Laragon launch; `bin\...\my.ini` (wrong `mysql-8.4`) rewritten at MySQL start.

---

## 7. Exact root cause

Controlled mysqld restart used the corrected configuration, but a full Laragon startup after Windows reboot selected or regenerated a different datadir authority pointing to `mysql-8.4`.

MLI-03R.1 updated `bin\my.ini` in-session; MLI-03R.2 validated controlled restart only. Neither prevented Laragon from **regenerating** `bin\my.ini` on cold application start after OS reboot.

---

## 8. Current-session recovery

1. Evidence captured (process inventory, variables, config timestamps, checker output).
2. MySQL shut down via `mysqladmin -u root shutdown`.
3. Canonical `bin\my.ini` restored (`datadir=mysql-8.4.3`, `bind-address=127.0.0.1`, `mysqlx=0`).
4. `data\my.ini` mirror synced.
5. MySQL started with `--log-error=...\mysql-8.4.3\mysqld.log`.
6. Effective datadir `mysql-8.4.3`; MLI databases visible; checker **PASS**.

---

## 9. Durable remediation selected

**OPTION B + read-only pin (MLI-03R.3 composite):**

| Layer | Action |
|-------|--------|
| B — User template | `usr\tpl\MySQL.my.ini.tpl` — explicit `datadir`, `bind-address`, `mysqlx=0` |
| A — Binary config | `bin\mysql\mysql-8.4.3-winx64\my.ini` — canonical full file |
| Pin | `attrib +R` on `bin\my.ini` — prevents Laragon generator overwrite |
| Mirror | `data\my.ini` — operator reference (unchanged role) |

**Not selected:** junction (unnecessary once config is pinned); datadir realignment; `--defaults-file` hook (unsupported in Laragon UI).

---

## 10. Durable remediation implementation

| Path | Change |
|------|--------|
| `D:\MARS-Localhost\laragon\usr\tpl\MySQL.my.ini.tpl` | Canonical `[mysqld]` with `datadir=.../mysql-8.4.3` |
| `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini` | Full canonical config; **ReadOnly=True** |
| `D:\MARS-Localhost\laragon\data\my.ini` | Mirror synced |
| `D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1` | Wrong-datadir guidance + durable mechanism check |
| `D:\MARS-Localhost\tools\recover-mli-mysql-datadir.ps1` | Audit / optional `-Apply` recovery |

---

## 11. Rollback procedure

1. Stop MySQL (`mysqladmin -u root shutdown` or Laragon Stop All).
2. `attrib -R D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini`
3. Restore pre-remediation files from `D:\MARS-Localhost\backups\runtime\mysql\MLI-03R3-REBOOT-DATADIR-DRIFT-20260624-161018\` or latest `MLI-03R3-RECOVER-*` backup.
4. Start MySQL; accept Laragon default `mysql-8.4` datadir drift risk.

---

## 12. First Laragon cold-start test

| Step | Result |
|------|--------|
| Stop MySQL + Apache; exit `laragon.exe` | PASS — 0 listeners |
| Launch `laragon.exe` | PASS |
| `bin\my.ini` after launch | **ReadOnly=True**; `datadir=mysql-8.4.3` unchanged |
| Start MySQL (Laragon-style `--log-error=mysql-8.4`) | PASS |
| Effective datadir | `mysql-8.4.3` |
| Checker | **PASS** |

---

## 13. Second Laragon cold-start test

| Step | Result |
|------|--------|
| Full stack stop + `laragon.exe` relaunch | PASS |
| `bin\my.ini` persistence | **ReadOnly=True**; datadir line unchanged |
| Effective datadir | `mysql-8.4.3` |
| Checker | **PASS** |

---

## 14. Final datadir state

| Variable | Value |
|----------|-------|
| `datadir` | `D:\MARS-Localhost\laragon\data\mysql-8.4.3\` |
| `basedir` | `D:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\` |

---

## 15. Network hardening state

| Check | Result |
|-------|--------|
| `bind_address` | `127.0.0.1` |
| Port 3306 | loopback only |
| Port 33060 | absent |
| `mysqlx` | `0` in pinned `my.ini` |

---

## 16. FP-0002 validation

| Check | Result |
|-------|--------|
| `wp db check` | **PASS** |
| HTTP `shpigovsky.test` | **200** |
| `blog_public` | `0` |

---

## 17. FWS-0001 validation

| Check | Result |
|-------|--------|
| `wp db check` | **PASS** |
| Active theme | `fws-synthetic` |
| Active plugins | `fws-synthetic-core`, `advanced-custom-fields` |
| HTTPS runtime | **200** + synthetic marker |

---

## 18. Post-reboot checker update

`verify-mli-after-reboot.ps1` now emits explicit wrong-datadir guidance and checks durable mechanism (`readOnly`, `bin\my.ini` datadir line, `usr\tpl` datadir line).

---

## 19. Recovery tooling

`recover-mli-mysql-datadir.ps1` — audit by default; `-Apply` after MySQL stop restores canonical files from embedded templates with backup.

---

## 20. Runtime and documentation updates

Brain-side reconciliation in this commit: OPERATIONAL-INDEX, DATABASE-STANDARD, post-reboot procedure, runtime manifests, FP-0002 foundation report status section.

---

## 21. Windows reboot gate

```text
Operator action after this remediation:
1. Full Windows reboot (when convenient).
2. Start Laragon normally.
3. Run: & "D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1"
4. Require SUMMARY: PASS before declaring Windows reboot persistence PROVEN.
```

---

## Related

- [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)
- [MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md](MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md)
- [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](../MARS-LOCALHOST-DATABASE-STANDARD-v1.md)

---

*MLI-03R.3 Laragon reboot datadir persistence v1.*
