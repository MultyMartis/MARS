# FWS-0001 — WordPress Correctness Live Validation v1

**Document type:** WordPress correctness validation report  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-05R  
**Runtime:** MLI-WP-SYN-001

---

## Active packages

| Package | Slug | Status |
|---------|------|--------|
| Theme | `fws-synthetic` | **Active** |
| Functionality plugin | `fws-synthetic-core` | **Active** |
| ACF Free | `advanced-custom-fields` | **Active** (6.8.4) |

---

## Template and registration checks

| ID | Check | Result |
|----|-------|--------|
| W-01 | `style.css` theme header valid | **PASS** |
| W-02 | Template hierarchy per map | **PASS** |
| W-03 | CPT `service` registered on `init` | **PASS** — archive `/services/` |
| W-04 | ACF JSON loads | **PASS** — 3 field groups |
| W-08 | No PHP fatals on front routes | **PASS** — HTTP 200 on key URLs |

---

## Content model (live)

| Entity | Count / ID | Notes |
|--------|------------|-------|
| CPT `service` | 4 posts | Synthetic fixtures |
| Home page | ID 5 | Front page assigned |
| Contacts page | ID 6 | Static page |
| Primary menu | Assigned | `primary` location |

---

## Theme switch persistence test

| Step | Result |
|------|--------|
| Switch to `twentytwentyfive` | **PASS** |
| Switch back to `fws-synthetic` | **PASS** |
| 4 services persisted | **PASS** |

---

## Route smoke (HTTP 200)

| Route | Result |
|-------|--------|
| `/` (home) | **PASS** |
| `/services/` (archive) | **PASS** |
| `/services/testovaya-usluga/` (single) | **PASS** |
| `/contacts/` | **PASS** |

---

## Verdict

**PASS** — WordPress correctness checks pass on live MLI runtime.

---

## Related

- [FWS-0001-FUNCTIONAL-LIVE-VALIDATION-v1.md](FWS-0001-FUNCTIONAL-LIVE-VALIDATION-v1.md)
- [FWS-0001-FW-V-03-WORDPRESS-CORRECTNESS-LIVE-v1.md](FWS-0001-FW-V-03-WORDPRESS-CORRECTNESS-LIVE-v1.md)

---

*WordPress correctness live validation v1 — FWS-0001.*
