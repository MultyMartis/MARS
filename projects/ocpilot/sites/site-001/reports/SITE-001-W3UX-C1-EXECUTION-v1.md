# SITE-001 W3UX-C1 Execution v1

**Type:** Execution report — W3UX-C1 Used Catalog Card Density  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W3UX-C1-2026-06  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Executive summary

W3UX-C1 executed on TEST: **CSS-only** density optimization for **used catalog cards** (`.used_catalog` scoped). FTP upload of 2 files, cache clear, **5/5 URL verification PASS**. Desktop card height **530 → 403 px (−24%)**; tablet **573 → 434 px (−24%)**. Mobile **451 → 484 px (+7%)** — see N-W3UX-C1-02.

**Evidence (local, not in git):** `.recovery-temp/site-001-w3ux-c1-result.json` · screenshots `sites/site-001/qa/w3ux-c1-screenshots/`

---

## 1. Pre-execution

| Step | Status |
|------|--------|
| Write charter | [SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](SITE-001-W3UX-C1-WRITE-CHARTER-v1.md) — **ACTIVE** |
| Change request | CR-SITE-001-W3UX-C1-2026-06 |
| Discovery | [SITE-001-W3UX-C1-DISCOVERY-v1.md](SITE-001-W3UX-C1-DISCOVERY-v1.md) — **DONE** |
| Backup | `pre-w3ux-c1-20260609-0416` — **DONE** |

---

## 2. Files modified

| Remote path | Pre (bytes/lines) | Post (bytes/lines) | Change |
|-------------|-------------------|---------------------|--------|
| `css/main.css` | 109 454 / 7 015 | 112 140 / ~7 130 | W3UX-C1 block (+~115 lines) · `.used_catalog` scoped |
| `css/media.css` | 30 602 / 2 206 | 31 145 / ~2 220 | Responsive W3UX-C1 block |

**Rollback marker:** `SITE-001 W3UX-C1 Used Catalog Card Density` comment block in both files.

**Pre-write backup:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3ux-c1-20260609-0416\`

---

## 3. Density changes applied

| Area | Changes |
|------|---------|
| **Tokens** | `--w3ux-space-xs/sm/md/lg`, `--w3ux-card-img-max-h: 180px` |
| **Image** | margin-top 30→8px; max-height 180px; object-fit cover |
| **Tags** | padding 15→8px; badge font 12px |
| **Info pad** | 15→10px |
| **Title** | 18px/600; mb 6px; line-height 1.15 |
| **Specs** | mb 6px; li 13px; tighter gap |
| **Price** | **24px/600** — dominant hierarchy |
| **Credit** | mt 8px; mb 0; pt 8px |
| **CTA** | mt 8px; min-height 40px — location unchanged |
| **Scope guard** | All rules under `.used_catalog` |

---

## 4. Upload and cache

| Action | Result |
|--------|--------|
| FTP STOR `css/main.css` | **OK** — 112 140 bytes |
| FTP STOR `css/media.css` | **OK** — 31 145 bytes |
| Cache system clear | HTTP 200 |
| Cache modification clear | HTTP 200 |
| Cache image clear | HTTP 200 |
| Modification refresh | HTTP 200 |

---

## 5. Card height measurements

**Method:** Playwright `getBoundingClientRect()` on first `body.used_catalog .catalog_item` at `/cars/`

| Viewport | Before (px) | After (px) | Change |
|----------|-------------|------------|--------|
| Desktop 1440×900 | 530 | 403 | **−24.0%** |
| Tablet 768×1024 | 573 | 434 | **−24.3%** |
| Mobile 390×844 | 451 | 484 | **+7.3%** |

**Target:** 15–20% reduction — **MET** on desktop and tablet.

---

## 6. Verification matrix

| Label | URL | HTTP | Body class | Forms | Pass |
|-------|-----|------|------------|-------|------|
| used_catalog_root | `/cars/` | 200 | `used_catalog` | yes | **PASS** |
| used_catalog_bmw | `/cars/bmw/` | 200 | `used_catalog` | yes | **PASS** |
| used_catalog_audi | `/cars/audi/` | 200 | `used_catalog` | yes | **PASS** |
| new_catalog_control | `/auto/` | 200 | `new_catalog` | yes | **PASS** |
| homepage_control | `/` | 200 | — | yes | **PASS** |

**CSS live check:** `/css/main.css` — W3UX-C1 block present · `.used_catalog` scope present — **PASS**

**Summary:** **5/5** pages · **overall PASS**

---

## 7. Screenshots

**Location:** `projects/ocpilot/sites/site-001/qa/w3ux-c1-screenshots/`

| File | Description |
|------|-------------|
| `before-desktop-cars-catalog.png` | `/cars/` viewport before |
| `after-desktop-cars-catalog.png` | `/cars/` viewport after |
| `before-desktop-card-first.png` | Single card before (530 px) |
| `after-desktop-card-first.png` | Single card after (403 px) |
| `before-tablet-*` / `after-tablet-*` | Tablet equivalents |
| `before-mobile-*` / `after-mobile-*` | Mobile equivalents |

---

## 8. Regression checks

| Check | Result |
|-------|--------|
| Layout breaks | **None** — all routes HTTP 200 |
| Overflow / clipped text | **None flagged** (automated) |
| Broken images | **None** — object-fit cover applied |
| New catalog unchanged | **PASS** — `/auto/` control |
| Homepage unchanged | **PASS** — no `used_catalog` body |
| Header/footer/twig | **Unchanged** |
| JS / forms / filters | **Present** on all probed pages |
| Production | **Not touched** |

---

## 9. Notes

| ID | Note |
|----|------|
| N-W3UX-C1-01 | Sparse inventory on `/cars/` root — `/cars/audi/` richer for manual spot-check |
| N-W3UX-C1-02 | Mobile card +7% taller — single-column layout; image max-height trade-off; operator mobile review recommended |
| N-W3UX-C1-03 | T1 rollback = restore 2 files from `pre-w3ux-c1-20260609-0416` |

---

## 10. Rollback readiness

| Tier | Ready |
|------|-------|
| T1 — restore 2 CSS files | **YES** — `pre-w3ux-c1-20260609-0416` |
| T2 — full TEST restore | Per Phase 1 checkpoint |
| T3 — halt | Standard procedure |
