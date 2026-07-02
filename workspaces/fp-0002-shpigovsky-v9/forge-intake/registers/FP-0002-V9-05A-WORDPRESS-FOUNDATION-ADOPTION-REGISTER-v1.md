# FP-0002 V9-05A — WordPress Foundation Adoption Register v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-05A  
**Date:** 2026-07-02  
**Gate:** [FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md](../validation/FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md)

---

## Adoption decision

```text
Prepared WordPress foundation: ADOPTED
Classification as obsolete legacy: REJECTED
Clean rebuild: NOT SELECTED
Forward model: PRESERVE + CONTROLLED V9 INTEGRATION
```

---

## PRESERVE AS FOUNDATION

| Item | Current state | Decision |
|------|---------------|----------|
| MLI runtime (`MLI-WP-FP0002-LOCAL`) | Active on `X:\MARS-Localhost` | **PRESERVE** |
| WordPress installation | WP 7.0 ru_RU at `sites/wordpress/projects/shpigovsky` | **PRESERVE** |
| Database identity | `mars_wp_fp0002`, prefix `fp02_` | **PRESERVE** |
| Domain | `http://shpigovsky.test/` | **PRESERVE** |
| Theme bootstrap | `shpigovsky` foundation theme active | **PRESERVE** |
| Plugin bootstrap | `shpigovsky-core` 0.1.0 active | **PRESERVE** |
| ACF Free | 6.8.4 active | **PRESERVE** |
| Menu registration | Primary, Footer, Legal locations registered | **PRESERVE** |
| Compatible menu assignments | Existing assignments where V9-compatible | **PRESERVE** (reconcile later) |
| ACF JSON wiring | Path configured in theme/plugin bootstrap | **PRESERVE** |
| MU local guard | `mars-local-runtime.php` | **PRESERVE** |
| Permalink structure | `/%postname%/` | **PRESERVE** |
| Compatible existing WP Pages | ~18 skeleton pages aligned with V9 hierarchy | **PRESERVE** (reconcile titles/parents) |
| Front-page / Posts-page settings | Configured for local dev | **PRESERVE** |
| Rollback evidence | `foundation-001` baseline + scripts | **PRESERVE** (refresh in V9-05B) |
| `blog_public = 0` | Discourage indexing | **PRESERVE** |

---

## EXTEND FOR V9

| Item | Current state | Required V9 extension |
|------|---------------|----------------------|
| Template hierarchy | Foundation PHP only | Full V9 template families (12) |
| Template parts | `.gitkeep` skeleton | V9 partial port per component map |
| Compiled assets | `foundation.css` only | Gulp-built assets from V9 `src/` |
| Theme `functions.php` / includes | Bootstrap only | Asset enqueue, supports, V9 hooks |
| Plugin includes | Bootstrap class only | Modal, forms hooks, ACF registration helpers |
| ACF field groups | None registered | 13 documented groups |
| V9 route objects | 14 routes missing | Create per route conflict register |
| Page template assignments | Default only | Assign per page-to-template map |
| Blog archive + single | Posts page exists; no fixture | `home.php`, single, fixture post |
| Consultation modal | Not in WP | Triumph lifecycle + Shpigovsky visuals |
| Scroll-to-Top | Not in WP | `scrollY > 500` contract |
| Fancybox | Not in WP | Gallery lightbox per V9 |
| Section reveal | Not in WP | Progressive enhancement + reduced motion |
| Forms frontend | Not in WP | Static demo UI; no backend |
| Content and media | Placeholder copy | Migrate from V9 `dist/` authority |
| Visual parity QA | Not started | Compare against V9 `dist/` |

---

## RECONCILE

| Item | Conflict | Future action |
|------|----------|---------------|
| Missing V9 routes | 14 required objects absent in DB | **CREATE** in V9-06+ |
| Route title / hierarchy | FW-06A registry vs V9 manifest deltas | **UPDATE** / **REPARENT** |
| Legal publication state | DEMO tokens in V9; WP pages exist as placeholders | **REVIEW** before **PUBLISH** |
| Blog fixture | No reference post | **CREATE** fixture post |
| Menu contents | Extra foundation items; missing V9 leaves | **UPDATE** menus |
| Tracked source ownership | V6 `WORDPRESS/` tracked; ops canonical path empty | **REVIEW** — see source authority decision |
| Stale path references | D/E/C drive paths in historical docs | **REVIEW** docs; X-native scripts in V9-05B |
| Backup scripts | Pre-V9 checkpoint identity | **REVIEW** before use; V9-05B creates fresh baseline |

---

## REMOVE OR RETIRE LATER

| Item | Reason | Future disposition | Destructive gate |
|------|--------|-------------------|------------------|
| `/uslugi/genotipirovanie/` page | Not in V9 manifest | **RETIRE** | Exact ID + backup + dry-run + operator approval |
| Top-level `specyalisty` | No V9 route | **RETIRE** or **REVIEW** redirect | Same |
| `intervyu-i-smi` | No V9 route | **RETIRE** or **REVIEW** | Same |
| `pravovaya-informaciya-pilzovatelyu` | No V9 route | **RETIRE** or **REVIEW** | Same |
| Obsolete FW-06A page registry assumptions | Superseded by V9 31-route map | **REVIEW** docs only | N/A |

**No deletion authorized by this register.**

---

## Foundation adoption table

| Foundation surface | Current role | Decision |
|--------------------|--------------|----------|
| MLI runtime | Shared localhost execution | **ADOPT** |
| WordPress core install | Local project site | **ADOPT** |
| Database | Page skeleton + config | **ADOPT** |
| Domain binding | `shpigovsky.test` | **ADOPT** |
| Theme (`shpigovsky`) | Foundation bootstrap | **ADOPT** — extend, do not replace |
| Plugin (`shpigovsky-core`) | Foundation bootstrap | **ADOPT** — extend, do not replace |
| ACF wiring | JSON path ready | **ADOPT** |
| Menus | Registered + partial assignments | **ADOPT** — reconcile contents |
| Permalinks | Post-name structure | **ADOPT** |
| MU guard | Local safety | **ADOPT** |
| Page skeleton | FW-06A placeholders | **ADOPT** — reconcile to V9 |
| Backup architecture | `foundation-001` concept | **ADOPT** — refresh in V9-05B |

---

*Planning register only. No runtime mutations authorized.*
