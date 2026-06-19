# Website Factory — Validation Architecture Charter v1

**Status:** **documented** — canonical SoT for Validation Layers, Flow, Signals, Evidence, and Lifecycle Boundaries.  
**Not:** validator runtime, CI pipeline, visual diff SaaS, orchestration engine, or automated enforcement product.

**Date:** 2026-06-17  
**Implementation pass:** WF-A02 — Pass 01 + Pass 02 (VL3 Domains)  
**Authority chain:** [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) (WF-A01) · [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) (WF-A02 Pass 02) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) · [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md)

**Evidence base:** [reports/website-factory-validation-architecture-audit-v1.md](../reports/website-factory-validation-architecture-audit-v1.md) · [reports/website-factory-validation-architecture-design-v1.md](../reports/website-factory-validation-architecture-design-v1.md) · [reports/FP-0002-STRESS-TEST-FORENSIC-v1.md](../reports/FP-0002-STRESS-TEST-FORENSIC-v1.md)

**Honesty boundary:** Validation Architecture is **human-operated documentation**. Project-local scripts may satisfy evidence classes; Factory does **not** claim global automation in WF-A02.

---

## 1. Purpose

This charter is the **single canonical source of truth** for:

| Domain | Definition location |
|--------|---------------------|
| Validation Layers (VL0–VL6) | §3 |
| VL3 Domains (VL3a–VL3f) | [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) |
| Validation Flow | §6 |
| Validation Signals | §4 |
| Validation Evidence | §5 |
| Lifecycle Boundaries (BUILT / VERIFIED / PRODUCTION PASS) | §5, §6 |
| False-Green Closure | §7 |
| Production Mode Integration | §8 |

**Validation Architecture does not replace** existing gate documents — it **orders and connects** them into a blocking, evidence-backed chain.

**Explicit non-goals (WF-A02):** Validator Runtime · Frontend QA Runtime · Vision Runtime · Screenshot Engine · Render Diff Engine · Pixel Factory · WF-A03 automation layers.

---

## 2. Architectural planes (orthogonal)

```text
PLANE 1 — VALIDATION LAYERS (VL0–VL6)     WHAT / WHEN / blocking order
PLANE 2 — REPORTING LAYERS (A–F)          HOW results are recorded
PLANE 3 — PRODUCTION MODE                 WHICH gates apply (PIXEL_PERFECT | TEMPLATE_ART)
PLANE 4 — ORTHOGONAL RISK                 Forge mode · Exception Registry · operational modes
```

**Rule:** Reporting Layer A **PASS** ≠ lifecycle **VERIFIED**. Layer F lifecycle states attach to VL4/VL5/VL6 boundaries only.

**Default entry:** [operational-qa-entry-v1.md](operational-qa-entry-v1.md) — Production Mode QA Router + pointer to this charter.

---

## 3. Validation Layer Registry (VL0–VL6)

### VL0 — Intake & Mode

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Confirm project is declared, production mode is known, sources are inventoried — before any frontend production work. |
| **Inputs** | LOC-ZONE passport; Source Discovery intake; charter mode rules; onboarding step 0 record. |
| **Outputs** | `INTAKE_VALIDATED` state; mode branch selection; A0 inventory register; REPORT header `Production mode:` line. |
| **Exit criteria** | `production_mode ∈ { PIXEL_PERFECT, TEMPLATE_ART }`; Critical sources READ or scoped; mode ↔ source alignment documented; passport fields per [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../../workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md). |
| **Lifecycle boundary** | Prerequisite for VL1 — **no lifecycle state claim** at VL0. |
| **Failure signals** | **STOP** — `production_mode` UNDECLARED / UNKNOWN / CONFLICT; NOT READ Critical source; PIXEL without visual SSOT; TEMPLATE without blueprint/content path. |

**Primary authorities:** [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) §5 · [website-factory-source-discovery-v1.md](website-factory-source-discovery-v1.md) A0, A0.5 · [onboarding-flow-v1.md](onboarding-flow-v1.md) step 0.

---

### VL1 — Architecture & Blueprint

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Validate commercial logic, IA, SEO, block compatibility before design extract or frontend bootstrap. |
| **Inputs** | Site Type Registry; Block Registry; blueprint artifacts; adoption/survivability context. |
| **Outputs** | `ARCHITECTURE_VALIDATED` state; blueprint QA record; block compatibility disposition. |
| **Exit criteria** | Site type aligned; incompatible `block_id` resolved or scoped; architecture completeness gate satisfied per mode weight. |
| **Lifecycle boundary** | Prerequisite for VL2 — **no lifecycle state claim** at VL1. |
| **Failure signals** | **FAIL** — incompatible block without waiver; IA incomplete (TEMPLATE primary); **UNKNOWN** — scope ambiguous. |

**Mode fork:** TEMPLATE_ART — Blueprint QA **primary blocking**; PIXEL_PERFECT — **secondary** (design-led consistency).

**Primary authorities:** [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) · reference-v1 `GATE_ARCHITECTURE_COMPLETE` · [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md).

---

### VL2 — Design Contract

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Lock design contract — mapping, standards, calibration — before HTML/SCSS generation. |
| **Inputs** | Design Audit (post-A0); FIG/wireframe SSOT; Production Standards Draft; mapping artifacts. |
| **Outputs** | `DESIGN_CONTRACT_VALIDATED` state; APPROVED Production Standards; Mapping QA record. |
| **Exit criteria** | Mapping QA gate PASS (full PIXEL / reduced TEMPLATE); Standards Approval HITL complete; no Critical design conflicts open. |
| **Lifecycle boundary** | Prerequisite for VL3 — **no lifecycle state claim** at VL2. |
| **Failure signals** | **STOP** — Mapping QA not executed pre-Shell (PIXEL); content contract missing (TEMPLATE); **FAIL** — token drift; Critical design conflict. |

**Primary authorities:** [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) · [production-standards-governance-v1.md](production-standards-governance-v1.md) · [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md).

---

### VL3 — Composition & Extract

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Validate composition truth before and during generation — INSTANCE resolution, asset identity, assembly order, text lock, build authorization. **Critical layer** — FP-0002 failure cluster. |
| **Inputs** | GROUP-ID register; Layout Spec; FIG extract; component instances; asset export manifest; VL2 Mapping QA artifacts. |
| **Outputs** | `COMPOSITION_VALIDATED` state; Group Register; APPROVED Layout Spec; Asset manifest; Assembly Decision record (when required); text lock artifacts; visual order record. |
| **Exit criteria** | All VL3 domains PASS per [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) §9 rollup; anti-generative-fill attestation (PIXEL). |
| **Lifecycle boundary** | Prerequisite for generation / staged build — **no BUILT claim** at VL3. |
| **Failure signals** | **STOP** — missing Layout Spec (PIXEL); INSTANCE subtree invisible; generative fill on missing extract; unresolved assembly order; brand collision before wire; silent layer-index default; **FAIL** — instance count ≠ HTML card count; failure codes **GL-** · **IR-** · **AI-** · **TL-** · **VO-** · **AD-** per VL3 Domains Charter §5. |

**Domain graph (execution order):**

```text
VL3e (Foundation) → VL3a (Instance Resolver)
                      ├─► VL3b (Asset Identity) ∥ VL3d (Text Lock)
                            └─► VL3c (Visual Ordering) → VL3f (Assembly Decision)
```

**Sub-layers / domains:**

| Domain | Role | PIXEL | TEMPLATE |
|--------|------|-------|----------|
| VL3e Composition Foundation | GROUP-ID register; Layout Spec APPROVED | **Mandatory** | Optional |
| VL3a Instance Resolver | INSTANCE walk; count ↔ HTML binding | **Mandatory** | Optional |
| VL3b Asset Identity | Brand chain; hash dedup; `section → nodeId → src` | **Mandatory** | Shared (brand) |
| VL3d Text Lock | FIG extract ↔ planned HTML; anti-paraphrase | **Mandatory** | Content deck diff |
| VL3c Visual Ordering | `bounds.y` vs layer index; order contract | **Mandatory** | Low priority |
| VL3f Assembly Decision | AUTO_ASSEMBLE / ESCALATE / STOP authorization | **Mandatory** on conflict | Optional |

**Canonical detail:** [website-factory-vl3-domains-charter-v1.md](website-factory-vl3-domains-charter-v1.md) — per-domain contracts, failure registry, FP-0002 mapping, mode matrix, VL2/VL4 handoff.

**Primary authorities:** [group-decomposition-law-v1.md](group-decomposition-law-v1.md) · [layout-spec-law-v1.md](layout-spec-law-v1.md) · [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) · charter §7 anti-generative-fill.

---

### VL4 — Build

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Confirm artifact **exists and compiles** — and **only that**. |
| **Inputs** | Approved composition artifacts; gulp workspace; staged section scope. |
| **Outputs** | `dist/` artifacts; build log; **lifecycle state BUILT**. |
| **Exit criteria** | `npm run build` exit 0; output path exists; build log uses **BUILT** vocabulary (not VERIFIED). |
| **Lifecycle boundary** | **BUILT** — first lifecycle state. Successful VL4 ⇒ artifact is **BUILT only**. |
| **Failure signals** | Compile **FAIL** — no BUILT; build log claiming VERIFIED/PRODUCTION PASS without VL5 — **false-green** (§7). |

**Explicit non-claims at VL4:** content fidelity; FIG hash match; production readiness; operator approval.

**Primary authorities:** [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · gulp pipeline · FP-0002 FAIL-001.

---

### VL5 — Fidelity & Verification

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Verify artifact against **mode-specific contract** — semantic, pixel, render, enforcement. |
| **Inputs** | BUILT artifact; mode router checklist; SSOT extracts; enforcement targets. |
| **Outputs** | VL5 evidence bundle; Layer A–E gate lines; **lifecycle state VERIFIED** (when criteria met). |
| **Exit criteria** | Mode-specific E2/E3 evidence complete (§5); no open Critical Layer A FAIL; no Critical Layer C PARTIAL (PIXEL); ROOT COMPLIANCE recorded; PF-* executed (PIXEL) or N/A with charter ref (TEMPLATE). |
| **Lifecycle boundary** | **VERIFIED** — second lifecycle state. Successful VL5 ⇒ artifact is **VERIFIED**. |
| **Failure signals** | **FAIL** / **PARTIAL** (Layer C Critical) — blocks VERIFIED; **UNKNOWN** — blocks VERIFIED; agent self-attestation without E3 — blocks VERIFIED. |

**Primary authorities:** [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) · [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) · [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) · [operational-qa-entry-v1.md](operational-qa-entry-v1.md) Production Mode QA Router.

---

### VL6 — Acceptance & Production

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Roll up delivery acceptance — operator sign-off, release gates, FINAL VERDICT. |
| **Inputs** | VERIFIED bundle; operator review; freeze/release context; Layer A rollup. |
| **Outputs** | FINAL VERDICT block; **lifecycle state PRODUCTION PASS** (when criteria met). |
| **Exit criteria** | VERIFIED precedent; OPERATOR VISUAL ACCEPT (Layer E); all required Layer A gates PASS or permitted WAIVED; ROOT COMPLIANCE PASS; mode acceptance rules satisfied. |
| **Lifecycle boundary** | **PRODUCTION PASS** — terminal lifecycle state for slice/project close. |
| **Failure signals** | **STOP** — no OPERATOR ACCEPT; **FAIL** / **UNKNOWN** on required gates; ROOT COMPLIANCE not PASS; PRODUCTION PASS claimed without VERIFIED. |

**Primary authorities:** [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) · [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §6 · [freeze-discipline-v1.md](freeze-discipline-v1.md) · charter §3.6 / §4.6.

---

### Layer summary

| Layer | Name | Output state | BUILT | VERIFIED | PROD PASS |
|-------|------|--------------|:-----:|:--------:|:---------:|
| VL0 | Intake & Mode | INTAKE_VALIDATED | — | — | — |
| VL1 | Architecture & Blueprint | ARCHITECTURE_VALIDATED | — | — | — |
| VL2 | Design Contract | DESIGN_CONTRACT_VALIDATED | — | — | — |
| VL3 | Composition & Extract | COMPOSITION_VALIDATED | — | — | — |
| VL4 | Build | **BUILT** | ✓ | — | — |
| VL5 | Fidelity & Verification | **VERIFIED** | — | ✓ | — |
| VL6 | Acceptance & Production | **PRODUCTION PASS** | — | — | ✓ |

---

## 4. Validation Signals (canonical)

### 4.1 Signal definitions

| Signal | Plane | Semantics | Scope |
|--------|-------|-----------|-------|
| **STOP** | Operational command | Halt work — scope cannot proceed until resolved | VL0–VL6; generation; VERIFIED/PRODUCTION PASS claims |
| **FAIL** | Layer A gate verdict | Criteria not met; Critical/Major blocker open | Gate rollup; blocks PRODUCTION PASS; may block VERIFIED |
| **PASS** | Layer A gate verdict | Criteria met for executed scope | Gate rollup; contributes to PRODUCTION PASS |
| **PASS WITH NOTES** | Layer A | Minor waived with Lead ack | Contributes with documented notes |
| **UNKNOWN** | Layer A | Gate attempted; evidence insufficient | Blocks PRODUCTION PASS |
| **PARTIAL** | Layer C entity status | Assembled but incomplete vs SSOT | **Blocks VERIFIED** in PIXEL_PERFECT on Critical entities |
| **SAFE UNKNOWN** | Layer D | Bounded evidence gap; escalation required | Does not auto-pass; **blocks PRODUCTION PASS** until resolved or scoped |
| **BUILT** | Layer F lifecycle | Compile succeeded; artifact exists | VL4 exit only |
| **VERIFIED** | Layer F lifecycle | Mode fidelity checks complete | VL5 exit only |
| **PRODUCTION PASS** | Layer F lifecycle | Delivery contract met | VL6 exit only |

### 4.2 Allowed transitions (lifecycle)

```text
(none) → BUILT          via VL4 only
BUILT → VERIFIED        via VL5 only — requires mode evidence bundle
VERIFIED → PRODUCTION PASS   via VL6 only — requires operator + rollup
```

**Forbidden transitions:**

| From | To | Reason |
|------|-----|--------|
| BUILT | PRODUCTION PASS | Skips fidelity (FP-0002 FAIL-001) |
| BUILT | VERIFIED | Without VL5 evidence |
| Build log PASS | VERIFIED | False-green |
| Layer A PASS (single gate) | VERIFIED | Orthogonal planes |
| PARTIAL (Critical entity) | VERIFIED | PIXEL_PERFECT rule |
| SAFE UNKNOWN (unresolved) | PRODUCTION PASS | Escalation required |

### 4.3 Blocking signals

| Signal | Blocks BUILT | Blocks VERIFIED | Blocks PRODUCTION PASS | Blocks generation |
|--------|:------------:|:---------------:|:----------------------:|:-----------------:|
| STOP | — | ✓ | ✓ | ✓ |
| FAIL (Critical) | if compile fails | ✓ | ✓ | context-dependent |
| UNKNOWN | — | ✓ | ✓ | — |
| PARTIAL (Critical, PIXEL) | — | ✓ | ✓ | — |
| SAFE UNKNOWN (open) | — | — | ✓ | — |
| FAIL (compile) | ✓ | ✓ | ✓ | ✓ |

---

## 5. Validation Evidence Model

Evidence classes extend [validation-evidence-model-v0.md](validation-evidence-model-v0.md) with Website Factory bundles.

### 5.1 Evidence class hierarchy

| Class | Description |
|-------|-------------|
| **E0 — Provenance** | who / when / scope / mode |
| **E1 — Artifact** | files, paths, hashes, build logs |
| **E2 — Checklist** | human gate execution record |
| **E3 — Diff** | extract ↔ output comparison |
| **E4 — Attestation** | operator sign-off |
| **E5 — Forensic** | post-hoc audit — **never sufficient alone for VERIFIED** |

**Rules:** E5 alone **never** satisfies VERIFIED. E4 required for PRODUCTION PASS. E3 required for PIXEL_PERFECT VERIFIED.

### 5.2 BUILT evidence

| Class | Required artifact |
|-------|-------------------|
| E0 | Scope record — section IDs in this build run |
| E1 | `npm run build` log — exit 0 |
| E1 | `dist/` output path listing |
| E2 | Staged build charter — ≤3 sections/run (recommended) |

**Sufficient:** E0 + E1 (compile + artifact).  
**Insufficient alone:** agent assertion; section count match; FIG presence.

**REPORT line:** `BUILD LIFECYCLE — BUILT`

### 5.3 VERIFIED evidence

**Common (both modes):**

| Class | Required artifact |
|-------|-------------------|
| E0 | `production_mode` in REPORT header |
| E1 | BUILT bundle complete |
| E2 | Frontend Design QA Matrix executed — Layer A lines |
| E2 | Enforcement pack EG rollup — ROOT COMPLIANCE recorded |
| E2 | No open Critical Layer A FAIL |
| E1/E3 | No Critical Layer C PARTIAL |

**PIXEL_PERFECT additions:**

| Class | Required artifact |
|-------|-------------------|
| E2 | PF-* audit executed for in-scope sections |
| E3 | Render diff or documented human side-by-side per section |
| E3 | Text lock diff — FIG strings ↔ HTML |
| E2 | VL3 composition gates PASS — Group Register, Layout Spec, Asset manifest |
| E2 | Anti-generative-fill attestation |

**TEMPLATE_ART additions:**

| Class | Required artifact |
|-------|-------------------|
| E2 | Blueprint QA PASS |
| E2 | Content contract reference |
| E2 | Block provenance — `block_id` traceability |
| E2 | PF-* marked N/A with charter citation |

**REPORT line:** `VERIFICATION LIFECYCLE — VERIFIED | NOT VERIFIED | UNKNOWN`

### 5.4 PRODUCTION PASS evidence

| Class | Required artifact |
|-------|-------------------|
| All VERIFIED | Complete VERIFIED bundle per mode |
| E4 | OPERATOR VISUAL ACCEPT (Layer E) |
| E2 | FINAL VERDICT block — reporting standard §6 |
| E2 | Required Layer A gates PASS or permitted WAIVED |
| E2 | ROOT COMPLIANCE — PASS |
| E0 | Passport `production_mode` aligned with REPORT |

**Forbidden:** PRODUCTION PASS with only matrix line; with UNKNOWN gates; without ROOT PASS; without VERIFIED precedent.

### 5.5 Evidence staleness

| Event | Effect |
|-------|--------|
| Source file change after VERIFIED | VERIFIED → stale; re-run VL3–VL5 |
| Mode transition | Re-run affected layers per charter §6 |
| Section rebuild after VERIFIED | Slice VERIFIED stale for that section |
| Exception Registry waiver | Waiver ID required in E0 |

### 5.6 Production mode linkage

| Lifecycle state | PIXEL_PERFECT extra evidence | TEMPLATE_ART extra evidence |
|---------------|------------------------------|----------------------------|
| BUILT | Same | Same |
| VERIFIED | PF-* + E3 render/text + VL3 stack | Blueprint + content + provenance |
| PRODUCTION PASS | Side-by-side operator accept | Requirements/brand accept |

---

## 6. Validation Flow

### 6.1 End-to-end chain

```text
VL0 ─► VL1 ─► VL2 ─► VL3 ─► [GENERATION] ─► VL4 ──► BUILT
                                              │
                                              ▼
                                            VL5 ──► VERIFIED
                                              │
                                              ▼
                                            VL6 ──► PRODUCTION PASS
```

### 6.2 Transition table

| Transition | Required evidence | Allowed signals | STOP conditions |
|------------|-------------------|-----------------|-----------------|
| → VL0 | Passport draft; intake trigger | PASS prerequisites | Mode undeclared; NOT READ Critical |
| VL0 → VL1 | INTAKE_VALIDATED; mode branch | PASS | Mode/source mismatch |
| VL1 → VL2 | ARCHITECTURE_VALIDATED | PASS, PASS WITH NOTES | Blueprint FAIL (TEMPLATE primary) |
| VL2 → VL3 | DESIGN_CONTRACT_VALIDATED | PASS | Mapping QA STOP (PIXEL) |
| VL3 → GEN | COMPOSITION_VALIDATED | PASS | Missing spec; INSTANCE invisible; generative fill |
| GEN → VL4 | Approved scope; composition artifacts | — | Upstream STOP |
| VL4 → BUILT | E0+E1 build bundle | BUILT only | Compile FAIL |
| BUILT → VL5 | BUILT evidence | PASS sub-checks | — |
| VL5 → VERIFIED | Mode E2/E3 bundle | VERIFIED | Critical FAIL/PARTIAL; missing E3 (PIXEL) |
| VERIFIED → VL6 | VERIFIED bundle | PASS rollup inputs | — |
| VL6 → PRODUCTION PASS | VERIFIED + E4 + §6 FINAL VERDICT | PRODUCTION PASS | No operator accept; ROOT FAIL |

### 6.3 Canonical STOP triggers

| Trigger | Layer | Mode |
|---------|-------|------|
| `production_mode ∈ { UNDECLARED, UNKNOWN, CONFLICT }` | VL0 | Both |
| NOT READ Critical source | VL0 | Both |
| PIXEL ∧ no visual SSOT | VL0 | PIXEL |
| TEMPLATE ∧ no blueprint/content path | VL0 | TEMPLATE |
| Missing Layout Spec | VL3 | PIXEL |
| INSTANCE subtree invisible | VL3 | PIXEL |
| Generative fill on missing extract | VL3 | PIXEL |
| Unresolved assembly order conflict | VL3 | PIXEL |
| OPERATOR VISUAL ACCEPT missing at close | VL6 | Both |

---

## 7. False-Green Closure Contract

**Authority:** FP-0002 FAIL-001, FAIL-018; WF-A01 Layer F; this charter.

### 7.1 Core rules

```text
Build Success ≠ VERIFIED
VERIFIED ≠ PRODUCTION PASS
npm run build PASS ≠ sufficient for PRODUCTION PASS
```

### 7.2 Formal closure rule

```text
IF build_log.verdict == "PASS" AND content_verification == NOT_EXECUTED
THEN lifecycle_state = BUILT
     forensic_eligible = true
     VERIFIED = FORBIDDEN
     PRODUCTION_PASS = FORBIDDEN
```

### 7.3 Operator obligations

| Situation | Required action |
|-----------|-----------------|
| Build log says PASS for sections | Map to **BUILT** + Layer C findings — not VERIFIED |
| Agent claims «production-ready» after build | Reject — require VL5 evidence bundle |
| 15/15 PASS pattern (FP-0002) | Emit `VERIFICATION LIFECYCLE — NOT VERIFIED`; cite forensic gap |
| Compact operational QA pass | **Not** PRODUCTION PASS authority |

### 7.4 Migration vocabulary

| Legacy term | Canonical mapping |
|-------------|-------------------|
| Build log section PASS | **BUILT** (Layer F) |
| «Production ready» after gulp only | **BUILT** |
| Agent self-attestation | **Insufficient** for VERIFIED |
| Forensic PARTIAL/FAIL | **NOT VERIFIED** |

**Cross-ref:** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §1.1, §3 migration table.

---

## 8. Production Mode Integration

Production mode (`PIXEL_PERFECT` | `TEMPLATE_ART`) forks validation at **VL0** and sets criteria at **VL3**, **VL5**, **VL6**.

```text
passport.production_mode
        │
        ▼
   VL0 Mode Router
        │
   ┌────┴────┐
PIXEL_PERFECT   TEMPLATE_ART
   │                │
   ├─ VL1 secondary blueprint    ├─ VL1 primary blueprint
   ├─ VL2 full mapping           ├─ VL2 content contract
   ├─ VL3 full composition       ├─ VL3 reduced composition
   ├─ VL5 PF + render + text     ├─ VL5 semantic + provenance
   └─ VL6 side-by-side accept    └─ VL6 requirements accept
```

### 8.1 Shared checks (both modes)

VL0 mode + Source Discovery A0 · VL1 site type + block registry · VL4 Foundation QA · VL5 Design QA Matrix (semantic) · VL5–VL6 Enforcement EG + ROOT · VL6 Operator Visual ACCEPT · Layer A–F reporting · Asset Identity (brand/logos) at VL3b · Exception Registry path.

### 8.2 Mode-specific checks

| Domain | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Visual SSOT | **Required** (VL0) | Optional |
| Blueprint QA weight | Secondary (VL1) | **Primary** (VL1) |
| Mapping QA | Full FIG extract (VL2) | Reduced token/brand |
| Group / Layout Spec | **Mandatory** (VL3) | Optional |
| Instance Resolver | **Mandatory** INSTANCE-heavy (VL3a) | Optional |
| Visual Ordering | **Mandatory** (VL3c) | Low |
| Text Lock | FIG extract SSOT (VL3d) | Content deck |
| Anti-generative-fill | **STOP** (VL3) | Allowed in bounds |
| PF-* | **Mandatory** (VL5) | **N/A** + charter ref |
| Render Diff | **Required for VERIFIED** (VL5) | Waived |
| Visual regression (VL6) | On visual changes | Semantic only |

### 8.3 Mode validation matrix

| Gate / Validation | PIXEL | TEMPLATE | STOP if violated |
|-------------------|:-----:|:--------:|:----------------:|
| Mode declared | ✓ | ✓ | ✓ |
| Visual SSOT | **M** | — | ✓ (PIXEL) |
| Blueprint + content | — | **M** | ✓ (TEMPLATE) |
| Mapping QA full | **M** | Reduced | ✓ (PIXEL) |
| Group/Layout Spec | **M** | Opt | ✓ (PIXEL) |
| Instance Resolver | **M** | Opt | ✓ (PIXEL INSTANCE-heavy) |
| Asset Identity | **M** | **M** (brand) | ✓ |
| Visual Ordering | **M** | — | ✓ (PIXEL conflict) |
| Text Lock | **M** | Content deck | ✓ (PIXEL missing) |
| `npm run build` | ✓ | ✓ | — |
| PF-* | **M** | N/A | — |
| Render Diff | **M** for VERIFIED | Waived | — |
| Blueprint QA | Secondary | **M** | ✓ (TEMPLATE) |
| Operator Visual ACCEPT | **M** | **M** | ✓ |
| PRODUCTION PASS rollup | ✓ | ✓ | ✓ |

*M = mandatory for VERIFIED at this mode*

**No new production modes** are introduced by this charter.

---

## 9. FP-0002 integration (empirical register)

Retroactive assessment through VL5:

| Metric | FP-0002 result |
|--------|----------------|
| Lifecycle | **BUILT** (compile succeeded) |
| VERIFIED | **NOT VERIFIED** (12 PARTIAL + 2 FAIL) |
| PRODUCTION PASS | **BLOCKED** |

| FAIL ID | Layer | Would block |
|---------|-------|-------------|
| FAIL-001 | VL4 | VERIFIED |
| FAIL-002–003, 012–016 | VL3d | VERIFIED |
| FAIL-004, 005, 009, 017 | VL3b | STOP or VERIFIED |
| FAIL-006, 008, 014, 015 | VL3a | VERIFIED |
| FAIL-007 | VL3c, VL3f | VERIFIED |
| FAIL-010 | VL5/VL6 | PRODUCTION PASS (scoped) |
| FAIL-011 | VL5 | VERIFIED |
| FAIL-018 | VL5 | VERIFIED |

---

## 10. Cross-surface representation

| Surface | Pointer |
|---------|---------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Validation Architecture row |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Mode router + VL map |
| [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) | Layer F + signal vocabulary |
| [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) | Mode fork + lifecycle §9 |
| LOC-ZONE passport | `production_mode`, `lifecycle_state`, `validation_status` |
| [roadmap.md](roadmap.md) | WF-A02 complete; WF-A03 deferred |

---

## 11. Related roadmap

| ID | Name | Status |
|----|------|--------|
| **WF-A01** | Production Modes Contract | **Complete (Pass 01)** |
| **WF-A02** | Validation Architecture | **This document** — Pass 01 + Pass 02 (VL3 Domains) complete |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** — see [roadmap.md](roadmap.md) |

**WF-A03 start condition:** WF-A01 **and** WF-A02 complete. **Auto-start forbidden.** Before WF-A03: separate Web-GPT Research Pass required.

**WF-A03 explicit non-goals:** Vision Layer · Visual Diff Layer · Pixel QA Runtime · Screenshot Engine · Agent Runtime.

---

## 12. Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-17 |
| Updated | 2026-06-18 — VL3 Domains integration (Pass 02) |
| Runtime | **Not claimed** |
| Automation | **Not claimed** |

*Validation Architecture Charter v1 — WF-A02 Pass 01 + Pass 02. Human-operated documentation only.*
