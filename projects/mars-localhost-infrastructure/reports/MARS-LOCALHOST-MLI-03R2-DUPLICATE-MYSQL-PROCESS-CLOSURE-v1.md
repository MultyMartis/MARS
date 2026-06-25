# MARS Localhost MLI-03R.2 — Duplicate MySQL Process Closure v1

**Document type:** Remediation closure report  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.2  
**Prior observation:** two `mysqld.exe` PIDs (18436, 18108) after MLI-03R.1

---

## 1. Result

```text
MYSQL PROCESS STATE:
NORMAL — VERIFIED MULTI-PROCESS INTERNAL MODEL

MLI MySQL process state:
PROVEN — SINGLE CANONICAL SERVER

MLI MySQL current state:
PROVEN

Controlled MySQL restart:
PASS

Full Windows reboot:
DEFERRED OPERATOR GATE

FP-0002 WordPress foundation:
READY — CURRENT SESSION VALIDATED

FWS-0001 synthetic runtime:
ACTIVE — HTTPS VALIDATED

FW-06B:
WAITING FOR FP-0002 FRONTEND PRODUCTION PASS
```

No duplicate server instance was found. No process termination was required.

---

## 2. Git preflight

| Field | Value |
|-------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| Local HEAD at start | `5c65f793` |
| Origin HEAD at start | `5c65f793` |
| Ahead/behind | in sync |
| Reconciliation commit `b5358b4` | ancestor of HEAD; already on origin |
| Staged | none |
| Unrelated WIP | preserved (not staged) |

**Note:** Task brief expected local HEAD `b5358b4` unpushed; actual state had two later FP-0002 commits and `b5358b4` already reconciled on origin.

---

## 3. MySQL process inventory

See [MARS-LOCALHOST-MLI-03R2-MYSQL-PROCESS-IDENTITY-AUDIT-v1.md](MARS-LOCALHOST-MLI-03R2-MYSQL-PROCESS-IDENTITY-AUDIT-v1.md).

Summary:

| Metric | Pre-restart | Post-restart |
|--------|-------------|--------------|
| `mysqld.exe` count | 2 | 2 |
| TCP listeners on 3306 | 1 | 1 |
| Listener owner | child PID | child PID |
| Parent-child link | 18108 ← 18436 | 26532 ← 7968 |

---

## 4. PID and parent mapping

| PID | PPID | Parent executable | Creation (session) |
|-----|------|-------------------|--------------------|
| 18436 | 12944 | exited after spawn | 2026-06-24 12:31:41 |
| 18108 | 18436 | mysqld.exe | 2026-06-24 12:31:41 |
| 7968 | 30752 | Start-Process parent (exited) | post-restart |
| 26532 | 7968 | mysqld.exe | post-restart |

---

## 5. Port ownership

| Port | Address | Owner | Status |
|------|---------|-------|--------|
| 3306 | 127.0.0.1 | child mysqld | LISTEN |
| 33060 | — | — | absent |

**PRIMARY SERVER PID:** child mysqld (listener on 3306)  
**SECONDARY PID:** parent mysqld (no listener; supervisor)

---

## 6. Windows service and Laragon audit

| Check | Result |
|-------|--------|
| MySQL/MariaDB Windows services | none |
| Scheduled tasks | none matched |
| Laragon instances | 1 (`laragon.exe`) |
| Second manual mysqld launch | not evidenced |

---

## 7. MySQL server identity

| Item | Value |
|------|-------|
| Version | 8.4.3 |
| Datadir | `D:\MARS-Localhost\laragon\data\mysql-8.4.3\` |
| bind_address | 127.0.0.1 |
| server_uuid | `bbb926c1-6e4e-11f1-9bca-6045cb844e2e` |
| X Protocol | disabled (no 33060 listener) |

---

## 8. Second process classification

**CASE A — NORMAL PARENT/CHILD MODEL**

- Not a duplicate server.
- Not same-datadir unsafe duplicate (single listener, single identity).
- No closure/termination performed.

---

## 9. Duplicate closure actions

None required. Primary listener was never stopped blindly.

---

## 10. Canonical Laragon restart test

| Step | Result |
|------|--------|
| `mysqladmin -u root shutdown` | PASS — all mysqld exited; 3306 released |
| Canonical `mysqld --log-error=...\mysql-8.4.3\mysqld.log` | PASS |
| Readiness | PASS within 8s |
| Post-restart process count | 2 (parent + child) |
| Post-restart listener | `127.0.0.1:3306` on child PID |
| Effective datadir | `mysql-8.4.3` |
| bind_address | 127.0.0.1 |
| Port 33060 | absent |

---

## 11. Final MySQL process state

```text
Persistent mysqld server instances (logical): 1
Observed mysqld.exe processes (Windows model): 2 (parent + child)
Duplicate server: NO
```

---

## 12. Datadir and listener state

| Check | Status |
|-------|--------|
| Authoritative datadir `mysql-8.4.3` | PROVEN |
| `mysql-8.4` datadir | not deleted (unchanged) |
| Loopback-only 3306 | PROVEN |
| X Protocol off | PROVEN |

---

## 13. FP-0002 regression validation

| Check | Result |
|-------|--------|
| `wp core is-installed` | PASS |
| `wp core verify-checksums` | PASS |
| `wp db check` | PASS |
| `http://shpigovsky.test/` | HTTP 200 |
| `http://shpigovsky.test/wp-login.php` | HTTP 200 |
| `http://shpigovsky.test/wp-json/` | HTTP 200 |

---

## 14. FWS-0001 regression validation

| Check | Result |
|-------|--------|
| `wp core is-installed` | PASS |
| `wp core verify-checksums` | PASS |
| `wp db check` | PASS |
| Active plugin `fws-synthetic-core` | PASS |
| Active theme `fws-synthetic` | PASS |
| `http://fws-0001.test/` | HTTP 200 |
| `https://fws-0001.test/` | HTTP 200 + synthetic marker |

---

## 15. Post-reboot checker update

Runtime script `D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1` updated (D: only):

- `MySQL single server listener` — exactly one `127.0.0.1:3306`
- `MySQL process model` — accepts parent/child two-process Windows model when only child owns 3306

Brain procedure updated: [MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md).

---

## 16. Files created

| Path |
|------|
| `projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R2-MYSQL-PROCESS-IDENTITY-AUDIT-v1.md` |
| `projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md` |

---

## 17. Files updated

| Path |
|------|
| `projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md` |
| `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md` |
| `D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1` (runtime only) |

---

## 18. Sensitive and excluded artifacts

- No credentials published.
- `runtime.env` files not read.
- Unrelated WIP not staged.
- Runtime checker on D: not committed to Git.

---

## 19. Validation results

All 29 task validation items satisfied except git push of `b5358b4` as a discrete ahead commit — that commit was already on origin as ancestor; branch was in sync at `5c65f793`.

---

## 20. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Full Windows reboot post-MLI-03R.2 | DEFERRED — operator gate |
| Whether parent mysqld always persists entire server lifetime on all Windows builds | observed stable in this session; not exhaustively documented by vendor in local brain |

---

## 21. Deferred decisions

- Full OS reboot verification — operator runs `verify-mli-after-reboot.ps1` after next natural reboot.
- `mysql-8.4` legacy datadir cleanup — separate task; not in MLI-03R.2 scope.

---

## 22. Git push reconciliation

| Field | Value |
|-------|-------|
| `b5358b4` push | already on origin (ancestor) |
| Push required at closeout | only if MLI-03R.2 selective commit created |
| Unrelated WIP | excluded |

---

*Duplicate MySQL process closure v1 — MLI-03R.2.*
