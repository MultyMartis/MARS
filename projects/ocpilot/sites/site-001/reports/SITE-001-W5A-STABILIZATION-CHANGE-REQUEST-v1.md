# SITE-001 W5-A Stabilization Pass Change Request v1

**Change request ID:** CR-SITE-001-W5A-STAB-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** W5-A PARTIAL PASS · W5-B **BLOCKED**

---

## Summary

Stabilization fix pass on W5-A header shell. Address operator findings: promo overlap, broken «Услуги» dropdown, crowded navigation at 1280px, responsive shell risk. **No redesign.**

## Objective

W5-A reaches production-clean header shell on TEST; W5-B unblocked after operator visual HITL.

## Scope

| Task | Fix |
|------|-----|
| W5-A-S-A | Dropdown recovery — remove nav-group clipping; z-index; faster transition |
| W5-A-S-B | Promo integration — flush sibling inset; zero margin-top collision |
| W5-A-S-C | Nav density — «Ещё» dropdown (Спецпредложения · Акции · Отзывы · Об автосалоне); tighter grid/gaps |
| W5-A-S-D | Responsive block — 1600 / 1440 / 1280 / 1024 / 768 / 390 |
| W5-A-S-E | Interaction verification — logo · links · CTAs · dropdowns · offcanvas |

## Files

- `catalog/view/theme/auto/template/common/header.twig`
- `css/main.css`
- `css/media.css`

## Baseline

W5-A on TEST (`pre-w5a-header-shell-20260609-2251` remains prior rollback)

## Backup

`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w5a-stabilization-YYYYMMDD-HHMM\`

## Risk

**Low–medium** — CSS + nav DOM grouping only; all URLs preserved; mitigated by backup + 8-URL matrix + Playwright audits

## Rollback

T1 — restore from `pre-w5a-stabilization-*`; clear caches. Full W5-A rollback remains `pre-w5a-header-shell-20260609-2251`.

## Verification URLs

| URL | Expect |
|-----|--------|
| `/` | Shell; «Ещё» nav; no sticky |
| `/about` | Shell; dropdowns |
| `/contact/` | Forms |
| `/cars/` | Promo inset flush below header |
| `/cars/bmw/` | Brand catalog |
| `/auto/` | New catalog |
| `/auto/haval/` | Brand catalog |
| `/audi-a1-2012-s-probegom-149-000-km-799` | W4 markers preserved |
