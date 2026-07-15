# FP-0002 accepted local state — E29C → E35-FIX01

**Timestamp:** 2026-07-13 03:25:49 (+07)  
**Runtime:** `http://shpigovsky.test` (`X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`)  
**DB:** `mars_wp_fp0002` (prefix `fp02_`)  
**Source authority:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`  
**Persistence backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29c-e35-fix01-persistence-before-20260713-032549\`  
**Evidence export:** `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-persistence\v9-06e29c-e35-fix01-20260713-032549\`

This document describes the **accepted local WordPress runtime**. It does **not** claim production deployment or hosting sync.

## Stage stack (operator-accepted)

| Stage | Summary | Report |
|---|---|---|
| E29C | Excel structure completion / generic pages / favicon / service deep routes | `REPORTS/REPORT-FP-0002-V9-06E29C-excel-structure-completion-generic-pages-favicon.md` |
| E30 | Services catalog hierarchy + display controls | `REPORTS/REPORT-FP-0002-V9-06E30-services-catalog-child-services-listing-controls.md` |
| E31 | Program pages / direction links / service admin validation relax | `REPORTS/REPORT-FP-0002-V9-06E31-program-pages-direction-links-validation-relax.md` |
| E32 | Home services accordion + Home gallery service links + placeholder | `REPORTS/REPORT-FP-0002-V9-06E32-home-services-accordion-gallery-service-placeholder.md` |
| E33 | Service image admin binding + placeholder fix + `/uslugi/` slider | `REPORTS/REPORT-FP-0002-V9-06E33-service-image-admin-binding-placeholder-uslugi-slider.md` |
| E33-FIX01 | `/uslugi/` sliders match Home gallery (dots, no prev/next) | `REPORTS/REPORT-FP-0002-V9-06E33-FIX01-uslugi-sliders-match-home-gallery.md` |
| E34 | Specialists child pages + automatic specialists slider | `REPORTS/REPORT-FP-0002-V9-06E34-specialists-child-pages-auto-slider.md` |
| E35 | Specialist no-photo + 5 demo posts + Home articles real posts slider | (runtime/DB; see E35-FIX01 + inventories) |
| E35-FIX01 | Restore alcohol article thematic featured image | `REPORTS/REPORT-FP-0002-V9-06E35-FIX01-alcohol-article-image-restore.md` |

## Accepted facts (validated in this persistence wave)

### Services / `/uslugi/`

- `/uslugi/` HTTP 200
- Genotyping removed from services catalog; `/uslugi/genotipirovanie/` expected 404
- Category markers sequential; category sliders use Swiper dots (no prev/next) per E33-FIX01
- Service cards clickable; service image admin binding + placeholder present
- Canonical internet service slug: `internet-zavisimost`
- Duplicate `lechenie-internet-zavisimosti` expected 404 under `/uslugi/zavisimosti/`

### Program pages (`/o-centre/programma-lecheniya/`)

- `genotipirovanie`, `neyropsihologicheskaya-korrektsiya`, `psihokorrektsiya`, `kinezioterapiya` — published pages, generic template

### Home

- Services accordion from service CPT tree
- Gallery = clickable service slides
- Articles from real WP posts; slider dots / no prev-next
- Rehabilitation program direction links → program pages

### Specialists

- Children: `shipovsky`, `kazakov`, `kostyuk`, `shapiguzova`
- Slider auto from child pages; Shapiguzova uses no-photo placeholder

### Blog

- Alcohol article `/blog/nazvanie-stati/` featured → `article-alcohol-dependence.webp` (attachment `#1106`)
- Five E35 demo posts published with blog no-photo placeholder

## Evidence artefacts

| File | Location |
|---|---|
| Route smoke | `route-smoke.csv` (32/32 PASS) |
| Inventories | `pages-inventory.csv`, `services-inventory.csv`, `program-pages.csv`, `specialists-pages.csv`, `blog-posts.csv`, `media-attachments-summary.csv`, `trashed-objects-summary.csv` |
| Small source copy | `WORDPRESS/validation/v9-06e29c-e35-fix01-selective-persistence/` |

## Explicit non-claims

- No production hosting mutation
- No push
- Foreign monorepo WIP excluded from Git persistence
