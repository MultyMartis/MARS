# SITE-001 W4.1 Header & Hero Authority Change Request v1

**Change request ID:** CR-SITE-001-W4-1-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** W4 Used PDP baseline · `pre-w4-1-stable-*`

---

## Summary

Header & hero authority slice: unified premium header shell, red usage discipline, integrated promo strip, used PDP top authority band. Preserves W4 Used PDP structural work.

## Objective

Make first screen look more modern and authoritative — target 7/10 visual impact on homepage and used PDP without content/structure regression.

## Scope

| Phase | Target |
|-------|--------|
| W4.1-A | Unified header shell — sticky, single shadow, toolbar/nav seam |
| W4.1-B | Red discipline — primary CTA only; demote logo/phone red noise |
| W4.1-C | Promo strip — graphite integrated band, not legacy red ticker |
| W4.1-D | Used PDP top — breadcrumbs + H1 authority wrapper |
| W4.1-E | Catalog/inner page top rhythm |

## Files

- `catalog/view/theme/auto/template/common/header.twig`
- `catalog/view/theme/auto/template/product/product.twig`
- `css/main.css`
- `css/media.css`

## Baseline

W4 Used PDP + W3UX-C1 + W3ATMOSPHERE on TEST

## Backup

`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w4-1-stable-YYYYMMDD-HHMM\`

## Risk

Medium — header affects all pages; mitigated by class-scoped CSS + minimal twig class additions + pre-write stable backup

## Rollback

T1 — restore from `pre-w4-1-stable-*`; clear caches. See [SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/` | Header modern; nav/callback present |
| `/about` | Header usable; no regression |
| `/contact/` | Forms present |
| `/cars/` | Catalog renders; promo strip present |
| `/cars/bmw/` | Brand catalog OK |
| `/auto/` · `/auto/haval/` | New catalog OK |
| `/audi-a1-2012-s-probegom-149-000-km-799` | W4 preserved + W4.1 PDP top |
| `/baic-bj40-new` | New PDP header OK |
