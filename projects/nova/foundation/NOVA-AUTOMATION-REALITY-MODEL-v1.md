# NOVA Automation Reality Model v1

**Status:** design-only — Reality-layer execution-compression vocabulary, not runtime, not orchestration, not workflow engine, not n8n, not infrastructure, not deployment, not automation engine  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → NOVA Contract Reality Model v1 → NOVA Workflow Reality Model v1 → NOVA Role Reality Model v1 → NOVA Tool Reality Model v1 → NOVA Agent Reality Model v1 → **this document**  
**Non-claims:** no runtime, no orchestration, no automation engine, no agent cards, no agent registry, no implementation catalog, no deployment design, no infrastructure design, no database schema

**Parent Reality artifacts:**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`
- NOVA Decision Reality Model v1 — structural choice domains per `decision_type_code`
- NOVA Contract Reality Model v1 — obligation domains per `contract_type_code`
- NOVA Workflow Reality Model v1 — work structure domains per `workflow_type_code`
- NOVA Role Reality Model v1 — responsibility domains per `role_type_code`
- NOVA Tool Reality Model v1 — capability domains per `tool_type_code`
- NOVA Agent Reality Model v1 — occupant class domains per `agent_type_code`

**Evidence base:** Website Factory handoff-collapse and automation-before-ops lessons; ORCA semantic-vs-deployed sync and per-deploy registry discipline; MARS snapshot/rollback/recovery and protected-zone survivability lessons; real-world mobile delivery practices adapted to NOVA

---

## 1. Executive Summary

NOVA Automation Reality Model v1 — **финальный vocabulary-layer artifact RBM**. Он отвечает на вопрос:

> **«Какие классы automation compression могут существовать внутри NOVA reality и под какими ограничениями?»**

Не «какой runtime» (Runtime), не «какой orchestrator» (Orchestration), не «какой n8n flow» (Implementation), не «какой cron» (Deployment), не «какой bot в проде» (Agent Cards).

| Элемент | Содержание |
|---------|------------|
| **22 compression families** | `AU_DECISION_TRACE_COMPRESSION` … `AU_PRESERVATION_RECOVERY_COMPRESSION` (20 role-aligned + 2 trace cross-cutting) |
| **Canonical automation object** | `automation_type_code` + required reality fields |
| **Automation registry** | 22 rows with purpose, source agents/workflows/roles/tools, compression surface, failure modes |
| **Agent → Automation mapping** | 22 occupant classes → primary compression domains |
| **Workflow automation matrix** | 18 workflow families × automation suitability |
| **Lifecycle automation pressure matrix** | Dominant compression domains per `LC_*` stage |
| **Product class automation pressure matrix** | 8 focus classes × compression criticality |
| **Automation weight model** | 6 classes: `ATW_LATENT` → `ATW_TERMINAL` |
| **Automation state model** | 8 states: `ATS_LATENT` → `ATS_SUPERSEDED` |
| **Human authority model** | Mandatory boundaries — decision, lifecycle, approval, product authority preserved |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Automation Reality (this doc) | Automation Execution (NOT this) |
|-----------|------------------------------|--------------------------------|
| **Question** | What compression domains may exist because occupant coverage is repeatable? | Which job/cron/workflow-engine runs where? |
| **Layer** | Reality → Automation (structure) | Runtime · Orchestration · Implementation Catalog · Deployments |
| **Example** | `AU_COUPLING_SYNC_COMPRESSION` = compression domain for per-deploy registry parity when `AG_COUPLING_STEWARD` is `AS_ELIGIBLE` | n8n webhook, GitHub Action, scheduled Lambda |
| **Output** | Vocabulary + agent/workflow→compression maps | Schedules, triggers, pipelines, infra bindings |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answered:** «What must be true?» (`contract_type_code`)  
**Workflow Reality answered:** «How does obligation become structured work?» (`workflow_type_code`)  
**Role Reality answered:** «What responsibility domains must cover that work?» (`role_type_code`)  
**Tool Reality answered:** «What capabilities must exist for domains to produce coverage outputs?» (`tool_type_code`)  
**Agent Reality answered:** «What occupant classes may assume coverage within those domains?» (`agent_type_code`)  
**Automation Reality answers:** «What repeatable compression of that coverage may exist without re-opening upstream reality?» (`automation_type_code`)

Without automation reality, teams deploy cron jobs and bots before knowing which occupant behavior is safe to compress, automation substitutes for missing coverage, and **runtime mythology** replaces obligation honor.

**RBM completion:** This document closes the mandatory Reality Before Machinery chain. Nothing beyond Automation Reality is defined here.

---

## 2. Automation Philosophy

### 2.1 What automation means inside NOVA

В NOVA **automation** — это **домен bounded execution compression** (сжатие повторяемого исполнения), который:

1. **Существует потому что occupant coverage structurally repeatable** — не потому что в стеке уже есть cron, CI, или n8n
2. **Implementation-neutral** — описывает *какой класс compression* может существовать, не *какой runtime* его исполняет
3. **Привязан к полной upstream chain** — каждый `automation_type_code` traces to `source_agent_type_code` + `source_workflow_type_code` + `source_role_type_code` + `required_tool_type_codes[]`
4. **Сжимает уже определённое участие** — не создаёт obligations, roles, capabilities, occupant classes, или decisions
5. **Отделён от execution machinery** — Runtime, Orchestration, Deployments may *instantiate* compression later; domain exists first

Automation — **не runtime**. «GitHub Actions runs nightly» — implementation artifact. `AU_VERIFICATION_COMPRESSION` — compression domain that may repeat V-level checks when `AG_VERIFICATION_STEWARD` coverage pattern is proven stable.

**Website Factory lesson:** handoff collapse worsened when **automation-before-ops** compressed delivery artifacts without `AG_SURVIVABILITY_STEWARD` eligibility — files shipped, survivability compression domain never honestly derivable ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)).

**ORCA lesson:** one-time URL export treated as «automated sync» without standing `AU_COUPLING_SYNC_COMPRESSION` derivation from `WF_ECOSYSTEM_SYNC` + `AG_COUPLING_STEWARD` — semantic ≠ deployed drift returned ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

**MARS lesson:** transition without snapshot = `AU_PRESERVATION_RECOVERY_COMPRESSION` latent while humans improvised recovery — compression domain requires proven preservation occupant pattern first ([`snapshot-manifest-standard-v1.md`](../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)).

### 2.2 Why automation exists

Agents **определяют occupant class vocabulary**. Без automation layer eligible occupant coverage остаётся:

- re-executed manually every cycle without naming compression boundary;
- duplicated by ad-hoc scripts without upstream trace;
- expanded into fake autonomy when repeatability unproven;
- substituted for missing human authority at structural weight.

Automation **переводит proven occupant participation в compression vocabulary** — без выбора runtime, orchestrator, или deployment target.

| Agent + Workflow says | Automation crystallizes |
|-------------------------|-------------------------|
| `AG_REGULATORY_STEWARD` + stable `WF_COMPLIANCE_ALIGNMENT` at V2 | `AU_REGULATORY_ALIGNMENT_COMPRESSION` may repeat alignment checks |
| `AG_COUPLING_STEWARD` + `WF_ECOSYSTEM_SYNC` per deploy | `AU_COUPLING_SYNC_COMPRESSION` may repeat registry parity work |
| `AG_VERIFICATION_STEWARD` + cross-cutting `WF_VALIDATION` | `AU_VERIFICATION_COMPRESSION` may repeat evidence collection |
| `AG_SURVIVABILITY_STEWARD` + lite `WF_OPERATIONS_READINESS` | `AU_SURVIVABILITY_COMPRESSION` may repeat handoff checklist surfaces |

### 2.3 Why automation comes after agents

RBM chain (mandatory):

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random compression labels |
| **Lifecycle** | Stage-appropriate compression depth | Full ops automation pack at Concept |
| **Decisions** | Choice domains | Automation for unchosen problems |
| **Contracts** | Obligation structure | Compression without obligation trace |
| **Workflow** | Work structure | Automation attached to arbitrary tasks |
| **Roles** | Responsibility domains | Automation substitutes accountability |
| **Tools** | Capability vocabulary | Automation compresses missing surfaces |
| **Agents** | Occupant class vocabulary | Compression of unbounded occupant |
| **Automation** | Repeatable compression vocabulary | Runtime mythology |

**Automation без Agent Reality** — machinery theater:

- «We automated QA» before `AG_VERIFICATION_STEWARD` + `AS_ELIGIBLE`
- n8n flow before `RL_COMPLIANCE` + `TL_REGULATORY_EVIDENCE` scope
- CI green substituted for `WF_VALIDATION` alignment

Agents **не исполняются** автоматически — они определяют *какие классы occupants* могут покрывать domains. Automation **определяет какие классы compression* могут повторять уже-bound coverage* без re-opening upstream layers.

### 2.4 Why automation is not runtime

| Automation Reality | Runtime (NOT this) |
|--------------------|-------------------|
| **What compression domain** may exist | **Where/how** execution runs |
| `AU_RELEASE_COORDINATION_COMPRESSION` = repeatable rollout-check compression surface | Jenkins, Fastlane, internal deploy service |
| Survives hosting change if derivation chain intact | Resets when infra changes |
| Bounded by agent + role scope | Environment, scaling, health |
| Defines possibility | Defines execution |

**Boundary test:** If you remove all servers, cron, and CI, does the compression taxonomy still make sense given agents and upstream layers? **Yes** → automation reality. **No** → runtime artifact.

### 2.5 Why automation is not orchestration

| Automation Reality | Orchestration (NOT this) |
|--------------------|--------------------------|
| **What may repeat** within bounded scope | **How multiple actors coordinate** across steps |
| One compression domain per derivation chain | Multi-step graphs, fan-out, saga patterns |
| Derived from single agent class primary binding | May span many classes without reality map |
| Authority boundaries explicit | Often hides decision points |
| Precedes orchestration design | Requires named compression domains first |

Orchestration **coordinates** execution machinery. Automation Reality **names** which portions of already-defined coverage may be compressed. Orchestration without automation reality produces **hidden control planes**.

### 2.6 What transforms agent participation into automation potential?

**Transformation chain (conceptual — mandatory order):**

```text
workflow_type_code + workflow_state_code (WS_ALIGNED+)
    ↓ requires stable coverage
role_type_code + role_state_code (RS_COVERED+)
    ↓ requires capability
tool_type_code + tool_state_code (TS_AVAILABLE+)
    ↓ enables occupant
agent_type_code + agent_state_code (AS_ELIGIBLE+)
    ↓ enables compression consideration
automation_type_code + automation_weight_class (ATW_*) + automation_state_code (ATS_*)
    ↓ instantiated by (future Runtime/Implementation layers — NOT v1)
compression_binding producing compressed_coverage_outputs[] within bounds
```

**Transformers (this layer only):**

1. **Repeatability signal** — same coverage output class reproducible under unchanged obligation/workflow context
2. **Upstream stability** — no `WS_SUPERSEDED`, `AS_SUPERSEDED`, `RS_SUPERSEDED` on derivation chain
3. **Eligibility completeness** — agent `AS_ELIGIBLE` + tools `TS_AVAILABLE` + role `RS_COVERED` or `RS_REQUIRED` with explicit human co-coverage where required
4. **Authority exclusion** — compression surface excludes decision acts, lifecycle claims, approvals, product identity binding
5. **Human proof gate** — at `ATW_STRUCTURAL`+, at least one human-validated coverage cycle before `ATS_CANDIDATE` (HITL preservation)
6. **Workflow participation fit** — agent `WP_*` posture compatible with repetition (not all postures compress equally)

**What automation adds beyond agent:**

| Agent provides | Automation adds |
|----------------|-----------------|
| Occupant class — who/what *class* may cover | **Compression class** — what *repeatable portion* of that coverage may compress |
| Coverage participation posture (`WP_*`) | **Compression trigger posture** (`CTP_*`) — when repetition is structurally valid |
| `AS_ELIGIBLE` signal | **Compression eligibility signal** — `ATS_CANDIDATE` when repeatability proven |
| Bounded execution scope for instances | **Bounded repetition scope** — swappable machinery later, fixed compression boundary now |

**NOT transformers in v1:** cron expression, webhook URL, queue name, orchestration_graph_id, autonomy_level, infra_region.

**Rejected candidate definitions (why each alone is wrong):**

| Candidate | Rejection | Correct placement |
|-----------|-----------|-------------------|
| Automation = Agent Instance | Instance execution, not compression taxonomy | Agent Cards / Runtime |
| Automation = Workflow Engine | Machinery, not reality class | Orchestration / Runtime |
| Automation = Tool | Capability ≠ repetition domain | Tool Reality |
| Automation = Autonomy | Implies decision authority expansion | Forbidden — §12 Human Authority |
| Automation = Orchestration | Coordination graph ≠ compression domain | Orchestration — out of scope |

**Derived definition:** Automation = **bounded execution compression domain** — a named, implementation-neutral category of repeatable coverage participation that may reduce manual re-execution of already-defined occupant behavior within stable workflow obligations, role boundaries, tool capabilities, and agent eligibility — without creating, altering, or substituting upstream reality layers.

---

## 3. Automation Ontology

### 3.1 Derivation rationale

Test for each ontological dimension: *«Does NOVA treat compression eligibility, repetition boundary, and failure impact differently if this dimension is absent when source agent is `AS_ELIGIBLE`, source workflow is `WS_ALIGNED`+, and upstream chain is stable?»*

### 3.2 Primary ontological axes

Automation domains characterized by **six derived axes** — not cron schedules, not CI vendors, not n8n node types:

```text
Compression class    — what category of repeatable coverage reduction (AU_*)
Derivation binding   — full upstream chain: WF → RL → TL → AG
Repetition surface   — which coverage outputs may compress (not all outputs compress)
Authority exclusion  — which acts remain human-only regardless of compression
Stability precondition — upstream alignment required before compression valid
Compression depth    — how much of occupant domain may compress (ATW_*)
```

### 3.3 Ontological dimensions (derived, not assumed)

| Dimension | Code prefix | Meaning | NOT this |
|-----------|-------------|---------|----------|
| **Compression class** | `AU_*` | Named category of repeatable coverage reduction | Cron job instance |
| **Workflow-bound** | `source_workflow_type_code` | Work structure that defines repeatable obligation honor | The workflow engine |
| **Role-bounded** | `source_role_type_code` | Maximum accountability surface compression may touch | The role itself |
| **Capability-mediated** | `required_tool_type_codes[]` | Tools whose outputs compression repeats | The tools themselves |
| **Agent-derived** | `source_agent_type_code` | Occupant class whose proven coverage compresses | Agent card instance |
| **Trigger posture** | `CTP_*` | When repetition structurally valid | Runtime trigger config |
| **Authority firewall** | `AEX_*` | Excluded authority classes | Approval record |

**Rejected as primary ontology:**

| Rejected | Reason |
|----------|--------|
| **Scheduler** | Runtime artifact |
| **Bot** | Agent Card / Runtime |
| **Pipeline** | Implementation |
| **Autonomous agent** | Authority expansion — forbidden |
| **Self-healing system** | Often hides decision making |
| **Workflow engine** | Orchestration — not compression taxonomy |

### 3.4 Ontological composition

Every `automation_type_code` is a **composition**:

```text
automation_domain = compression_class_identity
                  × derivation_binding(WF → RL → TL → AG)
                  × repetition_surface(coverage_output_categories[])
                  × authority_exclusion(AEX_* set)
                  × trigger_posture(default_CTP_*)
                  × weight_class(default_ATW_*)
```

**Example composition:**

```text
AU_COUPLING_SYNC_COMPRESSION =
  compression_class: ecosystem coupling parity repetition
  × derivation: WF_ECOSYSTEM_SYNC → RL_ECOSYSTEM → TL_COUPLING_REGISTRY → AG_COUPLING_STEWARD
  × repetition_surface: [registry_diff, url_parity_check, semantic_deployed_map]
  × authority_exclusion: [AEX_DECISION, AEX_LIFECYCLE, AEX_PRODUCT_IDENTITY]
  × trigger_posture: CTP_EVENT_BOUND (per external deploy)
  × weight: ATW_STRUCTURAL default; ATW_CRITICAL at Production per-deploy
```

### 3.5 What automation fundamentally IS (v1 statement)

> Automation in NOVA is a **bounded execution compression domain** — a named, implementation-neutral category of repeatable coverage participation that may reduce manual re-execution of already-defined occupant behavior within stable workflow obligations, role boundaries, tool capabilities, and agent eligibility.

Automation **does not** create product reality, lifecycle state, decisions, contracts, workflows, roles, tools, or agents. Automation **may** compress proven coverage participation once the full derivation chain is stable and human authority boundaries are preserved.

### 3.6 Four compression primitives (derived sub-ontology)

These are **not** automation families — they describe *how* compression manifests within `AU_*` domains:

| Primitive | Meaning | Example domain |
|-----------|---------|----------------|
| **Execution compression** | Repeat artifact production steps within charter | `AU_ARTIFACT_PRODUCTION_COMPRESSION` |
| **Repeatability amplification** | Repeat same evidence/check cycle | `AU_VERIFICATION_COMPRESSION` |
| **Coordination amplification** | Repeat handoff/sync rituals | `AU_COUPLING_SYNC_COMPRESSION` |
| **Validation amplification** | Repeat alignment probes against obligations | `AU_REGULATORY_ALIGNMENT_COMPRESSION` |

A single `automation_type_code` may combine primitives; families are named by **domain**, not by primitive alone.

---

## 4. Automation Taxonomy

### 4.1 Derivation rationale

Test for each candidate compression family: *«Does NOVA treat compression eligibility, repetition failure, and authority breach differently if this automation type is undefined when its source agent is `AS_ELIGIBLE`, source workflow is `WS_ALIGNED`+, and repeatability is structurally expected?»*

**Derivation formula (mandatory):**

```text
automation_family = f(workflow_obligations, role_domain, tool_capabilities, agent_participation)
```

**NOT derived from:** cron, CI, n8n, Zapier, GitHub Actions, Lambda, Kubernetes, job titles, vendor brands.

**Design choice:** **22 compression families** — 20 aligned to agent+role+tool+workflow chains for clean derivation, plus **2 trace cross-cutting compression classes** mirroring Agent Reality trace layer. Preserves Workflow → Role → Tool → Agent → Automation chain without collapsing automation into agent or runtime.

### 4.2 Compression layers overview

```text
Trace layer:         AU_DECISION_TRACE_COMPRESSION · AU_OBLIGATION_TRACE_COMPRESSION
Attention layer:     AU_CONTEXT_BINDING_COMPRESSION
Identity layer:      AU_IDENTITY_STEWARDSHIP_COMPRESSION · AU_CLASS_REGISTRY_COMPRESSION
Boundary layer:      AU_BOUNDARY_STEWARDSHIP_COMPRESSION · AU_EXPERIENCE_MODELING_COMPRESSION
Commitment layer:    AU_STRUCTURE_DEFINITION_COMPRESSION · AU_DATA_ALIGNMENT_COMPRESSION
                     AU_REGULATORY_ALIGNMENT_COMPRESSION · AU_COMMERCIAL_ALIGNMENT_COMPRESSION
                     AU_SAFETY_ASSESSMENT_COMPRESSION
Execution layer:     AU_ARTIFACT_PRODUCTION_COMPRESSION
Verification layer:  AU_VERIFICATION_COMPRESSION
Operational layer:   AU_SURVIVABILITY_COMPRESSION · AU_RELEASE_COORDINATION_COMPRESSION
                     AU_COUPLING_SYNC_COMPRESSION
Temporal layer:      AU_LIFECYCLE_TRUTH_COMPRESSION · AU_EXPANSION_CHARTER_COMPRESSION
                     AU_INVESTMENT_POSTURE_COMPRESSION · AU_SUNSET_EXECUTION_COMPRESSION
Corrective layer:    AU_PRESERVATION_RECOVERY_COMPRESSION
```

### 4.3 Domain definitions (taxonomy)

#### `AU_DECISION_TRACE_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat decision-trace maintenance outputs when decision context stable |
| **Source agents** | `AG_DECISION_TRACE_STEWARD` |
| **Source workflows** | Any `WF_*` at `WW_COORDINATED`+ with decision-backed contracts |
| **Automation surface** | Rationale binding refresh; supersession flag checks; trace completeness probes |

---

#### `AU_OBLIGATION_TRACE_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat obligation-map maintenance and V-target context binding |
| **Source agents** | `AG_OBLIGATION_TRACE_STEWARD` |
| **Source workflows** | All alignment `WF_*` |
| **Automation surface** | Obligation map diff; contract-workflow linkage checks |

---

#### `AU_CONTEXT_BINDING_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat intake binding validation — not intake authorization |
| **Source agents** | `AG_CONTEXT_BINDER` |
| **Source workflows** | `WF_INTAKE` |
| **Automation surface** | Portfolio anchor checks; lifecycle label consistency |

---

#### `AU_IDENTITY_STEWARDSHIP_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat identity thesis drift checks — not identity decisions |
| **Source agents** | `AG_IDENTITY_STEWARD` |
| **Source workflows** | `WF_DEFINITION` |
| **Automation surface** | Semantic/deployed intent diff (ORCA); audience alignment probes |

---

#### `AU_CLASS_REGISTRY_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat class/tier binding validation — not reclassification |
| **Source agents** | `AG_CLASS_REGISTRAR` |
| **Source workflows** | `WF_CLASSIFICATION` |
| **Automation surface** | Registry consistency checks; tier trigger scans |

---

#### `AU_BOUNDARY_STEWARDSHIP_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat charter boundary probes — not scope decisions |
| **Source agents** | `AG_BOUNDARY_STEWARD` |
| **Source workflows** | `WF_CHARTER` |
| **Automation surface** | Scope creep detection; build-vs-charter diff |

---

#### `AU_EXPERIENCE_MODELING_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat journey consistency checks |
| **Source agents** | `AG_EXPERIENCE_STEWARD` |
| **Source workflows** | `WF_UX_JOURNEY` |
| **Automation surface** | Journey artifact parity; a11y regression probes |

---

#### `AU_STRUCTURE_DEFINITION_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat architecture truth probes — not architecture commits |
| **Source agents** | `AG_STRUCTURE_STEWARD` |
| **Source workflows** | `WF_ARCHITECTURE` |
| **Automation surface** | Dependency boundary scans; stack drift detection |

---

#### `AU_ARTIFACT_PRODUCTION_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat implementation production steps within locked charter |
| **Source agents** | `AG_IMPLEMENTATION_PRODUCER` |
| **Source workflows** | `WF_BUILD` |
| **Automation surface** | Lineage checks; build artifact regeneration within boundary |

---

#### `AU_VERIFICATION_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat verification evidence collection at declared V-level |
| **Source agents** | `AG_VERIFICATION_STEWARD` |
| **Source workflows** | `WF_VALIDATION`; overlays all alignment `WF_*` |
| **Automation surface** | V-level probe runs; alignment/misalignment signal collection |

---

#### `AU_DATA_ALIGNMENT_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat data/privacy alignment checks |
| **Source agents** | `AG_DATA_STEWARD` |
| **Source workflows** | `WF_DATA_ALIGNMENT` |
| **Automation surface** | Retention schedule probes; collection surface scans |

---

#### `AU_REGULATORY_ALIGNMENT_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat regulatory/store alignment probes — not legal approval |
| **Source agents** | `AG_REGULATORY_STEWARD` |
| **Source workflows** | `WF_COMPLIANCE_ALIGNMENT` |
| **Automation surface** | Store category diff; consent model probes |

---

#### `AU_COMMERCIAL_ALIGNMENT_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat monetization path checks — not pricing decisions |
| **Source agents** | `AG_COMMERCIAL_STEWARD` |
| **Source workflows** | `WF_COMMERCIAL_ALIGNMENT` |
| **Automation surface** | Payment path probes; pricing display consistency |

---

#### `AU_SAFETY_ASSESSMENT_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat safety boundary and harm-model probes |
| **Source agents** | `AG_SAFETY_STEWARD` |
| **Source workflows** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **Automation surface** | Autonomy limit scans; escalation path probes |

---

#### `AU_SURVIVABILITY_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat ops/handoff survivability checks — not ops ownership assignment |
| **Source agents** | `AG_SURVIVABILITY_STEWARD` |
| **Source workflows** | `WF_OPERATIONS_READINESS` |
| **Automation surface** | Runbook presence checks; handoff chain probes (Website Factory) |

---

#### `AU_RELEASE_COORDINATION_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat release readiness probes — not release authorization |
| **Source agents** | `AG_RELEASE_STEWARD` |
| **Source workflows** | `WF_RELEASE` |
| **Automation surface** | Channel truth diff; rollback test evidence collection |

---

#### `AU_COUPLING_SYNC_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat ecosystem coupling parity per deploy event |
| **Source agents** | `AG_COUPLING_STEWARD` |
| **Source workflows** | `WF_ECOSYSTEM_SYNC` |
| **Automation surface** | URL/registry diff; semantic↔deployed map (ORCA) |

---

#### `AU_LIFECYCLE_TRUTH_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat lifecycle label honesty probes — not stage transitions |
| **Source agents** | `AG_LIFECYCLE_STEWARD` |
| **Source workflows** | `WF_LIFECYCLE_TRANSITION` |
| **Automation surface** | Stage claim vs evidence bundle diff |

---

#### `AU_EXPANSION_CHARTER_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat expansion scope boundary checks — not expansion authorization |
| **Source agents** | `AG_EXPANSION_STEWARD` |
| **Source workflows** | `WF_EXPANSION` |
| **Automation surface** | Geo/feature charter drift detection |

---

#### `AU_INVESTMENT_POSTURE_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat investment posture signal collection — not portfolio decisions |
| **Source agents** | `AG_INVESTMENT_STEWARD` |
| **Source workflows** | `WF_INVESTMENT_REVIEW` |
| **Automation surface** | Maintain/harvest signal probes |

---

#### `AU_SUNSET_EXECUTION_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat sunset checklist steps — not decommission authorization |
| **Source agents** | `AG_SUNSET_STEWARD` |
| **Source workflows** | `WF_SUNSET` |
| **Automation surface** | Export/decommission step verification |

---

#### `AU_PRESERVATION_RECOVERY_COMPRESSION`

| Field | Value |
|-------|-------|
| **Purpose** | Repeat snapshot/rollback ritual steps — not recovery authorization |
| **Source agents** | `AG_PRESERVATION_STEWARD` |
| **Source workflows** | `WF_RECOVERY` |
| **Automation surface** | Snapshot manifest checks; rollback path probes (MARS) |

---

## 5. Automation Object Model

Canonical automation object describes **a compression class type in context**, not a cron job, pipeline, or orchestration graph. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`, `contract_type_code`, `workflow_type_code`, `role_type_code`, `tool_type_code`, `agent_type_code`.

### 5.1 Core identifier

**`automation_type_code`** — immutable registry key; one of 22 compression codes in §4 and §6.

### 5.2 Required fields (reality model)

```text
automation_reality_object {
  automation_type_code              // required — e.g. AU_COUPLING_SYNC_COMPRESSION
  compression_domain_layer          // required — trace | attention | identity | boundary | commitment | execution | verification | operational | temporal | corrective
  compression_class_subject         // required
  compression_purpose_statement     // required
  source_workflow_type_codes[]      // required
  source_role_type_codes[]          // required
  required_tool_type_codes[]        // required
  source_agent_type_codes[]         // required
  source_contract_type_codes[]      // required
  default_compression_trigger_posture // required — CTP_*
  default_weight_class              // required — ATW_*
  default_dominance_posture         // required — ADP_*
  authority_exclusion_classes[]     // required — AEX_*
  compressible_coverage_outputs[]   // required
  non_compressible_acts[]           // required
  prerequisite_agent_state          // required — typically AS_ELIGIBLE
  prerequisite_workflow_state       // required — typically WS_ALIGNED
  expected_compression_signals[]    // required
  typical_non_compression_signal    // required
  failure_impact_scope              // required
  is_workflow / is_role / is_tool / is_agent / is_runtime / is_orchestration / is_infrastructure / is_deployment  // all false
}
```

### 5.3 Compression trigger postures (`CTP_*`)

| Posture | Code | Meaning |
|---------|------|---------|
| **Manual invoke** | `CTP_MANUAL` | Human-initiated repetition only |
| **Periodic** | `CTP_PERIODIC` | Structural repetition on cadence — not cron config |
| **Event-bound** | `CTP_EVENT_BOUND` | Repetition on named event (deploy, violation) |
| **Continuous probe** | `CTP_CONTINUOUS_PROBE` | Standing alignment checks while workflow active |
| **Advisory-only** | `CTP_ADVISORY` | Signals only; human retains coverage claim |

### 5.4 Dominance postures (`ADP_*`)

| Posture | Code | Meaning |
|---------|------|---------|
| **Dormant** | `ADP_DORMANT` | Not material at current stage/class |
| **Latent** | `ADP_LATENT` | Manual coverage typical |
| **Pressured** | `ADP_PRESSURED` | Compression consideration mandatory |
| **Dominant** | `ADP_DOMINANT` | Highest compression pressure in slice |
| **Blocking gap** | `ADP_BLOCKING` | Repeat volume high; gap = operational failure |

**Non-claims:** no `cron_expr`, no `pipeline_id`, no `runtime_ref`, no `orchestration_ref` — future layers only.

---

## 6. Agent → Automation Mapping

### 6.1 Primary mapping (1:1 agent → automation)

| `agent_type_code` | Primary `automation_type_code` |
|-------------------|-------------------------------|
| `AG_DECISION_TRACE_STEWARD` | `AU_DECISION_TRACE_COMPRESSION` |
| `AG_OBLIGATION_TRACE_STEWARD` | `AU_OBLIGATION_TRACE_COMPRESSION` |
| `AG_CONTEXT_BINDER` | `AU_CONTEXT_BINDING_COMPRESSION` |
| `AG_IDENTITY_STEWARD` | `AU_IDENTITY_STEWARDSHIP_COMPRESSION` |
| `AG_CLASS_REGISTRAR` | `AU_CLASS_REGISTRY_COMPRESSION` |
| `AG_BOUNDARY_STEWARD` | `AU_BOUNDARY_STEWARDSHIP_COMPRESSION` |
| `AG_EXPERIENCE_STEWARD` | `AU_EXPERIENCE_MODELING_COMPRESSION` |
| `AG_STRUCTURE_STEWARD` | `AU_STRUCTURE_DEFINITION_COMPRESSION` |
| `AG_IMPLEMENTATION_PRODUCER` | `AU_ARTIFACT_PRODUCTION_COMPRESSION` |
| `AG_VERIFICATION_STEWARD` | `AU_VERIFICATION_COMPRESSION` |
| `AG_DATA_STEWARD` | `AU_DATA_ALIGNMENT_COMPRESSION` |
| `AG_REGULATORY_STEWARD` | `AU_REGULATORY_ALIGNMENT_COMPRESSION` |
| `AG_COMMERCIAL_STEWARD` | `AU_COMMERCIAL_ALIGNMENT_COMPRESSION` |
| `AG_SAFETY_STEWARD` | `AU_SAFETY_ASSESSMENT_COMPRESSION` |
| `AG_SURVIVABILITY_STEWARD` | `AU_SURVIVABILITY_COMPRESSION` |
| `AG_RELEASE_STEWARD` | `AU_RELEASE_COORDINATION_COMPRESSION` |
| `AG_COUPLING_STEWARD` | `AU_COUPLING_SYNC_COMPRESSION` |
| `AG_LIFECYCLE_STEWARD` | `AU_LIFECYCLE_TRUTH_COMPRESSION` |
| `AG_EXPANSION_STEWARD` | `AU_EXPANSION_CHARTER_COMPRESSION` |
| `AG_INVESTMENT_STEWARD` | `AU_INVESTMENT_POSTURE_COMPRESSION` |
| `AG_SUNSET_STEWARD` | `AU_SUNSET_EXECUTION_COMPRESSION` |
| `AG_PRESERVATION_STEWARD` | `AU_PRESERVATION_RECOVERY_COMPRESSION` |

### 6.2 Agent weight → automation weight

| Agent weight | Typical automation weight |
|--------------|---------------------------|
| `AW_LATENT` | `ATW_LATENT` / `ATW_ASSISTIVE` |
| `AW_SUPPORTIVE` | `ATW_ASSISTIVE` |
| `AW_OPERATIONAL` | `ATW_OPERATIONAL` |
| `AW_STRUCTURAL` | `ATW_OPERATIONAL` / `ATW_STRUCTURAL` |
| `AW_CRITICAL` | `ATW_STRUCTURAL` / `ATW_CRITICAL` |
| `AW_TERMINAL` | `ATW_TERMINAL` |

---

## 7. Workflow Automation Matrix

| Code | Meaning |
|------|---------|
| **H** | Human-dominant — max `ATW_ASSISTIVE` |
| **M** | Mixed — partial compression after proof |
| **A** | Automation-suitable when upstream aligned |
| **E** | Event-bound — `CTP_EVENT_BOUND` |

| `workflow_type_code` | Suit | Primary `automation_type_code` | Never compressed |
|----------------------|------|-------------------------------|------------------|
| `WF_INTAKE` | H | `AU_CONTEXT_BINDING_COMPRESSION` | Continue/hold/kill authorization |
| `WF_DEFINITION` | H | `AU_IDENTITY_STEWARDSHIP_COMPRESSION` | Identity/pivot decisions |
| `WF_CLASSIFICATION` | M | `AU_CLASS_REGISTRY_COMPRESSION` | Class binding sign-off |
| `WF_CHARTER` | H | `AU_BOUNDARY_STEWARDSHIP_COMPRESSION` | Scope decisions |
| `WF_UX_JOURNEY` | M | `AU_EXPERIENCE_MODELING_COMPRESSION` | Journey commitment |
| `WF_ARCHITECTURE` | M | `AU_STRUCTURE_DEFINITION_COMPRESSION` | Structure commitment |
| `WF_BUILD` | A | `AU_ARTIFACT_PRODUCTION_COMPRESSION` | Charter change |
| `WF_VALIDATION` | A | `AU_VERIFICATION_COMPRESSION` | Misalignment disposition |
| `WF_DATA_ALIGNMENT` | A | `AU_DATA_ALIGNMENT_COMPRESSION` | Retention policy change |
| `WF_COMPLIANCE_ALIGNMENT` | A | `AU_REGULATORY_ALIGNMENT_COMPRESSION` | Legal interpretation |
| `WF_COMMERCIAL_ALIGNMENT` | M | `AU_COMMERCIAL_ALIGNMENT_COMPRESSION` | Pricing decisions |
| `WF_TRUST_SAFETY_ALIGNMENT` | M | `AU_SAFETY_ASSESSMENT_COMPRESSION` | Autonomy limit change |
| `WF_OPERATIONS_READINESS` | A | `AU_SURVIVABILITY_COMPRESSION` | Ops ownership |
| `WF_RELEASE` | E | `AU_RELEASE_COORDINATION_COMPRESSION` | Release authorization |
| `WF_ECOSYSTEM_SYNC` | E | `AU_COUPLING_SYNC_COMPRESSION` | Coupling scope change |
| `WF_LIFECYCLE_TRANSITION` | H | `AU_LIFECYCLE_TRUTH_COMPRESSION` | Stage claims |
| `WF_EXPANSION` | M | `AU_EXPANSION_CHARTER_COMPRESSION` | Expansion authorization |
| `WF_INVESTMENT_REVIEW` | H | `AU_INVESTMENT_POSTURE_COMPRESSION` | Portfolio decisions |
| `WF_SUNSET` | M | `AU_SUNSET_EXECUTION_COMPRESSION` | Decommission authorization |
| `WF_RECOVERY` | E | `AU_PRESERVATION_RECOVERY_COMPRESSION` | Recovery authorization |

**Human-dominant families:** `WF_DEFINITION`, `WF_CHARTER`, `WF_LIFECYCLE_TRANSITION`, `WF_INVESTMENT_REVIEW`, `WF_INTAKE` (authorization stream).

**Naturally automation-suitable:** `WF_VALIDATION`, `WF_ECOSYSTEM_SYNC`, `WF_BUILD`, `WF_OPERATIONS_READINESS`, `WF_RECOVERY`.

---

## 8. Lifecycle Automation Pressure Matrix

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | — | context (advisory) | trace | ops, regulatory |
| **`LC_DISCOVERY`** | class, identity | alignment probes | structure | full survivability |
| **`LC_PROOF`** | boundary, artifact | verification, lifecycle truth | data | full survivability |
| **`LC_PILOT`** | survivability, release, verification | regulatory, safety, commercial | structure | expansion |
| **`LC_PRODUCTION`** | survivability, regulatory, release, coupling, verification | build, data, commercial | expansion | sunset |
| **`LC_GROWTH`** | expansion, verification, structure | regulatory, boundary | experience | intake |
| **`LC_MATURE`** | investment, survivability | regulatory, verification | expansion | identity major |
| **`LC_LEGACY`** | investment, sunset | survivability minimal, regulatory | coupling | expansion |
| **`LC_SUNSET`** | sunset, data, lifecycle truth | regulatory, release final | coupling | commercial |
| **`LC_HOLD`** | lifecycle truth, verification staleness | prior staleness probes only | — | new expansion |

---

## 9. Product Class Automation Pressure Matrix

Criticality: **●** Critical · **◐** Elevated · **○** Standard · **—** Rarely material

| Domain | COMMERCE | FIELD_OPS | AI_ASST | UTILITY | MARKET | HEALTH | FINTECH | AI_CONSOLE |
|--------|----------|-----------|---------|---------|--------|--------|---------|------------|
| `AU_VERIFICATION_COMPRESSION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AU_OBLIGATION_TRACE_COMPRESSION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AU_SURVIVABILITY_COMPRESSION` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `AU_COUPLING_SYNC_COMPRESSION` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `AU_REGULATORY_ALIGNMENT_COMPRESSION` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `AU_SAFETY_ASSESSMENT_COMPRESSION` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `AU_PRESERVATION_RECOVERY_COMPRESSION` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `AU_COMMERCIAL_ALIGNMENT_COMPRESSION` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |

---

## 10. Automation Weight Model

Derived from **influence radius × repetition frequency × dependency depth on agent/workflow chain × rollback complexity** — not from lines of code, cron count, or vendor hype.

### 10.1 Weight classes

#### `ATW_LATENT`

| Field | Value |
|-------|-------|
| **Influence radius** | Single signal; compression not structurally expected |
| **Dependency depth** | Shallow — manual default |
| **Rollback complexity** | Trivial — disable without product impact |
| **Examples** | Advisory trace compression at Concept |

#### `ATW_ASSISTIVE`

| Field | Value |
|-------|-------|
| **Influence radius** | Single workflow stream; draft/signal repetition |
| **Dependency depth** | Low |
| **Rollback complexity** | Low — human coverage absorbs |
| **Examples** | `AU_IDENTITY_STEWARDSHIP_COMPRESSION` drift probes at Discovery |

#### `ATW_OPERATIONAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Multi-artifact; daily repetition expected |
| **Dependency depth** | Medium — full derivation chain required |
| **Rollback complexity** | Medium — revert to manual coverage cycle |
| **Examples** | `AU_VERIFICATION_COMPRESSION` at Pilot; `AU_ARTIFACT_PRODUCTION_COMPRESSION` in build |

#### `ATW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Product-wide repeat surface |
| **Dependency depth** | High — mis-bound compression blocks trust in coverage |
| **Rollback complexity** | High — requires re-proof of manual coverage |
| **Examples** | `AU_COUPLING_SYNC_COMPRESSION` per-deploy; `AU_BOUNDARY_STEWARDSHIP_COMPRESSION` at Proof exit |

#### `ATW_CRITICAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Ops/legal/users depend on compressed checks |
| **Dependency depth** | High — over-compression = integrity failure |
| **Rollback complexity** | High — incident-grade manual recovery |
| **Examples** | `AU_REGULATORY_ALIGNMENT_COMPRESSION` Production; `AU_SURVIVABILITY_COMPRESSION` Production |

#### `ATW_TERMINAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Irreversible or impractical to undo |
| **Dependency depth** | Very high — paired human authority mandatory |
| **Rollback complexity** | Very high — may be impossible |
| **Examples** | `AU_SUNSET_EXECUTION_COMPRESSION` decommission steps; mass deletion paths |

---

## 11. Automation State Model

Automation states describe **compression eligibility and scope posture**, not job running, pod health, or pipeline success.

### 11.1 State codes

| State | Code | Meaning |
|-------|------|---------|
| **Latent** | `ATS_LATENT` | Derivation chain exists; compression not yet pressured |
| **Candidate** | `ATS_CANDIDATE` | Agent `AS_ELIGIBLE` + repeatability proven; compression may be authorized |
| **Active** | `ATS_ACTIVE` | Compression domain authorized within bounds — not «running in prod» |
| **Constrained** | `ATS_CONSTRAINED` | Upstream prerequisite gap blocks compression |
| **Suspended** | `ATS_SUSPENDED` | Human hold, incident, or authority review pauses compression |
| **Overbound** | `ATS_OVERBOUND` | Compression scope exceeds agent/role boundary |
| **Superseded** | `ATS_SUPERSEDED` | Upstream reality change replaced compression pressure |
| **Advisory-only** | `ATS_ADVISORY` | Signals only; cannot satisfy coverage at `ATW_STRUCTURAL`+ |

### 11.2 State transition rules (descriptive)

```text
ATS_LATENT ──(agent AS_ELIGIBLE + workflow WS_ALIGNED+)──► ATS_CANDIDATE
ATS_CANDIDATE ──(human proof cycle + authority check)──► ATS_ACTIVE
ATS_CANDIDATE ──(upstream gap)──► ATS_CONSTRAINED
ATS_ACTIVE ──(scope exceeds agent)──► ATS_OVERBOUND
ATS_ACTIVE ──(human hold / incident)──► ATS_SUSPENDED
ATS_SUSPENDED ──(hold cleared + re-proof)──► ATS_ACTIVE
ATS_* ──(upstream supersession)──► ATS_SUPERSEDED
ATS_* ──(stage/class irrelevant)──► ATS_LATENT (dormant posture)
```

### 11.3 Deliberate exclusions

| Rejected state | Reason | Correct layer |
|----------------|--------|---------------|
| **running** | Process health | Runtime |
| **deployed** | Instance binding | Implementation Catalog |
| **scheduled** | Trigger config | Deployment |
| **autonomous** | Authority claim | Forbidden |
| **orchestrated** | Coordination graph | Orchestration |

---

## 12. Human Authority Model

**Mandatory.** Automation Reality preserves HITL and SAFE UNKNOWN. Compression **never** expands authority.

### 12.1 Authority exclusion classes (`AEX_*`)

| Class | Code | What automation can NEVER do |
|-------|------|------------------------------|
| **Decision authority** | `AEX_DECISION` | Create, alter, or supersede `decision_type_code` choices |
| **Lifecycle authority** | `AEX_LIFECYCLE` | Advance, hold, regress, or kill `lifecycle_state_code` |
| **Approval authority** | `AEX_APPROVAL` | Sign-off, legal approval, release authorization |
| **Product authority** | `AEX_PRODUCT` | Bind identity, class, tier, or pivot product thesis |
| **Contract authority** | `AEX_CONTRACT` | Create or downgrade obligation weight |
| **Scope authority** | `AEX_SCOPE` | Expand charter boundary or redefine in/out scope |
| **Recovery authority** | `AEX_RECOVERY` | Authorize rollback, quarantine, or restore execution |

### 12.2 Explicit boundaries

| Authority domain | Human must retain | Automation may only |
|------------------|-------------------|---------------------|
| **Decisions** | All `DEC_*` crystallization and supersession | Repeat decision-trace maintenance |
| **Lifecycle** | Stage claims and transition bundles | Probe stage claim vs evidence diff |
| **Approvals** | V2/V3 sign-off acts | Collect pre-approval evidence |
| **Product** | Identity, class, audience commitment | Drift detection signals |

### 12.3 HITL preservation rules

1. **`ATW_STRUCTURAL`+ requires human proof cycle** before `ATS_ACTIVE`
2. **`ATS_ADVISORY` cannot alone satisfy coverage** at `AW_STRUCTURAL`+ agent domains
3. **Misalignment signals from compression trigger human disposition** — not auto-remediation by default
4. **SAFE UNKNOWN on compression domain at `ATW_CRITICAL`+** blocks `ATS_ACTIVE` claim
5. **Terminal compressions (`ATW_TERMINAL`) require named human authority** on each authorization act

---

## 13. Automation Failure Patterns

| Pattern | Signal | Root failure | Affected domains |
|---------|--------|--------------|------------------|
| **Automation before reality** | Cron exists; no product/lifecycle context | Skipped RBM chain | All |
| **Automation before workflow** | Script runs; no `WF_*` mapped | Work structure bypass | Orphan compression |
| **Automation before role** | Bot «owns QA»; `RL_*` vacant | Accountability substitution | Alignment |
| **Automation before tool** | Pipeline produces outputs; tools `TS_REQUIRED` | Capability bypass | `TW_CRITICAL`+ |
| **Automation before agent** | n8n flow; no `agent_type_code` | Unbounded compression | All |
| **Automation mythology** | «It's automated so it's covered» | Runtime = coverage | Production |
| **Hidden orchestration assumptions** | Multi-step graph before `AU_*` registry | Orchestration premature | All |
| **Fake autonomy** | Auto-remediation without authority model | `AEX_*` breach | Safety, regulatory |
| **Invisible decision making** | Pipeline auto-approves scope changes | `AEX_SCOPE` breach | Charter, build |
| **Human authority erosion** | Compression at `ATW_CRITICAL` without HITL proof | §12 violation | Ops, compliance |
| **One-time sync myth** | URL drift returns | `AU_COUPLING_SYNC_COMPRESSION` not event-bound | ORCA |
| **Handoff compression absent** | Delivery automated; survivability manual-only gap | Factory analog | `AU_SURVIVABILITY_COMPRESSION` |
| **Preservation compression skipped** | Transition without snapshot ritual | MARS analog | `AU_PRESERVATION_RECOVERY_COMPRESSION` |
| **Over-compression** | Compression exceeds agent role boundary | `ATS_OVERBOUND` | Matching `AG_*` |
| **Upstream supersession ignored** | Old compression active after pivot | `ATS_SUPERSEDED` not applied | Trace, identity |

---

## 14. Automation Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-U1** | Every `automation_type_code` must trace full chain: `WF_*` → `RL_*` → `TL_*` → `AG_*` | Agentless compression |
| **AC-U2** | No automation domain without prior Agent Reality registry entry | Automation-before-Agents |
| **AC-U3** | No `AU_ARTIFACT_PRODUCTION_COMPRESSION` at `ATW_STRUCTURAL`+ before `AU_BOUNDARY_STEWARDSHIP_COMPRESSION` reaches `ATS_CANDIDATE` | Build compression before charter |
| **AC-U4** | Extended class: regulatory/safety compressions cannot stay `ATS_LATENT` past `LC_DISCOVERY` when alignment workflows active | Compliance compression vacuum |
| **AC-U5** | Production claim requires survivability, regulatory, release compression domains `ATS_CANDIDATE`+ — not inferred from CI green | Runtime = coverage |
| **AC-U6** | Same `automation_type_code` at `ATW_STRUCTURAL`+ requires lifecycle/tier trigger to re-activate from `ATS_SUPERSEDED` | Compression churn |
| **AC-U7** | No universal compression class — every class maps to explicit derivation chain | Universal automation |
| **AC-U8** | `ATW_CRITICAL`+ domains require human proof cycle before `ATS_ACTIVE` | Fake active compression |
| **AC-U9** | Pilot with real users requires `AU_SURVIVABILITY_COMPRESSION` at lite minimum `ATS_CANDIDATE` | Handoff gap |
| **AC-U10** | Identity pivot requires lifecycle + decision trace compression refresh | Random pivot compression |
| **AC-U11** | One primary compression class per agent domain per workflow activation | Duplicate compression |
| **AC-U12** | `AU_CLASS_REGISTRY_COMPRESSION` re-required on tier bump or regulated feature trigger | Classification drift |
| **AC-U13** | Undocumented `ATW_CRITICAL`+ at `ATS_CANDIDATE` = SAFE UNKNOWN in REPORT | Silent critical gap |
| **AC-U14** | `UTILITY_TOOL` T1 exempt from commercial/regulatory compression until trigger | Over-engineering |
| **AC-U15** | Store/public release requires release + lifecycle truth compression eligible | Release confusion |
| **AC-U16** | Software/engine name alone cannot define compression class | Vendor-first thinking |
| **AC-U17** | Every active `automation_type_code` must trace to `source_workflow_type_code` | Compression without workflow |
| **AC-U18** | `AU_COUPLING_SYNC_COMPRESSION` must re-enter `ATS_CANDIDATE` on each external deploy | One-time sync (ORCA) |
| **AC-U19** | High-risk transitions require `AU_PRESERVATION_RECOVERY_COMPRESSION` eligible before claim | Preservation gap |
| **AC-U20** | No compression may claim `AEX_*` authority acts | Human authority erosion |
| **AC-U21** | No Runtime/Orchestration design may reference compression class not in registry | Implementation before Reality |
| **AC-U22** | `ATS_ACTIVE` requires `AS_ELIGIBLE` + `WS_ALIGNED` + `TS_AVAILABLE` on full chain | Fake eligibility |
| **AC-U23** | Human-dominant workflows (`WF_LIFECYCLE_TRANSITION`, etc.) — compression max `ATW_ASSISTIVE` for authority streams | Lifecycle automation |
| **AC-U24** | Auto-remediation forbidden at `ATW_CRITICAL`+ without explicit future charter | Fake autonomy |
| **AC-U25** | Automation Reality completes RBM — no further reality layers without human charter | RBM overreach |

---

## 15. Automation Relationships

### 15.1 Dependency chain

```text
┌─────────────────────────────────────────────────────────────┐
│                    REALITY LAYER (NOVA)                      │
├─────────────────────────────────────────────────────────────┤
│  Production Model · Taxonomy · Registry · Lifecycle          │
│  Decision Reality → Contract Reality → Workflow Reality      │
│  Role Reality → Tool Reality → Agent Reality                 │
│  Automation Reality Model v1 → automation_type_code    ◄── HERE │
└───────────────────────────────┬─────────────────────────────┘
                                │ compression domains ready for Implementation binding
                                ▼
┌─────────────────────────────────────────────────────────────┐
│     AGENT CARDS · IMPLEMENTATION · RUNTIME (future)          │
│  Instance + machinery bindings — NOT v1                        │
└─────────────────────────────────────────────────────────────┘
```

### 15.2 Full derivation chain (mandatory order)

```text
contract_type_code
    ↓ activates
workflow_type_code
    ↓ requires coverage
role_type_code
    ↓ requires capability
tool_type_code
    ↓ enables occupant
agent_type_code
    ↓ enables compression consideration
automation_type_code
    ↓ instantiated by (future — NOT v1)
implementation_binding / runtime_binding
```

**Why not Agent → Automation alone?** Agent defines occupant class; workflow defines repeatable work; role defines boundary; tool defines capability outputs. Compression without full chain produces **automation mythology**.

**Why not Automation → Agent → Workflow (reversed)?** Compression would invent work structure and occupant scope instead of deriving from proven coverage — root cause of automation-first architecture failures.

### 15.3 Combined pressure function (conceptual)

```text
automation_pressure(automation_type_code, product_class_code, lifecycle_state_code,
                    source_workflow_type_code, source_role_type_code,
                    required_tool_type_codes[], source_agent_type_code, tier)
  → dominance_posture ∈ { dormant, latent, pressured, dominant, blocking }
  → effective_weight_class (ATW_*)
  → automation_state_code (ATS_*)
  → compression_trigger_posture (CTP_*)
```

---

## 16. Automation Reality Boundaries

### 16.1 What is NOT automation (v1)

| Artifact | Layer | Why excluded |
|----------|-------|--------------|
| **Workflow** | Workflow Reality | Work structure ≠ compression class |
| **Role** | Role Reality | Accountability ≠ repetition |
| **Tool** | Tool Reality | Capability ≠ compression |
| **Agent** | Agent Reality | Occupant class ≠ compression domain |
| **Runtime** | Runtime (future) | Execution environment |
| **Orchestration** | Orchestration (future) | Coordination machinery |
| **Infrastructure** | Infrastructure (future) | Hosting |
| **Deployment** | Deployment (future) | Install/schedule records |
| **Agent Card** | Agent Cards (future) | Instance binding |
| **Cron / CI / n8n** | Implementation | Vendor artifacts |
| **Decision** | Decision Reality | Upstream — never created by automation |
| **Contract** | Contract Reality | Upstream — never created by automation |

### 16.2 Boundary tests

| Question | Automation Reality if YES |
|----------|---------------------------|
| Removing all cron, CI, and bots, does compression taxonomy still make sense given agents and upstream layers? | Yes |
| Does this primarily define work structure? | No → Workflow |
| Does this primarily define occupant class? | No → Agent |
| Does this execute on a server? | No → Runtime |
| Does this create or alter decisions/lifecycle/approvals? | No → Forbidden |

---

## 17. Automation Reality vs Runtime

```text
┌──────────────────────────────┐
│   AUTOMATION REALITY (v1)     │  automation_type_code — compression domain
│  Implementation-neutral · stable │
└──────────────┬───────────────┘
               │ instantiates (future)
               ▼
┌──────────────────────────────┐
│        RUNTIME (future)       │  runtime_binding_ref — NOT in v1
│  Schedules · workers · health │
└──────────────────────────────┘
```

| Concern | Automation Reality (v1) | Runtime (future) |
|---------|------------------------|------------------|
| **Existence** | Which compression domains may exist | Which worker executes |
| **Scope** | Derivation chain + authority exclusions | Env, scaling, retries |
| **State** | `ATS_*` eligibility | running, failed, scaled |
| **Failure** | Overbound, chain break, authority breach | Process crash, timeout |

**v1 rule:** teams may *run* cron and CI informally; **governance truth** remains `automation_type_code` eligibility and bounds — not pipeline green alone.

---

## 18. Automation Reality vs Agent Cards

```text
┌──────────────────────────────┐
│     AGENT REALITY (v1)        │  agent_type_code — occupant class
└──────────────┬───────────────┘
               │ occupant scope bounds compression
               ▼
┌──────────────────────────────┐
│   AUTOMATION REALITY (v1)     │  automation_type_code — compression domain
└──────────────┬───────────────┘
               │ instantiates (future)
               ▼
┌──────────────────────────────┐
│     AGENT CARDS (future)      │  agent_card_id — specific occupant instance
│  May bind compression to instance │
└──────────────────────────────┘
```

| Concern | Agent Reality | Automation Reality | Agent Cards (future) |
|---------|---------------|-------------------|----------------------|
| **Question** | What occupant class may exist? | What may repeat within that class? | Which instance runs? |
| **Stability** | Class taxonomy stable | Compression boundary stable | Instance swappable |
| **Failure** | Overbound occupant | Over-compression | Prompt/runtime drift |

Agent Cards **occupy** agent classes. Automation Reality **names compressible surfaces** of that occupation. Neither substitutes for the other.

---

## 19. RBM Completion Mapping

### 19.1 Full chain

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
Tools (TL_*)
    ↓ occupant class definition
Agents (AG_*)
    ↓ repeatable compression domain
Automation (AU_*)              ◄── this document — FINAL RBM LAYER
```

### 19.2 Why Automation is the final RBM layer

| Layer | Question answered | Why nothing after Automation in RBM |
|-------|-------------------|-------------------------------------|
| Workflow | What work exists? | Upstream of execution assignment |
| Role | What must be covered? | Upstream of capability |
| Tool | What must be possible? | Upstream of occupant |
| Agent | What occupant class may execute? | Upstream of compression |
| **Automation** | **What may repeat without re-opening upstream?** | **Downstream is machinery, not reality** |

RBM defines **what may exist in product reality** before machinery choices. Runtime, Orchestration, Implementation Catalog, Deployments, and Agent Cards are **implementation and binding layers** — they do not add new ontology; they **instantiate** approved reality vocabulary.

### 19.3 What RBM completion means

1. **Full vocabulary chain** from product identity through compression domain exists
2. **Derivation discipline** enforced: no layer may be designed before its upstream chain
3. **Authority firewall** explicit at automation boundary
4. **Implementation neutrality** preserved through final layer
5. **Post-RBM work** shifts from ontology to binding, policy, and machinery — only with human charter

### 19.4 What becomes possible after completion (not designed here)

- Honest Agent Cards charter referencing `agent_type_code` + compression exclusions
- Implementation Catalog mapping `AU_*` → concrete machinery
- Runtime concepts with health separate from `ATS_*`
- Automation Policies governing `ATS_ACTIVE` authorization
- Orchestration graphs bounded by named compression domains

---

## 20. Post-RBM Implications

Dependency-only sketch — **not designed in v1**.

| Future layer | Depends on Automation Reality for |
|--------------|----------------------------------|
| **Agent Cards Charter** | Which `agent_type_code` instances may bind compression; `AEX_*` exclusions |
| **Agent Registry** | Occupant classes that upstream compression references |
| **Implementation Catalog** | Approved `automation_type_code` → software/workflow-engine mapping |
| **Runtime Concepts** | Separation of `ATS_*` from process health |
| **Automation Policies** | Human authorization rules for `ATS_ACTIVE`; proof cycle requirements |
| **Orchestration Charter** | Multi-step coordination bounded by `AU_*` — not reverse-defining domains |
| **Deployment Records** | Cron/schedule as instance artifacts — not compression taxonomy |

**Explicit non-starters without charter:** Automation Engine product, autonomous ops platform, self-approving pipeline, universal NOVA bot.

---

## 21. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Automation-first regression | High | AC-U1, AC-U2, AC-U7 |
| Runtime mythology | High | AC-U5, §17 separation |
| Human authority erosion | High | §12; AC-U20, AC-U23 |
| Fake `ATS_ACTIVE` | High | AC-U8, AC-U22 |
| Orchestration-before-reality | High | AC-U21; §2.5 |
| 22-family operator fatigue | Medium | Matrices §8–9; Appendix A |
| Over-compression at Production | High | `ATW_CRITICAL` gates; AC-U8 |
| CI-green = validated confusion | High | §17; AC-U5 |
| Governance expansion beyond RBM | Medium | AC-U25 |
| Prior foundation files not all in-repo | Medium | Cross-reference `projects/nova/foundation/` |

---

## 22. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Optimal compression family count (22 vs consolidated) | Operator feedback after 2–3 products |
| Machine format for `automation_pressure_instance` | Future intake schema |
| Exact human proof cycle duration before `ATS_ACTIVE` | First Production pilot through NOVA |
| Whether trace compressions merge in v2 | Cross-product trace discipline review |
| Auto-remediation boundaries per class | Explicit future charter — default forbidden |
| `ATS_OVERBOUND` mandatory escalation | First Production incident |
| Orchestration graph ↔ `AU_*` cardinality | First Orchestration charter |
| Overlap with MARS survivability automation | NOVA ↔ MARS integration charter |
| Default human vs compressed coverage per class | Agent Cards + Staffing charter |

**Non-claims preserved:** no runtime, orchestration, automation engine, agent cards, implementation catalog, deployment design, infrastructure design, or automated compression enforcement.

---

## 23. Recommended Next Step

**RBM is complete.** Next artifacts are **post-RBM implementation layers** — human charter required; choose **one**:

1. **NOVA Agent Cards Charter v1** — instance bindings for approved `agent_type_code` classes; compression exclusions from `AEX_*`

2. **NOVA Implementation Catalog Charter v1** — machinery mappings for approved `tool_type_code` and `automation_type_code` only

3. **NOVA Automation Policies Charter v1** — human authorization rules for `ATS_ACTIVE`; proof cycles; suspension semantics

**Do not skip to:** full Orchestration platform, Runtime catalog, or Automation Engine until human explicitly charters and RBM artifacts are committed.

**Optional parallel:** update Agent Reality Model §21 Recommended Next Step to mark Automation complete; commit full NOVA foundation pack under `projects/nova/foundation/`.

---

## Appendix A — Automation Pressure Snapshot template

```markdown
# Automation Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| automation_type_code | dominance_posture | effective_weight | automation_state | trigger_posture | source_agent | source_workflow |
|----------------------|-------------------|------------------|------------------|-----------------|--------------|-----------------|
| AU_VERIFICATION_COMPRESSION | | | | | | |
| ... | | | | | | |

Dominant compression domains this stage:
Candidate but not active (ATS_CANDIDATE):
Overbound (ATS_OVERBOUND):
Authority exclusions in force (AEX_*):
SAFE UNKNOWN compression domains:
```

---

## Appendix B — Quick reference: `automation_type_code` registry

| Code | One-line compression class |
|------|---------------------------|
| `AU_DECISION_TRACE_COMPRESSION` | Repeat decision-trace maintenance within bounds |
| `AU_OBLIGATION_TRACE_COMPRESSION` | Repeat obligation-trace maintenance |
| `AU_CONTEXT_BINDING_COMPRESSION` | Repeat intake binding validation |
| `AU_IDENTITY_STEWARDSHIP_COMPRESSION` | Repeat identity drift checks |
| `AU_CLASS_REGISTRY_COMPRESSION` | Repeat class registry validation |
| `AU_BOUNDARY_STEWARDSHIP_COMPRESSION` | Repeat charter boundary probes |
| `AU_EXPERIENCE_MODELING_COMPRESSION` | Repeat journey consistency checks |
| `AU_STRUCTURE_DEFINITION_COMPRESSION` | Repeat architecture truth probes |
| `AU_ARTIFACT_PRODUCTION_COMPRESSION` | Repeat artifact production within charter |
| `AU_VERIFICATION_COMPRESSION` | Repeat verification evidence collection |
| `AU_DATA_ALIGNMENT_COMPRESSION` | Repeat data alignment probes |
| `AU_REGULATORY_ALIGNMENT_COMPRESSION` | Repeat regulatory alignment probes |
| `AU_COMMERCIAL_ALIGNMENT_COMPRESSION` | Repeat commercial path probes |
| `AU_SAFETY_ASSESSMENT_COMPRESSION` | Repeat safety boundary probes |
| `AU_SURVIVABILITY_COMPRESSION` | Repeat survivability/handoff checks |
| `AU_RELEASE_COORDINATION_COMPRESSION` | Repeat release readiness probes |
| `AU_COUPLING_SYNC_COMPRESSION` | Repeat coupling parity per deploy |
| `AU_LIFECYCLE_TRUTH_COMPRESSION` | Repeat lifecycle honesty probes |
| `AU_EXPANSION_CHARTER_COMPRESSION` | Repeat expansion boundary probes |
| `AU_INVESTMENT_POSTURE_COMPRESSION` | Repeat investment signal collection |
| `AU_SUNSET_EXECUTION_COMPRESSION` | Repeat sunset checklist steps |
| `AU_PRESERVATION_RECOVERY_COMPRESSION` | Repeat preservation ritual steps |

---

## Appendix C — RBM layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established |
| Decisions | Decision Reality Model v1 | Complete |
| Contracts | Contract Reality Model v1 | Complete |
| Workflow | Workflow Reality Model v1 | Complete |
| Roles | Role Reality Model v1 | Complete |
| Tools | Tool Reality Model v1 | Complete |
| Agents | Agent Reality Model v1 | Complete |
| **Automation** | **Automation Reality Model v1** | **This document — RBM COMPLETE** |

---

*End of NOVA Automation Reality Model v1 — final RBM layer. Nothing beyond Automation Reality.*
