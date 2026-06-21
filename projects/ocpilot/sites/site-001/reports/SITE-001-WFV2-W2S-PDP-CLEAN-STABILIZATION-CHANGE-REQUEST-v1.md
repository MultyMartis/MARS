# SITE-001 WF-V2-W2S PDP Clean Stabilization Change Request v1

**Change request ID:** CR-SITE-001-WFV2-W2S-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Baseline:** WF-V2-W1 Hybrid Header + WF-V2-W2 Flat PDP  
**Stable backup reference:** `pre-wfv2-w2-flat-pdp-20260610-0304`

---

## Summary

Stabilize WF-V2-W2 Used PDP: refine composition, price hierarchy, specs/trust/equipment/credit zones — twig hook + scoped CSS composition layer only. Not a new design wave.

## Objective

Move Used PDP from «flattened but fragmented» to «clean automotive showroom stage» per WF V2 concept mock `01` and subtractive principles spec `02`.

## Scope

| Phase | Target |
|-------|--------|
| W2S-A | Hero composition — align gallery/offer; remove empty zones and nested-box feeling |
| W2S-B | Price / offer — price anchor; clean discount rows; CTA tied to price |
| W2S-C | Specs — unified facts grid; easier scan |
| W2S-D | Trust strip — calm proof line; even statuses; VIN in row |
| W2S-E | Equipment — spec sheet scan; reduce line noise |
| W2S-F | Credit — connected section; reduce black-box heaviness |
| W2S-G | Noise purge — borders, dividers, nested layers, red accents |

## Files

- `catalog/view/theme/auto/template/product/product.twig`
- `css/main.css`
- `css/media.css`

## Baseline

WF-V2-W1 + WF-V2-W2 + W5-C + W4 Used PDP + W5-A/S + W3*

## Backup

`pre-wfv2-w2s-pdp-clean-YYYYMMDD-HHMM` — created at pre-write

## Risk

Low–medium — composition refinements atop W2; mitigated by scoped `.wfv2-clean-pdp` + pre-write backup + 8-URL matrix + before/after screenshots.

## Rollback

T1 — restore 3 deploy files from `pre-wfv2-w2s-pdp-clean-*`; clear caches. See [SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | W2S clean markers + W2/W5-C/W4 preserved |
| `/`, `/about`, `/contact/` | Hybrid header; no W2S leak |
| `/cars/`, `/cars/bmw/` | No W2S leak |
| `/auto/`, `/auto/haval/` | No W2S leak |

## Authorization

Operator WF-V2-W2S PDP Clean Stabilization task brief 2026-06-10 — **APPROVED for TEST execution**.
