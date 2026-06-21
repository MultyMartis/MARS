# SITE-001 W4 Used PDP Change Request v1

**Change request ID:** CR-SITE-001-W4-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Summary

Controlled **structural-visual slice** on **used car PDP only**: twig wrapper grouping + scoped CSS under `.used_car_page`. Replaces ineffective cosmetic-only waves (W3COLOR / W3ATMOSPHERE / W3WF) for PDP impact.

## Objective

Make used PDP visibly better without whole-site rewrite — hero composition, commercial offer panel, trust strip, equipment scan grid, premium credit panel.

## Scope

| Phase | Target |
|-------|--------|
| W4-A | Status badges — pill chips above hero |
| W4-B | Unified hero shell — single L2 card |
| W4-C | Gallery — edge-to-edge, 440px crop, thumb active ring |
| W4-D | Commercial offer — price 42px, credit pill, demoted discount strip |
| W4-E | Spec grid — 4-col card cells (desktop) |
| W4-F | CTA bar — primary dominance + outline secondaries |
| W4-G | Trust strip — light premium card (not nav clone) |
| W4-H | Equipment — 2-col scan grid in card shell |
| W4-I | Credit panel — inset form on dark gradient |

## Files

- `catalog/view/theme/auto/template/product/product.twig`
- `css/main.css`
- `css/media.css`

## Baseline

Phase 1 Stable Checkpoint + W3-V + W3V2 + W3UX-C1 + W3ATMOSPHERE-01 (cosmetic waves stopped for PDP)

## Backup

`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w4-20260609\` — **DONE** 2026-06-09

## Risk

Medium — first twig structural change since W3-C rollback lesson; mitigated by `.used_car_page` scope + `product.twig` is used-car-only template.

## Rollback

T1 — restore 3 files from `pre-w4-20260609`; clear caches. See [SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | W4 visual PASS |
| `/cars/` | No W4 markup/classes |
| `/cars/bmw/` | No regression |
| `/` | No regression |
| `/about` | No regression |
| `/contact/` | No regression |

## Authorization

Operator W4 task brief 2026-06-09 — **APPROVED for TEST execution**.
