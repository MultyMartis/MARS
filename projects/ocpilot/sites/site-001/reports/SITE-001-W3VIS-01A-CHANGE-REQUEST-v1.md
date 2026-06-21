# SITE-001 W3VIS-01A Change Request v1

**Change request ID:** CR-SITE-001-W3VIS-01A-2026-06  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Summary

Создать систему поверхностей и визуальную иерархию на PDP (used + new): единый hero L2, demotion discount/VIN/credit, доминирующая цена и primary CTA — **CSS-only**, без изменения layout/контента/Twig.

## Scope

| Task | Change |
|------|--------|
| A1 | Unified L2 hero surface (gallery + offer column) |
| A2 | Discount widget → L3 nested strip |
| A3 | CTA action zone — primary red / secondary outline |
| A4 | Price hierarchy — 36px/600 dominant |
| A5 | VIN block → supportive outline action |
| A6 | Credit calculator → light L2 panel, not second hero |

## Files

- `css/main.css` — append W3VIS-01A block after W3V2
- `css/media.css` — responsive overrides

## Risk

**Low** — scoped PDP selectors with `.used_car_page` / `.new_car_page` prefixes; T1 rollback from backup.

## Rollback plan (T1)

| Step | Action |
|------|--------|
| 1 | Locate backup `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3vis-01a-YYYYMMDD-HHMM\` |
| 2 | FTP STOR `css/main.css` from `css__main.css` |
| 3 | FTP STOR `css/media.css` from `css__media.css` |
| 4 | Clear TEST admin caches (system, modification, image) |
| 5 | Verify live CSS lacks `W3VIS-01A PDP Hero Surface System` marker |

**Alternative:** Remove W3VIS-01A comment blocks from both files (between marker and `END W3VIS-01A`).

## Authorization

Operator W3VIS-01A execution charter — **APPROVED for TEST execution** (2026-06-09).
