# Frontend foundation systems blueprint (Wave 1)

**Status:** **documented** — **blueprint only**; no implementation claim in MARS repo.  
**Purpose:** Canonical **direction** for shared UI systems in workspace implementations.

**Not:** component library code, design token runtime, or Storybook product.

**SoT today:** [frontend-production-model.md](frontend-production-model.md), [design-token-intelligence-governance.md](design-token-intelligence-governance.md), gulp pack constraints.

**Wave 2 implementation standards:** [foundation-systems/README.md](foundation-systems/README.md) — operational detail for systems in §2 map below.

---

## 1. Blueprint principles

- **src-first**, partial-based sections, **data-* behavior hooks**.
- **Semantic tokens** over ad hoc hex/spacing in sections.
- **Conversion blocks** are composable sections — not one-off CSS.
- **Motion and interaction** restrained — commercial landing, not SaaS demo.
- **One owner per hook** — idempotent JS bind on section scope.

---

## 2. System map (planned implementation)

| System | Direction | v1 implementation note |
|--------|-----------|---------------------------|
| **Tokens** | SCSS variables/maps: color, type, space, radius, shadow, z-index — semantic names (`$cta-primary`, not `$blue-2`) | Align [token-semantic-layer-model.md](token-semantic-layer-model.md); single `_tokens.scss` entry |
| **Spacing** | Cadence tiers XS–XL for **inter-section**; internal section spacing via component scale | [cadence-tier-model.md](cadence-tier-model.md) |
| **Typography** | `line-height = font-size + 4px` rhythm preference; heading scale locked in implementation pack | [typography-rhythm-governance.md](typography-rhythm-governance.md); RU word-splitting — [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) |
| **Responsive** | Mobile-first breakpoints from handoff; collapse taxonomy for QA | [responsive-intent-governance.md](responsive-intent-governance.md) |
| **Forms** | Field groups, labels, validation states, error summary, keyboard order — **state classes** not inline style | Blueprint phase 2 — shared `_forms.scss` + `data-form` module |
| **Modals** | Focus trap, scroll lock, `aria-modal`, restore focus, ESC close — one `data-modal` controller | Blueprint phase 2 — no duplicate modal JS per page |
| **Overlays** | Hero/media overlays separate from **modal** layer; z-index stack documented | [overlay-focal-balance-governance.md](overlay-focal-balance-governance.md) |
| **State classes** | `.is-active`, `.is-disabled`, `.is-loading`, `.has-error` — paired with `ui-state-taxonomy` | No fake disabled without attribute |
| **JS lifecycle** | `initSection(root)` → query `data-*` → bind once → `destroy` on hot-swap (future) | Module per section or shared registry |
| **Interaction** | Hover/focus visible; CTA single primary per viewport context | [interaction-intent-governance.md](interaction-intent-governance.md) |
| **Animation** | Prefer CSS transitions; no gratuitous scroll animations; `prefers-reduced-motion` respect | [motion-restraint-model.md](motion-restraint-model.md) |
| **Conversion blocks** | hero, proof strip, CTA band, pricing, FAQ — map to [block-registry-v0.md](block-registry-v0.md) `block_id` | Each block = partial + SCSS + optional JS |

---

## 3. Layered file intent (target workspace)

```text
src/
├── scss/
│   ├── _tokens.scss
│   ├── _mixins.scss
│   ├── foundations/     # forms, modals, overlays (phase 2)
│   └── sections/        # per block_id
├── html/
│   ├── partials/
│   └── pages/
└── js/
    ├── core/            # modal, form, overlay controllers
    └── sections/        # block-specific
```

**SAFE UNKNOWN:** exact paths until project workspace charter defines them.

---

## 4. Roadmap (implementation waves)

| Wave | Deliverable | Factory doc anchor |
|------|-------------|-------------------|
| **Wave 1 (done)** | Blueprint + section contract + operator entry | This file, section-replacement-contract |
| **Wave 2 (done — docs)** | Foundation system standards (tokens → conversion blocks) | [foundation-systems/README.md](foundation-systems/README.md) |
| **Wave 3 (done — reference)** | Real foundations + 3 blocks in reference workspace | [website-factory-reference-v1](../../workspaces/website-factory-reference-v1/), [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) |
| **Wave 4 (done)** | Adoption charter, 4 blocks, onboarding, REPORT examples, swap demo, extraction + compact QA | [onboarding-flow-v1.md](onboarding-flow-v1.md), [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md), reference workspace |
| **Wave 5** | Visual regression **process** (human-supervised) — not CV automation | visual-reconciliation-layer |

---

## 5. Modals vs overlays vs atmosphere

| Layer | Role | z-index discipline |
|-------|------|-------------------|
| **Atmosphere** | Hero background, gradients, media | Below content |
| **Overlay** | Text-on-image readability | Local to section |
| **Modal** | Blocking task UI | Top stack; focus trap |
| **Sticky CTA** | Conversion | Below modal; above content |

**HEADER != HERO** — shell partials own nav; hero partial owns first-screen decomposition.

---

## 6. Forms (blueprint)

- Label `for` / `id` pairing; required visible.
- Errors: `aria-describedby`, `.has-error` on group, not color-only.
- Submit disabled only with `.is-loading` + real pending state.
- Mobile: input types, tap targets, no zoom trap (font-size policy in implementation pack).

---

## 7. JS lifecycle (blueprint)

```text
DOM ready → initCore() (modals, forms if present)
         → initPage() → for each [data-section] → initSection(el)
Hot swap  → destroySection(el) → replace partial → initSection(el)
```

**Rules:** no global `window.MyApp` pollution; delegate events where lists are dynamic.

---

## 8. Reusable conversion blocks

Priority `block_id` implementations for Factory-native landings:

1. `hero` — primary CTA, proof hook
2. `social_proof` — logos / metrics
3. `services` or `features` — scan grid
4. `cta_band` — repeated conversion
5. `faq` — accordion with accessible disclosure

Each: handoff fields → partial contract → freeze per [section-replacement-contract-v1.md](section-replacement-contract-v1.md).

---

## 9. Honesty boundary

- No claim that shared foundations exist in repo until `workspaces/*` contains them.
- No automated token linter or modal runtime in MARS Phase 1.
- Blueprint **guides** human + Cursor implementation — validation via REPORT + QA checklists.

---

*Wave 1 — foundation systems direction only.*
