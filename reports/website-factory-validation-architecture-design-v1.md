# REPORT — WEBSITE FACTORY VALIDATION ARCHITECTURE

**Date:** 2026-06-17  
**Scope:** Architecture design only — **no implementation**, **no governance edits**, **no WF-A03 automation**.  
**Task:** WF-A02 — Validation Architecture design (deliverable v1)  
**Primary evidence:** [website-factory-validation-architecture-audit-v1.md](website-factory-validation-architecture-audit-v1.md)  
**Supporting evidence:** [website-factory-production-modes-architecture-v1.md](website-factory-production-modes-architecture-v1.md), [website-factory-production-modes-implementation-pass-01.md](website-factory-production-modes-implementation-pass-01.md), [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md)

**Honesty boundary:** Validation Architecture described here is a **documented, human-operated contract** — not a runtime engine, not CI enforcement, not an orchestration product. Optional project-local scripts may satisfy evidence classes; Factory does **not** claim global automation in WF-A02.

---

## Executive Summary

Website Factory обладает **высокой плотностью QA-документации** (~80+ validation-related артефактов) и **отсутствующей связующей Validation Architecture**. WF-A01 закрыл vocabulary gap (`PIXEL_PERFECT` | `TEMPLATE_ART`, **BUILT / VERIFIED / PRODUCTION PASS**), но FP-0002 доказал **false-green**: `npm run build` PASS + agent self-attestation ≠ проверенная fidelity.

**Validation Architecture** — это **упорядоченная, блокирующая, evidence-backed цепочка проверок**, связывающая существующие human gates, production mode router и пробелы FP-0002 в **единую модель слоёв, потока и доказательств**.

**Ключевые архитектурные решения v1:**

| Decision | Choice |
|----------|--------|
| **Слои валидации** | **7 validation layers (VL0–VL6)** — lifecycle-ordered, mode-forked |
| **Отчётные слои** | **Layer A–F** (reporting standard) — **ортогональны** VL0–VL6 |
| **BUILT** | Выход VL4 — артефакт скомпилирован |
| **VERIFIED** | Выход VL5 — mode-specific fidelity проверена |
| **PRODUCTION PASS** | Выход VL6 — rollup + operator + ROOT COMPLIANCE |
| **False-green closure** | Build log PASS → **BUILT only**; VERIFIED требует VL5 evidence |
| **Automation** | Human-first; project-local tooling — optional evidence class, не Factory product |

**Вердикт:** WF-A02 design target — **единый charter Validation Architecture** + mode matrix + evidence model + false-green wire spec. **Не** WF-A03 (vision/diff runtime).

---

## Validation Architecture Overview

### PART 1 — Definition

**Validation Architecture** в контексте Website Factory — это **архитектурная модель**, определяющая:

1. **Что** проверяется на каждом этапе производственного цикла (intake → release).
2. **Когда** проверка обязательна, опциональна или waived (production mode fork).
3. **Как** результат влияет на продвижение pipeline (**PASS** / **FAIL** / **UNKNOWN** / **STOP**).
4. **Какие доказательства** требуются для claims **BUILT**, **VERIFIED**, **PRODUCTION PASS**.
5. **Как** существующие ~80 governance-документов **встраиваются** в ordered chain без mythology drift.

**Validation Architecture — это НЕ:**

- validator runtime, CI pipeline, visual diff SaaS, orchestration engine;
- замена существующих gate-документов;
- автоматическое enforcement product (WF-A03 scope).

**Validation Architecture — это:**

- **связующий контракт** между разрозненными QA packs;
- **ordered validation layer chain** с blocking semantics;
- **mode-aware fork** (`PIXEL_PERFECT` | `TEMPLATE_ART`);
- **evidence model**, пригодный для human ops **и** будущего project-local tooling;
- **false-green prevention semantics** — разделение compile success и production readiness.

### Architectural planes (orthogonal)

```text
┌─────────────────────────────────────────────────────────────────┐
│  PLANE 1 — VALIDATION LAYERS (VL0–VL6)                          │
│  WHAT is checked, WHEN in lifecycle, blocking order             │
└─────────────────────────────────────────────────────────────────┘
                              ×
┌─────────────────────────────────────────────────────────────────┐
│  PLANE 2 — REPORTING LAYERS (A–F)                               │
│  HOW results are recorded in REPORT                             │
│  A=gate verdict · B=sub-check · C=entity · D=SAFE UNKNOWN       │
│  E=operator visual · F=BUILT/VERIFIED/PRODUCTION PASS           │
└─────────────────────────────────────────────────────────────────┘
                              ×
┌─────────────────────────────────────────────────────────────────┐
│  PLANE 3 — PRODUCTION MODE                                      │
│  WHICH gates apply, strictness, waiver rules                    │
│  PIXEL_PERFECT | TEMPLATE_ART                                   │
└─────────────────────────────────────────────────────────────────┘
                              ×
┌─────────────────────────────────────────────────────────────────┐
│  PLANE 4 — ORTHOGONAL RISK DIMENSIONS                           │
│  Forge mode · Operational modes · Exception Registry            │
└─────────────────────────────────────────────────────────────────┘
```

### Design principles (from audit + FP-0002)

| # | Principle | Basis |
|---|-----------|-------|
| 1 | **Evidence-first** — no pass without cited evidence class | Validation Runtime v0; FP-0002 FAIL-001 |
| 2 | **Blocking chain** — upstream FAIL/STOP blocks downstream VERIFIED | Audit gap: governance without enforcement |
| 3 | **Mode fork at VL0** — router determines VL3/VL5 criteria | WF-A01 charter |
| 4 | **BUILT ≠ VERIFIED ≠ PRODUCTION PASS** — lifecycle orthogonality | Layer F; FAIL-001/018 |
| 5 | **PARTIAL blocks VERIFIED** in PIXEL_PERFECT — assembled ≠ faithful | FP-0002: 12 PARTIAL undetected |
| 6 | **SAFE UNKNOWN escalates, does not auto-pass** | safe-unknown-boundary |
| 7 | **Human-operated default** — automation is optional evidence path | Audit: 0 auto products in-repo |
| 8 | **Staged validation** — max 2–3 sections/run for context survivability | FP-0002 memory analysis |

### End-to-end chain (conceptual)

```text
INTAKE
  └─► VL0 Intake & Mode Validation
         └─► VL1 Architecture & Blueprint Validation
                └─► VL2 Design Contract Validation
                       └─► VL3 Composition & Extract Validation
                              └─► BUILD (gulp)
                                     └─► VL4 Build Validation  ──► BUILT
                                            └─► VL5 Fidelity & Verification
                                                   └─► VERIFIED
                                                          └─► VL6 Acceptance & Production
                                                                 └─► PRODUCTION PASS
```

---

## Validation Layers

### PART 2 — Proposed model: VL0–VL6

Семь слоёв выбраны потому что:

- покрывают **полный Factory lifecycle** от intake до production acceptance;
- отделяют **compile** (VL4) от **fidelity** (VL5) — закрывает false-green;
- выделяют **composition/extract** (VL3) как отдельный блок — FP-0002 root cause cluster;
- не дублируют reporting Layer A–F (ортогональная плоскость);
- позволяют **mode fork** без третьего global pipeline.

Альтернатива «Layer A/B/C» как validation layers **отклонена** — эти буквы уже заняты reporting standard.

---

### VL0 — Intake & Mode Validation

**Purpose:** Убедиться, что проект **декларирован**, режим производства **известен**, источники **инвентаризированы** — до любой frontend работы.

| Check domain | Primary authority | Blocking? |
|--------------|-------------------|-----------|
| Production mode declared | Charter §5; passport `production_mode` | **STOP** if UNDECLARED |
| Mode ↔ source alignment | Charter §5; Source Discovery A0.5 | **STOP** on mismatch |
| Source Discovery A0 inventory | `website-factory-source-discovery-v1.md` | **STOP** on NOT READ Critical sources |
| Passport completeness | `FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md` | **STOP** if missing mode |
| Orthogonality ack | Forge mode ≠ production mode | Non-blocking record |

**Mode fork:**

| Check | PIXEL_PERFECT | TEMPLATE_ART |
|-------|---------------|--------------|
| Visual SSOT registered | **Required** | Optional |
| Blueprint/content path | Secondary | **Required** |
| A0 checklist branch | Full visual + structural | Structural + content |

**Output state:** `INTAKE_VALIDATED` — prerequisite for VL1.

---

### VL1 — Architecture & Blueprint Validation

**Purpose:** Проверить **коммерческую логику, IA, SEO, block compatibility** до design extract / frontend bootstrap.

| Check domain | Primary authority | Blocking? |
|--------------|-------------------|-----------|
| Site type alignment | Site Type Registry v1 | FAIL blocks VL2+ |
| Blueprint QA (12 categories) | `page-blueprint-qa-checklist-v0.md` | **Primary** in TEMPLATE_ART |
| Block registry compatibility | Block Registry + checklist §8 | FAIL on incompatible `block_id` |
| Architecture completeness | reference-v1 `GATE_ARCHITECTURE_COMPLETE` | FAIL if IA incomplete |
| Page-block validation semantics | reference-v1 `page-block-validation/` | UNKNOWN → scope decision |
| Adoption / survivability | `adoption-validation-flow-v1.md` | Conditional |

**Mode fork:**

| Weight | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Blueprint QA | Secondary — consistency design ↔ blueprint | **Primary — blocking** |
| Block provenance | Maps design sections → `block_id` | Selects `block_id` from palette |

**Output state:** `ARCHITECTURE_VALIDATED`.

---

### VL2 — Design Contract Validation

**Purpose:** Зафиксировать **design contract** — mapping, standards, decomposition — до HTML/SCSS generation.

| Check domain | Primary authority | Blocking? |
|--------------|-------------------|-----------|
| Design Audit (post-A0) | Source Discovery Phase A | FAIL on Critical conflicts |
| Design → Frontend Mapping QA | `design-source-to-frontend-mapping-governance-v1.md` | **STOP** pre-Shell |
| Production Standards Draft + Approval | `production-standards-governance-v1.md` | HITL gate |
| Design calibration | `frontend-design-calibration-stage-v1.md` | FAIL on token drift |
| GATE_DESIGN_COMPLETE | reference-v1 production-qa | Architectural human gate |

**Mode fork:**

| Check | PIXEL_PERFECT | TEMPLATE_ART |
|-------|---------------|--------------|
| Full FIG extract mapping | **Mandatory** | **Reduced** — token/brand only |
| Wireframe SSOT | If present — binding | Primary structural reference |
| Content contract | Supplements FIG gaps | **Mandatory** before page build |

**Output state:** `DESIGN_CONTRACT_VALIDATED`.

---

### VL3 — Composition & Extract Validation

**Purpose:** Проверить **composition truth** до и во время generation — INSTANCE resolution, asset identity, assembly order, text lock. **Критический слой** — FP-0002 failure cluster.

| Sub-layer | Role | PIXEL | TEMPLATE |
|-----------|------|-------|----------|
| **VL3a — Instance Resolver Validation** | INSTANCE subtree walk; instance count ↔ HTML card count | **Mandatory** | Optional (wireframe import) |
| **VL3b — Asset Identity Validation** | Brand chain, hash dedup, `section → nodeId → src` manifest | **Mandatory** | Shared (logos/favicons) |
| **VL3c — Visual Ordering Validation** | `bounds.y` vs layer index; ASSEMBLY DECISION record | **Mandatory** | Low — DOM from blueprint |
| **VL3d — Text Lock Validation** | FIG extract ↔ planned HTML strings; anti-paraphrase | **Mandatory** | Content deck diff |
| **VL3e — Group / Layout Spec Gates** | GROUP-ID register; APPROVED Layout Spec before HTML | **Mandatory** | Optional |

| Check domain | Primary authority | Blocking? |
|--------------|-------------------|-----------|
| Group Decomposition Gate | `group-decomposition-law-v1.md` | **STOP** without register |
| Layout Spec Gate | `layout-spec-law-v1.md` | **STOP** without APPROVED spec |
| Anti-generative-fill | Charter §7 | **STOP** on missing extract (PIXEL) |
| Brand Asset Detection | `failures/asset-identity-collision-v1.md` | **STOP** before logo wire |
| Assembly Decision | FAIL-007 lesson; charter SAFE UNKNOWN | **STOP** on unresolved conflict |

**Output state:** `COMPOSITION_VALIDATED` — prerequisite for generation / staged build.

**Audit verdict:** VL3 — **partially documented, not gated as unified layer** — WF-A02 primary design target.

---

### VL4 — Build Validation

**Purpose:** Подтвердить, что **артефакт создан и компилируется** — и **только это**.

| Check domain | Mechanism | Result |
|--------------|-----------|--------|
| `npm run build` | Gulp pipeline | **Auto** — compile |
| dist/ artifact exists | Filesystem | **Auto** |
| Foundation QA rollup | `frontend-foundation-qa-governance-v1.md` | Human |
| Staged build charter | Max 2–3 sections/run | Human discipline |
| Build log vocabulary | **BUILT** — not PASS/VERIFIED | Human + tooling wire |

**Lifecycle boundary:** Successful VL4 ⇒ artifact state **BUILT**.

**Explicit non-claims at VL4:**

- content fidelity;
- FIG hash match;
- production readiness;
- operator approval.

**False-green closure rule:** Any build log line previously labeled «PASS» without content verification maps to **BUILT** (Layer F). **VERIFIED forbidden** at VL4 exit.

---

### VL5 — Fidelity & Verification Validation

**Purpose:** Проверить артефакт **против mode-specific contract** — semantic, pixel, render, enforcement.

| Sub-domain | PIXEL_PERFECT | TEMPLATE_ART |
|------------|---------------|--------------|
| Frontend Design QA Matrix (DQ-*) | Full | Full — semantic emphasis |
| Pixel Fidelity Audit (PF-*) | **Mandatory** | **N/A** (waived with charter ref) |
| Render Diff (FIG ↔ dist) | **Required for VERIFIED** | Waived |
| Text diff / lock verify | Per-section FIG ↔ HTML | Content deck ↔ HTML |
| Enforcement pack EG-01–EG-05 | Full | Full |
| ROOT COMPLIANCE | Required | Required |
| Entity completeness (Layer C) | PARTIAL on any Critical entity → blocks VERIFIED | PARTIAL on content entities → blocks |
| P0 Technical vs Visual | AUTOMATED_PASS ≠ VISUAL_ACCEPT | Brand/UX vs requirements |

**Lifecycle boundary:** Successful VL5 ⇒ artifact state **VERIFIED**.

**FP-0002 mapping:** Forensic 12 PARTIAL + 2 FAIL ⇒ **NOT VERIFIED** — would block if VL5 operational.

---

### VL6 — Acceptance & Production Validation

**Purpose:** Rollup **delivery acceptance** — operator sign-off, release gates, FINAL VERDICT.

| Check domain | Primary authority | Blocking? |
|--------------|-------------------|-----------|
| Operator Visual ACCEPT | `operator-visual-approval-law-v1.md` | **STOP** without sign-off |
| Layer A gate rollup | `frontend-qa-reporting-standard-v1.md` §6 | FAIL/UNKNOWN blocks |
| ROOT COMPLIANCE — PASS | Enforcement pack §6 | Blocks PRODUCTION PASS |
| Release / freeze discipline | `freeze-discipline-v1.md`, visual regression | Conditional |
| GATE_PRODUCTION_QA_PASS | reference-v1 | Architectural |
| Mode acceptance rules | Charter §3.6 / §4.6 | Mode-specific checklist |

**Lifecycle boundary:** Successful VL6 ⇒ **PRODUCTION PASS** (FINAL VERDICT).

---

### Layer summary table

| Layer | Name | Primary output | BUILT | VERIFIED | PROD PASS |
|-------|------|----------------|-------|----------|-----------|
| VL0 | Intake & Mode | INTAKE_VALIDATED | — | — | — |
| VL1 | Architecture & Blueprint | ARCHITECTURE_VALIDATED | — | — | — |
| VL2 | Design Contract | DESIGN_CONTRACT_VALIDATED | — | — | — |
| VL3 | Composition & Extract | COMPOSITION_VALIDATED | — | — | — |
| VL4 | Build | **BUILT** | **✓** | — | — |
| VL5 | Fidelity & Verification | **VERIFIED** | — | **✓** | — |
| VL6 | Acceptance & Production | **PRODUCTION PASS** | — | — | **✓** |

---

## Validation Flow

### PART 3 — BUILT / VERIFIED / PRODUCTION PASS placement

Трёхуровневая модель (WF-A01 Layer F) — **lifecycle states на границах VL4/VL5/VL6**, не gate verdicts.

```text
VL0 ─► VL1 ─► VL2 ─► VL3 ─► [GENERATION] ─► VL4 ──► BUILT
                                              │
                                              ▼
                                            VL5 ──► VERIFIED
                                              │
                                              ▼
                                            VL6 ──► PRODUCTION PASS
```

| State | Definition | Minimum evidence | Forbidden shortcuts |
|-------|------------|------------------|---------------------|
| **BUILT** | Artifact exists; compile succeeded | `npm run build` log; dist path; staged scope record | Calling «production-ready»; skipping VL5 |
| **VERIFIED** | Mode-appropriate fidelity checks complete | VL5 evidence bundle (see Evidence Model) | Build PASS alone; agent self-attestation |
| **PRODUCTION PASS** | Delivery contract met | VERIFIED + VL6 rollup + OPERATOR ACCEPT + ROOT PASS | VERIFIED without operator; UNKNOWN gates |

**Orthogonality to Layer A:**

- Layer A **PASS** on a single gate ≠ **VERIFIED**.
- Layer F **BUILT** may coexist with Layer A **FAIL** on fidelity gates — state is inconsistent; REPORT must not claim VERIFIED.
- **FINAL VERDICT — PRODUCTION PASS** requires **VERIFIED** precedent (reporting standard §1.1).

**False-green closure (architectural rule):**

```text
IF build_log.verdict == "PASS" AND content_verification == NOT_EXECUTED
THEN lifecycle_state = BUILT
     forensic_eligible = true
     VERIFIED = FORBIDDEN
     PRODUCTION_PASS = FORBIDDEN
```

---

### PART 4 — SAFE UNKNOWN / STOP / FAIL / PARTIAL / PASS in flow

#### Signal taxonomy

| Signal | Plane | Semantics | Pipeline effect |
|--------|-------|-----------|-----------------|
| **STOP** | Operational command | Halt work — scope cannot proceed until resolved | **Hard halt** — no generation, no VERIFIED claim |
| **FAIL** | Layer A gate verdict | Criteria not met; Critical/Major blocker open | Blocks PRODUCTION PASS; may block VERIFIED |
| **PASS** | Layer A gate verdict | Criteria met for executed scope | Contributes to PRODUCTION PASS rollup |
| **PASS WITH NOTES** | Layer A | Minor waived with Lead ack | Contributes with notes |
| **UNKNOWN** | Layer A | Gate attempted but evidence insufficient | Blocks PRODUCTION PASS |
| **PARTIAL** | Layer C entity status | Assembled but incomplete vs SSOT | **Blocks VERIFIED** in PIXEL_PERFECT; investigate in TEMPLATE |
| **SAFE UNKNOWN** | Layer D | Bounded evidence gap; escalation required | Does **not** auto-block BUILT; **blocks PRODUCTION PASS** until resolved or scoped |
| **WAIVED** | Layer A | Exception Registry override | Contributes if peer gates PASS; never waives ROOT |

#### Flow diagram

```text
                    ┌──────────────┐
                    │   VL0 start  │
                    └──────┬───────┘
                           │
              mode UNDECLARED / source mismatch
                           │
                           ▼
                      ┌─────────┐
                      │  STOP   │◄──── VL3: missing extract (PIXEL)
                      └─────────┘      VL3: assembly conflict unresolved
                           ▲          VL6: no OPERATOR ACCEPT
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
    gate FAIL                           gate UNKNOWN
    (Critical)                          (evidence gap)
         │                                   │
         ▼                                   ▼
  PRODUCTION BLOCKED              PRODUCTION UNKNOWN
  (may still be BUILT               (may still be BUILT
   if VL4 ran)                       if VL4 ran)

  Entity PARTIAL (Layer C) ──► VERIFIED blocked (PIXEL)
  SAFE UNKNOWN (Layer D) ──► logged; PRODUCTION PASS blocked until HITL
```

#### STOP triggers (canonical set)

| Trigger | Layer | Mode |
|---------|-------|------|
| `production_mode ∈ { UNDECLARED, UNKNOWN, CONFLICT }` | VL0 | Both |
| NOT READ Critical source | VL0 | Both |
| PIXEL ∧ no visual SSOT | VL0 | PIXEL |
| TEMPLATE ∧ no blueprint/content path | VL0 | TEMPLATE |
| Missing Layout Spec (PIXEL) | VL3 | PIXEL |
| INSTANCE subtree invisible | VL3 | PIXEL |
| Generative fill attempt on missing extract | VL3 | PIXEL |
| Unresolved assembly order conflict | VL3 | PIXEL |
| OPERATOR VISUAL ACCEPT missing at close | VL6 | Both |

#### PARTIAL vs PASS distinction (FP-0002 lesson)

| Context | PARTIAL means | Effect |
|---------|---------------|--------|
| Forensic section audit | DOM exists; content/asset fidelity incomplete | Section-level — rollup blocks VERIFIED |
| Layer C entity compare | MATCH / PARTIAL / MISSING vs SSOT | Entity-level — Critical PARTIAL blocks VERIFIED |
| Build log (legacy) | **Deprecated** — map to BUILT + Layer C findings | Must not imply PASS |

**Rule:** In PIXEL_PERFECT, **any Critical entity PARTIAL** on in-scope sections ⇒ lifecycle **NOT VERIFIED**, regardless of compile success.

---

### Named validation roles (PART 5)

Каждая роль — **validation domain** внутри VL0–VL6, не обязательно отдельный agent product.

#### Instance Resolver Validation

| Attribute | Value |
|-----------|-------|
| **Layer** | VL3a |
| **Purpose** | Walk INSTANCE subtrees; ensure component instances map to HTML elements |
| **PIXEL_PERFECT** | **Mandatory** before INSTANCE-heavy sections |
| **TEMPLATE_ART** | Optional — wireframe/component import only |
| **Blocking** | Instance count ≠ card count → **STOP** section build |
| **Evidence** | Group Register; instance enumeration record; FIG-AUTO-GROUP-REGISTER-TEST pattern |
| **FP-0002** | FAIL-006, FAIL-008, FAIL-014, FAIL-015 |
| **Existing foundation** | `group-decomposition-law-v1.md`; charter SAFE UNKNOWN |
| **Gap** | No operational resolver gate; no pre-build blocking |

#### Asset Identity Validation

| Attribute | Value |
|-----------|-------|
| **Layer** | VL3b |
| **Purpose** | Unique asset binding; brand detection; hash dedup; forbid frame-export pollution |
| **PIXEL_PERFECT** | **Mandatory** |
| **TEMPLATE_ART** | **Shared** — logos, favicons, brand marks |
| **Blocking** | Collision / first-image-as-logo → **STOP** before wire |
| **Evidence** | Asset manifest `section → nodeId → hash → src`; brand allowlist |
| **FP-0002** | FAIL-004, FAIL-005, FAIL-009, FAIL-017 |
| **Existing foundation** | `failures/asset-identity-collision-v1.md`; PF-07; DQ-08 |
| **Gap** | No pre-wire blocking gate; no hash dedup registry product |

#### Visual Ordering Validation

| Attribute | Value |
|-----------|-------|
| **Layer** | VL3c |
| **Purpose** | Section DOM order matches visual SSOT; resolve bounds.y vs layer-index conflicts |
| **PIXEL_PERFECT** | **Mandatory** |
| **TEMPLATE_ART** | Low — order from blueprint DOM, not FIG |
| **Blocking** | Unresolved anomaly → **STOP** or **ASSEMBLY DECISION** record required |
| **Evidence** | Assembly Decision record; ordered section list with y-coordinates |
| **FP-0002** | FAIL-007 |
| **Existing foundation** | Discovery anomaly flag; charter ASSEMBLY DECISION |
| **Gap** | No assembly rule policy; silent layer-index default |

#### Frontend Validation

| Attribute | Value |
|-----------|-------|
| **Layers** | VL4 (build) + VL5 (fidelity subset) |
| **Purpose** | Compile verification + human QA chain (matrix, PF, enforcement) |
| **PIXEL_PERFECT** | Full PF-* + render/text diff |
| **TEMPLATE_ART** | Semantic matrix; PF N/A |
| **Blocking** | EG FAIL → blocks PRODUCTION PASS; compile fail → no BUILT |
| **Evidence** | Build log (BUILT); DQ/PF checklists; ROOT COMPLIANCE block |
| **FP-0002** | FAIL-001, FAIL-010, FAIL-011, FAIL-018 |
| **Existing foundation** | 12+ frontend QA docs; enforcement pack; reporting standard |
| **Gap** | False-green; BUILT/VERIFIED not in build tooling |

#### Release Validation

| Attribute | Value |
|-----------|-------|
| **Layer** | VL6 (pre-deploy slice) |
| **Purpose** | Freeze discipline, visual regression baseline, delivery lifecycle |
| **PIXEL_PERFECT** | Visual regression **mandatory** on visual changes |
| **TEMPLATE_ART** | Responsive + semantic regression |
| **Blocking** | Freeze violation → **STOP** release |
| **Evidence** | Screenshot baselines; freeze record; delivery stage sign-off |
| **Existing foundation** | `visual-regression-workflow-v1.md`; `freeze-discipline-v1.md` |
| **Gap** | No unified release rollup across LOC-ZONE + workspace |

#### Production Validation

| Attribute | Value |
|-----------|-------|
| **Layer** | VL6 |
| **Purpose** | FINAL VERDICT; mode acceptance rollup; PRODUCTION PASS claim |
| **PIXEL_PERFECT** | VERIFIED + side-by-side operator accept |
| **TEMPLATE_ART** | VERIFIED + requirements/brand accept |
| **Blocking** | Any required gate FAIL/UNKNOWN; ROOT not PASS |
| **Evidence** | FINAL VERDICT block; Layer A rollup; Layer F lifecycle line |
| **FP-0002** | Would yield PRODUCTION BLOCKED if VL5 applied retroactively |
| **Existing foundation** | reporting standard §6; charter §9; operational-qa-entry router |
| **Gap** | Operators may skip VERIFIED; no enforcement |

---

### Production mode split (PART 6)

#### Shared (both modes)

| Domain | Layer | Notes |
|--------|-------|-------|
| VL0 mode declaration + Source Discovery A0 | VL0 | Full inventory both modes |
| Site type + block registry compatibility | VL1 | Shared |
| Foundation QA | VL4 | Shared |
| Frontend Design QA Matrix (semantic/responsive/a11y) | VL5 | PF waived in TEMPLATE |
| Enforcement pack EG-01–EG-05 + ROOT COMPLIANCE | VL5–VL6 | Shared |
| Operator Visual ACCEPT | VL6 | Different acceptance criteria |
| BUILT / VERIFIED / PRODUCTION PASS lifecycle | VL4–VL6 | VERIFIED criteria differ |
| Asset Identity (brand/logos) | VL3b | Shared |
| Exception Registry / waiver path | All | Shared |
| Reporting Layer A–F | REPORT | Shared vocabulary |

#### PIXEL_PERFECT only

| Domain | Layer | Waived in TEMPLATE? |
|--------|-------|---------------------|
| Full Design → Frontend Mapping QA (FIG extract) | VL2 | Reduced |
| Group Decomposition + Layout Spec (mandatory) | VL3e | Optional |
| Instance Resolver Validation | VL3a | Optional |
| Visual Ordering / ASSEMBLY DECISION | VL3c | Low priority |
| Text Lock (FIG extract SSOT) | VL3d | → content deck diff |
| Anti-generative-fill gate | VL3 | N/A — generative allowed in bounds |
| Pixel Fidelity Audit (PF-*) | VL5 | **N/A** |
| Render Diff (FIG ↔ dist) | VL5 | **Waived** |
| `section-NN.lock.json` SSOT | VL3d | Optional |
| Block-by-block operator approval (client AGENTS.md) | VL5 | Inactive |
| Visual regression on visual changes | VL6 | Semantic only |

#### TEMPLATE_ART only

| Domain | Layer | Waived in PIXEL? |
|--------|-------|------------------|
| Blueprint QA as **primary blocking** gate | VL1 | Secondary in PIXEL |
| Content contract completeness before build | VL2 | FIG-led |
| Block provenance audit (`block_id` traceability) | VL1/VL5 | Different emphasis |
| Foundation adoption validation | VL1/VL4 | Same path, different SSOT |
| PF-* explicit N/A with charter reference | VL5 | Mandatory in PIXEL |
| «No pixel-perfect claims» in REPORT/comms | VL6 | PIXEL claims fidelity |

#### Mode validation matrix (summary)

| Gate / Validation | PIXEL_PERFECT | TEMPLATE_ART | STOP if violated |
|-------------------|:-------------:|:------------:|:----------------:|
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

---

## Validation Evidence Model

### PART 7 — Evidence for BUILT / VERIFIED / PRODUCTION PASS

Evidence classes extend Validation Runtime v0 semantics with WF-specific bundles.

#### Evidence class hierarchy

```text
E0 — Provenance     (who/when/scope)
E1 — Artifact       (files, paths, hashes)
E2 — Checklist      (human gate execution record)
E3 — Diff           (extract ↔ output comparison)
E4 — Attestation    (operator sign-off)
E5 — Forensic       (post-hoc audit — not sufficient alone for VERIFIED)
```

**Rule:** E5 alone **never** satisfies VERIFIED. E4 required for PRODUCTION PASS. E3 required for PIXEL VERIFIED.

---

#### BUILT — minimum evidence bundle

| Class | Required artifact | Example |
|-------|-------------------|---------|
| E0 | Scope record | Section IDs in this build run |
| E1 | Build log | `npm run build` exit 0 |
| E1 | Output path | `dist/` file listing |
| E2 | Staged build charter | ≤3 sections/run record (recommended) |

**Sufficient condition:** E0 + E1 (compile + artifact).

**Insufficient alone:** agent assertion; section count match; FIG presence.

---

#### VERIFIED — minimum evidence bundle

**Common (both modes):**

| Class | Required artifact |
|-------|-------------------|
| E0 | `production_mode` in REPORT header |
| E1 | BUILT bundle complete |
| E2 | Frontend Design QA Matrix executed — Layer A lines |
| E2 | Enforcement pack EG rollup — ROOT COMPLIANCE recorded |
| E2 | No open Critical Layer A FAIL |
| E1/E3 | Entity completeness — no Critical Layer C PARTIAL |

**PIXEL_PERFECT additions:**

| Class | Required artifact |
|-------|-------------------|
| E2 | PF-* audit executed for in-scope sections |
| E3 | Render diff or **documented human side-by-side** per section (if no script — SAFE UNKNOWN on automation, not on verification) |
| E3 | Text lock diff — FIG strings ↔ HTML (per section or `section-NN.lock.json`) |
| E2 | VL3 composition gates PASS — Group Register, Layout Spec, Asset manifest |
| E2 | Anti-generative-fill attestation — no invented copy |

**TEMPLATE_ART additions:**

| Class | Required artifact |
|-------|-------------------|
| E2 | Blueprint QA PASS |
| E2 | Content contract reference |
| E2 | Block provenance — `block_id` traceability |
| E2 | PF-* marked N/A with charter citation |

**Sufficient condition:** BUILT bundle + mode-specific E2/E3 complete + no Critical FAIL/PARTIAL.

---

#### PRODUCTION PASS — minimum evidence bundle

| Class | Required artifact |
|-------|-------------------|
| All VERIFIED | Complete VERIFIED bundle |
| E4 | OPERATOR VISUAL ACCEPT (Layer E) |
| E2 | FINAL VERDICT block — §6 compliant |
| E2 | All required Layer A gates PASS or permitted WAIVED |
| E2 | ROOT COMPLIANCE — PASS |
| E0 | Passport `production_mode` aligned with REPORT |

**Sufficient condition:** VERIFIED + E4 + §6 FINAL VERDICT emitted.

**Forbidden:** PRODUCTION PASS with only matrix line; with UNKNOWN gates; without ROOT PASS.

---

#### Evidence staleness rules

| Event | Effect on evidence |
|-------|-------------------|
| Source file change after VERIFIED | VERIFIED → stale; re-run VL3–VL5 |
| Mode transition | Re-run affected layers per charter §6 |
| Section rebuild after VERIFIED | Slice VERIFIED stale for that section |
| Exception Registry waiver | Evidence of waiver ID required (E0) |

---

#### Optional machine-readable evidence (WF-A02 design target, not implementation)

```text
validation_evidence/
  intake_record.json          # VL0
  composition_manifest.json   # VL3 — instances, assets, order, text locks
  build_record.json           # VL4 — BUILT
  verification_record.json    # VL5 — gate lines + diff summaries
  production_acceptance.json  # VL6 — FINAL VERDICT inputs
```

Human REPORT remains **authoritative**; JSON artifacts are **supporting** when present.

---

## Production Mode Integration

WF-A01 Production Modes Contract integrates with Validation Architecture as **Plane 3** — fork at VL0, criteria at VL3/VL5, acceptance at VL6.

```text
passport.production_mode
        │
        ▼
   VL0 Mode Router ─────────────────────────────┐
        │                                        │
   PIXEL_PERFECT                          TEMPLATE_ART
        │                                        │
        ├─ VL1: design-led blueprint             ├─ VL1: blueprint-primary
        ├─ VL2: full mapping                     ├─ VL2: content contract
        ├─ VL3: full composition stack           ├─ VL3: reduced composition
        ├─ VL5: PF + render + text diff          ├─ VL5: semantic + provenance
        └─ VL6: side-by-side accept              └─ VL6: requirements accept
```

**Orthogonal dimensions (must not conflate in REPORT):**

| Dimension | Controls | Example mistake |
|-----------|----------|-----------------|
| `production_mode` | VL3/VL5 criteria | Running PF-* on TEMPLATE_ART without transition |
| Forge mode (Lite/Standard/Critical) | Checklist depth | Claiming Critical Forge = VERIFIED |
| Operational modes | Governance density | Compressing Layer A lines |

**Mode transition:** Updates passport `mode_history[]`; triggers **partial re-validation** from first affected layer (charter §6).

---

## FP-0002 Findings Integration

Forensic failures map to Validation Architecture layers and **would-have-blocked** semantics.

| FAIL ID | Title | Layer | Would block | Evidence class needed |
|---------|-------|-------|-------------|----------------------|
| FAIL-001 | False-green build log | VL4 | VERIFIED | E3 diff not executed |
| FAIL-002 | Review hallucination | VL3d | VERIFIED (PIXEL) | E3 text lock |
| FAIL-003 | Intro text drift | VL3d | VERIFIED | E3 text lock |
| FAIL-004 | Image hash collision | VL3b | BUILT or STOP | E1 asset manifest |
| FAIL-005 | Asset orphans | VL3b | VERIFIED | E1 manifest binding |
| FAIL-006 | Component instance blindness | VL3a | VERIFIED | E2 instance register |
| FAIL-007 | Visual order drift | VL3c | VERIFIED | E2 assembly decision |
| FAIL-008 | Specialists placeholders | VL3a | VERIFIED | E3 instance mapping |
| FAIL-009 | Articles missing assets | VL3b | VERIFIED | E1 per-component assets |
| FAIL-010 | Interaction stubs | VL5 | PRODUCTION PASS (scoped) | KNOWN NON-GOALS record |
| FAIL-011 | Empty alt | VL5 | VERIFIED (a11y) | E2 DQ line |
| FAIL-012 | Stat description loss | VL3d | VERIFIED | E3 text lock |
| FAIL-013 | Quote truncation | VL3d | VERIFIED | E3 text lock |
| FAIL-014 | Program cards invented | VL3a | VERIFIED | E2 instance walk |
| FAIL-015 | Services invented | VL3a | VERIFIED | E2 instance walk |
| FAIL-016 | Disclaimer leak | VL3d | VERIFIED | E3 section-scoped binding |
| FAIL-017 | Logo collision | VL3b | STOP | E2 brand chain |
| FAIL-018 | No post-build FIG diff | VL5 | VERIFIED | E3 render/text diff |

**Retroactive FP-0002 assessment through VL5:**

- Lifecycle state: **BUILT** (compile succeeded).
- VERIFIED: **NOT VERIFIED** (12 PARTIAL + 2 FAIL).
- PRODUCTION PASS: **BLOCKED**.

**Recommended validation token registry (WF-A02 implementation follow-up):** Link each `FAIL-*` to VL layer + expected gate + attribution token — audit Priority B item.

---

## Reusable Foundation

### PART 8 — Existing documents as WF-A02 foundation

Документы **не заменяются** — они **встраиваются** в VL0–VL6.

#### Tier 1 — Structural backbone (direct map to layers)

| Document | Validation layer | Role in architecture |
|----------|------------------|----------------------|
| `website-factory-production-modes-charter-v1.md` | VL0, VL5, VL6 | Mode fork + lifecycle + anti-fill |
| `operational-qa-entry-v1.md` | VL5–VL6 | QA router entry |
| `frontend-qa-reporting-standard-v1.md` | All (reporting plane) | Layer A–F vocabulary |
| `website-factory-source-discovery-v1.md` | VL0 | Intake gate |
| `design-source-to-frontend-mapping-governance-v1.md` | VL2 | Pre-shell mapping |
| `group-decomposition-law-v1.md` | VL3e | Composition gate |
| `layout-spec-law-v1.md` | VL3e | Composition gate |
| `website-factory-enforcement-pack-v1.md` | VL5–VL6 | ROOT COMPLIANCE |
| `frontend-design-qa-matrix-v1.md` | VL5 | Fidelity domain catalog |
| `pixel-fidelity-audit-rules-v1.md` | VL5 | PIXEL fidelity |
| `operator-visual-approval-law-v1.md` | VL6 | Operator accept |
| `frontend-compliance-decision-model-v1.md` | VL5–VL6 | Verdict routing |
| `frontend-failure-attribution-model-v1.md` | Post-VL5 | Investigation |

#### Tier 2 — Semantic runtime vocabulary

| Document | Role |
|----------|------|
| `validation-runtime-overview-v0.md` + 9 linked docs | Evidence, waiver, escalation semantics |
| `qa-validation-model.md` | Validator Agent framing (planned) |
| `safe-unknown-boundary.md` | Layer D discipline |

#### Tier 3 — Blueprint / reference plane

| Document | Layer |
|----------|-------|
| `workspaces/website-factory-reference-v1/production-qa/` | VL1, VL2, VL6 architectural gates |
| `page-blueprint-qa-checklist-v0.md` | VL1 |
| `reference-v1/generation-contracts/GENERATION-GATES-v1.md` | Upstream VL1 |

#### Tier 4 — Empirical + operational

| Document | Role |
|----------|------|
| `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md` | Empirical gap proof; failure register |
| `FP-0002-*-lesson-v1.md` | Promoted discipline |
| `failures/asset-identity-collision-v1.md` | VL3b failure class |
| `workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md` | VL0 context SoT |
| `governance/P0-VISUAL-GATES-v1.md` | Cross-program VL5–VL6 |
| `agents/mars-forge/qa-checklist.md` | Extended human depth (Tier 3) |

#### Tier 5 — New architecture artifacts (WF-A02 implementation targets)

| Artifact | Purpose |
|----------|---------|
| **Validation Architecture charter** (this design → implementation) | Canonical VL0–VL6 + evidence model |
| Mode validation matrix (single table) | Gate × mode × STOP |
| False-green closure spec | Build log → BUILT wire |
| PIXEL / TEMPLATE layer checklists | Routable operator paths |
| `section-NN.lock.json` SSOT spec | VL3d machine contract |
| Validation token registry (FAIL-* → layer) | FP-0002 integration |

---

## Risks

| Risk | Severity | Mitigation in architecture |
|------|----------|----------------------------|
| **False-green persists** | Critical | VL4/VL5 boundary; BUILT-only build log; E3 required for VERIFIED |
| **Governance without unified layer map** | Critical | VL0–VL6 single charter; operational-qa-entry pointer |
| **VL3 gaps ungated** | Critical | Instance/Asset/Ordering/Text Lock as explicit sub-layers |
| **Operators skip VERIFIED** | High | Evidence bundle checklist; PARTIAL blocks VERIFIED |
| **Mode router documentation-only** | High | VL0 STOP; matrix in charter |
| **WF-A02 scope creep → WF-A03** | High | Explicit non-goals: no vision runtime, no CI SaaS |
| **Governance fatigue (80+ docs)** | Medium | Single entry map; proportional Forge Lite path |
| **Doctrine vs operations drift** | Medium | Passport SoT; reference-v1 crosswalk |
| **Agent mythology (Validator exists)** | Medium | Roles = domains; agents = planned |
| **Context truncation at scale** | High | Staged VL3–VL4; max 2–3 sections/run |

---

## SAFE UNKNOWN

| Item | Status | What would verify |
|------|--------|-----------------|
| Operator adoption of Layer F post–WF-A01 | **SAFE UNKNOWN** | Sample audit of FP-* REPORTs |
| Project-local FIG diff scripts | **SAFE UNKNOWN** | WF-A02 tooling template + pilot |
| `section-NN.lock.json` first adoption | **SAFE UNKNOWN** | First PIXEL project using locks |
| reference-v1 production-qa ↔ mars-website-factory pack alignment | **SAFE UNKNOWN** | Consolidation crosswalk |
| OCPilot SITE-001 ↔ production mode | **SAFE UNKNOWN** | Dedicated crosswalk doc |
| Hybrid `page_mode_map` validation | **Design only** | Pilot on mixed-scope project |
| Automated visual diff (Percy/Chromatic/Playwright) | **Per-project** | Project CI charter |
| Build log migration to BUILT vocabulary | **Not started** | WF-A02 wire spec + workspace script |
| Full AI Website Factory Research in repo | **SAFE UNKNOWN** | Canonical copy |
| FP-0002 ROC enrollment | **Pending** | LOC-ZONE catalog update |

---

## Recommended WF-A02 Scope

Architecture design complete. **Implementation pass** (documentation integration — not runtime) should follow priorities below.

### Priority A — mandatory

1. **Validation Architecture charter** — canonical VL0–VL6 doc derived from this design; single operator entry.
2. **False-green closure spec** — build log vocabulary (BUILT only); pre-REPORT mandatory checklist; migration table enforcement narrative.
3. **Mode validation matrix** — one table: gate × `PIXEL_PERFECT` × `TEMPLATE_ART` × STOP × layer.
4. **PIXEL_PERFECT validation layer checklist** — VL3a–VL3e + VL5 mapped to existing docs + gaps.
5. **Pre-PRODUCTION-PASS mandatory evidence list** — per mode; closes FAIL-001/018.
6. **Anti-generative-fill validation gate** — VL3 formal STOP semantics (charter §7 operationalization).
7. **Asset Identity validation gate spec** — VL3b manifest shape + brand chain blocking.
8. **operational-qa-entry-v1.md pointer** — Validation Architecture layer map row (single edit when implementation chartered).

### Priority B — desirable

1. **TEMPLATE_ART validation layer checklist** — VL1/VL2/VL5 emphasis path.
2. **Assembly Decision validation** — VL3c bounds.y policy + record shape.
3. **`section-NN.lock.json` SSOT spec** — VL3d machine-readable per-section contract.
4. **Validation evidence model v1** — extend `validation-evidence-model-v0.md` with WF bundles (BUILT/VERIFIED/PROD).
5. **frontend_qa_agent operational_doc_pack** — mode-aware routable checklists (human-operated).
6. **FP-0002 findings → validation token registry** — FAIL-* → VL layer → gate → attribution.
7. **Staged build validation gate** — max 2–3 sections/run in VL4 discipline.
8. **reference-v1 ↔ mars-website-factory consolidation map** — VL1/VL6 gate alignment.

### Priority C — defer (WF-A03 or project-local)

1. Automated vision / CV layer.
2. Pixel QA Runtime / Screenshot Engine / Agent Runtime.
3. Factory-wide CI visual diff SaaS.
4. Validation orchestration engine / LangGraph.
5. Validator Agent **runtime** implementation.
6. ROC enrollment automation.
7. Machine-readable evidence JSON schema **enforcement** (optional adoption only).

---

## Appendix — Reporting plane cross-reference

| Reporting layer | Validation architecture relationship |
|-----------------|--------------------------------------|
| **Layer A** — gate verdict | Output of VL1–VL6 gate executions |
| **Layer B** — sub-check | Granularity within VL5/VL6 checklists |
| **Layer C** — entity status | VL5 completeness; PARTIAL blocks VERIFIED |
| **Layer D** — SAFE UNKNOWN | Evidence gaps across all VL; escalation |
| **Layer E** — operator visual | VL6 mandatory input |
| **Layer F** — BUILT/VERIFIED/PROD PASS | Lifecycle states at VL4/VL5/VL6 boundaries |

---

## Appendix — WF-A03 boundary reminder

Per WF-A01 Pass 01 roadmap: **WF-A03 DEFERRED** until WF-A01 **and** WF-A02 complete.

**Explicit non-goals for WF-A02:** Vision Layer · Visual Diff Layer · Pixel QA Runtime · Screenshot Engine · Agent Runtime.

WF-A02 delivers **architecture + human-operated gate wiring in documentation** — not automation products.

---

**STOP AFTER REPORT** — No implementation. No governance edits. No runtime. No WF-A03.

*End of Validation Architecture design v1 — WF-A02 deliverable.*
