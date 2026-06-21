# REPORT — SITE-002 Stable Checkpoint M9.7D After Manual UI

**Program:** BZPM Product Roadmap  
**Site:** SITE-002 (ЗПМ)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Checkpoint:** `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI`  
**Authority:** LIVE TEST STATE AFTER MANUAL UI REFINEMENT (operator manual edits post M9.7C)  
**Execution UTC:** 2026-06-15  
**Mode:** Read-only checkpoint — **no** deploy · **no** production · **no** commit · **no** push

---

## Baseline policy

| Rule | Value |
|------|-------|
| Visual / UI baseline | **This checkpoint** — post-operator manual refinement |
| **Do NOT use** | `SITE-002-STABLE-M9-COMPLETE-20260615` or M9.7C patch pack as visual baseline |
| Supersedes (code rollback only) | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Prior M9.7C deploy evidence | `m9.7c-image-megamenu-work/backups/m9.7c-deploy-20260614-215218.json` |

Operator manual changes (Twig/CSS/hub/megamenu spacing) are **legitimate** and captured from **live FTP**, not restored from old backups.

---

## QA Snapshot

**Summary:** 26 pass · 0 fail · 0 warn  
**Evidence:** `backups/stable-baselines/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI/qa-snapshot.json`

### Pre-flight

| Check | Result |
|-------|--------|
| TEST accessible | **PASS** — all required URLs HTTP 200 |
| PHP warnings/notices | **PASS** |
| M9 profiles active | **PASS** — 301/80/322/207/326 branch filters verified |
| Root Hub | **PASS** — `category--hub`, 5 branch cards, real WebP thumbs |
| Megamenu neutral | **PASS** — 5 tiles, no zero-count, no forbidden empty branches |
| M8 cleanup active | **PASS** |
| Category images (301/80/322/207/326) | **PASS** — WebP deployed, no placeholders |

### Required URLs

| URL | Result |
|-----|--------|
| `/` | **PASS** |
| `/katalog` | **PASS** |
| `/katalog/nejtralnoe-oborudovanie` | **PASS** — hub, 5 cards |
| Branch PLPs 301/80/322/207/326 | **PASS** |
| Reference table + sink PDP | **PASS** |

### Megamenu / hub (post manual UI)

| Surface | Count | Names |
|---------|------:|-------|
| Megamenu neutral tiles | 5 | Подтоварники и подставки, Столы, Тележки сервировочные, Зонты вытяжные, Моечные ванны |
| Hub branch cards | 5 | Столы, Моечные ванны, Подтоварники и подставки, Зонты вытяжные, Тележки сервировочные |

---

## Captured artifacts

**Baseline folder:** `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI/`

| Layer | Count | Notes |
|-------|------:|-------|
| PHP controllers + ZPM library | 11 | incl. M9.7C `category_visibility.php`, `header.php`, `katalog.php` |
| Twig templates | 7 | megamenu, category (hub), offcanvas, filterssidebar, etc. |
| M9 filter profiles | 6 | 301/80/322/207/326 + global_hidden |
| OpenCart theme CSS | 1 | `catalog/view/theme/default/stylesheet/stylesheet.css` |
| **Site CSS (manual UI)** | 3 | `assets/css/style.css`, `style.min.css`, `sd.css` — **primary manual UI layer** |
| Category WebP images | 5 | `images/category-image/*.webp` |
| DB JSON exports | 6 scoped tables | partial export; scoped SQL dump failed (PMA 500) |
| QA + data snapshots | 2 | `qa-snapshot.json`, `data-snapshot.json` |

**Manual UI delta vs M9-COMPLETE (hash-verified):**

| File | Changed |
|------|---------|
| `assets/css/style.css` | **YES** — 279 KB (not in M9-COMPLETE baseline) |
| `assets/css/style.min.css` | **YES** |
| `system/library/zpm/category_visibility.php` | YES (M9.7C) |
| `catalog/controller/common/header.php` | YES (M9.7C) |
| `catalog/controller/product/katalog.php` | YES (M9.7C) |
| `megamenu.twig`, `category.twig`, `offcanvasmenu.twig` | **NO** hash change vs M9-COMPLETE FTP capture |

Evidence: `supplement-audit.json`

---

## Data snapshot

| Metric | Value |
|--------|------:|
| Active SKU (`status=1`) | **608** |
| Branch category images in DB | 301/80/322/207/326 → WebP paths set |
| Profile categories | 79 (hub), 301, 80, 322, 207, 326 |

---

## Rollback

1. Upload all files from `files/` to matching FTP paths.
2. Upload `images/category-image/*.webp` → `image/catalog/Category-image/`.
3. Clear OpenCart caches (`system/storage/cache/`, template cache, `cat-list-header`).
4. Optional DB: per-table JSON under `database/` (TEST only).
5. **Do not** restore pre-manual UI from M9.7C backup packs unless explicitly rolling back M9.7C code only.

**Prior checkpoint:** `SITE-002-STABLE-M9-COMPLETE-20260615` — pre-M9.7D / pre-manual UI.

---

## UNKNOWN / SECURITY RISK

**UNKNOWN:** PMA scoped SQL full export returned HTTP 500; JSON row exports succeeded for core tables but `oc_attribute` export returned 0 rows (PMA parse anomaly — DB live state assumed unchanged from M9).

**SECURITY RISK:** none. FTP/DB credentials used per existing ops pattern; not committed.

---

## Git status

New checkpoint folder, scripts, reports — **uncommitted** (policy: no commit unless requested).
