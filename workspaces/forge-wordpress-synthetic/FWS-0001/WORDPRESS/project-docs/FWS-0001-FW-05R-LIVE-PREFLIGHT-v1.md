# FWS-0001 — FW-05R Live Preflight v1

**Document type:** Live validation preflight  
**Version:** v1  
**Date:** 2026-06-23  
**Case:** FWS-0001  
**Stage:** FW-05R  
**Git checkpoint:** commit `4a46267` on `mars/post-cycle8-live-tests`

---

## Runtime binding

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-WP-SYN-001 |
| **Physical path** | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| **Canonical URL** | `http://fws-0001.test/` |
| **Consumer workspace** | `workspaces/forge-wordpress-synthetic/FWS-0001/` |
| **Manifest** | [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../../../../projects/mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |

---

## Preflight checks

| Check | Result | Notes |
|-------|--------|-------|
| WordPress core installed | **PASS** | WP 7.0 ru_RU |
| Isolated DB/user | **PASS** | `mars_wp_fws0001` / `mli_fws0001_app` @ 127.0.0.1 |
| Pre-install backup | **PASS** | `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\pre-forge-fw05r` |
| `wp db check` | **PASS** | `mysqlcheck` available in MLI session |
| MySQL loopback (3306) | **PASS** | 127.0.0.1 only |
| MySQL X Protocol (33060) | **PASS** | `mysqlx=0` in my.ini; port not listening after restart |
| Hosts `fws-0001.test` | **WITH LIMITATIONS** | Not in hosts file; HTTP 200 via Host header and Playwright host-resolver-rules |
| Hosts `mli-smoke-001.test` | **PASS** | Present in managed block |
| FP-0002 isolation | **PASS** | Untouched |
| Credentials in reports | **PASS** | Excluded per policy |

---

## Package install plan

| Package | Action |
|---------|--------|
| Theme `fws-synthetic` | Install + activate |
| Plugin `fws-synthetic-core` | Install + activate |
| ACF Free 6.8.4 | Install + activate |
| Synthetic content | Populate (4 services, pages, menu) |

---

## Stop conditions (observed)

- No FP-0002 or client data used
- No production deployment
- No AG-WP-001 registry promotion without charter
- Reset only via documented baseline scripts

---

## Operator gates

| Gate | Status |
|------|--------|
| WV6 visual approval | **PENDING** |
| Hosts elevation for `fws-0001.test` | **PENDING** (non-blocking for scripted validation) |

---

## Related

- [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-RUNTIME-VALIDATION-INPUT-v1.md](../../../../projects/mars-website-factory/subsystems/forge-wordpress/reports/FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-RUNTIME-VALIDATION-INPUT-v1.md)
- [FORGE-WORDPRESS-FW-05R-PRE-INSTALL-BASELINE-v1.md](../../../../projects/mars-website-factory/subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-FW-05R-PRE-INSTALL-BASELINE-v1.md)

---

*FW-05R live preflight v1 — FWS-0001.*
