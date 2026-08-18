# WP Forge Smart Search Module Spec v1

**Class:** B  
**Maturity:** PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Reference:** FP-0002 P09 / FU01 / P10 Admin / P11 CPT retarget

---

## Architecture

```text
Admin groups/min-chars/limits/order/scopes/exclusions
        ↓
REST endpoint (namespaced)
        ↓
One JS controller: debounce, AbortController, keyboard, NBSP normalize
        ↓
Multiple DOM instances (header desktop, mobile offcanvas, …)
```

- Group by **content type**; user-visible labels stay stable when the storage type changes (Page → CPT).
- Desktop and mobile share logic; visual parity is a QA item.
- Empty query / below min chars → no panel spam.
- Do not create a second search backend per breakpoint.

## Security

Auth as designed (typically public GET with rate awareness). No privileged content. Escape titles/URLs.

## QA

Keyboard nav; abort in-flight; 3+ char; groups; after CPT migration no duplicate IDs in Pages + CPT.

## Extraction

Theme `inc/search-helpers.php` + CSS/JS + core REST — **B: reusable after extraction** (namespaces, text domain).

---

*Spec v1.*
