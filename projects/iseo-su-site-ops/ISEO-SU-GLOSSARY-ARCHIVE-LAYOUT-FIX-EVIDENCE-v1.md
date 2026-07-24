# ISEO-SU GLOSSARY ARCHIVE LAYOUT FIX EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-ARCHIVE-EMPTY-STATE-AND-LAYOUT-FIX  
**Date:** 2026-07-24  
**Site:** https://i-seo.su/

---

## 1. Defect

Authenticated glossary archive preview rendered an orphan `#` group heading, a tall yellow dotted vertical column, no visible term titles, and an abnormally tall page that pushed the footer far down — despite **241** draft glossary terms existing in WordPress.

## 2. Screenshot Symptoms

Baseline authenticated capture (`_glossary-scratch/layout-fix/baseline-auth-archive.*`):

- Hero / intro / search / alphabet chrome present
- Alphabet chip showed only `# (241)`
- One `h2` = `#`
- **241** list items as `<a href=""></a>` (empty title + empty href)
- Tall `ul` (~6748px) with yellow list-marker color `rgb(255, 204, 0)` — visually a long yellow dotted vertical line
- `document.body.scrollHeight` ≈ **11385**
- Anonymous `/glossary/` remained **404**

## 3. Root Cause

Production diagnostic on the live main query:

| Signal | Value |
|--------|-------|
| SQL | Correct `post_type=glossary` + draft/publish/… statuses |
| `found_posts` | 241 |
| `post_count` | 241 |
| `count( $wp_query->posts )` | **0** |
| Loop via `have_posts()` / `get_post()` | **241 nulls** |

The archive template collected the main loop into `$posts`, then grouped with `get_the_title()` / `get_permalink()`. Null posts yielded empty titles → all assigned to `#` → 241 empty anchors → yellow list bullets formed the giant dotted line. This is a **query hydration / loop** defect, not a CSS defect.

## 4. Query Behavior

- `pre_get_posts` correctly requested draft statuses for `edit_posts` users.
- Main query **counted** 241 rows but left `$wp_query->posts` empty, so the Loop advanced `post_count` times over missing post objects.
- Fix: dedicated `WP_Query` in `iseo_glossary_get_archive_posts()` (helpers), independent of main-loop hydration.

## 5. Draft Preview Model

| Viewer | Behavior |
|--------|----------|
| Anonymous (gate closed) | `template_redirect` → **404**; drafts not exposed |
| User with `edit_posts` | Archive loads drafts via dedicated query |
| Term URL in archive | `get_preview_post_link()` when `edit_post` capability; no public draft permalinks |
| Published + public gate | Future path uses `get_permalink()` only when `ISEO_GLOSSARY_PUBLIC_EXPOSURE` is true |

No admin nonces hardcoded in templates. No terms published.

## 6. Alphabet Grouping Fix

- Titles from raw `$post->post_title` via `iseo_glossary_term_title()`
- Empty titles skipped (never become `#` fallback for empty dataset)
- `#` only for genuine non-letter / non-digit first characters
- Cyrillic А–Я (+ Ё), Latin A–Z, `0-9` supported
- Groups with zero terms never rendered; alphabet chips only for populated groups

Post-fix: **47** populated letter groups; **no** `#` group (no symbol-only titles in current 241); **241** linked terms.

## 7. Empty-state Fix

If the authorized query yields no groupable terms:

- Message: `Термины пока не добавлены.` (or search no-results copy)
- No alphabet nav, no letter wrappers, no list bullets

## 8. Existing Style Reuse

| Element | Pattern |
|---------|---------|
| Hero | `page_scene` (unchanged) |
| Intro / search | `content_block` + plain form |
| Alphabet | `blog_filter*` (unchanged) |
| Letter headings | Plain `h2` inside `content_block` — **privacy-policy body heading pattern** |
| Removed from letter groups | `content_block__title` (88px section chrome; unsuitable for single-letter labels) |

**No new CSS, selectors, or inline styles.** Yellow list markers next to real terms are pre-existing list styling, not an empty decorative timeline.

## 9. Files Changed

Theme package / production `iseoblog`:

- `archive-glossary.php`
- `inc/glossary-helpers.php`
- `inc/glossary-cpt.php` (status helper alignment + comment)

Scoped production backups: `*.bak-glossary-layoutfix-20260724T064614Z` (+ diagnostic bak retained).

## 10. Validation

| Check | Result |
|-------|--------|
| Draft count | **241** |
| Published | **0** (admin publish tab empty / null count) |
| Auth archive terms | **241** linked preview URLs |
| Orphan `#` group | **absent** |
| Empty anchors | **0** |
| `content_block__title` in glossary lists | **absent** (still used by pre-existing Telegram/audit chrome) |
| Single draft preview | OK (`?post_type=glossary&p=…&preview=true`) |
| Anonymous `/glossary/` | **404** |
| `/`, privacy, blog, tariff-calc, offers | **200** |
| PHP fatal | none |

## 11. Anonymous Boundary

Public exposure gate unchanged (`ISEO_GLOSSARY_PUBLIC_EXPOSURE = false`). Sitemap exclude and noindex filters unchanged. No menu link added. No drafts visible anonymously.

## 12. Rollback

1. Restore the three theme files from `*.bak-glossary-layoutfix-20260724T064614Z` (or prior glossary bak).
2. Confirm anonymous `/glossary/` 404 and baseline routes.
3. Full Beget restore only if scoped file rollback fails.

## 13. Remaining Limitations

- Archive term links are **preview URLs** while drafts remain unpublished (correct for gate-closed state).
- Definitions/excerpts still empty in WP (editorial HOLD).
- Main query still may report `found_posts` without hydrated posts; archive no longer depends on it.
- List marker color remains theme-default yellow beside real terms (not treated as a defect).

## 14. Stop Condition

- No glossary term published
- Public exposure remains closed
- Authenticated preview shows 241 terms in populated alphabet groups
- No giant empty `#` bullet column
- No new CSS
- No push; await operator review

---

*Glossary archive layout fix evidence v1 · 2026-07-24.*
