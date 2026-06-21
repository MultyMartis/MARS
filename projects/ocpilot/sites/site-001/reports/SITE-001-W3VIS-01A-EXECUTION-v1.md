# SITE-001 W3VIS-01A Execution v1

**Type:** Execution report — W3VIS-01A PDP Hero Surface System  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W3VIS-01A-2026-06  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Executive summary

W3VIS-01A выполнен на TEST: **CSS-only** PDP hero surface system — unified L2 hero, L3 discount strip, CTA/price hierarchy, VIN + credit demotion. FTP upload, cache clear, **9/9 URL verification PASS**, live CSS marker confirmed.

**Evidence (local, not git):** `.recovery-temp/site-001-w3vis-01a-result.json` · screenshots `projects/ocpilot/sites/site-001/qa/w3vis-01a-screenshots/`

---

## 1. Pre-execution

| Step | Status |
|------|--------|
| Discovery | [SITE-001-W3VIS-01A-DISCOVERY-v1.md](SITE-001-W3VIS-01A-DISCOVERY-v1.md) — **DONE** |
| Write charter | [SITE-001-W3VIS-01A-WRITE-CHARTER-v1.md](SITE-001-W3VIS-01A-WRITE-CHARTER-v1.md) — **ACTIVE** |
| Change request | CR-SITE-001-W3VIS-01A-2026-06 |
| Rollback plan | T1 in [SITE-001-W3VIS-01A-CHANGE-REQUEST-v1.md](SITE-001-W3VIS-01A-CHANGE-REQUEST-v1.md) |
| Backup | `pre-w3vis-01a-20260609-0517` — **DONE** |

---

## 2. Files modified

| Remote path | Pre (bytes/lines) | Post (bytes/lines) | Change |
|-------------|-------------------|---------------------|--------|
| `css/main.css` | 118 851 / 7 418 | 126 979 / 7 756 | W3VIS-01A block (+338 lines) |
| `css/media.css` | 31 485 / 2 249 | 32 669 / 2 301 | W3VIS-01A responsive (+52 lines) |

**Rollback marker:** `SITE-001 W3VIS-01A PDP Hero Surface System` in both files.

---

## 3. Tasks applied

| Task | Implementation |
|------|----------------|
| **A1** | `.used_car_page .car_main_info` — L2 card shell; internal column split; `.newcar_newDesign` + `.new_car_NEW__wrapper` — L2 on new PDP |
| **A2** | `.car_main_info__discount` — alt L3 surface, reduced padding/type, no white island border |
| **A3** | `.car_main_info__btns` action band; primary red + CTA shadow; secondary outline graphite; fixed shared red hover |
| **A4** | Price 36px/600; old/credit muted tiers; specs 14px secondary |
| **A5** | `.car_vin_check` — light panel; title 18px; green outline button 44px |
| **A6** | `.used_car__credit` — light panel, no bg image; calculator on alt L3 inset |

**Tokens added:** `--vis-border-subtle`, `--vis-hero-pad`, `--vis-hero-pad-sm`

---

## 4. Verification matrix

| # | Label | URL | HTTP | Pass |
|---|-------|-----|------|------|
| 1 | homepage | `/` | 200 | **PASS** |
| 2 | about | `/about` | 200 | **PASS** |
| 3 | contact | `/contact/` | 200 | **PASS** |
| 4 | used_catalog | `/cars/` | 200 | **PASS** |
| 5 | used_brand | `/cars/bmw/` | 200 | **PASS** |
| 6 | new_catalog | `/auto/` | 200 | **PASS** |
| 7 | new_brand | `/auto/haval/` | 200 | **PASS** |
| 8 | used_pdp | `/audi-a1-2012-s-probegom-149-000-km-799` | 200 | **PASS** |
| 9 | new_pdp | `/baic-bj40-new` | 200 | **PASS** |

**Live CSS:** `/css/main.css` — W3VIS-01A marker present — **PASS**

**Screenshots:** desktop/tablet/mobile — used PDP, new PDP, used catalog, homepage (`qa/w3vis-01a-screenshots/`)

---

## 5. Self-review (success criteria)

| Question | Assessment |
|----------|------------|
| PDP reads as one commercial block? | **YES** — single L2 shell on used; new top + config sections unified |
| Price → CTA → specs scan order? | **YES** — price band + action zone at column bottom |
| Layout/content unchanged? | **YES** — CSS-only, no Twig |
| «Дороже без логотипа»? | **YES** (agent) — operator sign-off **PENDING** |

---

## 6. Explicitly not changed

Twig · PHP · JS · DB · SEO · routes · content · header/footer structure · W3UX-C1 used catalog density · W3V2 base tokens

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **EXECUTED** — W3VIS-01A on TEST |
