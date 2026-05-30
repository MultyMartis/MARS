# NOVA Workflow Reality Model v1

**Status:** design-only — Reality-layer workflow vocabulary, not workflow engine, not role system, not approval gates, not templates, not automation, not runtime  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → NOVA Contract Reality Model v1 → **this document**  
**Non-claims:** no agents, no orchestration, no automated workflow enforcement, no task/ticket storage, no approval chains, no template library, no role registry, no database schema

**Parent Reality artifacts:**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`
- NOVA Decision Reality Model v1 — structural choice domains per `decision_type_code`
- NOVA Contract Reality Model v1 — obligation domains per `contract_type_code`

**Evidence base:** Website Factory production-drift and handoff-collapse lessons; ORCA semantic-vs-deployed sync and URL registry alignment; MARS survivability snapshot/rollback/recovery discipline; real-world mobile delivery practices adapted to NOVA

---

## 1. Executive Summary

NOVA Workflow Reality Model v1 — **первый execution-oriented artifact NOVA**. Он отвечает на вопрос:

> **«Как продуктовые обязательства становятся структурированной работой?»**

Не «кто выполняет» (Roles), не «каким агентом» (Agents), не «каким инструментом» (Tools), не «каким шаблоном» (Templates), не «кто утверждает» (Approvals).

| Элемент | Содержание |
|---------|------------|
| **18 workflow families** | `WF_INTAKE` … `WF_RECOVERY` — derived taxonomy |
| **Canonical workflow object** | `workflow_type_code` + required reality fields |
| **Workflow registry** | 18 rows with purpose, source contracts, outputs, failure modes |
| **Contract → Workflow mapping** | 18 contract families → activation patterns |
| **Lifecycle workflow pressure matrix** | Dominant workflow families per `LC_*` stage |
| **Product class workflow pressure matrix** | 8 focus classes × workflow criticality |
| **Workflow weight model** | 5 classes: `WW_ROUTINE` → `WW_TERMINAL` |
| **Workflow state model** | 9 states: `WS_LATENT` → `WS_SUPERSEDED` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Workflow Reality (this doc) | Workflow Execution (NOT this) |
|-----------|----------------------------|-------------------------------|
| **Question** | How do obligations become structured work? | Who runs which step with which tool? |
| **Layer** | Reality → Workflow (structure) | Roles · Tools · Agents · Automation (future) |
| **Example** | `WF_COMPLIANCE_ALIGNMENT` exists when `CTR_COMPLIANCE` is active | Legal review meeting Tuesday with named approver |
| **Output** | Vocabulary + obligation→work maps | Task boards, templates, sign-offs, bots |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answered:** «What must be true?» (`contract_type_code`)  
**Workflow Reality answers:** «How does obligation pressure become structured execution work?» (`workflow_type_code`)

Without workflow reality, teams execute tasks without obligation context, contracts remain documents, and work inflates without lifecycle or class discipline.

---

## 2. Workflow Philosophy

### 2.1 What a workflow means inside NOVA

В NOVA **workflow** — это **структурный паттерн превращения обязательств в работу**, который:

1. **Активируется обязательством** — не существует «сам по себе» без `contract_type_code` pressure
2. **Привязан к lifecycle context** — глубина и доминирование зависят от `lifecycle_state_code`
3. **Role-neutral** — описывает *какую работу* и *в какой последовательности*, не *кто* её делает
4. **Производит alignment outputs** — артефакты/состояния, доказывающие honor obligation на уровне V0–V3
5. **Отделён от Production Model P-phases** — P9 build может проходить внутри `WF_BUILD`, но workflow ≠ P-phase

Workflow — **не процесс в BPMN-смысле**. Это **реality vocabulary** для execution structure.

**Website Factory lesson:** handoff collapse = obligations crystallized (`CTR_OPERATIONS`) but **no structured ops-readiness work** (`WF_OPERATIONS_READINESS`) ever activated — delivery files exist, survivability work never sequenced ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)).

**ORCA lesson:** URL registry desync = `CTR_ECOSYSTEM` + `CTR_RELEASE` obligations active, but **`WF_ECOSYSTEM_SYNC` work pattern** absent or run once instead of per deployment ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

### 2.2 Why workflow exists

Contracts **фиксируют что должно оставаться истинным**. Без workflow layer обязательства остаются:

- implicit in tickets;
- assumed from prior projects;
- validated only at crisis;
- disconnected from lifecycle stage.

Workflow **переводит obligation pressure в structured work domains** — без назначения исполнителей.

| Contract says | Workflow structures |
|---------------|----------------------|
| `CTR_COMPLIANCE` must be honored | Compliance alignment work sequence |
| `CTR_SCOPE` boundary exists | Charter definition and boundary verification work |
| `CTR_OPERATIONS` survivability required | Ops readiness work before Production claim |
| `CTR_RELEASE` distribution truth | Release and rollout alignment work |

**MARS Survivability lesson:** snapshot before transition = **`WF_RECOVERY` prerequisite pattern** embedded in lifecycle transition work — not optional heroics ([`snapshot-manifest-standard-v1.md`](../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)).

### 2.3 Why workflow comes after contracts

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random work labels |
| **Lifecycle** | Stage-appropriate work depth | Full ops pack at Concept |
| **Decisions** | Choice domains | Work on wrong problems |
| **Contracts** | Obligation structure | Workflow validates noise |
| **Workflow** | Obligation → work structure | Roles assign arbitrary tasks |

**Workflow без Contract Reality** — process theater:

- QA checklist without knowing which `CTR_*` is under verification
- Release pipeline without `CTR_RELEASE` obligation context
- «Discovery workshop» without `CTR_PRODUCT` / `CTR_CLASSIFICATION` pressure

Contracts **не исполняются** — они описывают commitment. Workflow **структурирует work**, необходимую чтобы honor commitments at expected verification level.

### 2.4 Why workflow is not a role system

| Workflow Reality | Roles (future) |
|------------------|----------------|
| **What work structure** obligation requires | **Who** owns obligation domain |
| `WF_COMPLIANCE_ALIGNMENT` = compliance alignment work pattern | Legal counsel assignment |
| Survives team reorg | Resets when people change |
| Role-neutral sequencing | Authority and accountability |

**Boundary test:** If you remove all people titles, does the work structure still make sense? **Yes** → workflow. **No** → role artifact.

Examples:

| Artifact | Layer |
|----------|-------|
| «Compliance alignment must verify store category vs implementation» | `WF_COMPLIANCE_ALIGNMENT` — workflow |
| «Maria approves privacy policy» | Roles + Approvals — not workflow |
| «Build core purchase journey» | `WF_BUILD` inside `CTR_SCOPE` boundary | 
| «Sprint 14 goal» | Team scheduling — not workflow family |
| «Rollback tested before wide release» | `WF_RELEASE` verification step | 
| «QA lead sign-off in Jira» | Roles + Tools — not workflow |

### 2.5 What transforms obligations into executable work?

**Transformation chain (conceptual):**

```text
decision_type_code
    ↓ crystallizes
contract_type_code + effective_weight_class + verification_expectation_level
    ↓ activates (when pressure_rank ≥ active)
workflow_type_code + workflow_weight_class
    ↓ produces (future Roles/Tools layer assigns execution)
alignment_outputs[] satisfying obligation at V-level
```

**Transformers (this layer only):**

1. **Contract pressure** — which obligations are dominant now
2. **Lifecycle context** — which work depth applies
3. **Class/tier modifiers** — which workflows elevate
4. **Workflow family registry** — canonical work structure per obligation domain
5. **Verification expectation (V0–V3)** — how deep alignment work must go

**NOT transformers in v1:** assignee, tool, template, approval chain, automation trigger.

---

## 3. Workflow Taxonomy

### 3.1 Derivation rationale

Test for each candidate family: *«Does NOVA treat work sequencing, prerequisite structure, and validation depth differently if this workflow type is absent when its source contracts are active?»*

**Rejected as standalone workflow families:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Sprint** | Team time-box | Roles + execution tooling |
| **Code review** | Quality gate on implementation | Roles/Templates; may evidence `WF_VALIDATION` |
| **Meeting** | Process container | May surface work; not workflow family |
| **Approval gate** | Authority act | Roles + Approvals (future) |
| **P-phase (P0–P12)** | Production Model execution machinery | Orthogonal; consumed inside `WF_BUILD` etc. |
| **Ticket/issue** | Tracking artifact | Tools — may reference workflows |
| **Template fill** | Expression format | Templates layer (future) |
| **Agent run** | Execution actor | Agents layer (future) |
| **Checklist item** | Micro-step | Inside `WF_VALIDATION`; not family |
| **Store submission event** | Release event | Informs `WF_RELEASE`; event ≠ workflow |

### 3.2 Workflow families overview

```text
Attention layer:     WF_INTAKE
Identity layer:      WF_DEFINITION · WF_CLASSIFICATION
Boundary layer:      WF_CHARTER · WF_UX_JOURNEY
Commitment layer:    WF_ARCHITECTURE · WF_DATA_ALIGNMENT · WF_COMPLIANCE_ALIGNMENT
                     WF_COMMERCIAL_ALIGNMENT · WF_TRUST_SAFETY_ALIGNMENT
Execution layer:     WF_BUILD
Verification layer:  WF_VALIDATION
Operational layer:   WF_OPERATIONS_READINESS · WF_RELEASE · WF_ECOSYSTEM_SYNC
Temporal layer:      WF_LIFECYCLE_TRANSITION · WF_EXPANSION · WF_INVESTMENT_REVIEW · WF_SUNSET
Corrective layer:    WF_RECOVERY
```

**Design choice:** 18 families — parallel density to contract registry; one primary workflow per major obligation domain, plus cross-cutting `WF_VALIDATION` and `WF_RECOVERY`. Preserves clean Contract → Workflow activation while allowing compound work within families.

### 3.3 Family definitions

#### `WF_INTAKE`

| Field | Value |
|-------|-------|
| **Purpose** | Bind product instance to NOVA reality context at entry or re-entry |
| **Source contracts** | `CTR_EXISTENCE`, latent `CTR_CLASSIFICATION` |
| **Lifecycle relevance** | `LC_CONCEPT` entry; `LC_HOLD` resume; companion mid-life entry |
| **Execution significance** | Without intake work, downstream workflows lack class/lifecycle anchor |

---

#### `WF_DEFINITION`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work to define product identity, value hypothesis, and audience |
| **Source contracts** | `CTR_PRODUCT`, `CTR_AUDIENCE` |
| **Lifecycle relevance** | Dominant `LC_CONCEPT`–`LC_DISCOVERY`; pivot at `LC_PROOF` |
| **Execution significance** | Prevents build-before-thesis; ORCA semantic/deployed split starts here |

---

#### `WF_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work to bind and validate `product_class_code`, tier, modifiers |
| **Source contracts** | `CTR_CLASSIFICATION` |
| **Lifecycle relevance** | Mandatory before `LC_PROOF`; re-trigger on tier bump |
| **Execution significance** | Wrong class → wrong workflow depth for all downstream families |

---

#### `WF_CHARTER`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work to define and maintain phase scope boundaries |
| **Source contracts** | `CTR_SCOPE`, `CTR_LIFECYCLE` (boundary aspect) |
| **Lifecycle relevance** | Critical at `LC_PROOF`, `LC_PILOT`, `LC_GROWTH` entry |
| **Execution significance** | Anti-perpetual-proof; scope inflation guard |

---

#### `WF_UX_JOURNEY`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work on interaction model and core journey architecture |
| **Source contracts** | `CTR_UX` |
| **Lifecycle relevance** | `LC_DISCOVERY` model → `LC_PROOF` journey lock |
| **Execution significance** | Core journey rework cost if deferred past Proof exit |

---

#### `WF_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work on technical structure commitments |
| **Source contracts** | `CTR_ARCHITECTURE` |
| **Lifecycle relevance** | Rises `LC_DISCOVERY`→`LC_PROOF` exit; strain at `LC_GROWTH` |
| **Execution significance** | Production incidents when architecture work skipped or mis-timed |

---

#### `WF_BUILD`

| Field | Value |
|-------|-------|
| **Purpose** | Structure implementation work converting definitions into product artifacts |
| **Source contracts** | All boundary/commitment contracts (implementation honor) |
| **Lifecycle relevance** | `LC_PROOF`–`LC_PRODUCTION`; maintenance in `LC_MATURE` |
| **Execution significance** | Primary artifact production; orthogonal to P-phases but consumes them |

---

#### `WF_VALIDATION`

| Field | Value |
|-------|-------|
| **Purpose** | Structure obligation verification work at V0–V3 depth |
| **Source contracts** | All `CTR_*` at verification expectation level |
| **Lifecycle relevance** | Every stage boundary; intensifies at Production entry |
| **Execution significance** | Cross-cutting; prevents fake completion and validation bypass |

---

#### `WF_DATA_ALIGNMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work aligning data handling with privacy obligations |
| **Source contracts** | `CTR_DATA_PRIVACY` |
| **Lifecycle relevance** | Before `LC_PILOT` if PII; terminal at `LC_SUNSET` |
| **Execution significance** | Privacy label mismatch; sunset export failure |

---

#### `WF_COMPLIANCE_ALIGNMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work aligning product with regulatory and store obligations |
| **Source contracts** | `CTR_COMPLIANCE` |
| **Lifecycle relevance** | Hypothesis `LC_DISCOVERY`; binding before `LC_PRODUCTION` |
| **Execution significance** | Store rejection; market access loss |

---

#### `WF_COMMERCIAL_ALIGNMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work aligning monetization implementation with commercial obligations |
| **Source contracts** | `CTR_COMMERCIAL` |
| **Lifecycle relevance** | `LC_DISCOVERY` model; real money at `LC_PILOT` |
| **Execution significance** | Chargebacks; payment-without-pilot-path failure |

---

#### `WF_TRUST_SAFETY_ALIGNMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work on safety boundaries, abuse handling, AI limits |
| **Source contracts** | `CTR_TRUST_SAFETY` |
| **Lifecycle relevance** | Early AI/marketplace; mandatory pilot proof |
| **Execution significance** | Harm incidents; store removal |

---

#### `WF_OPERATIONS_READINESS`

| Field | Value |
|-------|-------|
| **Purpose** | Structure survivability work — support, monitoring, handoff, incident response |
| **Source contracts** | `CTR_OPERATIONS`, `CTR_INVESTMENT` (maintain aspect) |
| **Lifecycle relevance** | Lite at `LC_PILOT`; full at `LC_PRODUCTION` entry |
| **Execution significance** | Handoff collapse (Factory); delivery-and-forget |

---

#### `WF_RELEASE`

| Field | Value |
|-------|-------|
| **Purpose** | Structure distribution, rollout, and rollback alignment work |
| **Source contracts** | `CTR_RELEASE`, `CTR_LIFECYCLE` (release≠stage aspect) |
| **Lifecycle relevance** | Internal at `LC_PROOF`; controlled at `LC_PILOT`; governed at `LC_PRODUCTION`+ |
| **Execution significance** | Public exposure without rollback; lifecycle mislabel from ship event |

---

#### `WF_ECOSYSTEM_SYNC`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work keeping external couplings aligned — parity, URLs, APIs |
| **Source contracts** | `CTR_ECOSYSTEM`, secondary `CTR_PRODUCT` (companion) |
| **Lifecycle relevance** | Companion Discovery; ongoing at Production; per-deploy for ORCA-style stacks |
| **Execution significance** | Semantic ≠ deployed; URL registry drift |

---

#### `WF_LIFECYCLE_TRANSITION`

| Field | Value |
|-------|-------|
| **Purpose** | Structure work bundle for stage advance, hold, regress, or kill |
| **Source contracts** | `CTR_LIFECYCLE`, `CTR_EXISTENCE` (kill path) |
| **Lifecycle relevance** | Every `LC_*` boundary; `LC_HOLD` overlay |
| **Execution significance** | Premature Production; perpetual Pilot; skip without evidence |

---

#### `WF_EXPANSION`

| Field | Value |
|-------|-------|
| **Purpose** | Structure growth charter execution work — feature, geo, segment expansion |
| **Source contracts** | `CTR_EXPANSION` |
| **Lifecycle relevance** | Dominant `LC_GROWTH`; entry from `LC_PRODUCTION` |
| **Execution significance** | Feature explosion; geo compliance overreach |

---

#### `WF_INVESTMENT_REVIEW`

| Field | Value |
|-------|-------|
| **Purpose** | Structure maintain/harvest/legacy posture work |
| **Source contracts** | `CTR_INVESTMENT`, `CTR_EXISTENCE` (continue/harvest) |
| **Lifecycle relevance** | `LC_MATURE`, `LC_LEGACY` |
| **Execution significance** | Zombie product; security rot masked as stability |

---

#### `WF_SUNSET`

| Field | Value |
|-------|-------|
| **Purpose** | Structure end-of-life execution work — migration, export, decommission |
| **Source contracts** | `CTR_SUNSET`, `CTR_DATA_PRIVACY` (retention) |
| **Lifecycle relevance** | `LC_LEGACY` planning → `LC_SUNSET` execution |
| **Execution significance** | Data loss; abrupt shutdown |

---

#### `WF_RECOVERY`

| Field | Value |
|-------|-------|
| **Purpose** | Structure corrective retreat work — rollback, regression, quarantine, restore |
| **Source contracts** | Triggered by violation of any `CW_CRITICAL`+ contract; explicit `CTR_LIFECYCLE` regress |
| **Lifecycle relevance** | Any stage; mandatory pattern at high-risk transitions |
| **Execution significance** | MARS survivability discipline; ORCA freeze lesson |

---

## 4. Workflow Object Model

Canonical workflow object describes **a workflow type in context**, not an execution record. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`, `contract_type_code`.

### 4.1 Core identifier

**`workflow_type_code`** — immutable registry key; one of 18 family codes in §3.

### 4.2 Required fields (reality model)

```text
workflow_reality_object {
  // Identity
  workflow_type_code              // required — e.g. WF_COMPLIANCE_ALIGNMENT
  workflow_family_layer           // required — attention | identity | boundary | commitment |
                                  //            execution | verification | operational | temporal | corrective

  // Definition
  work_subject                    // required — short noun phrase: what work is structured
  work_purpose_statement          // required — canonical purpose form (not process SOP)

  // Contract binding (conceptual — not storage)
  source_contract_type_codes[]    // required — which contracts activate this workflow
  lifecycle_state_codes[]         // required — stages where workflow is structurally active
  product_class_affinity[]        // required — classes where criticality elevates

  // Classification
  default_weight_class            // required — WW_* (see §9)
  default_activation_posture      // required — AP_* (see §4.3)

  // Work model (descriptive only)
  expected_work_streams[]         // required — obligation-aligned work categories (not tasks)
  prerequisite_workflows[]        // required — upstream workflow_type_codes that must reach WS_ALIGNED or WS_DORMANT
  expected_alignment_outputs[]    // required — output categories proving obligation honor
  typical_failure_signal          // required — one-line mis-execution indicator

  // Verification binding
  verification_expectation_levels[] // required — which V-levels this workflow must satisfy per contract

  // Boundaries
  is_role_assignment              // required — always false
  is_approval_gate                // required — always false for valid workflow types
  is_template                     // required — always false for valid workflow types
  is_p_phase                      // required — always false (P-phases orthogonal)
  confusion_cues[]                // optional — what people mistake for this workflow
}
```

### 4.3 Activation posture (descriptive, not automation)

| Posture | Meaning |
|---------|---------|
| **AP_LATENT** | Workflow exists in vocabulary; not yet structurally required |
| **AP_ACTIVE** | Contract pressure requires work structure now |
| **AP_DOMINANT** | Primary work focus for current stage/class |
| **AP_BLOCKING** | Downstream workflows cannot reach alignment until satisfied |
| **AP_DORMANT** | Not applicable at current stage/class |

### 4.4 Instance overlay (future binding, not v1 storage)

When applied to a product instance:

```text
workflow_pressure_instance {
  workflow_type_code,
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  source_contract_type_code,       // triggering contract
  effective_weight_class,          // may elevate above default
  activation_posture,              // AP_* at this moment
  workflow_state_code,             // WS_* (see §10)
  verification_target_level,       // V0–V3 for this activation
  class_amplification_notes
}
```

**Non-claims:** no `workflow_run_id`, no `assignee`, no `started_at`, no `tool_ref`, no `template_ref` — those belong to Execution Records / Roles / Tools layers (future), explicitly out of scope.

---

## 5. Workflow Registry

Immutable registry rows parallel to contract and lifecycle registries. Codes frozen at v1.

### 5.1 Registry rows

#### `WF_INTAKE`

| Field | Value |
|-------|-------|
| **code** | `WF_INTAKE` |
| **definition** | Work to bind product to NOVA context — class hypothesis, lifecycle entry, sponsor alignment |
| **source contract families** | `CTR_EXISTENCE`, `CTR_CLASSIFICATION` (hypothesis) |
| **expected outputs** | Intake binding record; lifecycle entry posture; continue/hold/kill work authorization |
| **lifecycle applicability** | `LC_CONCEPT`, `LC_HOLD` resume, companion entry |
| **common failure patterns** | Stealth product without intake; wrong lifecycle label at entry |

---

#### `WF_DEFINITION`

| Field | Value |
|-------|-------|
| **code** | `WF_DEFINITION` |
| **definition** | Work to articulate value hypothesis, product identity, and audience |
| **source contract families** | `CTR_PRODUCT`, `CTR_AUDIENCE` |
| **expected outputs** | Product thesis; audience sketch; differentiation boundaries |
| **lifecycle applicability** | `LC_CONCEPT`–`LC_DISCOVERY`; pivot at `LC_PROOF` |
| **common failure patterns** | Build before thesis; internal audience claimed as market proof |

---

#### `WF_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **code** | `WF_CLASSIFICATION` |
| **definition** | Work to bind and validate class, tier, modifiers against registry |
| **source contract families** | `CTR_CLASSIFICATION` |
| **expected outputs** | Class binding; tier estimate; Extended vs Core path selection |
| **lifecycle applicability** | Before `LC_PROOF`; tier bump re-validation |
| **common failure patterns** | T1 label on T3 product; utility creep without reclassification |

---

#### `WF_CHARTER`

| Field | Value |
|-------|-------|
| **code** | `WF_CHARTER` |
| **definition** | Work to define and maintain in/out scope for current phase |
| **source contract families** | `CTR_SCOPE`, `CTR_LIFECYCLE` |
| **expected outputs** | Proof/pilot/growth charter; kill/pivot criteria; boundary list |
| **lifecycle applicability** | `LC_PROOF`, `LC_PILOT`, `LC_GROWTH` entry |
| **common failure patterns** | Perpetual proof; MVP inflation; charter absent |

---

#### `WF_UX_JOURNEY`

| Field | Value |
|-------|-------|
| **code** | `WF_UX_JOURNEY` |
| **definition** | Work on core journey architecture and interaction model |
| **source contract families** | `CTR_UX` |
| **expected outputs** | Journey map; pattern decisions; a11y posture |
| **lifecycle applicability** | `LC_DISCOVERY`–`LC_PROOF` exit |
| **common failure patterns** | Screen polish without journey; a11y deferred |

---

#### `WF_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **code** | `WF_ARCHITECTURE` |
| **definition** | Work on committed technical structure — stack, sync, integrations |
| **source contract families** | `CTR_ARCHITECTURE` |
| **expected outputs** | Architecture record; spike conclusions; integration boundaries |
| **lifecycle applicability** | Discovery feasibility → Proof exit; Growth strain |
| **common failure patterns** | Diagram ≠ committed stack; scale surprise |

---

#### `WF_BUILD`

| Field | Value |
|-------|-------|
| **code** | `WF_BUILD` |
| **definition** | Implementation work producing product artifacts honoring upstream definitions |
| **source contract families** | All active boundary/commitment contracts |
| **expected outputs** | Product artifacts; build alignment to charter and architecture |
| **lifecycle applicability** | `LC_PROOF`–`LC_PRODUCTION`; selective in Mature/Legacy |
| **common failure patterns** | Build outside charter; implementation drift from definitions |

---

#### `WF_VALIDATION`

| Field | Value |
|-------|-------|
| **code** | `WF_VALIDATION` |
| **definition** | Cross-cutting verification work structuring obligation checks at V0–V3 |
| **source contract families** | All `CTR_*` under verification |
| **expected outputs** | Validation report per contract; alignment/misalignment declaration |
| **lifecycle applicability** | All stages; blocking at transitions |
| **common failure patterns** | Validation bypass; green QA without obligation mapping |

---

#### `WF_DATA_ALIGNMENT`

| Field | Value |
|-------|-------|
| **code** | `WF_DATA_ALIGNMENT` |
| **definition** | Work aligning collection, retention, export, deletion with privacy obligations |
| **source contract families** | `CTR_DATA_PRIVACY` |
| **expected outputs** | Data category map; retention schedule; export/delete path proof |
| **lifecycle applicability** | Pre-Pilot with PII; Sunset terminal |
| **common failure patterns** | Privacy label mismatch; shadow collection |

---

#### `WF_COMPLIANCE_ALIGNMENT`

| Field | Value |
|-------|-------|
| **code** | `WF_COMPLIANCE_ALIGNMENT` |
| **definition** | Work aligning regulatory, legal, and store posture with product |
| **source contract families** | `CTR_COMPLIANCE` |
| **expected outputs** | Compliance posture record; store category alignment; consent model proof |
| **lifecycle applicability** | Discovery hypothesis → Production binding |
| **common failure patterns** | Legal later; doc exists but product violates |

---

#### `WF_COMMERCIAL_ALIGNMENT`

| Field | Value |
|-------|-------|
| **code** | `WF_COMMERCIAL_ALIGNMENT` |
| **definition** | Work aligning monetization implementation with commercial obligations |
| **source contract families** | `CTR_COMMERCIAL` |
| **expected outputs** | Payment path proof; refund path; pricing honesty alignment |
| **lifecycle applicability** | Discovery model; Pilot real money |
| **common failure patterns** | First payment in Production; hidden fees |

---

#### `WF_TRUST_SAFETY_ALIGNMENT`

| Field | Value |
|-------|-------|
| **code** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **definition** | Work on safety boundaries, abuse paths, AI autonomy limits |
| **source contract families** | `CTR_TRUST_SAFETY` |
| **expected outputs** | Safety policy alignment; escalation path proof; monitoring hooks |
| **lifecycle applicability** | AI/marketplace Discovery; Pilot mandatory |
| **common failure patterns** | Autonomy beyond declared limits; no escalation |

---

#### `WF_OPERATIONS_READINESS`

| Field | Value |
|-------|-------|
| **code** | `WF_OPERATIONS_READINESS` |
| **definition** | Work establishing survivability — support, monitoring, handoff, incident response |
| **source contract families** | `CTR_OPERATIONS`, `CTR_INVESTMENT` |
| **expected outputs** | Ops playbook; handoff bundle; monitoring coverage; rollback ownership |
| **lifecycle applicability** | Lite Pilot; full Production entry |
| **common failure patterns** | Handoff collapse; tribal knowledge only |

---

#### `WF_RELEASE`

| Field | Value |
|-------|-------|
| **code** | `WF_RELEASE` |
| **definition** | Work structuring distribution, rollout phasing, and rollback readiness |
| **source contract families** | `CTR_RELEASE`, `CTR_LIFECYCLE` |
| **expected outputs** | Release posture record; channel truth; rollback test evidence |
| **lifecycle applicability** | Proof internal → Pilot controlled → Production governed |
| **common failure patterns** | Ship = Production confusion; rollback untested |

---

#### `WF_ECOSYSTEM_SYNC`

| Field | Value |
|-------|-------|
| **code** | `WF_ECOSYSTEM_SYNC` |
| **definition** | Work keeping external couplings aligned — parity, URLs, APIs, registries |
| **source contract families** | `CTR_ECOSYSTEM`, `CTR_PRODUCT` (companion) |
| **expected outputs** | Sync audit; registry alignment; parity evidence |
| **lifecycle applicability** | Companion Discovery; per-deploy at Production |
| **common failure patterns** | One-time sync; semantic ≠ deployed |

---

#### `WF_LIFECYCLE_TRANSITION`

| Field | Value |
|-------|-------|
| **code** | `WF_LIFECYCLE_TRANSITION` |
| **definition** | Work bundle for stage advance, hold, regress, or kill with evidence |
| **source contract families** | `CTR_LIFECYCLE`, `CTR_EXISTENCE` |
| **expected outputs** | Transition evidence bundle; stage claim honesty; regression charter if retreat |
| **lifecycle applicability** | Every boundary; `LC_HOLD` |
| **common failure patterns** | Skip without evidence; store badge = stage |

---

#### `WF_EXPANSION`

| Field | Value |
|-------|-------|
| **code** | `WF_EXPANSION` |
| **definition** | Work executing growth charter — feature, geo, segment expansion |
| **source contract families** | `CTR_EXPANSION` |
| **expected outputs** | Expansion charter execution; re-validation triggers fired |
| **lifecycle applicability** | `LC_GROWTH`; Production→Growth entry |
| **common failure patterns** | Undocumented geo launch; feature explosion |

---

#### `WF_INVESTMENT_REVIEW`

| Field | Value |
|-------|-------|
| **code** | `WF_INVESTMENT_REVIEW` |
| **definition** | Work reviewing maintain vs harvest vs legacy posture |
| **source contract families** | `CTR_INVESTMENT`, `CTR_EXISTENCE` |
| **expected outputs** | Investment posture declaration; maintenance scope; legacy honesty |
| **lifecycle applicability** | `LC_MATURE`, `LC_LEGACY` |
| **common failure patterns** | Zombie stability; security rot |

---

#### `WF_SUNSET`

| Field | Value |
|-------|-------|
| **code** | `WF_SUNSET` |
| **definition** | Work executing end-of-life — migration, export, decommission, comms |
| **source contract families** | `CTR_SUNSET`, `CTR_DATA_PRIVACY` |
| **expected outputs** | Sunset timeline; export proof; store removal plan; retention honored |
| **lifecycle applicability** | `LC_LEGACY` plan → `LC_SUNSET` execute |
| **common failure patterns** | Abrupt shutdown; data loss |

---

#### `WF_RECOVERY`

| Field | Value |
|-------|-------|
| **code** | `WF_RECOVERY` |
| **definition** | Work structuring corrective retreat — snapshot, rollback, quarantine, restore |
| **source contract families** | Violation-triggered; `CTR_LIFECYCLE` regress |
| **expected outputs** | Recovery charter; restore evidence; misalignment root cause mapped to contract |
| **lifecycle applicability** | Any; mandatory at high-risk transitions |
| **common failure patterns** | Fix-forward without recovery work; no snapshot before transition |

---

## 6. Contract → Workflow Mapping

Core mapping: every major contract family **activates** one or more workflow families when obligation pressure is active or dominant.

### 6.1 Primary mapping (1:1 contract → workflow)

| `contract_type_code` | Primary `workflow_type_code` | Work structured |
|----------------------|------------------------------|-----------------|
| `CTR_EXISTENCE` | `WF_INTAKE`, `WF_INVESTMENT_REVIEW` | Portfolio attention and posture work |
| `CTR_PRODUCT` | `WF_DEFINITION` | Identity and thesis work |
| `CTR_CLASSIFICATION` | `WF_CLASSIFICATION` | Class/tier binding work |
| `CTR_AUDIENCE` | `WF_DEFINITION` | Audience definition work stream |
| `CTR_SCOPE` | `WF_CHARTER` | Phase boundary work |
| `CTR_UX` | `WF_UX_JOURNEY` | Journey architecture work |
| `CTR_ARCHITECTURE` | `WF_ARCHITECTURE` | Technical structure work |
| `CTR_DATA_PRIVACY` | `WF_DATA_ALIGNMENT` | Privacy alignment work |
| `CTR_COMPLIANCE` | `WF_COMPLIANCE_ALIGNMENT` | Regulatory alignment work |
| `CTR_COMMERCIAL` | `WF_COMMERCIAL_ALIGNMENT` | Monetization alignment work |
| `CTR_TRUST_SAFETY` | `WF_TRUST_SAFETY_ALIGNMENT` | Safety alignment work |
| `CTR_OPERATIONS` | `WF_OPERATIONS_READINESS` | Survivability readiness work |
| `CTR_RELEASE` | `WF_RELEASE` | Distribution/rollout work |
| `CTR_LIFECYCLE` | `WF_LIFECYCLE_TRANSITION` | Stage transition work bundle |
| `CTR_EXPANSION` | `WF_EXPANSION` | Growth charter work |
| `CTR_ECOSYSTEM` | `WF_ECOSYSTEM_SYNC` | External coupling sync work |
| `CTR_INVESTMENT` | `WF_INVESTMENT_REVIEW` | Maintain/harvest work |
| `CTR_SUNSET` | `WF_SUNSET` | Decommission work |

### 6.2 Secondary activations

| Trigger contract | Also activates | Condition |
|------------------|----------------|-----------|
| Any `CTR_*` at V1+ | `WF_VALIDATION` | Verification expected |
| Any `CW_CRITICAL`+ violation | `WF_RECOVERY` | Corrective retreat required |
| `CTR_SCOPE` + build pressure | `WF_BUILD` | Implementation within boundary |
| `CTR_ARCHITECTURE` + Proof exit | `WF_BUILD` + `WF_VALIDATION` | Build must honor architecture |
| `CTR_LIFECYCLE` Production entry | `WF_OPERATIONS_READINESS`, `WF_COMPLIANCE_ALIGNMENT`, `WF_RELEASE` | Full ops/compliance/release work |
| `CTR_ECOSYSTEM` + deploy event | `WF_ECOSYSTEM_SYNC` | Per-deployment sync (ORCA) |
| `CTR_EXPANSION` + geo | `WF_COMPLIANCE_ALIGNMENT`, `WF_DATA_ALIGNMENT` | Jurisdiction expansion |
| `CTR_SUNSET` | `WF_DATA_ALIGNMENT`, `WF_COMPLIANCE_ALIGNMENT` | Terminal data obligations |

### 6.3 Contract weight → workflow weight elevation

| Contract weight | Typical workflow weight | Notes |
|-----------------|------------------------|-------|
| `CW_DESCRIPTIVE` | `WW_ROUTINE` | Light alignment work |
| `CW_OPERATIONAL` | `WW_ROUTINE` or `WW_COORDINATED` | Single-domain work streams |
| `CW_STRUCTURAL` | `WW_COORDINATED` or `WW_STRUCTURAL` | Multi-artifact sequencing |
| `CW_CRITICAL` | `WW_STRUCTURAL` or `WW_CRITICAL` | Blocking alignment work |
| `CW_BINDING` | `WW_CRITICAL` or `WW_TERMINAL` | Irreversible path work |

### 6.4 Mapping diagram

```text
CTR_EXISTENCE ──────────► WF_INTAKE · WF_INVESTMENT_REVIEW
CTR_PRODUCT ────────────► WF_DEFINITION
CTR_CLASSIFICATION ─────► WF_CLASSIFICATION
CTR_AUDIENCE ───────────► WF_DEFINITION (audience stream)
CTR_SCOPE ──────────────► WF_CHARTER ──────────► WF_BUILD
CTR_UX ─────────────────► WF_UX_JOURNEY ───────► WF_BUILD
CTR_ARCHITECTURE ───────► WF_ARCHITECTURE ─────► WF_BUILD · WF_VALIDATION
CTR_DATA_PRIVACY ───────► WF_DATA_ALIGNMENT ───► WF_VALIDATION
CTR_COMPLIANCE ─────────► WF_COMPLIANCE_ALIGNMENT ► WF_VALIDATION
CTR_COMMERCIAL ─────────► WF_COMMERCIAL_ALIGNMENT ► WF_VALIDATION
CTR_TRUST_SAFETY ───────► WF_TRUST_SAFETY_ALIGNMENT ► WF_VALIDATION
CTR_OPERATIONS ─────────► WF_OPERATIONS_READINESS ► WF_VALIDATION
CTR_RELEASE ────────────► WF_RELEASE ──────────► WF_ECOSYSTEM_SYNC (if coupled)
CTR_LIFECYCLE ──────────► WF_LIFECYCLE_TRANSITION ► WF_RECOVERY (if regress)
CTR_EXPANSION ──────────► WF_EXPANSION ────────► WF_COMPLIANCE_ALIGNMENT (geo)
CTR_ECOSYSTEM ──────────► WF_ECOSYSTEM_SYNC
CTR_INVESTMENT ─────────► WF_INVESTMENT_REVIEW
CTR_SUNSET ─────────────► WF_SUNSET ───────────► WF_DATA_ALIGNMENT

All CTR_* at verification ─► WF_VALIDATION (cross-cutting)
Any CW_CRITICAL+ breach ───► WF_RECOVERY (corrective)
```

### 6.5 Example chain (user charter)

```text
DEC_COMPLIANCE
    ↓ crystallizes
CTR_COMPLIANCE (verification V2 at Pilot, V3 at Production)
    ↓ activates
WF_COMPLIANCE_ALIGNMENT + WF_VALIDATION
    ↓ produces (role-neutral)
compliance posture alignment + validation evidence
```

No roles. No agents. No approvals. Only execution flow reality.

---

## 7. Lifecycle Workflow Pressure Matrix

Dominant workflow families per lifecycle stage. **Dominant** = structurally highest work pressure if absent; **Active** = required secondary; **Latent** = usually dormant; **Dormant** = atypical.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `WF_INTAKE`, `WF_DEFINITION` | `WF_CLASSIFICATION` (hypothesis) | `WF_VALIDATION` (V0) | `WF_BUILD`, `WF_OPERATIONS_READINESS`, `WF_COMPLIANCE_ALIGNMENT` |
| **`LC_DISCOVERY`** | `WF_DEFINITION`, `WF_CLASSIFICATION`, `WF_CHARTER` (hypothesis) | `WF_UX_JOURNEY`, `WF_DATA_ALIGNMENT`, `WF_COMPLIANCE_ALIGNMENT` (hypothesis), `WF_COMMERCIAL_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT`, `WF_ECOSYSTEM_SYNC` | `WF_ARCHITECTURE` | `WF_OPERATIONS_READINESS`, `WF_RELEASE` |
| **`LC_PROOF`** | `WF_CHARTER`, `WF_LIFECYCLE_TRANSITION`, `WF_UX_JOURNEY`, `WF_BUILD` | `WF_ARCHITECTURE`, `WF_VALIDATION`, `WF_DEFINITION` (pivot) | `WF_DATA_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT` | `WF_OPERATIONS_READINESS` (full), `WF_EXPANSION` |
| **`LC_PILOT`** | `WF_LIFECYCLE_TRANSITION`, `WF_OPERATIONS_READINESS` (lite), `WF_RELEASE`, `WF_VALIDATION` | `WF_COMMERCIAL_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT`, `WF_COMPLIANCE_ALIGNMENT`, `WF_DATA_ALIGNMENT` | `WF_ARCHITECTURE` | `WF_EXPANSION`, `WF_INVESTMENT_REVIEW` |
| **`LC_PRODUCTION`** | `WF_LIFECYCLE_TRANSITION`, `WF_OPERATIONS_READINESS`, `WF_COMPLIANCE_ALIGNMENT`, `WF_RELEASE`, `WF_VALIDATION` | `WF_ARCHITECTURE`, `WF_DATA_ALIGNMENT`, `WF_COMMERCIAL_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT`, `WF_BUILD` | `WF_EXPANSION` (entry) | `WF_SUNSET` |
| **`LC_GROWTH`** | `WF_EXPANSION`, `WF_LIFECYCLE_TRANSITION`, `WF_ARCHITECTURE`, `WF_VALIDATION` | `WF_COMPLIANCE_ALIGNMENT`, `WF_COMMERCIAL_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT`, `WF_CHARTER` | `WF_UX_JOURNEY` (new surfaces) | `WF_INTAKE` |
| **`LC_MATURE`** | `WF_INVESTMENT_REVIEW`, `WF_LIFECYCLE_TRANSITION` | `WF_OPERATIONS_READINESS`, `WF_COMPLIANCE_ALIGNMENT`, `WF_BUILD` (maintenance) | `WF_EXPANSION` (refresh) | `WF_DEFINITION` |
| **`LC_LEGACY`** | `WF_INVESTMENT_REVIEW`, `WF_SUNSET` (planning), `WF_LIFECYCLE_TRANSITION` | `WF_OPERATIONS_READINESS` (minimal), `WF_COMPLIANCE_ALIGNMENT`, `WF_DATA_ALIGNMENT` | `WF_ECOSYSTEM_SYNC` (successor) | `WF_EXPANSION` |
| **`LC_SUNSET`** | `WF_SUNSET`, `WF_DATA_ALIGNMENT`, `WF_LIFECYCLE_TRANSITION` | `WF_COMPLIANCE_ALIGNMENT`, `WF_OPERATIONS_READINESS` (wind-down), `WF_RELEASE` (final) | `WF_ECOSYSTEM_SYNC` | `WF_COMMERCIAL_ALIGNMENT`, `WF_EXPANSION` |
| **`LC_HOLD`** | `WF_INTAKE`, `WF_LIFECYCLE_TRANSITION` | All prior-stage workflows — **staleness review** via `WF_VALIDATION` | — | New `WF_EXPANSION` |

### 7.1 Stage-critical workflow questions

| Stage | If only three workflows could run |
|-------|-----------------------------------|
| `LC_CONCEPT` | `WF_INTAKE` · `WF_DEFINITION` · `WF_CLASSIFICATION` (hypothesis) |
| `LC_DISCOVERY` | `WF_CLASSIFICATION` · `WF_DEFINITION` · `WF_CHARTER` (hypothesis) |
| `LC_PROOF` | `WF_CHARTER` · `WF_BUILD` · `WF_LIFECYCLE_TRANSITION` |
| `LC_PILOT` | `WF_OPERATIONS_READINESS` · `WF_RELEASE` · `WF_VALIDATION` |
| `LC_PRODUCTION` | `WF_OPERATIONS_READINESS` · `WF_COMPLIANCE_ALIGNMENT` · `WF_RELEASE` |
| `LC_GROWTH` | `WF_EXPANSION` · `WF_ARCHITECTURE` · `WF_COMPLIANCE_ALIGNMENT` |
| `LC_MATURE` | `WF_INVESTMENT_REVIEW` · `WF_OPERATIONS_READINESS` · `WF_VALIDATION` |
| `LC_LEGACY` | `WF_INVESTMENT_REVIEW` · `WF_SUNSET` (plan) · `WF_OPERATIONS_READINESS` (minimal) |
| `LC_SUNSET` | `WF_SUNSET` · `WF_DATA_ALIGNMENT` · `WF_COMPLIANCE_ALIGNMENT` |

---

## 8. Product Class Workflow Pressure Matrix

Criticality scale: **●** Critical · **◐** Elevated · **○** Standard · **—** Rarely material

Rows = workflow families · Columns = 8 focus classes from charter

| Workflow family | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-----------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `WF_INTAKE` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `WF_DEFINITION` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `WF_CLASSIFICATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `WF_CHARTER` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `WF_UX_JOURNEY` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `WF_ARCHITECTURE` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `WF_BUILD` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `WF_VALIDATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `WF_DATA_ALIGNMENT` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `WF_COMPLIANCE_ALIGNMENT` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `WF_COMMERCIAL_ALIGNMENT` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `WF_TRUST_SAFETY_ALIGNMENT` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `WF_OPERATIONS_READINESS` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `WF_RELEASE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `WF_ECOSYSTEM_SYNC` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `WF_LIFECYCLE_TRANSITION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `WF_EXPANSION` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `WF_INVESTMENT_REVIEW` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `WF_SUNSET` | ◐ | ◐ | ○ | ○ | ● | ● | ● | ● |
| `WF_RECOVERY` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |

### 8.1 Class-specific workflow amplifications

| Class | Workflows disproportionately critical |
|-------|--------------------------------------|
| **`COMMERCE`** | `WF_COMMERCIAL_ALIGNMENT`, `WF_OPERATIONS_READINESS`, `WF_UX_JOURNEY`, `WF_VALIDATION` |
| **`FIELD_OPERATIONS`** | `WF_ARCHITECTURE`, `WF_CHARTER`, `WF_DATA_ALIGNMENT`, `WF_RECOVERY` (data loss) |
| **`AI_ASSISTANT`** | `WF_TRUST_SAFETY_ALIGNMENT`, `WF_DATA_ALIGNMENT`, `WF_COMPLIANCE_ALIGNMENT`, `WF_OPERATIONS_READINESS` |
| **`UTILITY_TOOL`** | `WF_CHARTER` (anti-creep), `WF_CLASSIFICATION`; most at ○ unless triggers |
| **`MARKETPLACE`** | `WF_TRUST_SAFETY_ALIGNMENT`, `WF_COMMERCIAL_ALIGNMENT`, `WF_ECOSYSTEM_SYNC`, `WF_VALIDATION` |
| **`HEALTH_MEDICAL`** | `WF_COMPLIANCE_ALIGNMENT`, `WF_DATA_ALIGNMENT`, `WF_TRUST_SAFETY_ALIGNMENT`, `WF_VALIDATION` |
| **`FINTECH_WALLET`** | `WF_COMPLIANCE_ALIGNMENT`, `WF_COMMERCIAL_ALIGNMENT`, `WF_ARCHITECTURE`, `WF_VALIDATION` |
| **`AI_AGENT_CONSOLE`** | `WF_TRUST_SAFETY_ALIGNMENT`, `WF_COMPLIANCE_ALIGNMENT`, `WF_ARCHITECTURE`, `WF_RECOVERY` |

**Tier modifier (all classes):** T3+ elevates `WF_ARCHITECTURE`, `WF_OPERATIONS_READINESS`, `WF_VALIDATION` to blocking at Production; T4 elevates nearly all alignment workflows to ●.

---

## 9. Workflow Weight Model

Derived from **work scope × sequencing depth × verification burden × blocking power** — not from team size or calendar duration.

### 9.1 Weight classes

#### `WW_ROUTINE`

| Field | Value |
|-------|-------|
| **Scope** | Single work stream; one obligation domain |
| **Execution depth** | Shallow sequencing; few prerequisites |
| **Validation expectations** | V0–V1 alignment sufficient |
| **Examples** | `WF_INTAKE` at Concept; hypothesis `WF_DEFINITION` |

---

#### `WW_COORDINATED`

| Field | Value |
|-------|-------|
| **Scope** | Multiple work streams within one workflow family |
| **Execution depth** | Ordered prerequisites; cross-artifact consistency |
| **Validation expectations** | V1–V2 |
| **Examples** | `WF_CHARTER` in Proof; lite `WF_OPERATIONS_READINESS` in Pilot |

---

#### `WW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Scope** | Multi-domain; affects product shape or release posture |
| **Execution depth** | Deep sequencing; upstream workflows must align first |
| **Validation expectations** | V2; measured alignment |
| **Examples** | `WF_ARCHITECTURE` at Proof exit; `WF_RELEASE` public rollout; `WF_EXPANSION` |

---

#### `WW_CRITICAL`

| Field | Value |
|-------|-------|
| **Scope** | Product-wide blocking; ops/legal/users depend |
| **Execution depth** | Full work bundle; downstream workflows blocked until aligned |
| **Validation expectations** | V2–V3 |
| **Examples** | `WF_COMPLIANCE_ALIGNMENT` Production; `WF_OPERATIONS_READINESS` Production; `WF_TRUST_SAFETY_ALIGNMENT` live AI |

---

#### `WW_TERMINAL`

| Field | Value |
|-------|-------|
| **Scope** | Irreversible or impractical to undo |
| **Execution depth** | Complete work path; recovery work paired |
| **Validation expectations** | V3 mandatory |
| **Examples** | `WF_SUNSET` decommission execution; mass deletion path |

### 9.2 Default weight by workflow family

| Family | Default weight | Elevates to `WW_CRITICAL` when |
|--------|----------------|--------------------------------|
| `WF_INTAKE` | `WW_ROUTINE` | Production product re-intake after kill |
| `WF_DEFINITION` | `WW_COORDINATED` | Post-Production identity change |
| `WF_CLASSIFICATION` | `WW_STRUCTURAL` | Extended class or T3+ |
| `WF_CHARTER` | `WW_STRUCTURAL` | Proof/Pilot boundary |
| `WF_UX_JOURNEY` | `WW_STRUCTURAL` | Core journey lock at Proof exit |
| `WF_ARCHITECTURE` | `WW_STRUCTURAL` | Production baseline; `WW_CRITICAL` at scale |
| `WF_BUILD` | `WW_COORDINATED` | T3+ Production build |
| `WF_VALIDATION` | `WW_COORDINATED` | `CW_CRITICAL`+ contracts under test |
| `WF_DATA_ALIGNMENT` | `WW_STRUCTURAL` | PII; `WW_CRITICAL` regulated |
| `WF_COMPLIANCE_ALIGNMENT` | `WW_CRITICAL` | Extended classes always |
| `WF_COMMERCIAL_ALIGNMENT` | `WW_CRITICAL` | Real money |
| `WF_TRUST_SAFETY_ALIGNMENT` | `WW_CRITICAL` | AI/marketplace live |
| `WF_OPERATIONS_READINESS` | `WW_CRITICAL` | Production entry |
| `WF_RELEASE` | `WW_STRUCTURAL` | Public wide release |
| `WF_ECOSYSTEM_SYNC` | `WW_STRUCTURAL` | Deep platform embed; per-deploy ORCA |
| `WF_LIFECYCLE_TRANSITION` | `WW_STRUCTURAL` | Production transition claim |
| `WF_EXPANSION` | `WW_CRITICAL` | Geo/compliance expansion |
| `WF_INVESTMENT_REVIEW` | `WW_COORDINATED` | Legacy declaration |
| `WF_SUNSET` | `WW_TERMINAL` | Decommission execution |
| `WF_RECOVERY` | `WW_CRITICAL` | Production rollback; regulated product |

---

## 10. Workflow State Model

Workflow states describe **alignment posture of structured work**, not task status, sprint state, or approval outcome. Role-neutral.

### 10.1 State codes

| State | Code | Meaning |
|-------|------|---------|
| **Latent** | `WS_LATENT` | Contract exists; workflow not yet structurally required |
| **Activated** | `WS_ACTIVATED` | Obligation pressure triggered workflow; work structure defined |
| **In progress** | `WS_IN_PROGRESS` | Alignment work underway (no assignee implied) |
| **Blocked** | `WS_BLOCKED` | Prerequisite workflow or obligation gap prevents progress |
| **Verifying** | `WS_VERIFYING` | `WF_VALIDATION` active at target V-level |
| **Aligned** | `WS_ALIGNED` | Obligation honored at required verification level for current context |
| **Misaligned** | `WS_MISALIGNED` | Verification failed or obligation gap confirmed |
| **Superseded** | `WS_SUPERSEDED` | Lifecycle/decision/contract change replaced this workflow pressure |
| **Dormant** | `WS_DORMANT` | Not applicable at current stage/class |

### 10.2 State transition rules (descriptive)

```text
WS_LATENT ──(contract pressure ≥ active)──► WS_ACTIVATED
WS_ACTIVATED ──(work begins)──► WS_IN_PROGRESS
WS_IN_PROGRESS ──(prerequisite fail)──► WS_BLOCKED
WS_BLOCKED ──(prerequisite satisfied)──► WS_IN_PROGRESS
WS_IN_PROGRESS ──(validation starts)──► WS_VERIFYING
WS_VERIFYING ──(V-level pass)──► WS_ALIGNED
WS_VERIFYING ──(V-level fail)──► WS_MISALIGNED
WS_MISALIGNED ──(WF_RECOVERY or rework)──► WS_IN_PROGRESS
WS_* ──(lifecycle/decision change)──► WS_SUPERSEDED
WS_* ──(stage/class makes irrelevant)──► WS_DORMANT
```

### 10.3 Deliberate exclusions

| Rejected state | Reason | Correct layer |
|----------------|--------|---------------|
| **approved** | Authority act | Roles + Approvals |
| **completed** (generic) | Implies fake closure | Use `WS_ALIGNED` with V-level |
| **assigned** | Person binding | Roles |
| **automated** | Execution mode | Automation |
| **sprint_active** | Team scheduling | Execution tooling |

### 10.4 Alignment vs fake completion

**`WS_ALIGNED` requires:**

1. Named `source_contract_type_code`
2. Stated `verification_target_level` (V0–V3)
3. Lifecycle context where alignment is claimed
4. No unresolved `WS_MISALIGNED` on prerequisite workflows at `WW_STRUCTURAL`+

**Not sufficient for `WS_ALIGNED`:** checklist tick; ship event; doc exists; meeting held.

---

## 11. Workflow Failure Patterns

Derived from Contract Failure Patterns §10, Website Factory drift, ORCA battle, MARS survivability — reframed as **work structure failures**, not people failures.

| Pattern | Signal | Root workflow failure | Affected workflows |
|---------|--------|----------------------|-------------------|
| **Obligation without work** | Contract crystallized; no workflow activated | Contract → workflow activation missing | Any — work vacuum |
| **Work without obligation** | Sprint/tasks run; no `CTR_*` mapped | Execution without source reality | `WF_BUILD`, ad-hoc work |
| **Workflow drift** | Work continues after lifecycle/decision supersession | `WS_SUPERSEDED` not applied | Any stale workflow |
| **Validation bypass** | Ship/merge without `WF_VALIDATION` at required V-level | Verification structure skipped | `WF_VALIDATION`, all alignment |
| **Contract ignored in work** | Alignment work runs but wrong obligation domain | Work stream mis-mapped to contract | Alignment families |
| **Orphan workflow** | `WF_*` active with no source contract | Fake work structure | Any |
| **Workflow duplication** | Two parallel work streams for same contract | Same family, conflicting alignment | Same `workflow_type_code` |
| **Execution without lifecycle context** | Production-depth work at Concept stage | Lifecycle pressure ignored | `WF_OPERATIONS_READINESS`, `WF_COMPLIANCE_ALIGNMENT` |
| **Workflow inflation** | Full alignment pack on utility T1 | Wrong-depth work applied | Compliance/commercial alignment |
| **Fake completion** | `WS_ALIGNED` claimed at V0 for `CW_CRITICAL` contract | Weight/state violation | `WF_VALIDATION` |
| **Handoff work absent** | Delivery complete; `WF_OPERATIONS_READINESS` never lite in Pilot | Factory handoff-collapse analog | `WF_OPERATIONS_READINESS` |
| **Sync work once-only** | URL/registry drift after deploy | `WF_ECOSYSTEM_SYNC` not per-deploy | `WF_ECOSYSTEM_SYNC` — ORCA |
| **Release = transition confusion** | Store live; `WF_LIFECYCLE_TRANSITION` skipped | Release event substituted for transition work | `WF_RELEASE`, `WF_LIFECYCLE_TRANSITION` |
| **Build before charter** | `WF_BUILD` before `WF_CHARTER` aligned | Prerequisite violation | `WF_BUILD`, `WF_CHARTER` |
| **Recovery absent** | Production incident; no `WF_RECOVERY` structure | Corrective work ad hoc | `WF_RECOVERY` |
| **Pilot ops work gap** | Real users; lite ops readiness never activated | `WF_OPERATIONS_READINESS` latent in Pilot | `WF_OPERATIONS_READINESS` |
| **Commercial work jump** | First payment in Production without Pilot alignment work | `WF_COMMERCIAL_ALIGNMENT` sequencing error | `WF_COMMERCIAL_ALIGNMENT` |
| **Semantic/deployed work split** | PPC/ads against intent not deployed product | `WF_DEFINITION` vs `WF_ECOSYSTEM_SYNC` desync | `WF_DEFINITION`, `WF_ECOSYSTEM_SYNC`, `WF_RELEASE` |

---

## 12. Workflow Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-W1** | Every dominant contract of current `lifecycle_state_code` must activate corresponding workflow or mark SAFE UNKNOWN | Obligation without work |
| **AC-W2** | No `WF_BUILD` at `WW_STRUCTURAL`+ before `WF_CHARTER` reaches `WS_ALIGNED` or explicit charter waiver | Build before boundary |
| **AC-W3** | Extended class: `WF_COMPLIANCE_ALIGNMENT` and `WF_TRUST_SAFETY_ALIGNMENT` cannot stay `WS_LATENT` past `LC_DISCOVERY` | Compliance work vacuum |
| **AC-W4** | `WF_LIFECYCLE_TRANSITION` Production claim requires evidence bundle — not inferred from `WF_RELEASE` alone | Release = stage confusion |
| **AC-W5** | Same `workflow_type_code` at `WW_STRUCTURAL`+ requires lifecycle or tier trigger to re-activate from `WS_SUPERSEDED` | Workflow churn |
| **AC-W6** | Tasks/tickets cannot substitute for workflow — name `workflow_type_code` and `source_contract_type_code` | Hidden work structure |
| **AC-W7** | `WF_CHARTER` must reach `WS_ALIGNED` before `LC_PROOF` build obligation | Charter inflation |
| **AC-W8** | `WW_CRITICAL`+ workflows must declare target V-level before `WS_ALIGNED` claim | Fake completion |
| **AC-W9** | Pilot with real users requires `WF_OPERATIONS_READINESS` at lite minimum `WS_ACTIVATED` | Pilot ops work gap |
| **AC-W10** | `WF_DEFINITION` pivot requires paired `WF_LIFECYCLE_TRANSITION` consideration | Random pivot work |
| **AC-W11** | One workflow family per obligation activation event — no mega-workflows bundling unrelated contracts | Workflow inflation |
| **AC-W12** | `WF_CLASSIFICATION` re-run on tier bump or payments/PII/regulated feature | Classification work drift |
| **AC-W13** | Undocumented `WW_CRITICAL`+ workflow at `WS_IN_PROGRESS` = SAFE UNKNOWN in REPORT | Silent critical work |
| **AC-W14** | `UTILITY_TOOL` T1 exempt from commercial/compliance alignment workflows until trigger feature | Over-engineering work |
| **AC-W15** | Store/public release activates `WF_RELEASE` + often `WF_LIFECYCLE_TRANSITION` — never implicit | AC-L10 lifecycle analog |
| **AC-W16** | Document/template alone cannot satisfy workflow — implementation alignment required | Doc ≠ work confusion |
| **AC-W17** | Every active `workflow_type_code` must trace to `source_contract_type_code` | Contractless work |
| **AC-W18** | Duplicate alignment work for same contract family requires reconciliation to single pressure instance | Workflow duplication |
| **AC-W19** | High-risk lifecycle transitions require `WF_RECOVERY` prerequisite pattern (snapshot/rollback charter) | Recovery absent |
| **AC-W20** | `WF_ECOSYSTEM_SYNC` must re-activate on each external deploy when `CTR_ECOSYSTEM` dominant | One-time sync (ORCA) |

---

## 13. Workflow Relationships

### 13.1 Dependency chain

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
│  Workflow Reality Model v1  ──► workflow_type_code     ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ work structure ready for role/tool assignment
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    ROLES (future)                            │
│  Obligation ownership · authority · assignee                 │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
                         Tools · Agents · Automation
```

### 13.2 Why workflow requires all previous layers

| Input | Provides | Without it |
|-------|----------|------------|
| **`product_class_code`** | Which workflows are material; default weights | Payment alignment work on offline utility |
| **`lifecycle_state_code`** | Which workflows dominate now; work depth | Full compliance work at Concept |
| **`decision_type_code`** | Which choices created obligations | Work on unchosen domains |
| **`contract_type_code`** | Which obligations activate work | Random process steps |
| **`workflow_type_code`** | The actual work structure domain | Roles assign meaningless tasks |

**Combined pressure function (conceptual, not algorithm):**

```text
workflow_pressure(workflow_type_code, product_class_code, lifecycle_state_code, source_contract_type_code, tier)
  → activation_posture ∈ { dormant, latent, active, dominant, blocking }
  → effective_weight_class
  → verification_target_level
  → workflow_state_code
```

**Examples:**

| Context | Pressure outcome |
|---------|------------------|
| `WF_COMMERCIAL_ALIGNMENT` + `UTILITY_TOOL` + `LC_PROOF` + T1 | `WS_DORMANT` unless monetization trigger |
| `WF_COMMERCIAL_ALIGNMENT` + `COMMERCE` + `LC_PILOT` + T3 | `AP_DOMINANT`; V2 real transactions |
| `WF_ARCHITECTURE` + `AI_AGENT_CONSOLE` + `LC_DISCOVERY` + T4 | `AP_ACTIVE`; spike-level only |
| `WF_SUNSET` + `HEALTH_MEDICAL` + `LC_SUNSET` + T4 | `AP_BLOCKING`; `WW_TERMINAL`; V3 |

### 13.3 Cross-layer binding (conceptual instance)

```text
nova_workflow_context {
  product_class_code,           // registry
  complexity_tier,              // registry / intake
  lifecycle_state_code,         // lifecycle
  decision_type_code,           // source decision (trace)
  contract_type_code,           // activating obligation
  workflow_type_code,           // structured work domain
  effective_weight_class,       // WW_*
  verification_target_level,    // V0–V3
  workflow_state_code           // WS_*
}
```

### 13.4 Cross-workflow dependencies (reality, not roles)

| Upstream workflow | Downstream workflows constrained |
|-------------------|----------------------------------|
| `WF_INTAKE` | All — context anchor |
| `WF_CLASSIFICATION` | All alignment workflows — depth selection |
| `WF_CHARTER` | `WF_BUILD`, `WF_VALIDATION` scope |
| `WF_ARCHITECTURE` | `WF_BUILD`, `WF_EXPANSION` |
| `WF_DEFINITION` | `WF_UX_JOURNEY`, `WF_CHARTER`, `WF_ECOSYSTEM_SYNC` |
| `WF_*_ALIGNMENT` | `WF_VALIDATION` at contract V-level |
| `WF_LIFECYCLE_TRANSITION` | Re-evaluates all dominant workflows at new stage |
| `WF_RECOVERY` | May reset misaligned workflows to `WS_IN_PROGRESS` |

### 13.5 Production Model orthogonality

| Dimension | Workflow Reality | Production Model P0–P12 |
|-----------|------------------|-------------------------|
| **Question** | What work structure honors obligations? | How does NOVA execute production steps? |
| **Binding** | `{ class × lifecycle × contract }` | Build pipeline phases |
| **Example** | `WF_BUILD` inside Proof charter | `P9` implementation phase |
| **Rule** | P-phase completion ≠ workflow alignment | AC-W8; separate evidence |

One product in `LC_PROOF` may run `WF_BUILD` while in `P10` validation — lifecycle and P-phase are **orthogonal coordinates**.

---

## 14. Workflow Reality Boundaries

### 14.1 What is NOT workflow (in this layer)

| Not workflow | Why | Correct layer |
|--------------|-----|---------------|
| **Role** | Person/accountability assignment | Roles (future) |
| **Agent** | Autonomous execution actor | Agents (future) |
| **Tool** | Helper that assists work | Tools (future) |
| **Template** | Reusable document pattern | Templates (future) |
| **Approval** | Authority sign-off | Roles + Approvals (future) |
| **Meeting** | Process container | May surface work; not workflow family |
| **Sprint** | Team time-box | Execution scheduling |
| **Ticket/task** | Work unit instance | Tools — may implement workflow steps |
| **P-phase** | Production Model milestone | Orthogonal execution machinery |
| **Gate pass/fail** | Enforcement outcome | Future gate layer; validates workflow alignment |
| **Automation rule** | Unattended trigger | Automation (future) |
| **Runtime/orchestrator** | Execution engine | Not claimed in MARS/NOVA v1 |
| **Checklist item** | Micro-step | Inside `WF_VALIDATION`; not family |
| **Contract** | Obligation existence | Contract Reality — upstream |
| **Decision** | Choice domain | Decision Reality — upstream |

### 14.2 Boundary tests

Apply before labeling something a workflow family:

1. **Contract-origin test:** Does this work structure trace to named `contract_type_code`(s)?
2. **Lifecycle test:** Does work depth change by `lifecycle_state_code`?
3. **Role-neutrality test:** Is structure meaningful with zero named people?
4. **Obligation test:** Does absence leave obligations executable only via ad-hoc tasks?

**Pass all four** → workflow family applies. **Fail any** → likely task, role, tool, or template artifact.

### 14.3 Common misuse prevention

| Misuse | Correction |
|--------|------------|
| «Jira workflow = NOVA workflow» | Jira is tool; name `workflow_type_code` |
| «Sprint = Discovery Workflow» | Sprint schedules; `WF_DEFINITION` structures obligation work |
| «Legal review = compliance workflow» | Review may be role step inside `WF_COMPLIANCE_ALIGNMENT` |
| «CI green = validated» | CI may evidence `WF_VALIDATION`; not substitute |
| «Agent run = workflow» | Agent executes; workflow defines structure |
| «P10 complete = Production ready» | P-phase ≠ lifecycle; check `WF_LIFECYCLE_TRANSITION` |

### 14.4 Layer leakage prevention

| Leakage direction | Block |
|-------------------|-------|
| Workflow → Roles | No assignee fields in v1 object model |
| Workflow → Templates | No template_ref in v1 |
| Workflow → Approvals | No approval state codes |
| Workflow → Automation | No trigger/automation vocabulary |
| Workflow → Contracts | Workflows activate from contracts; do not redefine obligations |
| Workflow → Decisions | Decisions upstream; workflows do not invent choices |

---

## 15. RBM Mapping

```text
Reality
├── Production Model v1        … what NOVA is
├── Product Taxonomy v1        … what classes exist
├── Product Class Registry v1  … what each class means operationally
├── Lifecycle Model v1         … where the product is in life
├── Decision Reality Model v1  … what decisions exist in product nature
├── Contract Reality Model v1  … what obligations exist because of decisions
└── Workflow Reality Model v1  … how obligations become structured work  ◄── first execution-oriented band vocabulary
        │
        ▼
Roles                          … who owns obligation domains (future)
        │
        ▼
Tools                          … helpers (future)
        │
        ▼
Agents                         … only if proven necessary (future)
        │
        ▼
Automation                     … last, if ever (future)
```

### 15.1 Why Workflow is the first execution-oriented layer

| Order | Reason |
|-------|--------|
| **Reality before Lifecycle** | Must know product identity before work depth |
| **Lifecycle before Decisions** | Stage determines active choice domains |
| **Decisions before Contracts** | Obligations crystallize from choices |
| **Contracts before Workflow** | Work structures honor known obligations — not invent them |
| **Workflow before Roles** | Assign people to work domains that already exist |
| **Workflow before Tools** | Tools assist structured work — not define it |
| **Workflow before Agents** | Agents execute within structure — not replace it |
| **Workflow before Automation** | Automate proven work patterns — not guess obligations |

**Completion of Workflow Reality band (vocabulary only):** After this artifact, NOVA knows **identity**, **time**, **choice structure**, **commitment structure**, and **work structure**. Downstream layers can assign `{ product_class × lifecycle × contract × workflow }` instead of improvising process.

**Explicitly NOT in Workflow band:** role registry, agent cards, tool catalog, templates, approval chains, task storage, gate automation, runtime orchestration.

### 15.2 Why Roles must come later

Roles answer **«кто несёт ответственность за domain obligation/work?»** — meaningless without:

- `contract_type_code` — what obligation exists
- `workflow_type_code` — what work structure honors it
- `verification_target_level` — how deep alignment must go

Assigning «QA lead» before `WF_VALIDATION` and `CTR_*` mapping exists produces **political coverage**, not operational structure.

**Roles will consume from Workflow Reality:**

- obligation ownership per `contract_type_code`
- work stream ownership per `workflow_type_code`
- escalation paths when `WS_MISALIGNED` or `WS_BLOCKED`

**Not designed here.**

### 15.3 Downstream layers (future — not designed here)

| Layer | Will consume from Workflow Reality |
|-------|-------------------------------------|
| **Roles** | Work domain ownership; authority at V2/V3 |
| **Tools** | Helpers per workflow family (validators, diff advisors) |
| **Agents** | Scoped execution within workflow structure — if proven |
| **Automation** | Repeatable alignment checks after human proof |

---

## 16. Risks

| Risk | Severity | Mitigation in v1 |
|------|----------|------------------|
| Workflow Reality confused with BPM/engine | High | Scope boundary; no runtime claims |
| Workflow Reality confused with Roles | High | §2.4; §14; role-neutrality tests |
| Workflow inflation (too many types) | Medium | 18 families with rejection table §3.1; AC-W11 |
| Workflow confused with P-phases | High | Orthogonality §13.5; `is_p_phase` always false |
| Weight class used to skip validation | Medium | Derived criteria §9; AC-W8 |
| Lifecycle-workflow conflation | High | Separate codes; AC-W4; matrix §7 |
| Class matrix oversimplification | Medium | Tier modifier §8.1; SAFE UNKNOWN |
| Silent critical work | High | AC-W13; failure patterns §11 |
| Contract-workflow 1:1 oversimplification | Medium | Secondary activations §6.2; `WF_VALIDATION` cross-cutting |
| Governance expansion drift | Medium | No Roles/Tools/Agents in v1; RBM §15 |
| Prior foundation files not all in-repo | Medium | Cross-reference existing docs |
| Human enforcement fatigue | Medium | 20 anti-chaos rules; not automation pretense |
| Fake `WS_ALIGNED` at scale | High | V-level binding §10.4; AC-W8 |

---

## 17. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Exact mapping workflow weight → gate depth | First NOVA Roles v1 charter |
| Whether `WF_ECOSYSTEM_SYNC` splits intent vs deployed in v2 | First ORCA-style dual-domain product through NOVA |
| Machine format for `workflow_pressure_instance` | Future intake schema |
| Optimal count of workflow families (18 vs consolidated) | Operator feedback after 2–3 products |
| Prior Production Model / Taxonomy / Registry markdown in-repo | Human commit of foundation pack |
| Workflow Records vs Execution Tasks layer split | Future charter after Roles design |
| Whether `WS_MISALIGNED` triggers mandatory `WF_RECOVERY` | First Production incident through NOVA workflow |
| P-phase ↔ workflow binding matrix detail | Production Model commit + pilot |
| Overlap with MARS survivability safe-execution layer | NOVA ↔ MARS integration charter |
| AI agent workflow domains beyond trust/safety/build | First `AI_AGENT_CONSOLE` production pilot |

**Non-claims preserved:** this model does not assert workflow engine, task storage, role assignment, template library, approval automation, agent orchestration, or runtime enforcement.

---

## 18. Recommended Next Step

**Single next artifact:** `NOVA ROLE REALITY MODEL v1` (or phased Roles charter) — first layer **after** Workflow Reality, defining:

- obligation and work domain ownership vocabulary
- authority semantics bound to `contract_type_code × workflow_type_code`
- explicit separation from Approvals and Templates

**Do not skip to:** Role Registry automation, Agent Cards, Tool Catalog, Templates, Approval Systems, Workflow Records storage, Runtime, or Automation until Roles charter approved — or human explicitly charters a different next layer.

**Optional parallel (human choice):** commit full NOVA foundation pack to `projects/nova/foundation/` including this file.

**Prior artifact update (optional):** Contract Reality Model §18 Recommended Next Step — mark Workflow Reality as complete; point to Roles as next.

---

## Appendix A — Workflow Pressure Snapshot template

```markdown
# Workflow Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| workflow_type_code | activation_posture | effective_weight | workflow_state | source_contract | V-target |
|--------------------|--------------------|------------------|----------------|-----------------|----------|
| WF_INTAKE          |                    |                  |                |                 |          |
| ...                |                    |                  |                |                 |          |

Dominant workflows this stage:
Blocked workflows (WS_BLOCKED):
Misaligned workflows (WS_MISALIGNED):
SAFE UNKNOWN workflows:
```

---

## Appendix B — RBM layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | Decision Reality Model v1 | Complete |
| Contracts | Contract Reality Model v1 | Complete |
| **Workflow** | **Workflow Reality Model v1** | **This document — vocabulary complete** |
| Roles | — | Not started (recommended next) |
| Tools | — | Not started |
| Agents | — | Not started |
| Automation | — | Not started |

---

**Document status:** v1 design complete — first execution-oriented workflow vocabulary for NOVA mobile products. Nothing beyond Workflow Reality.




