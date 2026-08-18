# REPORT — ISEO-SU SITE OPS GLOSSARY PAGE_SCENE SERVICES ALIGNMENT

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT  
**Date:** 2026-08-18  
**Final status:** **COMPLETE — GLOSSARY HERO ALIGNED TO SERVICES / SECOND-SCREEN CTA WORKING**

---

## 1. Execution Summary

Glossary archive and all public glossary singles now render a structural copy of the production `/services.html` `page_scene`. `.page_scene__rates` is not rendered on glossary routes. Archive H1 is `Глоссарий` with the operator description `span`. Singles use the canonical term title and have no hero description. CTA is `Подробнее` → `#SecondScreen` and smooth-scrolls. `/services.html` SHA unchanged. 184 published glossary articles untouched.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:), healthy |
| Branch | `mars/canonical-post-recovery` |
| HEAD (start) | `b7b1144e3d103af8d103ce2b5c588658b534cd8e` |
| origin/mars/canonical-post-recovery | `e49af6317b961a008df26e4a31c4e7ada8a4f013` |
| Unpushed commits | **present** (pre-existing; this task did not push) |
| Staged index | **not empty** — foreign `client-ops-reporting-bridge` WIP preserved; not included in this commit |
| Foreign WIP | preserved (no pull / reset / clean / stash) |

## 3. Backup State

| Layer | Evidence |
|-------|----------|
| Full hosting | Operator confirmed fresh full production backup before this task; agent did not open Beget |
| Scoped theme backups | Remote `*.bak-glossary-heroalign-20260818T062716Z` for overwritten files |
| Local rollback copies | `projects/iseo-su-site-ops/_glossary-scratch/hero-align/rollback-20260818T062716Z/` |
| DB backup | **not taken** — no database write |

## 4. Operator Requirements

Implemented as chartered: services-structure hero; no rates; glossary breadcrumbs/H1; archive-only exact description; singles without hero description; `Подробнее` → `#SecondScreen`; reuse existing scroll; no new CSS; no unrelated surfaces.

## 5. Services Hero Source

Authoritative file: production `services.html` (not browser-only reconstruction). Block lives in `<header>` after the shared topbar include. Classes: `page_scene`, `page_scene_inner`, `page_scene__description`, `page_scene__btns`, `page_scene__btn_order`, `page_scene__rates` (omitted on glossary), `page_scene__info`, `see_more_btn`. Decorative asset: `img/services_title_img.svg`. CTA originally `modalbox` → `#callback__FORM_popup`.

## 6. Previous Glossary Implementation

Privacy-style compact hero in `archive-glossary.php` and `single-glossary.php`. Intro paragraph on archive lived under `<main>`. `id="SecondScreen"` already on `<main>`. `see_more_btn` already pointed at it.

## 7. Source Changes

| File | Change |
|------|--------|
| `template-parts/content-glossary-page-scene.php` | **new** shared hero |
| `archive-glossary.php` | include helper; move description out of `content_block` |
| `single-glossary.php` | include helper; article body unchanged |
| `inc/glossary-helpers.php` | glossary-only inline scroll on `iseoblog-common` |

## 8. Archive Hero

Services structure. Breadcrumb Главная → Глоссарий. H1 `Глоссарий`. Description `span` with the exact operator sentence. CTA `Подробнее`. No rates. Illustration is the existing services SVG.

## 9. Single Hero

Same structure. Breadcrumb Главная → Глоссарий → current `the_title()`. H1 = canonical title. No description `span`. Same CTA. No rates.

## 10. Breadcrumbs

Markup/classes match services (`ul.breadcrumbs`). Archive current item unlinked. Single `Глоссарий` uses `get_post_type_archive_link( 'glossary' )`; term uses `the_title()`.

## 11. Description Rules

Archive: one `span` in the hero, exact text, removed from `content_block` so it appears once. Singles: span omitted (not empty). Article excerpt remains in the article, not the hero.

## 12. CTA and SecondScreen

CTA classes: `page_scene__btn_order` only (no `modalbox`). `href="#SecondScreen"`. Target remains the existing `<main id="SecondScreen">` (archive: search/alphabet/list; single: article). Count = 1 per page.

## 13. Smooth Scroll

Existing `js/common.js` `$(".see_more_btn").click(...)` animate (1000ms) still applies to the copied arrow. Glossary-only `wp_add_inline_script` applies the same animate to the yellow CTA. `common.js` not modified. Degrades to native hash jump without JS.

## 14. No-New-Style Validation

No new stylesheet, selector, or inline style. No glossary-specific background or new decorative file.

## 15. Production Deployment

SFTP overwrite of four theme files, stamp `20260818T062716Z`. Receipt: `_glossary-scratch/hero-align/deploy-heroalign-receipt.json`. `services.html` not uploaded.

## 16. Archive Validation

| Check | Result |
|-------|--------|
| HTTP | 200 |
| `page_scene` count | 1 |
| `.page_scene__rates` | 0 |
| H1 | `Глоссарий` |
| Description | exact text, once |
| CTA | `Подробнее` `#SecondScreen` |
| `#SecondScreen` | 1, on `<main>` |
| Search | works (`glossary_q=nofollow` → 1 term) |
| Alphabet | present |
| Unique term links | **184** |

## 17. Single Validation

| URL | HTTP | H1 | Hero desc | CTA | SecondScreen |
|-----|------|----|-----------|-----|--------------|
| `/glossary/apdejt-algoritma` | 200 | Апдейт алгоритма | none | Подробнее | 1 |
| `/glossary/nofollow` | 200 | Nofollow | none | Подробнее | 1 |
| `/glossary/geo` | 200 | GEO | none | Подробнее | 1 |
| `/glossary/e-e-a-t` | 200 | E-E-A-T | none | Подробнее | 1 |
| `/glossary/core-web-vitals` | 200 | Core Web Vitals | none | Подробнее | 1 |
| `/glossary/robots-txt` | 200 | robots.txt | none | Подробнее | 1 |
| `/glossary/kanonicheskij-url` | 200 | Канонический URL | none | Подробнее | 1 |
| `/glossary/snippet` | 200 | Сниппет | none | Подробнее | 1 |

Article content and related-term lists unchanged except vertical position under the taller hero.

## 18. Mobile Validation

Playwright 390×844 on archive, `/nofollow`, `/geo`: H1 readable; breadcrumbs wrap; yellow button in view; archive description wraps; singles have no hero span and layout remains intact; decorative SVG stacks with existing `media.css`. Click `Подробнее` scrolls. Horizontal delta: glossary `scrollWidth` 395 vs viewport 390 (**5px**). `services.html` at the same width has no overflow. Cause: WP theme `style.css` `.row` padding on glossary (WP) routes; static `services.html` does not load that file. No new CSS added (charter). Not treated as a new visual concept.

## 19. Services Regression

`https://i-seo.su/services.html` HTTP 200. H1 still `SEO&nbsp;услуги для&nbsp;вашего бизнеса`. Description unchanged. `Бесплатная консультация` + `modalbox` + `#callback__FORM_popup` unchanged. `.page_scene__rates` still present. File SHA-256 identical before and after this task.

## 20. Site Regression

| URL | HTTP | Fatal |
|-----|------|-------|
| `/` | 200 | no |
| `/services.html` | 200 | no |
| `/blog/` | 200 | no |
| `/tariff-calc` | 200 | no |
| `/offers` | 200 | no |
| `/privacy-policy.html` | 200 | no |
| `/glossary` | 200 | no |
| representative singles | 200 | no |

No maintenance mode. WPilot / plugins / WP core untouched.

## 21. Rollback Readiness

Restore `archive-glossary.php`, `single-glossary.php`, `inc/glossary-helpers.php` from `.bak-glossary-heroalign-20260818T062716Z`. Remove `template-parts/content-glossary-page-scene.php` (new file). Leave post statuses and bodies untouched. Full Beget restore not required unless bounded restore fails.

## 22. Files Created or Updated

**Created**

- `wordpress/iseoblog-glossary/template-parts/content-glossary-page-scene.php`
- `ISEO-SU-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-PAGE-SCENE-SERVICES-ALIGNMENT.md`

**Updated**

- `wordpress/iseoblog-glossary/archive-glossary.php`
- `wordpress/iseoblog-glossary/single-glossary.php`
- `wordpress/iseoblog-glossary/inc/glossary-helpers.php`
- `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md`
- `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `OPERATIONAL-INDEX.md`

Scratch/deploy receipts under `_glossary-scratch/hero-align/` are local operational files, not Git persistence.

## 23. Production Mutations

SFTP only, theme `iseoblog`, four paths listed above. No DB writes. No `services.html` write. No plugin/WPilot/core/menu/sitemap mutation.

## 24. Git Persistence

One scoped commit after validation. Subject: `fix(iseo-su): align glossary hero with services page`. **No push.** Foreign staged WIP excluded via pathspec-only commit.

## 25. Operator Review

Visual review of `/glossary` and any term single against `/services.html` hero (rates expected only on services). Confirm yellow `Подробнее` scrolls to search/listing or article, not to a modal.

## 26. Stop Condition

**COMPLETE — GLOSSARY HERO ALIGNED TO SERVICES / SECOND-SCREEN CTA WORKING**

No further glossary redesign or SEO phase started.

---

*REPORT · 2026-08-18 · stamp 20260818T062716Z.*
