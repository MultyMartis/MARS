# SITE-001 W3VIS-01B Change Request v1

**Change request ID:** CR-SITE-001-W3VIS-01B-2026-06  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Baseline:** post-W3VIS-01A

---

## Summary

Усилить **commercial attention hierarchy** на PDP (used + new): доминирующая цена, primary CTA после цены, demotion support-виджетов (discount, specs, VIN, credit) — **CSS-only**, без изменения layout/контента/Twig.

## Scope

| Task | Change |
|------|--------|
| B1 | Price 44px/700, L3 zone, strongest contrast in right column |
| B2 | Primary CTA 52px/shadow at rest; secondary outline; tertiary text-link |
| B3 | Single dominant pair (price + CTA); support widgets flat |
| B4 | VIN → trust element, text-link action, no card chrome |
| B5 | Specs 13px compressed rows, muted scan list |
| B6 | L1–L5 surface stack; CSS flex `order` for CTA before specs |

## Files

- `css/main.css` — append W3VIS-01B block after W3VIS-01A
- `css/media.css` — responsive overrides

## Risk

**Low** — scoped `.used_car_page` / `.new_car_page` selectors; T1 rollback from `pre-w3vis-01b-*` backup.

## Rollback plan (T1)

| Step | Action |
|------|--------|
| 1 | Locate backup `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3vis-01b-YYYYMMDD-HHMM\` |
| 2 | FTP STOR `css/main.css` from `css__main.css` |
| 3 | FTP STOR `css/media.css` from `css__media.css` |
| 4 | Clear TEST admin caches (system, modification, image) |
| 5 | Verify live CSS lacks `W3VIS-01B PDP Commercial Authority` marker |

**Alternative:** Remove W3VIS-01B comment blocks from both files (between marker and `END W3VIS-01B`).

## Authorization

Operator W3VIS-01B execution charter — **APPROVED for TEST execution** (2026-06-09).
