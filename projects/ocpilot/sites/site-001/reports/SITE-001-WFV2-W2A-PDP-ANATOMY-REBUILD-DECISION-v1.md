# SITE-001 WF-V2-W2A PDP Anatomy Rebuild Decision v1

**Type:** Post-execution decision — WF V2 Wave 2-A  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST — `https://sibcar.new-site.space/`  
**Execution:** [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-EXECUTION-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-EXECUTION-v1.md)

---

## Decision summary

| Gate | Result |
|------|--------|
| Scope compliance (anatomy only, no cosmetic pass) | **PASS** |
| Allow-list files only | **PASS** |
| 8/8 URL verification | **PASS** |
| PDP anatomy order (C-08..C-11) | **PASS** |
| Modal functional | **PASS** |
| Header/catalog/homepage untouched | **PASS** |
| Automated overall | **PASS WITH NOTES** |

**Wave status:** **COMPLETE ON TEST** — pending operator visual HITL.

---

## Success criteria review

| # | Criterion | Evidence | Result |
|---|-----------|----------|--------|
| 1 | Commercial stage = one object | `wfv2-anatomy-pdp` wraps identity+hero+trust | **PASS** |
| 2 | H1 inside stage | Single H1 in identity row; no pdp-top title | **PASS** |
| 3 | Trust part of scene | `wfv2-pdp-trust-line` inside commercial stage | **PASS** |
| 4 | Equipment + Credit one zone | `wfv2-pdp-layer3` 60/40 grid | **PASS** |
| 5 | Reviews after Layer 3 | `wfv2-pdp-reviews-zone` follows layer3 in DOM | **PASS** |
| 6 | No duplicate car photo in credit | `used_car__credit__slider` removed | **PASS** |
| 7 | Showroom page read vs OC card | Structural shift complete; visual HITL pending | **PENDING** |

---

## Composition audit items

| ID | Requirement | Result |
|----|-------------|--------|
| C-01 | H1 in commercial stage | **PASS** |
| C-03 | Stage = identity + hero + trust | **PASS** |
| C-08 | lcd_display not between hero and equipment | **PASS** (below reviews) |
| C-09 | Equipment + Credit side-by-side desktop | **PASS** |
| C-10 | Reviews after Equipment+Credit | **PASS** |
| C-11 | No credit car image duplicate | **PASS** |

---

## Notes (N-W2A)

| ID | Note | Severity |
|----|------|----------|
| N-W2A-01 | First deploy produced partial twig; fixed in same session using backup `0356` | **Medium** — resolved |
| N-W2A-02 | Rollback anchor = backup `0356` (clean pre-W2A), not `0401` (intermediate live) | **Info** |
| N-W2A-03 | PDP Composition Audit doc not found as repo artefact — mandate items applied directly | **Info** |
| N-W2A-04 | Operator 3-second showroom perception test | **PENDING** |

---

## Authorization

| Action | Status |
|--------|--------|
| WF-V2-W2A on TEST | **DONE** |
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

---

## Rollback reference

T1: restore from `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0356` — see [ROLLBACK-PLAN](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md).

---

## Operator HITL checklist

1. Open used PDP desktop — confirm H1+status+gallery+offer read as one stage  
2. Scroll — Equipment and Credit appear side-by-side (desktop)  
3. Confirm reviews appear **after** equipment+credit block  
4. Confirm no car photo in credit column  
5. Confirm promo ticker not interrupting hero→equipment path  
6. Repeat on tablet (834px) and mobile (390px)  

*SITE-001 WF-V2-W2A PDP Anatomy Rebuild Decision v1*
