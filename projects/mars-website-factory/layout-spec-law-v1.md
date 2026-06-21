# MARS Website Factory — Layout Spec Law v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** law for Website Factory frontend visual implementation.  
**Not:** runtime orchestration, automated layout parser, Figma plugin, CI gate, or policy engine.

**Version:** v1  
**Date:** 2026-06-14

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules)

**Provenance:** FP-0002 Shpigovsky.ru — header composition failure (2026-06-14). Agent received Visual SSOT but implemented Header from internal interpretation; result radically unlike design. **Not** a PDF, Figma, or format failure — a **missing mandatory artifact** failure.

**Peer authorities (detail — do not duplicate here):**

| Document | Role |
|----------|------|
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Token/spacing extraction — **does not** replace Layout Spec |
| [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | Named LP-* patterns — selected **after** Layout Spec defines zones |
| [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) | Operator gate **after** HTML/CSS — Layout Spec gate is **before** code |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Shell-first order — Clean Shell (Phase 0.5) then Layout Spec **before** Phase 1 shell HTML |
| [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) | Mandatory empty shell — NOT STARTED markers only until Layout Spec |
| [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) | Phase C–F integration |
| [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) | Failure class **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** |
| [FP-0002-layout-spec-lesson-v1.md](FP-0002-layout-spec-lesson-v1.md) | Instance lesson — read-only provenance |
| [FP-0002-clean-shell-lesson-v1.md](FP-0002-clean-shell-lesson-v1.md) | Instance lesson — beautiful starter vs empty shell |
| [group-decomposition-law-v1.md](group-decomposition-law-v1.md) | **Group Decomposition Gate** — discrete GROUP-IDs per ROW **before** Layout Spec |
| [FP-0002-group-decomposition-lesson-v1.md](FP-0002-group-decomposition-lesson-v1.md) | Instance lesson — CONTACT BLOCK aggregation in JPG test |

**Honesty boundary:** This law is **documentation discipline**. It does **not** claim an in-repo Layout Spec linter or automated gate unless a project explicitly adopts checklists as tooling.

---

## 1. Purpose

Close the **composition gap** between approved **Visual SSOT** and **HTML/CSS implementation**.

Factory governance already requires Design Audit, Production Standards, Mapping QA, shell-first order, and operator visual approval **after** implementation. None of these **mandate a written layout decomposition** that locks **zone order, row structure, grouping logic, and container model** before an agent writes markup.

**Without Layout Spec**, agents default to:

```text
Visual SSOT → "I understood the design" → HTML/CSS
```

That path is **forbidden**.

**Required path:**

```text
Visual SSOT → Layout Spec → Operator APPROVED → HTML/CSS
```

---

## 2. Definitions

| Term | Definition |
|------|------------|
| **Visual SSOT** | Any **operator-approved** visual source of truth for a block, shell zone, or page — format irrelevant; approval status matters. |
| **Layout Spec** | A **written, block-scoped** decomposition artifact that describes **composition structure** (zones, rows, grouping, hierarchy, container model) derived from Visual SSOT — **without** implementing HTML/CSS. |
| **Layout Spec Gate** | Mandatory stop: Layout Spec filed → operator decision **APPROVED** or **REVISE** → only **APPROVED** unlocks HTML/CSS for that scope. |
| **Block scope** | One Layout Spec per implementable unit: Header, Footer, Hero, section block, or full page shell composition — not one mega-doc for the whole site unless operator waives per-block split. |

### 2.1 Visual SSOT — accepted formats

Visual SSOT may be any **approved** visual source, including but not limited to:

- Figma (frames, components, exports)
- PDF
- PNG · JPG · WebP
- Sketch · Adobe XD
- HTML prototype
- Approved screenshot pack
- Any other operator-designated visual source

**Rule:** Format does **not** determine validity. **Operator approval** of the source as SSOT for the scoped work determines validity.

**Rule:** Layout Spec Law does **not** blame PDF vs Figma vs PNG. Failures from skipping Layout Spec are **composition failures**, not **source-format failures**.

---

## 3. LAYOUT SPEC LAW (normative)

### 3.1 Forbidden without Layout Spec

It is **forbidden** to start **HTML/CSS implementation** (markup, SCSS, layout partials) for:

| Scope | Examples |
|-------|----------|
| **Shell** | Header, Footer, sticky bar, mobile shell chrome |
| **Page blocks** | Hero, FAQ, CTA, catalog grid, any section partial |
| **Full pages** | Home, inner pages, landing slices |
| **Any visual block** | Including “small” or “obvious” blocks |

until **all** of the following exist for that scope:

1. **Layout Spec** document filed (project REPORT path or `<PROJECT>-LAYOUT-SPEC-<block-id>-vN.md`)
2. **Operator decision** recorded: **APPROVED**
3. Visual SSOT reference cited in Layout Spec

### 3.2 What Layout Spec is not

| Artifact | Why it does not substitute |
|----------|----------------------------|
| **Design Audit** | Inventory, gaps, block list — not per-block composition |
| **Production Standards** | Tokens, radius, typography law — not zone layout |
| **DESIGN → FRONTEND MAPPING QA** | Numeric/token extraction — not structural decomposition |
| **Header content audit / mini-audit** | Element presence list — not row/zone composition model |
| **Layout Pattern Library pick alone** | LP-* name without zone spec still allows agent fantasy |
| **Agent verbal summary** | “I see two rows” in chat — **not** a Layout Spec |
| **HTML/CSS draft** | Implementation is **downstream**, never upstream proof of understanding |

### 3.3 Agent behavior

| Situation | Required response |
|-----------|-------------------|
| Operator or task requests Header/Footer/block HTML | **STOP** if Layout Spec missing or not **APPROVED** |
| Visual SSOT received; agent “understands” layout | Write Layout Spec first; **do not** code |
| Layout Spec **REVISE** | Fix spec only; **do not** patch HTML to compensate |
| Multiple blocks in one task | **One Layout Spec per block**; one approval cycle per block unless operator bundles scope in writing |

---

## 4. Layout Spec — minimum mandatory content

Layout Spec must be **detailed enough that another agent**, seeing **only** the Layout Spec (+ cited Visual SSOT reference), can assemble composition **close to the design** without inventing structure.

**Not required:** pixel-perfect measurements, exhaustive token tables, or duplicating Production Standards.

**Required:** structural truth the agent must not reinterpret.

### 4.1 Universal fields (every Layout Spec)

| # | Field | Content |
|---|-------|---------|
| L-01 | **Block ID / scope** | e.g. `BLK-001+002 Header`, `Footer`, `Hero PG-001` |
| L-02 | **Visual SSOT reference** | SOURCE-ID, file name, frame/page, viewport |
| L-03 | **Viewport** | e.g. desktop ≥1024px — Phase C default |
| L-04 | **Visual zones** | Named zones top-to-bottom (or reading order) |
| L-05 | **Zone order** | Strict sequence; no reordering without REVISE |
| L-06 | **Row count** | How many horizontal bands / rows in the block |
| L-07 | **Row composition** | What each row contains — groups left-to-right |
| L-08 | **Grouping logic** | Which elements share a visual group; flex/grid intent at prose level |
| L-09 | **Visual hierarchy** | Primary vs secondary vs utility; what dominates visually |
| L-10 | **Container model** | Full-bleed vs contained; which zones use page container; WF-GRID alignment |
| L-11 | **Block boundaries** | What is **inside** this block vs **outside** (e.g. breadcrumb below header, not in header) |
| L-12 | **Merged vs separate** | What must stay **one** block vs what must **not** be merged |
| L-13 | **Frozen decisions** | What agent **must not change** (labels, row split, nav count, CTA placement) |
| L-14 | **SAFE UNKNOWN** | Composition gaps — must not be silently invented in HTML |
| L-15 | **Layout Pattern reference** | LP-* / WF zone if applicable — or explicit “no named pattern” |

### 4.2 Header example (illustrative — FP-0002 class)

For a dual-row commercial header, Layout Spec must state at minimum:

| Dimension | Example content (structure only) |
|-----------|----------------------------------|
| **Zones** | Zone A: utility top bar · Zone B: main nav row |
| **Order** | A above B; both inside `<header>` shell |
| **Rows** | **2 rows** — not single-row collapse on desktop |
| **Row A composition** | Left group: region links · Center/right: hours · Right group: utility links + phones |
| **Row B composition** | Left: logo + brand text stack · Center: primary nav (N items, named) · Right: CTA button |
| **Grouping** | Phones grouped with top bar right; nav items single horizontal group; logo+tagline one group |
| **Hierarchy** | Row B nav + CTA dominant; Row A utility secondary |
| **Container** | Both rows share same inner container width; section full-bleed background if design shows |
| **Boundaries** | Breadcrumb / page title trail **below** header — **not** part of header Layout Spec |
| **Frozen** | Dual-row structure; 5 nav labels; 2 phone numbers; CTA label; no hamburger on desktop Phase C |
| **UNKNOWN** | Exact px heights, sticky behavior — record; do not invent structure to fill gaps |

---

## 5. OPERATOR GATE (mandatory)

After Layout Spec is written, the agent **must stop**. **No HTML/CSS** for that scope.

### 5.1 Agent obligation

1. File Layout Spec at agreed project path
2. Present Layout Spec to operator (summary + link/path)
3. Request explicit decision
4. **Wait**

**Required request text (Russian or English equivalent):**

```text
Layout Spec готов для <scope>.
Проверьте декомпозицию против Visual SSOT.
Требуется решение: APPROVED или REVISE.
Верстка запрещена до APPROVED.
```

### 5.2 Operator decisions

| Decision | Meaning | HTML/CSS |
|----------|---------|----------|
| **APPROVED** | Composition decomposition accepted | **Permitted** for approved scope only |
| **REVISE** | Composition wrong or incomplete | **Forbidden** — revise Layout Spec; re-submit |

**Rule:** **APPROVED** on Layout Spec is **not** Operator Visual Acceptance of implemented HTML. Implementation still requires [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) after build.

**Rule:** Technical PASS, Mapping QA PASS, Design Audit complete — **none** substitute for Layout Spec **APPROVED**.

---

## 6. Workflow placement

```text
Visual SSOT (approved)
        ↓
Group Decomposition (per block) — [group-decomposition-law-v1.md](group-decomposition-law-v1.md)
        ↓
Design Audit / Production Standards / Mapping QA  (peer gates — unchanged)
        ↓
Layout Spec (per block)
        ↓
OPERATOR GATE — APPROVED | REVISE
        ↓
HTML/CSS implementation
        ↓
Build → Technical QA → Operator Visual Review
```

**Shell-first:** Layout Spec for **Header** and **Footer** before Phase C HTML — see [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md).

**Page production:** Layout Spec per block before Phase F slice — see [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md).

---

## 7. FAILURE CLASS — VISUAL INTERPRETATION WITHOUT LAYOUT SPEC

| Field | Value |
|-------|-------|
| **Class ID** | `VISUAL INTERPRETATION WITHOUT LAYOUT SPEC` |
| **Definition** | Agent implemented HTML/CSS from Visual SSOT using **internal composition interpretation** without a filed, operator-**APPROVED** Layout Spec for that scope. |
| **FP-0002 instance** | Header radically unlike design; agent skipped decomposition; error found only at operator screenshot compare |
| **Expected capture point** | **Layout Spec Gate** — before first line of Header/Footer/block HTML |
| **Why prior gates missed it** | Design Audit = inventory; Mapping QA = tokens; shell-first = order not composition; Operator Visual Law = post-implementation; Pixel Fidelity = post-implementation |
| **Failure cause token** | **LAYOUT SPEC SKIPPED** — see [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) |
| **Attribution** | **Layout Spec Gate** (agent/operator pair — operator if APPROVED spec that was wrong) |

---

## 8. Reporting

When Layout Spec is filed or gated, REPORT must include:

```text
LAYOUT SPEC — <block-id> — DRAFT | APPROVED | REVISE
LAYOUT SPEC GATE — PASS (APPROVED) | FAIL (REVISE pending) | FAIL (SKIPPED)
VISUAL SSOT REF — <SOURCE-ID or path>
```

Implementation REPORT for the same block must cite:

```text
LAYOUT SPEC REF — <path> — APPROVED <date>
```

**Forbidden:** `LAYOUT SPEC GATE — PASS` when decision is still pending.

---

## 9. Scope

**Applies to:** All Website Factory greenfield frontend — shell (Header, Footer), Visual Foundation demo layout if non-trivial, and every production block/page slice.

**Factory-wide mandatory:** **Yes** — unless project charter documents explicit dated exception with Lead signature.

**Does not modify:** FP-0002 workspace artefacts, frontend source code, Production Standards numeric SSOT, Enforcement Pack logic.

---

## 10. Changelog

| Date | Change |
|------|--------|
| 2026-06-14 | v1 — Layout Spec Law promotion from FP-0002 header failure; canonical Factory authority. |
| 2026-06-14 | v1.1 — Pointer to [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) — Clean Shell precedes Layout Spec. |
| 2026-06-15 | v1.2 — Pointer to [group-decomposition-law-v1.md](group-decomposition-law-v1.md) — Group Decomposition precedes Layout Spec. |
