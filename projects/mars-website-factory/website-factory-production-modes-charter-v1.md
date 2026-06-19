# MARS Website Factory — Production Modes Charter v1

**Status:** **documented** — canonical Source of Truth for Website Factory **production modes**.  
**Not:** runtime flag, orchestration router, automated mode detector, or governance expansion.

**Version:** v1  
**Date:** 2026-06-17  
**Implementation pass:** WF-A01 — Production Modes Contract (Pass 01)

**Honesty boundary:** Production modes describe **human-operated fidelity contracts**. They do **not** imply in-repo automation unless a future charter explicitly implements tooling.

**Architecture basis:** [reports/website-factory-production-modes-architecture-v1.md](../../reports/website-factory-production-modes-architecture-v1.md) · [reports/website-factory-architecture-alignment-v1.md](../../reports/website-factory-architecture-alignment-v1.md) · [reports/FP-0002-STRESS-TEST-FORENSIC-v1.md](../../reports/FP-0002-STRESS-TEST-FORENSIC-v1.md)

---

## 1. Purpose

Website Factory delivers sites through **two primary production modes**. Each mode defines a different **Source of Truth**, creativity boundary, QA fork, and acceptance contract.

**Production mode** answers: *What fidelity contract binds this project?*

**Production mode is orthogonal to:**

| Dimension | Controls | Document |
|-----------|----------|----------|
| **Forge mode** (Lite / Standard / Critical) | Task risk, checklist depth, freeze posture | [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md) |
| **Operational modes** (Lite → Critical → Freeze-validation …) | Governance density, report compression | [operational-modes-model.md](operational-modes-model.md) |

Valid combinations: `PIXEL_PERFECT` + Forge Critical · `TEMPLATE_ART` + Forge Lite — **not** conflated vocabulary.

---

## 2. Canonical mode tokens

| Token | Working name | One-line contract |
|-------|--------------|-------------------|
| `PIXEL_PERFECT` | Pixel-perfect mode | Approved visual design is **SSOT**; frontend must **reproduce** layout, typography, spacing, assets, and copy fidelity — not reinterpret. |
| `TEMPLATE_ART` | Template-art mode | Requirements, IA, content, and block registry are **SSOT**; visual design is **produced** within Factory foundations — not extracted from FIG hash. |

**Forbidden global tokens:** `UNDECLARED`, `UNKNOWN`, `CONFLICT` — treated as **blocking** until resolved to `PIXEL_PERFECT` or `TEMPLATE_ART`.

**Hybrid scope:** per-page `page_mode_map` with **primary mode** in passport — not a third global enum (v1).

---

## 3. PIXEL_PERFECT

### 3.1 Definitions

**When:** Client supplies approved visual design (FIG, PNG, JPG, PDF, screenshot pack, or mixed design pack) and delivery contract requires **maximum visual reproduction fidelity**.

**Goal:** Exact reproduction of approved visual design.

**Generative fill:** **FORBIDDEN** — see §8.

### 3.2 Source Of Truth

| Rank | Authority | Role |
|------|-----------|------|
| **1** | **Approved visual design source** | Primary evidence for layout, composition, assets, copy |
| **2** | **Project Production Standards** (post-approval) | Numeric SSOT after Mapping QA + Standards Approval |
| **3** | **Layout Spec + Group Decomposition + Assembly Spec** (approved) | Composition chain before HTML |
| **4** | **section-NN.lock.json** (recommended machine SSOT) | Per-section text/image/order lock |
| **5** | Operator Laws + Factory precision (OL-*, WF-GRID, WF-LAYOUT) | Normalization only — **never** override approved design |

**Design source priority:** [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) — Figma → PNG/PDF → …

**Non-SSOT:** starter template aesthetics, agent aesthetic judgment, block library defaults without mapping record, generative paraphrase of missing copy.

### 3.3 Allowed inputs

| Category | Allowed | Notes |
|----------|---------|-------|
| Visual | Figma, PNG, JPG, PDF, WebP, screenshot pack, mixed design pack | Mandatory visual SSOT registration in Source Discovery |
| Structural | XLSX IA, briefs, sitemap, URL strategy | Governs IA/navigation — must not silently override visual order without ASSEMBLY DECISION |
| Content | Copy deck, legal micro-copy | May **supplement** FIG text when extract incomplete — triggers HITL, not auto-fill |
| Technical | Production Standards Draft, numeric rules, layout specs | Factory-generated from design |
| **Forbidden as silent substitute** | Block library hero «as default», invented card copy, first-image-as-logo heuristic | FP-0002 failure classes |

### 3.4 Creativity rules

| Area | Allowed | Forbidden |
|------|---------|-----------|
| Layout / spacing / type | **None** beyond documented OL-01 mapping | Beautification drift |
| Copy | **None** — lock FIG/copy-deck strings | Paraphrase, hallucinated reviews/cards |
| Assets | Select **only** from approved extract + brand detection chain | Positional heuristics without brand confirmation |
| Responsive | Per design exports; infer **only** with SAFE UNKNOWN + HITL | Invent alternate layouts |
| Interactions | Minimal stubs per charter or explicit KNOWN NON-GOALS | Fake functional forms/video without charter |
| Build staging | 2–3 sections per agent run | Full-page generative pass in one context |

**Creativity level:** **0 — reproduction only.**

### 3.5 QA rules

| Gate | Mandatory | Automation |
|------|-----------|------------|
| Production Mode declared in passport | Yes | Human |
| Source Discovery A0 | Yes | Human-operated |
| Design → Frontend Mapping QA | Yes | Human |
| Group Decomposition → Layout Spec → Assembly Spec | Yes | Human |
| Brand Asset Detection chain | Yes before logo wire | Documented; not in-repo engine |
| Design Calibration + Foundation QA | Yes (greenfield chain) | Human |
| Block-by-block operator approval | Yes | Human |
| Pixel Fidelity Audit (PF-*) | Yes | Human DevTools + side-by-side |
| Frontend Design QA Matrix | Yes | Human |
| Render Diff (FIG extract ↔ dist) | **Required for VERIFIED** | Manual or project-scripted |
| Text lock diff | Required per section | Human |
| Artifact lifecycle | **BUILT** ≠ **VERIFIED** — see [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §1.1 | Addresses FP-0002 FAIL-001 |

**QA router:** [operational-qa-entry-v1.md](operational-qa-entry-v1.md) § **Production Mode QA Router**.

**Forge mode:** typically **Standard** minimum for section slices; **Critical** for freeze/unfreeze, brand disputes.

### 3.6 Acceptance rules

Production slice/page may be declared **complete** only when **all** hold:

1. `production_mode: PIXEL_PERFECT` recorded in passport.
2. Visual SSOT locked and referenced in Production Standards Approval.
3. All mandatory gates **PASS** or **PASS WITH NOTES** per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md).
4. State is **VERIFIED** (mode-appropriate checklist + render/text diff) — not merely **BUILT**.
5. **OPERATOR VISUAL ACCEPT** recorded — TECHNICAL PASS ≠ approval.
6. No open Critical failure class: `ASSET_IDENTITY_COLLISION`, generative fill, false-green log.
7. Scoped KNOWN NON-GOALS documented if out of contract.

### 3.7 SAFE UNKNOWN (PIXEL_PERFECT)

| Situation | Required behavior |
|-----------|-------------------|
| No visual design source | **STOP** — reclassify to `TEMPLATE_ART` or park |
| Visual source partial (mobile missing) | Document scope; **UNKNOWN** on uncovered viewports; HITL before PASS |
| FIG text not machine-exportable | **UNKNOWN** + HITL — **forbid** generative fill |
| Pixel spacing/type not measured | PF gate **UNKNOWN** — not PASS |
| Assembly order conflict (bounds.y vs layer index) | **ASSEMBLY DECISION** record required — silent default forbidden |
| Render diff tooling absent | **SAFE UNKNOWN** on automated diff; mandatory human side-by-side |
| INSTANCE subtree invisible in flat extract | **STOP** section build until Group Register pass |

---

## 4. TEMPLATE_ART

### 4.1 Definitions

**When:** No approved pixel design; delivery driven by brief, SEO structure, blueprint, content deck, commercial requirements, wireframe/prototype, or blueprint-only charter.

**Goal:** Create the best design within requirements and Factory foundations.

**Generative fill:** **ALLOWED** within content contract and block registry bounds — not for logos/brand identity without brand chain.

### 4.2 Source Of Truth

| Rank | Authority | Role |
|------|-----------|------|
| **1** | **Intake + approved blueprint / page architecture** | IA, page list, URL logic, block requirements |
| **2** | **Content contract** (copy deck, approved texts) | Copy SSOT — not FIG extract |
| **3** | **Site Type Registry + Block Registry** | `site_type_id`, `block_id`, compatibility, quality tiers |
| **4** | **Foundation adoption + reference tokens** | [foundation-adoption-charter-v1.md](foundation-adoption-charter-v1.md) |
| **5** | Strategy / SEO artifacts | Messaging, keyword structure, CTA narrative |
| **6** | Wireframe / prototype (if present) | Structural intent — not pixel measurement |

**Non-SSOT:** FIG hash diff, pixel-perfect PF-* against nonexistent design export, starter demo copy as final content.

**Explicit non-goals:** FIG extract requirements, Render Diff against design, Group Decomposition for non-imported visuals (unless wireframe SSOT exists).

### 4.3 Allowed inputs

| Category | Allowed | Notes |
|----------|---------|-------|
| Requirements | ТЗ, brief, commercial requirements, compliance flags | Intake SSOT |
| Architecture | Sitemap, blueprint, page-block validation, SEO structure | Upstream of frontend |
| Content | Copy deck, product data, legal | Mandatory before page build |
| Visual direction | Mood boards, brand guidelines, token tables | Inform `_tokens.scss` — not pixel lock |
| Prototype | Low-fi wireframe, clickable prototype | Structure reference |
| Library | [curated-library-index-v1.md](curated-library-index-v1.md), reference-v1 blocks | **Provenance required** (`block_id`) |

### 4.4 Creativity rules

| Area | Allowed | Constraints |
|------|---------|-------------|
| Visual design | **High** within Factory foundations | Must respect `block_id`, quality tiers |
| Layout composition | Select LP-* patterns, registry blocks | No ad-hoc column math outside WF-GRID/WF-LAYOUT |
| Copy | Write from content contract + strategy | No lorem; no keyword stuffing |
| Imagery | Brand-appropriate assets, library art | Asset identity still applies for logos |
| Responsive | Factory breakpoint discipline | Foundation adoption patterns |
| New sections | Compose from registry + foundations | Extract-to-library optional post-delivery |

**Creativity level:** **High for design synthesis; low for architecture drift.**

### 4.5 QA rules

| Gate | Mandatory | Waived vs PIXEL_PERFECT |
|------|-----------|-------------------------|
| Production Mode declared in passport | Yes | Same |
| Source Discovery A0 | Yes (brief, content, brand — not FIG) | Same |
| Site Type + Blueprint QA | **Primary** | Stronger weight |
| Content contract completeness | Yes before page build | N/A in pixel |
| Foundation adoption validation | Yes | Same |
| Design → Frontend Mapping QA | **Reduced** — token/brand mapping | No full L-07 FIG extract |
| Pixel Fidelity Audit (PF-*) | **N/A** or brand/semantic only | Explicit waiver |
| Render Diff | **Waived** | Non-goal |
| Frontend Design QA Matrix | Yes — semantic, responsive, a11y | No FIG hash checks |
| `ru-landing-qa-preset-v1.md` | If RU commercial | Same |
| Block provenance audit | `block_id` traceable to registry | Template-art specific |

**Forge mode:** **Lite** viable for local token/section edits; **Standard** for new section from handoff.

### 4.6 Acceptance rules

1. `production_mode: TEMPLATE_ART` in passport.
2. Blueprint + content contract approved (HITL G1/G2 equivalent).
3. All pages trace to `site_type_id` + `block_id` set.
4. Foundation adoption QA **PASS**.
5. Frontend Design QA Matrix **PASS** / **PASS WITH NOTES** — PF-* marked **N/A** with charter reference.
6. No claim of pixel-perfect fidelity in REPORT or client comms.
7. OPERATOR VISUAL ACCEPT on brand/UX intent — not measurement diff.
8. **VERIFIED** = semantic + responsive + enforcement gates — not render diff.

### 4.7 SAFE UNKNOWN (TEMPLATE_ART)

| Situation | Required behavior |
|-----------|-------------------|
| Blueprint incomplete | **STOP** frontend page build |
| Content deck missing | **STOP** — no invented long-form copy at scale |
| Brand tokens undefined | **UNKNOWN** on color/type; HITL before freeze |
| Block not in registry | **STRUCTURE CHANGE** or registry update |
| Client later supplies FIG | **Mode transition** required — §7 |
| «Good enough» without operator sign-off | **STOP** — OPERATOR VISUAL ACCEPT mandatory |

---

## 5. Mode Selection Rules

### 5.1 Blocking gate

**Production Mode MUST be declared** before:

- `WF_V0_S10` frontend handoff
- LOC-ZONE passport finalize
- Any frontend production (HTML/SCSS), including scaffold and Production Standards Draft that assumes extract depth
- Path B step 4b greenfield chain ([onboarding-flow-v1.md](onboarding-flow-v1.md))

**If mode is absent or ambiguous:**

```text
production_mode ∈ { UNDECLARED, UNKNOWN, CONFLICT }
→ SAFE UNKNOWN
→ STOP
```

### 5.2 Gate matrix

| Lifecycle event | Mode action | If absent / ambiguous |
|-----------------|-------------|------------------------|
| **Новый проект** | **Mandatory declare** at `WF_V0_S01_INTAKE` | **STOP** — no frontend handoff, no passport finalize |
| **Новый production cycle** | **Confirm** mode still valid | **STOP** if charter contradicts passport without transition |
| **Новый frontend cycle** | **Read** passport mode; route QA | **STOP** — run intake gate retroactively |
| **Новый дизайн поверх старого проекта** | **Evaluate transition** | **STOP** until visual SSOT + transition approved |
| **Перезапуск проекта** | **Re-declare** mode | **STOP** — reconstruction until passport rewritten |
| **Unknown state** | Treat as **UNDECLARED** | **STOP** all frontend production |

### 5.3 Blocking surfaces

Frontend work **must not start** when:

```text
production_mode ∈ { UNDECLARED, UNKNOWN, CONFLICT }
OR
(PIXEL_PERFECT ∧ no visual SSOT registered in Source Discovery)
OR
(TEMPLATE_ART ∧ no approved blueprint/content path)
```

### 5.4 Minimum record at gate

| Field | Location |
|-------|----------|
| `production_mode` | `FP-XXXX-PROJECT-PASSPORT.md` |
| `mode_declared_at` | passport metadata |
| `mode_declared_by` | operator / coordinator ID |
| `mode_rationale` | 1–3 sentences + source evidence pointer |
| `mode_waivers` | optional — scoped PF N/A, interaction stubs |
| `mode_history[]` | passport — transition log |

**LOC-ZONE contract:** [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../../workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md)

### 5.5 Selection heuristics (operator)

| Evidence present | Typical mode |
|------------------|--------------|
| Approved FIG/PNG/PDF/screenshot pack + pixel delivery contract | `PIXEL_PERFECT` |
| Brief + blueprint + content deck; no approved pixel design | `TEMPLATE_ART` |
| Both design pack and blueprint-only path | Operator declares **primary mode** + `page_mode_map` if hybrid |
| Design pack exists but client waives pixel fidelity | **Mode transition** to `TEMPLATE_ART` with record — not silent downgrade |

---

## 6. Mode Transition Rules

### 6.1 Permitted transitions

| From | To | Permitted? | Typical trigger |
|------|-----|------------|-----------------|
| `TEMPLATE_ART` | `PIXEL_PERFECT` | **Yes** | Client delivers approved FIG/PDF |
| `PIXEL_PERFECT` | `TEMPLATE_ART` | **Yes, rare** | Design contract cancelled |
| Same → Same | — | **Yes** | Confirm only on new cycle |
| Hybrid scope | — | **Via primary mode + waiver** | Per-page `page_mode_map` |

### 6.2 Forbidden implicit transitions

- Running PF-* audit on template-art without transition record.
- Applying generative fill after pixel mode declared.
- Treating foundation adoption as pixel-perfect because «it looks similar».

### 6.3 Transition protocol

```text
1. Operator files MODE TRANSITION REQUEST in REPORT
2. HITL approves (coordinator + lead)
3. Update passport production_mode + mode_history[]
4. Re-run affected gates (mode-specific checklist)
5. Freeze impact assessment — may require Critical Forge mode
```

### 6.4 mode_history[] entry shape

```yaml
- from: PIXEL_PERFECT | TEMPLATE_ART
  to: PIXEL_PERFECT | TEMPLATE_ART
  at: ISO-8601 date
  by: operator ID
  rationale: string
  report_ref: path to MODE TRANSITION REPORT
  gates_rerun: [list of gate names]
```

---

## 7. Anti-Generative-Fill Policy (PIXEL_PERFECT)

**Authority:** FP-0002 FAIL-002, FAIL-003, FAIL-006, FAIL-008, FAIL-009, FAIL-014, FAIL-018.

When `production_mode: PIXEL_PERFECT`:

| Missing data | Forbidden | Required |
|--------------|-----------|----------|
| FIG/component text | Generate, paraphrase, invent copy | **SAFE UNKNOWN** or **STOP** + HITL |
| Review/card/article bodies | Generic filler paragraphs | Text lock from extract; Instance Resolver pass |
| Images from component instances | CSS placeholders, wrong hash reuse | Asset manifest binding; brand detection chain |
| Layout values | Agent «cleaner» spacing/type | Measure or **UNKNOWN** — PF gate blocks |
| Section order anomaly | Silent layer-index default | **ASSEMBLY DECISION** record |

**Rule:** Generative fill is a **mode violation** in `PIXEL_PERFECT`, not a style preference.

**Cross-ref:** [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) §0.4 · [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md).

---

## 8. QA Router (documentation contract)

Production mode selects **which QA path** applies. **No runtime router** — human operators and REPORT headers route per this charter.

| Router branch | Entry | Primary gates | VERIFIED means |
|---------------|-------|---------------|----------------|
| **PIXEL_PERFECT QA** | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | PF-*, Mapping QA, render/text diff, Operator Visual side-by-side | Mode checklist + diff evidence |
| **TEMPLATE_ART QA** | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Blueprint QA, content contract, semantic matrix, block provenance | Semantic + responsive chain; PF-* **N/A** |

**REPORT header (mandatory when production work):**

```text
Production mode: PIXEL_PERFECT | TEMPLATE_ART
Artifact lifecycle: BUILT | VERIFIED | (pending PRODUCTION PASS)
```

Detail: [operational-qa-entry-v1.md](operational-qa-entry-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §1.1.

---

## 9. Artifact lifecycle vocabulary

Three-level model — **distinct from gate verdict Layer A**:

| Term | Meaning | Typical evidence |
|------|---------|------------------|
| **BUILT** | Artifact created — compile succeeded | `npm run build` PASS; files exist in `dist/` |
| **VERIFIED** | Artifact checked per **mode** rules | PIXEL: diff + PF-*; TEMPLATE: semantic matrix + provenance |
| **PRODUCTION PASS** | Project/slice meets mode requirements after **VERIFIED** + operator sign-off | FINAL VERDICT block per reporting standard |

**Rule:** **BUILT** alone is **insufficient** for production claims (FP-0002 FAIL-001).

**Authority:** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §1.1.

---

## 10. Cross-surface representation

| Surface | Field / pointer |
|---------|-----------------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Production mode router row |
| [onboarding-flow-v1.md](onboarding-flow-v1.md) | Step 0 — mode before Path B |
| [website-factory-workflow-v0.md](website-factory-workflow-v0.md) | `WF_V0_S01` output: `production_mode` |
| [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md) | A0.5 mode branch |
| LOC-ZONE passport | `production_mode`, `mode_history[]` |
| MOC-01 / MOC-03 | `factory.production_mode` display when enrolled |
| REPORT header | `Production mode:` line |

---

## 11. Explicit non-goals (v1)

This charter does **not** authorize:

- Vision Layer, Visual Diff Layer, Pixel QA Runtime, Screenshot Engine, Agent Runtime — deferred to **WF-A03**
- Third global production mode enum
- Automated mode detection or enforcement engine
- Governance expansion beyond mode contract + passport fields

---

## 12. Related roadmap items

| ID | Name | Status |
|----|------|--------|
| **WF-A01** | Production Modes Contract | **This document** — Pass 01 complete |
| **WF-A02** | Validation Architecture | **Complete (Pass 01)** — [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** — see [roadmap.md](roadmap.md) |

**WF-A03 start condition:** WF-A01 **and** WF-A02 complete. **Not auto-started.** Before WF-A03: separate Web-GPT Research Pass required.

---

## 13. Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-17 |
| Runtime | **Not claimed** |
| Commit / push | Not performed by default |

---

*Canonical SoT for PIXEL_PERFECT and TEMPLATE_ART. Human-operated documentation only.*
