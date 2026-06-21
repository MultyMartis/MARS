# SITE-001 W5-A Header Shell Recomposition Change Request v1

**Change request ID:** CR-SITE-001-W5A-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** W4.1 + W4 Used PDP · W5 Blueprint **APPROVED**

---

## Summary

Header shell recomposition per Concept B: collapse three competing horizontal bands into **one dealer shell** — contact rail + primary band (logo · centered nav · CTA cluster) + **inset promo** via CSS. Revert W4.1 sticky. **Architecture only** — not cosmetics wave.

## Objective

Visitor recognizes **modern dealership** within 3 seconds — without logo, without A/B. Header stops reading as OpenCart `auto` template stack.

## Scope

| Phase | Target |
|-------|--------|
| W5-A-A | **Static header** — full W4.1 sticky rollback |
| W5-A-B | **Contact rail** — hours · address muted · phone/WA compact |
| W5-A-C | **Primary band** — logo anchor · centered nav · unified CTA cluster |
| W5-A-D | **CTA hierarchy** — callback primary · phone secondary · WhatsApp supportive |
| W5-A-E | **Inset promo** — sibling `.lcd_display.header` integrated into shell footer |
| W5-A-F | **Tagline demoted** — hidden from header chrome |

## Files

- `catalog/view/theme/auto/template/common/header.twig`
- `css/main.css`
- `css/media.css`

## Baseline

W4.1 + W4 Used PDP + W3UX-C1 + W3ATMOSPHERE on TEST

## Backup

`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w5a-header-shell-YYYYMMDD-HHMM\`

## Risk

**Medium-high** — header DOM regroup affects all pages; mitigated by pre-write backup · frozen links/content · scoped W5-A CSS block · 8-URL QA matrix

## Rollback

T1 — restore from `pre-w5a-header-shell-*`; clear caches. See [SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md](SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md).

## Verification URLs

| URL | Expect |
|-----|--------|
| `/` | Shell loads; menu; callback; promo; no sticky |
| `/about` | Shell; no Twig errors |
| `/contact/` | Forms; phone |
| `/cars/` | Catalog; promo inset |
| `/cars/bmw/` | Brand catalog |
| `/auto/` · `/auto/haval/` | New catalog |
| `/audi-a1-2012-s-probegom-149-000-km-799` | W4 markers preserved |
