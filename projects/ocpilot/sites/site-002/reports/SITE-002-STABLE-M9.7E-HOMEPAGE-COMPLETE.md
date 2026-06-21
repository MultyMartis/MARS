# REPORT — SITE-002 Stable Checkpoint M9.7E Homepage Complete

**Program:** BZPM Product Roadmap  
**Site:** SITE-002 (ЗПМ)  
**Environment:** TEST only — https://zpm.new-site.space/  
**Checkpoint:** `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE`  
**Authority:** LIVE TEST STATE after M9.7E homepage deploy + M9.7D manual UI + Beget global backup (operator)  
**Execution UTC:** 2026-06-15  
**Mode:** Read-only checkpoint — **no** deploy · **no** production · **no** commit · **no** push

---

## Baseline policy

| Rule | Value |
|------|-------|
| Visual / UI baseline | **This checkpoint** — M9.7E homepage + M9.7D manual UI |
| **Do NOT use** | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` as current baseline (homepage still 1 root card) |
| Supersedes | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| M9.7E deploy evidence | [REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md](REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md) · `m9.7e-homepage-neutral-branches-work/backups/m9.7e-deploy-20260614-224916.json` |

---

## QA Snapshot

**Summary:** 33 pass · 0 fail · 0 warn  
**Evidence:** `backups/stable-baselines/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE/qa-snapshot.json`

### Pre-flight

| Check | Result |
|-------|--------|
| TEST accessible | **PASS** — all required URLs HTTP 200 |
| PHP warnings/notices | **PASS** |
| M9 profiles active | **PASS** — 301/80/322/207/326 branch filters verified |
| Root Hub | **PASS** — `category--hub`, 5 branch cards, real WebP thumbs |
| Megamenu neutral | **PASS** — 5 tiles, no zero-count, no forbidden empty branches |
| **Homepage categories (M9.7E)** | **PASS** — 5 branch cards, correct order, no root card, hub parity |
| M8 cleanup active | **PASS** |
| Category images (301/80/322/207/326) | **PASS** — WebP deployed, no placeholders |

### Required URLs

| URL | Result |
|-----|--------|
| `/` | **PASS** — 5 homepage branch cards |
| `/katalog` | **PASS** |
| `/katalog/nejtralnoe-oborudovanie` | **PASS** — hub, 5 cards |
| Branch PLPs 301/80/322/207/326 | **PASS** |
| Reference table + sink PDP | **PASS** |

### Homepage / hub / megamenu parity (M9.7E)

| Surface | Count | Order |
|---------|------:|-------|
| Homepage `zpm-cat-sections` | **5** | Столы → Моечные ванны → Подтоварники → Зонты → Тележки |
| Hub branch cards | **5** | Same set |
| Megamenu neutral tiles | **5** | Same set (tile order may differ) |

Root «Нейтральное оборудование» **absent** from homepage category block (by design M9.7E).

---

## Captured artifacts

**Baseline folder:** `projects/ocpilot/sites/site-002/backups/stable-baselines/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE/`

| Layer | Count | Notes |
|-------|------:|-------|
| PHP controllers + ZPM library | 11 | incl. M9.7E `home.php`, `category_visibility.php` |
| Twig templates | 7 | megamenu, category (hub), offcanvas, filterssidebar, catalogsections |
| M9 filter profiles | 6 | 301/80/322/207/326 + global_hidden |
| OpenCart theme CSS | 1 | `stylesheet.css` |
| **Site CSS (manual UI)** | 3 | `assets/css/style.css`, `style.min.css`, `sd.css` |
| Category WebP images | 5 | `images/category-image/*.webp` |
| DB JSON exports | 6 scoped tables | partial; scoped SQL dump failed (PMA 500) |
| QA + data snapshots | 2 | `qa-snapshot.json`, `data-snapshot.json` |

**Missing from FTP (same as M9.7D):** `catalog/view/theme/default/stylesheet/zpm.css`, `zpm-catalog.css` — files not on live host (550).

**M9.7E delta vs M9.7D (hash-verified on capture):**

| File | Changed |
|------|---------|
| `catalog/controller/common/home.php` | **YES** — M9.7E `buildHomepageCategoryCards()` |
| `system/library/zpm/category_visibility.php` | **YES** — M9.7E homepage builder method |

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
5. **Pre-M9.7E rollback:** restore M9.7D baseline — homepage reverts to 1 root card.

**Prior checkpoint:** `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` — pre-M9.7E homepage.

---

## UNKNOWN / SECURITY RISK

**UNKNOWN:** PMA scoped SQL full export returned HTTP 500; JSON row exports partial (`oc_attribute` 0 rows — PMA parse anomaly). Live DB assumed unchanged.

**SECURITY RISK:** none. FTP/DB credentials used per existing ops pattern; not committed.

---

## Git status

New checkpoint folder, scripts, reports — **uncommitted** (policy: no commit unless requested).
