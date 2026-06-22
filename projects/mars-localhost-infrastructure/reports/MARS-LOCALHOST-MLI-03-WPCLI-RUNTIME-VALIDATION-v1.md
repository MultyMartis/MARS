# MARS Localhost MLI-03 — WP-CLI Runtime Validation v1

**Document type:** WP-CLI runtime validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Target

| Field | Value |
|-------|-------|
| WP-CLI | 2.12.0 (from MLI-02 baseline) |
| Site path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| Site URL | `fws-0001.test` |

---

## Command results

| Command / check | Result |
|-----------------|--------|
| `wp core is-installed` | **PROVEN** — core installed |
| `wp core verify-checksums` | **PROVEN** — PASS |
| `wp db check` | **WITH LIMITATIONS** — **PARTIAL**; `mysqlcheck` not on PATH |
| Site management against live DB | **PROVEN** — install and runtime checks succeeded |

---

## `db check` limitation detail

WP-CLI `db check` delegates to `mysqlcheck`. On this host, `mysqlcheck` is **not on PATH** at validation time. This does **not** invalidate WordPress DB connectivity (proven by install and HTTP smoke), but full WP-CLI DB integrity tooling is **not PROVEN** until `mysqlcheck` is reachable or an equivalent check is documented.

---

## Recommended follow-up (non-blocking for MLI-03 core proof)

1. Add Laragon MySQL `bin` to PATH for operator sessions, **or**
2. Document explicit path invocation for `mysqlcheck` in MLI tooling notes.

---

## Related

- [MARS-LOCALHOST-WPCLI-STANDARD-v1.md](../MARS-LOCALHOST-WPCLI-STANDARD-v1.md)
- [MARS-LOCALHOST-MLI-03-WORDPRESS-DATABASE-PROVISIONING-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-DATABASE-PROVISIONING-v1.md)

---

*WP-CLI runtime validation report v1 — MLI-03.*
