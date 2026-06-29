# FP-0002 V8 O-Centre Page Anatomy + Reuse Charter v1

**Date:** 2026-06-29 (resolution update 2026-06-29)
**Status:** Charter complete — **implementation NOT authorized**
**HEAD at charter:** `7f5d7f23` · **HEAD at resolution:** `508837a0` (`mars/canonical-post-recovery`)

---

## 1. Canonical anchors

| Anchor | Value |
|---|---|
| Repository | `C:/MARS Phenix/AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Manual polish authority | `472be1ab` — verified ancestor of HEAD |
| CF-010 clinic landscape | `7f5d7f23` — HEAD |
| CF-011 program CTA band | `4d98d6fb` — verified ancestor |
| CF-012 program modifiers | `9e8fa083` — verified ancestor |
| Consolidation | CF-003–CF-012 COMPLETE; page-wide DOM gate PASS |
| V8 workspace | `workspaces/fp-0002-shpigovsky-v8` |

---

## 2. Source authority

| Layer | Authority |
|---|---|
| Design composition | `Spig_v1.2.fig` frames «О центре» / «О центре - моб» |
| Historical fig | `Шпиговский.fig` — **not** used on conflict |
| Block composition | `FP-0002-BLOCK-INVENTORY-v1.md` PG-005 |
| Implementation patterns | V8 source post operator polish + CF-010 naming |
| Rejected WIP | V7 `o-centre-v1.html` — content hints only |

---

## 3. Page purpose

Institutional hub **«О центре»** (`/o-centre/`): introduce the rehabilitation center, condition spectrum, approach, program, comfort, team, reviews, FAQ. Subpages under `/o-centre/*` are **out of scope** for this charter.

---

## 4. Design evidence

See `FP-0002-V8-OCENTRE-DESIGN-EVIDENCE-v1.md`.

- Desktop: 1437×12830, 13 sections + footer
- Mobile: 390×16586 (380 content width), 11 sections + footer
- Limitation: no live Figma MCP read; parse artifacts used

---

## 5. Page anatomy

See `FP-0002-V8-OCENTRE-PAGE-ANATOMY-v1.md` — 13 content blocks OC-B01…OC-B13.

---

## 6. Reuse decisions (summary)

| Verdict | Blocks |
|---|---|
| DIRECT_REUSE | Header, footer, modal, comfort, specialists, reviews, faq, program-cta-band |
| REUSE_WITH_CONTENT_PARAMETERS | inner hero, internal-page-nav, services-program-v2, founder-quote |
| REUSE_WITH_EXISTING_FUNCTIONAL_MODIFIER | who-we-treat band via services-category-section-v2 |
| GENUINELY_UNIQUE | BLK-036 narrative, BLK-037/038 infrastructure bands (1–2 new partials) |
| REJECTED false reuse | home-gallery, home-staff-photo, home hero |

Full map: `FP-0002-V8-OCENTRE-COMPOSITION-MAP-v1.md`.

---

## 7. Gallery decision

**Classification:** `SIMILAR_BUT_DIFFERENT` — see gallery audit.
**Use:** `comfort.html` + category grid; **not** `home-gallery.html`.

---

## 8. Staff-photo decision

**Classification:** `HOME_SPECIFIC` — not on PG-005; use specialists slider instead.

---

## 9. Hero decision

| Item | Finding |
|---|---|
| Candidate | `services-inner-hero-v2.html` (BLK-007ˢ) |
| Structural match | Yes — same partial on all service templates |
| Visual match | Yes — service/about hero variant |
| Parameters | eyebrow, H1, lead, image, CTA source id |
| Variant needed | No new hero architecture |
| Classification | **REUSE_WITH_CONTENT_PARAMETERS** |
| CF-013 HOLD | Inner hero already proven on 3 templates — extend to O-Centre |

Breadcrumb/nav relation: separate `internal-page-nav` below hero (not inside hero shell).

---

## 10. Unique blocks

| Block | Why unique | Proposed family | Reuse potential | Risk |
|---|---|---|---|---|
| OC-B03 BLK-036 | Institutional «Кто мы» long copy | `institutional-narrative` or `page-intro` family | Other institutional pages | Medium — copy-heavy |
| OC-B08 BLK-037/038 | «Наш Дом» + infrastructure | `infrastructure-narrative` + optional bleed photo | About subpages later | High — assets missing |
| OC-B04 who-we-treat | Spectrum list + gallery | Extend category-section modifier | Service pages pattern | Low if modifier only |

Inline page section vs component: prefer **one new section partial** for BLK-036; combine 037/038 only if design proves single DOM.

---

## 11. Content status

**Correction note (2026-06-29):** Visual structural correction applied — page status `CORRECTED_PENDING_OPERATOR_REVIEW`. Evidence: `audits/o-centre-visual-correction/`.

See content inventory. **Confirmed:** hero pattern, comfort, shared tails, much WIP copy for who-we-are/treat. **Missing:** BLK-037/038 PDF text, steps copy, About hero asset confirmation.

---

## 12. Asset status

Reuse comfort, program, services category thumbs. **Export required:** About-specific narrative/infrastructure imagery from Spig_v1.2.fig.

---

## 13. Responsive model

Prefer **single DOM** + CSS breakpoints @1024. See anatomy responsive table. Mobile clarifies comfort as distinct tall section.

---

## 14. Accessibility model

See accessibility charter. One H1; section `aria-labelledby`; page-scoped ids; fix comfort placeholder link in implementation.

---

## 15. Link/navigation model

Production href `/o-centre/`; footer subpages remain separate future pages. In-page anchors vs footer URLs — **operator decision** (CF-006).

---

## 16. Implementation phases

### Phase 0 — Safety and backup

- Preflight, source hashes, build baseline
- **Stop:** hash mismatch on protected partials

### Phase 1 — Page shell

- Create `o-centre.html` only
- Header, footer, modal, meta
- **Protected:** all existing pages

### Phase 2 — Direct canonical reuse

- comfort, specialists, reviews, faq, program-cta-band, founder-quote (params)

### Phase 3 — Parameterized reuse

- services-inner-hero-v2, internal-page-nav, services-program-v2, category-section modifier

### Phase 4 — Unique blocks

- New narrative partial(s) BLK-036–038 only after assets/copy gate

### Phase 5 — Integration

- Links, ids, ARIA, comfort href fix

### Phase 6 — QA

- build, DOM gate, desktop/mobile visual, functional sliders/accordion/modal

### Phase 7 — Operator review

- Full page + shared block regression on Home and uslugi-v2

---

## 17. Scope manifest (implementation)

| File/path | Expected action | Allowed |
|---|---|---:|
| `src/pages/o-centre.html` | CREATE | 1 |
| `src/partials/sections/*` (new narrative) | CREATE 1–2 | 1 |
| Canonical partials CF-003–012 | INCLUDE only | 0 |
| `src/scss/style.scss` | ADD scoped blocks for new sections only | 1 |
| `src/js/main.js` | CHANGE only if new hook required | 0 expected |
| About assets under `src/img/` | ADD exports | 1 |
| Registries / audits | UPDATE status | 1 |

---

## 18. Protected source

All operator-canonical shared blocks (CF-003–CF-012), non-target `style.scss` regions, Home page sequence, V7, ORCA, SITE-002, package-lock, dist manual edits.

---

## 19. Risks

See risk register. Top: missing BLK-036–038 assets/copy; false reuse; SCSS regression.

---

## 20. Readiness gates

| Gate | Status | Missing |
|---|---|---|
| Design | PASS_WITH_KNOWN_GAPS | Fresh node IDs; PDF not in tree |
| Content | PASS_WITH_KNOWN_GAPS | BLK-037/038, steps |
| Assets | PASS_WITH_KNOWN_GAPS | About narrative exports |
| Reuse | PASS | — |
| Responsive | PASS | — |
| Accessibility | PASS_WITH_KNOWN_GAPS | Subnav label, comfort link |
| Implementation | PASS | Scope defined |

**Overall:** Ready for implementation **prompt** with asset/content prep in parallel.

---

## 21. Recommended implementation prompt scope

1. Phase 0–2 only if operator approves partial BLK-036 WIP copy
2. Asset prep task for Spig_v1.2.fig About frames before pixel QA on BLK-037/038
3. Explicit exclusions: home-gallery, home-staff-photo, V7 file copy
4. Commit boundary: page + new partials + scoped SCSS only

---

## 22. Final verdict

**`FP0002_V8_OCENTRE_PAGE_ANATOMY_REUSE_CHARTER_COMPLETE_WITH_KNOWN_GAPS`**

`implementation_authorized`: **false**

---

## 23. Asset + content resolution (2026-06-29)

**Task:** FP-0002 V8 O-Centre Asset + Content Resolution  
**Pack:** `../o-centre-asset-content-resolution/`

| Item | Result |
|---|---|
| Canonical Figma | `Spig_v1.2.fig` via fresh parse (`data/FP-0002-V8-OCENTRE-SPIG-V1-FIG-EXTRACT.json`) |
| Hero asset | `EXPORT_CANONICAL` → `src/img/content/o-centre/o-centre-hero.webp` |
| BLK-037/038 copy | **Resolved** — single `преимущества` frame `1:2440` |
| BLK-037/038 assets | **22 photos pending export** |
| BLK-018 steps | **RETIRED** — not in O-Centre Spig_v1.2; frame `1:2310` is who-we-treat (reconciliation 2026-06-29) |
| FAQ | **No accordion** — reuse CF-009 final form, not CF-008 |
| Subnav | **7 labels confirmed** (`1:2241`–`1:2247`) |
| Founder quote | **Blocked** — Lorem ipsum in node `1:2301` |

**Revised verdict:** `FP0002_V8_OCENTRE_ASSET_CONTENT_RESOLUTION_COMPLETE_WITH_KNOWN_GAPS`  
**Gate:** `READY_FOR_FP0002_V8_OCENTRE_TARGETED_ASSET_EXPORT`  
**implementation_authorized:** **false**

---

## Child documents

| Document | Path |
|---|---|
| Source register | `FP-0002-V8-OCENTRE-SOURCE-REGISTER-v1.md` |
| Design evidence | `FP-0002-V8-OCENTRE-DESIGN-EVIDENCE-v1.md` |
| Page anatomy | `FP-0002-V8-OCENTRE-PAGE-ANATOMY-v1.md` |
| Gallery audit | `FP-0002-V8-OCENTRE-GALLERY-REUSE-AUDIT-v1.md` |
| Staff-photo audit | `FP-0002-V8-OCENTRE-STAFF-PHOTO-REUSE-AUDIT-v1.md` |
| Content inventory | `FP-0002-V8-OCENTRE-CONTENT-INVENTORY-v1.md` |
| Asset inventory | `FP-0002-V8-OCENTRE-ASSET-INVENTORY-v1.md` |
| Composition map | `FP-0002-V8-OCENTRE-COMPOSITION-MAP-v1.md` |
| Link map | `FP-0002-V8-OCENTRE-LINK-MAP-v1.md` |
| Accessibility | `FP-0002-V8-OCENTRE-ACCESSIBILITY-CHARTER-v1.md` |
| Risks | `FP-0002-V8-OCENTRE-RISK-REGISTER-v1.md` |
| Machine-readable | `data/FP-0002-V8-OCENTRE-PAGE-ANATOMY-REUSE-CHARTER.json` |
| Resolution pack | `../o-centre-asset-content-resolution/` |
