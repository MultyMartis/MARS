# MARS Website Factory — Frontend Shell-First Start Protocol v1

**Status:** **documented** — mandatory **pre-production gate** before full page implementation in Factory Gulp projects.  
**Not:** runtime orchestration, automated workspace bootstrap, or CI enforcement.

**Triggers:** Any task to implement a **full site**, **multi-page set**, or **Home page first** without an existing approved foundation.

**Related:**

| Document | Role |
|----------|------|
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | **Canonical authority hierarchy** — ranks 1–6; OL-01–OL-07 |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | **Draft + Approval** — mandatory pre-Shell standards gate |
| [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | Section spacing tokens required in Production Standards |
| [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) | Mandatory Foundation Demo Page composition |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Token/visual review before Foundation QA |
| [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) | Compiled CSS + Operator Law enforcement |
| [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) | Operator Visual Review gate after every visual stage |
| [layout-spec-law-v1.md](layout-spec-law-v1.md) | **Layout Spec Gate** — composition spec before HTML/CSS; operator APPROVED |
| [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | **Clean Shell baseline** — HEADER/MAIN/FOOTER NOT STARTED only; before Layout Spec |
| [layout-shell-governance.md](layout-shell-governance.md) | HEADER != HERO; shell ownership |
| [frontend-production-rules-v0.md](frontend-production-rules-v0.md) | Source-first, build discipline |
| [website-factory-workflow-v0.md](website-factory-workflow-v0.md) | S10 Handoff → S11 Production |
| [onboarding-flow-v1.md](onboarding-flow-v1.md) Path B | Workspace bootstrap (partial overlap) |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## 1. Problem statement

Factory workflows historically allowed operators to request **«сверстать Главную»** immediately. That skips:

- Project **Production Standards** approval (radius, spacing, typography law)
- **Shell** (header / main / footer) and global tokens
- **Typography / UI demo page** for QA before page complexity
- **Desktop-first base** verification before mobile shell pass

**Gap identified (FP-0002 audit 2026-06-13):** Factory had **layout-shell-governance** and **cadence** methodology but **no mandatory start sequence** that forces Production Standards + foundation before Home page.

**Gap identified (FP-0002 header failure 2026-06-14):** Agent could receive Visual SSOT and implement Header from **internal composition interpretation** without a mandatory **Layout Spec** — closed by [layout-spec-law-v1.md](layout-spec-law-v1.md).

**Gap identified (FP-0002 RESET V3 2026-06-14):** Rich gulp-starter / foundation demo residue invited agent reuse before Layout Spec — closed by [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md).

---

## 2. Canonical stage chain (Factory v1)

```text
Production Standards Draft → DESIGN → FRONTEND MAPPING QA → Production Standards Approval → Shell → Visual Foundation → Design Calibration → Foundation QA → Home Production → Design Completeness → Frontend Design QA Matrix → Pixel Fidelity → Production PASS
```

**Foundation QA authority:** [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) — consolidated checklist; Phase 5 maps here.  
**Page QA (post–Home):** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) §7 · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6.

| Stage | Authority |
|-------|-----------|
| Production Standards Draft + Approval | [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| Visual Foundation | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) |
| Design Calibration | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |

Phases 0–6 below map to this chain; Phase 1–2 ≈ Shell + Visual Foundation; Phase 3–4 ≈ shell verification + mobile; **Design Calibration** runs after demo content is complete and before Phase 5 Foundation QA.

---

## 3. Protocol (mandatory order)

When Website Factory receives a frontend production request:

### Phase 0 — Standards gate (before any HTML)

**Authority:** [production-standards-governance-v1.md](production-standards-governance-v1.md)

| # | Deliverable | Owner | Blocks code if missing |
|---|-------------|-------|------------------------|
| 0.1 | **Production Standards Draft** — all mandatory categories (C-01–C-16) | Frontend Lead / Engineering | **Yes** (blocks Mapping QA) |
| 0.2 | **DESIGN → FRONTEND MAPPING QA** — mapping completeness gate on Draft | Frontend Lead / Engineering | **Yes** (blocks Approval) |
| 0.3 | **Production Standards Approval** — Lead sign-off on draft as project SSOT | Project Lead / Frontend Lead | **Yes** (blocks Shell) |
| 0.4 | Frontend Normalization / Numeric rules (if design pack exists) | Engineering | Partial — placeholders allowed per project policy |
| 0.5 | Section spacing mapped per [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | Production Standards doc | **Yes** |

**Rule:** If operator asks for Home page first → **redirect to Phase 1–3**; cite this protocol. Draft alone does **not** unlock Shell — **Mapping QA PASS** and **Approval PASS** required.

### Phase 0.5 — Clean Shell gate (before Layout Spec)

**Authority:** [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md)

| # | Deliverable | Blocks Layout Spec if missing |
|---|-------------|-------------------------------|
| 0.5.1 | Workspace on **Canonical Clean Shell v1** — `desktop-shell.html` with NOT STARTED markers only | **Yes** |
| 0.5.2 | No forbidden starter residue (header html, ui-demo, tokens, buttons, hero, etc.) | **Yes** |

**Rule:** Boring screen = correct. **AGENT HAS NOT STARTED INVENTING.**

### Phase 0.6 — Layout Spec gate (before shell HTML)

**Authority:** [layout-spec-law-v1.md](layout-spec-law-v1.md)

| # | Deliverable | Blocks shell HTML if missing |
|---|-------------|------------------------------|
| 0.6.1 | **Layout Spec — Header** | **Yes** |
| 0.6.2 | **Layout Spec — Footer** | **Yes** |
| 0.6.3 | Operator decision **APPROVED** on each spec | **Yes** |

**Rule:** **Forbidden** path: `Visual SSOT → Header/Footer HTML/CSS`. Agent **must stop** after Layout Spec until operator **APPROVED**.

### Phase 1 — Base shell (not Home)

| # | Step | Output |
|---|------|--------|
| 1.1 | Layout partials: **header**, **main**, **footer** | `src/partials/layout/` |
| 1.2 | Page shell entry (not Home) | e.g. `foundation.html` / `ui-demo.html` |
| 1.3 | Inside **`main`**: Visual Foundation demo content | [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §3 |

### Phase 2 — Global foundation styles

| # | Step | Output |
|---|------|--------|
| 2.1 | Global reset, base, typography tokens | `src/scss/base/` |
| 2.2 | Default content styles (lists, links, quotes, tables) | `src/scss/base/` or `components/` |
| 2.3 | Header + footer styles (desktop) | `src/scss/layout/` |
| 2.4 | Logo, favicon, core assets wired | `src/img/`, `src/favicon/` — logo selection per [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) when FIG has multi-brand candidates |

### Phase 3 — Desktop verification

| # | Step | Evidence |
|---|------|----------|
| 3.1 | Build succeeds | `npm run build` log in REPORT |
| 3.2 | Desktop QA: shell + demo page at ≥1024px | REPORT § QA + **OPERATOR VISUAL REVIEW** §5.7 |
| 3.3 | Production Standards spot-check (radius, type, spacing samples visible on demo page) | Lead ack or REPORT |
| 3.4 | **STOP** — operator visual review required before Phase 4 | [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) §5 — agent must request: «Откройте страницу. Проверьте результат. Требуется решение оператора.» |

### Phase 4 — Mobile shell pass

| # | Step | Output |
|---|------|--------|
| 4.1 | Header mobile behavior | Condensed nav / menu pattern |
| 4.2 | Footer stack | Mobile layout |
| 4.3 | Base typography + spacing mobile overrides | Per Production Standards |
| 4.4 | Sticky bar (if in scope) | Project block charter |

### Phase 4b — Design Calibration (before Foundation QA)

| # | Step | Authority |
|---|------|-----------|
| 4b.1 | Token spot-check on Foundation Demo Page vs Production Standards | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) §5 |
| 4b.2 | **COMPILED CSS SPOT-CHECK** on `dist/*.css` + Operator Law compliance | Calibration §5.7 · Enforcement Pack EG-02 |
| 4b.3 | Lead acknowledgment — `DESIGN CALIBRATION — PASS \| PASS WITH NOTES \| FAIL` | §6–7 |
| 4b.4 | Correction loop if FAIL — no Home work until PASS or approved partial | §7 |
| 4b.5 | **OPERATOR VISUAL REVIEW** — Design Calibration close | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.7 · **DESIGN CALIBRATION PASS ≠ OPERATOR APPROVAL** |

### Phase 5 — Foundation QA gate

**Authority:** [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) — mandatory checks §6; PASS/FAIL §5.

| # | Check |
|---|-------|
| 5.1 | Visual Foundation Contract complete ([frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §3) |
| 5.2 | Design Calibration PASS recorded |
| 5.3 | No Home page sections implemented yet |
| 5.4 | Enforcement gates: Operator Law, Compiled CSS, Inline Style, Authority Conflict, **ROOT COMPLIANCE** | [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) §6.13–6.17 |
| 5.5 | `# REPORT — <project> foundation QA` filed per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.1 + §5.4 + §5.7 |
| 5.6 | **OPERATOR VISUAL REVIEW** — **OPERATOR VISUAL ACCEPT — ACCEPT** on foundation demo URL | [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) · **FOUNDATION QA PASS ≠ OPERATOR APPROVAL** |

### Phase 6 — Page production (Home and others)

Only after Phase 5 technical PASS **and** Phase 5.6 **OPERATOR VISUAL ACCEPT — ACCEPT** (or Lead waiver):

- Home page (PG-001)
- Inner pages per Page Inventory / handoff

**After page/slice production:** run **Design Completeness → Frontend Design QA Matrix (full) → Pixel Fidelity → Production PASS** per [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12 — Foundation QA does **not** substitute for page closure.

---

## 4. Foundation Demo Page content (summary)

**Full obligation:** [frontend-visual-foundation-contract-v1.md](frontend-visual-foundation-contract-v1.md) §3.

Minimum demo blocks on the foundation page (legacy summary — do not treat as narrower than the contract):

| Block | Elements |
|-------|----------|
| **Headings** | H1–H6 per Production Standards scale |
| **Body** | Paragraphs, lead text, small/caption |
| **Lists** | ul, ol, nested |
| **Links** | inline, button-styled, nav sample |
| **Buttons** | primary, secondary, text CTA per standards |
| **Forms** | label, input, textarea, select if used, error state sample |
| **Text sections** | quote / demo block |
| **Tables** | if project uses tables |
| **Spacing samples** | same-bg gap, diff-bg gap labels (visual QA aid) |

**Purpose:** Single URL to verify tokens before multi-section Home complexity.

---

## 5. Agent / operator behavior

| Situation | Required response |
|-----------|-------------------|
| User: «Сверстай главную» | Acknowledge; **execute Phases 0–5 first** unless foundation REPORT exists |
| Missing Production Standards Draft | **STOP** — start Draft per [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| Draft exists, not approved | **STOP** — route to Lead for Approval; no Shell |
| Missing section spacing tokens | **STOP** — map [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| Workspace not on Clean Shell (starter demo, ui-demo, chrome visible) | **STOP** — [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) |
| Header/Footer HTML requested; Layout Spec missing or not APPROVED | **STOP** — [layout-spec-law-v1.md](layout-spec-law-v1.md) |
| Existing foundation REPORT + approved standards | May proceed to requested page **only if** **OPERATOR VISUAL ACCEPT — ACCEPT** recorded for foundation close |
| Agent closes visual stage without operator page review request | **STOP** — workflow violation per [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) §12 |

---

## 6. Workflow stage alignment

| Factory stage | This protocol |
|---------------|---------------|
| **Pre-S11** | Phases 0–5 = **Frontend Foundation** sub-stage (not in legacy S11 text — **documentation addendum**) |
| **S11 Frontend Production** | Starts at Phase 6 for page blocks **or** Phase 1 if greenfield |
| **S10 Handoff** | Must reference Production Standards + shell-first flag |

**Recommended handoff field (future):** `foundation_complete: true|false`.

---

## 7. Project instance — FP-0002

**Project sequence doc:** [FP-0002-FRONTEND-START-SEQUENCE-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-START-SEQUENCE-v1.md)

**Production Standards SSOT:** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md)

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — created from FP-0002 audit; closes Factory gap for automatic standards/foundation request. |
| 2026-06-13 | v1.1 — Evolution Pack: stage chain, Design Calibration phase, Visual Foundation Contract pointer. |
| 2026-06-13 | v1.2 — Production Standards Governance Pack: Draft + Approval split; Phase 0 aligned to [production-standards-governance-v1.md](production-standards-governance-v1.md). |
| 2026-06-13 | v1.3 — [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) pointer in Related. |
| 2026-06-14 | v1.4 — Enforcement Pack v1: Phase 4b compiled CSS spot-check; Phase 5 enforcement + ROOT COMPLIANCE. |
| 2026-06-14 | v1.5 — Operator Visual Approval Law: Phase 3.4 / 4b.5 / 5.6 operator visual review gates. |
| 2026-06-14 | v1.6 — Layout Spec Law: Phase 0.6 gate before shell HTML; [layout-spec-law-v1.md](layout-spec-law-v1.md). |
| 2026-06-14 | v1.7 — Canonical Clean Shell v1: Phase 0.5 gate; [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md). |
