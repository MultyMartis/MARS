# MARS Localhost MLI-03 — Playwright WordPress Smoke v1

**Document type:** Playwright WordPress smoke validation  
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
| Fixture base | `D:\MARS-Localhost\tools\playwright-smoke\` (MLI-02 lineage) |

---

## Test matrix

| # | Scenario | Result |
|---|----------|--------|
| 1 | Front-end load | **PROVEN** — PASS |
| 2 | Admin login via `wp-login.php` | **PROVEN** — PASS |
| 3 | REST API reachable | **PROVEN** — PASS |
| 4 | HTTPS front-end (direct domain) | **NOT PROVEN** — FAIL until `fws-0001.test` in hosts |

**Summary:** **3 / 4 PASS**

---

## HTTP routing note

HTTP scenarios succeed with loopback + Host-header or Playwright host resolver patterns consistent with MLI-02 smoke fixture. Direct domain resolution for `fws-0001.test` remains blocked until managed hosts elevation completes.

---

## HTTPS Playwright failure context

HTTPS Playwright test **FAIL** is **expected** while `fws-0001.test` is absent from the hosts file. This is an **environment prerequisite** gap, not a WordPress core defect. See [MARS-LOCALHOST-MLI-03-WORDPRESS-HTTPS-BASELINE-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-HTTPS-BASELINE-v1.md).

---

## MLI-02 smoke site (reference)

| Site | DNS | HTTP | Browser |
|------|-----|------|---------|
| `mli-smoke-001.test` | 127.0.0.1 | 200 | **OPERATOR-VERIFIED PASS** |

---

## Related

- [MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md](MARS-LOCALHOST-MLI-02-PLAYWRIGHT-SMOKE-REPORT-v1.md)
- [MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md](../MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md)

---

*Playwright WordPress smoke report v1 — MLI-03.*
