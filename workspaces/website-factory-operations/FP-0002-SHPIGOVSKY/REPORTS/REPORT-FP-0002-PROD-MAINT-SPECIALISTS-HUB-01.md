# REPORT — FP-0002 SPECIALISTS HUB IMPLEMENTATION 01

**Date:** 2026-08-24  
**Project:** FP-0002 — Шпиговский  
**Production:** https://shpigovsky.ru/  
**Wave:** Specialists Hub production implementation (`/specyalisty/`)  
**Verdict:** **PASS**

---

## 1. Verdict

**PASS**

Dedicated Specialists Hub is live on Page `#1030` (`https://shpigovsky.ru/specyalisty/`). Current published specialists render automatically via existing helper/card system. No new visual CSS. Reusable-block ownership reused. Indexing remained OPEN. `/specialisty/` untouched. Source↔runtime semantic parity **7/7**. Selective commit/push completed from clean worktree.

---

## 2. Current-origin preflight

| Check | Result |
|------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Fetched origin tip (implementation base) | `251959293c2046dd06e2996e08701d6856698891` |
| Clean worktree | `X:\AI MARS\worktrees\fp0002-specialists-hub-01` |
| Worktree branch | `wave/fp0002-specialists-hub-01` → tracks `origin/mars/canonical-post-recovery` |
| Shared dirty main | **not used** (foreign WIP preserved) |

---

## 3. Fresh production / editorial intake

Evidence: `REPORTS/evidence/prod-maint-specialists-hub-01/01-intake.json`

| Surface | Fresh truth |
|---------|-------------|
| Page `#1030` | title `Специалисты`, slug `specyalisty`, status `publish` |
| Template (pre) | `page-templates/generic.php` |
| `generic_page_body` / `post_content` | historical placeholder still present |
| `generic_page_lead` | empty |
| `generic_page_reusable_blocks` | empty |
| `page_layout_mode` | `full` |
| SEO ACF title/description | empty (Page remains SEO owner) |
| Published specialists | **9** (menu_order 10…80) |
| Hub template file | missing pre-deploy |
| Core | `0.3.25-olya-robots` |
| `blog_public` | `1` |
| robots SHA | `2594093919…` (unchanged later) |

Placeholder confirmed identical to historical text → authorized clear.

---

## 4. Root cause confirmed

**HUB NEVER IMPLEMENTED.**

Page + CPT singles were healthy; listing presentation for `/specyalisty/` was never built. Generic Content showed preparation placeholder. No routing collision; not source/runtime drift.

---

## 5. Implementation

| Surface | Path |
|---------|------|
| Page template | `WORDPRESS/theme/shpigovsky/page-templates/specialists-hub.php` (`Template Name: Specialists Hub`) |
| Hub shell | `WORDPRESS/theme/shpigovsky/template-parts/specialist/hub-content.php` |
| Listing | `WORDPRESS/theme/shpigovsky/template-parts/specialist/hub-list.php` |
| Fancybox gate | `WORDPRESS/theme/shpigovsky/inc/fancybox-vendors.php` (also allow Specialists Hub) |
| ACF location extend | `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` (`group_fp02_page_generic_content`) |
| ACF JSON | `WORDPRESS/acf-json/group_fp02_page_generic_content.json` |
| Core version | `0.3.26-specialists-hub` |

Data owner unchanged: `shpigovsky_get_specialists_cards()` (CPT `specialist`, `menu_order`, published-only).

---

## 6. Existing design / component reuse

**No new visual CSS.**

Reused:

- page shell: `page-plain-content__main`, `plain-page-content`, `container`, `plain-page-content__title`, `plain-page-content__body`, `generic-content-page__lead`
- breadcrumbs: `shpigovsky_render_breadcrumbs()` / internal-page-nav shell
- cards: `specialists__card`, `specialists__card-link`, `specialists__photo`, `specialists__name`, `specialists__role`
- static responsive grid primitive: `home-feature-grid__card-grid` (existing 3→2→1 breakpoints)
- reusable blocks markup/order: same as Generic Content (`generic-content-page__reusable`)

Hub is **static grid**, not carousel (no `data-specialists-slider` on hub).

---

## 7. Reusable blocks

| Layer | Behavior |
|-------|----------|
| Admin ownership | Same field `generic_page_reusable_blocks` (checkbox) under group `group_fp02_page_generic_content` |
| Location | OR: Generic Content **or** Specialists Hub templates |
| Frontend order | intro/body (optional) → specialists listing → reusable blocks → footer |
| Storage key | unchanged (no duplicate field) |
| Current Page `#1030` selection | empty (structurally wired; no fake QA content inserted) |

---

## 8. Page `#1030` changes

| Field | Action |
|-------|--------|
| `_wp_page_template` | `generic.php` → `specialists-hub.php` |
| `generic_page_body` | cleared (exact historical placeholder) |
| `post_content` | cleared (same placeholder) |
| lead / reusable / SEO / title / slug / status | **preserved** |

---

## 9. Deployment

Exact-file SFTP upload + bounded PHP mutation (WPilot write **OFF**).

Deployed:

1. `specialists-hub.php`
2. `hub-content.php`
3. `hub-list.php`
4. `fancybox-vendors.php`
5. `FieldGroups.php`
6. `shpigovsky-core.php`
7. `group_fp02_page_generic_content.json` → production `wp-content/acf-json/`

Manifest: `REPORTS/evidence/prod-maint-specialists-hub-01/02-deploy-manifest.json`  
Mutation: `…/03-mutate.json`

---

## 10. Live QA

Evidence: `…/04-live-qa.json`

| Area | Result |
|------|--------|
| Hub HTTP | 200 |
| H1 / breadcrumbs | present |
| Placeholder | gone |
| Cards | 9 / 9, no duplicates |
| Order | matches current `menu_order` |
| Links | all `/specyalisty/{slug}/` |
| No hub swiper | PASS |
| Singles smoke | shpigovsky / kostyuk / filippova → 200 |
| Home specialists slider | present (9 cards) |
| Services specialists | present on `/uslugi/zavisimosti/` (+ alcohol child) |
| `/specialisty/` | still 404 |
| PHP fatals/warnings on hub | none |

Responsive: hub uses existing `home-feature-grid__card-grid` breakpoints (3 / 2 / 1). No custom responsive CSS added.

---

## 11. SEO / indexing / robots safety

| Check | Result |
|-------|--------|
| Canonical hub | `/specyalisty/` |
| `/specialisty/` redirect | **not added** (operator deferred) |
| `blog_public` | `1` throughout |
| robots.txt SHA | unchanged `2594093919…` |
| sitemap | 200 |
| Page `#1030` SEO owner | preserved |

---

## 12. Production ↔ source parity

`05-parity.json` → **PASS 7/7** (LF-normalized semantic match).

Page config after deploy: template `specialists-hub.php`, body/content empty, core `0.3.26-specialists-hub`, `blog_public=1`.

---

## 13. Backup / rollback

- Operator **full Beget backup** before wave: **acknowledged**.
- Bounded Layer B snapshots: `REPORTS/evidence/prod-maint-specialists-hub-01/layer-b-pre/` + `layer-b-pre-deploy/` + intake/mutate JSON.

### Rollback (exact)

1. Restore Page `#1030` template meta to `page-templates/generic.php`.
2. If needed, restore prior `generic_page_body` / `post_content` from `03-mutate.json` → `before` (placeholder only).
3. Restore/remove only wave files from Layer B snapshots (theme hub templates + fancybox + FieldGroups + core header + acf-json). Do **not** full theme/DB restore.

---

## 14. Files changed (source)

- `WORDPRESS/theme/shpigovsky/page-templates/specialists-hub.php` (**new**)
- `WORDPRESS/theme/shpigovsky/template-parts/specialist/hub-content.php` (**new**)
- `WORDPRESS/theme/shpigovsky/template-parts/specialist/hub-list.php` (**new**)
- `WORDPRESS/theme/shpigovsky/inc/fancybox-vendors.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php`
- `WORDPRESS/acf-json/group_fp02_page_generic_content.json`
- `PROJECT-STATUS.md`
- `REPORTS/REPORT-FP-0002-PROD-MAINT-SPECIALISTS-HUB-01.md` (this file)
- `REPORTS/evidence/prod-maint-specialists-hub-01/**`
- `REPORTS/FP-0002-NEXT-WEBGPT-HANDOFF.md` (tip update)

---

## 15. Git

See closeout section after push (commit SHA + final `origin/mars/canonical-post-recovery` tip).

---

## 16. Residuals

- `/specialisty/` alias/redirect — **intentionally deferred** by operator (discuss with Olya later). Not an immediate action item.
- Olya may later fill hub lead/body and select reusable blocks via Admin (fields already available).

---

## 17. WP Forge harvesting

**NO NEW HARVEST REQUIRED.**

Reuse of existing Generic Content reusable-block ownership + specialist card helper + feature-grid primitive is consistent with already harvested FP-0002 patterns. No new architectural lesson beyond “hub page was never implemented.”

---

## 18. Mutation statement

**Intentionally changed:**

- Added Specialists Hub theme presentation files.
- Extended existing ACF generic content group location to Specialists Hub.
- Bumped core to `0.3.26-specialists-hub`.
- Assigned Page `#1030` template to Specialists Hub.
- Cleared confirmed historical preparation placeholder from Page `#1030` body/content.

**Preserved:**

- All specialists CPT entities / ACF profiles / `menu_order`.
- Hub slug `/specyalisty/`, title, SEO ownership, empty lead, empty reusable selection.
- robots, indexing OPEN, forms/SMTP/anti-spam/privacy/Metrika/P18G/watchdog.
- Home/service specialist sliders.
- `/specialisty/` (still 404, no redirect).
- Foreign WIP on shared dirty main.
