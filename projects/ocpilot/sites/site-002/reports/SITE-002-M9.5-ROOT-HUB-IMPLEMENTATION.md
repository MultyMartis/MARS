# REPORT — BZPM M9.5 Root Hub Implementation

**Program:** BZPM Product Roadmap  
**Milestone:** M9.5 Neutral Root Category UX  
**Site:** SITE-002  
**Environment:** TEST only — https://zpm.new-site.space/  
**Authority:** `BZPM-M9.5-NEUTRAL-ROOT-UX-v1.md` · `BZPM-M9-FILTER-PROFILE-SYSTEM-v1.md` · `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159`  
**Deploy UTC:** 2026-06-14T20:31:41Z  
**Git commit:** No (per task)  
**Production:** No  

---

## Pre-flight

| Check | Result |
| --- | --- |
| Stable baseline | **PASS** — `backups/stable-baselines/SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159/` + manifest |
| Rollback source | **PASS** — `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` |
| M9 Phase 3 state | **PASS** — profiles 301/80/322/207/326 on TEST |
| Pre-M9.5 backup | **PASS** — `m9.5-root-hub-work/backups/pre-m9.5-*` (3 files) + manifest `m9.5-root-hub-deploy-20260614-203141.json` |
| Git status | Uncommitted — new `m9.5-root-hub-work/`, `qa/m9.5-root-hub/`; no commit |

**Files expected to change (planned):**

| Remote path | Role |
| --- | --- |
| `system/library/zpm/category_visibility.php` | Hub category id + branch list constants |
| `catalog/controller/product/category.php` | `hub` display mode, `hub_categories` data, skip PLP query on cat 79 |
| `catalog/view/theme/default/template/product/category.twig` | Hub grid markup; hide PLP chrome on hub |

---

## Architecture

**Display mode** (`category_display_mode`):

| Mode | `category_id` | Behavior |
| --- | ---: | --- |
| `hub` | **79** | Subcategory `zpm-cat-card` grid; no filter; no product grid |
| `branch` | 80, 207, 301, 322, 326, … | Existing M9 PLP unchanged |

**Hub branch selection** — commercial priority list in `CategoryVisibility::getNeutralHubBranchIds()`:

`301 → 80 → 322 → 207 → 326`

Each branch included only if `getTotalProducts(subtree) > 0`. Empty siblings (83, 86, 85, 82, …) never appear as cards.

**Pageintro** on hub — approved draft copy under H1.

**Option A** (spec): product grid, pagination, filter sidebar, mobile filter button, sort/view controls, and subcategory chips are **not rendered** on category 79.

**Reuse:** existing `zpm-cat-sections` + `zpm-cat-card` markup (same as `/katalog` / homepage pattern); `thumb300` via `model_tool_image->resize(300,300)`; placeholder when `oc_category.image` empty.

---

## Files Modified

### Deployed to TEST (3 files)

| File | SHA-256 (deployed) | Bytes |
| --- | --- | ---: |
| `system/library/zpm/category_visibility.php` | `029b22a35513cb79d728a7e78b07f9a4741b2dde4650562cf0297da5b508623f` | 3965 |
| `catalog/controller/product/category.php` | `4ed6db8db424cf7c2123ab6ea6c74e8dad8c9d10b3e922e2014cf207c611538e` | 22103 |
| `catalog/view/theme/default/template/product/category.twig` | `291daa368db27daca9185c47a9164cb07139a1be727cd0d47e7cb0190c65c94e` | 5769 |

### Repo work package (local)

| Path | Role |
| --- | --- |
| `m9.5-root-hub-work/patch/` | Source patches (mirror of deployed files) |
| `m9.5-root-hub-work/m9.5-root-hub-deploy.py` | FTP deploy + pre-backup |
| `m9.5-root-hub-work/m9.5-root-hub-qa.py` | Storefront QA |
| `m9.5-root-hub-work/backups/pre-m9.5-*` | Pre-deploy server snapshots |
| `m9.5-root-hub-work/backups/m9.5-root-hub-deploy-20260614-203141.json` | Deploy manifest |
| `qa/m9.5-root-hub/m9.5-root-hub-qa-result.json` | QA evidence |

---

## Hub Categories

| Order | ID | Name | SEO path | Show |
| ---: | ---: | --- | --- | :---: |
| 1 | **301** | Столы | `/katalog/nejtralnoe-oborudovanie/stoly/` | ✅ |
| 2 | **80** | Моечные ванны | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny/` | ✅ |
| 3 | **322** | Подтоварники и подставки | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/` | ✅ |
| 4 | **207** | Зонты вытяжные | `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/` | ✅ |
| 5 | **326** | Тележки сервировочные | `/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/` | ✅ |

**Hidden (0 SKU or duplicate):** 83 Полки · 86 Стеллажи · 85 Тележки · 82 Подтоварники (parent) · 87 · 88 · 89

---

## Hidden Elements

On **category 79 only** (hub mode):

| Element | Hidden |
| --- | :---: |
| Filter sidebar (`data-filter-sidebar`) | ✅ |
| Mobile «Фильтры» (`data-filter-open`) | ✅ |
| Sort controls | ✅ |
| View switcher (`data-category-view`) | ✅ |
| Product grid (`category__grid` / `p-card`) | ✅ |
| Pagination | ✅ |
| Subcategory chips (`zpm-sub-cat-chips`) | ✅ |

**Preserved on hub:** breadcrumbs · H1 + pageintro · certificates · dealers form.

**Branch PLPs (301, 80, 322, 207, 326):** unchanged — filter + product grid + M9 profiles.

---

## QA Results

**Runner:** `m9.5-root-hub-work/m9.5-root-hub-qa.py`  
**Evidence:** `qa/m9.5-root-hub/m9.5-root-hub-qa-result.json`  
**Summary:** **19 / 19 PASS** (2026-06-14T20:33 UTC)

| ID | URL / scope | Result |
| --- | --- | :---: |
| QA-01–14 | `/katalog/nejtralnoe-oborudovanie` | PASS |
| QA-BR-301 | `/stoly/` | PASS — M9 profile primary filters |
| QA-BR-80 | `/moechnye-vanny/` | PASS — M9 profile primary filters |
| QA-BR-322 | `/podtovarniki-i-podstavki/` | PASS |
| QA-BR-207 | `/zonty-vytyazhnye/` | PASS |
| QA-BR-326 | `/telezhki-servirovochnye/` | PASS |

**Verified on hub:** HTTP 200 · no PHP error markers · `category--hub` · 5 `zpm-cat-card` · correct branch hrefs · intro copy · certificates + dealers blocks · no filter/grid/pagination/chips.

---

## Rollback Procedure

1. Restore pre-M9.5 files from `m9.5-root-hub-work/backups/pre-m9.5-*` to FTP paths (or re-upload M9 Phase 3 `category.php` from `m9-phase3-remaining-work/patch/`).
2. Restore `category_visibility.php` from `pre-m9.5-system__library__zpm__category_visibility.php` (M7.1 without hub helpers).
3. Flush Twig + attribute caches (`system/storage/cache/template`, `cache.category.attributes.*`).
4. **Full rollback to M8.3:** `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` baseline + remove M9 library files.

**M9 Phase 3 rollback reference:** `m9-phase3-remaining-work/backups/m9-phase3-deploy-20260614-200051.json`

---

## Image Status

| category_id | DB image | Hub card |
| ---: | --- | --- |
| 301 | empty | `placeholder.png` resize 300×300 |
| 80 | empty | placeholder |
| 322 | empty | placeholder |
| 207 | empty | placeholder |
| 326 | empty | placeholder |
| 79 (root) | `nejtralnoe-oborudovanie-2.webp` | not used on hub grid (branch cards only) |

No images generated in M9.5. Asset milestone deferred per spec.

---

## M10 Readiness

| Item | Status |
| --- | --- |
| Neutral root hub UX (cat 79) | **Done on TEST** |
| M9 branch profiles (80, 207, 301, 322, 326) | **Regression PASS** |
| Branch category card images | **Deferred** — placeholders acceptable for TEST v1 |
| Root profile 79 / `hidden_global` absorption | **Still pending** — hub mode bypasses filter build; not a profile file |
| M10 dynamic visibility | **Not started** (per scope) |
| Production deploy | **Not done** |

**Recommendation before M10:** upload 5 branch images per `BZPM-M9.5-NEUTRAL-ROOT-UX-v1.md` Image Strategy; optional product count on cards.

---

## Git status

- **Commit:** none  
- **Push:** none  
- **New (untracked):** `projects/ocpilot/sites/site-002/m9.5-root-hub-work/`, `projects/ocpilot/sites/site-002/qa/m9.5-root-hub/`  
- **This report:** `projects/ocpilot/sites/site-002/reports/SITE-002-M9.5-ROOT-HUB-IMPLEMENTATION.md`

---

## UNKNOWN

- Exact live heading strings inside `sections/certificates.twig` (QA uses section/markers; block confirmed present).
