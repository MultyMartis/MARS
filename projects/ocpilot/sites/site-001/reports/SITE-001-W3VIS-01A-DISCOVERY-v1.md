# SITE-001 W3VIS-01A Discovery v1

**Type:** Pre-execution discovery — PDP hero surface (read-only + live CSS baseline)  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Wave:** W3VIS-01A — PDP Hero Surface System  
**Parent:** [SITE-001-W3VIS-01-DISCOVERY-v1.md](SITE-001-W3VIS-01-DISCOVERY-v1.md)

**Methods:** HTTP probe · live CSS fetch · selector inventory · post-W3V2 baseline  
**Evidence (local, not git):** `.recovery-temp/site-001-w3vis-01-probe.json` · `.recovery-temp/site-001-w3vis-01a-result.json`

---

## Executive summary

PDP hero на used-страницах — **50/50 flex без общей оболочки** (`.car_main_info { margin: -10px }`). Discount widget — **отдельный white island** (padding 30px, border). CTA row — graphite + red одинакового веса; W3V2 hover делает все кнопки красными. VIN и credit — **dark chrome clone** nav/footer.

New PDP (`/baic-bj40-new`) — другая разметка: `.newcar_newDesign` (image + price) + `.new_car_NEW__wrapper` (photo + config); photo box с собственным border.

**Вывод:** CSS-only wrapper на parent + demotion дочерних surfaces достаточен — Twig не требуется.

---

## 1. URL inventory (2026-06-09)

| Surface | URL | HTTP | Body class | Hero selectors |
|---------|-----|------|------------|----------------|
| Homepage | `/` | 200 | — | — |
| About | `/about` | 200 | — | — |
| Contact | `/contact/` | 200 | — | — |
| Used catalog | `/cars/` | 200 | `used_catalog` | — |
| Used brand | `/cars/bmw/` | 200 | `used_catalog` | — |
| New catalog | `/auto/` | 200 | `new_catalog` | — |
| New brand | `/auto/haval/` | 200 | `new_catalog` | — |
| **Used PDP** | `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | `used_car_page` | `.car_main_info`, discount, VIN, credit |
| **New PDP** | `/baic-bj40-new` | 200 | `new_car_page` | `.newcar_newDesign`, `.new_car_main_info` |

**Live CSS baseline:** W3V2 active — ~118 KB `main.css`, marker `W3V2 Visual Identity Refresh`.

---

## 2. Used PDP DOM map

```
.car_main_info                    ← A1 target (L2 wrapper)
├── .car_main_info__photo        ← gallery
└── .car_main_info__main
    ├── .car_main_info__main__top_wrap
    │   └── .car_main_info__price ← A4
    ├── .car_main_info__discount   ← A2
    ├── .car_main_info__characteristics
    └── .car_main_info__btns       ← A3

.car_vin_check                     ← A5 (below hero)
.used_car__credit                   ← A6 (below hero)
```

---

## 3. Baseline CSS findings

| Selector | Issue | W3VIS-01A fix |
|----------|-------|---------------|
| `.car_main_info` | No surface chrome | L2 border/radius/shadow |
| `.car_main_info__discount` | White card, 30px pad | L3 alt surface, no border |
| `.car_main_info__price_main` | 30px/500 | 36px/600 |
| `.car_main_info__btns > a` | Graphite = secondary size | Outline secondary; red primary |
| `.car_main_info__btns > a:hover` | All turn red (W3V2) | Scoped hover override |
| `.car_vin_check` | Dark 50px green CTA | Light panel + outline green |
| `.used_car__credit` | Dark + bg image + 30px title | Light L2 panel, no hero bg |

---

## 4. New PDP map

| Block | Role | Target |
|-------|------|--------|
| `.newcar_newDesign` | Top hero (image + price + timer) | L2 surface |
| `.new_car_NEW__wrapper` | Config + photo | L2 surface |
| `.new_car_main_info__photo` | Bordered white box | Transparent inside L2 |
| `.new_car_main_info__btns` | CTA row | A3 parity |

---

## 5. Cross-wave compatibility

| Active wave | Constraint |
|-------------|------------|
| W3UX-C1 | Do not touch `.used_catalog` rules |
| W3V2 | Append after `END W3V2`; reuse `--w3v2-*` tokens |
| W3-V | Radius/spacing compatible |

---

## 6. Backup requirement

Pre-write backup of `css/main.css` + `css/media.css` to `pre-w3vis-01a-*` before FTP upload.

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3VIS-01A scoped discovery |
