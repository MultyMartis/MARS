# MARS Localhost — Post-Reboot Verification Procedure v1

**Document type:** Operator procedure (read-only verification)  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.1 reconciliation

---

## Purpose

After a **full Windows reboot**, confirm that Laragon MySQL still loads the authoritative `mysql-8.4.3` datadir, loopback binding holds, and both MLI WordPress runtimes (FP-0002, FWS-0001) remain healthy — **without** automatic repairs, config changes, or service restarts.

This procedure complements controlled MySQL restart validation (already **PASS** during MLI-03R.1). It does **not** replace operator observation; it provides a single repeatable command.

---

## When to run

| Trigger | Action |
|---------|--------|
| Next natural Windows reboot | Operator runs verification once Laragon has started |
| Suspected post-reboot DB drift | Run before any remediation |
| Before `mysql-8.4` datadir cleanup task | Require **PASS** from this script |

**Not required** for normal daily work if current session checks already pass.

---

## Prerequisites

1. Laragon started (Apache + MySQL running).
2. No Windows reboot in progress.
3. Approved local secrets remain at brain-side `C:\AI MARS\local\mli\{slug}\runtime.env` (not read or printed by the script).

---

## Single command

```powershell
& "D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1"
```

**Exit code:** `0` = all checks PASS; non-zero = one or more FAIL (review console output).

---

## Checks performed (read-only)

| # | Check |
|---|--------|
| 1 | `mysqld.exe` process exists |
| 2 | Binary path under `mysql-8.4.3-winx64` |
| 3 | Effective `datadir` contains `mysql-8.4.3` |
| 4 | Effective `bind_address` = `127.0.0.1` |
| 5 | Port `3306` loopback-only |
| 6 | Port `33060` not listening |
| 7 | `shpigovsky.test` resolves |
| 8 | `fws-0001.test` resolves |
| 9 | FP-0002 `wp db check` |
| 10 | FWS-0001 `wp db check` |
| 11 | FP-0002 HTTP 200 |
| 12 | FWS-0001 HTTPS 200 + synthetic marker |
| 13 | PASS/FAIL summary |

The script does **not**: output passwords, modify `my.ini`, restart MySQL/Apache, delete `mysql-8.4`, or alter WordPress data.

---

## Expected outcomes

| Area | PASS criteria |
|------|----------------|
| MySQL | Version 8.4.3 family; datadir `...\laragon\data\mysql-8.4.3\` |
| Network | `127.0.0.1:3306` only; no `33060` |
| FP-0002 | `wp db check` success; `http://shpigovsky.test/` HTTP 200 |
| FWS-0001 | `wp db check` success; `https://fws-0001.test/` HTTP 200 with synthetic runtime content |

HTTP→HTTPS redirect on FWS-0001 may be direct HTTP 200 or 3xx depending on vhost/browser; HTTPS endpoint must serve the demo site.

---

## On failure

1. Record script output (no secrets).
2. Do **not** delete `mysql-8.4` datadir.
3. Escalate to MLI remediation charter — reference [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md).

---

## Related

- Runtime script (D: only, not in Git): `D:\MARS-Localhost\tools\verify-mli-after-reboot.ps1`
- Remediation master report: [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)

---

*Post-reboot verification procedure v1 — MLI-03R.1 reconciliation.*
