# FP-0002 V9-06D9-0 WP Current Visual Inventory v1

**Date:** 2026-07-05  
**Task:** V9-06D9-0 Full V9 Visual Port Charter  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/wp-current-visual-inventory.json`

## Runtime

| Field | Value |
|-------|-------|
| URL | `http://shpigovsky.test/` |
| Runtime root | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| WP source | `WORDPRESS/theme/shpigovsky/` |

## Header inventory

| Item | WP source | Render state | ACF / data | Repair |
|------|-----------|--------------|------------|:------:|
| Header shell | `layout/header.php` | present | D8-A options seeded | no |
| Desktop messengers | `navigation/messenger-links.php` | **omitted** | `social_links` empty (D8-A skip) | **yes** |
| Mobile messengers | `navigation/messenger-links.php` | **omitted** | same | **yes** |
| Primary nav | `navigation/primary-desktop.php` | flat WP menu | differs from V9 labels | **yes** |
| Search button | `navigation/primary-desktop.php` | present | — | no |
| Offcanvas | `navigation/offcanvas.php` | partial (no messengers) | social_links empty | **yes** |

**Key finding:** Messenger template code **exists** but conditionally returns when `social_links` option rows are empty. D8-A intentionally skipped `social_links` (no invented URLs). Static V9 uses `href="#"` placeholders — visual parity does not require operator URLs.

## Home rendered vs missing

### Visible (6)

1. Hero — degraded (no `hero__media`)
2. Feature grid — OK
3. Treatment/prevention — visible, media gaps
4. Rehabilitation program — visible, image gaps
5. FAQ — OK
6. Final form — OK

### Orchestrated but hidden (2)

- Gallery — `gallery.php` early return (ACF empty)
- Articles teaser — no posts

### Not in `front-page.php` (12)

home-recovery-intro, founder-quote, home-why-us, home-staff-photo, clinic-landscape, home-recovery-life, reviews, home-rehabilitation-requirements, home-genotyping, comfort, home-videos, specialists

## Asset enqueue

| Enqueued | Not enqueued |
|----------|--------------|
| `v9-style.css` | Swiper CSS/JS |
| `v9-shell.js` | Fancybox CSS/JS |
| | Inputmask |
| | Page interaction modules from V9 `main.js` |

Font delivery: 5/10 Inter requests 404 at `/assets/fonts/...` (D9-A).

## Result

WP inventory complete. Runtime is MVP skeleton with intentional deferrals — not accidental catastrophic failure.
