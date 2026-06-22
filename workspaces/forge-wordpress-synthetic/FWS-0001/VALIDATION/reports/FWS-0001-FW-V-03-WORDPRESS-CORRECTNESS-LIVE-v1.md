# REPORT — FW-V-03 WordPress Correctness LIVE — FWS-0001

**Validator ID:** FW-V-03  
**Mode:** Live (FW-05R)  
**Version:** v1  
**Date:** 2026-06-23  
**Runtime:** MLI-WP-SYN-001

---

## Verdict

**PASS**

---

## Template / CPT / ACF checks

| ID | Check | Result |
|----|-------|--------|
| W-01 | style.css header | **PASS** |
| W-02 | Template hierarchy | **PASS** |
| W-03 | CPT `service` on init | **PASS** |
| W-04 | ACF JSON sync | **PASS** — 3 groups |
| W-08 | No fatals on front load | **PASS** |

---

## Runtime smoke

| Route | HTTP |
|-------|------|
| `/` | 200 |
| `/services/` | 200 |
| `/services/testovaya-usluga/` | 200 |
| `/contacts/` | 200 |

---

## Related

- [FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md](FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md)
- [FWS-0001-ACF-COMPATIBILITY-LIVE-v1.md](FWS-0001-ACF-COMPATIBILITY-LIVE-v1.md)

---

*FW-V-03 LIVE v1 — FWS-0001.*
