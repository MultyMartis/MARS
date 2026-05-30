# NOVA Tool Reality Model v1

**Status:** design-only — Reality-layer capability vocabulary, not software catalog, not vendor catalog, not application inventory, not agent cards, not staffing, not runtime, not automation  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → NOVA Contract Reality Model v1 → NOVA Workflow Reality Model v1 → NOVA Role Reality Model v1 → **this document**  
**Non-claims:** no agents, no orchestration, no software procurement, no vendor selection, no tool deployment automation, no MCP catalog, no database schema

**Parent Reality artifacts:**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`
- NOVA Decision Reality Model v1 — structural choice domains per `decision_type_code`
- NOVA Contract Reality Model v1 — obligation domains per `contract_type_code`
- NOVA Workflow Reality Model v1 — work structure domains per `workflow_type_code`
- NOVA Role Reality Model v1 — responsibility domains per `role_type_code`

**Evidence base:** Website Factory handoff-collapse, onboarding fragility, and delivery-survivability lessons; ORCA semantic-vs-deployed sync and per-deploy registry discipline; MARS snapshot/rollback/recovery and protected-zone survivability lessons; real-world mobile delivery practices adapted to NOVA

---

## 1. Executive Summary

NOVA Tool Reality Model v1 — **первый capability-domain artifact NOVA после Role Reality**. Он отвечает на вопрос:

> **«Какие capability domains должны существовать, чтобы responsibility domains могли выполнять workflow obligations?»**

Не «какое ПО купить» (Software Catalog), не «какой вендор» (Vendor Catalog), не «какая модель ИИ» (Model Catalog), не «кто нажимает кнопку» (Staffing), не «какой агент» (Agent Cards), не «как автоматизировать» (Automation).

| Элемент | Содержание |
|---------|------------|
| **20 capability families** | `TL_CONTEXT_BINDING` … `TL_PRESERVATION_RECOVERY` + upstream trace capabilities |
| **Canonical tool object** | `tool_type_code` + required reality fields |
| **Tool registry** | 20 rows with definition, source roles/workflows/contracts, outputs, failure modes |
| **Role → Tool mapping** | 18 role domains → primary + secondary capability requirements |
| **Workflow → Tool mapping** | 18 workflow families → capability activation patterns |
| **Lifecycle tool pressure matrix** | Dominant capability domains per `LC_*` stage |
| **Product class tool pressure matrix** | 8 focus classes × capability criticality |
| **Tool weight model** | 5 classes: `TW_LATENT` → `TW_TERMINAL` |
| **Tool state model** | 8 states: `TS_LATENT` → `TS_SUPERSEDED` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |
| **Implementation separation** | Tool Reality vs Software Implementations (generic model only) |

**Ключевое различие:**

| Dimension | Tool Reality (this doc) | Tool Execution (NOT this) |
|-----------|-------------------------|---------------------------|
| **Question** | What capabilities must exist for domains to honor work? | Which software/vendor/agent implements each capability? |
| **Layer** | Reality → Tools (structure) | Software Catalog · Vendor Catalog · Agent Cards · Runtime (future) |
| **Example** | `TL_COUPLING_REGISTRY` = ecosystem truth maintenance capability must exist when `RL_ECOSYSTEM` is `RS_REQUIRED` | Figma, GitHub, internal URL spreadsheet |
| **Output** | Vocabulary + role/workflow→capability maps | Licenses, installs, integrations, bots |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answered:** «What must be true?» (`contract_type_code`)  
**Workflow Reality answered:** «How does obligation become structured work?» (`workflow_type_code`)  
**Role Reality answered:** «What responsibility domains must cover that work?» (`role_type_code`)  
**Tool Reality answers:** «What capabilities must exist so domains can produce coverage outputs?» (`tool_type_code`)

Without tool reality, teams select software before knowing which capability gaps they are filling, responsibility domains appear covered because a product is installed, and agents attach to arbitrary apps instead of named capability requirements.

---

## 2. Tool Philosophy

### 2.1 What a tool means inside NOVA

В NOVA **tool** — это **домен capability** (способность), который:

1. **Существует потому что responsibility domain требует executable surface** — не потому что в стеке уже есть приложение
2. **Implementation-neutral** — описывает *какую способность* нужно обеспечить, не *какой продукт* её реализует
3. **Привязан к role coverage** — каждый `role_type_code` at `RS_REQUIRED`+ требует named `tool_type_code` availability or explicit SAFE UNKNOWN
4. **Производит capability outputs** — evidence, truth surfaces, coordination artifacts, preservation bundles — не «login to Jira»
5. **Отделён от occupants** — human, team, agent may *use* implementations later; capability domain exists first

Tool — **не приложение**. «Cursor» — implementation artifact. `TL_ARTIFACT_LINEAGE` — capability for build/deliverable custody and traceability.

**Website Factory lesson:** handoff collapse = `RL_OPERATIONS` domain could be «covered» by people, but **`TL_SURVIVABILITY_POSTURE` capability absent** — no runbook surface, no onboarding truth, no delivery evidence chain ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)).

**ORCA lesson:** URL registry desync = `TL_COUPLING_REGISTRY` treated as one-time export, not **standing coupling-truth capability** re-required per deploy ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

**MARS lesson:** transition without snapshot = `TL_PRESERVATION_RECOVERY` capability not structurally available before lifecycle move ([`snapshot-manifest-standard-v1.md`](../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)).

### 2.2 Why tools exist

Roles **определяют домены ответственности**. Без tool layer ответственность остаётся:

- claimed because software exists;
- fragmented across duplicate apps with overlapping capability;
- impossible to verify — no named capability output;
- blocked when domain is `RS_REQUIRED` but no capability surface exists to produce coverage evidence.

Tool **переводит responsibility coverage в capability requirement** — без выбора вендора и без назначения агента.

| Role says | Tool crystallizes |
|-----------|-------------------|
| `RL_COMPLIANCE` must cover alignment outputs | `TL_REGULATORY_EVIDENCE` capability must be available |
| `RL_OPERATIONS` must cover survivability before Production | `TL_SURVIVABILITY_POSTURE` capability must be available |
| `RL_VALIDATION` cross-cuts verification | `TL_VERIFICATION_EVIDENCE` capability must be available |
| `RL_ECOSYSTEM` must cover coupling per deploy | `TL_COUPLING_REGISTRY` capability must be re-available |

### 2.3 Why tools come after roles

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random capability labels |
| **Lifecycle** | Stage-appropriate capability depth | Full ops capability pack at Concept |
| **Decisions** | Choice domains | Capabilities for unchosen problems |
| **Contracts** | Obligation structure | Capabilities without obligation trace |
| **Workflow** | Work structure | Tools attached to arbitrary tasks |
| **Roles** | Responsibility domains | Software selected before coverage gaps known |
| **Tools** | Capability vocabulary | Agents automate wrong surfaces |

**Tools без Role Reality** — stack theater:

- «We have Jira» before knowing `RL_VALIDATION` verification depth
- Figma license before `RL_UX` / `WF_UX_JOURNEY` scope defined
- AI assistant before `RL_TRUST_SAFETY` domain pressure mapped

Roles **не исполняются** инструментами — они определяют *какую ответственность* нужно покрыть. Tools **определяют какие способности** должны быть доступны, чтобы домен мог произвести coverage outputs.

### 2.4 Why tools are not software products

| Tool Reality | Software / Vendor (NOT this) |
|--------------|------------------------------|
| **What capability** domain requires | **Which product** implements it |
| `TL_RELEASE_COORDINATION` = distribution truth coordination capability | App Store Connect, Play Console, internal release dashboard |
| Survives vendor swap | Resets when license changes |
| One capability; many possible implementations | One app ≠ one capability |
| Vendor-neutral vocabulary | Procurement and install records |

**Boundary test:** If you remove all installed applications and vendor contracts, do capability requirements still make sense? **Yes** → tool. **No** → implementation artifact.

Examples:

| Artifact | Layer |
|----------|-------|
| «Coupling registry truth must be maintainable per external deploy» | `TL_COUPLING_REGISTRY` — tool |
| «We use Notion for docs» | Software Implementation — not tool |
| «Verification evidence must be producible at V2 for CTR_COMPLIANCE» | `TL_VERIFICATION_EVIDENCE` — tool |
| «QA uses TestRail» | Software Implementation — not tool |
| «Snapshot before Production transition» | `TL_PRESERVATION_RECOVERY` — tool |
| «GitHub Actions runs deploy» | Automation + Implementation — not tool family |

### 2.5 What transforms responsibility domains into executable capability?

**Transformation chain (conceptual):**

```text
role_type_code + role_state_code + effective_weight_class (RW_*)
    ↓ requires capability availability
tool_type_code + tool_weight_class + tool_state_code
    ↓ satisfied by (future Implementation layer — NOT v1)
implementation_binding[] producing capability_outputs[]
```

**Transformers (this layer only):**

1. **Role activation** — which `role_type_code` is `RS_REQUIRED`+ for current workflow/lifecycle
2. **Coverage depth** — `RW_STRUCTURAL`+ domains require non-`TS_LATENT` tool capabilities
3. **Cross-cutting overlay** — `RL_VALIDATION` always requires `TL_VERIFICATION_EVIDENCE` when any alignment role is `RS_REQUIRED`
4. **Upstream trace** — `TL_DECISION_TRACE` and `TL_OBLIGATION_TRACE` required when decision/contract-backed work is active at `WW_COORDINATED`+
5. **Lifecycle/class depth** — same `tool_type_code`; weight and dominance vary by context

**What tool adds beyond role:**

| Role provides | Tool adds |
|---------------|-----------|
| Responsibility domain and accountability surface | **Capability requirement** — what must be *possible* to produce outputs |
| Expected coverage outputs | **Capability output categories** — evidence/truth/coordination types |
| `RS_VACANT` signal | **Capability gap** — which `tool_type_code` is unavailable or fragmented |
| Actor-neutral domain | **Implementation-neutral capability** — swappable machinery later |

**NOT transformers in v1:** software SKU, vendor ID, agent_ref, API key, license seat, automation trigger.

---

## 3. Tool Taxonomy

### 3.1 Derivation rationale

Test for each candidate capability family: *«Does NOVA treat capability availability, output producibility, and failure impact differently if this tool type is absent when its source role is `RS_REQUIRED` and source workflow is `WS_ACTIVATED`+?»*

**Rejected as standalone tool families:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Cursor / ChatGPT / Claude** | Implementation products | Software Implementations §16 |
| **GitHub / GitLab** | Repository host | Implementation of `TL_ARTIFACT_LINEAGE` |
| **Figma** | Design host | Implementation of `TL_EXPERIENCE_MODELING` |
| **Jira / Linear** | Issue tracker | May assist workflows; not capability family |
| **Slack** | Communication channel | Staffing/execution — not capability |
| **Employee** | Human actor | Staffing |
| **Agent** | Execution actor | Agents layer (future) |
| **Team** | Group | Staffing |
| **Runtime** | Execution environment | Runtime layer (future) |
| **Meeting** | Process container | Workflow execution |
| **Template file** | Expression format | Templates (future) |
| **Approval button** | Authority act | Approvals (future) |

**Design choice:** **20 capability families** — 18 aligned to workflow/role density for clean derivation, plus **2 upstream trace capabilities** (`TL_DECISION_TRACE`, `TL_OBLIGATION_TRACE`) because capability without decision/contract trace reproduces Website Factory classification drift and ORCA semantic/deployed split.

### 3.2 Capability layers overview

```text
Trace layer:         TL_DECISION_TRACE · TL_OBLIGATION_TRACE
Attention layer:     TL_CONTEXT_BINDING
Identity layer:      TL_IDENTITY_STEWARDSHIP · TL_CLASS_REGISTRY
Boundary layer:      TL_BOUNDARY_STEWARDSHIP · TL_EXPERIENCE_MODELING
Commitment layer:    TL_STRUCTURE_DEFINITION · TL_DATA_TRUTH · TL_REGULATORY_EVIDENCE
                     TL_COMMERCIAL_TRUTH · TL_SAFETY_ASSESSMENT
Execution layer:     TL_ARTIFACT_LINEAGE
Verification layer:  TL_VERIFICATION_EVIDENCE
Operational layer:   TL_SURVIVABILITY_POSTURE · TL_RELEASE_COORDINATION · TL_COUPLING_REGISTRY
Temporal layer:      TL_LIFECYCLE_TRUTH · TL_EXPANSION_CHARTER · TL_INVESTMENT_POSTURE · TL_SUNSET_EXECUTION
Corrective layer:    TL_PRESERVATION_RECOVERY
```

### 3.3 Domain definitions (taxonomy)

#### `TL_DECISION_TRACE`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain traceable surfaces linking work and outputs to `decision_type_code` domains |
| **Source roles** | All domains at `RW_STRUCTURAL`+; especially `RL_LIFECYCLE`, `RL_PRODUCT`, `RL_CHARTER` |
| **Source workflows** | Any `WF_*` at `WW_COORDINATED`+ with decision-backed contracts |
| **Responsibility coverage** | Prevents execution without named choice context |

---

#### `TL_OBLIGATION_TRACE`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain traceable surfaces linking work and outputs to `contract_type_code` obligations |
| **Source roles** | All alignment domains; `RL_VALIDATION` |
| **Source workflows** | All `WF_*` alignment families |
| **Responsibility coverage** | Prevents work without obligation context (workflow theater) |

---

#### `TL_CONTEXT_BINDING`

| Field | Value |
|-------|-------|
| **Purpose** | Bind product instance to NOVA reality context at portfolio entry |
| **Source roles** | `RL_INTAKE` |
| **Source workflows** | `WF_INTAKE` |
| **Responsibility coverage** | Intake honesty; lifecycle label; continue/hold/kill evidence |

---

#### `TL_IDENTITY_STEWARDSHIP`

| Field | Value |
|-------|-------|
| **Purpose** | Steward product identity, value hypothesis, and audience truth surfaces |
| **Source roles** | `RL_PRODUCT` |
| **Source workflows** | `WF_DEFINITION` |
| **Responsibility coverage** | Identity alignment; pivot trace; semantic intent truth (ORCA) |

---

#### `TL_CLASS_REGISTRY`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain authoritative `product_class_code` binding and tier modifiers |
| **Source roles** | `RL_CLASSIFICATION` |
| **Source workflows** | `WF_CLASSIFICATION` |
| **Responsibility coverage** | Class honesty; re-classification on tier/feature triggers |

---

#### `TL_BOUNDARY_STEWARDSHIP`

| Field | Value |
|-------|-------|
| **Purpose** | Steward scope charter and boundary verification surfaces |
| **Source roles** | `RL_CHARTER` |
| **Source workflows** | `WF_CHARTER` |
| **Responsibility coverage** | Scope anti-creep; build constraint truth |

---

#### `TL_EXPERIENCE_MODELING`

| Field | Value |
|-------|-------|
| **Purpose** | Articulate and maintain journey/experience truth for implementation constraint |
| **Source roles** | `RL_UX` |
| **Source workflows** | `WF_UX_JOURNEY` |
| **Responsibility coverage** | Journey architecture; UX alignment evidence |

---

#### `TL_STRUCTURE_DEFINITION`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain technical structure truth: components, dependencies, constraints |
| **Source roles** | `RL_ARCHITECTURE` |
| **Source workflows** | `WF_ARCHITECTURE` |
| **Responsibility coverage** | Architecture alignment; scale/AI console structure |

---

#### `TL_ARTIFACT_LINEAGE`

| Field | Value |
|-------|-------|
| **Purpose** | Custody and lineage of build/deliverable artifacts — source authority, not IDE brand |
| **Source roles** | `RL_IMPLEMENTATION` |
| **Source workflows** | `WF_BUILD` |
| **Responsibility coverage** | Deliverable traceability; reproducible build truth |

---

#### `TL_VERIFICATION_EVIDENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Produce and steward independent verification evidence at target V-level |
| **Source roles** | `RL_VALIDATION` (cross-cutting) |
| **Source workflows** | `WF_VALIDATION`; overlays all alignment `WF_*` |
| **Responsibility coverage** | Verification coverage; anti-fake-completion |

---

#### `TL_DATA_TRUTH`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain data inventory, flows, retention, and privacy alignment surfaces |
| **Source roles** | `RL_DATA_PRIVACY` |
| **Source workflows** | `WF_DATA_ALIGNMENT` |
| **Responsibility coverage** | PII/regulated data truth |

---

#### `TL_REGULATORY_EVIDENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain regulatory/store/category alignment evidence surfaces |
| **Source roles** | `RL_COMPLIANCE` |
| **Source workflows** | `WF_COMPLIANCE_ALIGNMENT` |
| **Responsibility coverage** | Compliance alignment producibility |

---

#### `TL_COMMERCIAL_TRUTH`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain monetization, pricing, and payment-alignment truth surfaces |
| **Source roles** | `RL_COMMERCIAL` |
| **Source workflows** | `WF_COMMERCIAL_ALIGNMENT` |
| **Responsibility coverage** | Real-money alignment evidence |

---

#### `TL_SAFETY_ASSESSMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain trust/safety evaluation and harm-mitigation evidence surfaces |
| **Source roles** | `RL_TRUST_SAFETY` |
| **Source workflows** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **Responsibility coverage** | AI/marketplace/live-user safety evidence |

---

#### `TL_SURVIVABILITY_POSTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain ops readiness: handoff, onboarding, runbooks, deployment assumptions, continuity |
| **Source roles** | `RL_OPERATIONS` |
| **Source workflows** | `WF_OPERATIONS_READINESS` |
| **Responsibility coverage** | Delivery survivability; handoff-collapse prevention |

---

#### `TL_RELEASE_COORDINATION`

| Field | Value |
|-------|-------|
| **Purpose** | Coordinate distribution truth: channels, rollout posture, store metadata alignment |
| **Source roles** | `RL_RELEASE` |
| **Source workflows** | `WF_RELEASE` |
| **Responsibility coverage** | Release vs lifecycle-transition separation |

---

#### `TL_COUPLING_REGISTRY`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain ecosystem coupling truth: URLs, occupants, semantic↔deployed mapping |
| **Source roles** | `RL_ECOSYSTEM` |
| **Source workflows** | `WF_ECOSYSTEM_SYNC` |
| **Responsibility coverage** | Per-deploy registry discipline (ORCA) |

---

#### `TL_LIFECYCLE_TRUTH`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain lifecycle stage truth and transition evidence bundles |
| **Source roles** | `RL_LIFECYCLE` |
| **Source workflows** | `WF_LIFECYCLE_TRANSITION` |
| **Responsibility coverage** | Stage claims; hold/regress/kill honesty |

---

#### `TL_EXPANSION_CHARTER`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain growth charter surfaces: feature/geo/segment expansion truth |
| **Source roles** | `RL_EXPANSION` |
| **Source workflows** | `WF_EXPANSION` |
| **Responsibility coverage** | Expansion within charter; geo compliance triggers |

---

#### `TL_INVESTMENT_POSTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain portfolio investment posture evidence: maintain/harvest/legacy |
| **Source roles** | `RL_INVESTMENT` |
| **Source workflows** | `WF_INVESTMENT_REVIEW` |
| **Responsibility coverage** | Investment honesty; maintenance scope |

---

#### `TL_SUNSET_EXECUTION`

| Field | Value |
|-------|-------|
| **Purpose** | Maintain end-of-life execution surfaces: migration, export, decommission evidence |
| **Source roles** | `RL_SUNSET` |
| **Source workflows** | `WF_SUNSET` |
| **Responsibility coverage** | Terminal path evidence |

---

#### `TL_PRESERVATION_RECOVERY`

| Field | Value |
|-------|-------|
| **Purpose** | Preserve recoverable state: snapshot, rollback, quarantine, restore evidence |
| **Source roles** | `RL_RECOVERY` |
| **Source workflows** | `WF_RECOVERY` |
| **Responsibility coverage** | Corrective retreat; MARS snapshot discipline |

---

## 4. Tool Object Model

Canonical tool object describes **a capability domain type in context**, not a software license or install record. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`, `contract_type_code`, `workflow_type_code`, `role_type_code`.

### 4.1 Core identifier

**`tool_type_code`** — immutable registry key; one of 20 capability codes in §3 and §5.

### 4.2 Required fields (reality model)

```text
tool_reality_object {
  // Identity
  tool_type_code                    // required — e.g. TL_COUPLING_REGISTRY
  capability_domain_layer           // required — trace | attention | identity | boundary |
                                    //            commitment | execution | verification |
                                    //            operational | temporal | corrective

  // Definition
  capability_subject                // required — short noun phrase: what ability exists
  capability_purpose_statement      // required — canonical requirement form (not product name)

  // Role binding (conceptual — not storage)
  source_role_type_codes[]          // required — which roles require this capability when RS_REQUIRED+
  source_workflow_type_codes[]      // required — which workflows activate capability pressure
  source_contract_type_codes[]      // required — upstream obligations capability supports
  source_decision_type_codes[]      // optional — decisions requiring trace via TL_DECISION_TRACE
  lifecycle_state_codes[]           // required — stages where capability is structurally required
  product_class_affinity[]          // required — classes where criticality elevates

  // Classification
  default_weight_class              // required — TW_* (see §10)
  default_dominance_posture         // required — CP_* (see §4.3)

  // Capability model (descriptive only)
  capability_obligations[]          // required — what outputs capability must enable
  prerequisite_tool_type_codes[]    // required — upstream capabilities at TS_AVAILABLE or TS_DORMANT
  expected_capability_outputs[]     // required — output categories producible when TS_AVAILABLE
  typical_unavailability_signal     // required — one-line capability-gap indicator

  // Failure surface
  failure_impact_scope              // required — what breaks when capability absent/degraded
  fragmentation_risk_domains[]      // optional — capabilities commonly duplicated in software

  // Boundaries
  is_software_product               // required — always false
  is_vendor                         // required — always false
  is_human                          // required — always false
  is_agent                          // required — always false
  is_runtime                        // required — always false
}
```

### 4.3 Dominance postures (`CP_*`)

| Posture | Code | Meaning |
|---------|------|---------|
| **Dormant** | `CP_DORMANT` | Capability not material at current stage/class |
| **Latent** | `CP_LATENT` | Capability exists structurally; low pressure |
| **Required** | `CP_REQUIRED` | Role `RS_REQUIRED`; capability must become available |
| **Dominant** | `CP_DOMINANT` | Highest capability pressure in context slice |
| **Blocking** | `CP_BLOCKING` | Downstream coverage impossible until capability `TS_AVAILABLE` |

### 4.4 Context instance (conceptual)

```text
nova_tool_context {
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  contract_type_code,
  workflow_type_code,
  role_type_code,
  tool_type_code,
  effective_weight_class,       // TW_*
  tool_state_code,              // TS_*
  capability_depth_expectation  // from role coverage + workflow V-target
}
```

---

## 5. Tool Registry

Full registry rows. **Outputs** = capability output categories (not file paths). **Failures** = capability-domain failures (not vendor outages).

### 5.1 Trace layer

#### `TL_DECISION_TRACE`

| Field | Value |
|-------|-------|
| **code** | `TL_DECISION_TRACE` |
| **definition** | Capability to bind work and artifacts to named decision domains |
| **source role domains** | All at `RW_STRUCTURAL`+ |
| **supported workflows** | All `WF_*` at `WW_COORDINATED`+ |
| **supported contracts** | All `CTR_*` with decision crystallization |
| **expected outputs** | Decision domain references; choice rationale surfaces; supersession markers |
| **common failure patterns** | Execution without `DEC_*` context; classification drift |

---

#### `TL_OBLIGATION_TRACE`

| Field | Value |
|-------|-------|
| **code** | `TL_OBLIGATION_TRACE` |
| **definition** | Capability to bind work and artifacts to named contract obligations |
| **source role domains** | All alignment roles; `RL_VALIDATION` |
| **supported workflows** | All alignment `WF_*` |
| **supported contracts** | All `CTR_*` |
| **expected outputs** | Obligation maps; V-target declarations; pressure rank context |
| **common failure patterns** | Ticket work without `CTR_*`; fake alignment |

---

### 5.2 Attention · Identity · Boundary

#### `TL_CONTEXT_BINDING`

| Field | Value |
|-------|-------|
| **code** | `TL_CONTEXT_BINDING` |
| **definition** | Capability to bind product instance to NOVA reality context |
| **source role domains** | `RL_INTAKE` |
| **supported workflows** | `WF_INTAKE` |
| **supported contracts** | `CTR_EXISTENCE` |
| **expected outputs** | Intake binding record; lifecycle entry label; portfolio context anchor |
| **common failure patterns** | Shadow products without registry binding |

---

#### `TL_IDENTITY_STEWARDSHIP`

| Field | Value |
|-------|-------|
| **code** | `TL_IDENTITY_STEWARDSHIP` |
| **definition** | Capability to steward product identity and audience truth |
| **source role domains** | `RL_PRODUCT` |
| **supported workflows** | `WF_DEFINITION` |
| **supported contracts** | `CTR_PRODUCT`, `CTR_AUDIENCE` |
| **expected outputs** | Identity thesis surfaces; audience alignment evidence; pivot trace |
| **common failure patterns** | Semantic/deployed split (ORCA); ads against wrong intent |

---

#### `TL_CLASS_REGISTRY`

| Field | Value |
|-------|-------|
| **code** | `TL_CLASS_REGISTRY` |
| **definition** | Capability to maintain authoritative class/tier binding |
| **source role domains** | `RL_CLASSIFICATION` |
| **supported workflows** | `WF_CLASSIFICATION` |
| **supported contracts** | `CTR_CLASSIFICATION` |
| **expected outputs** | Class binding record; tier modifier declaration; re-class triggers |
| **common failure patterns** | Universal-site build without class (Website Factory analog) |

---

#### `TL_BOUNDARY_STEWARDSHIP`

| Field | Value |
|-------|-------|
| **code** | `TL_BOUNDARY_STEWARDSHIP` |
| **definition** | Capability to steward scope charter and boundary verification |
| **source role domains** | `RL_CHARTER` |
| **supported workflows** | `WF_CHARTER` |
| **supported contracts** | `CTR_SCOPE` |
| **expected outputs** | Charter truth; boundary checks; waiver markers |
| **common failure patterns** | Build before charter capability available |

---

#### `TL_EXPERIENCE_MODELING`

| Field | Value |
|-------|-------|
| **code** | `TL_EXPERIENCE_MODELING` |
| **definition** | Capability to articulate journey/experience truth for build constraint |
| **source role domains** | `RL_UX` |
| **supported workflows** | `WF_UX_JOURNEY` |
| **supported contracts** | `CTR_UX` |
| **expected outputs** | Journey maps; flow constraints; UX alignment evidence |
| **common failure patterns** | Implementation guesses UX without modeling capability |

---

### 5.3 Commitment · Execution · Verification

#### `TL_STRUCTURE_DEFINITION`

| Field | Value |
|-------|-------|
| **code** | `TL_STRUCTURE_DEFINITION` |
| **definition** | Capability to maintain technical structure truth |
| **source role domains** | `RL_ARCHITECTURE` |
| **supported workflows** | `WF_ARCHITECTURE` |
| **supported contracts** | `CTR_ARCHITECTURE` |
| **expected outputs** | Structure diagrams; dependency truth; constraint registry |
| **common failure patterns** | Tacit architecture only in heads/repos |

---

#### `TL_ARTIFACT_LINEAGE`

| Field | Value |
|-------|-------|
| **code** | `TL_ARTIFACT_LINEAGE` |
| **definition** | Capability for build/deliverable custody and reproducible lineage |
| **source role domains** | `RL_IMPLEMENTATION` |
| **supported workflows** | `WF_BUILD` |
| **supported contracts** | `CTR_SCOPE`, `CTR_ARCHITECTURE` |
| **expected outputs** | Source authority map; build reproducibility evidence; deliverable manifests |
| **common failure patterns** | «Here are the files» without lineage (handoff collapse) |

---

#### `TL_VERIFICATION_EVIDENCE`

| Field | Value |
|-------|-------|
| **code** | `TL_VERIFICATION_EVIDENCE` |
| **definition** | Capability to produce independent verification evidence at V-level |
| **source role domains** | `RL_VALIDATION` |
| **supported workflows** | `WF_VALIDATION`; all alignment workflows |
| **supported contracts** | All `CTR_*` at V1+ |
| **expected outputs** | Test/audit trails; V-level pass/fail bundles; verification scope declarations |
| **common failure patterns** | Ship without verification capability; checklist theater |

---

#### `TL_DATA_TRUTH`

| Field | Value |
|-------|-------|
| **code** | `TL_DATA_TRUTH` |
| **definition** | Capability to maintain data/privacy truth surfaces |
| **source role domains** | `RL_DATA_PRIVACY` |
| **supported workflows** | `WF_DATA_ALIGNMENT` |
| **supported contracts** | `CTR_DATA_PRIVACY` |
| **expected outputs** | Data inventory; flow maps; retention posture evidence |
| **common failure patterns** | PII handling without inventory capability |

---

#### `TL_REGULATORY_EVIDENCE`

| Field | Value |
|-------|-------|
| **code** | `TL_REGULATORY_EVIDENCE` |
| **definition** | Capability to maintain regulatory alignment evidence |
| **source role domains** | `RL_COMPLIANCE` |
| **supported workflows** | `WF_COMPLIANCE_ALIGNMENT` |
| **supported contracts** | `CTR_COMPLIANCE` |
| **expected outputs** | Store category maps; regulatory checklists; alignment attestations |
| **common failure patterns** | Compliance claimed via legal opinion only — no evidence surface |

---

#### `TL_COMMERCIAL_TRUTH`

| Field | Value |
|-------|-------|
| **code** | `TL_COMMERCIAL_TRUTH` |
| **definition** | Capability to maintain commercial/monetization truth |
| **source role domains** | `RL_COMMERCIAL` |
| **supported workflows** | `WF_COMMERCIAL_ALIGNMENT` |
| **supported contracts** | `CTR_COMMERCIAL` |
| **expected outputs** | Pricing truth; payment flow evidence; monetization alignment |
| **common failure patterns** | First payment without commercial capability history |

---

#### `TL_SAFETY_ASSESSMENT`

| Field | Value |
|-------|-------|
| **code** | `TL_SAFETY_ASSESSMENT` |
| **definition** | Capability to maintain trust/safety evaluation evidence |
| **source role domains** | `RL_TRUST_SAFETY` |
| **supported workflows** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **supported contracts** | `CTR_TRUST_SAFETY` |
| **expected outputs** | Harm models; red-team summaries; safety gate evidence |
| **common failure patterns** | Live AI without safety assessment capability |

---

### 5.4 Operational · Temporal · Corrective

#### `TL_SURVIVABILITY_POSTURE`

| Field | Value |
|-------|-------|
| **code** | `TL_SURVIVABILITY_POSTURE` |
| **definition** | Capability to maintain delivery/ops survivability surfaces |
| **source role domains** | `RL_OPERATIONS` |
| **supported workflows** | `WF_OPERATIONS_READINESS` |
| **supported contracts** | `CTR_OPERATIONS` |
| **expected outputs** | Runbooks; onboarding packs; deployment assumptions; handoff chains |
| **common failure patterns** | Delivery-readiness illusion; handoff collapse |

---

#### `TL_RELEASE_COORDINATION`

| Field | Value |
|-------|-------|
| **code** | `TL_RELEASE_COORDINATION` |
| **definition** | Capability to coordinate distribution and rollout truth |
| **source role domains** | `RL_RELEASE` |
| **supported workflows** | `WF_RELEASE` |
| **supported contracts** | `CTR_RELEASE` |
| **expected outputs** | Channel maps; rollout plans; store metadata alignment |
| **common failure patterns** | Store event substituted for lifecycle transition capability |

---

#### `TL_COUPLING_REGISTRY`

| Field | Value |
|-------|-------|
| **code** | `TL_COUPLING_REGISTRY` |
| **definition** | Capability to maintain ecosystem coupling truth per deploy |
| **source role domains** | `RL_ECOSYSTEM` |
| **supported workflows** | `WF_ECOSYSTEM_SYNC` |
| **supported contracts** | `CTR_ECOSYSTEM` |
| **expected outputs** | URL/occupant registry; semantic↔deployed mapping; sync evidence |
| **common failure patterns** | One-time export; registry drift (ORCA) |

---

#### `TL_LIFECYCLE_TRUTH`

| Field | Value |
|-------|-------|
| **code** | `TL_LIFECYCLE_TRUTH` |
| **definition** | Capability to maintain lifecycle stage and transition evidence |
| **source role domains** | `RL_LIFECYCLE` |
| **supported workflows** | `WF_LIFECYCLE_TRANSITION` |
| **supported contracts** | `CTR_LIFECYCLE` |
| **expected outputs** | Stage claims; transition bundles; hold/regress evidence |
| **common failure patterns** | Production claim without lifecycle truth capability |

---

#### `TL_EXPANSION_CHARTER`

| Field | Value |
|-------|-------|
| **code** | `TL_EXPANSION_CHARTER` |
| **definition** | Capability to maintain growth expansion charter surfaces |
| **source role domains** | `RL_EXPANSION` |
| **supported workflows** | `WF_EXPANSION` |
| **supported contracts** | `CTR_EXPANSION` |
| **expected outputs** | Expansion scope; geo triggers; feature charter |
| **common failure patterns** | Geo expansion without compliance capability re-activation |

---

#### `TL_INVESTMENT_POSTURE`

| Field | Value |
|-------|-------|
| **code** | `TL_INVESTMENT_POSTURE` |
| **definition** | Capability to maintain portfolio investment posture evidence |
| **source role domains** | `RL_INVESTMENT` |
| **supported workflows** | `WF_INVESTMENT_REVIEW` |
| **supported contracts** | `CTR_INVESTMENT` |
| **expected outputs** | Maintain/harvest/legacy posture records |
| **common failure patterns** | Legacy products without investment capability |

---

#### `TL_SUNSET_EXECUTION`

| Field | Value |
|-------|-------|
| **code** | `TL_SUNSET_EXECUTION` |
| **definition** | Capability to execute and evidence end-of-life paths |
| **source role domains** | `RL_SUNSET` |
| **supported workflows** | `WF_SUNSET` |
| **supported contracts** | `CTR_SUNSET` |
| **expected outputs** | Migration plans; export evidence; decommission bundles |
| **common failure patterns** | Terminal data actions without sunset capability |

---

#### `TL_PRESERVATION_RECOVERY`

| Field | Value |
|-------|-------|
| **code** | `TL_PRESERVATION_RECOVERY` |
| **definition** | Capability to preserve and recover product state |
| **source role domains** | `RL_RECOVERY` |
| **supported workflows** | `WF_RECOVERY` |
| **supported contracts** | Violation-triggered; `CTR_LIFECYCLE` regress |
| **expected outputs** | Snapshots; rollback evidence; quarantine records |
| **common failure patterns** | No snapshot before transition (MARS) |

---

## 6. Role → Tool Mapping

Core mapping: every `role_type_code` at `RS_REQUIRED`+ **requires** primary capability availability plus cross-cutting trace/verification capabilities.

### 6.1 Primary mapping (1:1 role → tool)

| `role_type_code` | Primary `tool_type_code` | Capability activated |
|------------------|--------------------------|----------------------|
| `RL_INTAKE` | `TL_CONTEXT_BINDING` | Portfolio context binding |
| `RL_PRODUCT` | `TL_IDENTITY_STEWARDSHIP` | Identity/audience truth |
| `RL_CLASSIFICATION` | `TL_CLASS_REGISTRY` | Class/tier binding |
| `RL_CHARTER` | `TL_BOUNDARY_STEWARDSHIP` | Scope charter truth |
| `RL_UX` | `TL_EXPERIENCE_MODELING` | Journey/experience truth |
| `RL_ARCHITECTURE` | `TL_STRUCTURE_DEFINITION` | Technical structure truth |
| `RL_IMPLEMENTATION` | `TL_ARTIFACT_LINEAGE` | Deliverable lineage |
| `RL_VALIDATION` | `TL_VERIFICATION_EVIDENCE` | Verification evidence |
| `RL_DATA_PRIVACY` | `TL_DATA_TRUTH` | Data/privacy truth |
| `RL_COMPLIANCE` | `TL_REGULATORY_EVIDENCE` | Regulatory evidence |
| `RL_COMMERCIAL` | `TL_COMMERCIAL_TRUTH` | Commercial truth |
| `RL_TRUST_SAFETY` | `TL_SAFETY_ASSESSMENT` | Safety assessment |
| `RL_OPERATIONS` | `TL_SURVIVABILITY_POSTURE` | Survivability surfaces |
| `RL_RELEASE` | `TL_RELEASE_COORDINATION` | Release coordination |
| `RL_ECOSYSTEM` | `TL_COUPLING_REGISTRY` | Coupling registry |
| `RL_LIFECYCLE` | `TL_LIFECYCLE_TRUTH` | Lifecycle truth |
| `RL_EXPANSION` | `TL_EXPANSION_CHARTER` | Expansion charter |
| `RL_INVESTMENT` | `TL_INVESTMENT_POSTURE` | Investment posture |
| `RL_SUNSET` | `TL_SUNSET_EXECUTION` | Sunset execution |
| `RL_RECOVERY` | `TL_PRESERVATION_RECOVERY` | Preservation/recovery |

### 6.2 Secondary capability activations

| Trigger role / condition | Also requires `tool_type_code` | Condition |
|--------------------------|-------------------------------|-----------|
| Any `RL_*` at `RW_STRUCTURAL`+ | `TL_DECISION_TRACE` | Decision-backed work |
| Any alignment `RL_*` at `RS_REQUIRED` | `TL_OBLIGATION_TRACE` | Contract-backed alignment |
| Any `RL_*` at `RW_COORDINATED`+ (via workflow) | `TL_VERIFICATION_EVIDENCE` | V-target expected |
| `RL_IMPLEMENTATION` at Proof+ | `TL_BOUNDARY_STEWARDSHIP` | Charter constraint |
| `RL_LIFECYCLE` Production transition | `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE`, `TL_RELEASE_COORDINATION` | Full capability set |
| `RL_ECOSYSTEM` per deploy | `TL_COUPLING_REGISTRY` re-required | ORCA discipline |
| `RL_EXPANSION` + geo | `TL_REGULATORY_EVIDENCE`, `TL_DATA_TRUTH` | Jurisdiction |
| `RL_SUNSET` | `TL_DATA_TRUTH`, `TL_REGULATORY_EVIDENCE` | Terminal obligations |
| Any `RW_CRITICAL`+ breach | `TL_PRESERVATION_RECOVERY` | Corrective capability |

### 6.3 Role weight → tool weight elevation

| Role weight | Typical tool weight | Notes |
|-------------|----------------------|-------|
| `RW_SUPPORTING` | `TW_LATENT` or `TW_SUPPORTIVE` | Light capability sufficient |
| `RW_STRUCTURAL` | `TW_OPERATIONAL` or `TW_STRUCTURAL` | Capability must be explicitly available |
| `RW_CRITICAL` | `TW_STRUCTURAL` or `TW_CRITICAL` | Gap = coverage failure |
| `RW_TERMINAL` | `TW_TERMINAL` | Irreversible path capability |

### 6.4 Mapping diagram

```text
RL_INTAKE ──────────────► TL_CONTEXT_BINDING
RL_PRODUCT ─────────────► TL_IDENTITY_STEWARDSHIP
RL_CLASSIFICATION ──────► TL_CLASS_REGISTRY
RL_CHARTER ─────────────► TL_BOUNDARY_STEWARDSHIP ──► TL_ARTIFACT_LINEAGE (constraint)
RL_UX ──────────────────► TL_EXPERIENCE_MODELING ────► TL_ARTIFACT_LINEAGE (constraint)
RL_ARCHITECTURE ────────► TL_STRUCTURE_DEFINITION ───► TL_ARTIFACT_LINEAGE · TL_VERIFICATION_EVIDENCE
RL_IMPLEMENTATION ──────► TL_ARTIFACT_LINEAGE
RL_VALIDATION ──────────► TL_VERIFICATION_EVIDENCE (cross-cutting)
RL_DATA_PRIVACY ────────► TL_DATA_TRUTH
RL_COMPLIANCE ──────────► TL_REGULATORY_EVIDENCE
RL_COMMERCIAL ──────────► TL_COMMERCIAL_TRUTH
RL_TRUST_SAFETY ────────► TL_SAFETY_ASSESSMENT
RL_OPERATIONS ──────────► TL_SURVIVABILITY_POSTURE
RL_RELEASE ─────────────► TL_RELEASE_COORDINATION
RL_ECOSYSTEM ───────────► TL_COUPLING_REGISTRY
RL_LIFECYCLE ───────────► TL_LIFECYCLE_TRUTH
RL_EXPANSION ───────────► TL_EXPANSION_CHARTER
RL_INVESTMENT ──────────► TL_INVESTMENT_POSTURE
RL_SUNSET ──────────────► TL_SUNSET_EXECUTION
RL_RECOVERY ────────────► TL_PRESERVATION_RECOVERY

All RL_* at RW_STRUCTURAL+ ─► TL_DECISION_TRACE · TL_OBLIGATION_TRACE
All alignment RS_REQUIRED ──► TL_VERIFICATION_EVIDENCE
Any RW_CRITICAL+ breach ───► TL_PRESERVATION_RECOVERY
```

### 6.5 Example chain

```text
RL_COMPLIANCE (RS_REQUIRED, RW_CRITICAL)
    ↓ requires capability
TL_REGULATORY_EVIDENCE (TS_REQUIRED, TW_CRITICAL)
    ↓ plus cross-cutting
TL_VERIFICATION_EVIDENCE · TL_OBLIGATION_TRACE · TL_DECISION_TRACE
    ↓ produces (future Implementation layer selects products)
regulatory evidence surfaces + V2 verification bundle traceable to CTR_COMPLIANCE
```

No software names. No agents. Only capability requirement reality.

---

## 7. Workflow → Tool Mapping

Workflow activation **requires** capability set to produce alignment outputs. Often **broader** than 1:1 because trace and verification overlay.

### 7.1 Primary mapping (workflow → primary tool)

| `workflow_type_code` | Primary `tool_type_code` | Notes |
|----------------------|--------------------------|-------|
| `WF_INTAKE` | `TL_CONTEXT_BINDING` | |
| `WF_DEFINITION` | `TL_IDENTITY_STEWARDSHIP` | |
| `WF_CLASSIFICATION` | `TL_CLASS_REGISTRY` | |
| `WF_CHARTER` | `TL_BOUNDARY_STEWARDSHIP` | |
| `WF_UX_JOURNEY` | `TL_EXPERIENCE_MODELING` | |
| `WF_ARCHITECTURE` | `TL_STRUCTURE_DEFINITION` | |
| `WF_BUILD` | `TL_ARTIFACT_LINEAGE` | |
| `WF_VALIDATION` | `TL_VERIFICATION_EVIDENCE` | |
| `WF_DATA_ALIGNMENT` | `TL_DATA_TRUTH` | |
| `WF_COMPLIANCE_ALIGNMENT` | `TL_REGULATORY_EVIDENCE` | |
| `WF_COMMERCIAL_ALIGNMENT` | `TL_COMMERCIAL_TRUTH` | |
| `WF_TRUST_SAFETY_ALIGNMENT` | `TL_SAFETY_ASSESSMENT` | |
| `WF_OPERATIONS_READINESS` | `TL_SURVIVABILITY_POSTURE` | |
| `WF_RELEASE` | `TL_RELEASE_COORDINATION` | |
| `WF_ECOSYSTEM_SYNC` | `TL_COUPLING_REGISTRY` | Per-deploy |
| `WF_LIFECYCLE_TRANSITION` | `TL_LIFECYCLE_TRUTH` | |
| `WF_EXPANSION` | `TL_EXPANSION_CHARTER` | |
| `WF_INVESTMENT_REVIEW` | `TL_INVESTMENT_POSTURE` | |
| `WF_SUNSET` | `TL_SUNSET_EXECUTION` | |
| `WF_RECOVERY` | `TL_PRESERVATION_RECOVERY` | |

### 7.2 Secondary workflow → tool activations

| Trigger workflow | Also requires | Condition |
|------------------|---------------|-----------|
| Any `WF_*` at `WW_COORDINATED`+ | `TL_OBLIGATION_TRACE`, `TL_DECISION_TRACE` | Traceable work |
| Any alignment `WF_*` | `TL_VERIFICATION_EVIDENCE` | V-level |
| `WF_BUILD` at Proof+ | `TL_BOUNDARY_STEWARDSHIP` | Scope lock |
| `WF_LIFECYCLE_TRANSITION` Production | `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE`, `TL_RELEASE_COORDINATION`, `TL_PRESERVATION_RECOVERY` | Transition bundle |
| `WF_ECOSYSTEM_SYNC` + deploy | `TL_COUPLING_REGISTRY` | Re-activation |
| `WF_SUNSET` | `TL_DATA_TRUTH`, `TL_REGULATORY_EVIDENCE` | Terminal |
| Any `WW_CRITICAL`+ violation | `TL_PRESERVATION_RECOVERY` | Mandatory |

---

## 8. Lifecycle Tool Pressure Matrix

**Dominant** = highest capability pressure if unavailable; **Active** = required secondary; **Latent** = low depth; **Dormant** = atypical.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `TL_CONTEXT_BINDING`, `TL_IDENTITY_STEWARDSHIP` | `TL_CLASS_REGISTRY` | `TL_DECISION_TRACE` | `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE` |
| **`LC_DISCOVERY`** | `TL_IDENTITY_STEWARDSHIP`, `TL_CLASS_REGISTRY`, `TL_BOUNDARY_STEWARDSHIP` | `TL_EXPERIENCE_MODELING`, `TL_DATA_TRUTH`, `TL_REGULATORY_EVIDENCE`, `TL_COMMERCIAL_TRUTH`, `TL_SAFETY_ASSESSMENT`, `TL_COUPLING_REGISTRY` | `TL_STRUCTURE_DEFINITION` | `TL_SURVIVABILITY_POSTURE` (full) |
| **`LC_PROOF`** | `TL_BOUNDARY_STEWARDSHIP`, `TL_LIFECYCLE_TRUTH`, `TL_EXPERIENCE_MODELING`, `TL_ARTIFACT_LINEAGE` | `TL_STRUCTURE_DEFINITION`, `TL_VERIFICATION_EVIDENCE`, `TL_IDENTITY_STEWARDSHIP` | `TL_DATA_TRUTH` | `TL_SURVIVABILITY_POSTURE` (full) |
| **`LC_PILOT`** | `TL_LIFECYCLE_TRUTH`, `TL_SURVIVABILITY_POSTURE` (lite), `TL_RELEASE_COORDINATION`, `TL_VERIFICATION_EVIDENCE` | `TL_COMMERCIAL_TRUTH`, `TL_SAFETY_ASSESSMENT`, `TL_REGULATORY_EVIDENCE`, `TL_DATA_TRUTH` | `TL_STRUCTURE_DEFINITION` | `TL_EXPANSION_CHARTER` |
| **`LC_PRODUCTION`** | `TL_LIFECYCLE_TRUTH`, `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE`, `TL_RELEASE_COORDINATION`, `TL_VERIFICATION_EVIDENCE` | `TL_STRUCTURE_DEFINITION`, `TL_DATA_TRUTH`, `TL_COMMERCIAL_TRUTH`, `TL_SAFETY_ASSESSMENT`, `TL_ARTIFACT_LINEAGE` | `TL_EXPANSION_CHARTER` | `TL_SUNSET_EXECUTION` |
| **`LC_GROWTH`** | `TL_EXPANSION_CHARTER`, `TL_LIFECYCLE_TRUTH`, `TL_STRUCTURE_DEFINITION`, `TL_VERIFICATION_EVIDENCE` | `TL_REGULATORY_EVIDENCE`, `TL_COMMERCIAL_TRUTH`, `TL_SAFETY_ASSESSMENT`, `TL_BOUNDARY_STEWARDSHIP` | `TL_EXPERIENCE_MODELING` | `TL_CONTEXT_BINDING` |
| **`LC_MATURE`** | `TL_INVESTMENT_POSTURE`, `TL_LIFECYCLE_TRUTH` | `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE`, `TL_ARTIFACT_LINEAGE` | `TL_EXPANSION_CHARTER` | `TL_IDENTITY_STEWARDSHIP` (major) |
| **`LC_LEGACY`** | `TL_INVESTMENT_POSTURE`, `TL_SUNSET_EXECUTION`, `TL_LIFECYCLE_TRUTH` | `TL_SURVIVABILITY_POSTURE` (minimal), `TL_REGULATORY_EVIDENCE`, `TL_DATA_TRUTH` | `TL_COUPLING_REGISTRY` | `TL_EXPANSION_CHARTER` |
| **`LC_SUNSET`** | `TL_SUNSET_EXECUTION`, `TL_DATA_TRUTH`, `TL_LIFECYCLE_TRUTH` | `TL_REGULATORY_EVIDENCE`, `TL_SURVIVABILITY_POSTURE`, `TL_RELEASE_COORDINATION` | `TL_COUPLING_REGISTRY` | `TL_COMMERCIAL_TRUTH`, `TL_EXPANSION_CHARTER` |
| **`LC_HOLD`** | `TL_CONTEXT_BINDING`, `TL_LIFECYCLE_TRUTH` | All prior-stage capabilities — **staleness review** via `TL_VERIFICATION_EVIDENCE` | — | New `TL_EXPANSION_CHARTER` |

### 8.1 Stage-critical capability questions

| Stage | If only three capabilities must be available |
|-------|-----------------------------------------------|
| `LC_CONCEPT` | `TL_CONTEXT_BINDING` · `TL_IDENTITY_STEWARDSHIP` · `TL_DECISION_TRACE` |
| `LC_DISCOVERY` | `TL_CLASS_REGISTRY` · `TL_IDENTITY_STEWARDSHIP` · `TL_OBLIGATION_TRACE` |
| `LC_PROOF` | `TL_BOUNDARY_STEWARDSHIP` · `TL_ARTIFACT_LINEAGE` · `TL_LIFECYCLE_TRUTH` |
| `LC_PILOT` | `TL_SURVIVABILITY_POSTURE` · `TL_RELEASE_COORDINATION` · `TL_VERIFICATION_EVIDENCE` |
| `LC_PRODUCTION` | `TL_SURVIVABILITY_POSTURE` · `TL_REGULATORY_EVIDENCE` · `TL_RELEASE_COORDINATION` |
| `LC_GROWTH` | `TL_EXPANSION_CHARTER` · `TL_STRUCTURE_DEFINITION` · `TL_REGULATORY_EVIDENCE` |
| `LC_MATURE` | `TL_INVESTMENT_POSTURE` · `TL_SURVIVABILITY_POSTURE` · `TL_VERIFICATION_EVIDENCE` |
| `LC_LEGACY` | `TL_INVESTMENT_POSTURE` · `TL_SUNSET_EXECUTION` · `TL_PRESERVATION_RECOVERY` |
| `LC_SUNSET` | `TL_SUNSET_EXECUTION` · `TL_DATA_TRUTH` · `TL_REGULATORY_EVIDENCE` |

---

## 9. Product Class Tool Pressure Matrix

Criticality: **●** Critical · **◐** Elevated · **○** Standard · **—** Rarely material

| Capability domain | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-------------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `TL_DECISION_TRACE` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `TL_OBLIGATION_TRACE` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `TL_CONTEXT_BINDING` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `TL_IDENTITY_STEWARDSHIP` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `TL_CLASS_REGISTRY` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `TL_BOUNDARY_STEWARDSHIP` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `TL_EXPERIENCE_MODELING` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `TL_STRUCTURE_DEFINITION` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `TL_ARTIFACT_LINEAGE` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `TL_VERIFICATION_EVIDENCE` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `TL_DATA_TRUTH` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `TL_REGULATORY_EVIDENCE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `TL_COMMERCIAL_TRUTH` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `TL_SAFETY_ASSESSMENT` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `TL_SURVIVABILITY_POSTURE` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `TL_RELEASE_COORDINATION` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `TL_COUPLING_REGISTRY` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `TL_LIFECYCLE_TRUTH` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `TL_EXPANSION_CHARTER` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `TL_INVESTMENT_POSTURE` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `TL_SUNSET_EXECUTION` | ◐ | ◐ | ○ | ○ | ● | ● | ● | ● |
| `TL_PRESERVATION_RECOVERY` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |

### 9.1 Class-specific capability amplifications

| Class | Capabilities disproportionately critical |
|-------|----------------------------------------|
| **`COMMERCE`** | `TL_COMMERCIAL_TRUTH`, `TL_SURVIVABILITY_POSTURE`, `TL_EXPERIENCE_MODELING`, `TL_VERIFICATION_EVIDENCE` |
| **`FIELD_OPERATIONS`** | `TL_STRUCTURE_DEFINITION`, `TL_BOUNDARY_STEWARDSHIP`, `TL_DATA_TRUTH`, `TL_PRESERVATION_RECOVERY` |
| **`AI_ASSISTANT`** | `TL_SAFETY_ASSESSMENT`, `TL_DATA_TRUTH`, `TL_REGULATORY_EVIDENCE`, `TL_SURVIVABILITY_POSTURE` |
| **`UTILITY_TOOL`** | `TL_BOUNDARY_STEWARDSHIP`, `TL_CLASS_REGISTRY`; most ○ unless triggers |
| **`MARKETPLACE`** | `TL_SAFETY_ASSESSMENT`, `TL_COMMERCIAL_TRUTH`, `TL_COUPLING_REGISTRY`, `TL_VERIFICATION_EVIDENCE` |
| **`HEALTH_MEDICAL`** | `TL_REGULATORY_EVIDENCE`, `TL_DATA_TRUTH`, `TL_SAFETY_ASSESSMENT`, `TL_VERIFICATION_EVIDENCE` |
| **`FINTECH_WALLET`** | `TL_REGULATORY_EVIDENCE`, `TL_COMMERCIAL_TRUTH`, `TL_STRUCTURE_DEFINITION`, `TL_VERIFICATION_EVIDENCE` |
| **`AI_AGENT_CONSOLE`** | `TL_SAFETY_ASSESSMENT`, `TL_REGULATORY_EVIDENCE`, `TL_STRUCTURE_DEFINITION`, `TL_PRESERVATION_RECOVERY` |

**Tier modifier:** T3+ elevates `TL_STRUCTURE_DEFINITION`, `TL_SURVIVABILITY_POSTURE`, `TL_VERIFICATION_EVIDENCE` to blocking at Production; T4 elevates nearly all alignment capabilities to ●.

---

## 10. Tool Weight Model

Derived from **coverage radius × output producibility × downstream blocking power** — not from license cost or popularity.

### 10.1 Weight classes

#### `TW_LATENT`

| Field | Value |
|-------|-------|
| **Dependency radius** | Single artifact stream; optional |
| **Failure impact** | Confusion; workaround possible |
| **Replacement difficulty** | Low — informal substitutes tolerated |
| **Examples** | `TL_CONTEXT_BINDING` at Concept hypothesis |

---

#### `TW_SUPPORTIVE`

| Field | Value |
|-------|-------|
| **Dependency radius** | Single role/workflow stream |
| **Failure impact** | Slowdown; quality drift |
| **Replacement difficulty** | Low–medium |
| **Examples** | `TL_INVESTMENT_POSTURE` at Mature lite review |

---

#### `TW_OPERATIONAL`

| Field | Value |
|-------|-------|
| **Dependency radius** | Multi-artifact; daily use |
| **Failure impact** | Coverage outputs delayed or partial |
| **Replacement difficulty** | Medium — process friction on swap |
| **Examples** | `TL_EXPERIENCE_MODELING` at Proof; `TL_ARTIFACT_LINEAGE` during build |

---

#### `TW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Dependency radius** | Product-wide truth surfaces |
| **Failure impact** | Role coverage cannot produce defensible outputs |
| **Replacement difficulty** | High — migration of truth surfaces |
| **Examples** | `TL_BOUNDARY_STEWARDSHIP` at Proof exit; `TL_COUPLING_REGISTRY` per-deploy |

---

#### `TW_CRITICAL`

| Field | Value |
|-------|-------|
| **Dependency radius** | Ops/legal/users depend on capability |
| **Failure impact** | Integrity failure at current stage |
| **Replacement difficulty** | High — regulated/ops coupling |
| **Examples** | `TL_REGULATORY_EVIDENCE` Production; `TL_SURVIVABILITY_POSTURE` Production |

---

#### `TW_TERMINAL`

| Field | Value |
|-------|-------|
| **Dependency radius** | Irreversible or impractical to undo |
| **Failure impact** | Permanent harm if capability absent before action |
| **Replacement difficulty** | Very high — terminal path coupling |
| **Examples** | `TL_SUNSET_EXECUTION` decommission; mass deletion paths |

### 10.2 Default weight by tool domain (selected)

| Domain | Default weight | Elevates to `TW_CRITICAL` when |
|--------|----------------|--------------------------------|
| `TL_DECISION_TRACE` | `TW_OPERATIONAL` | `RW_STRUCTURAL`+ roles active |
| `TL_OBLIGATION_TRACE` | `TW_OPERATIONAL` | Any alignment workflow active |
| `TL_VERIFICATION_EVIDENCE` | `TW_STRUCTURAL` | `CW_CRITICAL`+ contracts under test |
| `TL_SURVIVABILITY_POSTURE` | `TW_STRUCTURAL` | Production entry |
| `TL_REGULATORY_EVIDENCE` | `TW_CRITICAL` | Extended classes always |
| `TL_COUPLING_REGISTRY` | `TW_STRUCTURAL` | Deep embed; per-deploy ORCA |
| `TL_PRESERVATION_RECOVERY` | `TW_CRITICAL` | Production rollback; regulated |
| `TL_SUNSET_EXECUTION` | `TW_TERMINAL` | Decommission execution |

---

## 11. Tool State Model

Tool states describe **availability and health of capability domains**, not software uptime, license renewal, or agent status.

### 11.1 State codes

| State | Code | Meaning |
|-------|------|---------|
| **Latent** | `TS_LATENT` | Role/workflow exists; capability not yet structurally required |
| **Required** | `TS_REQUIRED` | Role `RS_REQUIRED`; capability must become available |
| **Available** | `TS_AVAILABLE` | Capability producibly available; outputs can be generated |
| **Constrained** | `TS_CONSTRAINED` | Capability present but blocked by prerequisite capability gap |
| **Degraded** | `TS_DEGRADED` | Capability partially available — outputs incomplete/untrusted |
| **Fragmented** | `TS_FRAGMENTED` | Multiple implementations duplicate/conflict — no single truth surface |
| **Superseded** | `TS_SUPERSEDED` | Lifecycle/decision/workflow change replaced capability pressure |
| **Dormant** | `TS_DORMANT` | Not applicable at current stage/class |

### 11.2 State transition rules (descriptive)

```text
TS_LATENT ──(role RS_REQUIRED+)──► TS_REQUIRED
TS_REQUIRED ──(capability satisfied)──► TS_AVAILABLE
TS_REQUIRED ──(no capability surface)──► remains TS_REQUIRED (gap)
TS_AVAILABLE ──(prerequisite tool unavailable)──► TS_CONSTRAINED
TS_CONSTRAINED ──(prerequisite TS_AVAILABLE)──► TS_AVAILABLE
TS_AVAILABLE ──(partial outputs / stale truth)──► TS_DEGRADED
TS_AVAILABLE ──(duplicate conflicting implementations)──► TS_FRAGMENTED
TS_FRAGMENTED ──(reconciled to single truth surface)──► TS_AVAILABLE
TS_* ──(lifecycle/workflow change)──► TS_SUPERSEDED
TS_* ──(stage/class irrelevant)──► TS_DORMANT
```

### 11.3 Deliberate exclusions

| Rejected state | Reason | Correct layer |
|----------------|--------|---------------|
| **installed** | Software binding | Software Implementations |
| **licensed** | Procurement | Vendor Catalog |
| **running** | Runtime health | Runtime |
| **assigned_to_agent** | Actor binding | Agent Cards |
| **subscribed** | SaaS billing | Vendor Catalog |

### 11.4 Available vs fake availability

**`TS_AVAILABLE` requires:**

1. Named `source_role_type_code` and `source_workflow_type_code`
2. Stated capability depth matching role coverage expectation
3. Producible `expected_capability_outputs[]` — not merely software login exists
4. No unresolved `TS_FRAGMENTED` or `TS_DEGRADED` on prerequisite tools at `TW_STRUCTURAL`+

**Not sufficient for `TS_AVAILABLE`:** tool installed; vendor paid; agent has API access; «we use Notion».

---

## 12. Tool Failure Patterns

Derived from Role Failure Patterns §12, Website Factory drift, ORCA battle, MARS survivability — reframed as **capability domain failures**.

| Pattern | Signal | Root tool failure | Affected capabilities |
|---------|--------|-------------------|----------------------|
| **Software mistaken for capability** | «We have Jira» but no verification outputs | Product substituted for `tool_type_code` | Any |
| **Vendor lock-in as reality** | Cannot swap implementation; capability = vendor | Implementation bound too early | Operational capabilities |
| **Role without capability** | `RS_COVERED` role; all tools `TS_LATENT` | Role→tool mapping missing | Matching `TL_*` |
| **Workflow unsupported** | `WS_IN_PROGRESS`; required `TL_*` unavailable | Workflow→tool gap | Active workflow families |
| **Capability fragmentation** | Three docs systems; conflicting truth | `TS_FRAGMENTED` | Truth/registries |
| **Capability inflation** | Full ops pack for utility T1 | Wrong-depth capabilities | Compliance/survivability |
| **Trace capability absent** | Work without decision/contract trace | `TL_DECISION_TRACE` / `TL_OBLIGATION_TRACE` gap | All coordinated work |
| **Verification capability theater** | Checklist exists; no V-level evidence | `TL_VERIFICATION_EVIDENCE` degraded | Cross-cutting |
| **Handoff capability absent** | Delivery files only | `TL_SURVIVABILITY_POSTURE` unavailable | Website Factory analog |
| **Registry sync once-only** | URL drift post-deploy | `TL_COUPLING_REGISTRY` superseded incorrectly | ORCA |
| **Lineage capability absent** | No source authority | `TL_ARTIFACT_LINEAGE` unavailable | Build/handoff |
| **Preservation capability absent** | Transition without snapshot | `TL_PRESERVATION_RECOVERY` latent | MARS |
| **Release capability confusion** | Store live; lifecycle truth missing | `TL_RELEASE_COORDINATION` without `TL_LIFECYCLE_TRUTH` | Release vs transition |
| **Commercial capability jump** | Payments without commercial truth surface | `TL_COMMERCIAL_TRUTH` never available in Pilot | Commercial |
| **Semantic/deployed split** | Ads vs intent | `TL_IDENTITY_STEWARDSHIP` vs `TL_COUPLING_REGISTRY` desync | ORCA |
| **Agent before capability** | Agent automates missing capability | Agent Cards premature | Agents — out of scope |
| **Automation before capability** | Bot runs broken process | Automation premature | Automation — out of scope |
| **Tool-as-domain-owner** | Software owner = role coverage | Violates AC-R22 analog | Role confusion |
| **Duplicate capability** | Two products same `TL_*` | `TS_FRAGMENTED` | Registries, docs |
| **Fake TS_AVAILABLE** | Login exists; no outputs | Availability theater | `TW_CRITICAL`+ |

---

## 13. Tool Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-T1** | Every `role_type_code` at `RS_REQUIRED`+ must map to available `tool_type_code` or SAFE UNKNOWN | Role without capability |
| **AC-T2** | No `TL_ARTIFACT_LINEAGE` at `TW_STRUCTURAL`+ before `TL_BOUNDARY_STEWARDSHIP` reaches `TS_AVAILABLE` | Build before charter capability |
| **AC-T3** | Extended class: `TL_REGULATORY_EVIDENCE` and `TL_SAFETY_ASSESSMENT` cannot stay `TS_LATENT` past `LC_DISCOVERY` when alignment workflows active | Compliance capability vacuum |
| **AC-T4** | Production claim requires `TL_LIFECYCLE_TRUTH`, `TL_SURVIVABILITY_POSTURE`, `TL_REGULATORY_EVIDENCE` available — not inferred from release tooling | Release = lifecycle confusion |
| **AC-T5** | Same `tool_type_code` at `TW_STRUCTURAL`+ requires lifecycle or tier trigger to re-activate from `TS_SUPERSEDED` | Capability churn |
| **AC-T6** | Software product names cannot substitute for `tool_type_code` | Software-first thinking |
| **AC-T7** | `TL_BOUNDARY_STEWARDSHIP` must reach `TS_AVAILABLE` before `LC_PROOF` build capability claim | Charter capability inflation |
| **AC-T8** | `TW_CRITICAL`+ capabilities must declare output depth before `TS_AVAILABLE` claim | Fake availability |
| **AC-T9** | Pilot with real users requires `TL_SURVIVABILITY_POSTURE` at lite minimum `TS_AVAILABLE` | Handoff capability gap |
| **AC-T10** | Identity pivot requires `TL_LIFECYCLE_TRUTH` + `TL_DECISION_TRACE` refresh | Random pivot without trace |
| **AC-T11** | One primary `tool_type_code` per role domain — no mega-capabilities bundling unrelated roles | Capability inflation |
| **AC-T12** | `TL_CLASS_REGISTRY` re-required on tier bump or payments/PII/regulated feature | Classification capability drift |
| **AC-T13** | Undocumented `TW_CRITICAL`+ capability at `TS_REQUIRED` = SAFE UNKNOWN in REPORT | Silent critical gap |
| **AC-T14** | `UTILITY_TOOL` T1 exempt from commercial/regulatory capabilities until trigger feature | Over-engineering |
| **AC-T15** | Store/public release requires `TL_RELEASE_COORDINATION` + often `TL_LIFECYCLE_TRUTH` | AC-W4/AC-R15 analog |
| **AC-T16** | Vendor name alone cannot satisfy capability — explicit `tool_type_code` | Vendor-first thinking |
| **AC-T17** | Every active `tool_type_code` must trace to `source_role_type_code` and `source_workflow_type_code` | Capability without responsibility |
| **AC-T18** | Duplicate implementations for same `tool_type_code` require reconciliation or `TS_FRAGMENTED` declaration | Duplicate capabilities |
| **AC-T19** | High-risk lifecycle transitions require `TL_PRESERVATION_RECOVERY` available before claim | Preservation absent |
| **AC-T20** | `TL_COUPLING_REGISTRY` must re-enter `TS_REQUIRED` on each external deploy when `WF_ECOSYSTEM_SYNC` active | One-time sync (ORCA) |
| **AC-T21** | No Agent Card may reference capability not in tool registry | Agent Cards before Tool Reality |
| **AC-T22** | No software catalog row without mapped `tool_type_code` | Software catalog before Tool Reality |
| **AC-T23** | `TL_DECISION_TRACE` and `TL_OBLIGATION_TRACE` required for any `WW_COORDINATED`+ workflow | Trace capability absent |
| **AC-T24** | Tool cannot own a `role_type_code` — assists coverage only | Tool-as-domain-owner |

---

## 14. Tool Relationships

### 14.1 Dependency chain

```text
┌─────────────────────────────────────────────────────────────┐
│                    REALITY LAYER (NOVA)                      │
├─────────────────────────────────────────────────────────────┤
│  Production Model v1                                         │
│  Product Taxonomy v1                                         │
│  Product Class Registry v1  ──► product_class_code           │
│  Lifecycle Model v1         ──► lifecycle_state_code         │
│  Decision Reality Model v1  ──► decision_type_code           │
│  Contract Reality Model v1  ──► contract_type_code           │
│  Workflow Reality Model v1  ──► workflow_type_code           │
│  Role Reality Model v1      ──► role_type_code               │
│  Tool Reality Model v1      ──► tool_type_code         ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ capability domains ready for implementation/agent binding
                                ▼
┌─────────────────────────────────────────────────────────────┐
│              SOFTWARE IMPLEMENTATIONS (future)               │
│  Vendor-neutral bindings: capability → product(s)            │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENTS (future)                            │
│  Scoped execution within roles — requires named capabilities   │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
                         Automation (future)
```

### 14.2 Why tools derive from roles (not software)

| Input | Provides | Without it |
|-------|----------|------------|
| **`role_type_code`** | Which responsibility must be coverable | Random app purchases |
| **`role_state_code`** | Whether capability is required now | Perpetual license sprawl |
| **`effective_weight_class` (RW_*)** | How deep capability must go | Feature-rich tools for shallow needs |
| **`source_workflow_type_code`** | Which work outputs capability must enable | Tools detached from work |
| **`tool_type_code`** | The actual capability domain | Stack charts substitute for reality |

**Combined pressure function (conceptual):**

```text
tool_pressure(tool_type_code, product_class_code, lifecycle_state_code, source_role_type_code, source_workflow_type_code, tier)
  → dominance_posture ∈ { dormant, latent, required, dominant, blocking }
  → effective_weight_class
  → tool_state_code
  → capability_depth_expectation
```

### 14.3 Cross-capability dependencies

| Upstream capability | Downstream capabilities constrained |
|---------------------|-------------------------------------|
| `TL_DECISION_TRACE` | All coordinated work |
| `TL_OBLIGATION_TRACE` | All alignment evidence |
| `TL_CLASS_REGISTRY` | Depth selection for all alignment capabilities |
| `TL_BOUNDARY_STEWARDSHIP` | `TL_ARTIFACT_LINEAGE`, `TL_VERIFICATION_EVIDENCE` scope |
| `TL_STRUCTURE_DEFINITION` | `TL_ARTIFACT_LINEAGE`, `TL_EXPANSION_CHARTER` |
| `TL_IDENTITY_STEWARDSHIP` | `TL_EXPERIENCE_MODELING`, `TL_COUPLING_REGISTRY` |
| Alignment `TL_*` | `TL_VERIFICATION_EVIDENCE` at contract V-level |
| `TL_LIFECYCLE_TRUTH` | Re-evaluates dominant capabilities at new stage |
| `TL_PRESERVATION_RECOVERY` | May reset misaligned capabilities to `TS_REQUIRED` |

### 14.4 Workflow → Role → Tool chain

```text
contract_type_code
    ↓ activates
workflow_type_code
    ↓ requires coverage
role_type_code
    ↓ requires capability
tool_type_code
    ↓ implemented by (future — NOT v1)
implementation_binding
```

**Why not Workflow → Tool directly?** Workflow defines *what work exists*; role defines *what responsibility must cover that work*; tool defines *what must be possible* for the domain to produce coverage outputs. Skipping role layer produces capabilities attached to tasks without accountability surfaces — duplicate apps, orphaned evidence, and «tool owner» confusion (AC-R22).

---

## 15. Tool Reality Boundaries

### 15.1 What is NOT a tool (v1)

| Artifact | Layer | Why excluded |
|----------|-------|--------------|
| **Application / SaaS product** | Software Implementations | Brand name ≠ capability class |
| **Vendor / license** | Vendor Catalog | Procurement ≠ reality vocabulary |
| **Employee / contractor** | Staffing | Person ≠ capability |
| **Team / department** | Staffing / Org | Group ≠ capability |
| **Agent / bot** | Agents (future) | Actor ≠ capability |
| **Runtime / hosting** | Runtime (future) | Environment ≠ capability domain |
| **Workflow** | Workflow Reality | Work structure ≠ ability surface |
| **Role** | Role Reality | Responsibility ≠ ability |
| **Contract** | Contract Reality | Obligation ≠ ability |
| **Decision** | Decision Reality | Choice domain ≠ ability |
| **Template** | Templates (future) | Format ≠ capability |
| **Approval** | Approvals (future) | Authority act ≠ capability |
| **Ticket / issue** | Execution tracking | Record ≠ capability family |
| **Meeting** | Execution container | Event ≠ capability |
| **MCP server** | Implementation integration | Integration product ≠ `tool_type_code` |

### 15.2 Boundary tests

| Question | Tool Reality if YES |
|----------|---------------------|
| Removing all software, does the capability requirement still make sense? | Yes |
| Is this primarily a responsibility domain? | No → Role layer |
| Is this primarily structured work? | No → Workflow layer |
| Is this a chosen product to buy/install? | No → Implementation layer |
| Does this execute tasks autonomously? | No → Agent/Automation layer |

### 15.3 Common misuse prevention

| Misuse | Correct handling |
|--------|------------------|
| «Our tool is Figma» | Map Figma → implementation of `TL_EXPERIENCE_MODELING` (future catalog) |
| «DevOps owns operations» | `RL_OPERATIONS` coverage + `TL_SURVIVABILITY_POSTURE` availability |
| «AI agent is our QA tool» | Agent Card (future) scoped to `RL_VALIDATION` using `TL_VERIFICATION_EVIDENCE` |
| «GitHub is source of truth» | Implementation of `TL_ARTIFACT_LINEAGE` — truth rules still NOVA-defined |

---

## 16. Tool Implementation Layer

Explicit separation — **defined generically in v1; populated in future charter only.**

### 16.1 Two-layer model

```text
┌──────────────────────────────┐
│      TOOL REALITY (v1)        │  tool_type_code — capability class
│  Vendor-neutral · stable      │
└──────────────┬───────────────┘
               │ maps_to (future)
               ▼
┌──────────────────────────────┐
│  SOFTWARE IMPLEMENTATIONS     │  implementation_id — NOT in v1
│  Replaceable · time-stamped   │
└──────────────────────────────┘
```

### 16.2 Implementation binding object (future schema sketch)

```text
tool_implementation_binding {
  tool_type_code,              // required — reality key
  implementation_label,        // human label — not vendor truth
  implementation_class,        // e.g. doc_surface | registry | ci_pipeline | design_surface | comms_channel
  satisfies_capability_outputs[], // must ⊆ tool registry expected outputs
  fragmentation_risk,          // low | medium | high
  replacement_difficulty,      // aligns with TW_* 
  effective_from,              // date or lifecycle gate
  effective_until,             // supersession
  notes                        // operational — not governance truth
}
```

### 16.3 Example structure only (NOT a catalog)

| `tool_type_code` | Capability (reality) | Possible implementation classes (generic) |
|------------------|------------------------|---------------------------------------------|
| `TL_VERIFICATION_EVIDENCE` | Independent verification evidence | test harness registry; audit log surface; signed attestation store |
| `TL_COUPLING_REGISTRY` | Ecosystem coupling truth | URL registry file; deploy manifest coupling section; semantic map |
| `TL_SURVIVABILITY_POSTURE` | Ops/handoff survivability | runbook repo; onboarding doc set; delivery evidence chain |
| `TL_ARTIFACT_LINEAGE` | Deliverable custody | VCS; artifact manifest; reproducible build record |
| `TL_EXPERIENCE_MODELING` | Journey truth | design file system; journey spec repository |

**v1 rule:** teams may *use* implementations informally; **governance truth** remains `tool_type_code` availability and output categories — not product brands.

### 16.4 Multi-implementation rules (future)

| Condition | Requirement |
|-----------|-------------|
| Two implementations same `tool_type_code` | Declare `TS_FRAGMENTED` until reconciled |
| Implementation swap | Prove output continuity per `expected_capability_outputs[]` |
| Implementation without `tool_type_code` | Forbidden in formal NOVA REPORT (AC-T22) |

---

## 17. RBM Mapping

### 17.1 Full chain

```text
Reality (Product Model · Taxonomy · Registry · Lifecycle)
    ↓ temporal and identity pressure
Lifecycle (LC_*)
    ↓ choice domains
Decisions (DEC_*)
    ↓ obligations
Contracts (CTR_*)
    ↓ work structure
Workflow (WF_*)
    ↓ responsibility coverage
Roles (RL_*)
    ↓ capability requirement
Tools (TL_*)                    ◄── this document
    ↓ occupant/executor binding (future)
Agents
    ↓ repeated execution (future)
Automation
```

### 17.2 Why Tools come after Roles

| If Tools before Roles | Failure mode |
|----------------------|--------------|
| Buy design suite before `RL_UX` domain defined | Software-first thinking |
| Automate QA before `RL_VALIDATION` scope known | Capability theater |
| Deploy agent before responsibility map | Agent Cards chaos |
| Map GitHub before `RL_IMPLEMENTATION` coverage depth | Lineage confusion |

Roles answer **who must answer for work**. Tools answer **what must be possible** for that answer to be evidenced. Without roles, capabilities float without accountability — exactly the handoff collapse pattern where ops *files* exist but **no domain** required survivability outputs.

### 17.3 Why Agents cannot be designed correctly before Tool Reality

| Agent design needs | Tool Reality provides |
|--------------------|----------------------|
| Bounded scope | Named `tool_type_code` set per role domain |
| Output types | `expected_capability_outputs[]` |
| Failure semantics | `TS_*` states and failure patterns |
| Replacement path | Implementation layer separation |
| Anti-automation-chaos | AC-T21 — no agent without capability registry |

**Without Tool Reality:** agents attach to software brands, duplicate human capabilities, automate missing evidence surfaces, and confuse **execution** with **coverage**.

**Automation (later still):** may only compress capability execution when `TS_AVAILABLE` and outputs are defined — never invent obligations.

### 17.4 Layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | Decision Reality Model v1 | Complete |
| Contracts | Contract Reality Model v1 | Complete |
| Workflow | Workflow Reality Model v1 | Complete |
| Roles | Role Reality Model v1 | Complete |
| **Tools** | **Tool Reality Model v1** | **This document — vocabulary complete** |
| Agents | — | Not started — blocked without Tools |
| Automation | — | Not started — blocked without Agents |

---

## 18. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Software-first regression | High | AC-T6, AC-T16, AC-T22; §15 boundaries |
| Capability fragmentation | High | `TS_FRAGMENTED`; AC-T18; failure patterns §12 |
| 20-family count vs operator fatigue | Medium | Matrices §8–9; pressure snapshots Appendix A |
| Role–tool 1:1 oversimplification | Medium | Secondary activations §6.2; trace/verification overlays |
| Trace capabilities skipped | High | AC-T23; ORCA/Website Factory lessons |
| Fake `TS_AVAILABLE` at scale | High | §11.4; AC-T8 |
| Implementation catalog started early | Medium | §16 explicit future layer; non-claims header |
| Prior foundation files not all in-repo | Medium | Cross-reference existing `projects/nova/foundation/` |
| Tool–role conflation | High | AC-T24; AC-R22 analog |
| Agent/automation pressure | High | §17.3; recommended next step §19 |
| Class matrix oversimplification | Medium | Tier modifier §9.1; SAFE UNKNOWN |
| Governance expansion drift | Medium | No Software/Vendor/Agent catalogs in v1 |

---

## 19. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Optimal count of tool families (20 vs consolidated) | Operator feedback after 2–3 products through NOVA |
| Machine format for `tool_pressure_instance` | Future intake schema |
| Implementation binding ID scheme | First Software Implementation charter (explicitly out of v1) |
| Whether `TL_DECISION_TRACE` and `TL_OBLIGATION_TRACE` merge in v2 | Cross-product trace discipline review |
| Capability output schema per `TL_*` | Future Evidence/Records charter |
| Multi-implementation reconciliation automation | Never claimed in v1 |
| MCP/tooling integration as implementation class | First integration charter after Software layer |
| AI model selection as implementation | Model catalog — explicitly out of scope |
| Overlap with MARS survivability tooling | NOVA ↔ MARS integration charter |
| Exact mapping `TW_*` → procurement priority | First Vendor Catalog charter |
| Whether `TS_DEGRADED` triggers mandatory escalation | First Production incident through NOVA tools |

**Non-claims preserved:** this model does not assert software catalog, vendor catalog, agent cards, staffing, tool deployment automation, runtime health monitoring, MCP registry, or automated capability gap detection.

---

## 20. Recommended Next Step

**Single next artifact:** `NOVA AGENT REALITY MODEL v1` (or phased Agents charter) — first layer **after** Tool Reality, defining:

- agent scope bounded by `role_type_code` + required `tool_type_code` set
- explicit separation from Software Implementations and Staffing
- agent boundary rules preventing agent-as-capability or agent-as-role confusion

**Do not skip to:** Agent Cards registry, Software Catalog, Vendor Catalog, Runtime orchestration, or Automation until Agents charter approved — or human explicitly charters Implementation Catalog as next (still after Tools, parallel to Agents only if human directs).

**Optional parallel (human choice):** update Role Reality Model §19 to mark Tools complete; point to Agents.

**Optional parallel:** commit full NOVA foundation pack under `projects/nova/foundation/`.

---

## Appendix A — Tool Pressure Snapshot template

```markdown
# Tool Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| tool_type_code | dominance_posture | effective_weight | tool_state | source_role | source_workflow |
|----------------|---------------------|------------------|------------|-------------|-----------------|
| TL_CONTEXT_BINDING | | | | | |
| ... | | | | | |

Dominant capabilities this stage:
Required but unavailable (TS_REQUIRED):
Fragmented capabilities (TS_FRAGMENTED):
SAFE UNKNOWN capabilities:
```

---

## Appendix B — Quick reference: `tool_type_code` registry

| Code | One-line capability |
|------|---------------------|
| `TL_DECISION_TRACE` | Bind work to decision domains |
| `TL_OBLIGATION_TRACE` | Bind work to contract obligations |
| `TL_CONTEXT_BINDING` | Bind product to NOVA context |
| `TL_IDENTITY_STEWARDSHIP` | Steward identity/audience truth |
| `TL_CLASS_REGISTRY` | Maintain class/tier binding |
| `TL_BOUNDARY_STEWARDSHIP` | Steward scope charter |
| `TL_EXPERIENCE_MODELING` | Articulate journey truth |
| `TL_STRUCTURE_DEFINITION` | Maintain technical structure truth |
| `TL_ARTIFACT_LINEAGE` | Custody deliverable lineage |
| `TL_VERIFICATION_EVIDENCE` | Produce verification evidence |
| `TL_DATA_TRUTH` | Maintain data/privacy truth |
| `TL_REGULATORY_EVIDENCE` | Maintain regulatory evidence |
| `TL_COMMERCIAL_TRUTH` | Maintain commercial truth |
| `TL_SAFETY_ASSESSMENT` | Maintain safety assessment evidence |
| `TL_SURVIVABILITY_POSTURE` | Maintain ops/handoff survivability |
| `TL_RELEASE_COORDINATION` | Coordinate distribution truth |
| `TL_COUPLING_REGISTRY` | Maintain ecosystem coupling registry |
| `TL_LIFECYCLE_TRUTH` | Maintain lifecycle transition truth |
| `TL_EXPANSION_CHARTER` | Maintain expansion charter |
| `TL_INVESTMENT_POSTURE` | Maintain investment posture evidence |
| `TL_SUNSET_EXECUTION` | Execute sunset evidence paths |
| `TL_PRESERVATION_RECOVERY` | Preserve/recover product state |

---

*End of NOVA Tool Reality Model v1*
