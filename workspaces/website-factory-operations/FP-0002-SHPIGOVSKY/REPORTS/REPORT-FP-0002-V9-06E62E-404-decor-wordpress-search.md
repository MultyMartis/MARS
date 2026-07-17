# REPORT — FP-0002 V9-06E62E 404 Decor and WordPress Search

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e62e-404-decor-wordpress-search/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62e-before-404-decor-wordpress-search-20260717-173256`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** (local validation) |
| Operator review | **pending** |
| DB writes | **0** |
| Commit / push / freeze | **no** |

Completed: operator CSS canonization; 404 decor asset replacement; header search dropdown; native WordPress search query scope; search results template + pagination + SEO.

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62e-before-404-decor-wordpress-search-20260717-173256` |
| DB dump | `mars_wp_fp0002.sql` — ~4 346 550 bytes — `CREATE TABLE` present; dump completed |
| Validation | **PASS** (`BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md` |

Note: `mysqldump` warned about PROCESS privilege / tablespaces; dump body is valid.

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| CSS `v9-style.css` | Runtime → source promote: `18114D3C…` → **`C22462401023F08D…`** (preserved through wave) |
| CSS `fp02-404.css` | Runtime → source promote then wave-local decor width edit: pre `DF8C77B5…` / rt `52E549DE…` → post-wave **`31F9D6FD…`** |
| Templates / HTML | Pre-wave PHP MATCH except CSS drift |
| Plugin | **0** drift |
| ACF JSON | Source-only groups remain (pre-existing; **not** synced) |
| Protected | Breadcrumbs, nav, lifebuoy, CTA, E62D 404 typography/spacing (aside from decor width) |

---

## 4. 404 Asset Replacement

| Item | Value |
|------|-------|
| Operator source | `INCOMING/OPERATOR-ASSETS/404/404-decor.png` (preserved) |
| Theme asset | `assets/img/404/404-decor.png` |
| Intrinsic size | **670×425** |
| SHA256 | `5EF4AD2BBCECE6D1BB88694638756ABE11F9E1587490CF4E4AEDEAB76B097313` |
| Old asset | `assets/img/404/404-visual.png` — references removed; **deleted** from source + runtime |
| Semantics | Decorative `<img alt="" role="presentation">` inside `<figure aria-hidden="true">`; non-clickable |

---

## 5. 404 Validation

| Check | Result |
|-------|--------|
| Viewports | Screenshots 1440 / 1024 / 480 / 370 captured |
| Typography | E62D Inter / `#475371` sizes retained |
| Spacing | Preserved; decor width capped at 670px |
| HTTP | **404** |
| Robots | `noindex, nofollow` |
| Canonical | none (correct) |
| Errors / overflow | No PHP warnings in captures; no old asset |

---

## 6. Search Trigger Audit

| Surface | Before | After |
|---------|--------|-------|
| Desktop nav | `.site-header__search` — no panel | Same button + `data-search-toggle` / ARIA |
| Floating header | No search | Added `.fp02-floating-header__search` |
| Mobile bar (≤1024) | No search (bottom nav hidden) | Added mobile search toggle |
| Offcanvas | No search | Unchanged |
| Dormant dropdown | None | New `#site-header-search` panel |

---

## 7. Search Dropdown

| Item | Detail |
|------|--------|
| Markup | `template-parts/navigation/search-panel.php` + `searchform.php` |
| Content | «Поиск по сайту»; hint «Начните вводить…»; input `name=s`; submit «Поиск»; close |
| Interactions | Toggle / Escape / outside click / focus input; closes offcanvas+modal; no scroll-lock |
| ARIA | `aria-expanded`, `aria-controls="site-header-search"`; panel `hidden` when closed |
| Responsive | Header-attached panel; under floating at `top:80px`; z-index 960 |
| Conflicts | Opening search closes offcanvas/modal; opening those closes search |

---

## 8. Search Query Architecture

| Item | Value |
|------|-------|
| Engine | Native WordPress main search query |
| Included | `post`, `page`, `service` |
| Excluded | attachments (not queried); private/password; legal pages `user-agreement`, `consent-personal-data`, `cookie-files-policy`, `privacy-policy` |
| Per page | **12** |
| Ordering | WordPress default relevance/date |
| Empty query | Forced zero results (`post__in` = `[0]`) |

---

## 9. Search Results Page

| Item | Detail |
|------|--------|
| Template | `search.php` (`page-search`) |
| Card | `template-parts/search/result-card.php` |
| Labels | Услуга / Специалист / Статья / Страница |
| Excerpt | Manual excerpt → short ACF fields → cleaned content; ~36 words |
| Image | Featured image only when present |
| No-results | Message + secondary form + Home/Services links |

---

## 10. Search Pagination

| Item | Detail |
|------|--------|
| Component | `template-parts/search/pagination.php` (Blog-style) |
| Example | `/page/2/?s=зависим` and `/?s=зависим&paged=2` → **200**, 4 cards (of 16) |
| Invalid | `/page/99/?s=зависим` → **404** |
| Query preserved | Yes via core `paginate_links` |

---

## 11. Search SEO

| Route | Status | Title | Robots | Canonical | Result |
|-------|--------|-------|--------|-----------|--------|
| `/?s=алкоголь` | 200 | Результаты поиска: алкоголь — … | `noindex, follow` | none | 2 |
| `/?s=zzzznotfoundxyz` | 200 | Результаты поиска: zzzz… | `noindex, follow` | none | 0 |
| `/page/2/?s=зависим` | 200 | … — Страница 2 — … | `noindex, follow` | none | page 2 |
| `/missing-e62e/` | 404 | Страница не найдена — … | `noindex, nofollow` | none | 404 |

Local site also has blog_public discouragement (`noindex, nofollow` on normal pages) — search overrides to `noindex, follow`.

---

## 12. Accessibility and Security

- Keyboard: toggle, Escape, Enter submit, focus to input  
- Escaping: `esc_html` / `esc_attr` / `esc_url` on query and titles  
- Form semantics: `role="search"`, labeled input, submit button name  
- No direct SQL  
- Decorative 404 image not exposed to AT  

---

## 13. Database Changes

| Scope | Writes |
|-------|--------|
| Content / options / ACF | **0** |
| Temporary validation records | **0** |

---

## 14. Exact Files Changed

### Source (`WORDPRESS/theme/shpigovsky/`)
- Updated: `404.php`, `search.php`, `functions.php`, `inc/assets.php`, `inc/navigation.php`, `assets/css/v9-style.css` (canon), `assets/css/fp02-404.css`, `assets/js/v9-shell.js`, `template-parts/layout/header.php`, `template-parts/layout/floating-header.php`, `template-parts/navigation/primary-desktop.php`
- Added: `searchform.php`, `inc/search-helpers.php`, `assets/css/fp02-search.css`, `assets/img/404/404-decor.png`, `template-parts/navigation/search-panel.php`, `template-parts/search/result-card.php`, `template-parts/search/pagination.php`
- Removed: `assets/img/404/404-visual.png`

### Runtime
- Exact-file copies of the above; old visual deleted

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E62E-404-decor-wordpress-search.md`
- `REPORTS/evidence/v9-06e62e-404-decor-wordpress-search/*`
- `PROJECT-STATUS.md`, `WORDPRESS/SOURCE-AUTHORITY.md`

---

## 15. Source-to-Runtime Delivery

Exact-file delivery only (no broad sync). All listed theme files **MATCH** post-delivery (`source-runtime-hashes.csv`). Operator `v9-style` hash **`C2246240…`** preserved.

---

## 16. Validation

- Queries: service/specialist/blog/Cyrillic/nonsense/empty/special chars — PASS  
- Pagination: page 2 PASS; invalid page 404 PASS  
- 404 decor active; old visual absent  
- Viewports screenshots captured  
- PHP warning patterns: **0** in HTML captures  

---

## 17. Regression

Checked routes `/`, `/uslugi/`, service leaf, `/specyalisty/`, `/o-centre/`, `/kontakty/`, `/blog/`, `/otzyvy/`, 404, search URLs — HTTP expected. Header / floating / offcanvas / modal architecture preserved (search integrates without replacing them).

---

## 18. Risks and SAFE UNKNOWN

- Native WP search relevance is title/content-only (no ACF field indexing yet)  
- Future tuning may need weighted CPT relevance  
- Source-only ACF JSON drift remains out of scope  
- JS console tooling limited in this environment (interaction validated via markup + script presence)  
- Screenshot dropdown-open state not captured (static headless); open panel present in DOM on all pages  

---

## 19. Remaining Project Tails

- Operator visual review (404 decor + search UI)  
- Advanced search / ACF indexing  
- Demo content cleanup decision  
- Out-of-scope ACF source-only drift  
- Final freeze / commit / push  

---

## 20. Git Status

- **No commit / no push**  
- Exact FP-0002 scope mutated  
- Foreign WIP in monorepo untouched by this wave’s staging (none performed)  

---

## 21. Operator Review Pages

1. `http://shpigovsky.test/missing-e62e/` — 404 decor  
2. `http://shpigovsky.test/` — click search (desktop); mobile search icon ≤1024; floating search after scroll  
3. `http://shpigovsky.test/?s=алкоголь` — mixed results  
4. `http://shpigovsky.test/?s=Шпиговский` — specialist hit  
5. `http://shpigovsky.test/?s=сила+воли` — blog hit  
6. `http://shpigovsky.test/?s=зависим` — pagination  
7. `http://shpigovsky.test/page/2/?s=зависим` — page 2  
8. `http://shpigovsky.test/?s=zzzznotfoundxyz` — empty state  

Keyboard: open search → type → Enter; Escape closes; outside click closes.
