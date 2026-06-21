# REPORT — BZPM STATE FREEZE + ROADMAP UPDATE

**Program:** BZPM Product Roadmap  
**Site:** SITE-002 (ЗПМ) TEST — https://zpm.new-site.space/  
**Task:** Authority state freeze after M9.7D + M9.8 roadmap registration  
**Execution UTC:** 2026-06-17  
**Mode:** Documentation only — **no** site code · **no** DB · **no** TEST deploy · **no** production · **no** commit · **no** push

---

## 1. Documents updated

| File | Change |
|------|--------|
| [site-passport.md](../site-passport.md) | Authority → `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI`; MANUAL UI CANONICAL policy; project status; M9.8 active stage |
| [README.md](../README.md) | Active checkpoint, authority policy, completed phases, M9.8 roadmap link, EC-01 open bug |
| [OCPILOT-STATE.md](../../../OCPILOT-STATE.md) | SITE-002 section rewritten; evidence cutoff 2026-06-17 |
| [BZPM-PRODUCT-ROADMAP-v1.md](../../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) | OCPilot delivery track; M9.8 UX Polish Pack (M9.8.1–M9.8.8); current state; change log |
| [REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md](REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md) | This report |

**Source documents read (not modified):**

- [SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md)
- [SITE-002-STABLE-M9-COMPLETE.md](SITE-002-STABLE-M9-COMPLETE.md)
- [REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md](REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md)
- [REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md](REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md)
- [REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md](REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md)

---

## 2. New authority state

| Field | Value |
|-------|-------|
| **Checkpoint** | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| **Environment** | TEST only — https://zpm.new-site.space/ |
| **Baseline folder** | `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI/` |
| **QA (at capture)** | 26 pass · 0 fail · 0 warn |
| **Policy** | **MANUAL UI REFINEMENTS ARE CANONICAL** |

### What is canonical

- Current TEST site state as captured post M9.7C + **operator manual CSS** (`assets/css/style.css`, `style.min.css`, `sd.css`)
- Operator manual Twig/UX refinements on live FTP (not restored from pre-manual backups)
- M9 filter profiles, M9.5 hub, M9.7C megamenu/image layer where present in baseline capture

### Conflict rule

If any M9.x documentation contradicts current TEST state → **source of truth** = `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` (live FTP capture + baseline folder).

### Historical (not authority label)

| Checkpoint | Role |
|------------|------|
| `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE` | Historical capture — homepage 5-branch deploy evidence |
| `SITE-002-STABLE-M9-COMPLETE-20260615` | Pre-M9.7D / pre-manual UI rollback only |
| `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` | Pre-M9 rollback |

---

## 3. Project status (BZPM)

### Завершено

| Phase | Notes |
|-------|-------|
| M7.1 Launch Mode | Neutral Equipment launch scope on TEST |
| M8 Cleanup | Wave 1 DB + Wave 2 attribute visibility |
| M9 Filter Profiles | 301 / 80 / 322 / 207 / 326 + global_hidden |
| M9.5 Hub Mode | Category 79 hub — 5 branch cards |
| M9.7 Images | WebP category images deployed |
| M9.7 Megamenu Cleanup | Empty categories removed from megamenu/`/katalog` |
| Homepage Neutral Branches | 5 branch cards aligned with hub (M9.7E deploy evidence) |
| Manual UI Refinement | Operator CSS/UX on live TEST — **canonical visual layer** |

### Активный этап

**M9.8 UX Polish Pack** — research, task preparation, and EC-01 bug fix charter (implementation not part of this task).

### Not authorized

- **M10** Dynamic Filter Visibility (ROAD-005)
- Production deploy

---

## 4. Roadmap structure — M9.8 UX Polish Pack

Registered in [BZPM-PRODUCT-ROADMAP-v1.md](../../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) § *OCPilot Delivery Track — SITE-002*.

| ID | Task | Type | Implementation |
|----|------|------|----------------|
| M9.8.1 | PDP Gallery Compact | Research | **No** — thumbnails below main image, reduce whitespace, more useful PDP area |
| M9.8.2 | PDP Lightbox Constraints | Research | **No** — limit lightbox image size; no fullscreen scale |
| M9.8.3 | Homepage Hero Compression | Research | **No** — lower hero; first category row visible without clip |
| M9.8.4 | PLP Density Optimization | Research | **No** — shorter cards, less vertical gap, denser catalog |
| M9.8.5 | Products Per Page Selector | Task prep | **No** — options 10 / 20 / 50 / 100 |
| M9.8.6 | UltraWide Catalog Layout | Research | **No** — two list-view cards per row on wide screens |
| M9.8.7 | EC-01 Filter Cleanup | Bug fix | Charter required — hide empty subcategories in filter sidebar (branch 80) |
| M9.8.8 | PDP Thumbnail Rail Research | Research only | **No** — Alibaba-style vertical compact rail pattern |

### Open bug registry (post M9.7D)

| ID | Location | Issue |
|----|----------|-------|
| **EC-01** | Filter sidebar «Подкатегории», branch 80 Моечные ванны | 13 subcategories with 0 active products still visible |

All other audited surfaces (hub, megamenu, `/katalog`, chips, footer, offcanvas) — **clean** per [REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md](REPORT-BZPM-EMPTY-CATEGORY-FINAL-AUDIT.md).

---

## 5. Recommended next tasks (first)

| Order | ID | Why first |
|------:|-----|-----------|
| **1** | **M9.8.7** EC-01 Filter Cleanup | Only registered open bug; low complexity; `totalsub > 0` pattern already used in hub/chips/`category.php` |
| **2** | **M9.8.1** PDP Gallery Compact | Primary Алексей PDP feedback; highest impact on product page UX |
| **3** | **M9.8.2** PDP Lightbox Constraints | Natural follow-up to gallery layout research |
| **4** | **M9.8.4** PLP Density Optimization | Catalog browsing efficiency — second major feedback theme |
| **5** | **M9.8.3** Homepage Hero Compression | Homepage first-screen density |
| **6** | **M9.8.5** Products Per Page Selector | Standalone PLP control; clear spec (10/20/50/100) |
| **7** | **M9.8.6** UltraWide Catalog Layout | Depends on list-view density decisions from M9.8.4 |
| **8** | **M9.8.8** PDP Thumbnail Rail Research | Pattern research; may inform or replace direction from M9.8.1 |

**Suggested first implementation charter (when authorized):** M9.8.7 only — single-file filter sidebar fix with existing audit evidence and rollback from M9.7D baseline.

**Suggested first research pack (no code):** M9.8.1 + M9.8.2 — PDP gallery + lightbox, combined discovery document with screenshots from reference PDPs (SPKB-18/7-ВЛ5, ВМЦ-П3-2/500).

---

## 6. Scope compliance

| Constraint | Status |
|------------|--------|
| Site code changed | **NO** |
| Database changed | **NO** |
| TEST modified | **NO** |
| Production modified | **NO** |
| Documentation / state / roadmap only | **YES** |

---

## UNKNOWN / SECURITY RISK

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Whether live TEST currently matches M9.7D baseline byte-for-byte after any post-checkpoint operator edits — re-verify via FTP before next deploy |
| **UNKNOWN** | M10 authorization timeline |
| **SECURITY RISK** | none — no credentials committed; no live writes |

---

## Git status

Documentation updates — **uncommitted** (policy: no commit unless requested).

**Changed paths:**

- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/README.md`
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md`
- `projects/ocpilot/sites/site-002/reports/REPORT-BZPM-STATE-FREEZE-ROADMAP-UPDATE.md`
