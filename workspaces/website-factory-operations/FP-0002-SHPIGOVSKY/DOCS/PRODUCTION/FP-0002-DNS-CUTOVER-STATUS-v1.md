# FP-0002 — DNS Cutover Status v1

**Wave:** PROD-P02 · **updated P17-FU02** (internal tails closed; still no NS write)  
**Date:** 2026-08-18 (FU02)  
**Status:** **`DNS_CUTOVER = DEFERRED`** — READY FOR MANUAL NS SWITCH; NS **not** switched

---

| Field | Value |
|-------|-------|
| Current working host | `http://shpigovsky.beget.tech/` |
| Future canonical domain | `shpigovsky.ru` |
| DNS for `shpigovsky.ru` | Still on **REG.RU hosting NS** `ns1.hosting.reg.ru` / `ns2.hosting.reg.ru` (P17 inventory) |
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

## P17 CONT1

Public zone inventoried. Target Beget NS recorded from published KB (panel confirm still required). **No NS write. No SSL. No siteurl.**

Evidence: `REPORTS/evidence/prod-p17-precutover/`

## This wave (historical P02 note)

P02: No DNS, SSL, robots, or redirect mutations.  
P17 CONT1: legacy path 301s on the temporary host only; DNS remains deferred.

---

*DNS Cutover Status v1 · PROD-P02.*
