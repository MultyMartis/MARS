# FP-0002 V9-04 Forge Implementation Sequence v1

**Date:** 2026-07-02 | **Planning only — do not execute in V9-04**

| Phase | Name | Outputs |
|-------|------|---------|
| F0 | Intake verification | manifest validator PASS, env gate |
| F1 | Theme skeleton | style.css, functions.php, enqueue |
| F2 | Global layout/assets | header, footer, CSS/JS parity |
| F3 | Menus/breadcrumbs | registered locations |
| F4 | Modal + scroll-to-top | global partials + JS |
| F5 | Generic page family | page.php fallbacks |
| F6 | Full special pages | home, contacts, reviews, o-centre |
| F7 | Service hierarchy | hub, subdivision, leaf, alcohol |
| F8 | Blog | home.php, single.php, fixture post |
| F9 | Reviews | repeater migration |
| F10 | Legal | 4 pages + DEMO flags |
| F11 | Placeholders | 18 pages reserved |
| F12 | Forms backend | handler/plugin |
| F13 | SEO plugin | meta ownership |
| F14 | Route parity QA | acceptance matrix |
| F15 | Launch gate | blocker register clear |

Each phase: inputs from this pack, visual diff vs `dist/`, stop on parity failure.
