# REPORT — FP-0002 V9-06E62E-FIX01 Search Wrapper and Trigger Placement

**Date:** 2026-07-17  
**Project:** FP-0002 — Shpigovsky.ru  
**Wave:** V9-06E62E-FIX01 — Search breadcrumb wrapper + Search trigger placement  
**Status:** **PASS** (local validation)  
**Operator review:** pending  
**DB writes:** **0**  
**Commit / push / freeze:** **none**

---

## 1. Status

| Gate | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | pending |
| DB writes | **0** |
| Commit / push / freeze | **none** |

---

## 2. Pre-Change Backup

| Field | Value |
|-------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62e-fix01-before-search-wrapper-trigger-placement-20260717-174720\` |
| DB dump | `mars_wp_fp0002.sql` (~6 739 215 bytes UTF-8 export) |
| Validation | `CREATE TABLE` present; `Dump completed` present; live schema table count **14** |
| Hashes | `hashes-before.csv` |
| Operator manifest | `operator-change-manifest.csv` (preflight drift **0**) |
| Marker | `BACKUP-OK.txt` |

Note: `mysqldump` PROCESS/tablespaces warning (same class as E62E); dump body valid.

---

## 3. Latest Operator Changes Canonized

| Item | Result |
|------|--------|
| Preflight source↔runtime theme drift | **0** (MATCH) |
| Promote required | **No** — runtime already matched canonical source |
| Operator CSS `v9-style.css` | **Preserved** — `C22462401023F08D…` unchanged |
| Templates / Search panel design | Preserved (no redesign) |
| Unresolved drift | **None** in scoped theme files |

---

## 4. Search Breadcrumb Wrapper

| Item | Value |
|------|--------|
| Previous DOM | `.page-search__breadcrumbs > .container > .breadcrumbs` |
| Final DOM | `.internal-page-nav > .container > .breadcrumbs` |
| Affected routes | Search only (`/?s=…`, paginated search) |
| CSS cleanup | Removed obsolete `.page-search__breadcrumbs` from `fp02-search.css` |
| Toggle behavior | Existing `shpigovsky_breadcrumbs_enabled_for_context()` preserved |
| Other templates | Untouched (Blog / Services / Contacts / Reviews / etc.) |

Evidence: `REPORTS/evidence/v9-06e62e-fix01-search-wrapper-trigger-placement/search-breadcrumb-dom-before-after.md`

---

## 5. Search Trigger Ownership

| Location | Before | Final | Implementation |
|----------|--------|-------|----------------|
| Desktop main Header | Dropdown toggle (`data-search-toggle`) in primary nav | **Kept** | `primary-desktop.php` / nav fallback |
| Floating Header | `fp02-floating-header__search` + `data-search-toggle` | **Removed** | `floating-header.php` |
| Mobile Header bar | `site-header__search--mobile` + `data-search-toggle` | **Removed** | `header.php` |
| Mobile offcanvas | — | **Search link** → `/?s=` | `offcanvas.php` (`a.offcanvas__nav-link--search`, **no** `data-search-toggle`) |

Desktop/mobile breakpoint (project CSS): **`max-width: 1024px`** shows mobile bar and hides `.site-header__bottom` (desktop search). Desktop layout effectively **≥ 1025px**.

---

## 6. Mobile Search Link

| Field | Value |
|-------|-------|
| Markup | `<a class="offcanvas__nav-link offcanvas__nav-link--search">` + FA search icon + «Поиск» |
| URL | `esc_url( home_url( '/?s=' ) )` → `http://shpigovsky.test/?s=` |
| Position | Inside `.offcanvas__nav`, after primary menu list (actions list) |
| Style | Reuses offcanvas nav link system + small gap for icon (`fp02-search.css`) |
| Behavior | Full navigation to blank Search page; closes offcanvas via navigation; no JS toggle |

---

## 7. Blank Search Page

| Field | Value |
|-------|-------|
| Empty-query behavior | Ready-to-search state (not “0 results”) |
| Instruction | «Введите поисковый запрос» |
| Form | Present (`#page-search-empty-field`), empty input |
| Cards / pagination | Absent |
| SEO | `noindex, follow` |
| HTTP | **200** |

Non-empty no-results copy unchanged.

---

## 8. Search JavaScript

| Field | Value |
|-------|-------|
| Retained trigger | `[data-search-toggle]` (desktop main Header only) |
| Removed bindings | Floating/mobile toggles gone from DOM; floating-anchor scroll/resize logic removed |
| Interactions | Open/focus, Escape, outside click, offcanvas/modal conflict close — retained |
| Offcanvas Search link | Not bound as dropdown toggle |
| Console errors | **0** |

---

## 9. Exact Files Changed

### Source (`WORDPRESS/theme/shpigovsky/`)

- `search.php`
- `inc/search-helpers.php`
- `assets/css/fp02-search.css`
- `assets/js/v9-shell.js`
- `template-parts/layout/header.php`
- `template-parts/layout/floating-header.php`
- `template-parts/navigation/offcanvas.php`

### Runtime (`wp-content/themes/shpigovsky/`)

Exact-file copy of the seven paths above (hashes MATCH).

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E62E-FIX01-search-wrapper-trigger-placement.md`
- `REPORTS/evidence/v9-06e62e-fix01-search-wrapper-trigger-placement/*`
- `PROJECT-STATUS.md` (status line update)

`v9-style.css` **not** modified. `SOURCE-AUTHORITY.md` **not** changed (authority unchanged).

---

## 10. Source-to-Runtime Delivery

| Gate | Result |
|------|--------|
| Hashes | All changed files source↔runtime **MATCH** (see evidence CSV) |
| Delivery | Exact-file only |
| Broad sync | **No** |
| Operator CSS | Preserved (`C2246240…`) |

---

## 11. Validation

| Area | Result |
|------|--------|
| Desktop 1440 | Search button visible; opens dropdown; focus; Escape closes |
| Floating Header | No Search button; layout closes gap |
| Mobile Header 1024/480/370 | No Search button |
| Offcanvas 1024/480/370 | «Поиск» → `/?s=` blank page ready |
| Search pages | internal-page-nav crumbs; blank / results / no-results / page 2 |
| JS errors | **0** |
| Horizontal overflow | **0** (spot-checked home 1440 + blank search 480) |
| PHP warnings in HTML | **0** (smoke routes) |

---

## 12. Regression

Routes smoke: `/`, Service leaf + section, `/o-centre/`, `/kontakty/`, `/blog/`, `/otzyvy/`, blank Search, Search results, 404 — HTTP expected; shared Header/offcanvas/callback/masks/breadcrumbs/lifebuoy/footer not redesigned.

---

## 13. Risks and Tails

| Risk / Tail | Note |
|-------------|------|
| Desktop breakpoint | Driven by CSS `1024px` mobile switch; desktop Search lives in hidden-on-mobile `.site-header__bottom` (still one DOM toggle) |
| Floating Header Search absence | By design after scroll on desktop — Search only from main Header while at top |
| Operator visual review | Confirm crumbs + Header placements on real viewports |
| Freeze | Not requested |

---

## 14. Git Status

- **No commit**
- **No push**
- Exact FP-0002 scope only
- Foreign WIP in monorepo untouched
- Forbidden git ops not used

---

## 15. Operator Review

Please inspect:

1. `http://shpigovsky.test/?s=алкоголь` — crumbs = `.internal-page-nav > .container > .breadcrumbs`
2. `http://shpigovsky.test/?s=zzzznotfoundxyz` — no-results + same crumb shell
3. `http://shpigovsky.test/page/2/?s=зависим` — paginated Search crumbs
4. `http://shpigovsky.test/?s=` — blank ready state («Введите поисковый запрос» + form)
5. Desktop **1440**: main Header Search → dropdown
6. Desktop scrolled: floating Header **without** Search
7. **1024 / 480 / 370**: mobile Header **without** Search; offcanvas **«Поиск»** → blank Search

Screenshots: `REPORTS/evidence/v9-06e62e-fix01-search-wrapper-trigger-placement/`

---

**End of report.**
