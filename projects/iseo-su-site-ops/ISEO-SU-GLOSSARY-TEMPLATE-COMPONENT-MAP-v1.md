# ISEO-SU GLOSSARY TEMPLATE COMPONENT MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24  
**Rule:** no new CSS; map sections to existing site classes/components only.

## Shared chrome

| Section | Source component | Classes / includes |
|---------|------------------|--------------------|
| Document head | `header.php` | `wp_head`, favicons, LPTracker (existing) |
| Mobile menu | `template-parts/content-mobilemenu.php` | existing |
| Topbar | `template-parts/content-topbar.php` | existing |
| Footer blocks | `footer.php` + `content-footer.php` | existing Telegram / audit / footer |
| Body modifiers | `body_class` filter | `overlay_on`, `content` (same family as legal HTML pages) |

## Archive (`archive-glossary.php`)

| Section | Reused pattern | Classes |
|---------|----------------|---------|
| Hero / title band | privacy-policy `page_scene` | `page_scene`, `container`, `row`, `page_scene_inner`, `page_scene__description` |
| Breadcrumbs | privacy / blog | `ul.breadcrumbs` |
| H1 | privacy | plain `h1` inside scene |
| Scroll cue | privacy | `a.see_more_btn` |
| Intro + search | legal `content_block` + native form controls | `content_block`, plain `form` / `input` / `button` (no lead-form ids) |
| Alphabet nav | blog tag filter | `blog_filter`, `blog_filter__navigations`, `blog_filter__label`, `blog_filter__item`, `blog_filter__btn` |
| Letter groups | privacy body headings (not oversized section chrome) | `content_block` + plain `h2` + `ul`/`li`/`a` — **do not** wrap letter labels in `content_block__title` (that class is 88px section chrome used by Telegram/audit blocks) |
| Empty state | content paragraph | `content_block` + `p` |

Archive data source: dedicated `iseo_glossary_get_archive_posts()` query (not the main Loop). Draft term links use capability-gated preview URLs while public exposure is closed.

## Single (`single-glossary.php`)

| Section | Reused pattern | Classes |
|---------|----------------|---------|
| Hero / title | privacy `page_scene` | same scene stack as archive |
| Breadcrumbs | privacy / blog | `breadcrumbs` with archive link |
| Article body | legal content | `article.content_block` + paragraphs / `h2` |
| Synonyms | content heading + paragraph | `h2` + `p` |
| Back link | ordinary content link | `a` to archive |

## Intentionally not reused

| Pattern | Why |
|---------|-----|
| Blog article stats / likes / ratings / author | Task forbids fake meta |
| `blog_teaser` cards | Not needed; list semantics clearer |
| Lead forms (`*__FORM*`) | Avoid mail/common.js side effects |
| Offer template layout | Commercial KP-specific |

## CSS additions

**None.** No new stylesheet, no new selectors, no inline styles in glossary templates.

---

*Glossary template component map v1 · 2026-07-24.*
