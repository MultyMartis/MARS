# Forge WordPress — External integration ownership standard v1

**ID:** FW-S-45  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  

No integration should silently depend on developer-local state.

---

## Card (every integration)

| Field | |
|-------|--|
| Owner | module or plugin |
| Credentials location | host env / SMTP plugin / Site Settings — **not** Git |
| Environment | staging vs production IDs |
| Failure behavior | empty → no output; form → honest error |
| Frontend dependency | blocking or additive |
| Admin setting | which screen |
| Launch gate | required before indexing / optional |

Typical rows: analytics, site verification, SMTP, captcha, maps, external APIs.

Empty Site Settings fields must not emit scripts ([SEO standard](FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md)).

---

*FW-S-45 v1.*
