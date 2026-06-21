# SITE-001 WF-V2-W2 Flat PDP Change Request v1

**Change request ID:** CR-SITE-001-WFV2-W2-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Baseline:** WF-V2-W1 Hybrid Header + W5-C Used PDP Commercial Stage  
**Stable backup reference:** `pre-w5c-commercial-stage-20260610-0002`

---

## Summary

Subtract visual noise from Used PDP: flatten W5-C commercial stage surfaces, restore price authority, simplify trust/spec/equipment/credit zones — twig hook + scoped CSS overrides only.

## Objective

Move Used PDP from «card-in-card OpenCart dealer widgets» to «clean automotive showroom stage» per WF V2 concept mock `01` and subtractive principles spec `02`.

## Scope

| Phase | Target |
|-------|--------|
| W2-A | Hero flattening — reduce container hierarchy, borders, separators |
| W2-B | Price authority — increase price dominance; demote discount/credit chrome |
| W2-C | Trust strip — single band; preserve statuses + VIN CTA |
| W2-D | Specs — grid with dividers, not boxed tiles |
| W2-E | Equipment — reduce boxes/separators; keep columns |
| W2-F | Credit — reduce nesting and framing; preserve calculator/submit/legal |
| W2-G | Global noise reduction — no new effects |

## Files

- `catalog/view/theme/auto/template/product/product.twig`
- `css/main.css`
- `css/media.css`

## Baseline

WF-V2-W1 Hybrid Header + W5-C + W4 Used PDP + W5-A/S + W3*

## Backup

`pre-wfv2-w2-flat-pdp-YYYYMMDD-HHMM` — created at pre-write

## Risk

Medium — W5-C surface reversal may collapse hierarchy if overrides too aggressive; mitigated by scoped `.wfv2-flat-pdp` + pre-write backup + 8-URL matrix + before/after screenshots.

## Rollback

T1 — restore 3 deploy files from `pre-wfv2-w2-flat-pdp-*`; clear caches. See [SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | W2 flat markers + W5-C/W4 preserved |
| `/`, `/about`, `/contact/` | Hybrid header; no W2 leak |
| `/cars/`, `/cars/bmw/` | No W2 leak |
| `/auto/`, `/auto/haval/` | No W2 leak |

## Authorization

Operator WF-V2-W2 Flat PDP task brief 2026-06-10 — **APPROVED for TEST execution**.
