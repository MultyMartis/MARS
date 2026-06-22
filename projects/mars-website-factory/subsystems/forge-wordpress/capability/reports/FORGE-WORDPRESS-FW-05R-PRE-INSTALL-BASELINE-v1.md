# Forge WordPress FW-05R — Pre-Install Baseline v1

**Document type:** Pre-install baseline record  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R  
**Case:** FWS-0001  
**Runtime:** MLI-WP-SYN-001

---

## Purpose

Document MLI runtime state immediately before Forge theme/plugin install and synthetic population for FW-05R live validation.

---

## Runtime snapshot

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-WP-SYN-001 |
| **Path** | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| **URL** | `http://fws-0001.test/` |
| **WordPress** | 7.0 ru_RU |
| **Git checkpoint** | `4a46267` on `mars/post-cycle8-live-tests` |

---

## Backup

| Field | Value |
|-------|-------|
| **Backup ID** | `pre-forge-fw05r` |
| **Location** | `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\pre-forge-fw05r` |
| **Purpose** | Rollback point before Forge package install |

---

## Pre-install state

| Component | State |
|-----------|-------|
| WordPress core | Installed, checksums verified (MLI-03) |
| Default bundled theme | Present |
| Forge theme `fws-synthetic` | **Not installed** |
| Forge plugin `fws-synthetic-core` | **Not installed** |
| ACF | **Not installed** |
| Synthetic content | **Not loaded** |
| Database | Empty of Forge CPT/content |

---

## Infrastructure baseline (verified)

| Check | Result |
|-------|--------|
| MySQL 127.0.0.1:3306 | **PASS** |
| `mysqlx=0` / port 33060 | **PASS** — not listening after restart |
| `wp db check` | **PASS** (MLI session) |
| HTTP reachability | **PASS** (Host header / Playwright resolver) |

---

## Post-baseline actions (FW-05R)

1. Install and activate `fws-synthetic-core`
2. Install and activate `fws-synthetic` theme
3. Install and activate ACF Free 6.8.4
4. Populate synthetic content
5. Run validation suite

---

## Related

- [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../../../../../mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md)
- [FWS-0001-FW-05R-LIVE-PREFLIGHT-v1.md](../../../../../workspaces/forge-wordpress-synthetic/FWS-0001/WORDPRESS/project-docs/FWS-0001-FW-05R-LIVE-PREFLIGHT-v1.md)

---

*FW-05R pre-install baseline v1.*
