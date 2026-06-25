# MARS Website Factory — Design Source → Frontend Mapping Governance v1

**Status:** **documented** — Foundation-level **canonical mapping law** for converting **any** approved design source into frontend implementation inputs.  
**Not:** runtime extractor, Figma plugin, computer vision, automated pixel diff, CI gate, or project-specific token values.

**Purpose:** Fix the **mandatory chain** from design evidence to production HTML/CSS — independent of source format. This document governs **what must be extracted**, **how values transfer**, **what is forbidden**, and **when work must STOP** on SAFE UNKNOWN.

**Scope:** All Website Factory frontend surfaces (Gulp static, OpenCart, WordPress, corporate, landing, catalog, PDP, homepage) when implementation is driven by design evidence.

**Supported source types (non-exhaustive parity):**

| Type | Notes |
|------|-------|
| **Figma** | Preferred when available — frames, components, variables, export specs |
| **PDF** | Static artboards; measure from vector/raster layers |
| **PNG** | Raster export; watch compression and crop artifacts |
| **JPG** | Same as PNG — lower fidelity for fine type/spacing |
| **WebP** | Same as PNG — verify color profile |
| **Screenshot Pack** | Ordered viewport captures; may be only source |
| **Mixed Sources** | e.g. Figma desktop + PNG mobile + PDF legal micro-copy — requires explicit **source priority** in Production Decisions |

**This is not a Figma-only document.** Figma is **priority 1** when present; all rules apply to raster and mixed packs equally.

**Authority order (canonical):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)

**Production mode:** Full extract chain is **mandatory** when passport `production_mode: PIXEL_PERFECT` — [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md). **Reduced** mapping depth permitted for `TEMPLATE_ART` with charter waiver.

| Rank | Layer | Role in mapping |
|------|-------|-----------------|
| **1** | Project Production Standards | **Wins** — per-project SSOT after approval |
| **2** | Approved Operator Laws (OL-01–OL-07) | Spacing normalization, layout pattern first, typography precision |
| **3** | **This doc** + related Factory governance | Mapping chain, extraction layers, drift prohibitions, QA gate |
| **4** | Layout Pattern Library (LP-* / WF zones) | Named patterns — no ad-hoc column math |
| **5–6** | Industry Best Practice · Agent Preference | **Never** override ranks 1–4 |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Project instances (read-only):** FP-0002 v3, SITE-001 governance artefacts — **do not edit** for Factory evolution.

**Related (integration — not duplication):**

| Document | Role |
|----------|------|
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Canonical 6-layer hierarchy + OL-01–OL-07 |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Draft + Approval stage; C-01–C-16 categories receive mapped values |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Spacing/type normalization detail under OL-01, OL-05 |
| [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Container Layer — mandatory grid contract |
| [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | Layout Layer — inner-zone splits |
| [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | LP-* selection before HTML |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Verifies **implementation** vs approved standards — not re-mapping |
| [source-interpretation-governance.md](source-interpretation-governance.md) | Observed / Inferred / Assumed / Unknown read discipline |
| [design-intent-transfer-governance.md](design-intent-transfer-governance.md) | Intent fidelity, hierarchy, reconstruction traceability |
| [beautification-drift-governance.md](beautification-drift-governance.md) | Aesthetic overreach taxonomy |
| [responsive-intent-governance.md](responsive-intent-governance.md) | Breakpoint and collapse intent when source is partial |

---

## 1. Purpose and scope

### 1.1 What this document governs

| In scope | Out of scope |
|----------|--------------|
| Mandatory **extraction layers** from any design source | Autonomous design reading or CV extraction |
| **Pixel transfer rules** for typography and spacing | Forge overlay semantics (see Forge checklists) |
| **Layout transfer chain** — Design Source → WF-GRID → WF-LAYOUT → Layout Pattern → HTML | Canonical Design Implementation Pack authorship (see [design-governance-layer.md](design-governance-layer.md)) |
| **Component transfer** minimum extraction schema | Block-level HTML/SCSS implementation |
| **Design reconstruction drift** prohibitions | Runtime validation products |
| **Missing design data** — UNKNOWN-first protocol | Project-specific px/hex values |
| **DESIGN → FRONTEND MAPPING QA** gate | Foundation QA full checklist (peer gate) |

### 1.2 When mapping applies

Mapping **must** complete (or explicit SAFE UNKNOWN with HITL) **before** Production Standards Approval and **before** any Shell HTML/SCSS work. **Layout Spec** (composition decomposition) is **mandatory before** Shell/block HTML per [layout-spec-law-v1.md](layout-spec-law-v1.md) — Mapping QA does **not** substitute for Layout Spec.

```text
Approved design source(s)
        ↓
Source interpretation (peer: source-interpretation-governance)
        ↓
Layer extraction (this doc §2)
        ↓
Normalization + layout chain (this doc §3–§5)
        ↓
Production Standards Draft (production-standards-governance C-01–C-16)
        ↓
DESIGN → FRONTEND MAPPING QA (this doc §8)
        ↓
Production Standards Approval
        ↓
Layout Spec (per block) → Operator APPROVED — [layout-spec-law-v1.md](layout-spec-law-v1.md)
        ↓
Shell → Visual Foundation → Design Calibration → Foundation QA
        ↓
Home Production → Design Completeness → Frontend Design QA Matrix → Pixel Fidelity → Production PASS
```

**Foundation QA authority:** [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md). **Page QA chain:** [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) §11–12.

### 1.3 Honesty boundary

This document is **human-operated governance**. It does **not** claim an in-repo mapping engine, linter, or automated gate unless a future project explicitly adopts checklists as tooling.

---

## 2. Source Authority Model

### 2.1 Principle

**Design source is evidence — not production law.** After Production Standards Approval, **Project Production Standards (rank 1)** supersede raw source numbers for implementation. Mapping produces the **draft SSOT**, not ad-hoc HTML.

### 2.2 Source priority (default)

When **Mixed Sources** conflict, resolve in Production Decisions (C-12) using this default order unless project charter states otherwise:

| Priority | Source class |
|----------|--------------|
| **S1** | Active Figma file / linked frame (named version) |
| **S2** | Signed PDF or coordinator numeric rules |
| **S3** | Highest-resolution PNG/WebP export per viewport |
| **S4** | JPG / lower-fidelity raster |
| **S5** | Screenshot pack (unordered) |
| **S6** | Prior implementation, archive, chat memory |

**Forbidden:** Treating archive, mockup folder, or agent memory as S1 without authority promotion.

### 2.3 Required extracted layers

Every mapping pass **must** attempt extraction into **all eight layers**. Silent omission is drift.

| Layer ID | Layer | Maps to Production Standards | Extraction minimum |
|----------|-------|------------------------------|-------------------|
| **L-01** | **Layout** | C-11, C-07 | Page regions, section order, container width signals, column structure, full-bleed vs inset, breakpoint artboards |
| **L-02** | **Typography** | C-02 | Font family, size, weight, line-height, letter-spacing (note: non-zero letter-spacing → OL-06 / project exception), heading tiers |
| **L-03** | **Spacing** | C-04, C-05 | Section gaps, internal padding, grid gaps, rhythm between repeated units |
| **L-04** | **Colors** | C-03 | Background, text, border, accent, state colors — hex or named role |
| **L-05** | **Components** | C-08 | Buttons, inputs, cards, nav, tables — at pattern/token level |
| **L-06** | **States** | C-10 | Default, hover, focus, active, disabled, open/closed — **only if present or explicitly UNKNOWN** |
| **L-07** | **Assets** | C-09 | Logos, icons, photos, favicon, font files — path or export reference |
| **L-08** | **Content** | Semantics / handoff | Copy, headings, CTA labels, entity counts — content authority, not invented filler |

### 2.4 Layer read classification

Each extracted value carries a read class (aligns with [source-interpretation-governance.md](source-interpretation-governance.md)):

| Class | Mapping posture |
|-------|-----------------|
| **Observed** | Record source path + measurement; map normally |
| **Inferred** | Record inference rule; map with confidence label |
| **Assumed** | **Avoid** — if used, Production Decisions + approximation disclosure |
| **UNKNOWN** | **SAFE UNKNOWN** register (C-14) — **no production guess** |

### 2.5 Layer completeness rule

Draft is **not ready** for DESIGN → FRONTEND MAPPING QA if any L-01–L-08 row is **blank without TBD + policy**. See [production-standards-governance-v1.md](production-standards-governance-v1.md) §3.4.

---

## 3. Pixel Transfer Rules

### 3.1 Typography — 1:1 transfer default

| Rule | Behavior |
|------|----------|
| **Transfer 1:1** | Observed font-size, weight, and line-height from source **enter the type table as measured values first** — before normalization |
| **No arbitrary resizing** | Agents **must not** change type sizes for “balance,” “cleaner look,” or “better hierarchy” without rank 1–2 authority |
| **Normalization boundary** | Line-height defaults to OL-05 (`font-size + 4px`) **only** when project SSOT adopts Factory default — record each row in Production Decisions if source line-height differed |
| **px in CSS** | Production UI type uses **px** unless project SSOT documents rem exception ([frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3) |
| **Forbidden drift** | Arbitrary line-heights, unitless ratios, or heading shrink/grow without source or SSOT |

**Authority on conflict:** Project Production Standards **win** over OL-05 for named tiers. OL-05 wins over Agent Preference.

### 3.2 Spacing — normalization only through Approved Operator Laws

| Rule | Behavior |
|------|----------|
| **Measure first** | Record raw px from source in mapping worksheet |
| **Normalize second** | Map to OL-01 gap scale and margin/padding scale ([frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §3 OL-01) |
| **Nearest approved value** | Round **toward** scale — never invent intermediate values “for better look” ([frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §1) |
| **Percentage padding** | OL-02 only — large volumetric containers; not grid splits |
| **Project override** | Lead-approved tokens in rank 1 SSOT supersede nearest-scale mapping — cite decision ID |
| **Forbidden** | Silent rounding to unstated px; spacing changes for aesthetic judgment |

### 3.3 Colors and radius

| Rule | Behavior |
|------|----------|
| **Extract hex or role** | Map to C-03 / C-06 named tokens |
| **No per-block invention** | Factory does not invent hex per section during mapping |
| **Raster caveat** | PNG/JPG/WebP color pick subject to compression — mark **Inferred** when uncertain |

### 3.4 Assets

| Rule | Behavior |
|------|----------|
| **Real assets only** | No placeholder logos/icons in mapping output unless project policy explicitly allows TBD |
| **Provenance** | Each L-07 row cites export path or Figma node |
| **Missing asset** | UNKNOWN + blocker classification — not SVG/CSS fake substitute without HITL |
| **Brand identity** | **Forbidden:** `FIRST IMAGE = LOGO` heuristic — see [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md); run Brand Asset Detection Layer when multi-candidate signals present |

---

## 4. Layout Transfer Rules

### 4.1 Mandatory chain (non-negotiable)

**Direct Design → HTML is forbidden.**

```text
Design Source
        ↓
   WF-GRID          ← Container Layer (section ≠ container, page grid contract)
        ↓
   WF-LAYOUT        ← Layout Layer (hero split, card grid, trust, finance, collapse)
        ↓
 Layout Pattern     ← LP-* ID or documented WF zone model (OL-03)
        ↓
      HTML           ← Shell/partials only after above layers are named in C-11
```

| Step | Authority | Failure if skipped |
|------|-----------|-------------------|
| **Design Source** | S1–S6 priority §2.2 | Unresolved layout read |
| **WF-GRID** | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Section/container conflation; rhythm breaks |
| **WF-LAYOUT** | [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | Ad-hoc `%` splits; zone drift |
| **Layout Pattern** | [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) · OL-03 · OL-04 | Eyeball column math |
| **HTML** | [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Premature markup before SSOT freeze |

### 4.2 WF-GRID mapping obligations

From design source, extract and name in C-11:

- `--container-max` (or project equivalent)
- `--container-pad` / padding-inline tiers
- Section vs full-bleed background ownership
- One page = one grid contract (WF-GRID-002)

### 4.3 WF-LAYOUT mapping obligations

From design source, extract and name in C-11:

- Hero split model (fr pair — not default `%` per WF-LAYOUT-002)
- Card grid column count at desktop
- Trust / finance zone splits where present
- Responsive collapse intent **or** UNKNOWN (§7)

### 4.4 Layout Pattern selection

Before HTML:

1. Match observed structure to **LP-* pattern** or documented WF zone type.
2. Record pattern ID in Production Standards C-11.
3. If no pattern fits → **STOP** — extend pattern library or HITL; do not invent `%` tracks.

---

## 5. Component Transfer Rules

### 5.1 Required extraction schema

Each distinct UI component **pattern** in source (not every instance) requires a mapping row with:

| Field | Required content |
|-------|------------------|
| **Purpose** | What job the component performs (CTA, proof, nav, filter, etc.) |
| **Structure** | DOM-level skeleton — regions, not final class names |
| **Hierarchy** | Primary / secondary / decorative within the component |
| **States** | Default + interaction states **present in source** — or UNKNOWN |
| **Content** | Copy roles, counts, limits — tied to content authority |

### 5.2 Component mapping rules

| Rule | Behavior |
|------|----------|
| **Pattern level** | Map to C-08 tokens — button heights, border radius tiers, input height |
| **No hallucinated structure** | Tabs, sliders, accordions not in source → **STOP** or UNKNOWN |
| **State honesty** | Hover absent in source → **do not invent hover styling** for mapping SSOT unless C-10 documents Factory default with Lead ack |
| **Reuse** | Prefer existing LP / block registry patterns before new component taxonomy |

### 5.3 Cross-ref

Semantic and intent fidelity beyond structure → [design-intent-transfer-governance.md](design-intent-transfer-governance.md).  
Interaction defaults when source silent → [interaction-intent-governance.md](interaction-intent-governance.md) + C-10.

---

## 6. Design Reconstruction Drift Rules

### 6.1 Explicit prohibition

The following justifications are **forbidden** as mapping or implementation rationale **unless** supported by **Project Production Standards (rank 1)** or **Approved Operator Laws (rank 2)** with documented decision:

| Forbidden rationale | Why |
|---------------------|-----|
| **"Looks cleaner"** | Aesthetic judgment replaces source authority |
| **"Looks modern"** | Trend substitution — see [beautification-drift-governance.md](beautification-drift-governance.md) |
| **"Looks better"** | Unbounded agent preference — rank 6 |

### 6.2 Permitted improvement paths

| Permitted when | Requirement |
|----------------|-------------|
| **Project Production Standards** | Lead-approved token or pattern explicitly differs from source — record in C-12 |
| **Approved Operator Laws** | e.g. OL-01 nearest spacing, OL-04 fr instead of `%` — record raw → production in C-12 |
| **Named Factory exception** | WF-LAYOUT-007 percentage exception + Lead ack |

### 6.3 Drift reporting

When mapping detects pressure toward forbidden rationale → log in Production Decisions or Forge **`BEAUTIFICATION DRIFT FINDINGS`** / **`RECONSTRUCTION FIDELITY FINDINGS`** as applicable — do not hide as “normalization.”

---

## 7. Missing Design Data Protocol

### 7.1 UNKNOWN-first

**Default posture:** If source does not decide a matter → **SAFE UNKNOWN** — **no guessing**.

Hidden ambiguity is more dangerous than visible uncertainty ([source-interpretation-governance.md](source-interpretation-governance.md) §3).

### 7.2 Common missing-data cases

| Missing data | Required response | Forbidden |
|--------------|-------------------|-----------|
| **Mobile absent** | C-14 UNKNOWN; responsive collapse **not specified** in C-07 until HITL or mobile source arrives | Invent mobile layout from desktop |
| **Tablet absent** | Same — mark breakpoint gap | Assume tablet = scaled desktop |
| **Hover absent** | C-10: state UNKNOWN or document Factory focus/hover parity **policy** with Lead ack | Invent hover visual from taste |
| **Active absent** | C-10 UNKNOWN for pressed/active | Copy hover as active without source |
| **Focus absent** | C-10: accessibility intent via [accessibility-intent-governance.md](accessibility-intent-governance.md) — **not** fake source state | Skip focus entirely |
| **Component state absent** | L-06 UNKNOWN per component | Full state matrix from agent habit |
| **Asset absent** | L-07 blocker or TBD policy | Placeholder logo/icon in mapping SSOT |
| **Copy absent** | Content UNKNOWN — coordinate content lane | Lorem or AI filler in mapping |
| **Copy absent (PIXEL_PERFECT)** | **STOP** or HITL — **forbid** generative fill per [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) §7 · FP-0002 | Paraphrase, invented review/card bodies |

### 7.3 Escalation

| Impact | Action |
|--------|--------|
| **Blocker** | Shell **NOT READY** — resolve or waive with HITL before Approval |
| **Non-blocker** | Document in C-13 Open Questions; may Approval with explicit waiver |
| **Responsive blocker** | See [responsive-intent-governance.md](responsive-intent-governance.md) — desktop-only mapping cannot claim full responsive PASS |

### 7.4 VERIFY-BY plan

Every C-14 row must include **what evidence would resolve UNKNOWN** (e.g. “Figma frame `Home / Mobile 390`” or “client PDF v2”).

---

## 8. Mapping QA Gate — DESIGN → FRONTEND MAPPING QA

### 8.1 Gate definition

**DESIGN → FRONTEND MAPPING QA** is a **mandatory human-operated gate** between **Production Standards Draft complete** and **Production Standards Approval PASS**.

**Not:** Design Calibration (that gate verifies **implementation** on Foundation Demo Page).  
**Not:** Foundation QA (downstream formal gate).

### 8.2 Entry criteria

| ID | Criterion |
|----|-----------|
| IN-M01 | Active design source set identified with S1–S6 priority |
| IN-M02 | Production Standards Draft covers C-01–C-16 (or explicit TBD + policy) |
| IN-M03 | All eight layers L-01–L-08 attempted |
| IN-M04 | Layout chain §4 documented in C-11 (WF-GRID + WF-LAYOUT + LP-*) |
| IN-M05 | Production Decisions (C-12) lists raw → normalized mappings |

### 8.3 Verification checklist

Verify **mapping quality** — not code:

| Check | Pass condition |
|-------|----------------|
| **Typography** | Type table cites source measurements; no arbitrary resize; OL-05 / project exceptions documented |
| **Spacing** | Raw → OL-01 scale mapping recorded; no unstated px |
| **Layout** | WF-GRID + WF-LAYOUT + LP-* named; **no** Design → HTML shortcut |
| **Components** | Each pattern has Purpose, Structure, Hierarchy, States, Content |
| **States** | Present states mapped; absent states UNKNOWN — not invented |
| **Assets** | L-07 complete or blocker flagged; no unapproved placeholders |

### 8.4 Exit artifacts

| ID | Output |
|----|--------|
| OUT-M01 | **Mapping QA RECORD** — inline in Approval REPORT or standalone `# REPORT — <project> design mapping QA` |
| OUT-M02 | **Layer coverage matrix** — L-01–L-08 × Observed / Inferred / UNKNOWN |
| OUT-M03 | **Layout chain diagram** — source → WF-GRID → WF-LAYOUT → LP-* |
| OUT-M04 | **Lead acknowledgment** — `DESIGN → FRONTEND MAPPING QA — PASS \| partial \| FAIL` |

**Recommended REPORT line:**

```text
DESIGN → FRONTEND MAPPING QA — PASS | partial (list) | FAIL
LAYER COVERAGE (L-01–L-08) — PASS | partial (list) | FAIL
LAYOUT CHAIN (WF-GRID → WF-LAYOUT → LP-*) — PASS | FAIL
RECONSTRUCTION DRIFT CHECK — PASS | FINDINGS (list) | FAIL
```

### 8.5 Gate outcomes

| Verdict | Meaning |
|---------|---------|
| **PASS** | Approval may proceed — SSOT mapping complete |
| **partial** | Written exception list + Lead ack; blockers must not include Shell-critical UNKNOWN without waiver |
| **FAIL** | Return to Draft — **no Approval**, **no Shell** |

### 8.6 Relationship to downstream QA

| Gate | Verifies |
|------|----------|
| **DESIGN → FRONTEND MAPPING QA** (this doc) | Source → Draft SSOT mapping |
| **Design Calibration** | Implemented tokens vs **approved** SSOT |
| **Foundation QA** | Shell + foundation demo + discipline lines — [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) |
| **Design Completeness · Matrix · PF · Production PASS** | Page/slice closure — [frontend-design-completeness-governance-v1.md](frontend-design-completeness-governance-v1.md) · [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5.2–§6 |

---

## 9. Authority integration summary

```text
Rank 1  Project Production Standards     ← output of mapping + Approval
Rank 2  Approved Operator Laws           ← spacing, layout pattern, type precision
Rank 3  This doc + precision + standards process
Rank 4  Layout Pattern Library
        WF-GRID / WF-LAYOUT              ← mandatory layout chain intermediates
Rank 5–6 Advisory / Forbidden override
```

| Peer document | Integration point |
|---------------|-------------------|
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Draft receives mapped values; Mapping QA before Approval |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | §3–§3.2 normalization detail |
| [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | §4.2 Container Layer |
| [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | §4.3 Layout Layer |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Post-implementation; does not replace Mapping QA |
| [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) | Conflict resolution §2 |

---

## 10. Agent / operator behavior

| Situation | Required response |
|-----------|-------------------|
| Only PNG desktop, no mobile | Mark C-07 + L-01 responsive UNKNOWN — **no mobile mapping guess** |
| Source gap 64px | Map to **70px** (OL-01) — record in C-12 |
| Agent skips WF-GRID, writes hero HTML | **STOP** — §4 forbidden chain violation |
| “Let's modernize the buttons” | **STOP** — §6 forbidden unless rank 1–2 |
| Figma + PDF disagree on H1 size | Production Decisions — S1 vs S2 priority §2.2 |
| Mapping QA FAIL | **No Approval** — fix Draft |

**REPORT expectation:** Cite `Authority: design-source-to-frontend-mapping-governance-v1 §N` plus rank 1–2 doc when resolving mapping conflicts.

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Foundation-level design source → frontend mapping governance; eight extraction layers; layout chain; Mapping QA gate; multi-source support; drift prohibitions; UNKNOWN-first protocol. |
| 2026-06-24 | §12 — Figma inspection authority cross-ref (visible content, hidden layers, layer-name conflict, audit contract). |

---

## 12. Figma inspection authority (when Figma is design source)

When **Figma** is an approved design source, mapping and extraction **must** also satisfy [figma-inspection-authority-rules-v1.md](figma-inspection-authority-rules-v1.md):

| Token | Requirement |
|-------|-------------|
| **FIGMA-VISIBLE-CONTENT-AUTHORITY** | Visible rendered content beats layer / component names |
| **FIGMA-INSTANCE-OVERRIDE-PRIORITY** | Instance overrides beat master defaults and names |
| **FIGMA-LAYER-NAME-CONFLICT** | Record `LAYER_NAME_CONTENT_CONFLICT` when name ≠ visible content |
| **FIGMA-HIDDEN-LAYER-EXCLUSION** | Hidden / opacity-0 / parent-hidden nodes excluded — `EXCLUDED_BY_VISIBILITY` |

**Forge:** [`../../agents/mars-forge/figma-inspection-checklist.md`](../../agents/mars-forge/figma-inspection-checklist.md).

Figma audits without visibility inheritance checks are **incomplete** for Mapping QA sign-off.
