# SITE-001 W3VIS-01B Discovery v1

**Type:** Pre-execution discovery — PDP commercial hierarchy (read-only + live CSS baseline)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Wave:** W3VIS-01B — PDP Commercial Authority  
**Parent:** [SITE-001-W3VIS-01A-EXECUTION-v1.md](SITE-001-W3VIS-01A-EXECUTION-v1.md)

**Methods:** HTTP probe · live CSS fetch · selector inventory · post-W3VIS-01A baseline  
**Evidence (local, not git):** `.recovery-temp/site-001-w3vis-01b-probe.py` · `.recovery-temp/site-001-w3vis-01b-result.json`

---

## Executive summary

После W3VIS-01A PDP стал **единым блоком**, но commercial score остаётся **~4/10**: цена 36px не доминирует, CTA band внизу колонки (после specs), discount/VIN/credit конкурируют с conversion zone, все кнопки визуально близки по весу.

**Вывод:** CSS-only усиление иерархии + flex `order` на `.car_main_info__main` (column) достаточно для eye path Photo → Price → CTA → Specs без Twig.

---

## 1. URL inventory (2026-06-09)

| Surface | URL | HTTP | Body class | Notes |
|---------|-----|------|------------|-------|
| **Used PDP** | `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | `used_car_page` | 3 CTA: main + 2× modalbox |
| **New PDP** | `/baic-bj40-new` | 200 | `new_car_page` | `.newcar_newDesign` + config CTAs |

**Live CSS baseline:** W3VIS-01A active — 126 979 bytes `main.css`, marker `W3VIS-01A PDP Hero Surface System`. W3VIS-01B absent pre-write.

---

## 2. Used PDP — commercial gap analysis

| Element | Post-01A state | 01B gap |
|---------|----------------|---------|
| Price | 36px/600 in alt band | Not first visual object after photo; credit price still secondary-competing |
| CTA row | Bottom of column (after specs) | Wrong scan order; equal-weight secondary buttons |
| Discount | L3 alt surface 14px pad | Still reads as offer block |
| Specs | 14px rows | Fights CTA zone visually |
| VIN | Light card + outline green btn | Still reads as purchase area |
| Credit | Light L2 panel, 22px title | Second hero competitor |

**DOM order (unchanged):** top_wrap → discount → characteristics → btns  
**Target visual order:** top_wrap → **btns** → discount → characteristics (CSS `order`)

---

## 3. CTA button inventory (used PDP)

| # | Class | Role (01B) |
|---|-------|------------|
| 1 | `car_main_info__btns_main` | L4 Primary — Купить в кредит |
| 2 | `modalbox` (nth 2) | Secondary outline |
| 3 | `modalbox` (nth 3+) | Tertiary text-link |

No dedicated `btns_second` / `btns_text` classes — tier via `:nth-child`.

---

## 4. New PDP map

| Block | 01B target |
|-------|------------|
| `.newcar_newDesign__DIV` | L3 price zone + red accent |
| `.new_car_main_info__btns` | L4 CTA band |
| `.second_phone` | Tertiary text-link |
| `.newcar_config__item_main > .btns` | Config primary/secondary parity |

---

## 5. Cross-wave compatibility

| Active wave | Constraint |
|-------------|------------|
| W3VIS-01A | Append after `END W3VIS-01A`; override 01A rules where needed |
| W3UX-C1 | Do not touch `.used_catalog` |
| W3V2 | Reuse `--w3v2-*` tokens |

---

## 6. Backup requirement

Pre-write backup of `css/main.css` + `css/media.css` to `pre-w3vis-01b-*` (baseline = post-01A).

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3VIS-01B scoped discovery |
