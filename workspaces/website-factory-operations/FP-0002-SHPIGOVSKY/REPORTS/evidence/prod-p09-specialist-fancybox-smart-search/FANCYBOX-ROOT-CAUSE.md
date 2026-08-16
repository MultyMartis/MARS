# PROD-P09 — Fancybox Root Cause (live)

**Route:** `http://shpigovsky.beget.tech/specyalisty/kostyuk/`  
**Probe:** HTTP GET HTML (2026-08-14)

## Before behavior

Clicking a certificate thumbnail navigates to the raw attachment JPEG URL in the browser tab (direct file), instead of opening the site Fancybox overlay.

## Proven present

| Signal | Live |
|--------|------|
| `data-fancybox="specialist-certs-1033"` on cert anchors | Yes |
| Full-size `href` to uploads JPEG | Yes (3 certs observed) |
| `fancybox.umd.js` enqueued | Yes |
| `fancybox.css` enqueued | Yes |
| `v9-shell.js` enqueued | Yes |

## Proven missing

| Signal | Live / source |
|--------|----------------|
| `Fancybox.bind` covering specialist cert gallery | **No** — only Comfort / o-centre / home-videos |

## Conclusion

Root cause = **missing Fancybox.bind for specialist certificate gallery**, not missing markup and not missing vendor enqueue.
