# FP-0002 — WordPress Database Provisioning v1

**Document type:** Database provisioning report  
**Version:** v1  
**Date:** 2026-06-23  
**Runtime ID:** MLI-WP-FP0002-LOCAL

---

## Provisioned resources

| Field | Value |
|-------|-------|
| Database | `mars_wp_fp0002` |
| Charset | `utf8mb4` / `utf8mb4_unicode_ci` |
| Application user | `mli_shpigovsky_app` |
| Host grants | `localhost`, `127.0.0.1` |
| Table prefix | `fp02_` |
| Root for app | **NO** — app uses dedicated user |
| FWS-0001 credentials | **NOT USED** |

---

## Secrets location

```text
X:\AI MARS\local\mli\fp-0002\runtime.env
```

Keys: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `TABLE_PREFIX`, `WP_ADMIN_*`, WordPress salts.

**Not in Git. Not in this document.**

---

## Provisioning method

Operator MySQL (`root` local Laragon) — `CREATE DATABASE`, `CREATE USER`, `GRANT` per MLI naming standard.

Evidence: database reachable via `mli_shpigovsky_app`; WP-CLI `core install` succeeded.

---

## Isolation

| Check | Result |
|-------|--------|
| Separate DB from FWS-0001 | **YES** (`mars_wp_fws0001` vs `mars_wp_fp0002`) |
| Separate app user | **YES** |
| `bind-address` | `127.0.0.1` (MLI profile) |

---

*FP-0002 database provisioning — FW-06A.*
