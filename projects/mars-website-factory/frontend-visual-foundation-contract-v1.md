# MARS Website Factory — Frontend Visual Foundation Contract v1

**Status:** **documented** — mandatory **Foundation Demo Page** composition for all future Website Factory Gulp projects.  
**Not:** runtime schema, Storybook product, automated UI inventory checker, or project-specific Production Standards.

**Purpose:** Answer one question with zero ambiguity:

> **What must exist in the workspace before Home Production (PG-001 / first commercial page) may start?**

**Authority chain:**

| Layer | Document | Role |
|-------|----------|------|
| Start gate | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Mandatory order before page production |
| Standards | [production-standards-governance-v1.md](production-standards-governance-v1.md) | Draft + Approval before Shell |
| Calibration | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Human token/visual review on foundation page |
| Spacing | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) | Inter-section tokens + demo labels |
| Production law | Project **Production Standards** (per-project SSOT) | Token values, radius, type scale |
| Grid | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Section/container alignment on demo page |
| Precision | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Spacing scale + line-height law on demo samples |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Provenance:** FP-0002 Shpigovsky audit (2026-06-13) — practices promoted to Factory system rules. FP-0002 instance docs remain **read-only** reference; this contract is **forward-looking**.

---

## 1. Scope boundary

### 1.1 In scope

- **Foundation Demo Page** — first non-Home page entry (project slug: e.g. `ui-demo.html`, `foundation.html`; see [Naming Analysis](#7-naming-note) in Evolution Pack report).
- **Content inside `main`** on that page — typography, UI primitives, spacing samples.
- **Shell already present:** `header` + `main` + `footer` layout partials (Visual Foundation **builds on** Shell; does not replace it).

### 1.2 Out of scope (explicit)

- Home page sections (hero, commercial blocks, page-specific PG-* content).
- Inner pages beyond the foundation demo URL.
- Production Standards authorship — must exist **before** Visual Foundation work.
- Automated visual regression or CI enforcement — **planned only** unless project defines jobs.

---

## 2. Mandatory pre–Home Production gate

Home Production is **blocked** until **all** rows below are satisfied:

| # | Gate | Evidence |
|---|------|----------|
| G-VF-01 | **Production Standards** approved (project SSOT) | Signed doc or Lead ack in REPORT |
| G-VF-02 | **Shell** complete — header, main, footer partials + foundation page entry | Build includes layout; not `index.html` Home |
| G-VF-03 | **Visual Foundation Contract** — every §3 category present on demo page | This document checklist |
| G-VF-04 | **Design Calibration** stage PASS | [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) |
| G-VF-05 | **Foundation QA** REPORT filed + Lead ack | `# REPORT — <project> foundation QA` |
| G-VF-06 | **No Home block leakage** in codebase | Code review — no PG-001 blocks in foundation page |

**Operator rule:** If user requests Home first → execute gates G-VF-01 through G-VF-05; cite [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md).

---

## 3. Foundation Demo Page — mandatory composition

All categories below must be **visually rendered** on the foundation demo URL inside `main`. Values come from **Project Production Standards** — this contract defines **presence**, not px truth.

### 3.1 Typography

| Element | Requirement | Notes |
|---------|-------------|-------|
| **H1** | One sample at display/hero scale | Per standards type scale |
| **H2** | Section heading sample | Primary section rhythm |
| **H3** | Subsection sample | |
| **H4** | Card/block title sample | |
| **H5** | Optional if in standards | Required when standards define H5 |
| **H6** | Optional if in standards | Required when standards define H6 |
| **Paragraphs** | Body default + at least one secondary size (lead, body-sm, or caption) | Weight/line-height per standards; default Factory rule **`line-height = font-size + 4px`** unless project SSOT documents named exceptions ([frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3) |
| **Links** | Inline text link + at least one button-styled or nav-context link | Hover/focus visible |
| **Lists** | `ul`, `ol`, nested list sample | Spacing per standards |
| **Blockquote** | At least one quote / pull-quote block | Typography distinct from body |

### 3.2 Forms

| Element | Requirement | Notes |
|---------|-------------|-------|
| **Input** | Text input with label | Radius/control tokens per standards |
| **Textarea** | Multi-line field with label | |
| **Select** | Native or styled select | Required if project uses selects; else **SAFE UNKNOWN** with Lead ack |
| **Checkbox** | At least one labeled checkbox | |
| **Radio** | Radio group (≥2 options) | |
| **Validation state** | Error (and success if standards define) on at least one field | `.has-error` / equivalent state class — not inline-only styling |

**Reference (implementation patterns):** [foundation-systems/form-system-v2.md](foundation-systems/form-system-v2.md) — Wave 2; adopt when workspace uses shared form partials.

### 3.3 Buttons

| Variant | Requirement |
|---------|-------------|
| **Primary** | Default CTA — full height/radius per standards |
| **Secondary** | Filled or tonal secondary action |
| **Outline** | Ghost/outline variant |
| **Disabled** | Visually distinct disabled state on one sample |

Include at least one **header-context** button size if standards define header CTA separately from body CTAs.

### 3.4 Content patterns

| Pattern | Requirement | Notes |
|---------|-------------|-------|
| **Cards** | At least one card surface | Radius/shadow per standards |
| **Table** | Simple data table | Required if project uses tables; else note **N/A** in REPORT |
| **FAQ** | Accordion or `<details>` demo | One-open behavior per [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) |
| **Alerts** | Info + error (or warning) alert samples | Semantic color roles |
| **Spacing examples** | Labeled blocks demonstrating **same-bg gap** and **different-bg / band gap** | Maps [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md); labels must name token or px value |

### 3.5 Media

| Element | Requirement | Notes |
|---------|-------------|-------|
| **Image** | Responsive image sample with alt text | Real asset or project placeholder policy |
| **Video wrapper** | 16:9 (or project ratio) embed shell | iframe or `<video>` wrapper — no autoplay policy violation |

---

## 4. Desktop and mobile visibility

| Viewport | Rule |
|----------|------|
| **Desktop** | All §3 categories visible at ≥ project desktop breakpoint (Factory default **1024px**) |
| **Mobile** | Shell + typography + primary button + one spacing sample readable at ≤ mobile breakpoint |
| **Full mobile pass** | May complete during Shell mobile phase; Visual Foundation content must not **break** mobile shell |

Design Calibration (separate stage) verifies token fidelity; this contract verifies **composition completeness**.

---

## 5. REPORT checklist line

Foundation QA REPORT must include:

```text
VISUAL FOUNDATION CONTRACT — PASS | partial (list missing) | FAIL
```

When **partial**, list missing §3 categories explicitly. **FAIL** blocks Home Production.

Optional compact matrix:

```text
VF-TYPE · VF-FORMS · VF-BUTTONS · VF-CONTENT · VF-MEDIA — PASS | FAIL
```

---

## 6. Relationship to Factory start sequence

**Canonical chain (Factory v1 evolution):**

```text
Production Standards Draft
        ↓
Production Standards Approval
        ↓
      Shell
        ↓
Visual Foundation   ← this contract (§3 composition)
        ↓
Design Calibration
        ↓
  Foundation QA
        ↓
 Home Production
        ↓
Design Completeness Audit → Frontend Design QA Matrix (full) → Pixel Fidelity Audit → Production PASS
```

**Foundation QA:** [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · **Page QA chain:** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12.

**Legacy alias:** “Typography / UI demo page” in older docs = **Visual Foundation** content on Foundation Demo Page — same obligation, clearer stage name.

---

## 7. Project instance reference (read-only)

FP-0002 Shpigovsky documents **instance** checklist — **do not edit** for Factory evolution:

- [FP-0002-FRONTEND-START-SEQUENCE-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-START-SEQUENCE-v1.md) Step 2
- [FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-FRONTEND-PRODUCTION-CHARTER-v1.md) §13.2

Future projects follow **this contract**, not FP-0002 row-by-row px values.

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — created from Website Factory Frontend Knowledge Audit / FP-0002 Shpigovsky practices; Evolution Pack v1. |
| 2026-06-13 | v1.1 — Stage chain: Production Standards Draft → Approval ([production-standards-governance-v1.md](production-standards-governance-v1.md)). |
| 2026-06-13 | v1.2 — Precision Governance cross-ref: line-height law on typography samples. |
