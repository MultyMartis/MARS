# REPORT — WEBSITE FACTORY ARCHITECTURE ALIGNMENT v1

**Date:** 2026-06-17  
**Scope:** Audit and design only — no implementation, no architecture changes, no document rewrites.  
**Evidence base:** Existing repository artifacts only (`projects/mars-website-factory/`, `workspaces/website-factory-reference-v1/`, `workspaces/website-factory-operations/`, `agents/`, `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md`, execution workspaces).  
**External reference:** AI Website Factory Research (user-provided summary) — compared, not imported as repo truth.

**Honesty boundary:** Website Factory in MARS is **documentation-first, human-operated methodology**. No in-repo Factory runtime, orchestration engine, or automated visual QA product is evidenced. Claims below distinguish **documented** vs **partially exercised in execution cases** vs **absent**.

---

## 1. Current State Map

### 1.1 What Website Factory is (proven from repo)

| Dimension | Location | Status |
|-----------|----------|--------|
| **Methodology pack** | `projects/mars-website-factory/` (~294 files) | **Operational documentation** — waves 1–6 + 2026-06 enforcement/QA packs |
| **Frozen reference architecture** | `workspaces/website-factory-reference-v1/` | **FROZEN FOUNDATION** — Registry → Blueprints → Block → SEO → Design → Content → Generation → Production QA → Runtime Architecture |
| **LOC-ZONE (records plane)** | `workspaces/website-factory-operations/` | **Operational** — manifests, passports, ROC catalog, FP-* project folders |
| **Navigation SoT** | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Tier-2 session router |
| **Workflow model** | `website-factory-workflow-v0.md` | 13 stages `WF_V0_S01` … `WF_V0_S13` — **documentation only** |
| **Layer vocabulary** | `layer-map.md` | 7 layers + Artifact Bus cross-cutting semantics |

**Explicit non-claims (repeated across pack):** not a runnable workflow engine, not autonomous agents, not CI validation product (`FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md`, `safe-unknown-boundary.md`, `governance/execution-model.md`).

### 1.2 Real layers (as documented + exercised)

```text
┌─────────────────────────────────────────────────────────────────┐
│ Supervisory (human + Control Plane design — no runtime)         │
├─────────────────────────────────────────────────────────────────┤
│ 1 Intake/Discovery    │ Source Discovery A0 (FP-0002-derived)   │
│ 2 Strategic           │ Marketing/SEO strategy (planned agents) │
│ 3 Page Architecture   │ IA + Blueprints + Block Registry        │
│ 4 Design              │ Implementation Pack, wireframes, FIG/PDF  │
│ 5 Production          │ Gulp static frontend (human + Cursor)     │
│ 6 QA / Validation     │ Human gates, matrices, enforcement pack   │
│ 7 Delivery            │ Workflow S13 + operator release discipline│
├─────────────────────────────────────────────────────────────────┤
│ Artifact Bus v0 — envelope/routing semantics (not transport)    │
└─────────────────────────────────────────────────────────────────┘
```

**Parallel frontend production chain** (greenfield, post–2026-06 packs — more detailed than WF v0 S11):

```text
A0 Source Discovery → Design Audit → Workspace → Production Standards Draft
  → DESIGN→FRONTEND MAPPING QA → Standards Approval → Shell → Visual Foundation
  → Design Calibration → Foundation QA → Page build (block-by-block)
  → Design Completeness → Frontend Design QA Matrix → Pixel Fidelity → Production PASS
```

Sources: `website-factory-source-discovery-v1.md`, `onboarding-flow-v1.md` Path B step 4b–4c, `frontend-shell-first-start-protocol-v1.md`.

### 1.3 Real agents (registry evidence)

| Agent | Status | Role |
|-------|--------|------|
| `gulp_frontend_agent` | **operational_doc_pack** | `agents/frontend-gulp-agent/` — HTML/SCSS/JS from handoff |
| `mars_forge_frontend_agent` | **operational_doc_pack** | Thin overlay on Gulp; Lite/Standard/Critical **operator** modes |
| Intake, Classifier, Marketing, SEO, IA, Blueprint, UX, Wireframe, AI Designer, Full Design, Design Governance | **planned** | Cards in `agents/cards/` |
| Frontend QA, Design QA, SEO QA, Conversion QA, Validator | **planned** | Cards only — no runtime |
| Design Governance Agent | **planned** | Pack authoring, not code |

**Not found as named concepts:** Pixel Factory, Frontend Factory.

### 1.4 Real workflows

| Workflow | Type | Evidence |
|----------|------|----------|
| WF v0 stage chain | Documented | `website-factory-workflow-v0.md` |
| Onboarding Path A/B/C | Documented | `onboarding-flow-v1.md` |
| Source Discovery A0→I | Documented | `website-factory-source-discovery-v1.md` |
| Operational QA entry | Documented | `operational-qa-entry-v1.md` |
| Visual regression (human screenshots) | Documented | `visual-regression-workflow-v1.md` |
| Forge operational modes | Documented | `forge-operational-modes-v1.md` (Lite default) |
| FP-0002 execution | **Human-operated case** | LOC-ZONE + `workspaces/fp-0002-shpigovsky-frontend/` |

### 1.5 Real registries

| Registry | Location | Maturity |
|----------|----------|----------|
| Site Type Registry v1 | `website-factory-reference-v1/registry/` | 8 types; Core 5 production-ready (docs) |
| Block Registry v1 | `block-registry/` | 29 `block_id` |
| Page Blueprint / validation | `page-architecture/`, `page-block-validation/` | Manual semantics |
| Site Type / Block v0 (pack) | `projects/mars-website-factory/site-type-registry-v0.md`, `block-registry-v0.md` | Workflow alignment |
| Execution cases | `execution-cases-registry-v1.md` | Triumph, ISBD, BZPM |
| Factory failure classes | `registries.md` §7 | e.g. `ASSET_IDENTITY_COLLISION` |
| ROC / FP catalog | `website-factory-operations/POC-02-registry-facet/` | FP-0001 enrolled; FP-0002 visibility-only |
| Agent registry | `agents/registry.md` | Contract only |

### 1.6 Real QA mechanisms (human-operated)

| Mechanism | Function | Automation |
|-----------|----------|------------|
| `operational-qa-entry-v1.md` | Default post-build QA surface | None |
| `frontend-design-qa-matrix-v1.md` | Design completeness + fidelity chain | None |
| `pixel-fidelity-audit-rules-v1.md` | PF-* human audit domains | None |
| `operator-visual-approval-law-v1.md` | TECHNICAL PASS ≠ OPERATOR APPROVAL | None |
| `website-factory-enforcement-pack-v1.md` | ROOT COMPLIANCE, compiled CSS, inline style | None |
| `frontend-compliance-decision-model-v1.md` | RAW VIOLATION → gate verdict | None |
| `frontend-failure-attribution-model-v1.md` | Post-escape investigation | None |
| `visual-reconciliation-layer.md` | Hierarchy/composition human read | Explicitly not CV |
| `production-qa/` (reference-v1) | Architecture integrity before frontend | Not browser testing |
| `governance/P0-VISUAL-GATES-v1.md` | Cross-program technical vs visual PASS | Human |
| FP-0002 forensic | Post-build stress test | Ad-hoc scripts + human review |

### 1.7 Real execution loci (not Factory engine)

| Workspace | Role |
|-----------|------|
| `workspaces/fp-0002-shpigovsky-frontend/` | FP-0002 Gulp build — FIG-driven stress test |
| `workspaces/triumph-manipulator-landing-v6/` | Active client reference |
| `workspaces/website-factory-reference-v1/src/` | Golden blocks + foundations |
| `workspaces/_template-client-v1/` | Client bootstrap template |

---

## 2. Industry Comparison

Comparison is **architectural posture**, not feature parity. External systems optimize for **speed of generation**; MARS Website Factory optimizes for **governance, gates, and honesty boundaries**.

| System | Overlap with MARS WF | Divergence | Implication |
|--------|----------------------|------------|-------------|
| **Builder** (Webflow, Framer, etc.) | Page/block vocabulary; design→publish intent | Builders ship **hosted runtime + WYSIWYG**; MARS targets **static Gulp export** with human Cursor execution | WF is methodology around external build repos, not a hosted builder |
| **v0** | Component/section generation from prompts | v0 is **generative UI** with implicit template aesthetic; WF forbids silent generative fill (FP-0002 lessons) | WF anti-pattern: inventing copy when extract incomplete |
| **Replit Agent** | End-to-end project scaffolding | Replit owns **runtime + deploy**; WF explicitly **excludes** autonomous deploy pipeline in-repo | WF needs explicit handoff to hosting (SAFE UNKNOWN per project) |
| **Cursor** | Primary execution surface for Gulp agent | Cursor is **IDE agent**, not a factory schema; WF adds **stage gates, registries, REPORT law** | Strength: disciplined human-in-loop; weakness: no native FIG diff in Cursor |
| **Claude Code** | Multi-file coherent edits | Same as Cursor — tool, not factory ontology | WF value is **what to verify**, not **how to type code** |
| **LangGraph / agent graphs** | Stage chain, handoff contracts map to graph nodes | WF documents workflow **without** graph runtime, state store, or checkpoint API | Planned alignment to Control Plane — **not implemented** |

### Strong sides (MARS architecture)

1. **Acceptance gate culture** — Operator Visual Approval Law, Production PASS vs TECHNICAL PASS, compliance decision model.
2. **Failure taxonomy from real incidents** — FP-0002 promoted to factory-wide classes (`ASSET_IDENTITY_COLLISION`, group decomposition law).
3. **Honesty boundaries** — Consistent "documentation only / not runtime" labeling reduces mythology drift.
4. **Dual-plane architecture** — Doctrine (`reference-v1`) vs records (`website-factory-operations` LOC-ZONE).
5. **Block registry + site types** — Upstream architecture gates before frontend (rare in pure codegen tools).

### Weak sides (vs industry research emphasis)

1. **Validation underweighted in automation** — Rich QA docs, minimal executable verification (FP-0002: build PASS while 12 PARTIAL + 2 FAIL).
2. **No production-mode fork** — Industry research mandates explicit Pixel-perfect vs Template-art pipelines; WF has neither named mode nor intake gate.
3. **Generative gap** — Industry tools ship fast prototypes; WF slow path is intentional but **without** compensating automated diff layers.
4. **Agent roster mostly planned** — Specialist QA agents exist as cards, not operational packs.
5. **FIG→HTML chain immature** — FP-0002 forensic scores: Component Extraction 38, Text 42, Pixel Fidelity 34 (inferred).

---

## 3. Pixel-perfect Mode Assessment

### 3.1 Is Pixel-perfect mode present today?

**Verdict: PARTIAL — as governance practice and client-workspace AGENTS.md workflow, NOT as an explicit Factory production mode.**

| Signal | Present? | Evidence |
|--------|----------|----------|
| Named `pixel-perfect mode` / `PRODUCTION_MODE=PIXEL` | **No** | Repo search: no production pipeline mode token |
| Pixel fidelity audit (human) | **Yes** | `pixel-fidelity-audit-rules-v1.md` |
| Visual reconciliation (human) | **Yes** | `visual-reconciliation-layer.md` |
| Block-by-block approval (gulp client copies) | **Yes** | `workspaces/*/AGENTS.md` pixel-perfect sections |
| FIG numeric rules / layout spec | **Yes** | `layout-spec-law-v1.md`, `FP-0002-NUMERIC-DESIGN-RULES-v2.md` |
| Automated pixel diff / vision | **No** | Explicitly disclaimed across pack |
| Mandatory mode selection at project intake | **No** | See §5 |

**Contradiction with industry research:** Research says Factory must not start production without mode selection. Current WF can start greenfield via `onboarding-flow-v1.md` Path B without declaring pixel-perfect vs template-art — only Forge Lite/Standard/Critical for **task risk**, not **delivery fidelity contract**.

### 3.2 Where Pixel-perfect mode should live (design only)

| Layer | Proposed home | Documents that would be required (not created in this task) |
|-------|---------------|-------------------------------------------------------------|
| **Intake gate** | `WF_V0_S01` + Source Discovery A0 | `PRODUCTION-MODE-CHARTER-v1.md` — binds project to pipeline |
| **LOC-ZONE passport** | `FP-XXXX-PROJECT-PASSPORT.md` template | Field: `production_mode: PIXEL_PERFECT \| TEMPLATE_ART` |
| **Doctrine** | `website-factory-reference-v1/generation-contracts/` | Mode-specific generation gate matrix |
| **Operations** | `OPERATIONAL-INDEX.md` Core Run row | Mode router before frontend packs |
| **QA** | `operational-qa-entry-v1.md` | Mode-specific checklist fork |

### 3.3 Systems touched by explicit Pixel-perfect mode

- Source Discovery (FIG/PNG/PDF as SSOT — mandatory)
- Design→Frontend Mapping QA
- Group Decomposition → Layout Spec → Assembly Spec chain
- Brand Asset Detection Layer (`failures/asset-identity-collision-v1.md`)
- Pixel Fidelity Audit (PF-*)
- Visual regression workflow (baseline screenshots)
- Block-by-block HITL (existing gulp AGENTS.md pattern)
- **Future:** FIG extract ↔ dist diff scripts (recommended by FP-0002, absent today)

---

## 4. Template-art Mode Assessment

### 4.1 Is Template-art mode present today?

**Verdict: IMPLICIT PARTIAL — block-library / template adoption path exists; NOT named or gated as a separate production pipeline.**

| Signal | Present? | Evidence |
|--------|----------|----------|
| Named `template-art mode` | **No** | Not in repo |
| Curated block library | **Yes** | `curated-library-index-v1.md`, reference-v1 blocks |
| `_template-client-v1` bootstrap | **Yes** | Wave 4–5 onboarding |
| Site type → block palette defaults | **Yes** | Site Type Registry, Block Registry |
| "Reused template art" as risk | **Yes** | `asset-identity-collision-v1.md` — wrong brand from multi-brand FIG |
| Generative section fill from blocks | **Partial** | Triumph extracts; not a formal template-art charter |

**What exists instead:** **Foundation adoption** path — copy reference foundations, swap tokens, add hero from library. This is **closer to template-art** than to FIG pixel-perfect, but operators are not asked to choose it explicitly at intake.

### 4.2 Where Template-art mode should live (design only)

Same intake/router surfaces as §3.2, with:

- Relaxed pixel fidelity charter (semantic + responsive QA primary)
- Mandatory block provenance (`block_id` from registry)
- Explicit **non-goals** for FIG hash diff
- Stronger **content contract** gates (copy deck as SSOT, not FIG text extract)

### 4.3 Systems touched

- Block Registry + quality tiers (`block-quality-tiers-v1.md`)
- Foundation adoption charter/rules
- Section swap / replacement contract
- SEO + blueprint stages (more weight than visual extract)
- Weaker: Group Decomposition, Layout Spec, Brand Asset Detection (still needed for logos)

---

## 5. FP-0002 Findings Mapping

Forensic source: `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md` (2026-06-17). Composite grade ~49/100.

### 5.1 Instance Resolver Layer

| Question | Answer |
|----------|--------|
| **Analog today?** | **Partial** — `group-decomposition-law-v1.md` (GROUP-IDs); FP-0002 `FIG-AUTO-GROUP-REGISTER-TEST`; flat TEXT extract in build scripts |
| **What exists** | Discovery names INSTANCE types (`Врач`, `отзыв`, `Статья`); Group Register test artifacts in REPORTS |
| **What is absent** | Operational **Instance Resolver** that walks INSTANCE subtrees before generation; FAIL-006, FAIL-008, FAIL-014 root cause |
| **Gap** | Flat extract → generic cards; no gate blocking build when instance count ≠ HTML card count |

### 5.2 Asset Identity Layer

| Question | Answer |
|----------|--------|
| **Analog today?** | **Partial** — `failures/asset-identity-collision-v1.md` + Brand Asset Detection Layer (§7 chain) |
| **What exists** | Forbidden `FIRST IMAGE = LOGO`; hash grouping procedure; FP-0002 logo fix documented |
| **What is absent** | Automated hash dedup registry; frame-export pollution fix (FAIL-004 `d3ac7d00`); asset manifest `section → nodeId → src` |
| **Gap** | 56% orphan exports (FAIL-005); collision hash across 10+ sections |

### 5.3 Visual Y Ordering Layer

| Question | Answer |
|----------|--------|
| **Analog today?** | **Absent as layer** — anomaly **documented** only |
| **What exists** | FAIL-007 in forensic; Discovery flags SECTION-10 `y=2389` anomaly |
| **What is absent** | Assembly rule: `bounds.y` primary, layer index fallback, explicit ASSEMBLY DECISION record |
| **Gap** | Silent default to layer index → visual order drift |

### 5.4 Frontend QA Layer

| Question | Answer |
|----------|--------|
| **Analog today?** | **Partial** — extensive human QA governance; **false-green** demonstrated |
| **What exists** | `frontend-design-qa-matrix-v1.md`, `pixel-fidelity-audit-rules-v1.md`, `operator-visual-approval-law-v1.md`, `frontend-qa-reporting-standard-v1.md` |
| **What is absent** | `frontend_qa_agent` runtime; mandatory pre-PASS FIG/text checklist; distinction `BUILT` vs `VERIFIED` (FAIL-001, FAIL-018) |
| **Gap** | Agent self-attestation; gulp PASS without content verification |

### 5.5 Render Diff Layer

| Question | Answer |
|----------|--------|
| **Analog today?** | **Absent** |
| **What exists** | Human visual regression workflow; visual reconciliation methodology; FP-0002 recommends FIG diff gate |
| **What is absent** | Automated `fig_extract ↔ dist` comparison; screenshot diff tooling (Percy/Chromatic class) |
| **Gap** | No machine-readable verification stage in pipeline |

### 5.6 FP-0002 → Industry research crosswalk

| FP-0002 finding | Research theme |
|-----------------|----------------|
| Instance Extraction (FAIL-006) | Component Detection + Structure Extraction |
| Asset Mapping (FAIL-004, FAIL-005, FAIL-017) | Asset Identity Layer |
| Section Ordering (FAIL-007) | Visual Y Ordering / Layout Measurement |
| Fake Green QA (FAIL-001, FAIL-018) | Pixel QA + Acceptance Gates |

---

## 6. Missing Layers (research vs repo)

| Layer | Status | Repo closest artifact | Gap |
|-------|--------|----------------------|-----|
| **Vision Layer** | **partial** | `visual-reconciliation-layer.md` | Human hierarchy read; no CV/vision model |
| **Layout Measurement Layer** | **partial** | `layout-spec-law-v1.md`, numeric design rules, WF-GRID | No instrumental measure-from-FIG; manual specs |
| **Component Detection Layer** | **partial** | `group-decomposition-law-v1.md`, FP-0002 forensic scripts | Not productized; no CI gate |
| **Structure Extraction Layer** | **partial** | `website-factory-source-discovery-v1.md`, FIG discovery JSON | Ad-hoc per project; flat TEXT insufficient |
| **Screenshot Layer** | **partial** | `visual-regression-workflow-v1.md` | Human capture discipline only |
| **Visual Diff Layer** | **absent** (automation) | Human side-by-side in visual-regression | No diff engine; disclaimed in visual-reconciliation |
| **Pixel QA Layer** | **partial** | `pixel-fidelity-audit-rules-v1.md` | Human PF-* audit; no automated pixel gate |

**Additional gaps (FP-0002 derived, not in research list):**

| Layer | Status |
|-------|--------|
| Instance Resolver | **absent** (partial decomposition law only) |
| Asset Identity Registry | **partial** (failure class documented) |
| Visual Y Ordering | **absent** |
| Render Diff (FIG↔HTML) | **absent** |
| Text Lock / anti-paraphrase gate | **absent** |
| Production Mode Router | **absent** |

---

## 7. Required Architectural Changes

**Design recommendations only — not implemented.**

### 7.1 P0 — Mode fork (industry alignment)

Introduce **explicit Production Mode** at intake:

```text
INTAKE → PRODUCTION MODE SELECTION (blocking gate)
           ├─ PIXEL_PERFECT  → full extract + diff + block-by-block + PF audit
           └─ TEMPLATE_ART   → registry blocks + content SSOT + relaxed pixel charter
```

**Minimal artifact set (future):**

1. `PRODUCTION-MODE-CHARTER-v1.md` — definitions, non-goals, QA fork
2. Passport field on all FP-* projects
3. `onboarding-flow-v1.md` step 0 — mode before Path B step 4b
4. QA entry router in `operational-qa-entry-v1.md`

### 7.2 P0 — Verification vocabulary

Split build outcomes:

| Term | Meaning |
|------|---------|
| `BUILT` | Gulp compile succeeded |
| `VERIFIED` | Mode-appropriate diff/checklist passed |
| `PRODUCTION PASS` | Human operator sign-off only after VERIFIED |

Addresses FAIL-001 false-green.

### 7.3 P1 — Pixel-perfect pipeline documentation chain

Without building automation, **document** ordered layers for PIXEL_PERFECT mode:

```text
Source Discovery → FIG/PNG SSOT lock
  → Structure Extraction (section inventory)
  → Component Detection (INSTANCE register)
  → Layout Measurement (bounds.y order + layout spec)
  → Asset Identity (brand detection chain)
  → Build (staged 2–3 sections/run)
  → Screenshot baseline
  → Render Diff (manual or scripted — project declares tooling)
  → Pixel QA (PF-*) → Operator Visual Approval
```

Map each step to existing docs where possible; mark **NEW DOC NEEDED** only where no analog exists.

### 7.4 P1 — Template-art pipeline documentation chain

```text
Site Type + Block selection → Foundation adoption
  → Content contract SSOT → Blueprint QA
  → Section implementation from library
  → Semantic + responsive QA (skip FIG hash diff)
  → Operator approval
```

### 7.5 P2 — Agent operationalization

Promote `frontend_qa_agent` from planned card to **operational_doc_pack** with mode-specific checklists — still human-operated, but routable.

### 7.6 Contradictions to resolve

| Current state | Industry best practice | Resolution direction |
|---------------|------------------------|----------------------|
| Single frontend path implied | Two pipelines | Mode charter |
| Pixel-perfect claimed in client AGENTS.md but disclaimed in Factory pack | Consistent vocabulary | Mode-scoped claims only |
| Forge Lite/Standard/Critical = task risk | Production mode = fidelity contract | Orthogonal dimensions: `production_mode` × `forge_mode` |
| Generative fill on missing extract (FP-0002) | Hard-fail + HITL | Text lock + UNKNOWN policy in pixel mode |

---

## 8. Risks

| Risk | Severity | Evidence |
|------|----------|----------|
| **False-green production** | **Critical** | FP-0002: 15/15 build PASS vs 1 PASS / 12 PARTIAL / 2 FAIL forensic |
| **Wrong production path** | **High** | No mode gate — pixel project may run template-art shortcuts |
| **Brand asset collision** | **Critical** | FP-0002 Skinerica logo incident; class documented, gate not automated |
| **Governance fatigue** | **Medium** | Large pack surface; operators may skip Tier 3 until incident |
| **Context truncation at scale** | **High** | FP-0002 memory analysis: 15 sections = HIGH token risk; 45+ = not viable in one run |
| **Doctrine vs operations drift** | **Medium** | reference-v1 frozen vs fast-moving 2026-06 enforcement packs |
| **Planned agent mythology** | **Medium** | 20+ planned agents in cards — easy to assume they exist |
| **No render diff** | **High** | Ship content drift undetected until forensic audit |

---

## 9. SAFE UNKNOWN

| Item | Unknown | What would verify |
|------|---------|-------------------|
| Automated visual diff tooling adoption | Whether team will adopt Percy/Chromatic/Playwright snapshot or custom FIG diff | Explicit project charter + CI config in workspace |
| FP-0002 ROC enrollment | Deferred per 2026-06 awareness pass | `website-factory-operations` ROC catalog update |
| Control Plane runtime | Mapping in workflow v0 only | Implementation in repo outside current evidence |
| Pixel fidelity scores without measurement | FP-0002 score 34 inferred | Instrumented spacing/type diff tool |
| INSTANCE text inside FIG symbols | Partially invisible in flat extract | Enhanced parser walk of symbol trees |
| External "AI Website Factory Research" full text | Only user summary provided | Attach full research doc to repo if canonical |
| Hosting/deploy pipeline per project | SAFE UNKNOWN in workflow S13+ | Per-project deploy runbook |
| Whether OCPilot SITE-001 path equals WF mode | Parallel compliance audits exist | Crosswalk doc SITE-001 ↔ production mode |

---

## 10. Recommended Roadmap

### Phase 0 — Alignment (documentation design, no runtime)

1. Author **Production Mode Charter** (pixel vs template-art definitions, blocking intake gate).
2. Add mode router pointers to OPERATIONAL-INDEX + onboarding-flow.
3. Define `BUILT` / `VERIFIED` / `PRODUCTION PASS` vocabulary in `frontend-qa-reporting-standard-v1.md` (future edit).
4. Crosswalk existing packs to mode columns (what applies to which mode).

### Phase 1 — Pixel-perfect discipline (human + optional scripts)

1. Promote FP-0002 lessons to **ordered layer checklist** for PIXEL_PERFECT projects.
2. Standardize `section-NN.lock.json` SSOT pattern (FP-0002 recommendation #7).
3. Staged build charters (max 2–3 sections per agent run).
4. Assembly order policy (`bounds.y` vs layer index).
5. Project-local FIG diff script template (optional tooling — not Factory runtime).

### Phase 2 — Template-art discipline

1. Template-art charter linked to block registry + foundation adoption.
2. Content SSOT gate before page build.
3. Explicit waiver of FIG extract requirements.

### Phase 3 — QA agent pack

1. `frontend_qa_agent` operational_doc_pack with mode-specific matrices.
2. Integrate failure attribution tokens for each missing layer.

### Phase 4 — Automation (only if chartered)

1. Render diff layer (project-scoped CI).
2. Asset identity hash registry tooling.
3. Instance resolver in FIG parse pipeline.

**Explicitly out of scope until human charter:** Factory engine runtime, LangGraph orchestration, autonomous deploy.

---

## Priority A — mandatory

1. **Production Mode Selection gate at intake** — pixel-perfect vs template-art; block all greenfield frontend until declared.
2. **BUILT vs VERIFIED vs PRODUCTION PASS** — end false-green (FP-0002 FAIL-001).
3. **Mode-specific QA router** — fork `operational-qa-entry-v1` logic by production mode.
4. **Anti-generative-fill policy for PIXEL_PERFECT** — missing text → UNKNOWN + HITL, not paraphrase (FP-0002 FAIL-002, FAIL-003).
5. **Brand Asset Detection Gate** — enforce documented chain before logo wire (existing failure class).

## Priority B — desirable

1. **Layer checklist for PIXEL_PERFECT** — map research layers to existing docs + gaps.
2. **Visual Y ordering / assembly decision record** — policy for FIG anomalies.
3. **Staged section build charters** — context survivability (FP-0002 §6).
4. **section-NN.lock.json SSOT** — machine-readable per-section contract.
5. **frontend_qa_agent operational_doc_pack** — mode-aware checklists.
6. **Template-art charter** — block library path with explicit non-goals.

## Priority C — defer

1. Automated vision / CV layer.
2. Factory engine runtime / LangGraph implementation.
3. Percy/Chromatic-class SaaS integration (unless project charters).
4. Pixel Factory / Frontend Factory as separate product names.
5. Full agent roster implementation (marketing, wireframe, AI designer cards).
6. ROC enrollment automation for FP-* projects.

---

## Appendix A — Document index (audit scope)

Key artifacts consulted:

- `projects/mars-website-factory/OPERATIONAL-INDEX.md`
- `projects/mars-website-factory/layer-map.md`
- `projects/mars-website-factory/website-factory-workflow-v0.md`
- `projects/mars-website-factory/onboarding-flow-v1.md`
- `projects/mars-website-factory/website-factory-source-discovery-v1.md`
- `projects/mars-website-factory/visual-reconciliation-layer.md`
- `projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md`
- `projects/mars-website-factory/visual-regression-workflow-v1.md`
- `projects/mars-website-factory/group-decomposition-law-v1.md`
- `projects/mars-website-factory/failures/asset-identity-collision-v1.md`
- `projects/mars-website-factory/operational-modes-model.md`
- `agents/mars-forge/forge-operational-modes-v1.md`
- `agents/frontend-gulp-agent/`, `agents/registry.md`
- `workspaces/website-factory-reference-v1/ARCHITECTURE-FOUNDATION-v1.md`
- `workspaces/website-factory-operations/README.md`
- `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md`
- `workspaces/fp-0002-shpigovsky-frontend/` (execution case)

**Terms not found in repo:** Pixel Factory, Frontend Factory, template-art mode, vision layer (as product name), Instance Resolver Layer, Render Diff Layer, Visual Y Ordering Layer.

---

*End of report — audit and design only. No implementation.*
