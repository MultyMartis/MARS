# Website Factory reference workspace v1



**Status:** **implementation reference** — not a client delivery project.  

**Wave:** 3 (foundations + 3 blocks) · 4 (adoption kit + 4 blocks) · 5 (`faq` real extract + hardening docs).  

**Standards:** [foundation-systems/README.md](../../projects/mars-website-factory/foundation-systems/README.md).

**Foundation frontend rules:** [frontend-rules/WF-GRID-DISCIPLINE-v1.md](frontend-rules/WF-GRID-DISCIPLINE-v1.md) — **MANDATORY** section/container grid discipline (promoted from SITE-001 WF-V3).

---



## Purpose



- Battle-test Wave 1–2 contracts with **real** `src/` artifacts.

- Golden pattern for tokens, lifecycle, forms, modals, **full conversion block kit**.

- Clone or copy `scss/foundations/` + `js/core/` into client workspaces.



**Not:** MARS runtime, not auto-synced to Factory docs.



---



## Canonical structure



```text

src/

├── pages/index.html              # page entry (@@include only)

├── partials/

│   ├── layout/                   # shell — not section-replaced by default

│   └── sections/                 # freeze/replace units

├── scss/

│   ├── main.scss                 # import order — do not reorder casually

│   ├── foundations/              # reusable — Critical blast radius

│   └── sections/                 # per block_id

└── js/

    ├── core/                     # lifecycle, modal, form

    ├── sections/sticky_cta.js    # registers sticky-cta module

    └── main.js                   # DOMContentLoaded entry

docs/

└── section-swap-demo.js          # console demo for replaceSectionContent

```



---



## Blocks in demo page



| block_id | Module |

|----------|--------|

| hero | — (modal via lifecycle delegate) |

| social_proof | — |

| pricing | — |

| lead_form | `form` |

| cta_band | — |

| contact_block | — |

| sticky_cta | `sticky-cta` (body-level orphan) |
| faq | — (native `<details>` — static, Wave 5 Triumph V2 extract) |



---



## Separation



| Layer | Path | Replace? |

|-------|------|----------|

| Foundation | `scss/foundations/*`, `js/core/*` | Critical — REPORT required |

| Section | `partials/sections/*`, `scss/sections/*` | Standard per [section-replacement-contract-v1.md](../../projects/mars-website-factory/section-replacement-contract-v1.md) |

| Project local | `pages/`, brand tweaks in `_tokens.scss` | Per charter |



---



## Build (operator)



```powershell

cd workspaces/website-factory-reference-v1

npm install

npm run build

```



Open `dist/index.html` — exercise modal, form, sticky scroll, resize 375px.



---



## Wave 4 operator docs



| Doc | Use |

|-----|-----|

| [foundation-adoption-charter-v1.md](../../projects/mars-website-factory/foundation-adoption-charter-v1.md) | New client workspace |

| [section-swap-demo-flow-v1.md](../../projects/mars-website-factory/section-swap-demo-flow-v1.md) | Section replacement demo |

| [reference-workspace-qa-flow-v1.md](../../projects/mars-website-factory/reference-workspace-qa-flow-v1.md) | Compact QA |

| [golden-report-examples-v1.md](../../projects/mars-website-factory/operational-examples/golden-report-examples-v1.md) | REPORT templates |



---



## data-module contract



- Sections: `data-section` + `data-block-id`

- Modules: `data-module="form|sticky-cta"` inside section or body orphan

- Init: `WfLifecycle.initPage()` — see `js/core/lifecycle.js`

- Replacement: `WfLifecycle.replaceSectionContent(el, html)` or destroy → swap → init



Details: [section-survivability-implementation-v1.md](../../projects/mars-website-factory/foundation-systems/section-survivability-implementation-v1.md).



---



## Golden slice



Full walkthrough: [golden-implementation-slice-v1.md](../../projects/mars-website-factory/golden-implementation-slice-v1.md).

