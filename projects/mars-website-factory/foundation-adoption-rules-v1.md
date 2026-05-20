# Foundation adoption rules v1 (Wave 4)

**Status:** **documented** — binding **operator** rules when copying or extending the foundation layer.  
**Charter:** [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md).

---

## 1. Token override rules

| Token class | Override allowed | Requires |
|-------------|------------------|--------|
| Brand primitives (`$color-brand`, hover) | Yes | Visual check 375 + desktop |
| Semantic text/surface/border | Yes, prefer map to primitives | REPORT if contrast risk |
| Spacing scale (`$space-*`, `$section-gap-*`) | Rare — HITL if page rhythm breaks | Standard+ |
| Z-index in `_layers.scss` | **No** without Critical + full stack QA | Critical |
| Overlay rgba tokens | Yes for brand atmospheres | Hero/modal regression |
| Typography scale | Yes — keep `clamp` on H1 | Mobile headline overflow check |

**Rule:** one project file `_tokens.scss` (or `_project-tokens.scss` imported after foundations) — **do not** scatter brand hex in section SCSS.

---

## 2. Local project override rules

| Layer | Path | Override |
|-------|------|----------|
| Foundation | `scss/foundations/*` | Copy once; edits = Critical blast radius |
| Section | `scss/sections/_*.scss` | Full control inside `.wf-section--{block_id}` |
| Layout shell | `partials/layout/*` | Project-owned; not default replace unit |
| Page | `pages/*.html` | Include graph only — no pasted section HTML |
| JS core | `js/core/*` | Copy once; patch only with REPORT + re-test all modules |

**Project override file pattern (optional):**

```scss
// scss/_project-overrides.scss — after foundations
@use 'foundations/tokens' as *;
// brand-only deltas
```

---

## 3. JS lifecycle preservation rules

| Rule | Detail |
|------|--------|
| Script order | `lifecycle.js` → `modal.js` → `form.js` → section modules → `main.js` |
| Registration | Section modules call `WfLifecycle.registerModule(name, { init, destroy })` |
| Section init | Only via `initPage` / `initSection` — never call `mod.init` directly from section code |
| Listeners | Bind on section root or module element; **remove in destroy** |
| Globals | No `window.onload` per block — use lifecycle |
| Replace | `destroySection` **before** innerHTML swap |

---

## 4. Z-index safety

Use **only** tokens from `_layers.scss`:

| Token | Use |
|-------|-----|
| `$z-overlay-readability` | Hero/atmospheric overlays inside section |
| `$z-sticky-cta` | Sticky bar |
| `$z-header` | Site header |
| `$z-modal-backdrop` / `$z-modal` | Modal stack |

**Forbidden:** `z-index: 9999`, per-section modal layers, sticky above modal.

---

## 5. Overlay safety

- Overlays inside sections: `pointer-events: none`, `aria-hidden="true"`.
- Do not stack multiple full-section dark overlays without readability check.
- CTA and text sit **above** overlay (`z-index: $z-base + 1` on content wrapper).

---

## 6. Modal safety

- Open only via `[data-modal-open="modal-id"]` (lifecycle delegated click).
- One modal id per callback pattern unless handoff defines more.
- After section swap: open modal from new CTA — body must not stay `is-modal-open`.
- Sticky CTA: verify modal opens **over** sticky bar (z-index stack).

---

## 7. Sticky CTA safety

- Module: `data-module="sticky-cta"` on bar root.
- `destroy` must `disconnect()` IntersectionObserver.
- Show bar only after hero sentinel leaves viewport (reference implementation).
- Do not duplicate sticky bars per page.

---

## 8. Form safety

- Keep `data-module="form"` on `<form>`.
- Production: set `data-form-endpoint`; remove mock delay in `form.js` or override attribute.
- On section replace: destroy clears `fetch` abort + `is-loading`.

---

## 9. Customization matrix (quick reference)

| Customize freely | Keep canonical |
|------------------|----------------|
| Section copy, images, metrics | `data-section`, `data-block-id` |
| Section SCSS (scoped) | Lifecycle API |
| Which blocks on page | Core JS destroy/init |
| Brand tokens | Z-index stack |
| CTA labels, hrefs | Modal open attribute contract |

---

## 10. Adoption QA minimum

Before calling a client workspace “adopted”:

- [ ] `npm run build` PASS or SAFE UNKNOWN documented
- [ ] 375px: no horizontal scroll on main page
- [ ] Modal + form + sticky (if present) exercised once
- [ ] REPORT lists copied paths and token edits

Full checklist: [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md).

*Wave 4 — foundation adoption rules.*
