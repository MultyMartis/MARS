# MARS Website Factory — Pixel Fidelity Audit Rules v1

**Status:** **documented** — **human-operated** audit rules that prevent visual drift between **approved design source** and **frontend implementation**.  
**Not:** automated pixel diff engine, Percy/Chromatic product, computer vision, or objective visual scoring system.

**Purpose:** Define **what to compare**, **acceptable variance**, and **non-acceptable variance** for typography, container, spacing, layout, components, responsive behavior, and assets — before **Production PASS**.

**Companion matrix:** [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) — domain PASS/FAIL and final verdict.

**Enforcement cross-ref:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) — PF-* numeric checks must use **`dist/*.css`** evidence when build succeeds; source-only SCSS does not satisfy Compiled CSS Compliance.

**Authority order:** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — **Project Production Standards (rank 1)** and **Approved Operator Laws (rank 2)** beat source measurement ambiguity and **always** beat agent aesthetic judgment.

---

## 0. Global audit principles

### 0.1 Authority sources (compare targets)

| Priority | Authority | Role in audit |
|----------|-----------|---------------|
| **1** | **Project Production Standards** (approved SSOT) | **Primary numeric authority** after Approval |
| **2** | **Approved design source** (Figma / PDF / PNG / JPG / WebP / Screenshot Pack / Mixed) | Evidence for values **before** or **alongside** SSOT mapping |
| **3** | **Operator Laws + Factory precision** (OL-01, OL-05, WF-GRID, WF-LAYOUT) | Normalization and layout chain |
| **4** | **Layout Pattern Library (LP-*)** | Named zone geometry |

**Typography:** project-approved values are **authority**.  
**Spacing:** project-approved values are **authority** (mapped to OL-01 scale when Factory-default).  
**Layout:** approved pattern (WF-GRID + WF-LAYOUT + LP-*) is **authority** — not eyeball composition.

### 0.2 Forbidden audit rationale

The following are **never** valid reasons to accept or introduce variance:

- “Looks cleaner”
- “Looks more modern”
- “Industry best practice prefers…”
- “Agent improved visual hierarchy”
- “Starter template looks fine”
- “Close enough visually” without SSOT or PF acceptable band

**Cross-ref:** [beautification-drift-governance.md](beautification-drift-governance.md) · [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) rank 6.

### 0.4 Anti-generative-fill (PIXEL_PERFECT only)

When passport `production_mode: PIXEL_PERFECT`:

| Missing data | Forbidden | Required |
|--------------|-----------|----------|
| FIG/component text | Generate, paraphrase, invent copy | **SAFE UNKNOWN** or **STOP** + HITL |
| Review/card bodies | Generic filler | Text lock from extract |
| Images | CSS placeholders, collision hashes | Asset manifest + brand chain |

**Authority:** [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) §7 · FP-0002 FAIL-002, FAIL-003, FAIL-006, FAIL-008.

**Rule:** PF-* **FAIL** or gate **UNKNOWN** — not «close enough» via generative fill.

### 0.5 Measurement method (honest scope)

| Method | Allowed claim |
|--------|---------------|
| DevTools computed styles vs SSOT table | **Numeric compare** for PF-* |
| Side-by-side screenshot vs export | **Qualitative + approximate** — cite viewport and zoom |
| Figma inspect / export spec | **Numeric** when spec is approved |
| Agent visual estimate without DevTools | **SAFE UNKNOWN** — not PASS |

**No pixel-perfect automation** is claimed by Factory v1 unless project documents tooling ([qa-drift-taxonomy.md](qa-drift-taxonomy.md) — unverifiable pixel claims).

---

## PF-01 — Typography fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| Font family stack | SSOT C-02 / type table |
| Font sizes (H1–H6, body, secondary) | SSOT px values |
| Font weights | SSOT |
| Line-heights | SSOT; default Factory rule `line-height = font-size + 4px` ([frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3) |
| Letter-spacing | SSOT when defined |
| RU overflow behavior | [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) |

### Acceptable variance

| Condition | Band |
|-----------|------|
| Size/weight/line-height **exact match** to SSOT | PASS |
| Named SSOT exception with C-12 / standards clause | PASS |
| Design raw value mapped to **nearest OL-01-adjacent type row** with documented mapping QA record | PASS |
| Line-height within **±0px** of SSOT or Factory default formula | PASS |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Any tier off SSOT without documented exception | **Major** minimum |
| Arbitrary font-size not in scale (e.g. `19px`, `22px`) without SSOT token | **Major** |
| Agent-changed size “for readability” | **Critical** (authority inversion) |
| Forbidden word-break / mid-word split on RU UI | **Critical** |
| Relative line-height (`1.15`, `1.375`) hiding px cadence when SSOT specifies px | **Major** |

---

## PF-02 — Container fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| `--container-max` / max-width | SSOT C-01 |
| `--container-pad` desktop / mobile | SSOT C-01 |
| Section vs inner container structure | WF-GRID-001 |
| Full-bleed band vs content width | WF-GRID-004 |
| Header / hero / section / footer alignment | WF-GRID-005 |

### Acceptable variance

| Condition | Band |
|-----------|------|
| Container tokens match SSOT exactly | PASS |
| `WF-GRID-EXCEPTION` comment with approver + date for local override | PASS WITH NOTES |
| Sub-pixel rounding from browser (±1px computed) | **Observation** only if no visible misalignment |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Container class on `<section>` / `<nav>` | **Critical** |
| Per-section silent max-width drift | **Major** |
| Column split bypassing shell / container | **Major** |
| Visible stair-step left/right edges across blocks | **Major** |
| Invented container width “to match design feel” | **Critical** |

**Authority:** [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md).

---

## PF-03 — Spacing fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| margin, padding, gap | OL-01 scale + SSOT spacing tokens |
| Section vertical spacing | [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |
| Percentage padding | OL-02 allowed set only — large inner containers |
| Grid/flex gaps | OL-01 gap scale |

**Spacing:** project-approved values are **authority** — expressed via SSOT tokens mapped to OL-01 unless project documents expanded scale.

### Acceptable variance

| Condition | Band |
|-----------|------|
| Value on OL-01 scale | PASS |
| SSOT token explicitly naming off-scale px (Lead-approved exception) | PASS WITH NOTES |
| Raw design 47px → mapped to 50px with C-12 mapping record | PASS |
| Browser rounding ±1px on computed gap | **Observation** |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Arbitrary px not on scale and not in SSOT (`17`, `23`, `37`, `13`, …) | **Major** |
| Per-block one-off spacing “matched in DevTools to screenshot” without SSOT update | **Major** |
| Percentage padding on small components or grid tracks | **Major** |
| Tightening whitespace for “cleaner look” | **Critical** (beautification drift) |

**Authority:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2 · OL-01.

---

## PF-04 — Layout fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| Hero column split | WF-LAYOUT-002 + named LP-* |
| Card grid column count | WF-LAYOUT-003 + SSOT C-11 |
| Trust / finance zones | WF-LAYOUT-004 / 005 |
| Responsive collapse order | WF-LAYOUT-006 + responsive intent doc |
| Grid track syntax | fr / minmax / repeat — not default `%` |

**Layout:** approved pattern is **authority** — not reinterpretation.

### Acceptable variance

| Condition | Band |
|-----------|------|
| Implemented LP-* matches SSOT C-11 binding | PASS |
| fr/minmax pair equivalent to approved pattern (documented) | PASS |
| `WF-LAYOUT-EXCEPTION` for `%` split with approver | PASS WITH NOTES |
| Collapse at SSOT breakpoint differs by ±0px breakpoint boundary only if handoff matches | PASS |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Default `%` tracks (`65% 35%`, `60% 40%`) without exception | **Major** |
| Layout assembled without WF-GRID → WF-LAYOUT → LP-* chain | **Critical** |
| FAQ 2-col grid with expanding answers (neighbor stretch) | **Major** |
| Different column count vs source without STRUCTURE CHANGE record | **Major** |
| “Balanced layout” change vs approved pattern | **Critical** |

**Authority:** [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) · [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md).

---

## PF-05 — Component fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| Control heights, radius tiers | SSOT C-03 / C-04 |
| Button variants (primary, secondary, outline) | SSOT + design source |
| Form field structure (label, input, error) | SSOT + mapping §5 |
| Card/chip/badge geometry | Design source + SSOT |
| Icon size and gap to label | SSOT / semantic iconography |

### Acceptable variance

| Condition | Band |
|-----------|------|
| Token match to SSOT | PASS |
| Component matches mapping schema (Purpose, Structure, Hierarchy, States) | PASS |
| Minor border-radius ±0px if SSOT tier exact | PASS |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Starter/demo component substituting for design component | **Major** |
| Missing required variant (e.g. no error state) | **Major** |
| Changed button height/radius per section without token | **Major** |
| “Simplified” component dropping design hierarchy | **Major** (intent drift) |

---

## PF-06 — Responsive fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| Breakpoints | Project SSOT + handoff — not ad-hoc |
| Layout collapse | WF-LAYOUT-006 + [responsive-intent-governance.md](responsive-intent-governance.md) |
| Overflow / horizontal scroll | None at required widths |
| RU commercial widths | [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) full set |
| Tap targets | Project a11y policy |

### Acceptable variance

| Condition | Band |
|-----------|------|
| All required widths PASS per preset / SSOT | PASS |
| Documented handoff supersedes Factory preset with REPORT note | PASS WITH NOTES |
| Intentional stack order change with STRUCTURE CHANGE + Lead ack | PASS WITH NOTES |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Horizontal scroll at any required width | **Critical** |
| RU preset not run for RU commercial landing | **Critical** (QA gap) |
| Invented breakpoint in section SCSS | **Major** |
| Desktop-only implementation claiming full responsive PASS | **Critical** |
| Overflow “fixed” with word-break forbidden on RU | **Critical** |

---

## PF-07 — Asset fidelity

### What to compare

| Element | Compare against |
|---------|-----------------|
| Logo version and clear space | Approved asset pack |
| Icons (SVG/FA) | Source + [semantic-iconography-governance.md](semantic-iconography-governance.md) |
| Photography / illustration crop and focal point | Design export |
| Favicon set | Project favicon sources |
| Image dimensions / aspect ratio | Source frame |

### Acceptable variance

| Condition | Band |
|-----------|------|
| Exact approved asset file used | PASS |
| Lead-approved substitute with same semantic role | PASS WITH NOTES |
| Web-optimized compression without visible artifact change | PASS |
| Retina `@2x` where project policy requires | PASS |

### Non-acceptable variance

| Condition | Severity |
|-----------|----------|
| Placeholder logo/icon/photo in production path | **Critical** |
| Wrong client brand logo (foreign mark from multi-brand source) | **Critical** — upstream: [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) |
| Wrong logo variant (color on wrong background) | **Major** |
| Distorted aspect ratio | **Major** |
| Missing favicon | **Minor** (unless charter requires — then Major) |
| Duplicating icons already baked into source raster | **Major** |

---

## Audit execution summary

### Per-audit minimum steps

1. Confirm **approved SSOT version** and design source set (with C-12 priority if mixed).
2. Run **PF-01 → PF-07** on scope (foundation demo or page slice).
3. Record variances with **severity** ([frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) §5).
4. Map PF results to **DQ domains** for matrix verdict.
5. Emit REPORT lines — do not claim PASS from chat summary alone.

### Recommended REPORT lines

```text
PIXEL FIDELITY AUDIT — PASS | PASS WITH NOTES | FAIL
PF-01 TYPOGRAPHY — PASS | FAIL (list)
PF-02 CONTAINER — PASS | FAIL (list)
PF-03 SPACING — PASS | FAIL (list)
PF-04 LAYOUT — PASS | FAIL (list)
PF-05 COMPONENTS — PASS | FAIL (list)
PF-06 RESPONSIVE — PASS | FAIL | SAFE UNKNOWN (widths)
PF-07 ASSETS — PASS | FAIL (list)
```

### Final rollup

| PF rollup | Matrix impact |
|-----------|---------------|
| All PF **PASS** | Supports **FRONTEND DESIGN QA MATRIX — PASS** |
| PF **PASS WITH NOTES** only (Minor/Observation/waived Major) | Supports **PASS WITH NOTES** |
| Any PF **FAIL** with Critical/Major unwaived | **FRONTEND DESIGN QA MATRIX — FAIL** |

---

## Relationship to visual reconciliation

| Layer | Question |
|-------|----------|
| **Pixel Fidelity Audit (this doc)** | “Do **numbers, tokens, patterns, and assets** match SSOT and layout law?” |
| **Visual reconciliation** | “Does the page **read** with correct emphasis, density, and intent?” |

Both may run on the same slice. PF-* **FAIL** on SSOT law blocks Production PASS even if reconciliation is subjective PASS. Reconciliation **FAIL** on business intent (DQ-11) blocks Production PASS even if PF-* numeric PASS.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Pixel Fidelity Audit Rules PF-01–PF-07; authority principles; acceptable vs non-acceptable variance; anti-aesthetic interpretation guardrails. |
| 2026-06-23 | FP-0002 V6: operator visual rejection overrides automated PASS; archived GROUP sources forbidden for structural reconstruction; clean audit required before re-implementation. |
