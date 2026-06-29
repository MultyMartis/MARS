# MARS Localhost — Smoke Suite v1

**Document type:** Reusable smoke suite specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-02

---

## Checks

| ID | Name | Method |
|----|------|--------|
| MLI-SMOKE-01 | Services | Apache/MySQL process + ports 80/443/3306 |
| MLI-SMOKE-02 | PHP CLI | `php -v` after activation |
| MLI-SMOKE-03 | MySQL | `mysql -u root -e "SELECT VERSION()"` |
| MLI-SMOKE-04 | Composer | `composer diagnose` |
| MLI-SMOKE-05 | WP-CLI | `wp --info`, `wp cli version` |
| MLI-SMOKE-06 | PHPCS/WPCS | `phpcs -i`, ruleset on fixture |
| MLI-SMOKE-07 | HTTP domain | `http://mli-smoke-001.test/` or documented fallback |
| MLI-SMOKE-08 | HTTPS | `https://mli-smoke-001.test/` or Playwright resolver |
| MLI-SMOKE-09 | Playwright | `tools\playwright-smoke\` headless |
| MLI-SMOKE-10 | Start/stop cleanup | Documented service control |

---

## Activation prerequisite

```bat
X:\MARS-Localhost\tools\activate-mli.cmd
```

---

## Honesty

Results may be `PASS`, `PASS WITH LIMITATION`, or `NOT EXECUTED`. Do not hide failures.

---

## Report

[reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md)

---

*Smoke suite v1 — MLI-02.*
