# MARS Localhost MLI-02 — Smoke Suite Report v1

**Document type:** Smoke suite execution report  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Results

| ID | Check | Result |
|----|-------|--------|
| MLI-SMOKE-01 | Services | **PASS** — Apache :80/:443, MySQL :3306 |
| MLI-SMOKE-02 | PHP CLI | **PASS** — 8.3.30 |
| MLI-SMOKE-03 | MySQL | **PASS** — 8.4.3 local query |
| MLI-SMOKE-04 | Composer | **PASS** — diagnose OK, pubkeys OK |
| MLI-SMOKE-05 | WP-CLI | **PASS** — 2.12.0 |
| MLI-SMOKE-06 | PHPCS/WPCS | **PASS** — fixture scan exit 0 |
| MLI-SMOKE-07 | HTTP domain | **PASS WITH LIMITATION** — Host-header 200; direct domain pending hosts |
| MLI-SMOKE-08 | HTTPS | **PASS** — Playwright + OpenSSL; browser trust not default |
| MLI-SMOKE-09 | Playwright | **PASS** |
| MLI-SMOKE-10 | Start/stop | **PASS WITH LIMITATION** — httpd stop via process kill per MLI-01 |

---

## Spec

[MARS-LOCALHOST-SMOKE-SUITE-v1.md](../MARS-LOCALHOST-SMOKE-SUITE-v1.md)

---

*Smoke suite report v1 — MLI-02.*
