# MARS Localhost MLI-03 — WordPress Profile Validation Matrix v1

**Document type:** Full profile validation matrix  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Profile under test

| Field | Value |
|-------|-------|
| Profile | WordPress synthetic — FWS-0001 |
| Slug | `fws-0001` |
| Domain | `fws-0001.test` |
| Path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| WordPress | 7.0 |

---

## Validation matrix

| ID | Area | Check | Status | Evidence / limitation |
|----|------|-------|--------|------------------------|
| M3-01 | Git / toolchain | MLI-02 baseline on branch | **PROVEN** | Commit `4621388` on `mars/post-cycle8-live-tests` |
| M3-02 | MySQL | `bind_address` 127.0.0.1 | **PROVEN** | Config verified |
| M3-03 | MySQL | 127.0.0.1:3306 LISTENING | **PROVEN** | Port scan |
| M3-04 | MySQL | 0.0.0.0:3306 NOT listening | **PROVEN** | Port scan |
| M3-05 | MySQL | 33060 loopback-only | **WITH LIMITATIONS** | X Protocol still on all interfaces |
| M3-06 | Database | DB provisioned for WP install | **PROVEN** | Core install succeeded |
| M3-07 | Database | Per-runtime credentials policy | **WITH LIMITATIONS** | Secrets outside Git; not re-audited here |
| M3-08 | WordPress | Core 7.0 installed | **PROVEN** | Path + WP-CLI |
| M3-09 | WordPress | `verify-checksums` | **PROVEN** | PASS |
| M3-10 | WordPress | Front-end HTTP 200 | **PROVEN** | Host-header routing |
| M3-11 | WordPress | `wp-login.php` HTTP 200 | **PROVEN** | Host-header routing |
| M3-12 | WordPress | REST `wp-json` HTTP 200 | **PROVEN** | After `mod_rewrite` enabled |
| M3-13 | WordPress | Permalinks / rewrite | **PROVEN** | REST dependency satisfied |
| M3-14 | WP-CLI | `core is-installed` | **PROVEN** | PASS |
| M3-15 | WP-CLI | `db check` | **WITH LIMITATIONS** | PARTIAL — `mysqlcheck` not on PATH |
| M3-16 | Theme / plugin | Default core baseline | **WITH LIMITATIONS** | No extended synthetic pack audited |
| M3-17 | Hosts | `fws-0001.test` managed entry | **WITH LIMITATIONS** | PENDING ELEVATION |
| M3-18 | Hosts | `mli-smoke-001.test` | **PROVEN** | DNS 127.0.0.1; operator browser PASS |
| M3-19 | HTTP | Direct `.test` domain (fws-0001) | **WITH LIMITATIONS** | Blocked until hosts elevation |
| M3-20 | Playwright | Front-end | **PROVEN** | PASS |
| M3-21 | Playwright | Admin login | **PROVEN** | PASS |
| M3-22 | Playwright | REST | **PROVEN** | PASS |
| M3-23 | Playwright | HTTPS direct domain | **WITH LIMITATIONS** | FAIL until fws-0001.test in hosts |
| M3-24 | HTTPS | TLS baseline for FWS-0001 | **WITH LIMITATIONS** | Inherits MLI-02 stack; not separately proven |
| M3-25 | Backup | `baseline-001` snapshot exists | **PROVEN** | Standard backup path |
| M3-26 | Backup | Restore drill | **WITH LIMITATIONS** | Not executed |
| M3-27 | Forge handoff | Runtime pointers documented | **PROVEN** | Handoff report |
| M3-28 | Forge handoff | FW-05R unblocked | **WITH LIMITATIONS** | HOLD until profile gaps closed |
| M3-29 | Scope | FP-0002 production | **OUT OF SCOPE** | Explicit charter required |
| M3-30 | Security | No passwords in reports | **PROVEN** | Policy applied |

---

## Summary counts

| Status | Count |
|--------|------:|
| **PROVEN** | 18 |
| **WITH LIMITATIONS** | 11 |
| **OUT OF SCOPE** | 1 |

---

## Overall profile verdict

**PROVEN WITH LIMITATIONS**

The WordPress synthetic runtime on Laragon is **operationally usable for Host-header and loopback validation** and **partially ready for Forge consumer intake**. Full profile acceptance requires:

1. Elevated hosts entry for `fws-0001.test`
2. Playwright HTTPS re-run (4/4)
3. Optional: `mysqlcheck` on PATH for complete WP-CLI DB check
4. Optional: restore drill for backup confidence
5. FW-05R charter execution (separate from MLI-03 documentation)

---

## Report index

| Report | File |
|--------|------|
| MySQL loopback | [MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md](MARS-LOCALHOST-MLI-03-MYSQL-LOOPBACK-HARDENING-v1.md) |
| DB provisioning | [MARS-LOCALHOST-MLI-03-WORDPRESS-DATABASE-PROVISIONING-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-DATABASE-PROVISIONING-v1.md) |
| Plugin/theme | [MARS-LOCALHOST-MLI-03-WORDPRESS-PLUGIN-THEME-BASELINE-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-PLUGIN-THEME-BASELINE-v1.md) |
| WP-CLI | [MARS-LOCALHOST-MLI-03-WPCLI-RUNTIME-VALIDATION-v1.md](MARS-LOCALHOST-MLI-03-WPCLI-RUNTIME-VALIDATION-v1.md) |
| Health | [MARS-LOCALHOST-MLI-03-WORDPRESS-HEALTH-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-HEALTH-v1.md) |
| Playwright | [MARS-LOCALHOST-MLI-03-PLAYWRIGHT-WORDPRESS-SMOKE-v1.md](MARS-LOCALHOST-MLI-03-PLAYWRIGHT-WORDPRESS-SMOKE-v1.md) |
| HTTPS | [MARS-LOCALHOST-MLI-03-WORDPRESS-HTTPS-BASELINE-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-HTTPS-BASELINE-v1.md) |
| Backup | [MARS-LOCALHOST-MLI-03-BACKUP-AND-RESET-BASELINE-v1.md](MARS-LOCALHOST-MLI-03-BACKUP-AND-RESET-BASELINE-v1.md) |
| Forge handoff | [MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md](MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md) |

---

*WordPress profile validation matrix v1 — MLI-03.*
