# FP-0002 V9-03B — Stacking Context Audit v1

## Final hierarchy (loaded state)

| Layer | z-index / notes |
|-------|-----------------|
| Page content (`.site-page-shell`) | Normal flow |
| Sticky/fixed header | Existing header z-index (unchanged) |
| Offcanvas overlay/panel | Existing offcanvas stack |
| Modal (`.modal-consultation`) | `z-index: 1200` |
| Fancybox (`.fancybox__container`) | Default `--fancybox-zIndex: 1050` — below modal when both exist; modal used for forms only |
| Preloader (`.site-preloader`) | `z-index: 99999` — **only during initial load** |

## Loading state

- Preloader: opaque `#ffffff`, covers full viewport
- Page shell: `opacity: 0` under preloader
- Preloader outside `.site-page-shell` — correct nesting

## After load

- `html.is-page-ready` — preloader `visibility: hidden; pointer-events: none`
- Preloader does not intercept clicks
- Modal/gallery remain above page content

## Verification

Build + 31-route HTTP 200; no invisible overlay reported in automated pass.
