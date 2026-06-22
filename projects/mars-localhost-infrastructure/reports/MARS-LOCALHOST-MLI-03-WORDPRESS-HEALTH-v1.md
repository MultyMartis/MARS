# MARS Localhost MLI-03 — WordPress Health v1

**Document type:** WordPress runtime health validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Target

| Field | Value |
|-------|-------|
| Site | `fws-0001` |
| Domain | `fws-0001.test` |
| Path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| WordPress | **7.0** |

---

## HTTP health (Host-header routing)

All checks via `http://127.0.0.1/` with `Host: fws-0001.test` unless noted.

| Endpoint | HTTP status | Result |
|----------|-------------|--------|
| Front-end `/` | 200 | **PROVEN** |
| Admin `wp-login.php` | 200 | **PROVEN** |
| REST `wp-json/` | 200 | **PROVEN** (requires `mod_rewrite` enabled) |

---

## Core integrity

| Check | Result |
|-------|--------|
| WP-CLI `core verify-checksums` | **PROVEN** — PASS |
| Permalink / rewrite dependency | **PROVEN** — REST 200 after `mod_rewrite` enabled |

---

## Domain and hosts

| Check | Result |
|-------|--------|
| Direct `http://fws-0001.test/` | **WITH LIMITATIONS** — hosts entry **PENDING ELEVATION** |
| Host-header HTTP | **PROVEN** |

---

## Overall health status

**PROVEN WITH LIMITATIONS**

- Runtime is healthy for synthetic validation via loopback + Host header.
- Direct `.test` browser/CLI access pending managed hosts elevation (`add-mli-host.ps1` updated for multi-domain).

---

## Related

- [MARS-LOCALHOST-MLI-03-PLAYWRIGHT-WORDPRESS-SMOKE-v1.md](MARS-LOCALHOST-MLI-03-PLAYWRIGHT-WORDPRESS-SMOKE-v1.md)
- [MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md](../MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md)

---

*WordPress health report v1 — MLI-03.*
