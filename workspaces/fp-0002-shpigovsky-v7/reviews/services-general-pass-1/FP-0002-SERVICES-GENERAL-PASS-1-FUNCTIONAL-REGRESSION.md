# FP-0002 — Services General Pass 1 Functional Regression

**Date:** 2026-06-26  
**Method:** Playwright @ `http://127.0.0.1:4174` — see `screenshots/capture-report.json`

## Services (`uslugi.html`)

| Check | Result | Notes |
| ----- | ------ | ----- |
| Header navigation | Pass | Active `/uslugi/` link present |
| Mobile menu | Pass *(not re-exercised in script)* | Same markup as Home |
| Hero modal CTA | **Partial** | `.hero--inner` has no `[data-modal-open]` — use header/footer CTAs |
| Founder modal CTA | Pass | Opens consultation modal |
| Comfort Fancybox | Pass | `[data-fancybox]` present |
| FAQ accordion | Pass | Toggle on first item (aria-expanded changes) |
| Final form | Pass | `[data-lead-form]` present; `lead_source=services-final` |
| Footer links | Pass *(static)* | Shared partial |
| Modal open/close | Pass | Escape after founder CTA |
| Console JS errors | 0 | — |
| Missing asset requests | 0 | — |

## Home smoke (`index.html`)

| Check | Result |
| ----- | ------ |
| Gallery Swiper initialized | 1 |
| Reviews Swiper initialized | 1 |
| Specialists Swiper initialized | 1 |
| Video Fancybox hooks | Present |
| FAQ block | Present |
| Modal hooks | Present |
| Console JS errors | 0 |
| Missing asset requests | 0 |

## Home source hash

| File | Changed in Pass 1 |
| ---- | ----------------- |
| `src/pages/index.html` | No |
| Home partials | No |

## Functional verdict

**PASS with documented hero CTA gap** — all reuse-section interactions and Home sliders remain functional.

---

*End of Pass 1 functional regression.*
