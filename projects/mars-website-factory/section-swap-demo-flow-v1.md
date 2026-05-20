# Section swap demo flow v1 (Wave 4)

**Status:** **documented** — operational demo for `replaceSectionContent` and destroy/init cleanup.  
**Runnable script:** [workspaces/website-factory-reference-v1/docs/section-swap-demo.js](../../workspaces/website-factory-reference-v1/docs/section-swap-demo.js).  
**API:** `js/core/lifecycle.js` in reference workspace.

**Not:** automated test harness.

---

## Prerequisites

```powershell
cd workspaces/website-factory-reference-v1
npm install
npm run build
```

Open `dist/index.html` in browser (static server optional).

---

## Demo A — Hero swap via `replaceSectionContent`

**Goal:** Prove CTA/modal survives innerHTML replacement.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open page — click hero **Get started** | Modal opens |
| 2 | DevTools → Console | — |
| 3 | Paste contents of `docs/section-swap-demo.js` | Hero copy changes to "Swapped hero (demo)" |
| 4 | Click **Modal still works** on new hero | Modal opens; no duplicate handlers |
| 5 | ESC | Modal closes; `body.is-modal-open` removed |

**Underlying sequence:**

```text
destroySection(hero)     → tears down data-module inside hero (none on hero)
hero.innerHTML = variant
initSection(hero)        → re-binds [data-modal-open] via lifecycle core click delegate
```

---

## Demo B — Lead form swap (form cleanup)

**Goal:** Prove form module destroy prevents double submit.

| Step | Action |
|------|--------|
| 1 | Focus form — start typing |
| 2 | Console: `var f = document.querySelector('[data-block-id="lead_form"]'); WfLifecycle.destroySection(f);` |
| 3 | Replace partial via rebuild **or** `replaceSectionContent` with same form HTML from partial |
| 4 | Submit once — only one network/mock request |

**Failure signature if skipped destroy:** two submit handlers, `is-loading` stuck.

---

## Demo C — Sticky CTA + modal stack

| Step | Action | Expected |
|------|--------|----------|
| 1 | Scroll past hero | Sticky bar visible (`aria-hidden="false"`) |
| 2 | Click sticky **Get started** | Modal above sticky (z-index) |
| 3 | `WfLifecycle.destroySection` on sticky element | Bar hidden; observer disconnected |
| 4 | Scroll again | No ghost show/hide (observer gone) |

**Sticky root:** `data-module="sticky-cta"` — **not** inside `data-section`; `initPage` initializes orphan modules.

---

## Demo D — Modal cleanup before removing modal node

| Step | Action |
|------|--------|
| 1 | Open modal from any CTA |
| 2 | Console: `window.WfModal.closeTop()` or destroy modal host per modal.js |
| 3 | Confirm `document.body` has no `is-modal-open` |

Do **not** remove `#modal-callback` from DOM while open.

---

## Console one-liners (reference)

```javascript
// Re-init section without HTML change
var el = document.querySelector('[data-block-id="lead_form"]');
WfLifecycle.reinitSection(el);

// Manual destroy → init (equivalent to replace without HTML change)
WfLifecycle.destroySection(el);
WfLifecycle.initSection(el);
```

---

## REPORT hook

After running demos in a real task, record in REPORT:

- Which `block_id` swapped
- Whether `destroySection` called explicitly
- Modal / form / sticky regression: pass | fail | SAFE UNKNOWN
- Build command run

Example REPORT: [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) §3.

---

## Related

- [section-replacement-contract-v1.md](section-replacement-contract-v1.md)
- [foundation-systems/section-survivability-implementation-v1.md](foundation-systems/section-survivability-implementation-v1.md)

*Wave 4 — section swap demo flow.*
