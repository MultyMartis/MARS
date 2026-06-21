# Foundation adoption charter v1 (Wave 4)

**Status:** **documented** — operator workflow for adopting Website Factory foundations into a **client workspace**.  
**Rules detail:** [foundation-adoption-rules-v1.md](foundation-adoption-rules-v1.md).  
**Reference:** [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/).

**Not:** runtime sync, not scaffolding automation, not governance expansion.

---

## Purpose

Turn Wave 2–3 foundation + reference slice into a **repeatable production start** — copy, customize safely, ship sections without poisoning the shared layer.

---

## When to use

| Situation | Action |
|-----------|--------|
| New client landing / commercial site | Follow **New workspace** below |
| Existing Gulp workspace, no WF layer | **Bootstrap** — copy foundations first, one section at a time |
| Section swap / redesign | [section-replacement-contract-v1.md](section-replacement-contract-v1.md) + [section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md) |
| Extract pattern from production project | [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md) |

---

## New client workspace (operator workflow)

```text
0. Production mode — declare TEMPLATE_ART (typical) or PIXEL_PERFECT if design SSOT exists — [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md)
1. Charter     — client slug, workspace path, site_type_id, block list
2. Scaffold    — Gulp/include layout matching reference (pages, partials, scss, js)
3. Copy layer  — scss/foundations/* + js/core/* from reference (wholesale)
4. Tokens      — edit _tokens.scss brand/semantic only (see adoption rules)
5. Shell       — header/footer/modal partials; do not section-replace shell by default
6. Sections    — copy block partials + scss/sections/*; wire @@include in page entry
7. Build       — npm install && npm run build — record in REPORT
8. QA          — [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md) (compact)
9. REPORT      — files, mode, freeze state, SAFE UNKNOWN
```

**Timebox first session:** foundations + **one** section (`hero` recommended) — not full page in one pass unless handoff demands it.

---

## Copy foundation layer

| Copy wholesale | Customize in client |
|----------------|---------------------|
| `js/core/lifecycle.js`, `modal.js`, `form.js` | `data-form-endpoint` on forms |
| `scss/foundations/_layers.scss`, `_breakpoints.scss`, `_motion.scss`, `_utilities.scss`, `_forms.scss`, `_modal.scss` | — |
| `scss/foundations/_tokens.scss` | **Brand colors, radii, font stack** only |
| Section **structure** (`data-section`, `data-block-id`) | Copy, visual design per handoff |
| Block partials from reference | Content, imagery, offer copy |

**Do not** copy `dist/` — always build.

---

## What stays canonical

| Canonical (do not fork semantics) | Project-local (allowed) |
|-----------------------------------|-------------------------|
| `WfLifecycle` init/destroy/replace API | Page entries, include graph |
| Z-index stack in `_layers.scss` | Section HTML content |
| `data-section` + `data-block-id` contract | `_tokens.scss` brand palette |
| Modal focus trap + `data-modal-open` | Section SCSS inside `.wf-section--{id}` |
| Form field structure + `data-module="form"` | Endpoint URL, field labels |
| SCSS import order in `main.scss` (foundations → sections) | Extra sections not in reference |

---

## Survivability guarantees (adoption)

1. **Section replace** — `destroySection` before DOM swap; `initSection` after — see swap demo.
2. **JS lifecycle** — modules register via `WfLifecycle.registerModule`; no anonymous global listeners on `document` from section code.
3. **Overlay safety** — hero overlays use `$z-overlay-readability`; no section z-index above `$z-header` except sticky CTA token.
4. **Modal safety** — sticky CTA and header stay **below** modal stack; test open modal after sticky visible.
5. **Chat ≠ SoT** — handoff + REPORT hold freeze state and file list.

---

## Forge mode at adoption

| Phase | Mode |
|-------|------|
| Copy foundations + token tweak | **Lite** if narrow; **Critical** if editing `_layers.scss` |
| First section build | **Standard** |
| Freeze first section | **Standard** minimum |
| Global token / shared partial change | **Critical** |

---

## Related (Wave 4)

| Doc | Role |
|-----|------|
| [foundation-adoption-rules-v1.md](foundation-adoption-rules-v1.md) | Token/local override, z-index, modal, JS rules |
| [onboarding-flow-v1.md](onboarding-flow-v1.md) | Single path: new operator / workspace / task |
| [operational-examples/golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md) | REPORT templates |
| [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md) | Grow library from real projects |

*Wave 4 — adoption charter.*
