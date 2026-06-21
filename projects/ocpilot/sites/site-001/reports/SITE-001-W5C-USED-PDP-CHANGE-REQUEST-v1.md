# SITE-001 W5-C Used PDP Change Request v1

**Change request ID:** CR-SITE-001-W5C-2026-06-10  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** `pre-w5c-commercial-stage-20260610-0002`

---

## Summary

Advance used PDP from W4 **structural slice** to W5-C **commercial offer stage**: unified hero scene, commercial price hierarchy, trust proof cards, equipment spec sheet, premium credit panel, modern modals — twig wrappers + scoped CSS only.

## Objective

Turn used PDP from «OpenCart product page» into «modern dealership vehicle offer page» per W5 Blueprint Concept B §Used PDP first screen.

## Scope

| Phase | Target |
|-------|--------|
| W5-C-A | Commercial stage shell — badges + hero + trust as one deck |
| W5-C-B | Gallery showroom strength — 480px crop |
| W5-C-C | Price commercial center — 52px anchor, credit side card, discount mini-cards |
| W5-C-D | Spec grid inside stage panel |
| W5-C-E | CTA commercial bar — 3-col grid |
| W5-C-F | Trust proof strip — 4-col cards, solid VIN CTA |
| W5-C-G | Equipment spec sheet — 3-col scan grid |
| W5-C-H | Credit panel — white inset form card |
| W5-C-I | PDP modals — light modern shell (`body.used_car_page` scoped) |

## Files

- `catalog/view/theme/auto/template/product/product.twig`
- `css/main.css`
- `css/media.css`

## Baseline

W5-A-S stabilization + W4 Used PDP + W4.1 PDP top + W3UX-C1 + W3ATMOSPHERE

## Backup

`pre-w5c-commercial-stage-20260610-0002` — **DONE** 2026-06-10

## Risk

Low–medium — twig wrapper only; modal CSS scoped to used PDP body class; mitigated by pre-write backup + 8-URL regression matrix.

## Rollback

T1 — restore 3 deploy files from `pre-w5c-commercial-stage-20260610-0002`; clear caches. See [SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | W5-C markers + W4 preserved |
| `/`, `/about`, `/contact/` | W5-A header; no W5-C leak |
| `/cars/`, `/cars/bmw/` | No W5-C leak |
| `/auto/`, `/auto/haval/` | No W5-C leak; new PDP unchanged |

## Authorization

Operator W5-C task brief 2026-06-10 — **APPROVED for TEST execution**.
