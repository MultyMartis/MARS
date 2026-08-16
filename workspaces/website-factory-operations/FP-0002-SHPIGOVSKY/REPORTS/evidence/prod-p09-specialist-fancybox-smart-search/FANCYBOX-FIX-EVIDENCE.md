# PROD-P09 — Fancybox Fix Evidence

## Root cause (unchanged)

Markup + Fancybox vendor present; `v9-shell.js` previously bound Comfort / o-centre / home-videos only.

## Fix

In `initComfortFancybox()`:

```js
fancybox.bind('.specialist-profile__certs-grid [data-fancybox]', galleryOptions);
```

Shared `FP0002_FANCYBOX_ANIMATION` options — no second lightbox library.

## Live QA (Playwright)

| Check | Result |
|-------|--------|
| Cert links on `/specyalisty/kostyuk/` | 3 |
| Opens Fancybox container | **PASS** |
| Raw JPEG navigation | **false** |
| Next / Prev (`1/3`→`2/3`→`1/3`) | **PASS** |
| Close | **PASS** |
| Mobile open (390) | **PASS** |
| Comfort gallery still opens | **PASS** |
| Existing binds retained | comfort / o-centre / home-videos **true** |

Verdict: `SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS`
