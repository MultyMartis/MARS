# FWS-0001 — Functional Live Validation v1

**Document type:** Functional validation report  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R  
**Runtime:** MLI-WP-SYN-001

---

## Environment

| Field | Value |
|-------|-------|
| **URL** | `http://fws-0001.test/` |
| **Access method** | Host header + Playwright host-resolver-rules |
| **Hosts file** | `fws-0001.test` **not** registered (limitation) |

---

## Functional checklist

| ID | Check | Result |
|----|-------|--------|
| F-01 | Homepage renders | **PASS** — HTTP 200 |
| F-02 | Page templates reachable | **PASS** — home, contacts |
| F-03 | CPT archive and single | **PASS** — `/services/`, `/services/testovaya-usluga/` |
| F-04 | Menus assign and display | **PASS** — primary menu assigned |
| F-05 | Options / ACF fields | **PASS WITH LIMITATION** — ACF Free profile |
| F-06 | Contact form submit | **NOT IN SCOPE** — stub acceptable per synthetic spec |
| F-07 | FAQ accordion | **NOT IN SCOPE** |
| F-08 | 404 template | **NOT EXECUTED** |

---

## Content population

| Method | Result |
|--------|--------|
| Populate script `mars-runtime/scripts/populate-fws-0001.ps1` | **WITH LIMITATIONS** — options JSON fix needed |
| Manual WP-CLI population | **PASS** — 4 services, pages, menu |

---

## Verdict

**PASS WITH DOCUMENTED LIMITATIONS** — core functional routes and CPT/menu behavior proven; populate script automation gap documented.

---

## Related

- [FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md](FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md)
- [FWS-0001-FW-V-04-FUNCTIONAL-LIVE-v1.md](FWS-0001-FW-V-04-FUNCTIONAL-LIVE-v1.md)

---

*Functional live validation v1 — FWS-0001.*
