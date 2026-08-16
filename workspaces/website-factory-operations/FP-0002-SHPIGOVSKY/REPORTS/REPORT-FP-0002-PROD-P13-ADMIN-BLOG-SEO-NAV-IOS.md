# REPORT — FP-0002 PROD-P13 Admin / Blog / SEO / Navigation / iOS

## 1. Status

- **PASS / PARTIAL**
- production file writes: **YES** (exact-file SFTP, 41 paths, then 2 hotfixes)
- DB/schema writes: **YES** (bounded: social migration flag + `social_platforms`; activity QA row delete)
- user writes: **YES** (reassign+delete `mli_admin_fp0002`; admin email; create `metacode`)
- settings migrations: **YES** (`social_links` → `social_platforms`, URLs preserved)
- WPilot writes: **0**
- commit/push: **none**

`OPERATOR/OLYA CURRENT PRODUCTION STATE PRESERVED`

`PROD-P13 TECHNICAL CLOSEOUT COMPLETE — OPERATOR/OLYA VISUAL + PHYSICAL DEVICE ACCEPTANCE PENDING`

PARTIAL items: requested `metacode` email already owned by `mars`; physical iPhone and MacBook trackpad QA pending; `WP_ENVIRONMENT_TYPE=local` residue left for P06.

## 2. Fresh Production Intake

- CWD `X:\AI MARS`, volume **AI WS**, branch `mars/canonical-post-recovery`.
- Intake: 57 files inspected — **54 MATCH / 2 DRIFT / 1 ABSENT_BOTH** (`fp02-search.js` never existed).
- Operator CSS drift canonized into local source **before** P13 edits:
  - `theme/assets/css/v9-style.css` (prod SHA `3314ea2527fbfecd…`)
  - `theme/assets/css/fp02-specialist-profile.css` (prod SHA `657b8d3eb05282ff…`)
- Olya DB/settings treated as authority. Social URLs not rewritten.
- Root cause of «LOCAL / Not production» notice: MU-plugin `mars-local-runtime.php` + `wp-config.php` `WP_ENVIRONMENT_TYPE='local'` leftover from local-stage import. Notices removed; constants left for P06.

`OPERATOR/OLYA CURRENT PRODUCTION STATE INTAKE COMPLETE`  
`OPERATOR FILE/CSS DRIFT PRESERVED AND CANONIZED`

## 3. Rollback

- Operator statement: a fresh Beget files+DB backup from the current working period was treated as **current / ACKNOWLEDGED**. P13 did **not** create a new full Beget backup.
- Exact-file Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p13-layer-b-pre\` (current production bytes + SHA-256 per relative path).
- Exact-object DB snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p13-db-snapshots\` (`db-mutate-result.json` before/after objects; no passwords).

`PROD-P13 EXACT-FILE / EXACT-OBJECT ROLLBACK READY`

## 4. Users

- `mli_admin_fp0002` removed: **YES** (ID 1). Content reassigned to `admin` ID 2 (`wp_delete_user(1, 2)`). Privacy page `#3` author now 2. Content not deleted.
- Olya/`admin` email updated to `ola4seo@yandex.ru`. Login/role preserved. Display name left as production value `admin` (not overwritten to «Ольга Дягилева»). Email-change notification filters disabled; MU mail suppress still on.
- `metacode` created: **YES** (ID 4, Administrator). Requested email `support@polygon-ws.ru` is already owned by `mars` (ID 3) → unique `metacode@polygon-ws.ru` used. **PARTIAL on email.** Password is **not** stored in this report.

## 5. Raw Options Admin Screen

- Owner: **ACF Extended PRO** (`acf-extended-pro/acf-extended.php`).
- Method: `acf_update_setting('acfe/modules/options', false)` + `acfe/modules/options/admin` → false + targeted `remove_menu_page` / title match `Options` (Site Settings slugs `fp02-site-settings*` excluded).
- ACFE not uninstalled. `wp_options` data not deleted.

`RAW OPTIONS ADMIN SCREEN REMOVED FROM NORMAL PRODUCTION UX`

## 6. Activity Log V2

- Menu remains **Журнал действий**.
- Columns: Дата и время / Пользователь / Действие / Тип / Объект (i18n source English + `ru_RU` pack).
- User ID 0 → **Система** (never `#0`). Filters include System.
- Object types: Страница / Статья / Услуга / Специалист / Отзыв.
- Object: title + edit link + secondary `#id`.
- Filters: user / action / type. Pagination 50. Newest first. `wp-list-table`.
- Exact P12 QA rows (titles `FP02 P12 QA%` / `FP02 P12 Collision%`) deleted: **7**. Operator/Olya history retained.

## 7. Admin System UX

- Global LOCAL MARS notice: **removed** (MU-plugin neutralized).
- ACFE «does not use ACFE APIs» global notice: **removed** from `AcfIntegration` (ACF Pro missing error kept).
- Root cause: display + leftover `WP_ENVIRONMENT_TYPE=local` in `wp-config.php` (not a live local host). Mail suppress kept. `home`/`siteurl` write guard **removed** (cutover risk).
- Dashboard widget **MetaCODE / Состояние системы** (`fp02_metacode_system_state`): FP-0002, runtime classification, WP version, theme/core versions, WPilot active/writes disabled, MU-plugin residue note. No secrets.

`MARS/METACODE SYSTEM INFO MOVED TO A SINGLE DASHBOARD WIDGET`

## 8. i18n

- Domains: `shpigovsky-core`, `shpigovsky`.
- P13 modules use English source strings + `ru_RU` / `en_US` PO/MO.
- Existing large ACF Russian source strings were **not** rewritten (stable convention).
- Locale QA via `switch_to_locale` only; production `WPLANG` remains `ru_RU`.
  - `ru_RU`: `Import from Word` → `Импорт из Word`; `System` → `Система`
  - `en_US`: `Журнал действий` → `Activity log`

`FP-0002 CUSTOM ADMIN/UI HAS WORKING ru_RU + en_US LANGUAGE PACKS`

## 9. DOCX Publisher

- Admin: **Статьи → Импорт из Word**.
- Multiple `.docx`, per-file status, draft links, discard, schedule via normal WP `future`/`publish`.
- No auto-publish. ZipArchive + `LIBXML_NONET`. Images via `wp_upload_bits`. HTML `wp_kses_post`.
- Capability `edit_posts` / nonce / MIME / 15 MB / path traversal blocked / temp not in webroot for parser.
- Template: plugin `assets/docx/fp02-article-template.docx` + `DOCS/assets/fp02-article-template.docx`.
- QA: parse OK, Title/H2/H3/lists, draft `#2008` created then discarded.

`BLOG DOCX → WORDPRESS DRAFT WORKFLOW LIVE`

## 10. SEO Meta Ownership

- Types: `page`, `post`, `service`, `specialist`. Reviews: no public single → no fields.
- Fields: SEO Title (`fp02_seo_title`), Meta Description (`fp02_seo_description`).
- Fallbacks: empty title → WordPress `title-tag` (object title + site name). Empty description → **omit** (no invented copy).
- No Yoast/Rank Math. Output owner: theme `inc/seo-entity-meta.php` (`document_title_parts` + `wp_head`).

`PUBLIC CONTENT ENTITIES HAVE EDITABLE SEO TITLE + META DESCRIPTION`

## 11. Hero

- First slide only: valid `<h1 class="hero__title"><span class="hero__tagline">…</span><span class="hero__title-main">…</span></h1>` (no `<p>` inside `<h1>`).
- Other slides remain non-H1. Home HTTP: **1** `<h1>`, tagline span present.
- Visual metrics for `.hero__title-main`: 70 / 50 / 40 / 30 px matching previous `.hero__title`. Tagline keeps existing `.hero__tagline` rules.

`HOME HERO HAS ONE SEMANTIC H1 WITH CURRENT VISUAL APPEARANCE PRESERVED`

## 12. Child Services CTA

- Button **Записаться на консультацию** in `.services-category-section-v2__actions` on the child-services template (hidden when the section is not rendered).
- Existing consultation modal (`data-modal-open="consultation"`). Red/`btn_dark`, left-aligned.
- HTTP `/uslugi/zavisimosti/`: CTA present.

`CHILD SERVICES CONSULTATION CTA LIVE`

## 13. CSS

- `.plain-page-content__title` font-weight **400** (was 600).
- `.site-search-suggest__heading` font-weight **500** (was 600).
- Operator CSS otherwise preserved; P13 additive CSS appended (hero H1 wrapper, dropdown, offcanvas submenu, subdivision actions).

## 14. Slug FIX01

P12 `save_post` + second `wp_update_post` lost to core/ACF rewrite — rejected.

FIX01: persist via `wp_insert_post_data` priority 99; native slug box + metabox `fp02_post_name`; empty → regenerate from title.

Draft collision: core `wp_unique_post_slug` returns early for drafts, so uniqueness is done in `make_unique_slug` (`-copy-01`).

QA (cleanup after):

| Entity | Persist | Empty regen | Collision |
|---|---|---|---|
| `service` | `fp02-p13-slug-persist` | from title | `…-copy-01` |
| `specialist` | `fp02-p13-spec-persist` | — | — |

Public CPTs with singles: `service`, `specialist` (plus core `post`/`page` native). Reviews: no public single.

`CUSTOM ENTITY SLUG EDIT PERSISTS AFTER SAVE + RELOAD`

## 15. Carousel Trackpad

- Library: **Swiper** (`swiper-bundle.min.js`).
- `mousewheel: { enabled, forceToAxis, releaseOnEdges }` via `attachFp02SliderNav` / infrastructure sliders.
- Hero Swipers excluded (earlier-wave exception preserved).
- No global `preventDefault` on wheel. Vertical-dominant gestures should release to page scroll (`forceToAxis` + `releaseOnEdges`).
- `MACBOOK TRACKPAD PHYSICAL QA = OLYA PENDING`

## 16. Blog TOC

- Owner: theme `inc/blog-helpers.php` (server-side).
- H2 only; H3 ignored for TOC; IDs assigned deterministically; existing IDs preserved when unique.
- Sample article `#750` `/blog/nazvanie-stati/`: **5** H2 TOC items; HTTP `toc_present=true`. Hidden when no H2s.

`BLOG TOC AUTO-GENERATES FROM ARTICLE H2 HEADINGS`

## 17. Social/Messenger Settings

- New options subpage + repeater: type / URL / show_header / show_footer.
- Types with existing icons: Telegram, WhatsApp, MAX (`max.svg`), YouTube (FA).
- Migration mapped «What's up» + `wa.me` → `whatsapp` without changing the URL.
- Legacy repeater hidden, data kept.

`SOCIAL/MESSENGER LINKS HAVE ONE ADMIN SOURCE OF TRUTH`

## 18. Social Frontend QA

- Header / floating / offcanvas: `show_header`.
- Footer: `show_footer`.
- Contacts: all configured URLs (flags independent).
- Home HTTP: Telegram + WhatsApp hrefs present; `whatsapp.svg` present; YouTube FA **0**.

`FOOTER SOCIAL/MESSENGER BUTTONS VISUALLY RESTORED`

## 19. Second-Level Navigation

- WordPress menu parent/child (`depth => 2`), no second data model.
- Desktop: dropdown, hover + `:focus-within`, `is-open`, Escape, parent link remains an `<a>`.
- Mobile: separate expand button, `aria-expanded` / `aria-controls`, submenu `hidden`.
- HTTP: submenu markup present on current primary menu.

`MAIN NAVIGATION SECOND LEVEL LIVE ON DESKTOP + MOBILE`

## 20. iOS Lifebuoy FIX02

- P12 physical FAIL acknowledged; translate3d/contain-on-fixed-root rejected as sufficient.
- New root cause: iOS containing-block / compositor freeze when the **fixed root** is transformed/contained; motion could be mathematically applied yet visually static.
- Strategy: iOS `top`/`left` fallback + `visualViewport`; Windows/Android transform path kept.
- Technical implementation LIVE. **Do not claim physical PASS.**

`IOS LIFEBUOY FIX02 IMPLEMENTED`  
`PHYSICAL IPHONE QA = OLYA PENDING`

## 21. Exact Files Changed

Theme `WORDPRESS/theme/shpigovsky/`: `assets/css/v9-style.css`, `fp02-search.css`, `fp02-lifebuoy-parallax.css`; `assets/js/fp02-lifebuoy-parallax.js`, `v9-shell.js`; `functions.php`; `inc/site-chrome.php`, `contacts-helpers.php`, `blog-helpers.php`, `nav-walker.php`, `seo-entity-meta.php`; `template-parts/home/hero.php`; `template-parts/service/children.php`; `template-parts/navigation/footer-social.php`, `messenger-links.php`, `primary-desktop.php`, `offcanvas.php`; `languages/shpigovsky*.{pot,po,mo}`.

Plugin `WORDPRESS/plugins/shpigovsky-core/`: `shpigovsky-core.php`; `src/ModuleRegistry.php`; `src/Admin/PermalinkSlugUX.php`, `ActivityLog.php`, `AdminMenuHygiene.php`, `SystemDashboard.php`, `DocxImporter.php`, `OptionsPage.php`; `src/Fields/AcfIntegration.php`, `FieldGroups.php`, `SeoEntityMeta.php`, `SocialPlatformsOptions.php`; `languages/shpigovsky-core*.{pot,po,mo}`; `assets/docx/fp02-article-template.docx`.

MU: `WORDPRESS/mu-plugins/mars-local-runtime.php` → production `wp-content/mu-plugins/mars-local-runtime.php`.

Docs: `DOCS/assets/fp02-article-template.docx`; `WORDPRESS/architecture/FP-0002-PROD-P13-OWNERSHIP-NOTES-v1.md`; this report; `PROJECT-STATUS.md`.

## 22. Exact DB/Schema/User Objects Changed

- User 1 `mli_admin_fp0002` deleted; authored posts/pages reassigned to user 2.
- User 2 email → `ola4seo@yandex.ru`.
- User 4 `metacode` created (Administrator).
- Option `fp02_social_platforms_migrated` = 1; ACF `social_platforms` written from legacy URLs.
- Deleted 7 P12 QA activity-log rows. No table-wide content rewrites. No broad options/user cleanup. No permalink mass regen. No ACF JSON sync.

## 23. Source / Production Parity

**41/41 MATCH** (deploy manifest, including hotfix SHA updates for `PermalinkSlugUX.php` and the DOCX template).

## 24. Regression

Frontend smoke (HTTP): home, hero H1=1, `/uslugi/`, `/uslugi/zavisimosti/` CTA, `/specyalisty/`, blog article TOC, footer/header socials, `/kontakty/`, sitemap/robots untouched (`blog_public=0`). Smart Search CSS weight 500. Lifebuoy FIX02 assets deployed.

Admin (PHP modules present): dashboard widget class, Options hygiene class, DOCX importer, slug UX, SEO group, social group, activity log V2. Global LOCAL MARS string absent from public HTML and MU-plugin.

P07–P12 surfaces not intentionally regressed; operator visual still pending.

## 25. WPilot

- `write_enabled=false`
- `metacode_wpilot_write_enabled=false`
- business writes **0**

## 26. Secret Safety

- evidence secrets **0**
- Git secrets **0**
- metacode password not written to repository, evidence, or this report

## 27. Git

- commit **none**
- push **none**
- foreign WIP **untouched** (including staged `projects/client-ops-reporting-bridge/` and unrelated `??` / `M` paths)

## 28. Deferred Plan

- Olya final visual check
- physical iPhone lifebuoy
- MacBook trackpad
- final backup
- Git checkpoint
- P06 leftover local/dev residue (`WP_ENVIRONMENT_TYPE`, debug log path, mail suppress, `mars` account)
- typography residual
- SMTP
- pre-cutover audit
- domain/SSL
- robots/indexing
- sitemap submissions

## 29. Acceptance

`PROD-P13 TECHNICAL CLOSEOUT COMPLETE — OPERATOR/OLYA VISUAL + PHYSICAL DEVICE ACCEPTANCE PENDING`

## 30. Final operator-only credential

Not stored on disk. Delivered only in the Cursor user-visible last line.
