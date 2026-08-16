# PROD-P09-FU01 — Mobile Search Ownership

**Date:** 2026-08-14

## Before FU01

| Item | Owner |
|------|--------|
| Mobile search entry | Offcanvas link `.offcanvas__nav-link--search` → `/?s=` |
| Live suggest | Desktop header panel only (`data-search-panel`) |
| JS | `initSiteSearchPanel()` bound to single desktop input |

## After FU01

| Item | Owner |
|------|--------|
| Mobile search UI | Offcanvas embedded `searchform.php` (`site-search-form--offcanvas`) |
| Input | `#offcanvas-search-field` / `[data-offcanvas] [data-smart-search-input]` |
| Form | `[data-offcanvas] [data-smart-search-form]` |
| Suggest root | `[data-offcanvas] [data-smart-search-suggest]` |
| Panel shell | Existing `[data-offcanvas]` / `[data-offcanvas-panel]` open/close |
| Close lifecycle | `[data-offcanvas-close]` + Escape; clears mobile suggest on close |
| Shared initializer | `initSmartSearchForms()` → `bindSmartSearchForm(form)` per instance |
| Desktop panel chrome | `initSiteSearchPanel()` open/close only (suggest via shared binder) |

## Shared architecture

- Same REST: `GET /wp-json/shpigovsky/v1/smart-search`
- Same threshold 3 / debounce 250 ms
- Same groups / ranking / limits
- Per-instance: input, suggest root, AbortController, request sequence, active index
- No cross-updating desktop ↔ mobile results
- Native `/?s=` submit fallback retained

## Breakpoint 768

Both forms remain in DOM (2 instances). Desktop toggle vs offcanvas visibility is CSS/shell owned; bindings do not double-fetch across instances.
