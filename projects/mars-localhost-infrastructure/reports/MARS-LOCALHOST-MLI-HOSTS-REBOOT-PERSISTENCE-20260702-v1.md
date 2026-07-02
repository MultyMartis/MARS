# MLI X-Drive Hosts Registration and Windows Reboot Persistence — Receipt v1

**Date:** 2026-07-02  
**Task:** MLI X-DRIVE HOSTS REGISTRATION AND WINDOWS REBOOT PERSISTENCE TEST  
**Authority:** `X:\MARS-Localhost\` (runtime) · `X:\AI MARS\` (governance)  
**Branch:** `mars/canonical-post-recovery` @ `de1169cfc4d58eb879bac4387d514cd1a540a1eb` (HEAD unchanged by this task)

---

## Summary

Controlled registration of three MLI `.test` hosts entries, normal browser DNS/HTTP validation, manual Windows reboot, post-reboot X Laragon startup, read-only WordPress checks, and second Laragon stop/start cycle — **PASS**.

---

## Hosts backup

| Field | Value |
|-------|-------|
| **Original path** | `C:\Windows\System32\drivers\etc\hosts` |
| **Original SHA-256** | `2D6BDFB341BE3A6234B24742377F93AA7C7CFB0D9FD64EFA9282C87852E57085` |
| **Backup path** | `X:\MARS-Localhost\backups\system-config\hosts\hosts-pre-mli-domains-20260702-191327` |
| **Manifest** | `X:\MARS-Localhost\backups\system-config\hosts\manifest-20260702-191327.txt` |
| **Final hosts SHA-256** | `C591492AC1D64CE515130C9F407F4AB700903B26F4E936C06D2D8BE1D583F326` |

Entries added (operator-elevated apply):

```text
127.0.0.1 fws-0001.test
127.0.0.1 shpigovsky.test
127.0.0.1 mli-smoke-001.test
```

---

## Pre-reboot validation (2026-07-02)

| URL | DNS | HTTP |
|-----|-----|-----:|
| `http://fws-0001.test/` | 127.0.0.1 | 200 |
| `http://fws-0001.test/wp-login.php` | 127.0.0.1 | 200 |
| `http://shpigovsky.test/` | 127.0.0.1 | 200 |
| `http://shpigovsky.test/wp-login.php` | 127.0.0.1 | 200 |
| `http://mli-smoke-001.test/` | 127.0.0.1 | 200 |

**Pre-reboot stop timestamp:** `2026-07-02T19:50:36+07:00` — Laragon, Apache, MySQL stopped; ports 80/3306 free.

---

## Reboot evidence

| Field | Value |
|-------|-------|
| **Pre-reboot timestamp** | `2026-07-02T19:50:36+07:00` |
| **Windows boot time** | `2026-07-02T19:55:20+07:00` |
| **Real reboot proven** | **YES** — boot time after pre-reboot stop |
| **Post-reboot Laragon auto-start** | **NO** (expected; `RunAtStartup=0`) |

---

## Post-reboot validation (2026-07-02)

| Component | Executable under `X:\MARS-Localhost\laragon\` | Port |
|-----------|-----------------------------------------------|------|
| Laragon | `laragon.exe` | — |
| Apache | `bin\apache\httpd-2.4.66-260223-Win64-VS18\bin\httpd.exe` | 80 |
| MySQL | `bin\mysql\mysql-8.4.3-winx64\bin\mysqld.exe` | 127.0.0.1:3306 |

### FWS-0001

| Check | Result |
|-------|--------|
| HTTP `/` and `/wp-login.php` | 200 |
| `wp db check` | PASS |
| Active theme | `fws-synthetic` |
| Active plugins | `fws-synthetic-core`, `advanced-custom-fields` |

### Shpigovsky (read-only; not admitted to AG-WP-001)

| Check | Result |
|-------|--------|
| HTTP `/` and `/wp-login.php` | 200 |
| `wp db check` | PASS |
| Active theme | `shpigovsky` |
| Active plugins | `shpigovsky-core`, `advanced-custom-fields` |

### MLI smoke

| Check | Result |
|-------|--------|
| HTTP `/` | 200 |

### Second Laragon cycle

Stop → ports free → restart → all five HTTP URLs **200**; MySQL listener `127.0.0.1:3306` — **consistent**.

---

## Remaining follow-up (unchanged by this task)

| Item | Status |
|------|--------|
| **FW-07C-1 baseline revalidation** | **REVALIDATION_REQUIRED** |
| **Canonical secrets layout** (`X:\AI MARS\local\mli\`) | **Pending** |
| **SSL** | **Deferred** |

---

## Safety

- Hosts file: append-only MLI block; unrelated entries unchanged  
- Old Laragon / E-drive runtime: **NOT EXECUTED**  
- Forge frozen baseline / FP-0002 frontend: **NOT CHANGED**  
- WordPress writes: **0**  
- Windows reboot initiated by Cursor: **NO**

---

*Receipt v1 — MLI hosts registration and Windows reboot persistence 2026-07-02.*
