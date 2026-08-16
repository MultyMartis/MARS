# FP-0002 — DNS Cutover Status v1

**Wave:** PROD-P02  
**Date:** 2026-08-13  
**Status:** **`DNS_CUTOVER = DEFERRED`**

---

| Field | Value |
|-------|-------|
| Current working host | `http://shpigovsky.beget.tech/` |
| Future canonical domain | `shpigovsky.ru` |
| DNS for `shpigovsky.ru` | Still on **old hosting** (operator-confirmed in PROD-P01) |
| Beget as canonical public host | **NO** until cutover charter |
| SSL / HTTPS on beget.tech | SAFE UNKNOWN / not usable in P01 probe |
| Agent DNS writes | **FORBIDDEN** |
| Redirects beget.tech → shpigovsky.ru | **FORBIDDEN** now |
| `siteurl` / `home` change to final domain | **FORBIDDEN** until cutover charter |

---

## Risks (unchanged from P01)

- Temporary host is publicly crawlable.  
- Dual public presence until cutover.  
- Site title still contains «локальная разработка».  
- Some hardcoded `shpigovsky.test` CTA links remain (content residue; not repaired here).

---

## This wave

No DNS, SSL, robots, or redirect mutations.

---

*DNS Cutover Status v1 · PROD-P02.*
