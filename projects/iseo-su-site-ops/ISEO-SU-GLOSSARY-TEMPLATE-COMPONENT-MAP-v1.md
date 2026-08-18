# ISEO-SU GLOSSARY TEMPLATE COMPONENT MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-08-18  
**Rule:** no new CSS; map sections to existing site classes/components only.

## Shared chrome

| Section | Source component | Classes / includes |
|---------|------------------|--------------------|
| Document head | `header.php` | `wp_head`, favicons, LPTracker (existing) |
| Mobile menu | `template-parts/content-mobilemenu.php` | existing |
| Topbar | `template-parts/content-topbar.php` | existing |
| Footer blocks | `footer.php` + `content-footer.php` | existing Telegram / audit / footer |
| Body modifiers | `body_class` filter | `overlay_on`, `content` (same family as legal HTML pages) |
| Glossary hero helper | `template-parts/content-glossary-page-scene.php` | services `page_scene` copy; archive vs single via `$args['context']` |

## Archive (`archive-glossary.php`)

| Section | Reused pattern | Classes |
|---------|----------------|---------|
| Hero / title band | `/services.html` `page_scene` (rates omitted) | `page_scene`, `container`, `row`, `page_scene_inner`, `page_scene__description`, `page_scene__btns`, `page_scene__btn_order`, `page_scene__info`, `page_scene__info_wrap`, `see_more_btn` |
| Decorative asset | services SVG | `/img/services_title_img.svg` |
| Breadcrumbs | services / privacy | `ul.breadcrumbs` — Главная → Глоссарий |
| H1 | services | plain `h1` inside scene: `Глоссарий` |
| Archive description | services `span` after H1 | exact operator sentence; not duplicated in `content_block` |
| CTA | services button classes, not modal | `a.page_scene__btn_order` `href="#SecondScreen"` label `Подробнее` (no `modalbox`) |
| Scroll cue | services | `a.see_more_btn` |
| Search | legal `content_block` + native form | `content_block`, plain `form` / `input` / `button` (no lead-form ids); wrapper `<main id="SecondScreen">` |
| Alphabet nav | blog tag filter | `blog_filter`, `blog_filter__navigations`, `blog_filter__label`, `blog_filter__item`, `blog_filter__btn` |
| Letter groups | privacy body headings (not oversized section chrome) | `content_block` + plain `h2` + `ul`/`li`/`a` — **do not** wrap letter labels in `content_block__title` (that class is 88px section chrome used by Telegram/audit blocks) |
| Empty state | content paragraph | `content_block` + `p` |

Archive data source: dedicated `iseo_glossary_get_archive_posts()` query (not the main Loop). Draft term links use capability-gated preview URLs while public exposure is closed.

## Single (`single-glossary.php`)

| Section | Reused pattern | Classes |
|---------|----------------|---------|
| Hero / title | same services `page_scene` helper | same scene stack as archive; **no** description `span` |
| Breadcrumbs | services / blog | `breadcrumbs` with archive link + current `the_title()` |
| H1 | services | canonical post title |
| CTA | same as archive | `Подробнее` → `#SecondScreen` |
| Article body | legal content | `article.content_block` + paragraphs / `h2` inside `<main id="SecondScreen">` |
| Synonyms | content heading + paragraph | `h2` + `p` |
| Back link | ordinary content link | `a` to archive |

## Intentionally not reused

| Pattern | Why |
|---------|-----|
| `.page_scene__rates` | Operator: do not render on glossary |
| `modalbox` / consultation popup | CTA must not open forms |
| Blog article stats / likes / ratings / author | Task forbids fake meta |
| `blog_teaser` cards | Not needed; list semantics clearer |
| Lead forms (`*__FORM*`) | Avoid mail/common.js side effects |
| Offer template layout | Commercial KP-specific |

## CSS additions

**None.** No new stylesheet, no new selectors, no inline styles in glossary templates.

## JS additions

Glossary-only `wp_add_inline_script` on `iseoblog-common`: same 1000ms `animate` as production `.see_more_btn` for the yellow CTA. Does not modify `js/common.js`.

---

*Glossary template component map v1 · updated 2026-08-18 services page_scene alignment.*
