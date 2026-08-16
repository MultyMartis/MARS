# PROD-P09 — Fancybox Ownership Audit

**Date:** 2026-08-14  
**Scope:** Read-only (source + live HTML). No production mutation.

## Library

| Item | Finding |
|------|---------|
| Package | Local theme vendor Fancybox UMD |
| Paths | `theme/assets/vendor/fancybox/fancybox.umd.js`, `fancybox.css` |
| Enqueue helper | `inc/fancybox-vendors.php` → `shpigovsky_enqueue_fancybox_vendor()` |
| CDN | **Not used** (local vendor only) |
| New library needed? | **No** |

## How assets load

- Fancybox CSS/JS registered as `shpigovsky-fancybox`.
- Shell script `shpigovsky-v9-shell` gains Fancybox as a dependency when vendor is enqueued.
- Conditional enqueue contexts already include Comfort / Generic reusable Comfort / Specialist certificates (`shpigovsky_maybe_enqueue_specialist_fancybox` in `inc/specialist-helpers.php`, priority 40).

## Working components (bind owners in `assets/js/v9-shell.js`)

| Context | Selector bound |
|---------|----------------|
| Comfort gallery | `.comfort__gallery [data-fancybox]` |
| O-centre infrastructure | `[data-fancybox="o-centre-infrastructure"]` |
| Home videos | `[data-fancybox="home-videos"]` |

Init pattern: `window.Fancybox.bind(selector, options)` inside IIFE; Comfort boot sets `booted = true` and only binds the Comfort / o-centre selectors above.

## Specialist certificate gallery (current)

| Layer | Status |
|-------|--------|
| Markup | `template-parts/specialist/profile.php` — anchors with `href=full`, `data-fancybox="specialist-certs-{page_id}"`, `data-caption`, thumbnail `<img>` |
| Group id | `specialist-certs-1033` on live `/specyalisty/kostyuk/` |
| Vendor enqueue | **Present on live** (`fancybox.css` + `fancybox.umd.js` in HTML) |
| Shell JS | **Present on live** (`v9-shell.js`) |
| Fancybox.bind for specialist group | **Missing** |

## Live HTML evidence (Kostyuk)

- Certificate links are real `<a href="…/uploads/….jpeg" data-fancybox="specialist-certs-1033">`.
- Without a bind covering this group, the browser follows the normal navigation to the image URL (direct file open).

## Exact failure reason

**Assets + markup are correct; initialization ownership gap.**  
`initComfortFancybox()` never binds `.specialist-profile__certs-grid [data-fancybox]` (or `specialist-certs-*`). Fancybox therefore does not intercept clicks.

## Preferred minimal fix (deferred until Backup Gate PASS)

1. Extend existing Comfort Fancybox boot in `v9-shell.js` with one additional bind, e.g.  
   `fancybox.bind('.specialist-profile__certs-grid [data-fancybox]', galleryOptions);`  
   **or** bind `[data-fancybox^="specialist-certs-"]`.
2. Reuse the same animation/toolbar options already used for Comfort.
3. No new library, no CDN, no DB change, no media change.
4. Exact-file deploy of `assets/js/v9-shell.js` only (unless drift gate proves another file must move with it).

## Acceptance target (after deploy)

`SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS`
