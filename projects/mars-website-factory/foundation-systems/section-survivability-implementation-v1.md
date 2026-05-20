# Section survivability — implementation notes (Wave 3)

**Status:** battle-tested against [website-factory-reference-v1](../../../workspaces/website-factory-reference-v1/).  
**Contract:** [section-replacement-contract-v1.md](../section-replacement-contract-v1.md).

---

## Replacement flow (operational)

```text
destroySection(root)
→ update partial HTML (include graph or innerHTML swap)
→ initSection(root)   // or WfLifecycle.replaceSectionContent(root, html)
```

**Reference API:** `WfLifecycle.replaceSectionContent(sectionEl, newInnerHtml)` in `js/core/lifecycle.js`.

---

## Module cleanup matrix

| Module | destroy must | Failure if skipped |
|--------|--------------|-------------------|
| **form** | remove submit/blur listeners; abort `fetch`; clear `is-loading` | Double submit, duplicate handlers |
| **modal** | close if open; remove backdrop click; release focus trap | Body lock stuck, ESC stack wrong |
| **sticky-cta** | `IntersectionObserver.disconnect()` | Ghost show/hide |
| **slider** | remove touch/resize; cancel rAF | Jank, duplicate slides |
| **tabs/accordion** | keydown + click off | Duplicate toggles |

---

## Validation performed (reference workspace)

| Check | Result |
|-------|--------|
| `destroySection` on `lead_form` removes `__wfFormBound` | Pass — re-init binds once |
| Form submit during swap | Pass — abort + `is-loading` cleared on destroy |
| Modal open → destroy modal node | Pass — `body.is-modal-open` removed via `closeModal` |
| `replaceSectionContent` on hero | Pass — CTA `data-modal-open` works after swap |
| Duplicate `initSection` | Pass — no-op via `__wfSectionInit` |

**Method:** manual + console inspection in browser after `npm run build` — automated harness **SAFE UNKNOWN**.

---

## Operator procedure

1. List files in REPORT (partial, section SCSS, section JS).
2. If section has `data-module`, call `WfLifecycle.destroySection(el)` **before** removing DOM.
3. Swap partial; rebuild.
4. `WfLifecycle.initSection(el)` on new root (same `data-block-id` recommended).
5. Regression: modal still below sticky header z-index; form submits once; 375px no horizontal scroll.

---

## Global foundation changes

Touching `scss/foundations/*` or `js/core/*` = **Critical** blast radius — re-test all reference blocks (7) + modal + sticky.

**Wave 4 demo:** [section-swap-demo-flow-v1.md](../section-swap-demo-flow-v1.md).

*Wave 3 — implementation survivability.*
