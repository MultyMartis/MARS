# CF-009 Pre-Implementation Inventory

**Family:** `home-final-form` → target `final-form`
**Date:** 2026-06-28

## Consumer table

| Page | Include path | Root class | Form hook | Phone hook | headingId | Page scope |
|---|---|---|---|---|---|---|
| index.html | partials/sections/home-final-form.html | home-final-form | data-lead-form | data-phone-input | home-final-form-heading | shared partial |
| uslugi.html | partials/sections/home-final-form.html | home-final-form | data-lead-form | data-phone-input | home-final-form-heading | shared partial |
| uslugi-v2.html | partials/sections/home-final-form.html | home-final-form | data-lead-form | data-phone-input | home-final-form-heading | shared partial |
| usluga-podrazdel-v1.html | partials/sections/home-final-form.html | home-final-form | data-lead-form | data-phone-input | service-subdivision-final-form-heading | page heading id |
| usluga-konechnaya-v1.html | partials/sections/home-final-form.html | home-final-form | data-lead-form | data-phone-input | service-leaf-final-form-heading | page heading id |

## Summary

- **Consumers:** 5
- **Inline copies:** 0
- **Duplicate partials:** 0
- **CSS copies:** 0 (single `.home-final-form__*` block in `style.scss`)
- **JS initializations:** 1 global `[data-lead-form]` handler in `main.js` (name-scoped class toggles for validation UI)
- **Content variants:** 0 (parameterized heading/lead only)
- **Structure variants:** 0

## Boundary

| Related family | Partial | Pages | Structural relationship | Included in CF-009 |
|---|---|---:|---|---:|
| home-final-form | home-final-form.html | 5 | Final lead form band | YES |
| modal-consultation | modal-consultation.html | all | Separate modal form | NO |
| services-program-v2 CTA bands | — | 3 | Reuses same background asset only | NO |

**Boundary decision:** CONFIRMED — only `home-final-form` family in scope.

## Component identity

**Classification:** SHARED_BUT_PAGE_NAMED
**Result:** CONFIRMED — identical HTML structure, CSS, JS behavior across all consumers.
