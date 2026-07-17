# REPORT — FP-0002 V9-06E62A 404, Breadcrumb Wrapper and Phone Mask

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e62a-404-breadcrumb-wrapper-phone-mask/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62a-before-404-breadcrumb-wrapper-phone-mask-20260717-160948`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** (local validation) |
| Operator review | **pending** |
| DB writes | **0** |
| Commit / push / freeze | **no** |

Completed in this wave: operator CSS canonization; Figma 404 page; Generic/Specialist breadcrumb wrapper; Triumph-pattern phone masks. E61 tails retained open. Blog/Reviews pagination and O-centre/Service ACF cleanup **not** in scope.

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62a-before-404-breadcrumb-wrapper-phone-mask-20260717-160948` |
| DB dump | `db/mars_wp_fp0002.sql` — 4 285 366 bytes — SHA256 `F77AF89C31502F84CA753CFE78CE2CCF11EFE2402B6461D7FE5E7C8FBDC5B2E3` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `--no-tablespaces`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv`, `BACKUP-INFO.md` |

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| CSS `v9-style.css` | Runtime → source promote **before** wave: `DCB0C163…` → **`E11627B9F73E…`** |
| Templates / HTML | Theme PHP source↔runtime match pre-wave (**0** HTML drift) |
| Plugin | **0** drift |
| ACF JSON | 8 source-only groups missing in runtime (pre-existing; **not** synced this wave) |
| Breadcrumb CSS | Operator **16px / 22px** on `.internal-page-nav` crumbs **unchanged** |
| Protected hash | `E11627B9F73EC345D4C8B89A77D2CEDA8B104F2520E1BB16A61709C0E825F720` |

---

## 4. 404 Figma Authority

| Item | Value |
|------|-------|
| Native Figma | `INCOMING/01_DESIGN/Spig_v1.2.fig` frames **`404`** / **`404 - моб`** |
| Approved PNG | `INCOMING/01_DESIGN/26.06.2026/Страница 404 - десктоп.png` (**1437×1900**) |
| Mobile PNG | `…/Страница 404 - мобильная.png` (**380×1734**) |
| V9 static | **No 404 page** (NOT STARTED) — not used as authority |
| Limitation | Visual cropped from desktop PNG (local asset only); Figma header chrome differs from live shell — live header/footer retained per charter |

---

## 5. 404 Implementation

| Item | Detail |
|------|--------|
| Template | `404.php` — class `page-404` |
| CSS | `assets/css/fp02-404.css` (404-local only; enqueued on `is_404()`) |
| Asset | `assets/img/404/404-visual.png` |
| Layout | Title + lead + logo + CTA + visual; normal header/floating header/footer/lifebuoy |
| Copy | «Мы не смогли найти эту страницу…» / «Но мы можем найти и устранить причины вашей зависимости» |
| CTA | Desktop «Вернуться на главную»; ≤767 «На главную» |
| HTTP | **404** on probe routes; **no** Home redirect |
| SEO | `noindex, nofollow`; **no** canonical to unrelated page |
| PHP warnings | **0** |

---

## 6. Breadcrumb Template Family

| Family | Template | Wrapper |
|--------|----------|---------|
| Specialist parent/child, Gallery, Generic | `page-templates/generic.php` | `.internal-page-nav > .container > .breadcrumbs` |
| Legal / default page | `legal.php` / `page.php` | same (auto wrap) |
| O-centre hub | `institutional.php` | existing `internal-page-nav` (subnav) |
| Contacts / Reviews / Blog archive / Blog single | dedicated shells | **excluded** from internal wrap |
| Service CPT | service stacks | existing `internal-page-nav` via subnav — **excluded** |

---

## 7. Breadcrumb Wrapper Implementation

| Item | Detail |
|------|--------|
| Helper | `shpigovsky_render_breadcrumbs( $args )` + `shpigovsky_breadcrumbs_should_use_internal_wrap()` |
| Final DOM | `<div class="internal-page-nav"><div class="container"><nav class="breadcrumbs"…>` |
| Toggle | E61 `show_breadcrumbs_pages` / `show_breadcrumbs_services` preserved; disabled → no empty wrappers |
| Styles | Operator crumb CSS untouched |
| Matrix | 9/9 wrapper expectations PASS (see evidence CSV) |

---

## 8. Triumph Phone Mask Reference

| Item | Value |
|------|-------|
| Path | `workspaces/triumph-manipulator-landing-v6/src/js/form.js` |
| Pattern | Custom `bindPhoneMask` (vanilla; **no** Inputmask; **no** jQuery) |
| Format | `+7 (XXX) XXX-XX-XX` |
| Behavior reused | 8→7 normalize, prepend 7, max 11 digits, `input` event formatting |

---

## 9. FP-0002 Phone Mask

| Item | Detail |
|------|--------|
| File | `assets/js/v9-shell.js` |
| Selectors | `input[type="tel"]`, `[name="phone"]`, `[data-phone-input]`, `[data-phone-mask]` |
| Forms | Final form + consultation modal (header/floating/footer triggers) |
| Placeholders | `+7 (___) ___-__-__` |
| Validation | `digits.length >= 10` (Triumph parity); incomplete values fail |
| Dynamic | Bind on boot + on modal open; `data-phone-mask-bound` prevents double init |
| Note | Prior Inputmask path was non-functional (vendor file absent) |

---

## 10. Database Changes

| Item | Result |
|------|--------|
| Exact writes | **none** |
| Unrelated writes | **none** |

---

## 11. Exact Files Changed

### Canonical source
- `WORDPRESS/theme/shpigovsky/404.php`
- `WORDPRESS/theme/shpigovsky/assets/css/fp02-404.css` *(new)*
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` *(operator promote)*
- `WORDPRESS/theme/shpigovsky/assets/img/404/404-visual.png` *(new)*
- `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js`
- `WORDPRESS/theme/shpigovsky/inc/assets.php`
- `WORDPRESS/theme/shpigovsky/inc/template-tags.php`
- `WORDPRESS/theme/shpigovsky/page-templates/institutional.php`
- `WORDPRESS/theme/shpigovsky/template-parts/components/final-form.php`
- `WORDPRESS/theme/shpigovsky/template-parts/layout/global-consultation-modal.php`

### Runtime
Exact copies of the same 10 paths under `wp-content/themes/shpigovsky/`.

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E62A-404-breadcrumb-wrapper-phone-mask.md`
- `REPORTS/evidence/v9-06e62a-404-breadcrumb-wrapper-phone-mask/**`
- `PROJECT-STATUS.md`, `WORDPRESS/SOURCE-AUTHORITY.md`

---

## 12. Source-to-Runtime Delivery

| Item | Result |
|------|--------|
| Method | Exact-file copy only (**no** broad sync) |
| Match | **10/10** SHA256 match after delivery |
| Operator CSS | Preserved (`E11627B9…`) |

---

## 13. Validation

| Area | Result |
|------|--------|
| 404 HTTP / body | 3/3 PASS |
| Breadcrumb wrappers | 9/9 PASS |
| Phone mask typing/paste | PASS (`+7 (999) 123-45-67`) |
| Viewports 404 | 1440 / 1024 / 480 / 370 screenshots captured |
| PHP warnings | 0 |
| JS errors (home/404 probes) | 0 observed in mask script path |
| Overflow 404@370 | not flagged in captured screenshots |

---

## 14. Regression

Routes checked HTTP expected: `/`, `/uslugi/`, `/uslugi/zavisimosti/`, alcohol service, `/specyalisty/`, gallery, `/o-centre/`, `/kontakty/`, `/blog/`, blog single, `/otzyvy/`, 404. Shared shell (header/footer/forms/lifebuoy) retained; operator crumb typography retained.

---

## 15. Open E61 Tails

Still open (not closed by E62A):

1. Founder’s Word reusable ACF ownership incomplete  
2. E61 full viewport/admin screenshot gap  
3. Nested CTA `<section>` risk in `#who-we-treat`  
4. Demo Blog posts remain (`#1745–1754`)  
5. Deep E61 regression tail  

---

## 16. Risks and SAFE UNKNOWN

| Item | Note |
|------|------|
| 404 visual crop | Cropped from PNG (silhouette/grey fringe may differ slightly from pure Figma export layer) |
| ACF JSON runtime gaps | 8 source-only groups still missing in runtime — unresolved pre-existing drift |
| Phone reopen teardown | Triumph also one-shot bind; reopen confirmed bound attr; full multi-open matrix partially exercised |
| Cursor mid-edit | Custom mask rewrites whole value on `input` (Triumph behavior) |

---

## 17. Git Status

- **No commit / no push / no freeze**
- Exact FP-0002 paths touched; foreign monorepo WIP untouched by this wave’s staging (none performed)

---

## 18. Operator Review Pages

Inspect:

1. `http://shpigovsky.test/this-page-definitely-does-not-exist-e62a/` (404 @ 1440/1024/480/370)  
2. `http://shpigovsky.test/o-centre/galereya-o-dome/` — breadcrumb wrapper  
3. `http://shpigovsky.test/specyalisty/` and one specialist child  
4. `http://shpigovsky.test/kontakty/`, `/otzyvy/`, `/blog/` — wrappers must stay specialized (not duplicated)  
5. Home / any page — «Заказать звонок» modal phone mask  
6. Home final-form phone field  
7. Confirm operator breadcrumb look unchanged after wrapper restore  
