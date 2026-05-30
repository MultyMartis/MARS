# NOVA Agent Reality Model v1

**Status:** design-only — Reality-layer occupant domain vocabulary, not agent cards, not agent registry, not prompts, not staffing, not runtime, not orchestration, not automation  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → NOVA Contract Reality Model v1 → NOVA Workflow Reality Model v1 → NOVA Role Reality Model v1 → NOVA Tool Reality Model v1 → **this document**  
**Non-claims:** no agent cards, no agent registry, no prompts, no orchestration, no runtime, no automation, no staffing records, no database schema

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

**Evidence base:** Website Factory handoff-collapse, onboarding fragility, and agent-before-ops lessons; ORCA semantic-vs-deployed sync and per-deploy registry discipline; MARS snapshot/rollback/recovery and protected-zone survivability lessons; real-world mobile delivery practices adapted to NOVA

---

## 1. Executive Summary

NOVA Agent Reality Model v1 — **первый occupant-domain artifact NOVA после Tool Reality**. Он отвечает на вопрос:

> **«Какие классы agent occupants могут существовать внутри NOVA и зачем они существуют?»**

Не «какой промпт» (Prompts), не «какой runtime» (Runtime), не «какой бот в проде» (Agent Cards), не «как автоматизировать» (Automation), не «кто сотрудник» (Staffing).

| Элемент | Содержание |
|---------|------------|
| **22 occupant families** | `AG_DECISION_TRACE_STEWARD` … `AG_PRESERVATION_STEWARD` (20 role-aligned + 2 trace cross-cutting) |
| **Canonical agent object** | `agent_type_code` + required reality fields |
| **Agent registry** | 22 rows with definition, source roles/tools/workflows, responsibility surface, failure modes |
| **Role → Agent mapping** | 18 role domains → primary + secondary occupant classes |
| **Tool → Agent mapping** | 20 capability domains → enabling occupant classes |
| **Workflow participation model** | 5 postures: `WP_PRIMARY` … `WP_EVENT_BOUND` |
| **Lifecycle agent pressure matrix** | Dominant occupant domains per `LC_*` stage |
| **Product class agent pressure matrix** | 8 focus classes × occupant criticality |
| **Agent weight model** | 6 classes: `AW_LATENT` → `AW_TERMINAL` |
| **Agent state model** | 8 states: `AS_LATENT` → `AS_SUPERSEDED` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Agent Reality (this doc) | Agent Execution (NOT this) |
|-----------|--------------------------|----------------------------|
| **Question** | What occupant classes can exist because roles require capabilities? | Which specific agent instance runs where? |
| **Layer** | Reality → Agents (structure) | Agent Cards · Prompts · Runtime · Orchestration · Automation (future) |
| **Example** | `AG_SURVIVABILITY_STEWARD` = occupant class that may cover `RL_OPERATIONS` via `TL_SURVIVABILITY_POSTURE` | Cursor agent named «Ops Helper» with MCP config |
| **Output** | Vocabulary + role/tool→occupant maps | Agent cards, prompts, runtime bindings, orchestration graphs |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answered:** «What must be true?» (`contract_type_code`)  
**Workflow Reality answered:** «How does obligation become structured work?» (`workflow_type_code`)  
**Role Reality answered:** «What responsibility domains must cover that work?» (`role_type_code`)  
**Tool Reality answered:** «What capabilities must exist for domains to produce coverage outputs?» (`tool_type_code`)  
**Agent Reality answers:** «What occupant classes may assume coverage within those domains through those capabilities?» (`agent_type_code`)

Without agent reality, teams deploy bots before knowing which responsibility domains they should occupy, agents attach to software brands instead of named capability requirements, and automation compresses broken coverage instead of bounded execution.

---

## 2. Agent Philosophy

### 2.1 What an agent means inside NOVA

В NOVA **agent** — это **домен occupant class** (класс потенциального исполнителя покрытия), который:

1. **Существует потому что role domain требует coverage через available capabilities** — не потому что в стеке уже есть LLM или bot framework
2. **Implementation-neutral** — описывает *какой класс occupant* может покрыть domain, не *какой промпт или runtime* его реализует
3. **Привязан к role + tool binding** — каждый `agent_type_code` traces to `source_role_type_code` + required `tool_type_code` set
4. **Производит coverage через capabilities** — не заменяет role accountability surface; assists or occupies coverage when bound (future)
5. **Отделён от instances** — Agent Card, human assignee, team may *instantiate* occupant class later; class exists first

Agent — **не бот**. «ChatGPT agent in Cursor» — implementation artifact. `AG_VERIFICATION_STEWARD` — occupant class that may cover cross-cutting verification work via `TL_VERIFICATION_EVIDENCE`.

**Website Factory lesson:** handoff collapse = delivery completed with files but **no occupant class** considered for `RL_OPERATIONS` survivability — humans assumed, agent/automation mythology skipped domain reality ([`production-drift-taxonomy.md`](../../projects/mars-website-factory/production-drift-taxonomy.md)).

**ORCA lesson:** per-deploy registry drift = `AG_COUPLING_STEWARD` domain never pressured when `WF_ECOSYSTEM_SYNC` re-activates — one-time human heroics substituted for standing occupant consideration ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

**MARS lesson:** transition without snapshot = `AG_PRESERVATION_STEWARD` occupant domain latent while `RL_RECOVERY` required — ad hoc human recovery substituted for named occupant class ([`snapshot-manifest-standard-v1.md`](../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)).

### 2.2 Why agents exist

Tools **определяют capability domains**. Без agent layer capability остаётся:

- operated only by implicit human assumption;
- attached to arbitrary software without role scope;
- automated before coverage boundaries are known;
- duplicated when multiple bots claim same domain without occupant taxonomy.

Agent **переводит capability availability в occupant class vocabulary** — без выбора промпта, runtime, или orchestration graph.

| Role + Tool says | Agent crystallizes |
|------------------|-------------------|
| `RL_COMPLIANCE` + `TL_REGULATORY_EVIDENCE` must produce alignment outputs | `AG_REGULATORY_STEWARD` occupant class may cover domain |
| `RL_OPERATIONS` + `TL_SURVIVABILITY_POSTURE` before Production | `AG_SURVIVABILITY_STEWARD` occupant class may cover survivability work |
| `RL_VALIDATION` + `TL_VERIFICATION_EVIDENCE` cross-cuts | `AG_VERIFICATION_STEWARD` occupant class may cover verification |
| `RL_ECOSYSTEM` + `TL_COUPLING_REGISTRY` per deploy | `AG_COUPLING_STEWARD` occupant class may cover sync work |

### 2.3 Why agents come after tools

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random occupant labels |
| **Lifecycle** | Stage-appropriate occupant depth | Full ops agent pack at Concept |
| **Decisions** | Choice domains | Agents for unchosen problems |
| **Contracts** | Obligation structure | Agents without obligation trace |
| **Workflow** | Work structure | Agents attached to arbitrary tasks |
| **Roles** | Responsibility domains | Agents substitute for accountability |
| **Tools** | Capability vocabulary | Agents automate missing surfaces |
| **Agents** | Occupant class vocabulary | Automation compresses broken coverage |

**Agents без Tool Reality** — bot theater:

- «We have an AI agent» before knowing `TL_VERIFICATION_EVIDENCE` depth
- Cursor agent before `RL_IMPLEMENTATION` + `TL_ARTIFACT_LINEAGE` scope defined
- Universal assistant before role/tool map exists

Tools **не исполняются** агентами автоматически — они определяют *какие способности* должны быть доступны. Agents **определяют какие классы occupants* могут использовать эти способности для coverage* в named role domains.

### 2.4 Why agents are not workflows

| Agent Reality | Workflow Reality |
|---------------|------------------|
| **What occupant class** may cover work | **What work structure** exists |
| `AG_REGULATORY_STEWARD` = class that may produce compliance coverage outputs | `WF_COMPLIANCE_ALIGNMENT` = compliance alignment work pattern |
| Survives workflow sequencing change if domain persists | Resets when obligation structure changes |
| Bounded by role scope | Defines obligation→work transformation |
| One occupant class; zero or many instances later | One workflow; many possible participants |

**Boundary test:** If you remove all agents, bots, and humans, does the work structure still exist? **Yes** → workflow. Does the occupant class taxonomy still make sense given roles and tools? **Yes** → agent domain.

### 2.5 Why agents are not roles

| Agent Reality | Role Reality |
|---------------|--------------|
| **What occupant class** may assume coverage | **What responsibility domain** must exist |
| `AG_IMPLEMENTATION_PRODUCER` may occupy `RL_IMPLEMENTATION` | `RL_IMPLEMENTATION` = implementation responsibility domain |
| Optional — domain may be covered by human only | Mandatory when workflow active |
| Capability-mediated execution | Actor-neutral accountability |
| Many agent classes must not claim one role without boundary | One domain per workflow activation |

**Boundary test:** If you remove all agents and humans, do responsibility domains still make sense? **Yes** → role. **No** → staffing or agent instance artifact.

Examples:

| Artifact | Layer |
|----------|-------|
| «Implementation domain must honor charter boundary» | `RL_IMPLEMENTATION` — role |
| «Occupant class may produce deliverables within charter via artifact lineage capability» | `AG_IMPLEMENTATION_PRODUCER` — agent |
| «Maria covers compliance» | Staffing — not agent |
| «Compliance bot v3 in prod» | Agent Card — not agent reality |

### 2.6 What transforms capability domains into agent domains?

**Transformation chain (conceptual):**

```text
workflow_type_code + workflow_obligations
    ↓ requires coverage
role_type_code + role_state_code + effective_weight_class (RW_*)
    ↓ requires capability availability
tool_type_code + tool_state_code + effective_weight_class (TW_*)
    ↓ enables occupant class definition
agent_type_code + agent_weight_class + agent_state_code (AS_*)
    ↓ instantiated by (future Agent Cards layer — NOT v1)
occupant_instance producing coverage_outputs[] via capability_outputs[]
```

**Transformers (this layer only):**

1. **Role pressure** — which `role_type_code` is `RS_REQUIRED`+ for current workflow/lifecycle
2. **Capability availability** — required `tool_type_code` at `TS_AVAILABLE` or explicit SAFE UNKNOWN blocks `AS_ELIGIBLE`
3. **Coverage repeatability** — domain work structurally benefits from named occupant class consideration (not every role requires agent domain at all times)
4. **Cross-cutting overlay** — `AG_VERIFICATION_STEWARD` always eligible when `RL_VALIDATION` + `TL_VERIFICATION_EVIDENCE` pressured
5. **Lifecycle/class depth** — same `agent_type_code`; weight and dominance vary by context

**What agent adds beyond tool:**

| Tool provides | Agent adds |
|---------------|------------|
| Capability requirement — what must be *possible* | **Occupant class** — who/what *class* may operate capability for coverage |
| Capability output categories | **Coverage participation posture** — how occupant relates to workflow |
| `TS_REQUIRED` gap signal | **Occupant eligibility signal** — `AS_PRESSURED` when role needs occupant consideration |
| Implementation-neutral ability surface | **Bounded execution scope** — swappable instances later, fixed domain boundary now |

**NOT transformers in v1:** prompt template, model ID, agent_card_ref, runtime_env, orchestration_graph, autonomy_level, API key.

**Rejected candidate definitions (why each alone is wrong):**

| Candidate | Rejection | Correct placement |
|-----------|-----------|-------------------|
| Agent = Role Occupant | Instance assignment, not class taxonomy | Staffing / Agent Cards |
| Agent = Capability Executor | Describes execution, not existence class | Runtime / Automation |
| Agent = Workflow Participant | Work structure ≠ occupant class | Workflow Participation Model §8 |
| Agent = Responsibility Amplifier | Implies autonomy expansion | Automation — blocked until Agents |

**Derived definition:** Agent = **bounded occupant class domain** — a named category of potential coverage occupants that may assume responsibility within a role domain by operating required tool capabilities to produce workflow-aligned outputs, without being the role, the tool, or the workflow.

---

## 3. Agent Ontology

### 3.1 Derivation rationale

Test for each ontological dimension: *«Does NOVA treat occupant eligibility, coverage participation, and failure impact differently if this dimension is absent when source role is `RS_REQUIRED` and source tools are `TS_AVAILABLE`?»*

### 3.2 Primary ontological axes

Agent domains are characterized by **five derived axes** — not job titles, not org charts, not model brands:

```text
Occupant class     — what category of coverage actor (human-augmented or non-human class)
Role binding       — which responsibility domain scope bounds the class
Capability mediation — which tool_type_code set the class may operate
Workflow posture   — how the class participates in structured work (WP_*)
Coverage depth     — how much of role domain the class may claim (AW_*)
```

### 3.3 Ontological dimensions (derived, not assumed)

| Dimension | Code prefix | Meaning | NOT this |
|-----------|-------------|---------|----------|
| **Occupant class** | `AG_*` | Named category of potential coverage actor | Specific bot instance |
| **Role-bound scope** | `source_role_type_code` | Maximum responsibility surface occupant may address | The role itself |
| **Capability-mediated** | `required_tool_type_codes[]` | Tools occupant may operate to produce outputs | The tools themselves |
| **Workflow participant** | `WP_*` | Posture in workflow execution structure | The workflow itself |
| **Coverage amplifier** | `AW_*` weight | Influence radius when occupying domain | Autonomy or orchestration |
| **Validator posture** | overlay on `AG_VERIFICATION_STEWARD` | Independent verification participation | Approval authority |

**Rejected as primary ontology:**

| Rejected | Reason |
|----------|--------|
| **Coordinator** | Orchestration layer — not occupant taxonomy |
| **Universal assistant** | Violates bounded scope; agent-first design |
| **Executor** (standalone) | Runtime behavior, not reality class |
| **Employee** | Staffing |
| **Team** | Staffing |

### 3.4 Ontological composition

Every `agent_type_code` is a **composition**:

```text
agent_domain = occupant_class_identity
             × role_binding(source_role_type_code)
             × capability_mediation(required_tool_type_codes[])
             × workflow_posture(default_WP_*)
             × weight_class(default_AW_*)
```

**Example composition:**

```text
AG_COUPLING_STEWARD =
  occupant_class: ecosystem coupling coverage steward
  × role_binding: RL_ECOSYSTEM
  × capability_mediation: [TL_COUPLING_REGISTRY, TL_OBLIGATION_TRACE]
  × workflow_posture: WP_EVENT_BOUND (per-deploy re-pressure)
  × weight: AW_STRUCTURAL default; AW_CRITICAL at Production per-deploy
```

### 3.5 What agents fundamentally ARE (v1 statement)

> An agent in NOVA is a **bounded occupant class** — a named, implementation-neutral category of potential coverage actors that may assume responsibility within a specific role domain by operating one or more required tool capabilities to produce workflow-aligned coverage outputs.

Agents **do not** create obligations. Agents **do not** define capabilities. Agents **do not** structure work. Agents **may** occupy coverage surfaces once roles require them and tools make execution possible.

---

## 4. Agent Taxonomy

### 4.1 Derivation rationale

Test for each candidate occupant family: *«Does NOVA treat occupant eligibility, workflow participation, and coverage failure differently if this agent type is undefined when its source role is `RS_REQUIRED`, source tools are `TS_AVAILABLE`, and source workflow is `WS_ACTIVATED`+?»*

**Derivation formula:**

```text
agent_family = f(role_type_code, tool_type_code, workflow_obligations)
```

**NOT derived from:** job titles, org charts, model vendors, IDE brands, agent framework names.

**Rejected as standalone agent families:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Universal NOVA Assistant** | Unbounded scope | Forbidden — AC-A7 |
| **Project Manager agent** | Staffing/coordination | Staffing |
| **Developer agent** | Job title | May occupy `AG_IMPLEMENTATION_PRODUCER` |
| **Legal agent** | Job title | May occupy `AG_REGULATORY_STEWARD` |
| **Cursor** | Implementation | Agent Cards + Runtime |
| **ChatGPT** | Model product | Software Implementation |
| **Orchestrator** | Coordination machinery | Orchestration — out of scope |
| **Autonomous runtime** | Execution environment | Runtime — out of scope |

**Design choice:** **22 occupant families** — 20 aligned to role+tool pairs for clean derivation, plus **2 trace cross-cutting occupant classes** (`AG_DECISION_TRACE_STEWARD`, `AG_OBLIGATION_TRACE_STEWARD`) mirroring Tool Reality trace layer. Preserves Role → Tool → Agent chain without collapsing agent into role or tool.

### 4.2 Occupant layers overview

```text
Trace layer:         AG_DECISION_TRACE_STEWARD · AG_OBLIGATION_TRACE_STEWARD
Attention layer:     AG_CONTEXT_BINDER
Identity layer:      AG_IDENTITY_STEWARD · AG_CLASS_REGISTRAR
Boundary layer:      AG_BOUNDARY_STEWARD · AG_EXPERIENCE_STEWARD
Commitment layer:    AG_STRUCTURE_STEWARD · AG_DATA_STEWARD · AG_REGULATORY_STEWARD
                     AG_COMMERCIAL_STEWARD · AG_SAFETY_STEWARD
Execution layer:     AG_IMPLEMENTATION_PRODUCER
Verification layer:  AG_VERIFICATION_STEWARD
Operational layer:   AG_SURVIVABILITY_STEWARD · AG_RELEASE_STEWARD · AG_COUPLING_STEWARD
Temporal layer:      AG_LIFECYCLE_STEWARD · AG_EXPANSION_STEWARD · AG_INVESTMENT_STEWARD · AG_SUNSET_STEWARD
Corrective layer:    AG_PRESERVATION_STEWARD
```

### 4.3 Domain definitions (taxonomy)

#### `AG_DECISION_TRACE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may maintain decision-trace coverage via decision trace capability |
| **Source roles** | All domains at `RW_STRUCTURAL`+ |
| **Source tools** | `TL_DECISION_TRACE` |
| **Source workflows** | Any `WF_*` at `WW_COORDINATED`+ with decision-backed contracts |
| **Responsibility surface** | Decision context binding; choice rationale preservation; supersession awareness |

---

#### `AG_OBLIGATION_TRACE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may maintain obligation-trace coverage via obligation trace capability |
| **Source roles** | All alignment domains; `RL_VALIDATION` |
| **Source tools** | `TL_OBLIGATION_TRACE` |
| **Source workflows** | All alignment `WF_*` |
| **Responsibility surface** | Obligation map maintenance; V-target context; anti-workflow-theater |

---

#### `AG_CONTEXT_BINDER`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover intake/context binding work |
| **Source roles** | `RL_INTAKE` |
| **Source tools** | `TL_CONTEXT_BINDING` |
| **Source workflows** | `WF_INTAKE` |
| **Responsibility surface** | Portfolio entry binding; lifecycle entry label; continue/hold/kill evidence |

---

#### `AG_IDENTITY_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover product identity and audience alignment work |
| **Source roles** | `RL_PRODUCT` |
| **Source tools** | `TL_IDENTITY_STEWARDSHIP` |
| **Source workflows** | `WF_DEFINITION` |
| **Responsibility surface** | Identity thesis; audience alignment; pivot trace (ORCA semantic intent) |

---

#### `AG_CLASS_REGISTRAR`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover class/tier binding work |
| **Source roles** | `RL_CLASSIFICATION` |
| **Source tools** | `TL_CLASS_REGISTRY` |
| **Source workflows** | `WF_CLASSIFICATION` |
| **Responsibility surface** | Class binding honesty; tier modifier; re-classification triggers |

---

#### `AG_BOUNDARY_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover scope charter and boundary work |
| **Source roles** | `RL_CHARTER` |
| **Source tools** | `TL_BOUNDARY_STEWARDSHIP` |
| **Source workflows** | `WF_CHARTER` |
| **Responsibility surface** | Scope anti-creep; charter truth; build constraint enforcement |

---

#### `AG_EXPERIENCE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover journey/experience modeling work |
| **Source roles** | `RL_UX` |
| **Source tools** | `TL_EXPERIENCE_MODELING` |
| **Source workflows** | `WF_UX_JOURNEY` |
| **Responsibility surface** | Journey architecture; UX alignment evidence |

---

#### `AG_STRUCTURE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover technical structure commitment work |
| **Source roles** | `RL_ARCHITECTURE` |
| **Source tools** | `TL_STRUCTURE_DEFINITION` |
| **Source workflows** | `WF_ARCHITECTURE` |
| **Responsibility surface** | Structure truth; dependency boundaries; scale posture |

---

#### `AG_IMPLEMENTATION_PRODUCER`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover implementation delivery work within charter |
| **Source roles** | `RL_IMPLEMENTATION` |
| **Source tools** | `TL_ARTIFACT_LINEAGE` |
| **Source workflows** | `WF_BUILD` |
| **Responsibility surface** | Deliverable production; lineage custody; build drift prevention |

---

#### `AG_VERIFICATION_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover cross-cutting verification work |
| **Source roles** | `RL_VALIDATION` |
| **Source tools** | `TL_VERIFICATION_EVIDENCE` |
| **Source workflows** | `WF_VALIDATION`; overlays all alignment `WF_*` |
| **Responsibility surface** | V-level evidence; alignment/misalignment declaration; anti-fake-completion |

---

#### `AG_DATA_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover data/privacy alignment work |
| **Source roles** | `RL_DATA_PRIVACY` |
| **Source tools** | `TL_DATA_TRUTH` |
| **Source workflows** | `WF_DATA_ALIGNMENT` |
| **Responsibility surface** | Data inventory; retention posture; export/delete path evidence |

---

#### `AG_REGULATORY_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover regulatory/store alignment work |
| **Source roles** | `RL_COMPLIANCE` |
| **Source tools** | `TL_REGULATORY_EVIDENCE` |
| **Source workflows** | `WF_COMPLIANCE_ALIGNMENT` |
| **Responsibility surface** | Regulatory evidence; store category alignment; jurisdiction posture |

---

#### `AG_COMMERCIAL_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover commercial/monetization alignment work |
| **Source roles** | `RL_COMMERCIAL` |
| **Source tools** | `TL_COMMERCIAL_TRUTH` |
| **Source workflows** | `WF_COMMERCIAL_ALIGNMENT` |
| **Responsibility surface** | Pricing truth; payment flow evidence; monetization alignment |

---

#### `AG_SAFETY_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover trust/safety evaluation work |
| **Source roles** | `RL_TRUST_SAFETY` |
| **Source tools** | `TL_SAFETY_ASSESSMENT` |
| **Source workflows** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **Responsibility surface** | Harm models; safety gates; autonomy limit evidence |

---

#### `AG_SURVIVABILITY_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover operational survivability work |
| **Source roles** | `RL_OPERATIONS` |
| **Source tools** | `TL_SURVIVABILITY_POSTURE` |
| **Source workflows** | `WF_OPERATIONS_READINESS` |
| **Responsibility surface** | Runbooks; onboarding; handoff chains; delivery evidence (Website Factory) |

---

#### `AG_RELEASE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover distribution and rollout alignment work |
| **Source roles** | `RL_RELEASE` |
| **Source tools** | `TL_RELEASE_COORDINATION` |
| **Source workflows** | `WF_RELEASE` |
| **Responsibility surface** | Channel truth; rollout phasing; store metadata alignment |

---

#### `AG_COUPLING_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover ecosystem coupling sync work |
| **Source roles** | `RL_ECOSYSTEM` |
| **Source tools** | `TL_COUPLING_REGISTRY` |
| **Source workflows** | `WF_ECOSYSTEM_SYNC` |
| **Responsibility surface** | URL/occupant registry; semantic↔deployed mapping (ORCA) |

---

#### `AG_LIFECYCLE_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover lifecycle transition work |
| **Source roles** | `RL_LIFECYCLE` |
| **Source tools** | `TL_LIFECYCLE_TRUTH` |
| **Source workflows** | `WF_LIFECYCLE_TRANSITION` |
| **Responsibility surface** | Stage claims; transition bundles; hold/regress/kill honesty |

---

#### `AG_EXPANSION_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover growth expansion charter work |
| **Source roles** | `RL_EXPANSION` |
| **Source tools** | `TL_EXPANSION_CHARTER` |
| **Source workflows** | `WF_EXPANSION` |
| **Responsibility surface** | Expansion scope; geo triggers; feature charter |

---

#### `AG_INVESTMENT_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover portfolio investment posture work |
| **Source roles** | `RL_INVESTMENT` |
| **Source tools** | `TL_INVESTMENT_POSTURE` |
| **Source workflows** | `WF_INVESTMENT_REVIEW` |
| **Responsibility surface** | Maintain/harvest/legacy posture evidence |

---

#### `AG_SUNSET_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover end-of-life execution work |
| **Source roles** | `RL_SUNSET` |
| **Source tools** | `TL_SUNSET_EXECUTION` |
| **Source workflows** | `WF_SUNSET` |
| **Responsibility surface** | Migration; export; decommission evidence |

---

#### `AG_PRESERVATION_STEWARD`

| Field | Value |
|-------|-------|
| **Purpose** | Occupant class that may cover preservation and recovery work |
| **Source roles** | `RL_RECOVERY` |
| **Source tools** | `TL_PRESERVATION_RECOVERY` |
| **Source workflows** | `WF_RECOVERY` |
| **Responsibility surface** | Snapshots; rollback; quarantine; restore evidence (MARS) |

---

## 5. Agent Object Model

Canonical agent object describes **an occupant class type in context**, not an agent card, prompt, or runtime instance. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`, `contract_type_code`, `workflow_type_code`, `role_type_code`, `tool_type_code`.

### 5.1 Core identifier

**`agent_type_code`** — immutable registry key; one of 22 occupant codes in §4 and §6.

### 5.2 Required fields (reality model)

```text
agent_reality_object {
  // Identity
  agent_type_code                   // required — e.g. AG_COUPLING_STEWARD
  occupant_domain_layer             // required — trace | attention | identity | boundary |
                                    //            commitment | execution | verification |
                                    //            operational | temporal | corrective

  // Definition
  occupant_class_subject            // required — short noun phrase: what occupant class is
  occupant_purpose_statement        // required — canonical bounded-coverage form (not product name)

  // Upstream binding (conceptual — not storage)
  source_role_type_codes[]          // required — role domains this class may occupy
  required_tool_type_codes[]        // required — capabilities class may operate (must be TS_AVAILABLE+ to reach AS_ELIGIBLE)
  source_workflow_type_codes[]      // required — workflows where class participates
  source_contract_type_codes[]      // required — upstream obligations class supports
  default_workflow_posture          // required — WP_* (see §8)
  lifecycle_state_codes[]           // required — stages where occupant domain is structurally pressured
  product_class_affinity[]          // required — classes where criticality elevates

  // Classification
  default_weight_class              // required — AW_* (see §11)
  default_dominance_posture         // required — AP_* (see §5.3)

  // Occupant model (descriptive only)
  coverage_obligations[]            // required — what coverage outputs class may produce when eligible
  prerequisite_agent_type_codes[]   // optional — upstream occupant classes at AS_ELIGIBLE
  prerequisite_role_state           // required — minimum role state for pressure (typically RS_REQUIRED)
  prerequisite_tool_states[]        // required — minimum tool states for eligibility
  expected_coverage_outputs[]       // required — output categories producible when AS_ELIGIBLE
  typical_unoccupancy_signal        // required — one-line occupant-gap indicator

  // Failure surface
  failure_impact_scope              // required — what breaks when class undefined or overbound
  overbound_risk_domains[]          // optional — roles commonly over-claimed by agents

  // Boundaries
  is_role                           // required — always false
  is_tool                           // required — always false
  is_workflow                       // required — always false
  is_prompt                         // required — always false
  is_runtime                        // required — always false
  is_automation                     // required — always false
  is_human                          // required — always false
}
```

### 5.3 Dominance postures (`AP_*`)

| Posture | Code | Meaning |
|---------|------|---------|
| **Dormant** | `AP_DORMANT` | Occupant class not material at current stage/class |
| **Latent** | `AP_LATENT` | Class exists structurally; human-only coverage typical |
| **Pressured** | `AP_PRESSURED` | Role `RS_REQUIRED`; occupant class consideration mandatory |
| **Dominant** | `AP_DOMINANT` | Highest occupant pressure in context slice |
| **Blocking** | `AP_BLOCKING` | Coverage gap if no occupant class eligible and human coverage absent |

### 5.4 Context instance (conceptual)

```text
nova_agent_context {
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  contract_type_code,
  workflow_type_code,
  role_type_code,
  tool_type_code,
  agent_type_code,
  effective_weight_class,           // AW_*
  agent_state_code,                 // AS_*
  workflow_participation_posture,   // WP_*
  coverage_depth_expectation        // from role + tool + workflow V-target
}
```

**Non-claims:** no `agent_card_id`, no `prompt_ref`, no `model_id`, no `runtime_ref`, no `assignee_id` — those belong to Agent Cards / Prompts / Runtime / Staffing layers (future), explicitly out of scope.

---

## 6. Role → Agent Mapping

Core mapping: every `role_type_code` at `RS_REQUIRED`+ **enables** primary occupant class eligibility plus cross-cutting trace/verification occupant classes.

### 6.1 Primary mapping (1:1 role → agent)

| `role_type_code` | Primary `agent_type_code` | Occupant class activated |
|------------------|---------------------------|--------------------------|
| `RL_INTAKE` | `AG_CONTEXT_BINDER` | Intake/context binding coverage |
| `RL_PRODUCT` | `AG_IDENTITY_STEWARD` | Identity/audience coverage |
| `RL_CLASSIFICATION` | `AG_CLASS_REGISTRAR` | Class/tier binding coverage |
| `RL_CHARTER` | `AG_BOUNDARY_STEWARD` | Scope charter coverage |
| `RL_UX` | `AG_EXPERIENCE_STEWARD` | Journey/experience coverage |
| `RL_ARCHITECTURE` | `AG_STRUCTURE_STEWARD` | Technical structure coverage |
| `RL_IMPLEMENTATION` | `AG_IMPLEMENTATION_PRODUCER` | Implementation delivery coverage |
| `RL_VALIDATION` | `AG_VERIFICATION_STEWARD` | Verification coverage |
| `RL_DATA_PRIVACY` | `AG_DATA_STEWARD` | Data/privacy alignment coverage |
| `RL_COMPLIANCE` | `AG_REGULATORY_STEWARD` | Regulatory alignment coverage |
| `RL_COMMERCIAL` | `AG_COMMERCIAL_STEWARD` | Monetization alignment coverage |
| `RL_TRUST_SAFETY` | `AG_SAFETY_STEWARD` | Safety alignment coverage |
| `RL_OPERATIONS` | `AG_SURVIVABILITY_STEWARD` | Survivability coverage |
| `RL_RELEASE` | `AG_RELEASE_STEWARD` | Distribution/rollout coverage |
| `RL_ECOSYSTEM` | `AG_COUPLING_STEWARD` | External coupling coverage |
| `RL_LIFECYCLE` | `AG_LIFECYCLE_STEWARD` | Stage transition coverage |
| `RL_EXPANSION` | `AG_EXPANSION_STEWARD` | Growth charter coverage |
| `RL_INVESTMENT` | `AG_INVESTMENT_STEWARD` | Investment posture coverage |
| `RL_SUNSET` | `AG_SUNSET_STEWARD` | End-of-life coverage |
| `RL_RECOVERY` | `AG_PRESERVATION_STEWARD` | Corrective retreat coverage |

### 6.2 Secondary occupant activations

| Trigger role / condition | Also enables `agent_type_code` | Condition |
|--------------------------|----------------------------------|-----------|
| Any `RL_*` at `RW_STRUCTURAL`+ | `AG_DECISION_TRACE_STEWARD` | Decision-backed work |
| Any alignment `RL_*` at `RS_REQUIRED` | `AG_OBLIGATION_TRACE_STEWARD` | Contract-backed alignment |
| Any `RL_*` at `RW_COORDINATED`+ (via workflow) | `AG_VERIFICATION_STEWARD` | V-target expected |
| `RL_IMPLEMENTATION` at Proof+ | `AG_BOUNDARY_STEWARD` | Charter constraint |
| `RL_LIFECYCLE` Production transition | `AG_SURVIVABILITY_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_RELEASE_STEWARD` | Full occupant set |
| `RL_ECOSYSTEM` per deploy | `AG_COUPLING_STEWARD` re-pressured | ORCA discipline |
| `RL_EXPANSION` + geo | `AG_REGULATORY_STEWARD`, `AG_DATA_STEWARD` | Jurisdiction |
| `RL_SUNSET` | `AG_DATA_STEWARD`, `AG_REGULATORY_STEWARD` | Terminal obligations |
| Any `RW_CRITICAL`+ breach | `AG_PRESERVATION_STEWARD` | Corrective occupant |

### 6.3 Role weight → agent weight elevation

| Role weight | Typical agent weight | Notes |
|-------------|----------------------|-------|
| `RW_SUPPORTING` | `AW_LATENT` or `AW_SUPPORTIVE` | Human-only coverage often sufficient |
| `RW_STRUCTURAL` | `AW_OPERATIONAL` or `AW_STRUCTURAL` | Occupant class must be explicitly eligible |
| `RW_CRITICAL` | `AW_STRUCTURAL` or `AW_CRITICAL` | Overbound or absent = coverage failure |
| `RW_TERMINAL` | `AW_TERMINAL` | Irreversible path occupant |

### 6.4 Mapping diagram

```text
RL_INTAKE ──────────────► AG_CONTEXT_BINDER
RL_PRODUCT ─────────────► AG_IDENTITY_STEWARD
RL_CLASSIFICATION ──────► AG_CLASS_REGISTRAR
RL_CHARTER ─────────────► AG_BOUNDARY_STEWARD ──► AG_IMPLEMENTATION_PRODUCER (constraint)
RL_UX ──────────────────► AG_EXPERIENCE_STEWARD ─► AG_IMPLEMENTATION_PRODUCER (constraint)
RL_ARCHITECTURE ────────► AG_STRUCTURE_STEWARD ──► AG_IMPLEMENTATION_PRODUCER · AG_VERIFICATION_STEWARD
RL_IMPLEMENTATION ──────► AG_IMPLEMENTATION_PRODUCER
RL_VALIDATION ──────────► AG_VERIFICATION_STEWARD (cross-cutting)
RL_DATA_PRIVACY ────────► AG_DATA_STEWARD
RL_COMPLIANCE ──────────► AG_REGULATORY_STEWARD
RL_COMMERCIAL ──────────► AG_COMMERCIAL_STEWARD
RL_TRUST_SAFETY ────────► AG_SAFETY_STEWARD
RL_OPERATIONS ──────────► AG_SURVIVABILITY_STEWARD
RL_RELEASE ─────────────► AG_RELEASE_STEWARD
RL_ECOSYSTEM ───────────► AG_COUPLING_STEWARD
RL_LIFECYCLE ───────────► AG_LIFECYCLE_STEWARD
RL_EXPANSION ───────────► AG_EXPANSION_STEWARD
RL_INVESTMENT ──────────► AG_INVESTMENT_STEWARD
RL_SUNSET ──────────────► AG_SUNSET_STEWARD
RL_RECOVERY ────────────► AG_PRESERVATION_STEWARD

All RL_* at RW_STRUCTURAL+ ─► AG_DECISION_TRACE_STEWARD · AG_OBLIGATION_TRACE_STEWARD
All alignment RS_REQUIRED ──► AG_VERIFICATION_STEWARD
Any RW_CRITICAL+ breach ───► AG_PRESERVATION_STEWARD
```

### 6.5 Example chain

```text
RL_COMPLIANCE (RS_REQUIRED, RW_CRITICAL)
    ↓ requires capability
TL_REGULATORY_EVIDENCE (TS_AVAILABLE, TW_CRITICAL)
    ↓ enables occupant class
AG_REGULATORY_STEWARD (AS_ELIGIBLE, AW_CRITICAL)
    ↓ plus cross-cutting
AG_VERIFICATION_STEWARD · AG_OBLIGATION_TRACE_STEWARD · AG_DECISION_TRACE_STEWARD
    ↓ produces (future Agent Cards layer binds instances)
regulatory coverage outputs + V2 verification bundle traceable to CTR_COMPLIANCE
```

No prompts. No agent cards. No runtime. Only occupant class reality.

---

## 7. Tool → Agent Mapping

Tool availability **enables** occupant class eligibility. Agent class without available capability remains `AS_CONSTRAINED`.

### 7.1 Primary mapping (1:1 tool → agent)

| `tool_type_code` | Primary `agent_type_code` | Capability enables |
|------------------|---------------------------|-------------------|
| `TL_DECISION_TRACE` | `AG_DECISION_TRACE_STEWARD` | Decision trace coverage |
| `TL_OBLIGATION_TRACE` | `AG_OBLIGATION_TRACE_STEWARD` | Obligation trace coverage |
| `TL_CONTEXT_BINDING` | `AG_CONTEXT_BINDER` | Intake binding coverage |
| `TL_IDENTITY_STEWARDSHIP` | `AG_IDENTITY_STEWARD` | Identity stewardship coverage |
| `TL_CLASS_REGISTRY` | `AG_CLASS_REGISTRAR` | Class registry coverage |
| `TL_BOUNDARY_STEWARDSHIP` | `AG_BOUNDARY_STEWARD` | Boundary stewardship coverage |
| `TL_EXPERIENCE_MODELING` | `AG_EXPERIENCE_STEWARD` | Experience modeling coverage |
| `TL_STRUCTURE_DEFINITION` | `AG_STRUCTURE_STEWARD` | Structure definition coverage |
| `TL_ARTIFACT_LINEAGE` | `AG_IMPLEMENTATION_PRODUCER` | Artifact production coverage |
| `TL_VERIFICATION_EVIDENCE` | `AG_VERIFICATION_STEWARD` | Verification coverage |
| `TL_DATA_TRUTH` | `AG_DATA_STEWARD` | Data truth coverage |
| `TL_REGULATORY_EVIDENCE` | `AG_REGULATORY_STEWARD` | Regulatory evidence coverage |
| `TL_COMMERCIAL_TRUTH` | `AG_COMMERCIAL_STEWARD` | Commercial truth coverage |
| `TL_SAFETY_ASSESSMENT` | `AG_SAFETY_STEWARD` | Safety assessment coverage |
| `TL_SURVIVABILITY_POSTURE` | `AG_SURVIVABILITY_STEWARD` | Survivability coverage |
| `TL_RELEASE_COORDINATION` | `AG_RELEASE_STEWARD` | Release coordination coverage |
| `TL_COUPLING_REGISTRY` | `AG_COUPLING_STEWARD` | Coupling registry coverage |
| `TL_LIFECYCLE_TRUTH` | `AG_LIFECYCLE_STEWARD` | Lifecycle truth coverage |
| `TL_EXPANSION_CHARTER` | `AG_EXPANSION_STEWARD` | Expansion charter coverage |
| `TL_INVESTMENT_POSTURE` | `AG_INVESTMENT_STEWARD` | Investment posture coverage |
| `TL_SUNSET_EXECUTION` | `AG_SUNSET_STEWARD` | Sunset execution coverage |
| `TL_PRESERVATION_RECOVERY` | `AG_PRESERVATION_STEWARD` | Preservation/recovery coverage |

### 7.2 Tool state → agent state gate

| Tool state | Agent state impact |
|------------|-------------------|
| `TS_LATENT` | `AS_LATENT` — capability not required; occupant not pressured |
| `TS_REQUIRED` | `AS_PRESSURED` — role needs coverage; occupant consideration starts |
| `TS_AVAILABLE` | `AS_ELIGIBLE` — occupant class may assume coverage (human or future instance) |
| `TS_CONSTRAINED` | `AS_CONSTRAINED` — prerequisite capability gap blocks eligibility |
| `TS_DEGRADED` | `AS_CONSTRAINED` or overbound risk — outputs untrusted |
| `TS_FRAGMENTED` | `AS_CONSTRAINED` — occupant cannot produce single truth surface |
| `TS_SUPERSEDED` | `AS_SUPERSEDED` | 
| `TS_DORMANT` | `AS_DORMANT` |

### 7.3 Capability depth → occupant scope

| Tool weight | Agent may claim coverage depth |
|-------------|-------------------------------|
| `TW_LATENT` | Advisory outputs only — `WP_ADVISORY` |
| `TW_SUPPORTIVE` | Partial domain assistance — `WP_SECONDARY` |
| `TW_OPERATIONAL` | Primary stream coverage — `WP_PRIMARY` when role `RS_REQUIRED` |
| `TW_STRUCTURAL` | Full domain coverage within role boundary — `WP_PRIMARY` |
| `TW_CRITICAL` | Full domain; overbound forbidden — `WP_PRIMARY` strict |
| `TW_TERMINAL` | Terminal path only; paired human review expected — `WP_PRIMARY` + escalation |

---

## 8. Workflow Participation Model

Agents **participate in** workflows; they **do not define** workflows. Participation posture describes how an occupant class relates to structured work when eligible.

### 8.1 Participation postures (`WP_*`)

| Posture | Code | Meaning | Typical agent families |
|---------|------|---------|------------------------|
| **Primary** | `WP_PRIMARY` | Main occupant class for workflow's primary role coverage | Domain-aligned `AG_*` stewards/producers |
| **Secondary** | `WP_SECONDARY` | Supports primary coverage; does not own accountability surface | Charter constraint on build; trace stewards |
| **Cross-cutting** | `WP_CROSS_CUTTING` | Spans multiple workflows; overlay participation | `AG_VERIFICATION_STEWARD`, trace stewards |
| **Advisory** | `WP_ADVISORY` | Produces evidence or drafts; human retains coverage claim | Early Concept identity/class work |
| **Event-bound** | `WP_EVENT_BOUND` | Activates on deploy, violation, or transition event | `AG_COUPLING_STEWARD`, `AG_PRESERVATION_STEWARD` |

### 8.2 Default posture by workflow family

| `workflow_type_code` | Primary agent | Secondary agents | Cross-cutting |
|----------------------|---------------|------------------|---------------|
| `WF_INTAKE` | `AG_CONTEXT_BINDER` | — | `AG_DECISION_TRACE_STEWARD` |
| `WF_DEFINITION` | `AG_IDENTITY_STEWARD` | — | trace stewards |
| `WF_CLASSIFICATION` | `AG_CLASS_REGISTRAR` | — | trace stewards |
| `WF_CHARTER` | `AG_BOUNDARY_STEWARD` | — | `AG_VERIFICATION_STEWARD` |
| `WF_UX_JOURNEY` | `AG_EXPERIENCE_STEWARD` | — | verification |
| `WF_ARCHITECTURE` | `AG_STRUCTURE_STEWARD` | — | verification |
| `WF_BUILD` | `AG_IMPLEMENTATION_PRODUCER` | `AG_BOUNDARY_STEWARD` | verification |
| `WF_VALIDATION` | `AG_VERIFICATION_STEWARD` | all alignment stewards | — |
| `WF_DATA_ALIGNMENT` | `AG_DATA_STEWARD` | — | verification |
| `WF_COMPLIANCE_ALIGNMENT` | `AG_REGULATORY_STEWARD` | — | verification |
| `WF_COMMERCIAL_ALIGNMENT` | `AG_COMMERCIAL_STEWARD` | — | verification |
| `WF_TRUST_SAFETY_ALIGNMENT` | `AG_SAFETY_STEWARD` | — | verification |
| `WF_OPERATIONS_READINESS` | `AG_SURVIVABILITY_STEWARD` | — | verification |
| `WF_RELEASE` | `AG_RELEASE_STEWARD` | `AG_COUPLING_STEWARD` (if coupled) | verification |
| `WF_ECOSYSTEM_SYNC` | `AG_COUPLING_STEWARD` | `WP_EVENT_BOUND` | obligation trace |
| `WF_LIFECYCLE_TRANSITION` | `AG_LIFECYCLE_STEWARD` | `AG_PRESERVATION_STEWARD` | verification |
| `WF_EXPANSION` | `AG_EXPANSION_STEWARD` | regulatory/data stewards | verification |
| `WF_INVESTMENT_REVIEW` | `AG_INVESTMENT_STEWARD` | — | trace |
| `WF_SUNSET` | `AG_SUNSET_STEWARD` | data/regulatory stewards | verification |
| `WF_RECOVERY` | `AG_PRESERVATION_STEWARD` | `WP_EVENT_BOUND` | verification |

### 8.3 Participation rules

1. **One primary posture per agent per workflow activation** — no duplicate primary claims
2. **Cross-cutting agents never substitute for primary role coverage** — verification verifies; does not replace compliance domain
3. **Event-bound agents re-pressure on each trigger** — ORCA per-deploy; MARS pre-transition
4. **Advisory posture cannot satisfy `RS_COVERED` alone at `RW_STRUCTURAL`+** — human or primary occupant must claim coverage
5. **Agent participation requires workflow activation** — no orphan agent domains

---

## 9. Lifecycle Agent Pressure Matrix

**Dominant** = highest occupant pressure if class undefined/overbound; **Active** = required secondary; **Latent** = human-only typical; **Dormant** = atypical.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `AG_CONTEXT_BINDER`, `AG_IDENTITY_STEWARD` | `AG_CLASS_REGISTRAR` | `AG_DECISION_TRACE_STEWARD` | `AG_SURVIVABILITY_STEWARD`, `AG_REGULATORY_STEWARD` |
| **`LC_DISCOVERY`** | `AG_IDENTITY_STEWARD`, `AG_CLASS_REGISTRAR`, `AG_BOUNDARY_STEWARD` | `AG_EXPERIENCE_STEWARD`, `AG_DATA_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_COMMERCIAL_STEWARD`, `AG_SAFETY_STEWARD`, `AG_COUPLING_STEWARD` | `AG_STRUCTURE_STEWARD` | `AG_SURVIVABILITY_STEWARD` (full) |
| **`LC_PROOF`** | `AG_BOUNDARY_STEWARD`, `AG_LIFECYCLE_STEWARD`, `AG_EXPERIENCE_STEWARD`, `AG_IMPLEMENTATION_PRODUCER` | `AG_STRUCTURE_STEWARD`, `AG_VERIFICATION_STEWARD`, `AG_IDENTITY_STEWARD` | `AG_DATA_STEWARD` | `AG_SURVIVABILITY_STEWARD` (full) |
| **`LC_PILOT`** | `AG_LIFECYCLE_STEWARD`, `AG_SURVIVABILITY_STEWARD` (lite), `AG_RELEASE_STEWARD`, `AG_VERIFICATION_STEWARD` | `AG_COMMERCIAL_STEWARD`, `AG_SAFETY_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_DATA_STEWARD` | `AG_STRUCTURE_STEWARD` | `AG_EXPANSION_STEWARD` |
| **`LC_PRODUCTION`** | `AG_LIFECYCLE_STEWARD`, `AG_SURVIVABILITY_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_RELEASE_STEWARD`, `AG_VERIFICATION_STEWARD` | `AG_STRUCTURE_STEWARD`, `AG_DATA_STEWARD`, `AG_COMMERCIAL_STEWARD`, `AG_SAFETY_STEWARD`, `AG_IMPLEMENTATION_PRODUCER` | `AG_EXPANSION_STEWARD` | `AG_SUNSET_STEWARD` |
| **`LC_GROWTH`** | `AG_EXPANSION_STEWARD`, `AG_LIFECYCLE_STEWARD`, `AG_STRUCTURE_STEWARD`, `AG_VERIFICATION_STEWARD` | `AG_REGULATORY_STEWARD`, `AG_COMMERCIAL_STEWARD`, `AG_SAFETY_STEWARD`, `AG_BOUNDARY_STEWARD` | `AG_EXPERIENCE_STEWARD` | `AG_CONTEXT_BINDER` |
| **`LC_MATURE`** | `AG_INVESTMENT_STEWARD`, `AG_LIFECYCLE_STEWARD` | `AG_SURVIVABILITY_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_IMPLEMENTATION_PRODUCER` | `AG_EXPANSION_STEWARD` | `AG_IDENTITY_STEWARD` (major) |
| **`LC_LEGACY`** | `AG_INVESTMENT_STEWARD`, `AG_SUNSET_STEWARD`, `AG_LIFECYCLE_STEWARD` | `AG_SURVIVABILITY_STEWARD` (minimal), `AG_REGULATORY_STEWARD`, `AG_DATA_STEWARD` | `AG_COUPLING_STEWARD` | `AG_EXPANSION_STEWARD` |
| **`LC_SUNSET`** | `AG_SUNSET_STEWARD`, `AG_DATA_STEWARD`, `AG_LIFECYCLE_STEWARD` | `AG_REGULATORY_STEWARD`, `AG_SURVIVABILITY_STEWARD`, `AG_RELEASE_STEWARD` | `AG_COUPLING_STEWARD` | `AG_COMMERCIAL_STEWARD`, `AG_EXPANSION_STEWARD` |
| **`LC_HOLD`** | `AG_CONTEXT_BINDER`, `AG_LIFECYCLE_STEWARD` | All prior-stage classes — **staleness review** via `AG_VERIFICATION_STEWARD` | — | New `AG_EXPANSION_STEWARD` |

### 9.1 Stage-critical occupant questions

| Stage | If only three occupant classes must be eligible |
|-------|------------------------------------------------|
| `LC_CONCEPT` | `AG_CONTEXT_BINDER` · `AG_IDENTITY_STEWARD` · `AG_DECISION_TRACE_STEWARD` |
| `LC_DISCOVERY` | `AG_CLASS_REGISTRAR` · `AG_IDENTITY_STEWARD` · `AG_OBLIGATION_TRACE_STEWARD` |
| `LC_PROOF` | `AG_BOUNDARY_STEWARD` · `AG_IMPLEMENTATION_PRODUCER` · `AG_LIFECYCLE_STEWARD` |
| `LC_PILOT` | `AG_SURVIVABILITY_STEWARD` · `AG_RELEASE_STEWARD` · `AG_VERIFICATION_STEWARD` |
| `LC_PRODUCTION` | `AG_SURVIVABILITY_STEWARD` · `AG_REGULATORY_STEWARD` · `AG_RELEASE_STEWARD` |
| `LC_GROWTH` | `AG_EXPANSION_STEWARD` · `AG_STRUCTURE_STEWARD` · `AG_REGULATORY_STEWARD` |
| `LC_MATURE` | `AG_INVESTMENT_STEWARD` · `AG_SURVIVABILITY_STEWARD` · `AG_VERIFICATION_STEWARD` |
| `LC_LEGACY` | `AG_INVESTMENT_STEWARD` · `AG_SUNSET_STEWARD` · `AG_PRESERVATION_STEWARD` |
| `LC_SUNSET` | `AG_SUNSET_STEWARD` · `AG_DATA_STEWARD` · `AG_REGULATORY_STEWARD` |

---

## 10. Product Class Agent Pressure Matrix

Criticality: **●** Critical · **◐** Elevated · **○** Standard · **—** Rarely material

| Occupant domain | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-----------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `AG_DECISION_TRACE_STEWARD` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `AG_OBLIGATION_TRACE_STEWARD` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AG_CONTEXT_BINDER` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `AG_IDENTITY_STEWARD` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `AG_CLASS_REGISTRAR` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AG_BOUNDARY_STEWARD` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `AG_EXPERIENCE_STEWARD` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `AG_STRUCTURE_STEWARD` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `AG_IMPLEMENTATION_PRODUCER` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AG_VERIFICATION_STEWARD` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AG_DATA_STEWARD` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `AG_REGULATORY_STEWARD` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `AG_COMMERCIAL_STEWARD` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `AG_SAFETY_STEWARD` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `AG_SURVIVABILITY_STEWARD` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `AG_RELEASE_STEWARD` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `AG_COUPLING_STEWARD` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `AG_LIFECYCLE_STEWARD` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `AG_EXPANSION_STEWARD` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `AG_INVESTMENT_STEWARD` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `AG_SUNSET_STEWARD` | ◐ | ◐ | ○ | ○ | ● | ● | ● | ● |
| `AG_PRESERVATION_STEWARD` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |

### 10.1 Class-specific occupant amplifications

| Class | Occupant classes disproportionately critical |
|-------|---------------------------------------------|
| **`COMMERCE`** | `AG_COMMERCIAL_STEWARD`, `AG_SURVIVABILITY_STEWARD`, `AG_EXPERIENCE_STEWARD`, `AG_VERIFICATION_STEWARD` |
| **`FIELD_OPERATIONS`** | `AG_STRUCTURE_STEWARD`, `AG_BOUNDARY_STEWARD`, `AG_DATA_STEWARD`, `AG_PRESERVATION_STEWARD` |
| **`AI_ASSISTANT`** | `AG_SAFETY_STEWARD`, `AG_DATA_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_SURVIVABILITY_STEWARD` |
| **`UTILITY_TOOL`** | `AG_BOUNDARY_STEWARD`, `AG_CLASS_REGISTRAR`; most ○ unless triggers |
| **`MARKETPLACE`** | `AG_SAFETY_STEWARD`, `AG_COMMERCIAL_STEWARD`, `AG_COUPLING_STEWARD`, `AG_VERIFICATION_STEWARD` |
| **`HEALTH_MEDICAL`** | `AG_REGULATORY_STEWARD`, `AG_DATA_STEWARD`, `AG_SAFETY_STEWARD`, `AG_VERIFICATION_STEWARD` |
| **`FINTECH_WALLET`** | `AG_REGULATORY_STEWARD`, `AG_COMMERCIAL_STEWARD`, `AG_STRUCTURE_STEWARD`, `AG_VERIFICATION_STEWARD` |
| **`AI_AGENT_CONSOLE`** | `AG_SAFETY_STEWARD`, `AG_REGULATORY_STEWARD`, `AG_STRUCTURE_STEWARD`, `AG_PRESERVATION_STEWARD` |

**Tier modifier:** T3+ elevates `AG_STRUCTURE_STEWARD`, `AG_SURVIVABILITY_STEWARD`, `AG_VERIFICATION_STEWARD` to blocking at Production; T4 elevates nearly all alignment occupant classes to ●.

---

## 11. Agent Weight Model

Derived from **influence radius × workflow coverage breadth × dependency depth on role/tool chain** — not from model size, token cost, or vendor hype.

### 11.1 Weight classes

#### `AW_LATENT`

| Field | Value |
|-------|-------|
| **Influence radius** | Single artifact stream; optional occupant consideration |
| **Workflow coverage** | Advisory or draft only |
| **Dependency depth** | Shallow — human coverage default |
| **Examples** | `AG_CONTEXT_BINDER` at Concept hypothesis |

---

#### `AW_SUPPORTIVE`

| Field | Value |
|-------|-------|
| **Influence radius** | Single role/workflow stream |
| **Workflow coverage** | Partial assistance to human coverage |
| **Dependency depth** | Low–medium |
| **Examples** | `AG_INVESTMENT_STEWARD` at Mature lite review |

---

#### `AW_OPERATIONAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Multi-artifact; daily participation |
| **Workflow coverage** | Primary stream when human co-coverage exists |
| **Dependency depth** | Medium — role+tool chain required |
| **Examples** | `AG_EXPERIENCE_STEWARD` at Proof; `AG_IMPLEMENTATION_PRODUCER` during build |

---

#### `AW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Product-wide coverage surface |
| **Workflow coverage** | Primary occupant for domain at `RS_REQUIRED` |
| **Dependency depth** | High — mis-scope blocks downstream claims |
| **Examples** | `AG_BOUNDARY_STEWARD` at Proof exit; `AG_COUPLING_STEWARD` per-deploy |

---

#### `AW_CRITICAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Ops/legal/users depend on occupant coverage quality |
| **Workflow coverage** | Full domain within role boundary |
| **Dependency depth** | High — overbound = integrity failure |
| **Examples** | `AG_REGULATORY_STEWARD` Production; `AG_SURVIVABILITY_STEWARD` Production |

---

#### `AW_TERMINAL`

| Field | Value |
|-------|-------|
| **Influence radius** | Irreversible or impractical to undo |
| **Workflow coverage** | Terminal path execution support only |
| **Dependency depth** | Very high — paired human authority expected |
| **Examples** | `AG_SUNSET_STEWARD` decommission; mass deletion paths |

### 11.2 Default weight by agent domain (selected)

| Domain | Default weight | Elevates to `AW_CRITICAL` when |
|--------|----------------|--------------------------------|
| `AG_DECISION_TRACE_STEWARD` | `AW_OPERATIONAL` | `RW_STRUCTURAL`+ roles active |
| `AG_OBLIGATION_TRACE_STEWARD` | `AW_OPERATIONAL` | Any alignment workflow active |
| `AG_VERIFICATION_STEWARD` | `AW_STRUCTURAL` | `CW_CRITICAL`+ contracts under test |
| `AG_SURVIVABILITY_STEWARD` | `AW_STRUCTURAL` | Production entry |
| `AG_REGULATORY_STEWARD` | `AW_CRITICAL` | Extended classes always |
| `AG_COUPLING_STEWARD` | `AW_STRUCTURAL` | Deep embed; per-deploy ORCA |
| `AG_PRESERVATION_STEWARD` | `AW_CRITICAL` | Production rollback; regulated |
| `AG_SUNSET_STEWARD` | `AW_TERMINAL` | Decommission execution |

---

## 12. Agent State Model

Agent states describe **eligibility and scope posture of occupant class domains**, not runtime health, prompt version, or agent card assignment status.

### 12.1 State codes

| State | Code | Meaning |
|-------|------|---------|
| **Latent** | `AS_LATENT` | Role/workflow exists; occupant class not yet structurally pressured |
| **Pressured** | `AS_PRESSURED` | Role `RS_REQUIRED`; occupant class consideration mandatory |
| **Eligible** | `AS_ELIGIBLE` | Role pressured + required tools `TS_AVAILABLE`; class may occupy coverage |
| **Constrained** | `AS_CONSTRAINED` | Class defined but blocked by role/tool prerequisite gap |
| **Overbound** | `AS_OVERBOUND` | Class scope exceeds role boundary or claims multiple primary domains |
| **Superseded** | `AS_SUPERSEDED` | Lifecycle/decision/workflow change replaced occupant pressure |
| **Dormant** | `AS_DORMANT` | Not applicable at current stage/class |
| **Advisory-only** | `AS_ADVISORY` | Class may produce drafts/evidence; cannot alone satisfy `RS_COVERED` at `RW_STRUCTURAL`+ |

### 12.2 State transition rules (descriptive)

```text
AS_LATENT ──(role RS_REQUIRED+)──► AS_PRESSURED
AS_PRESSURED ──(tools TS_AVAILABLE+)──► AS_ELIGIBLE
AS_PRESSURED ──(tools unavailable)──► AS_CONSTRAINED
AS_ELIGIBLE ──(scope exceeds role)──► AS_OVERBOUND
AS_OVERBOUND ──(scope reconciled)──► AS_ELIGIBLE
AS_ELIGIBLE ──(prerequisite role/tool gap)──► AS_CONSTRAINED
AS_CONSTRAINED ──(prerequisites satisfied)──► AS_ELIGIBLE
AS_* ──(lifecycle/workflow change)──► AS_SUPERSEDED
AS_* ──(stage/class irrelevant)──► AS_DORMANT
AS_PRESSURED + RW_SUPPORTING only ──► AS_ADVISORY (optional)
```

### 12.3 Deliberate exclusions

| Rejected state | Reason | Correct layer |
|----------------|--------|---------------|
| **running** | Runtime health | Runtime |
| **deployed** | Instance binding | Agent Cards |
| **prompted** | Prompt binding | Prompts |
| **assigned** | Person/instance binding | Staffing / Agent Cards |
| **autonomous** | Autonomy claim | Automation mythology |
| **orchestrated** | Coordination graph | Orchestration |

### 12.4 Eligible vs fake eligibility

**`AS_ELIGIBLE` requires:**

1. Named `source_role_type_code` at `RS_REQUIRED` or `RS_COVERED`
2. All `required_tool_type_codes[]` at `TS_AVAILABLE` (not degraded/fragmented at `TW_STRUCTURAL`+)
3. Stated coverage depth matching role + workflow V-target
4. No `AS_OVERBOUND` on same role domain
5. Workflow participation posture declared (`WP_*`)

**Not sufficient for `AS_ELIGIBLE`:** agent card exists; prompt written; model API available; «we use Cursor agents»; bot deployed in Slack.

---

## 13. Agent Failure Patterns

Derived from Tool Failure Patterns §12, Role Failure Patterns §12, Website Factory drift, ORCA battle, MARS survivability — reframed as **occupant domain failures**.

| Pattern | Signal | Root agent failure | Affected occupant classes |
|---------|--------|-------------------|---------------------------|
| **Agent-first architecture** | Agents designed before role/tool map | Skipped RBM chain | All — premature |
| **Roleless agent** | Bot exists; no `source_role_type_code` | Agent without responsibility boundary | Any |
| **Toolless agent** | Agent card references no `tool_type_code` | Capability bypass | Any |
| **Universal agent** | One assistant claims all domains | Unbounded scope | All alignment |
| **Duplicate agent domains** | Two classes claim same primary role | Overbound/duplicate taxonomy | Same `RL_*` pair |
| **Workflow bypass agent** | Agent executes tasks outside active `WF_*` | Participation without workflow | Orphan execution |
| **Capability bypass agent** | Agent produces outputs without `TS_AVAILABLE` tools | Fake eligibility | `TW_CRITICAL`+ |
| **Agent-as-role** | «The agent is our QA lead» | Role substitution | `RL_VALIDATION` |
| **Agent-as-tool** | «The agent is our Jira» | Tool substitution | Operational |
| **Automation mythology** | «Agent will figure it out» | Autonomy before coverage | Discovery/Proof |
| **Handoff agent absent** | Delivery complete; no `AG_SURVIVABILITY_STEWARD` consideration | Website Factory analog | `AG_SURVIVABILITY_STEWARD` |
| **Sync agent once-only** | URL drift; `AG_COUPLING_STEWARD` dormant after deploy | ORCA discipline failure | `AG_COUPLING_STEWARD` |
| **Preservation agent absent** | Transition without snapshot | MARS discipline failure | `AG_PRESERVATION_STEWARD` |
| **Verification agent theater** | Checklist bot; no V-level evidence | `AG_VERIFICATION_STEWARD` overbound | Cross-cutting |
| **Fake AS_ELIGIBLE** | Prompt exists; tools `TS_REQUIRED` | Eligibility theater | Any at `AW_CRITICAL`+ |
| **Runtime mythology** | «It runs in prod so coverage exists» | Runtime substituted for coverage | Production |
| **Prompt-as-reality** | Prompt doc treated as agent domain | Prompt layer confusion | Any |
| **Orchestration-before-agent** | Multi-agent graph before occupant taxonomy | Orchestration premature | All |
| **Human displacement without coverage** | Agent deployed; role `RS_VACANT` | Coverage vacuum | Matching `RL_*` |
| **Semantic/deployed agent split** | Ads agent vs product intent agent desync | ORCA identity/coupling split | `AG_IDENTITY_STEWARD` vs `AG_COUPLING_STEWARD` |

---

## 14. Agent Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-A1** | Every `agent_type_code` must trace to `source_role_type_code` + `required_tool_type_codes[]` | Roleless/toolless agent |
| **AC-A2** | No agent class may exist without prior role and tool registry entries | Agent-before-RBM |
| **AC-A3** | No `AG_IMPLEMENTATION_PRODUCER` at `AW_STRUCTURAL`+ before `AG_BOUNDARY_STEWARD` reaches `AS_ELIGIBLE` | Build before charter occupant |
| **AC-A4** | Extended class: `AG_REGULATORY_STEWARD` and `AG_SAFETY_STEWARD` cannot stay `AS_LATENT` past `LC_DISCOVERY` when alignment workflows active | Compliance occupant vacuum |
| **AC-A5** | Production claim requires `AG_LIFECYCLE_STEWARD`, `AG_SURVIVABILITY_STEWARD`, `AG_REGULATORY_STEWARD` eligible — not inferred from deployed bot | Runtime = coverage confusion |
| **AC-A6** | Same `agent_type_code` at `AW_STRUCTURAL`+ requires lifecycle or tier trigger to re-activate from `AS_SUPERSEDED` | Occupant churn |
| **AC-A7** | No universal or unbounded agent class — every class maps to explicit role scope | Universal agent |
| **AC-A8** | `AW_CRITICAL`+ classes must declare coverage depth before `AS_ELIGIBLE` claim | Fake eligibility |
| **AC-A9** | Pilot with real users requires `AG_SURVIVABILITY_STEWARD` at lite minimum `AS_ELIGIBLE` | Handoff occupant gap |
| **AC-A10** | Identity pivot requires `AG_LIFECYCLE_STEWARD` + `AG_DECISION_TRACE_STEWARD` refresh | Random pivot without trace occupant |
| **AC-A11** | One primary agent class per role domain per workflow activation | Duplicate agent domains |
| **AC-A12** | `AG_CLASS_REGISTRAR` re-required on tier bump or payments/PII/regulated feature | Classification occupant drift |
| **AC-A13** | Undocumented `AW_CRITICAL`+ class at `AS_PRESSURED` = SAFE UNKNOWN in REPORT | Silent critical occupant gap |
| **AC-A14** | `UTILITY_TOOL` T1 exempt from commercial/regulatory agent classes until trigger feature | Over-engineering |
| **AC-A15** | Store/public release requires `AG_RELEASE_STEWARD` + often `AG_LIFECYCLE_STEWARD` eligible | AC-T15 analog |
| **AC-A16** | Software/model name alone cannot define agent class — explicit `agent_type_code` | Vendor/model-first thinking |
| **AC-A17** | Every active `agent_type_code` must trace to `source_workflow_type_code` | Agent without workflow participation |
| **AC-A18** | Duplicate primary claims for same role require reconciliation to single occupant class | Overlapping agent domains |
| **AC-A19** | High-risk lifecycle transitions require `AG_PRESERVATION_STEWARD` eligible before claim | Preservation occupant absent |
| **AC-A20** | `AG_COUPLING_STEWARD` must re-enter `AS_PRESSURED` on each external deploy when `WF_ECOSYSTEM_SYNC` active | One-time sync (ORCA) |
| **AC-A21** | No Agent Card may reference class not in agent registry | Agent Cards before Agent Reality |
| **AC-A22** | No automation design may reference agent class not in registry | Automation before Agents |
| **AC-A23** | `AG_DECISION_TRACE_STEWARD` and `AG_OBLIGATION_TRACE_STEWARD` required for any `WW_COORDINATED`+ workflow participation | Trace occupant absent |
| **AC-A24** | Agent cannot own a `role_type_code` — occupies coverage within domain only | Agent-as-role |
| **AC-A25** | Agent cannot substitute for `tool_type_code` — operates capability, does not define it | Agent-as-tool |
| **AC-A26** | `AS_ADVISORY` cannot alone satisfy `RS_COVERED` at `RW_STRUCTURAL`+ | Advisory overclaim |
| **AC-A27** | No orchestration graph in v1 — occupant taxonomy only | Orchestration premature |

---

## 15. Agent Relationships

### 15.1 Dependency chain

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
│  Tool Reality Model v1      ──► tool_type_code               │
│  Agent Reality Model v1     ──► agent_type_code        ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ occupant classes ready for Agent Cards / Staffing binding
                                ▼
┌─────────────────────────────────────────────────────────────┐
│              AGENT CARDS · PROMPTS · RUNTIME (future)        │
│  Instance bindings: occupant class → specific execution      │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    AUTOMATION (future)                        │
│  Repeated execution compression — requires named agent classes │
└─────────────────────────────────────────────────────────────┘
```

### 15.2 Why agents derive from workflow, role, and tool (not agent-first)

| Input | Provides | Without it |
|-------|----------|------------|
| **`workflow_type_code`** | Which work structure occupant participates in | Random bot tasks |
| **`role_type_code`** | Which responsibility boundary bounds occupant | Universal assistant |
| **`tool_type_code`** | Which capabilities occupant may operate | Agent-as-tool confusion |
| **`agent_type_code`** | The actual occupant class taxonomy | Agent Cards attach to noise |

**Combined pressure function (conceptual):**

```text
agent_pressure(agent_type_code, product_class_code, lifecycle_state_code,
               source_role_type_code, required_tool_type_codes[], source_workflow_type_code, tier)
  → dominance_posture ∈ { dormant, latent, pressured, dominant, blocking }
  → effective_weight_class
  → agent_state_code
  → workflow_participation_posture
  → coverage_depth_expectation
```

### 15.3 Full derivation chain

```text
contract_type_code
    ↓ activates
workflow_type_code
    ↓ requires coverage
role_type_code
    ↓ requires capability
tool_type_code
    ↓ enables occupant class
agent_type_code
    ↓ instantiated by (future — NOT v1)
agent_card / staffing_binding
    ↓ may compress via (future — NOT v1)
automation_binding
```

**Why not Tool → Agent alone?** Tools define *what must be possible*. Roles define *what must be answered for*. Workflows define *what work exists*. Agent class without role scope becomes universal executor; without tool mediation becomes runtime mythology; without workflow participation becomes orphan automation.

**Why not Role → Agent directly?** Role defines accountability surface; tool defines executable capability. Occupant class without named capabilities produces agent-as-role theater — «the bot owns compliance» without `TL_REGULATORY_EVIDENCE` availability.

### 15.4 Cross-agent dependencies

| Upstream occupant / layer | Downstream occupant classes constrained |
|---------------------------|----------------------------------------|
| `AG_DECISION_TRACE_STEWARD` | All coordinated participation |
| `AG_OBLIGATION_TRACE_STEWARD` | All alignment stewards |
| `AG_CLASS_REGISTRAR` | Depth selection for all alignment occupant classes |
| `AG_BOUNDARY_STEWARD` | `AG_IMPLEMENTATION_PRODUCER`, verification scope |
| `AG_STRUCTURE_STEWARD` | `AG_IMPLEMENTATION_PRODUCER`, `AG_EXPANSION_STEWARD` |
| `AG_IDENTITY_STEWARD` | `AG_EXPERIENCE_STEWARD`, `AG_COUPLING_STEWARD` |
| Alignment `AG_*` stewards | `AG_VERIFICATION_STEWARD` at contract V-level |
| `AG_LIFECYCLE_STEWARD` | Re-evaluates dominant occupant classes at new stage |
| `AG_PRESERVATION_STEWARD` | May reset misaligned classes to `AS_PRESSURED` |

---

## 16. Agent Reality Boundaries

### 16.1 What is NOT an agent (v1)

| Artifact | Layer | Why excluded |
|----------|-------|--------------|
| **Workflow** | Workflow Reality | Work structure ≠ occupant class |
| **Role** | Role Reality | Responsibility domain ≠ occupant class |
| **Tool / capability** | Tool Reality | Ability surface ≠ occupant class |
| **Prompt** | Prompts (future) | Instruction artifact ≠ existence class |
| **Agent Card** | Agent Cards (future) | Instance binding ≠ occupant taxonomy |
| **Runtime / hosting** | Runtime (future) | Execution environment ≠ occupant class |
| **Orchestration graph** | Orchestration (future) | Coordination machinery ≠ occupant class |
| **Automation** | Automation (future) | Repeated compression ≠ occupant taxonomy |
| **Employee / contractor** | Staffing | Person ≠ occupant class |
| **Team / department** | Staffing / Org | Group ≠ occupant class |
| **Software product** | Software Implementations | Product ≠ occupant class |
| **LLM model brand** | Model catalog (future) | Model ≠ occupant class |
| **MCP server** | Implementation integration | Integration ≠ occupant class |
| **Approval act** | Approvals (future) | Authority ≠ occupant class |

### 16.2 Boundary tests

| Question | Agent Reality if YES |
|----------|---------------------|
| Removing all bots, prompts, and runtimes, does the occupant class taxonomy still make sense given roles and tools? | Yes |
| Is this primarily a responsibility domain? | No → Role layer |
| Is this primarily a capability domain? | No → Tool layer |
| Is this primarily structured work? | No → Workflow layer |
| Is this a specific deployed instance with prompt and config? | No → Agent Cards layer |
| Does this repeat execution on a schedule/trigger without occupant taxonomy? | No → Automation layer |

### 16.3 Common misuse prevention

| Misuse | Correct handling |
|--------|------------------|
| «Our agent is Cursor» | Map Cursor → Agent Card instance of e.g. `AG_IMPLEMENTATION_PRODUCER` (future) |
| «The compliance agent approves legal» | `AG_REGULATORY_STEWARD` produces evidence; Approvals layer for authority |
| «Multi-agent orchestrator is the architecture» | Orchestration future; name `agent_type_code` per bounded class first |
| «GPT-4 is the QA agent» | Model = implementation; class = `AG_VERIFICATION_STEWARD` |
| «We don't need roles — agents do everything» | Violates AC-A24; role domains mandatory |

---

## 17. Agent Reality vs Agent Cards

Explicit separation — **defined generically in v1; populated in future charter only.**

### 17.1 Two-layer model

```text
┌──────────────────────────────┐
│     AGENT REALITY (v1)        │  agent_type_code — occupant class
│  Implementation-neutral · stable │
└──────────────┬───────────────┘
               │ instantiates (future)
               ▼
┌──────────────────────────────┐
│       AGENT CARDS (future)    │  agent_card_id — NOT in v1
│  Prompt · model · scope · runtime binding │
└──────────────────────────────┘
```

### 17.2 Agent Card object (future schema sketch — NOT v1 design)

```text
agent_card_object {
  agent_type_code,              // required — reality key from this registry
  agent_card_label,             // human label — not governance truth
  source_role_type_code,        // must match agent registry binding
  required_tool_type_codes[],   // must ⊆ registry required tools
  prompt_ref,                   // future Prompts layer
  model_implementation_ref,     // future Model catalog
  runtime_binding_ref,          // future Runtime layer
  workflow_participation_posture, // WP_* — must match or narrow registry default
  effective_from,
  effective_until,
  notes                         // operational — not governance truth
}
```

### 17.3 Reality vs Card responsibilities

| Concern | Agent Reality (v1) | Agent Cards (future) |
|---------|-------------------|----------------------|
| **Existence** | Which occupant classes may exist | Which instance runs |
| **Scope** | Role + tool boundaries | Prompt + runtime constraints |
| **State** | `AS_*` eligibility | deployed, paused, versioned |
| **Failure** | Overbound, roleless, toolless | Runtime errors, prompt drift |
| **Replacement** | Class taxonomy stable | Swap instance; class persists |

**v1 rule:** teams may *use* agents informally; **governance truth** remains `agent_type_code` eligibility, participation posture, and coverage boundaries — not product brands or prompt files.

---

## 18. RBM Mapping

### 18.1 Full chain

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
Agents (AG_*)                   ◄── this document
    ↓ instance binding (future)
Agent Cards / Staffing
    ↓ repeated execution compression (future)
Automation
```

### 18.2 Why Agents come after Tools

| If Agents before Tools | Failure mode |
|------------------------|--------------|
| Deploy bot before `TL_VERIFICATION_EVIDENCE` defined | Agent-as-tool |
| Cursor agent before `RL_IMPLEMENTATION` scope | Roleless agent |
| Universal assistant before capability map | Agent-first architecture |
| Automate QA before verification depth known | Automation mythology |

Tools answer **what must be possible** for coverage outputs. Agents answer **what occupant classes may operate those possibilities** within role boundaries. Without tools, agents attach to software brands; without roles, agents have no accountability boundary.

### 18.3 Why Agent Reality is the final pre-automation layer

| Layer | Question | Automation dependency |
|-------|----------|----------------------|
| Workflow | What work exists? | Cannot automate undefined work |
| Role | What must be covered? | Cannot automate vacuum accountability |
| Tool | What must be possible? | Cannot automate missing capability |
| **Agent** | **What occupant class may execute?** | **Cannot automate unbounded occupant** |
| Automation | What repeats without re-deciding? | Requires all above |

Automation **compresses** execution of already-defined occupant behavior within already-available capabilities within already-covered roles within already-structured workflows. It does **not** invent obligations, domains, capabilities, or occupant scope.

### 18.4 Why Automation cannot be designed before Agent Reality

| Automation design needs | Agent Reality provides |
|-------------------------|------------------------|
| Bounded scope | Named `agent_type_code` per role+tool chain |
| Participation rules | `WP_*` postures |
| Eligibility gates | `AS_*` states |
| Weight/depth limits | `AW_*` classes |
| Anti-chaos | AC-A1–AC-A27 |
| Replacement path | Class stable; instances swappable |

**Without Agent Reality:** automation attaches to prompts and runtimes, duplicates human coverage without domain map, compresses broken processes, and produces **runtime mythology** — «it's automated so it's covered.»

### 18.5 Layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | Decision Reality Model v1 | Complete |
| Contracts | Contract Reality Model v1 | Complete |
| Workflow | Workflow Reality Model v1 | Complete |
| Roles | Role Reality Model v1 | Complete |
| Tools | Tool Reality Model v1 | Complete |
| **Agents** | **Agent Reality Model v1** | **This document — vocabulary complete** |
| Automation | — | Not started — blocked without Agents |

---

## 19. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Agent-first regression | High | AC-A2, AC-A7, §16 boundaries |
| Agent-as-role conflation | High | AC-A24; §2.5 boundary tests |
| Agent-as-tool conflation | High | AC-A25; Tool Reality cross-ref |
| 20-family count vs operator fatigue | Medium | Matrices §9–10; Appendix A |
| Role–agent 1:1 oversimplification | Medium | Secondary activations §6.2; cross-cutting overlays |
| Trace occupant classes skipped | High | AC-A23; ORCA/Website Factory lessons |
| Fake `AS_ELIGIBLE` at scale | High | §12.4; AC-A8 |
| Agent Cards pressure before Reality approved | High | AC-A21; §17 separation |
| Automation charter jump | High | AC-A22; §18.3–18.4 |
| Universal assistant mythology | High | AC-A7 |
| Prior foundation files not all in-repo | Medium | Cross-reference `projects/nova/foundation/` |
| Class matrix oversimplification | Medium | Tier modifier §10.1; SAFE UNKNOWN |
| Governance expansion drift | Medium | No Agent Cards/Prompts/Runtime in v1 |
| AI_AGENT_CONSOLE meta-confusion | Medium | Explicit: console product ≠ occupant taxonomy |

---

## 20. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Optimal count of occupant families (20 vs consolidated) | Operator feedback after 2–3 products through NOVA |
| Machine format for `agent_pressure_instance` | Future intake schema |
| Agent Card ID scheme | First Agent Cards charter (explicitly out of v1) |
| Whether trace stewards merge in v2 | Cross-product trace discipline review |
| Coverage output schema per `AG_*` | Future Evidence/Records charter |
| Human vs agent default occupancy per class | Staffing + Agent Cards charter |
| Prompt layer relationship to `agent_type_code` | First Prompts charter after Agent Cards |
| Runtime health vs `AS_ELIGIBLE` interaction | First Runtime charter |
| Orchestration graph vs `WP_*` mapping | First Orchestration charter |
| Overlap with MARS survivability agents | NOVA ↔ MARS integration charter |
| Exact mapping `AW_*` → automation priority | First Automation charter |
| Whether `AS_OVERBOUND` triggers mandatory escalation | First Production incident through NOVA agents |
| Multi-agent coordination within one `agent_type_code` | Orchestration charter — out of v1 |

**Non-claims preserved:** this model does not assert agent cards, agent registry, prompts, runtime, orchestration, automation, staffing automation, or automated occupant gap detection.

---

## 21. Recommended Next Step

**Single next artifact (human charter required):** choose **one** — not both by default:

1. **NOVA Automation Reality Model v1** — first layer after Agents, defining what may be compressed repeatedly without re-deciding scope; bounded by `agent_type_code` + `AS_ELIGIBLE` + `WP_*`

**OR**

2. **NOVA Agent Cards Charter v1** — first **implementation-layer** artifact: instance bindings for approved `agent_type_code` classes only (still not prompts/runtime/orchestration full design unless human directs)

**Do not skip to:** full Orchestration platform, Prompt Library, Runtime catalog, or Automation engine until human explicitly charters next layer.

**Optional parallel (human choice):** update Tool Reality Model §19 to mark Agents complete; point to Automation or Agent Cards.

**Optional parallel:** commit full NOVA foundation pack under `projects/nova/foundation/`.

---

## Appendix A — Agent Pressure Snapshot template

```markdown
# Agent Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| agent_type_code | dominance_posture | effective_weight | agent_state | workflow_posture | source_role | required_tools |
|-----------------|---------------------|------------------|-------------|------------------|-------------|----------------|
| AG_CONTEXT_BINDER | | | | | | |
| ... | | | | | | |

Dominant occupant classes this stage:
Pressured but not eligible (AS_PRESSURED / AS_CONSTRAINED):
Overbound classes (AS_OVERBOUND):
SAFE UNKNOWN occupant classes:
```

---

## Appendix B — Quick reference: `agent_type_code` registry

| Code | One-line occupant class |
|------|-------------------------|
| `AG_DECISION_TRACE_STEWARD` | Maintain decision-trace coverage participation |
| `AG_OBLIGATION_TRACE_STEWARD` | Maintain obligation-trace coverage participation |
| `AG_CONTEXT_BINDER` | Cover intake/context binding work |
| `AG_IDENTITY_STEWARD` | Cover identity/audience stewardship work |
| `AG_CLASS_REGISTRAR` | Cover class/tier registry work |
| `AG_BOUNDARY_STEWARD` | Cover scope charter stewardship work |
| `AG_EXPERIENCE_STEWARD` | Cover journey/experience modeling work |
| `AG_STRUCTURE_STEWARD` | Cover technical structure stewardship work |
| `AG_IMPLEMENTATION_PRODUCER` | Cover implementation delivery work |
| `AG_VERIFICATION_STEWARD` | Cover cross-cutting verification work |
| `AG_DATA_STEWARD` | Cover data/privacy alignment work |
| `AG_REGULATORY_STEWARD` | Cover regulatory alignment work |
| `AG_COMMERCIAL_STEWARD` | Cover commercial alignment work |
| `AG_SAFETY_STEWARD` | Cover trust/safety assessment work |
| `AG_SURVIVABILITY_STEWARD` | Cover ops/handoff survivability work |
| `AG_RELEASE_STEWARD` | Cover release coordination work |
| `AG_COUPLING_STEWARD` | Cover ecosystem coupling registry work |
| `AG_LIFECYCLE_STEWARD` | Cover lifecycle transition work |
| `AG_EXPANSION_STEWARD` | Cover expansion charter work |
| `AG_INVESTMENT_STEWARD` | Cover investment posture work |
| `AG_SUNSET_STEWARD` | Cover sunset execution work |
| `AG_PRESERVATION_STEWARD` | Cover preservation/recovery work |

---

*End of NOVA Agent Reality Model v1*
