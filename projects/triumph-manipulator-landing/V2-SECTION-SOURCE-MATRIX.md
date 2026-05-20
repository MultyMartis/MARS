# V2 Section Source Matrix

## 1. Purpose

This matrix **prevents V1/V2 blending** by tying each visible block on the current V2 homepage to **concrete include paths**, **SCSS entrypoints**, and **declared design layers**. Forge and frontend agents can use it as a **file-level map**: what is on the page, what styles it, and where truth still requires **pixel / operator** confirmation.

**Scope:** documentation only. It reflects `src/pages/index.html` and `src/scss/style.scss` as of the authoring pass; it does not replace **`projects/triumph-manipulator-landing/design/v2/`** (canonical V2 **visual** source). The retired V2 rules PDF is **not** authoritative — see [V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md).

---

## 2. Canonical rule

V2 implementation and edits must follow, in order:

1. [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md)
2. `projects/triumph-manipulator-landing/design/v2/`
3. Approved V2 text from **`design/v2/`** (as shown in PNGs) or **explicit operator instruction**
4. **Active** HTML: every `@@include(...)` referenced from `workspaces/triumph-manipulator-landing-v2/src/pages/index.html`
5. **Active** styles: every `@use` referenced from `workspaces/triumph-manipulator-landing-v2/src/scss/style.scss`

If any of the above conflict, **stop and report** (per [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) §6).

---

### NEXT IMPLEMENTATION RULE

The **next** implementation cycle must **start from** `projects/triumph-manipulator-landing/design/v2/01.png` and proceed **in order** through `07.png`, **screen by screen**. **Do not** continue from stale DOM assumptions; **do not** use `design/v1/` as semantic source; **do not** wire **`equipment-prices`** into the **homepage** `index.html` — it lives only on **`validation-equipment-prices.html`** (**EXPERIMENTAL / VALIDATION quarantine**, operator-approved 2026-05-16); **do not** invent copy; **do not** change section meaning without operator approval.

**Per screen (repeat until done):** (1) pick one `design/v2/NN.png`, (2) extract meaning + locked text, (3) confirm partial/SCSS or mark missing, (4) implement **only** that screen, (5) semantic QA, (6) responsive QA, (7) freeze before next screen.

Normative copy of this rule: [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) **NEXT IMPLEMENTATION RULE**.

---

### Design version isolation

Normative folder discipline (active generation, archive vs shared assets, visual ≠ semantic) lives in [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) §4 and [`design/README.md`](./design/README.md).

---

## 3. Section matrix

**Convention:** Paths below are relative to `workspaces/triumph-manipulator-landing-v2/src/` unless noted.

**Visual source:** Exact mapping of each row to `projects/triumph-manipulator-landing/design/v2/01.png` … `07.png` or `full.png` was **not** confirmed by image/PDF review in this task → **SAFE UNKNOWN** per row unless otherwise stated.

**Text/content source:** Markup may contain implementation copy; **canonical** copy is only what is approved on V2 mockups or by operator → default **SAFE UNKNOWN** until verified.

| Order | Section meaning | Include / partial path | SCSS path | Visual source | Text/content source | Status | Risk / SAFE UNKNOWN |
|------:|-----------------|------------------------|-----------|---------------|---------------------|--------|---------------------|
| 1 | Document `<head>` (meta, title, assets) | `partials/layout/head.html` | Global bundle via `scss/style.scss` (no section file) | **SAFE UNKNOWN** (not a full-screen mock slice by default) | Meta/title in include params — verify vs operator SEO/mockups | **ACTIVE** | Copy/SEO may drift from approved brief |
| 2 | Site header (nav, phone, social) | `partials/layout/header.html` | `scss/layout/_header.scss` | **SAFE UNKNOWN** | Nav labels in partial — verify vs mockups/PDF | **ACTIVE** | Anchor targets must stay aligned with section `id`s |
| 3 | Hero: offer, pricing band, primary conversion | `partials/sections/hero-conversion.html` | `scss/sections/_hero-conversion.scss` | **SAFE UNKNOWN** (`design/v2/*.png` not matched here) | Rich copy in partial — **verify** vs approved V2 mockups | **ACTIVE** | Do not “improve” headings without approval |
| 4 | **One machine:** specs, transport lists (Hino / UNIC) | `partials/sections/machine-specs-transport-lists.html` | `scss/sections/_machine-specs-transport-lists.scss` | **SAFE UNKNOWN** | Copy in partial — verify; section intent is **single machine** per stabilization doc | **ACTIVE** | Do not convert to multi-machine / fleet narrative |
| 5 | Trust / cases (layout present; much stub markup) | `partials/sections/trust-cases-social-proof.html` | `scss/sections/_trust-cases-social-proof.scss` | **`design/v2/03.png`** (visual third screen — cases) | **SAFE UNKNOWN** — stubs / minimal visible copy | **ACTIVE** (incomplete UX) | Filler/stub danger — no invented case copy |
| 6 | Segments / applications grid (stub cards) | `partials/sections/segments-applications-grid.html` | `scss/sections/_segments-applications-grid.scss` | **`design/v2/04.png`** | **SAFE UNKNOWN** — stubs | **ACTIVE** (incomplete UX) | Do not invent segment titles |
| 7 | Problem–solution matrix (stubs) | `partials/sections/problem-solution-matrix.html` | `scss/sections/_problem-solution-matrix.scss` | **`design/v2/05.png`** | **SAFE UNKNOWN** — stubs | **ACTIVE** (incomplete UX) | Do not invent FAQ answers |
| 8 | Consultation / lead form (stubs + CTA control) | `partials/sections/consultation-lead-form.html` | `scss/sections/_consultation-lead-form.scss` | **`design/v2/06.png`** | **SAFE UNKNOWN** — partial mostly stubs | **ACTIVE** (incomplete UX) | Form labels/legal copy need approved source |
| 9 | Site footer V2 (shell sections) | `partials/sections/site-footer-v2.html` | `scss/sections/_site-footer-v2.scss` + `scss/layout/_footer.scss` | **`design/v2/07.png`** | **SAFE UNKNOWN** — mostly empty columns in partial | **ACTIVE** (incomplete UX) | Footer legal/contact must come from approved source |
| 10 | Closing scripts | `partials/layout/scripts.html` | — (JS pipeline) | — | — | **ACTIVE** | Behavior must match approved design interactions |
| — | **Quarantine:** Equipment fleet cards / rental pricing (`equipment-prices`) | `partials/sections/equipment-prices.html` (included **only** from `pages/validation-equipment-prices.html`) | `scss/sections/_equipment-prices.scss` (still in bundle) | **No** matching `design/v2` slice between `02` and `03` | Copy in partial — **not** V2 homepage truth | **EXPERIMENTAL / VALIDATION** | **Not homepage.** Preserved for fleet-mode / validation review; CTA targets `index.html#kontakty`. Do **not** re-include into `index.html` without a new operator gate. |

**`<main>` block count on homepage (content sections only):** 6 — `hero-conversion` → `machine-specs-transport-lists` → `trust-cases-social-proof` → `segments-applications-grid` → `problem-solution-matrix` → `consultation-lead-form`, aligned with **`01.png`–`06.png`**; footer partial maps to **`07.png`** (after `</main>`).

---

## 4. Active implementation files

### 4.1 All `@@include` targets from `src/pages/index.html`

| Path |
|------|
| `partials/layout/head.html` |
| `partials/layout/header.html` |
| `partials/sections/hero-conversion.html` |
| `partials/sections/machine-specs-transport-lists.html` |
| `partials/sections/trust-cases-social-proof.html` |
| `partials/sections/segments-applications-grid.html` |
| `partials/sections/problem-solution-matrix.html` |
| `partials/sections/consultation-lead-form.html` |
| `partials/sections/site-footer-v2.html` |
| `partials/layout/scripts.html` |

**Validation-only page (not homepage):** `pages/validation-equipment-prices.html` → includes `partials/sections/equipment-prices.html` only.

Nested includes (e.g. `partials/components/*` inside sections/layout) are **ACTIVE** only when pulled in by the above; they are not listed exhaustively here.

### 4.2 All SCSS modules pulled in by `src/scss/style.scss`

**Base**

- `scss/base/_reset.scss`
- `scss/base/_base.scss`

**Layout**

- `scss/layout/_header.scss`
- `scss/layout/_footer.scss`

**Sections**

- `scss/sections/_page-intro.scss`
- `scss/sections/_advantages.scss`
- `scss/sections/_contacts.scss`
- `scss/sections/_hero-conversion.scss`
- `scss/sections/_machine-specs-transport-lists.scss`
- `scss/sections/_equipment-prices.scss`
- `scss/sections/_trust-cases-social-proof.scss`
- `scss/sections/_segments-applications-grid.scss`
- `scss/sections/_problem-solution-matrix.scss`
- `scss/sections/_consultation-lead-form.scss`
- `scss/sections/_site-footer-v2.scss`

**Components**

- `scss/components/_icon.scss`
- `scss/components/_button.scss`
- `scss/components/_breadcrumb.scss`
- `scss/components/_modal.scss`

**Note:** `_page-intro`, `_advantages`, and `_contacts` are **bundled** but **not** used by the current `index.html` (see §5).

---

## 5. Legacy / do-not-use files discovered nearby

Listed from **`src/partials/sections/`** and **`src/scss/sections/`** without repo-wide search. **Do not** treat these as homepage truth for V2 unless a page explicitly includes them later.

### 5.1 Section partials present on disk but **not** included in `index.html`

| File | Likely role |
|------|-------------|
| `partials/sections/landing-strip-01.html` | Legacy landing-strip naming (V1-era pattern) |
| `partials/sections/landing-strip-02.html` | Same |
| `partials/sections/landing-strip-03.html` | Same |
| `partials/sections/landing-strip-04.html` | Same |
| `partials/sections/faq-cta-footer.html` | Alternate FAQ/footer composition |
| `partials/sections/hero.html` | Legacy hero (distinct from `hero-conversion`) |
| `partials/sections/page-intro.html` | Generic intro block |
| `partials/sections/advantages.html` | Advantages block |
| `partials/sections/contacts.html` | Contacts block |
| `partials/sections/trust-reviews.html` | Reviews/trust variant |
| `partials/sections/equipment-prices.html` | **Quarantine:** used **only** by `validation-equipment-prices.html`, **not** by `index.html` |

**Status for current V2 homepage:** legacy partials in §5.1 are **not** in `index.html`. **`equipment-prices`** is **validation-page-only** (see §4.1), not homepage flow.

### 5.2 SCSS section files on disk **not** referenced by `style.scss`

Not compiled via current `style.scss` chain (orphan **.scss** neighbors):

| File |
|------|
| `scss/sections/_landing-strip-01.scss` |
| `scss/sections/_landing-strip-02.scss` |
| `scss/sections/_landing-strip-03.scss` |
| `scss/sections/_landing-strip-04.scss` |
| `scss/sections/_faq-cta-footer.scss` |
| `scss/sections/_hero.scss` |
| `scss/sections/_trust-reviews.scss` |

### 5.3 SCSS referenced by `style.scss` but **no** matching section partial in `index.html`

| SCSS module | Partial(s) on disk (not used by homepage) |
|-------------|-------------------------------------------|
| `_equipment-prices.scss` | `partials/sections/equipment-prices.html` (**only** `validation-equipment-prices.html`, not homepage) |
| `_page-intro.scss` | `partials/sections/page-intro.html` |
| `_advantages.scss` | `partials/sections/advantages.html` |
| `_contacts.scss` | `partials/sections/contacts.html` |

**Status:** **Bundle residue / potential legacy** for this page — CSS may still ship; HTML is absent. Prefer explicit cleanup plan later with operator approval.

---

## 6. Known conflicts

- **Old V1 strip maps** (`landing-strip-*` names) may describe **V1** structure — not authoritative for `index.html` order.
- **Legacy partial names** remain in the workspace; they are easy to confuse with active V2 sections.
- **V2 `index.html` order** may differ from older freeze or handoff docs — this matrix follows **live** includes only.
- **`design/v2/01.png`–`07.png` vs `<main>` blocks:** one-to-one mapping **not** established here → **SAFE UNKNOWN** until pixel/PDF mapping is done.
- **Third-screen semantics (resolved for homepage, 2026-05-16):** canonical **PNG** `03.png` (кейсы) ↔ **third `<main>` include** `trust-cases-social-proof`. Former **`equipment-prices`** / «третий include ≠ третий PNG» collision is **closed on the homepage** — that block is isolated on `validation-equipment-prices.html` only.

---

## 7. Editing protocol for Forge

**Default path:** follow [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md) **NEXT IMPLEMENTATION RULE** — one `design/v2/NN.png` at a time, starting at `01.png`, then semantic QA, responsive QA, freeze.

Before editing any block (including matrix rows **not** in the current PNG scope — avoid drive-by edits):

1. **Confirm** the active **`design/v2/NN.png`** for this step; **do not** assume correctness from current DOM order alone.
2. **Identify** the row in §3 (section matrix) that matches **that** PNG’s meaning.
3. **Verify** section meaning (and that it is not a legacy/V1 strip).
4. **Verify** visual source: open the **correct** `design/v2` PNG; if unclear, mark **SAFE UNKNOWN** and escalate.
5. **Verify** partial: path must match §4.1 for homepage work **or** be explicitly added for the PNG scope.
6. **Verify** SCSS: primary section file in §3; check §5 for stray globals/residue.
7. If **`design/v2/` vs `src/`** or **MD rules vs `src/`** conflict appears → **stop and report**; do not “pick” silently.
8. **Do not invent** marketing copy, FAQs, cases, or segment text.
9. **Do not import** V1 content, V1 mockups, or old strip order as truth.
10. **`equipment-prices`:** **homepage wiring removed** (2026-05-16). Block exists **only** on `validation-equipment-prices.html` — do **not** re-add to `index.html` without a **new** operator gate.

---

## 8. SAFE UNKNOWN

The following could **not** be confirmed **without** visual/PDF/pixel review, operator sign-off, or cross-doc freeze alignment:

| Item |
|------|
| Which `design/v2/01.png` … `07.png` (and `full.png`) map to which matrix row / partial |
| Whether current HTML copy in `hero-conversion`, `machine-specs-transport-lists`, and **`equipment-prices` (validation page only)** matches **approved** mockup text verbatim |
| Intended final content for stub-heavy sections: `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, `site-footer-v2` |
| Whether **`equipment-prices`** should ever return to homepage (requires **new** written operator decision beyond the 2026-05-16 removal) |
| Whether bundled `_page-intro` / `_advantages` / `_contacts` styles are intentional dead weight or planned for another page |
| All nested `partials/components/*` dependencies and their design source (not exhaustively enumerated here) |

---

## Document control

- **Companion:** [V2-FRONTEND-SOURCE-OF-TRUTH.md](./V2-FRONTEND-SOURCE-OF-TRUTH.md)  
- **Authoring method:** Read `index.html`, `style.scss`, section partial headers, and directory listings; **no** mockup pixels or PDF text extraction performed.
