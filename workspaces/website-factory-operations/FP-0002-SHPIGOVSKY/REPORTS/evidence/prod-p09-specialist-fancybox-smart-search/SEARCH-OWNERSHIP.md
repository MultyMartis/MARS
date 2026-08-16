# PROD-P09 — Search Ownership Map

**Date:** 2026-08-14  
**Status:** Ownership audit complete. Implementation **deployed** in P09 continuation (exact-file rollback mode).  
**Evidence path:** `REPORTS/evidence/prod-p09-specialist-fancybox-smart-search/SEARCH-OWNERSHIP.md`

## Current search UI owner

| Layer | Owner |
|-------|--------|
| Header dropdown panel markup | `template-parts/navigation/search-panel.php` (`data-search-panel`) |
| Form markup | `searchform.php` (`data-site-search-form`, input `name="s"`; live suggest when `enable_live_suggest`) |
| Trigger | Header control with `data-search-toggle` (desktop main header; FIX01) |
| Panel open/close + live suggest JS | `assets/js/v9-shell.js` → `initSiteSearchPanel()` |
| Styles | `assets/css/fp02-search.css` (+ related header rules in `v9-style.css`) |
| Full results page | `search.php` + `template-parts/search/*` (native `/?s=` fallback retained) |
| Query configuration | `inc/search-helpers.php` via `pre_get_posts` |
| Live suggest endpoint | `GET /wp-json/shpigovsky/v1/smart-search` |

**Decision:** Extend this existing header search UX. Do **not** invent a second competing search surface.

## Implementation status

**DEPLOYED** under operator exact-file rollback authorization. See main P09 report.


## Current endpoint

| Item | Finding |
|------|---------|
| Live suggestions endpoint | `GET /wp-json/shpigovsky/v1/smart-search` (theme REST) |
| Native WP full search | Retained — form submits GET `/?s=…` |
| Transport constraints | public published-only; sanitize; escape; no privileged fields; no WPilot; permalinks via `get_permalink()` |

## Content architecture (proven from source)

| Group (RU) | WordPress objects | How identified |
|------------|-------------------|----------------|
| **Услуги** | CPT `service` | `post_type === 'service'` |
| **Статьи** | CPT/core `post` | `post_type === 'post'` |
| **Специалисты** | Child `page` under hub `/specyalisty/` | Same logic as `shpigovsky_search_result_type_label()` / `shpigovsky_smart_search_group_key()` |
| **Страницы** | Other published `page` objects | `page` not Specialist; exclude system/legal |

## Exclusion rules (existing + P09)

From `shpigovsky_search_excluded_page_ids()` / search helpers:

- drafts, trash, revisions, attachments as standalone hits
- `has_password` false only / published only
- legal/system slugs: `user-agreement`, `consent-personal-data`, `cookie-files-policy`, `privacy-policy`
- hub `/specyalisty/` itself remains a **Страница** (not a specialist)
- Specialist children appear **only** under Специалисты (not again under Страницы)
- Services appear **only** under Услуги

## Trigger / UX contract (implemented)

| Rule | Value |
|------|-------|
| Min characters (trimmed) | **3** (Cyrillic-safe) |
| Debounce | 250 ms |
| Stale responses | AbortController + sequence token |
| Max per group | 5 |
| Empty | «Ничего не найдено» |
| Loading | subtle status line |
| Keyboard | Escape clears suggestions; Arrow/Enter when results present |

## JS ownership for suggestions

`initSiteSearchPanel()` in `v9-shell.js` renders suggestions inside the existing header panel (`data-smart-search-suggest`).

## DB / ACF

**No new fields / no DB schema.** Ranking via bounded WP_Query + PHP relevance sort.

