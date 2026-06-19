# REPORT — WF-R01.3.2 WAVE A3 TESTIMONIALS + TRUST SPLIT

**Artifact ID:** WF-R01.3.2 Wave A3 — TESTIMONIALS + TRUST split (v1)  
**Date:** 2026-06-19  
**Mode:** controlled reference-layer execution pass — **one wave slice (two partials, vocabulary split only)**  
**Authority:** [wf-r01-3-2-landing-completion-charter-v1.md](../projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md) (**ACCEPTED**)

**Honesty boundary:** Human-operated extraction pass. **REFERENCE PARTIAL BUILT** — **not** VERIFIED, **not** PRODUCTION PASS. **Not** runtime. **No** new `block_id` minted.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **RC** | **32/32** (unchanged) |
| **RPC before** | **11/32** (~34.4%) |
| **RPC after** | **12/32** (~37.5%) |
| **Current gate** | **G0** |
| **Next wave** | **WF-R01.3.2 Wave B1 — FOOTER** |

---

## 2. Pre-Wave Reconciliation

| Item | Detail |
|------|--------|
| **roadmap changes** | R01.2 Gate 2 **COMPLETE**; R01.3.2 **ACCEPTED / ACTIVE**; Wave A1/A2 status; pre-A3 next step |
| **OPERATIONAL-INDEX changes** | WF-R01 program row aligned to Gate 2 + Wave A1/A2 + G0 |
| **checkpoint commit** | `765d579` — `foundry: checkpoint WF-R01 through landing wave A2` (48 files, FOUNDRY scope only) |
| **push result** | **Not attempted** — branch `mars/post-cycle8-live-tests` has extensive unrelated WIP; safe isolated push deferred |

---

## 3. Source

| Item | Detail |
|------|--------|
| **exact Triumph V6 source path** | `workspaces/triumph-manipulator-landing-v6/src/partials/sections/screen-03-trust-reviews.html` (canonical); alternate: `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-page01/screen-03-trust-reviews.html` |
| **extracted structural pattern** | Two-zone composition: **left** `trust-cards` grid (objective proof cards) → **TRUST** semantics; **right** `review-panel` + `review-list` + `review-card` (quotes, author, role, stars, source) → **TESTIMONIALS** semantics |
| **excluded client-specific content** | Russian copy, brand names (Триумф, Крайинвест, etc.), personal names, platform logos (Yandex/Avito/2GIS), phone/CTA links, Font Awesome icons, production image paths |

---

## 4. Vocabulary Decision

| Block | Definition | Boundaries confirmed |
|-------|------------|---------------------|
| **TESTIMONIALS** | F3 Content block — curated quotes, ratings per review, author/role placeholders | **No** logos, metrics strip, badges, or aggregate trust KPIs as primary content |
| **TRUST** | F3 Content/evidence block — logos, metrics, badges | **No** full review list or quote cards |
| **Hard rule** | `TESTIMONIALS ≠ TRUST` | **No** new `block_id`; **no** SOCIAL_PROOF canonical type; **no** F5 Trust Pattern merge |

---

## 5. Files Created

| File | Purpose |
|------|---------|
| `workspaces/website-factory-reference-v1/src/partials/sections/testimonials.html` | TESTIMONIALS reference partial — 3 neutral review cards |
| `workspaces/website-factory-reference-v1/src/scss/sections/_testimonials.scss` | Scoped styles for testimonials block |
| `workspaces/website-factory-reference-v1/src/partials/sections/trust.html` | TRUST reference partial — metrics, logos, badges |
| `workspaces/website-factory-reference-v1/src/scss/sections/_trust.scss` | Scoped styles for narrowed TRUST block |
| `reports/wf-r01-3-2-wave-a3-testimonials-trust-v1.md` | This report |

---

## 6. Files Modified

| File | Change |
|------|--------|
| `workspaces/website-factory-reference-v1/src/pages/index.html` | Golden slice: TESTIMONIALS + TRUST after PROCESS; removed `social_proof` include |
| `workspaces/website-factory-reference-v1/src/scss/main.scss` | `@use testimonials` + `@use trust`; removed `social_proof` |
| `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | TESTIMONIALS → `testimonials.html` **PARTIAL**; TRUST → `trust.html` **PARTIAL, narrowed** |
| `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Reference rows + coverage table for TESTIMONIALS + TRUST |
| `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Split gap **IMPLEMENTED**; SCSS coverage list updated |
| `projects/mars-website-factory/roadmap.md` | Wave A3 **COMPLETE**; RPC **12/32**; next B1 FOOTER |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Wave A3 status line |

---

## 7. TESTIMONIALS Implementation

| Aspect | Detail |
|--------|--------|
| **structure** | `wf-section--testimonials` → header (eyebrow, h2, lead) → 3-column review card grid (`<ul>` / `<article>`) |
| **semantics** | `data-block-id="testimonials"`; quote + author + role + per-item star rating + neutral source label |
| **responsive behavior** | 3-column grid ≥1025px logic via `$bp-lg` down → single column stack |
| **exclusions** | No Swiper/JS; no platform logos; no trust metrics; no client brand |

---

## 8. TRUST Narrowing

| Aspect | Detail |
|--------|--------|
| **previous mixed semantics** | Registry mapped `social_proof.html` to TRUST while TESTIMONIALS row noted overlap; filename/class `social-proof` misaligned with vocabulary canon |
| **resulting TRUST-only semantics** | Metrics strip + logo placeholders + proof badges only |
| **rename decision** | **Renamed** `social_proof.html` → `trust.html`, `_social_proof.scss` → `_trust.scss`; classes `wf-trust__*`; `data-block-id="trust"` |
| **dependency updates** | `index.html`, `main.scss`, three registry docs (BLOCK-REGISTRY, CORE-BLOCK-LIBRARY, BLOCK-GAPS) |

**Note:** Legacy references to `social_proof` remain in frozen snapshots (`snapshots/engine-readiness-audit-v1/`), blueprint v1 human label, and README — **not** updated in this pass (out of Wave A3 registry row scope).

---

## 9. Registry Impact

| Row | Update |
|-----|--------|
| **TESTIMONIALS** | Reference partial `testimonials.html` — **PARTIAL** |
| **TRUST** | Reference partial `trust.html` — **PARTIAL, narrowed** |
| **RC** | **32/32** unchanged |
| **RPC calculation** | **11/32 → 12/32** — **+1** for new `testimonials.html` partial-equivalent; TRUST already counted in RPC (file rename/narrow only, no second RPC unit) |

---

## 10. Golden Slice

Exact section order after Wave A3:

```text
HERO
BENEFITS
PROCESS
TESTIMONIALS
TRUST
CASES
PRICING
LEAD_FORM
CTA (cta_band)
FAQ
CONTACTS (contact_block)
```

(+ layout `footer`, `sticky_cta`, `modal_callback` unchanged)

---

## 11. Validation

| Check | Result |
|-------|--------|
| HTML includes | **PASS** — `testimonials.html`, `trust.html` included; no `@@include` leftovers in dist |
| SCSS imports | **PASS** — `testimonials`, `trust` in `main.scss`; no `social_proof` import |
| orphan check | **PASS** — `social_proof.html` / `_social_proof.scss` removed |
| duplicate check | **PASS** — no duplicate includes or SCSS imports |
| desktop sanity | **PASS** (structural) — dist contains separate `wf-section--testimonials` and `wf-section--trust` |
| mobile sanity | **PASS** (structural) — testimonials grid collapses to 1 column via `$bp-lg` |

**Boundary:** BUILT ≠ VERIFIED ≠ PRODUCTION PASS — no pixel-perfect or operator visual approval claimed.

---

## 12. Build

| Field | Value |
|-------|-------|
| **command** | `npm install` + `npm run build` in `workspaces/website-factory-reference-v1/` |
| **exit result** | **0** |
| **dist verification** | `dist/index.html` contains `wf-section--testimonials` and `wf-section--trust`; no `wf-section--social-proof` |
| **warnings** | Dart Sass legacy JS API deprecation (pre-existing); npm audit vulnerabilities (pre-existing, not addressed) |

---

## 13. Drift and Risks

| Severity | Finding | Action |
|----------|---------|--------|
| Low | `LANDING-BLUEPRINT-v1.md` still lists `social_proof` filename | Defer to R01.6 hygiene / Wave B |
| Low | `SITE-TYPE-BLOCK-MAPPING-v1.md` reference list stale | Defer to registry sync pass |
| Low | Snapshot copies under `snapshots/` retain old `social_proof` mapping | Frozen audit artifacts — do not auto-sync |
| Info | Checkpoint push not performed | Local commits only; operator may push when branch clean |

---

## 14. Git State

| Field | Value |
|-------|-------|
| **branch** | `mars/post-cycle8-live-tests` |
| **first checkpoint commit** | `765d579` — `foundry: checkpoint WF-R01 through landing wave A2` |
| **Wave A3 commit** | *(pending in same session — `foundry: complete landing wave A3 testimonials trust split`)* |
| **push status** | **Not pushed** — unrelated lane WIP on branch |
| **remaining unrelated WIP** | MIG, OCPilot, Triumph v6, ORCA, `.recovery-temp`, etc. |
| **foreign lane confirmation** | Checkpoint commit contained **only** FOUNDRY-scope paths (48 files verified via `git diff --cached --name-status`) |

---

## 15. Final Status

```text
COMPLETE
```

---

## 16. Next Task

```text
WF-R01.3.2 Wave B1 — FOOTER
```

**Not executed.**

---

## 17. Exact Evidence Paths

- `workspaces/triumph-manipulator-landing-v6/src/partials/sections/screen-03-trust-reviews.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/testimonials.html`
- `workspaces/website-factory-reference-v1/src/partials/sections/trust.html`
- `workspaces/website-factory-reference-v1/src/scss/sections/_testimonials.scss`
- `workspaces/website-factory-reference-v1/src/scss/sections/_trust.scss`
- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/src/scss/main.scss`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md`
- `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md`
- `workspaces/website-factory-reference-v1/dist/index.html`
- `projects/mars-website-factory/roadmap.md`
- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `reports/wf-r01-3-2-wave-a3-testimonials-trust-v1.md`

---

## 18. Stop Confirmation

```text
Wave B1 FOOTER: NOT STARTED
Wave B2 LEGAL_LINKS: NOT STARTED
Wave C2 HEADER_NAV: NOT STARTED
```
