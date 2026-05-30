# NOVA Role Reality Model v1

**Status:** design-only — Reality-layer responsibility domain vocabulary, not staffing, not org chart, not job titles, not agent cards, not approval chains, not runtime  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → NOVA Contract Reality Model v1 → NOVA Workflow Reality Model v1 → **this document**  
**Non-claims:** no agents, no orchestration, no staffing records, no org structure, no role assignment automation, no agent cards, no tool catalog, no database schema

**Parent Reality artifacts:**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`
- NOVA Decision Reality Model v1 — structural choice domains per `decision_type_code`
- NOVA Contract Reality Model v1 — obligation domains per `contract_type_code`
- NOVA Workflow Reality Model v1 — work structure domains per `workflow_type_code`

**Evidence base:** Website Factory handoff-collapse and production-drift lessons; ORCA semantic-vs-deployed sync and URL registry alignment; MARS survivability snapshot/rollback/recovery discipline; real-world mobile delivery practices adapted to NOVA

---

## 1. Executive Summary

NOVA Role Reality Model v1 — **первый responsibility-domain artifact NOVA после Workflow Reality**. Он отвечает на вопрос:

> **«Какие домены ответственности существуют, потому что существуют workflow domains?»**

Не «кто выполняет работу» (Staffing), не «какой сотрудник» (HR), не «какой агент» (Agent Cards), не «какой отдел» (Org Structure), не «кто утверждает» (Approvals — future).

| Элемент | Содержание |
|---------|------------|
| **18 role domains** | `RL_INTAKE` … `RL_RECOVERY` — derived from workflow families |
| **Canonical role object** | `role_type_code` + required reality fields |
| **Role registry** | 18 rows with purpose, source workflows, outputs, failure modes |
| **Workflow → Role mapping** | 18 workflow families → primary responsibility domains |
| **Contract → Role mapping** | 18 contract families → obligation coverage domains |
| **Lifecycle role pressure matrix** | Dominant role domains per `LC_*` stage |
| **Product class role pressure matrix** | 8 focus classes × role criticality |
| **Role weight model** | 4 classes: `RW_SUPPORTING` → `RW_TERMINAL` |
| **Role state model** | 8 states: `RS_LATENT` → `RS_SUPERSEDED` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Role Reality (this doc) | Role Execution (NOT this) |
|-----------|------------------------|---------------------------|
| **Question** | What responsibility domains exist because workflows exist? | Who is assigned to each domain? |
| **Layer** | Reality → Roles (structure) | Staffing · Approvals · Agent Cards · Runtime (future) |
| **Example** | `RL_COMPLIANCE` = compliance alignment responsibility domain exists when `WF_COMPLIANCE_ALIGNMENT` is active | Legal counsel named as assignee |
| **Output** | Vocabulary + workflow→responsibility maps | RACI matrices, org charts, agent cards, on-call rosters |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answered:** «What must be true?» (`contract_type_code`)  
**Workflow Reality answered:** «How does obligation become structured work?» (`workflow_type_code`)  
**Role Reality answers:** «What responsibility domains must exist to cover that work?» (`role_type_code`)

Without role reality, workflows exist as orphan work structures, obligations have no coverage domain, and teams assign people to tasks without knowing which responsibility vacuum they are filling.

---

## 2. Role Philosophy

### 2.1 What a role means inside NOVA

В NOVA **role** — это **домен ответственности**, который:

1. **Существует потому что workflow domain существует** — не потому что в org chart есть должность
2. **Actor-neutral** — описывает *какую область ответственности* нужно покрыть, не *кто* её покрывает
3. **Привязан к workflow coverage** — каждый активный `workflow_type_code` требует named `role_type_code` coverage
4. **Производит accountability surface** — когда `WS_MISALIGNED` или `WS_BLOCKED`, domain определяет *где искать ответственность*, не *кого наказать*
5. **Отделён от execution assignment** — human, team, agent, tool may *occupy* domain later; domain exists first

Role — **не должность**. «Product Manager» — staffing artifact. `RL_PRODUCT` — responsibility domain for product identity and thesis alignment work.

**Website Factory lesson:** handoff collapse = `WF_OPERATIONS_READINESS` existed structurally via `CTR_OPERATIONS`, but **no responsibility domain** covered survivability work — delivery completed, ops domain vacant ([`production-drift-taxonomy.md`](../../projects/mars-website-factory/production-drift-taxonomy.md)).

**ORCA lesson:** URL registry desync = `WF_ECOSYSTEM_SYNC` active, but **ecosystem coupling responsibility** treated as one-time deploy task, not standing domain ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

### 2.2 Why roles exist

Workflows **структурируют работу**. Без role layer работа остаётся:

- executed by whoever is available;
- orphaned when people leave;
- duplicated when two actors cover same domain;
- vacant when critical workflow is active but no domain claims coverage.

Role **переводит workflow structure в responsibility structure** — без назначения исполнителей.

| Workflow says | Role crystallizes |
|---------------|-------------------|
| `WF_COMPLIANCE_ALIGNMENT` structures compliance work | `RL_COMPLIANCE` domain must exist to cover alignment outputs |
| `WF_OPERATIONS_READINESS` structures survivability work | `RL_OPERATIONS` domain must exist before Production claim |
| `WF_VALIDATION` cross-cuts all contracts | `RL_VALIDATION` domain owns verification coverage |
| `WF_RECOVERY` structures corrective retreat | `RL_RECOVERY` domain owns rollback/quarantine accountability |

**MARS Survivability lesson:** snapshot before transition requires **`RL_RECOVERY` + `RL_LIFECYCLE` coverage** — not optional heroics assigned ad hoc ([`snapshot-manifest-standard-v1.md`](../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)).

### 2.3 Why roles come after workflows

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random responsibility labels |
| **Lifecycle** | Stage-appropriate domain depth | Full ops domain at Concept |
| **Decisions** | Choice domains | Roles cover unchosen problems |
| **Contracts** | Obligation structure | Roles without obligation context |
| **Workflow** | Work structure domains | Roles assign people to arbitrary tasks |
| **Roles** | Responsibility domain vocabulary | Tools/agents attach to noise |

**Roles без Workflow Reality** — org theater:

- «QA lead» exists before knowing `WF_VALIDATION` scope
- «Dev team» owns everything because no workflow→role map
- Agent card assigned before knowing which domain it should occupy

Workflows **не назначаются** — они описывают work structure. Roles **определяют coverage domains**, необходимые чтобы work structure не осталась orphan.

### 2.4 Why roles are not people

| Role Reality | People / Staffing (NOT this) |
|--------------|-------------------------------|
| **What responsibility domain** workflow requires | **Who** currently covers it |
| `RL_COMPLIANCE` = compliance alignment coverage domain | Maria, Legal Dept, external counsel |
| Survives reorg, attrition, agent swap | Resets when people change |
| Actor-neutral domain vocabulary | Authority tied to person |
| One domain; zero or many occupants allowed later | One person = one job title |

**Boundary test:** If you remove all people, teams, and agents, do responsibility domains still make sense? **Yes** → role. **No** → staffing artifact.

Examples:

| Artifact | Layer |
|----------|-------|
| «Compliance alignment domain must cover store category vs implementation» | `RL_COMPLIANCE` — role |
| «Maria approves privacy policy» | Approvals + Staffing — not role |
| «Implementation domain must honor charter boundary» | `RL_IMPLEMENTATION` — role |
| «Sprint 14 owned by Team Alpha» | Team scheduling — not role |
| «Rollback accountability domain active before wide release» | `RL_RECOVERY` + `RL_RELEASE` — role |
| «QA lead sign-off in Jira» | Approvals + Tools — not role |

### 2.5 What transforms workflow responsibility into role responsibility?

**Transformation chain (conceptual):**

```text
workflow_type_code + workflow_state_code + effective_weight_class
    ↓ requires coverage
role_type_code + role_weight_class + role_state_code
    ↓ defines (future Staffing/Tools/Agents layer assigns occupants)
coverage_outputs[] + failure_accountability_surface
```

**Transformers (this layer only):**

1. **Workflow activation** — which `workflow_type_code` is structurally active (`WS_ACTIVATED`+)
2. **Coverage requirement** — active workflow at `WW_COORDINATED`+ requires non-vacant role domain
3. **Cross-cutting overlay** — `WF_VALIDATION` always requires `RL_VALIDATION` when any alignment workflow is active
4. **Obligation trace** — role domain must trace to `source_workflow_type_code` and upstream `contract_type_code`
5. **Lifecycle/class depth** — same role domain; weight and dominance vary by context

**What role adds beyond workflow:**

| Workflow provides | Role adds |
|-------------------|-----------|
| Work structure and sequencing | **Coverage obligation** — domain must exist |
| Expected alignment outputs | **Output accountability surface** — who domain answers for gaps |
| `WS_MISALIGNED` signal | **Failure domain** — which responsibility area owns resolution |
| Role-neutral execution | **Domain boundary** — what may not be delegated without explicit split |

**NOT transformers in v1:** assignee, team, agent_ref, on_call_rotation, approval_authority, RACI letter.

---

## 3. Role Taxonomy

### 3.1 Derivation rationale

Test for each candidate domain: *«Does NOVA treat responsibility coverage, failure accountability, and domain vacancy differently if this role type is absent when its source workflow is active?»*

**Rejected as standalone role domains:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Manager** | People hierarchy | Staffing / Org — not role |
| **Team** | Group of people | Staffing — not role |
| **Department** | Org structure | Explicitly forbidden |
| **Agent** | Execution actor | Agents layer (future) |
| **Tool operator** | Helper user | Tools layer (future) |
| **Approver** | Authority act | Approvals (future) |
| **Sponsor** | Portfolio person | May occupy `RL_INTAKE` later; not domain |
| **Scrum Master** | Process facilitation | Workflow execution — not domain |
| **Project Manager** | Coordination staffing | May span domains; not a role type |
| **Developer** | Job title | May occupy `RL_IMPLEMENTATION`; not domain |
| **Legal counsel** | Job title | May occupy `RL_COMPLIANCE`; not domain |

**Design choice:** 18 role domains — parallel density to workflow registry; one primary responsibility domain per workflow family. Preserves clean Workflow → Role derivation while allowing compound coverage within domains.

### 3.2 Role domains overview

```text
Attention layer:     RL_INTAKE
Identity layer:      RL_PRODUCT · RL_CLASSIFICATION
Boundary layer:      RL_CHARTER · RL_UX
Commitment layer:    RL_ARCHITECTURE · RL_DATA_PRIVACY · RL_COMPLIANCE
                     RL_COMMERCIAL · RL_TRUST_SAFETY
Execution layer:     RL_IMPLEMENTATION
Verification layer:  RL_VALIDATION
Operational layer:   RL_OPERATIONS · RL_RELEASE · RL_ECOSYSTEM
Temporal layer:      RL_LIFECYCLE · RL_EXPANSION · RL_INVESTMENT · RL_SUNSET
Corrective layer:    RL_RECOVERY
```

### 3.3 Domain definitions

#### `RL_INTAKE`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for binding product instance to NOVA reality context |
| **Source workflows** | `WF_INTAKE` |
| **Responsibility scope** | Portfolio entry honesty; lifecycle label at entry; continue/hold/kill coverage |
| **Lifecycle significance** | Dominant `LC_CONCEPT`; `LC_HOLD` resume |

---

#### `RL_PRODUCT`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for product identity, value hypothesis, and audience alignment work |
| **Source workflows** | `WF_DEFINITION` |
| **Responsibility scope** | Thesis truth; audience sketch; differentiation boundary; pivot honesty |
| **Lifecycle significance** | Dominant `LC_CONCEPT`–`LC_DISCOVERY`; pivot at `LC_PROOF` |

---

#### `RL_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for class, tier, and modifier binding work |
| **Source workflows** | `WF_CLASSIFICATION` |
| **Responsibility scope** | Registry-default honor; Extended vs Core path; tier honesty |
| **Lifecycle significance** | Mandatory before `LC_PROOF`; re-trigger on tier bump |

---

#### `RL_CHARTER`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for phase scope boundary definition and maintenance |
| **Source workflows** | `WF_CHARTER` |
| **Responsibility scope** | In/out scope; kill/pivot criteria; anti-perpetual-proof |
| **Lifecycle significance** | Critical at `LC_PROOF`, `LC_PILOT`, `LC_GROWTH` entry |

---

#### `RL_UX`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for core journey and interaction model work |
| **Source workflows** | `WF_UX_JOURNEY` |
| **Responsibility scope** | Journey coherence; pattern consistency; a11y posture |
| **Lifecycle significance** | `LC_DISCOVERY` model → `LC_PROOF` journey lock |

---

#### `RL_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for technical structure commitment work |
| **Source workflows** | `WF_ARCHITECTURE` |
| **Responsibility scope** | Stack honor; integration boundaries; scale posture |
| **Lifecycle significance** | Rises `LC_DISCOVERY`→`LC_PROOF` exit; strain at `LC_GROWTH` |

---

#### `RL_IMPLEMENTATION`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for implementation work honoring upstream definitions |
| **Source workflows** | `WF_BUILD` |
| **Responsibility scope** | Artifact production within charter; build drift prevention |
| **Lifecycle significance** | `LC_PROOF`–`LC_PRODUCTION`; maintenance in `LC_MATURE` |

---

#### `RL_VALIDATION`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for cross-cutting obligation verification work |
| **Source workflows** | `WF_VALIDATION` |
| **Responsibility scope** | V0–V3 verification coverage; alignment/misalignment declaration |
| **Lifecycle significance** | Every stage boundary; intensifies at Production entry |

---

#### `RL_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for data/privacy alignment work |
| **Source workflows** | `WF_DATA_ALIGNMENT` |
| **Responsibility scope** | Collection honesty; retention; export/delete path |
| **Lifecycle significance** | Before `LC_PILOT` if PII; terminal at `LC_SUNSET` |

---

#### `RL_COMPLIANCE`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for regulatory and store alignment work |
| **Source workflows** | `WF_COMPLIANCE_ALIGNMENT` |
| **Responsibility scope** | Store category; consent model; jurisdiction posture |
| **Lifecycle significance** | Hypothesis `LC_DISCOVERY`; binding before `LC_PRODUCTION` |

---

#### `RL_COMMERCIAL`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for monetization alignment work |
| **Source workflows** | `WF_COMMERCIAL_ALIGNMENT` |
| **Responsibility scope** | Payment path; refund path; pricing honesty |
| **Lifecycle significance** | `LC_DISCOVERY` model; real money at `LC_PILOT` |

---

#### `RL_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for safety, abuse, and AI limit alignment work |
| **Source workflows** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **Responsibility scope** | Safety policy; escalation path; autonomy limits |
| **Lifecycle significance** | Early AI/marketplace; mandatory pilot proof |

---

#### `RL_OPERATIONS`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for operational survivability work |
| **Source workflows** | `WF_OPERATIONS_READINESS` |
| **Responsibility scope** | Support path; monitoring; handoff bundle; incident response |
| **Lifecycle significance** | Lite at `LC_PILOT`; full at `LC_PRODUCTION` entry |

---

#### `RL_RELEASE`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for distribution and rollout alignment work |
| **Source workflows** | `WF_RELEASE` |
| **Responsibility scope** | Channel truth; rollout phasing; rollback readiness |
| **Lifecycle significance** | Internal at `LC_PROOF`; governed at `LC_PRODUCTION`+ |

---

#### `RL_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for external coupling sync work |
| **Source workflows** | `WF_ECOSYSTEM_SYNC` |
| **Responsibility scope** | Parity semantics; URL/registry alignment; API coupling |
| **Lifecycle significance** | Companion Discovery; per-deploy at Production |

---

#### `RL_LIFECYCLE`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for lifecycle transition work bundles |
| **Source workflows** | `WF_LIFECYCLE_TRANSITION` |
| **Responsibility scope** | Stage advance evidence; hold/regress/kill honesty |
| **Lifecycle significance** | Every `LC_*` boundary; `LC_HOLD` overlay |

---

#### `RL_EXPANSION`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for growth charter execution work |
| **Source workflows** | `WF_EXPANSION` |
| **Responsibility scope** | Feature/geo/segment expansion within charter |
| **Lifecycle significance** | Dominant `LC_GROWTH`; entry from `LC_PRODUCTION` |

---

#### `RL_INVESTMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for maintain/harvest/legacy posture work |
| **Source workflows** | `WF_INVESTMENT_REVIEW` |
| **Responsibility scope** | Investment honesty; maintenance scope; legacy withdrawal truth |
| **Lifecycle significance** | `LC_MATURE`, `LC_LEGACY` |

---

#### `RL_SUNSET`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for end-of-life execution work |
| **Source workflows** | `WF_SUNSET` |
| **Responsibility scope** | Migration; export; decommission; user communication |
| **Lifecycle significance** | `LC_LEGACY` planning → `LC_SUNSET` execution |

---

#### `RL_RECOVERY`

| Field | Value |
|-------|-------|
| **Purpose** | Cover responsibility for corrective retreat work |
| **Source workflows** | `WF_RECOVERY` |
| **Responsibility scope** | Snapshot; rollback; quarantine; restore evidence |
| **Lifecycle significance** | Any stage; mandatory at high-risk transitions |

---

## 4. Role Object Model

Canonical role object describes **a responsibility domain type in context**, not a staffing record. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`, `contract_type_code`, `workflow_type_code`.

### 4.1 Core identifier

**`role_type_code`** — immutable registry key; one of 18 domain codes in §3.

### 4.2 Required fields (reality model)

```text
role_reality_object {
  // Identity
  role_type_code                  // required — e.g. RL_COMPLIANCE
  role_domain_layer               // required — attention | identity | boundary | commitment |
                                  //            execution | verification | operational | temporal | corrective

  // Definition
  responsibility_subject        // required — short noun phrase: what domain covers
  responsibility_purpose_statement // required — canonical coverage form (not job description)

  // Workflow binding (conceptual — not storage)
  source_workflow_type_codes[]  // required — which workflows require this domain
  source_contract_type_codes[]  // required — upstream obligations this domain covers
  lifecycle_state_codes[]       // required — stages where domain is structurally required
  product_class_affinity[]      // required — classes where criticality elevates

  // Classification
  default_weight_class          // required — RW_* (see §10)
  default_dominance_posture     // required — DP_* (see §4.3)

  // Coverage model (descriptive only)
  coverage_obligations[]        // required — what alignment outputs domain must answer for
  prerequisite_role_type_codes[] // required — upstream domains that must reach RS_COVERED or RS_DORMANT
  expected_coverage_outputs[]   // required — output categories domain owns when workflow aligned
  typical_vacancy_signal        // required — one-line domain-unoccupied indicator

  // Failure surface
  failure_accountability_scope  // required — what misalignment types domain owns resolution for
  overlap_risk_domains[]        // optional — domains commonly confused with this one

  // Boundaries
  is_person                     // required — always false
  is_job_title                  // required — always false
  is_team                       // required — always false
  is_agent                      // required — always false
  is_approval_authority         // required — always false for valid role types
  confusion_cues[]              // optional — what people mistake for this role
}
```

### 4.3 Dominance posture (descriptive, not staffing)

| Posture | Meaning |
|---------|---------|
| **DP_LATENT** | Domain exists in vocabulary; not yet structurally required |
| **DP_REQUIRED** | Active workflow requires domain coverage now |
| **DP_DOMINANT** | Primary responsibility focus for current stage/class |
| **DP_BLOCKING** | Downstream domains cannot claim coverage until this domain is covered |
| **DP_DORMANT** | Not applicable at current stage/class |

### 4.4 Instance overlay (future binding, not v1 storage)

When applied to a product instance:

```text
role_pressure_instance {
  role_type_code,
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  source_workflow_type_code,     // triggering workflow
  source_contract_type_code,     // upstream obligation
  effective_weight_class,        // may elevate above default
  dominance_posture,             // DP_* at this moment
  role_state_code,               // RS_* (see §11)
  coverage_depth_expectation,    // derived from workflow V-target
  class_amplification_notes
}
```

**Non-claims:** no `assignee_id`, no `team_ref`, no `agent_ref`, no `on_call`, no `reports_to` — those belong to Staffing / Agent Cards / Approvals layers (future), explicitly out of scope.

---

## 5. Role Registry

Immutable registry rows parallel to workflow and contract registries. Codes frozen at v1.

### 5.1 Registry rows

#### `RL_INTAKE`

| Field | Value |
|-------|-------|
| **code** | `RL_INTAKE` |
| **definition** | Responsibility domain for NOVA context binding at product entry or re-entry |
| **source workflow families** | `WF_INTAKE` |
| **source contract families** | `CTR_EXISTENCE`, `CTR_CLASSIFICATION` (hypothesis) |
| **responsibility scope** | Entry honesty; lifecycle label; portfolio attention coverage |
| **expected outputs** | Intake coverage declaration; entry posture accountability |
| **common failure patterns** | Stealth product — no domain claimed; wrong lifecycle at entry |

---

#### `RL_PRODUCT`

| Field | Value |
|-------|-------|
| **code** | `RL_PRODUCT` |
| **definition** | Responsibility domain for product identity and thesis alignment work |
| **source workflow families** | `WF_DEFINITION` |
| **source contract families** | `CTR_PRODUCT`, `CTR_AUDIENCE` |
| **responsibility scope** | Value hypothesis; audience; differentiation; pivot honesty |
| **expected outputs** | Product thesis coverage; audience alignment accountability |
| **common failure patterns** | Build before thesis; semantic ≠ deployed (ORCA) |

---

#### `RL_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **code** | `RL_CLASSIFICATION` |
| **definition** | Responsibility domain for class/tier/modifier binding work |
| **source workflow families** | `WF_CLASSIFICATION` |
| **source contract families** | `CTR_CLASSIFICATION` |
| **responsibility scope** | Registry binding; tier honesty; Extended path selection |
| **expected outputs** | Class binding coverage; tier accountability |
| **common failure patterns** | T1 label on T3 product; utility creep without reclassification |

---

#### `RL_CHARTER`

| Field | Value |
|-------|-------|
| **code** | `RL_CHARTER` |
| **definition** | Responsibility domain for phase scope boundary work |
| **source workflow families** | `WF_CHARTER` |
| **source contract families** | `CTR_SCOPE`, `CTR_LIFECYCLE` |
| **responsibility scope** | In/out boundary; kill/pivot criteria; charter maintenance |
| **expected outputs** | Charter coverage; boundary violation accountability |
| **common failure patterns** | Perpetual proof; MVP inflation; charter vacuum |

---

#### `RL_UX`

| Field | Value |
|-------|-------|
| **code** | `RL_UX` |
| **definition** | Responsibility domain for core journey and interaction model work |
| **source workflow families** | `WF_UX_JOURNEY` |
| **source contract families** | `CTR_UX` |
| **responsibility scope** | Journey architecture; pattern consistency; a11y posture |
| **expected outputs** | Journey coverage; UX drift accountability |
| **common failure patterns** | Screen polish without journey; a11y deferred |

---

#### `RL_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **code** | `RL_ARCHITECTURE` |
| **definition** | Responsibility domain for technical structure commitment work |
| **source workflow families** | `WF_ARCHITECTURE` |
| **source contract families** | `CTR_ARCHITECTURE` |
| **responsibility scope** | Stack honor; integration boundaries; spike conclusions |
| **expected outputs** | Architecture coverage; scale surprise accountability |
| **common failure patterns** | Diagram ≠ committed stack; undeclared API surface |

---

#### `RL_IMPLEMENTATION`

| Field | Value |
|-------|-------|
| **code** | `RL_IMPLEMENTATION` |
| **definition** | Responsibility domain for implementation delivery honoring upstream definitions |
| **source workflow families** | `WF_BUILD` |
| **source contract families** | All active boundary/commitment contracts (implementation honor) |
| **responsibility scope** | Artifact production within charter; build drift |
| **expected outputs** | Build coverage; implementation misalignment accountability |
| **common failure patterns** | Build outside charter; drift from definitions |

---

#### `RL_VALIDATION`

| Field | Value |
|-------|-------|
| **code** | `RL_VALIDATION` |
| **definition** | Responsibility domain for cross-cutting obligation verification |
| **source workflow families** | `WF_VALIDATION` |
| **source contract families** | All `CTR_*` under verification |
| **responsibility scope** | V0–V3 coverage; alignment declaration; bypass prevention |
| **expected outputs** | Validation coverage map; misalignment declaration accountability |
| **common failure patterns** | Green QA without obligation mapping; validation bypass |

---

#### `RL_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **code** | `RL_DATA_PRIVACY` |
| **definition** | Responsibility domain for data/privacy alignment work |
| **source workflow families** | `WF_DATA_ALIGNMENT` |
| **source contract families** | `CTR_DATA_PRIVACY` |
| **responsibility scope** | Collection honesty; retention; export/delete |
| **expected outputs** | Data category coverage; privacy mismatch accountability |
| **common failure patterns** | Privacy label mismatch; shadow collection |

---

#### `RL_COMPLIANCE`

| Field | Value |
|-------|-------|
| **code** | `RL_COMPLIANCE` |
| **definition** | Responsibility domain for regulatory and store alignment work |
| **source workflow families** | `WF_COMPLIANCE_ALIGNMENT` |
| **source contract families** | `CTR_COMPLIANCE` |
| **responsibility scope** | Store category; consent; jurisdiction posture |
| **expected outputs** | Compliance posture coverage; store rejection accountability |
| **common failure patterns** | Legal later; doc exists but product violates |

---

#### `RL_COMMERCIAL`

| Field | Value |
|-------|-------|
| **code** | `RL_COMMERCIAL` |
| **definition** | Responsibility domain for monetization alignment work |
| **source workflow families** | `WF_COMMERCIAL_ALIGNMENT` |
| **source contract families** | `CTR_COMMERCIAL` |
| **responsibility scope** | Payment path; refund; pricing honesty |
| **expected outputs** | Commercial alignment coverage; chargeback accountability |
| **common failure patterns** | First payment in Production; hidden fees |

---

#### `RL_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **code** | `RL_TRUST_SAFETY` |
| **definition** | Responsibility domain for safety and AI limit alignment work |
| **source workflow families** | `WF_TRUST_SAFETY_ALIGNMENT` |
| **source contract families** | `CTR_TRUST_SAFETY` |
| **responsibility scope** | Safety policy; escalation; autonomy limits |
| **expected outputs** | Safety coverage; harm incident accountability |
| **common failure patterns** | Autonomy beyond limits; no escalation |

---

#### `RL_OPERATIONS`

| Field | Value |
|-------|-------|
| **code** | `RL_OPERATIONS` |
| **definition** | Responsibility domain for operational survivability work |
| **source workflow families** | `WF_OPERATIONS_READINESS` |
| **source contract families** | `CTR_OPERATIONS`, `CTR_INVESTMENT` |
| **responsibility scope** | Support; monitoring; handoff; incident response |
| **expected outputs** | Ops playbook coverage; handoff collapse accountability |
| **common failure patterns** | Handoff collapse (Factory); tribal knowledge only |

---

#### `RL_RELEASE`

| Field | Value |
|-------|-------|
| **code** | `RL_RELEASE` |
| **definition** | Responsibility domain for distribution and rollout alignment work |
| **source workflow families** | `WF_RELEASE` |
| **source contract families** | `CTR_RELEASE`, `CTR_LIFECYCLE` |
| **responsibility scope** | Channel truth; rollout; rollback readiness |
| **expected outputs** | Release posture coverage; untested rollback accountability |
| **common failure patterns** | Ship = Production confusion; rollback untested |

---

#### `RL_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **code** | `RL_ECOSYSTEM` |
| **definition** | Responsibility domain for external coupling sync work |
| **source workflow families** | `WF_ECOSYSTEM_SYNC` |
| **source contract families** | `CTR_ECOSYSTEM`, `CTR_PRODUCT` (companion) |
| **responsibility scope** | Parity; URL/registry; API coupling |
| **expected outputs** | Sync audit coverage; semantic ≠ deployed accountability |
| **common failure patterns** | One-time sync; URL registry drift (ORCA) |

---

#### `RL_LIFECYCLE`

| Field | Value |
|-------|-------|
| **code** | `RL_LIFECYCLE` |
| **definition** | Responsibility domain for lifecycle transition work bundles |
| **source workflow families** | `WF_LIFECYCLE_TRANSITION` |
| **source contract families** | `CTR_LIFECYCLE`, `CTR_EXISTENCE` |
| **responsibility scope** | Stage advance evidence; hold/regress/kill |
| **expected outputs** | Transition evidence coverage; stage lie accountability |
| **common failure patterns** | Skip without evidence; store badge = stage |

---

#### `RL_EXPANSION`

| Field | Value |
|-------|-------|
| **code** | `RL_EXPANSION` |
| **definition** | Responsibility domain for growth charter execution work |
| **source workflow families** | `WF_EXPANSION` |
| **source contract families** | `CTR_EXPANSION` |
| **responsibility scope** | Feature/geo/segment expansion within charter |
| **expected outputs** | Expansion execution coverage; overreach accountability |
| **common failure patterns** | Undocumented geo launch; feature explosion |

---

#### `RL_INVESTMENT`

| Field | Value |
|-------|-------|
| **code** | `RL_INVESTMENT` |
| **definition** | Responsibility domain for maintain/harvest/legacy posture work |
| **source workflow families** | `WF_INVESTMENT_REVIEW` |
| **source contract families** | `CTR_INVESTMENT`, `CTR_EXISTENCE` |
| **responsibility scope** | Investment honesty; maintenance scope; legacy truth |
| **expected outputs** | Investment posture coverage; zombie product accountability |
| **common failure patterns** | Zombie stability; security rot masked |

---

#### `RL_SUNSET`

| Field | Value |
|-------|-------|
| **code** | `RL_SUNSET` |
| **definition** | Responsibility domain for end-of-life execution work |
| **source workflow families** | `WF_SUNSET` |
| **source contract families** | `CTR_SUNSET`, `CTR_DATA_PRIVACY` |
| **responsibility scope** | Migration; export; decommission; comms |
| **expected outputs** | Sunset timeline coverage; data loss accountability |
| **common failure patterns** | Abrupt shutdown; retention breach |

---

#### `RL_RECOVERY`

| Field | Value |
|-------|-------|
| **code** | `RL_RECOVERY` |
| **definition** | Responsibility domain for corrective retreat work |
| **source workflow families** | `WF_RECOVERY` |
| **source contract families** | Violation-triggered; `CTR_LIFECYCLE` regress |
| **responsibility scope** | Snapshot; rollback; quarantine; restore |
| **expected outputs** | Recovery charter coverage; fix-forward accountability |
| **common failure patterns** | No snapshot before transition; recovery ad hoc |

---

## 6. Workflow → Role Mapping

Core mapping: every active workflow family **requires** a primary responsibility domain for coverage.

### 6.1 Primary mapping (1:1 workflow → role)

| `workflow_type_code` | Primary `role_type_code` | Responsibility domain activated |
|----------------------|--------------------------|--------------------------------|
| `WF_INTAKE` | `RL_INTAKE` | Portfolio entry coverage |
| `WF_DEFINITION` | `RL_PRODUCT` | Product identity coverage |
| `WF_CLASSIFICATION` | `RL_CLASSIFICATION` | Class binding coverage |
| `WF_CHARTER` | `RL_CHARTER` | Scope boundary coverage |
| `WF_UX_JOURNEY` | `RL_UX` | Journey architecture coverage |
| `WF_ARCHITECTURE` | `RL_ARCHITECTURE` | Technical structure coverage |
| `WF_BUILD` | `RL_IMPLEMENTATION` | Implementation delivery coverage |
| `WF_VALIDATION` | `RL_VALIDATION` | Verification coverage |
| `WF_DATA_ALIGNMENT` | `RL_DATA_PRIVACY` | Data/privacy alignment coverage |
| `WF_COMPLIANCE_ALIGNMENT` | `RL_COMPLIANCE` | Regulatory alignment coverage |
| `WF_COMMERCIAL_ALIGNMENT` | `RL_COMMERCIAL` | Monetization alignment coverage |
| `WF_TRUST_SAFETY_ALIGNMENT` | `RL_TRUST_SAFETY` | Safety alignment coverage |
| `WF_OPERATIONS_READINESS` | `RL_OPERATIONS` | Survivability coverage |
| `WF_RELEASE` | `RL_RELEASE` | Distribution/rollout coverage |
| `WF_ECOSYSTEM_SYNC` | `RL_ECOSYSTEM` | External coupling coverage |
| `WF_LIFECYCLE_TRANSITION` | `RL_LIFECYCLE` | Stage transition coverage |
| `WF_EXPANSION` | `RL_EXPANSION` | Growth charter coverage |
| `WF_INVESTMENT_REVIEW` | `RL_INVESTMENT` | Investment posture coverage |
| `WF_SUNSET` | `RL_SUNSET` | End-of-life coverage |
| `WF_RECOVERY` | `RL_RECOVERY` | Corrective retreat coverage |

### 6.2 Secondary domain activations

| Trigger workflow | Also requires domain | Condition |
|------------------|---------------------|-----------|
| Any `WF_*` at `WW_COORDINATED`+ | `RL_VALIDATION` | Verification expected |
| Any `WW_CRITICAL`+ violation | `RL_RECOVERY` | Corrective domain mandatory |
| `WF_BUILD` at Proof+ | `RL_CHARTER`, `RL_IMPLEMENTATION` | Both must be covered |
| `WF_LIFECYCLE_TRANSITION` Production | `RL_OPERATIONS`, `RL_COMPLIANCE`, `RL_RELEASE` | Full domain set |
| `WF_ECOSYSTEM_SYNC` + deploy | `RL_ECOSYSTEM` re-required | Per-deploy (ORCA) |
| `WF_EXPANSION` + geo | `RL_COMPLIANCE`, `RL_DATA_PRIVACY` | Jurisdiction expansion |
| `WF_SUNSET` | `RL_DATA_PRIVACY`, `RL_COMPLIANCE` | Terminal obligations |

### 6.3 Workflow weight → role weight elevation

| Workflow weight | Typical role weight | Notes |
|-----------------|----------------------|-------|
| `WW_ROUTINE` | `RW_SUPPORTING` | Light coverage sufficient |
| `WW_COORDINATED` | `RW_SUPPORTING` or `RW_STRUCTURAL` | Domain must be explicitly covered |
| `WW_STRUCTURAL` | `RW_STRUCTURAL` | Blocking if vacant |
| `WW_CRITICAL` | `RW_CRITICAL` | Vacancy = integrity failure |
| `WW_TERMINAL` | `RW_TERMINAL` | Irreversible path domain |

### 6.4 Mapping diagram

```text
WF_INTAKE ──────────────► RL_INTAKE
WF_DEFINITION ──────────► RL_PRODUCT
WF_CLASSIFICATION ──────► RL_CLASSIFICATION
WF_CHARTER ─────────────► RL_CHARTER ──────────► RL_IMPLEMENTATION (constraint)
WF_UX_JOURNEY ──────────► RL_UX ───────────────► RL_IMPLEMENTATION (constraint)
WF_ARCHITECTURE ────────► RL_ARCHITECTURE ─────► RL_IMPLEMENTATION · RL_VALIDATION
WF_BUILD ───────────────► RL_IMPLEMENTATION
WF_VALIDATION ──────────► RL_VALIDATION (cross-cutting)
WF_DATA_ALIGNMENT ──────► RL_DATA_PRIVACY ────► RL_VALIDATION
WF_COMPLIANCE_ALIGNMENT ► RL_COMPLIANCE ──────► RL_VALIDATION
WF_COMMERCIAL_ALIGNMENT ► RL_COMMERCIAL ──────► RL_VALIDATION
WF_TRUST_SAFETY_ALIGNMENT ► RL_TRUST_SAFETY ► RL_VALIDATION
WF_OPERATIONS_READINESS ► RL_OPERATIONS ──────► RL_VALIDATION
WF_RELEASE ─────────────► RL_RELEASE ────────► RL_ECOSYSTEM (if coupled)
WF_LIFECYCLE_TRANSITION ► RL_LIFECYCLE ──────► RL_RECOVERY (if regress)
WF_EXPANSION ───────────► RL_EXPANSION ───────► RL_COMPLIANCE (geo)
WF_ECOSYSTEM_SYNC ──────► RL_ECOSYSTEM
WF_INVESTMENT_REVIEW ───► RL_INVESTMENT
WF_SUNSET ──────────────► RL_SUNSET ──────────► RL_DATA_PRIVACY
WF_RECOVERY ────────────► RL_RECOVERY

All WF_* at verification ─► RL_VALIDATION must be covered
Any WW_CRITICAL+ breach ──► RL_RECOVERY domain mandatory
```

### 6.5 Example chain (user charter)

```text
WF_COMPLIANCE_ALIGNMENT (WS_ACTIVATED, WW_CRITICAL)
    ↓ requires coverage
RL_COMPLIANCE (RS_REQUIRED, RW_CRITICAL)
    ↓ plus cross-cutting
RL_VALIDATION (RS_REQUIRED, RW_STRUCTURAL)
    ↓ produces (future Staffing/Tools layer assigns occupants)
compliance alignment coverage + verification accountability surface
```

No people. No agents. No approvals. Only responsibility domain reality.

---

## 7. Contract → Role Mapping

Core mapping: every major contract family **requires** responsibility domain coverage when obligation pressure is active.

### 7.1 Primary mapping (contract → role)

| `contract_type_code` | Primary `role_type_code` | Coverage obligation |
|----------------------|--------------------------|---------------------|
| `CTR_EXISTENCE` | `RL_INTAKE`, `RL_INVESTMENT` | Portfolio attention coverage |
| `CTR_PRODUCT` | `RL_PRODUCT` | Identity alignment coverage |
| `CTR_CLASSIFICATION` | `RL_CLASSIFICATION` | Class binding coverage |
| `CTR_AUDIENCE` | `RL_PRODUCT` | Audience stream within product domain |
| `CTR_SCOPE` | `RL_CHARTER` | Boundary coverage |
| `CTR_UX` | `RL_UX` | Journey coverage |
| `CTR_ARCHITECTURE` | `RL_ARCHITECTURE` | Structure coverage |
| `CTR_DATA_PRIVACY` | `RL_DATA_PRIVACY` | Privacy alignment coverage |
| `CTR_COMPLIANCE` | `RL_COMPLIANCE` | Regulatory coverage |
| `CTR_COMMERCIAL` | `RL_COMMERCIAL` | Monetization coverage |
| `CTR_TRUST_SAFETY` | `RL_TRUST_SAFETY` | Safety coverage |
| `CTR_OPERATIONS` | `RL_OPERATIONS` | Survivability coverage |
| `CTR_RELEASE` | `RL_RELEASE` | Distribution coverage |
| `CTR_LIFECYCLE` | `RL_LIFECYCLE` | Transition coverage |
| `CTR_EXPANSION` | `RL_EXPANSION` | Growth coverage |
| `CTR_ECOSYSTEM` | `RL_ECOSYSTEM` | Coupling coverage |
| `CTR_INVESTMENT` | `RL_INVESTMENT` | Posture coverage |
| `CTR_SUNSET` | `RL_SUNSET` | End-of-life coverage |

### 7.2 Secondary coverage (contract triggers additional domains)

| Trigger contract | Also requires | Condition |
|------------------|---------------|-----------|
| Any `CTR_*` at V1+ | `RL_VALIDATION` | Verification coverage |
| Any `CW_CRITICAL`+ violation | `RL_RECOVERY` | Corrective domain |
| `CTR_SCOPE` + build | `RL_IMPLEMENTATION` | Implementation within boundary |
| `CTR_LIFECYCLE` Production | `RL_OPERATIONS`, `RL_COMPLIANCE`, `RL_RELEASE` | Full ops/compliance/release domains |
| `CTR_ECOSYSTEM` + deploy | `RL_ECOSYSTEM` | Per-deployment (ORCA) |
| `CTR_SUNSET` | `RL_DATA_PRIVACY`, `RL_COMPLIANCE` | Terminal data obligations |

### 7.3 Contract → Role diagram

```text
CTR_EXISTENCE ──────────► RL_INTAKE · RL_INVESTMENT
CTR_PRODUCT ────────────► RL_PRODUCT
CTR_CLASSIFICATION ─────► RL_CLASSIFICATION
CTR_AUDIENCE ───────────► RL_PRODUCT (audience stream)
CTR_SCOPE ──────────────► RL_CHARTER ──────────► RL_IMPLEMENTATION
CTR_UX ─────────────────► RL_UX
CTR_ARCHITECTURE ───────► RL_ARCHITECTURE
CTR_DATA_PRIVACY ───────► RL_DATA_PRIVACY
CTR_COMPLIANCE ─────────► RL_COMPLIANCE
CTR_COMMERCIAL ─────────► RL_COMMERCIAL
CTR_TRUST_SAFETY ───────► RL_TRUST_SAFETY
CTR_OPERATIONS ─────────► RL_OPERATIONS
CTR_RELEASE ────────────► RL_RELEASE
CTR_LIFECYCLE ──────────► RL_LIFECYCLE
CTR_EXPANSION ──────────► RL_EXPANSION
CTR_ECOSYSTEM ──────────► RL_ECOSYSTEM
CTR_INVESTMENT ─────────► RL_INVESTMENT
CTR_SUNSET ─────────────► RL_SUNSET

All CTR_* at verification ─► RL_VALIDATION
Any CW_CRITICAL+ breach ───► RL_RECOVERY
```

---

## 8. Lifecycle Role Pressure Matrix

Dominant role domains per lifecycle stage. **Dominant** = structurally highest coverage pressure if vacant; **Active** = required secondary; **Latent** = usually dormant; **Dormant** = atypical.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `RL_INTAKE`, `RL_PRODUCT` | `RL_CLASSIFICATION` (hypothesis) | `RL_VALIDATION` (V0) | `RL_IMPLEMENTATION`, `RL_OPERATIONS`, `RL_COMPLIANCE` |
| **`LC_DISCOVERY`** | `RL_PRODUCT`, `RL_CLASSIFICATION`, `RL_CHARTER` (hypothesis) | `RL_UX`, `RL_DATA_PRIVACY`, `RL_COMPLIANCE` (hypothesis), `RL_COMMERCIAL`, `RL_TRUST_SAFETY`, `RL_ECOSYSTEM` | `RL_ARCHITECTURE` | `RL_OPERATIONS`, `RL_RELEASE` |
| **`LC_PROOF`** | `RL_CHARTER`, `RL_LIFECYCLE`, `RL_UX`, `RL_IMPLEMENTATION` | `RL_ARCHITECTURE`, `RL_VALIDATION`, `RL_PRODUCT` (pivot) | `RL_DATA_PRIVACY`, `RL_TRUST_SAFETY` | `RL_OPERATIONS` (full), `RL_EXPANSION` |
| **`LC_PILOT`** | `RL_LIFECYCLE`, `RL_OPERATIONS` (lite), `RL_RELEASE`, `RL_VALIDATION` | `RL_COMMERCIAL`, `RL_TRUST_SAFETY`, `RL_COMPLIANCE`, `RL_DATA_PRIVACY` | `RL_ARCHITECTURE` | `RL_EXPANSION`, `RL_INVESTMENT` |
| **`LC_PRODUCTION`** | `RL_LIFECYCLE`, `RL_OPERATIONS`, `RL_COMPLIANCE`, `RL_RELEASE`, `RL_VALIDATION` | `RL_ARCHITECTURE`, `RL_DATA_PRIVACY`, `RL_COMMERCIAL`, `RL_TRUST_SAFETY`, `RL_IMPLEMENTATION` | `RL_EXPANSION` (entry) | `RL_SUNSET` |
| **`LC_GROWTH`** | `RL_EXPANSION`, `RL_LIFECYCLE`, `RL_ARCHITECTURE`, `RL_VALIDATION` | `RL_COMPLIANCE`, `RL_COMMERCIAL`, `RL_TRUST_SAFETY`, `RL_CHARTER` | `RL_UX` (new surfaces) | `RL_INTAKE` |
| **`LC_MATURE`** | `RL_INVESTMENT`, `RL_LIFECYCLE` | `RL_OPERATIONS`, `RL_COMPLIANCE`, `RL_IMPLEMENTATION` (maintenance) | `RL_EXPANSION` (refresh) | `RL_PRODUCT` |
| **`LC_LEGACY`** | `RL_INVESTMENT`, `RL_SUNSET` (planning), `RL_LIFECYCLE` | `RL_OPERATIONS` (minimal), `RL_COMPLIANCE`, `RL_DATA_PRIVACY` | `RL_ECOSYSTEM` (successor) | `RL_EXPANSION` |
| **`LC_SUNSET`** | `RL_SUNSET`, `RL_DATA_PRIVACY`, `RL_LIFECYCLE` | `RL_COMPLIANCE`, `RL_OPERATIONS` (wind-down), `RL_RELEASE` (final) | `RL_ECOSYSTEM` | `RL_COMMERCIAL`, `RL_EXPANSION` |
| **`LC_HOLD`** | `RL_INTAKE`, `RL_LIFECYCLE` | All prior-stage domains — **staleness review** via `RL_VALIDATION` | — | New `RL_EXPANSION` |

### 8.1 Stage-critical domain questions

| Stage | If only three domains must be covered |
|-------|---------------------------------------|
| `LC_CONCEPT` | `RL_INTAKE` · `RL_PRODUCT` · `RL_CLASSIFICATION` (hypothesis) |
| `LC_DISCOVERY` | `RL_CLASSIFICATION` · `RL_PRODUCT` · `RL_CHARTER` (hypothesis) |
| `LC_PROOF` | `RL_CHARTER` · `RL_IMPLEMENTATION` · `RL_LIFECYCLE` |
| `LC_PILOT` | `RL_OPERATIONS` · `RL_RELEASE` · `RL_VALIDATION` |
| `LC_PRODUCTION` | `RL_OPERATIONS` · `RL_COMPLIANCE` · `RL_RELEASE` |
| `LC_GROWTH` | `RL_EXPANSION` · `RL_ARCHITECTURE` · `RL_COMPLIANCE` |
| `LC_MATURE` | `RL_INVESTMENT` · `RL_OPERATIONS` · `RL_VALIDATION` |
| `LC_LEGACY` | `RL_INVESTMENT` · `RL_SUNSET` (plan) · `RL_OPERATIONS` (minimal) |
| `LC_SUNSET` | `RL_SUNSET` · `RL_DATA_PRIVACY` · `RL_COMPLIANCE` |

---

## 9. Product Class Role Pressure Matrix

Criticality scale: **●** Critical · **◐** Elevated · **○** Standard · **—** Rarely material

Rows = role domains · Columns = 8 focus classes from charter

| Role domain | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `RL_INTAKE` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `RL_PRODUCT` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `RL_CLASSIFICATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `RL_CHARTER` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `RL_UX` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `RL_ARCHITECTURE` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `RL_IMPLEMENTATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `RL_VALIDATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `RL_DATA_PRIVACY` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `RL_COMPLIANCE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `RL_COMMERCIAL` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `RL_TRUST_SAFETY` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `RL_OPERATIONS` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `RL_RELEASE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `RL_ECOSYSTEM` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `RL_LIFECYCLE` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `RL_EXPANSION` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `RL_INVESTMENT` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `RL_SUNSET` | ◐ | ◐ | ○ | ○ | ● | ● | ● | ● |
| `RL_RECOVERY` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |

### 9.1 Class-specific domain amplifications

| Class | Domains disproportionately critical |
|-------|-------------------------------------|
| **`COMMERCE`** | `RL_COMMERCIAL`, `RL_OPERATIONS`, `RL_UX`, `RL_VALIDATION` |
| **`FIELD_OPERATIONS`** | `RL_ARCHITECTURE`, `RL_CHARTER`, `RL_DATA_PRIVACY`, `RL_RECOVERY` |
| **`AI_ASSISTANT`** | `RL_TRUST_SAFETY`, `RL_DATA_PRIVACY`, `RL_COMPLIANCE`, `RL_OPERATIONS` |
| **`UTILITY_TOOL`** | `RL_CHARTER` (anti-creep), `RL_CLASSIFICATION`; most at ○ unless triggers |
| **`MARKETPLACE`** | `RL_TRUST_SAFETY`, `RL_COMMERCIAL`, `RL_ECOSYSTEM`, `RL_VALIDATION` |
| **`HEALTH_MEDICAL`** | `RL_COMPLIANCE`, `RL_DATA_PRIVACY`, `RL_TRUST_SAFETY`, `RL_VALIDATION` |
| **`FINTECH_WALLET`** | `RL_COMPLIANCE`, `RL_COMMERCIAL`, `RL_ARCHITECTURE`, `RL_VALIDATION` |
| **`AI_AGENT_CONSOLE`** | `RL_TRUST_SAFETY`, `RL_COMPLIANCE`, `RL_ARCHITECTURE`, `RL_RECOVERY` |

**Tier modifier (all classes):** T3+ elevates `RL_ARCHITECTURE`, `RL_OPERATIONS`, `RL_VALIDATION` to blocking at Production; T4 elevates nearly all alignment domains to ●.

---

## 10. Role Weight Model

Derived from **coverage radius × accountability depth × downstream blocking power** — not from headcount or seniority.

### 10.1 Weight classes

#### `RW_SUPPORTING`

| Field | Value |
|-------|-------|
| **Impact radius** | Single workflow stream; low external exposure |
| **Responsibility depth** | Light coverage; may share domain with adjacent roles |
| **Downstream influence** | Vacancy causes confusion, not immediate integrity failure |
| **Examples** | `RL_INTAKE` at Concept; hypothesis `RL_PRODUCT` |

---

#### `RW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Multi-artifact; affects product shape |
| **Responsibility depth** | Explicit domain coverage required; prerequisites enforced |
| **Downstream influence** | Vacancy blocks downstream domain claims |
| **Examples** | `RL_CHARTER` in Proof; `RL_ARCHITECTURE` at Proof exit; `RL_ECOSYSTEM` per-deploy |

---

#### `RW_CRITICAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Product-wide; ops/legal/users depend on coverage |
| **Responsibility depth** | Full domain accountability; no implicit coverage |
| **Downstream influence** | Vacancy = integrity failure at current stage |
| **Examples** | `RL_COMPLIANCE` Production; `RL_OPERATIONS` Production; `RL_TRUST_SAFETY` live AI |

---

#### `RW_TERMINAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Irreversible or impractical to undo |
| **Responsibility depth** | Complete domain coverage; paired recovery domain |
| **Downstream influence** | Vacancy before execution may cause permanent harm |
| **Examples** | `RL_SUNSET` decommission; mass deletion path |

### 10.2 Default weight by role domain

| Domain | Default weight | Elevates to `RW_CRITICAL` when |
|--------|----------------|--------------------------------|
| `RL_INTAKE` | `RW_SUPPORTING` | Production product re-intake after kill |
| `RL_PRODUCT` | `RW_STRUCTURAL` | Post-Production identity change |
| `RL_CLASSIFICATION` | `RW_STRUCTURAL` | Extended class or T3+ |
| `RL_CHARTER` | `RW_STRUCTURAL` | Proof/Pilot boundary |
| `RL_UX` | `RW_STRUCTURAL` | Core journey lock at Proof exit |
| `RL_ARCHITECTURE` | `RW_STRUCTURAL` | Production baseline; `RW_CRITICAL` at scale |
| `RL_IMPLEMENTATION` | `RW_STRUCTURAL` | T3+ Production build |
| `RL_VALIDATION` | `RW_STRUCTURAL` | `CW_CRITICAL`+ contracts under test |
| `RL_DATA_PRIVACY` | `RW_STRUCTURAL` | PII; `RW_CRITICAL` regulated |
| `RL_COMPLIANCE` | `RW_CRITICAL` | Extended classes always |
| `RL_COMMERCIAL` | `RW_CRITICAL` | Real money |
| `RL_TRUST_SAFETY` | `RW_CRITICAL` | AI/marketplace live |
| `RL_OPERATIONS` | `RW_CRITICAL` | Production entry |
| `RL_RELEASE` | `RW_STRUCTURAL` | Public wide release |
| `RL_ECOSYSTEM` | `RW_STRUCTURAL` | Deep platform embed; per-deploy ORCA |
| `RL_LIFECYCLE` | `RW_STRUCTURAL` | Production transition claim |
| `RL_EXPANSION` | `RW_CRITICAL` | Geo/compliance expansion |
| `RL_INVESTMENT` | `RW_STRUCTURAL` | Legacy declaration |
| `RL_SUNSET` | `RW_TERMINAL` | Decommission execution |
| `RL_RECOVERY` | `RW_CRITICAL` | Production rollback; regulated product |

---

## 11. Role State Model

Role states describe **coverage posture of responsibility domains**, not staffing assignment, on-call status, or approval outcome. Actor-neutral.

### 11.1 State codes

| State | Code | Meaning |
|-------|------|---------|
| **Latent** | `RS_LATENT` | Workflow exists; domain not yet structurally required |
| **Required** | `RS_REQUIRED` | Active workflow requires domain coverage now |
| **Covered** | `RS_COVERED` | Domain coverage declared; alignment outputs owned |
| **Vacant** | `RS_VACANT` | Required domain has no coverage claim — integrity gap |
| **Constrained** | `RS_CONSTRAINED` | Domain covered but blocked by prerequisite domain vacancy |
| **Overextended** | `RS_OVEREXTENDED` | Single domain claiming coverage beyond its scope |
| **Superseded** | `RS_SUPERSEDED` | Lifecycle/decision/workflow change replaced domain pressure |
| **Dormant** | `RS_DORMANT` | Not applicable at current stage/class |

### 11.2 State transition rules (descriptive)

```text
RS_LATENT ──(workflow WS_ACTIVATED+)──► RS_REQUIRED
RS_REQUIRED ──(coverage declared)──► RS_COVERED
RS_REQUIRED ──(no coverage claim)──► RS_VACANT
RS_VACANT ──(coverage declared)──► RS_COVERED
RS_COVERED ──(prerequisite domain vacant)──► RS_CONSTRAINED
RS_CONSTRAINED ──(prerequisite covered)──► RS_COVERED
RS_COVERED ──(scope creep detected)──► RS_OVEREXTENDED
RS_OVEREXTENDED ──(scope reconciled)──► RS_COVERED
RS_* ──(lifecycle/workflow change)──► RS_SUPERSEDED
RS_* ──(stage/class makes irrelevant)──► RS_DORMANT
```

### 11.3 Deliberate exclusions

| Rejected state | Reason | Correct layer |
|----------------|--------|---------------|
| **assigned** | Person binding | Staffing |
| **on_call** | Rotation schedule | Staffing + Tools |
| **approved** | Authority act | Approvals |
| **filled_by_agent** | Execution actor | Agent Cards |
| **vacant_headcount** | HR concept | Staffing |

### 11.4 Covered vs fake coverage

**`RS_COVERED` requires:**

1. Named `source_workflow_type_code`
2. Stated coverage depth matching workflow V-target
3. Lifecycle context where coverage is claimed
4. No unresolved `RS_VACANT` on prerequisite domains at `RW_STRUCTURAL`+

**Not sufficient for `RS_COVERED`:** job title exists; team named; agent card created; RACI row filled.

---

## 12. Role Failure Patterns

Derived from Workflow Failure Patterns §11, Website Factory drift, ORCA battle, MARS survivability — reframed as **responsibility domain failures**, not people failures.

| Pattern | Signal | Root role failure | Affected domains |
|---------|--------|-------------------|------------------|
| **Responsibility vacuum** | Active workflow; no domain claims coverage | Workflow → role mapping missing | Any — `RS_VACANT` |
| **Workflow without owner domain** | `WS_IN_PROGRESS`; all domains `RS_LATENT` | Activation without coverage requirement | Same as workflow |
| **Overlapping ownership** | Two domains claim same workflow coverage | Duplicate domain claims | Same `role_type_code` pair |
| **Role inflation** | Domain claims coverage for dormant workflow | Domain without workflow source | Alignment domains on utility T1 |
| **Authority without obligation** | Approver exists; no contract/workflow trace | Approval confused with domain | Approvals — not role |
| **Person-first modeling** | Job title treated as domain | Staffing substituted for role reality | Any |
| **Org-chart thinking** | Department owns «everything ops» | Department ≠ `RL_OPERATIONS` | Operational domains |
| **Handoff domain absent** | Delivery complete; `RL_OPERATIONS` vacant | Factory handoff-collapse analog | `RL_OPERATIONS` |
| **Sync domain once-only** | URL drift; `RL_ECOSYSTEM` dormant after deploy | Per-deploy coverage not re-required | `RL_ECOSYSTEM` — ORCA |
| **Validation domain bypass** | Ship without `RL_VALIDATION` covered | Verification coverage skipped | `RL_VALIDATION`, all alignment |
| **Implementation without charter domain** | `RL_IMPLEMENTATION` covered; `RL_CHARTER` vacant | Prerequisite domain violation | `RL_IMPLEMENTATION`, `RL_CHARTER` |
| **Recovery domain absent** | Production incident; `RL_RECOVERY` latent | Corrective domain not activated | `RL_RECOVERY` |
| **Lifecycle domain bypass** | Store live; `RL_LIFECYCLE` vacant | Release substituted for transition domain | `RL_RELEASE`, `RL_LIFECYCLE` |
| **Commercial domain jump** | First payment; `RL_COMMERCIAL` never covered in Pilot | Sequencing error | `RL_COMMERCIAL` |
| **Semantic/deployed split** | Ads against intent not product | `RL_PRODUCT` vs `RL_ECOSYSTEM` desync | `RL_PRODUCT`, `RL_ECOSYSTEM` |
| **Agent card before domain** | Agent assigned; no `role_type_code` | Agent Cards before Role Reality | Agents — premature |
| **Tool operator as domain** | «Jira admin owns QA» | Tool ≠ responsibility domain | Tools — premature |
| **Fake coverage** | `RS_COVERED` with no workflow alignment | Coverage theater | Any at `RW_CRITICAL`+ |

---

## 13. Role Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-R1** | Every active `workflow_type_code` at `WS_ACTIVATED`+ must have covered `role_type_code` or mark SAFE UNKNOWN | Workflow without owner domain |
| **AC-R2** | No `RL_IMPLEMENTATION` at `RW_STRUCTURAL`+ before `RL_CHARTER` reaches `RS_COVERED` | Build without boundary domain |
| **AC-R3** | Extended class: `RL_COMPLIANCE` and `RL_TRUST_SAFETY` cannot stay `RS_LATENT` past `LC_DISCOVERY` when workflows active | Compliance domain vacuum |
| **AC-R4** | Production claim requires `RL_LIFECYCLE`, `RL_OPERATIONS`, `RL_COMPLIANCE` covered — not inferred from release | Release = stage domain confusion |
| **AC-R5** | Same `role_type_code` at `RW_STRUCTURAL`+ requires lifecycle or tier trigger to re-activate from `RS_SUPERSEDED` | Domain churn |
| **AC-R6** | Job titles cannot substitute for domains — name `role_type_code` and `source_workflow_type_code` | People-first modeling |
| **AC-R7** | `RL_CHARTER` must reach `RS_COVERED` before `LC_PROOF` build domain claim | Charter domain inflation |
| **AC-R8** | `RW_CRITICAL`+ domains must declare coverage depth before `RS_COVERED` claim | Fake coverage |
| **AC-R9** | Pilot with real users requires `RL_OPERATIONS` at lite minimum `RS_REQUIRED` | Pilot ops domain gap |
| **AC-R10** | `RL_PRODUCT` pivot requires `RL_LIFECYCLE` domain review | Random pivot without transition domain |
| **AC-R11** | One role domain per workflow activation — no mega-domains bundling unrelated workflows | Role inflation |
| **AC-R12** | `RL_CLASSIFICATION` re-required on tier bump or payments/PII/regulated feature | Classification domain drift |
| **AC-R13** | Undocumented `RW_CRITICAL`+ domain at `RS_REQUIRED` = SAFE UNKNOWN in REPORT | Silent critical vacancy |
| **AC-R14** | `UTILITY_TOOL` T1 exempt from commercial/compliance domains until trigger feature | Over-engineering domains |
| **AC-R15** | Store/public release requires `RL_RELEASE` + often `RL_LIFECYCLE` covered | AC-W4 lifecycle analog |
| **AC-R16** | Team/department name alone cannot satisfy domain — explicit `role_type_code` coverage | Org-chart thinking |
| **AC-R17** | Every active `role_type_code` must trace to `source_workflow_type_code` | Responsibility without workflow |
| **AC-R18** | Duplicate domain claims for same workflow require reconciliation to single coverage instance | Overlapping ownership |
| **AC-R19** | High-risk lifecycle transitions require `RL_RECOVERY` domain covered (snapshot/rollback) | Recovery domain absent |
| **AC-R20** | `RL_ECOSYSTEM` must re-enter `RS_REQUIRED` on each external deploy when `WF_ECOSYSTEM_SYNC` active | One-time sync (ORCA) |
| **AC-R21** | No Agent Card may reference domain not in role registry | Agent Cards before Role Reality |
| **AC-R22** | No tool may be labeled as owning a domain — tools assist occupants | Tool-as-domain confusion |

---

## 14. Role Relationships

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
│  Role Reality Model v1      ──► role_type_code         ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ responsibility domains ready for tool/agent assignment
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    TOOLS (future)                            │
│  Helpers per workflow/role domain                            │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    AGENTS (future)                            │
│  Scoped execution within role domains — if proven            │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
                         Automation (future)
```

### 14.2 Why roles are derived from workflows

| Input | Provides | Without it |
|-------|----------|------------|
| **`workflow_type_code`** | Which work structure exists | Random domain labels |
| **`workflow_state_code`** | Whether coverage is required now | Domains always «someone's job» |
| **`effective_weight_class`** | How deep coverage must go | Seniority substitutes for domain depth |
| **`source_contract_type_code`** | Upstream obligation trace | Domains without obligation context |
| **`role_type_code`** | The actual responsibility domain | Staffing assigns meaningless titles |

**Combined pressure function (conceptual, not algorithm):**

```text
role_pressure(role_type_code, product_class_code, lifecycle_state_code, source_workflow_type_code, tier)
  → dominance_posture ∈ { dormant, latent, required, dominant, blocking }
  → effective_weight_class
  → role_state_code
  → coverage_depth_expectation
```

**Examples:**

| Context | Pressure outcome |
|---------|------------------|
| `RL_COMMERCIAL` + `UTILITY_TOOL` + `LC_PROOF` + T1 | `RS_DORMANT` unless monetization workflow active |
| `RL_COMMERCIAL` + `COMMERCE` + `LC_PILOT` + T3 | `DP_DOMINANT`; `RW_CRITICAL` |
| `RL_ARCHITECTURE` + `AI_AGENT_CONSOLE` + `LC_DISCOVERY` + T4 | `RS_REQUIRED`; spike depth only |
| `RL_SUNSET` + `HEALTH_MEDICAL` + `LC_SUNSET` + T4 | `DP_BLOCKING`; `RW_TERMINAL` |

### 14.3 Cross-layer binding (conceptual instance)

```text
nova_role_context {
  product_class_code,           // registry
  complexity_tier,              // registry / intake
  lifecycle_state_code,         // lifecycle
  contract_type_code,           // upstream obligation
  workflow_type_code,           // source workflow
  role_type_code,               // responsibility domain
  effective_weight_class,       // RW_*
  role_state_code,              // RS_*
  coverage_depth_expectation    // from workflow V-target
}
```

### 14.4 Cross-domain dependencies (reality, not staffing)

| Upstream domain | Downstream domains constrained |
|-----------------|--------------------------------|
| `RL_INTAKE` | All — context anchor |
| `RL_CLASSIFICATION` | All alignment domains — depth selection |
| `RL_CHARTER` | `RL_IMPLEMENTATION`, `RL_VALIDATION` scope |
| `RL_ARCHITECTURE` | `RL_IMPLEMENTATION`, `RL_EXPANSION` |
| `RL_PRODUCT` | `RL_UX`, `RL_CHARTER`, `RL_ECOSYSTEM` |
| `RL_*` alignment | `RL_VALIDATION` at contract V-level |
| `RL_LIFECYCLE` | Re-evaluates all dominant domains at new stage |
| `RL_RECOVERY` | May reset misaligned domains to `RS_REQUIRED` |

### 14.5 Why roles precede Tools and Agents

| Dimension | Role Reality | Tools / Agents (future) |
|-----------|--------------|-------------------------|
| **Question** | What responsibility domains must exist? | What helps occupy or execute within domains? |
| **Binding** | `{ class × lifecycle × contract × workflow }` | Domain-scoped helpers and actors |
| **Example** | `RL_VALIDATION` must be covered at Production | Diff validator tool; QA agent card |
| **Rule** | Tool/agent without domain = attachment to noise | AC-R21; AC-R22 |

---

## 15. Role Reality Boundaries

### 15.1 What is NOT a role (in this layer)

| Not a role | Why | Correct layer |
|------------|-----|---------------|
| **Employee** | Person | Staffing |
| **Manager** | People hierarchy | Staffing / Org |
| **Team** | Group of people | Staffing |
| **Department** | Org structure | Explicitly forbidden |
| **Job title** | HR label | Staffing — may occupy domain later |
| **Agent** | Execution actor | Agent Cards (future) |
| **Tool** | Helper | Tools (future) |
| **Approver** | Authority act | Approvals (future) |
| **Sponsor** | Portfolio person | May occupy `RL_INTAKE`; not domain |
| **RACI matrix** | Assignment format | Staffing — uses role codes |
| **On-call rotation** | Schedule | Staffing + Tools |
| **Workflow** | Work structure | Workflow Reality — upstream |
| **Contract** | Obligation | Contract Reality — upstream |
| **Approval gate** | Enforcement outcome | Future gate layer |
| **Agent Card** | Agent specification | Agents — requires Role Reality first |

### 15.2 Boundary tests

Apply before labeling something a role domain:

1. **Workflow-origin test:** Does this domain trace to named `workflow_type_code`(s)?
2. **Actor-neutrality test:** Is domain meaningful with zero named people and zero agents?
3. **Coverage test:** Does absence leave active workflow without accountability surface?
4. **Non-person test:** Is it defined without reference to job title, team, or department?

**Pass all four** → role domain applies. **Fail any** → likely staffing, tool, agent, or approval artifact.

### 15.3 Common misuse prevention

| Misuse | Correction |
|--------|------------|
| «PM = product role» | PM is job title; domain is `RL_PRODUCT` |
| «Dev team owns build» | Team is staffing; domain is `RL_IMPLEMENTATION` |
| «Legal owns compliance» | Department is org; domain is `RL_COMPLIANCE` |
| «Agent X is QA role» | Agent executes; domain is `RL_VALIDATION` |
| «Jira project = ops domain» | Tool tracks work; domain is `RL_OPERATIONS` |
| «RACI R = role in NOVA» | RACI letter is assignment; `role_type_code` is domain |

### 15.4 Layer leakage prevention

| Leakage direction | Block |
|-------------------|-------|
| Role → Staffing | No assignee fields in v1 object model |
| Role → Agent Cards | No agent_ref in v1; AC-R21 |
| Role → Tools | No tool ownership; AC-R22 |
| Role → Approvals | No approval authority codes |
| Role → Workflow | Roles cover workflows; do not redefine work structure |
| Role → Contracts | Roles trace to contracts via workflows; do not invent obligations |

---

## 16. RBM Mapping

```text
Reality
├── Production Model v1        … what NOVA is
├── Product Taxonomy v1        … what classes exist
├── Product Class Registry v1  … what each class means operationally
├── Lifecycle Model v1         … where the product is in life
├── Decision Reality Model v1  … what decisions exist in product nature
├── Contract Reality Model v1  … what obligations exist because of decisions
├── Workflow Reality Model v1  … how obligations become structured work
└── Role Reality Model v1      … what responsibility domains exist because workflows exist  ◄── HERE
        │
        ▼
Tools                          … helpers scoped to domains (future)
        │
        ▼
Agents                         … only if proven necessary (future)
        │
        ▼
Automation                     … last, if ever (future)
```

### 16.1 Why Roles come after Workflow and before Tools

| Order | Reason |
|-------|--------|
| **Reality before Lifecycle** | Must know product identity before domain depth |
| **Lifecycle before Decisions** | Stage determines active choice domains |
| **Decisions before Contracts** | Obligations crystallize from choices |
| **Contracts before Workflow** | Work structures honor known obligations |
| **Workflow before Roles** | Responsibility domains derive from work structure — not org chart |
| **Roles before Tools** | Tools assist domain occupants — not define domains |
| **Roles before Agents** | Agents occupy domains — not invent them |
| **Roles before Automation** | Automate within covered domains — not guess responsibility |

**Completion of Role Reality band (vocabulary only):** After this artifact, NOVA knows **identity**, **time**, **choice structure**, **commitment structure**, **work structure**, and **responsibility domain structure**. Downstream layers can attach `{ product_class × lifecycle × contract × workflow × role }` instead of improvising org charts.

**Explicitly NOT in Role band:** staffing records, org charts, job titles, agent cards, tool catalog, approval chains, RACI automation, runtime assignment.

### 16.2 Why Agent Cards cannot exist before Role Reality

Agent Cards answer **«какой агент в каком domain может действовать?»** — meaningless without:

- `workflow_type_code` — what work structure exists
- `role_type_code` — what responsibility domain must be covered
- `role_state_code` — whether domain requires occupancy
- `effective_weight_class` — how deep agent scope may go

Creating Agent Cards before Role Reality produces **agents attached to tasks**, not **agents scoped to responsibility domains** — the ORCA/Factory pattern of automation without survivability coverage repeats at agent layer.

**Agent Cards will consume from Role Reality:**

- domain scope per `role_type_code`
- coverage boundaries when `RS_COVERED` vs `RS_VACANT`
- escalation to human when domain is `RW_CRITICAL`+ and vacant

**Not designed here.**

### 16.3 Downstream layers (future — not designed here)

| Layer | Will consume from Role Reality |
|-------|-------------------------------|
| **Tools** | Helpers per `role_type_code` / `workflow_type_code` pair |
| **Agents** | Agent Cards scoped to domains — if proven |
| **Automation** | Repeatable checks within covered domains after human proof |
| **Staffing** (explicitly out of NOVA Role v1 scope) | Humans/teams occupying domains |

---

## 17. Risks

| Risk | Severity | Mitigation in v1 |
|------|----------|------------------|
| Role Reality confused with org chart / RACI | High | Scope boundary; §2.4; §15; AC-R6, AC-R16 |
| Role Reality confused with Agent Cards | High | §16.2; AC-R21 |
| Role inflation (too many domains) | Medium | 18 domains with rejection table §3.1; AC-R11 |
| Person-first modeling despite rules | High | Boundary tests §15.2; AC-R6 |
| Domain confused with job title | High | §15.3; `is_job_title` always false |
| Lifecycle-domain conflation | High | Separate codes; AC-R4; matrix §8 |
| Class matrix oversimplification | Medium | Tier modifier §9.1; SAFE UNKNOWN |
| Silent critical vacancy | High | AC-R13; failure patterns §12 |
| Workflow-role 1:1 oversimplification | Medium | Secondary activations §6.2; `RL_VALIDATION` cross-cutting |
| Governance expansion drift | Medium | No Staffing/Agents/Tools in v1; RBM §16 |
| Prior foundation files not all in-repo | Medium | Cross-reference existing docs |
| Human enforcement fatigue | Medium | 22 anti-chaos rules; not automation pretense |
| Fake `RS_COVERED` at scale | High | Coverage binding §11.4; AC-R8 |
| Tool labeled as domain owner | Medium | AC-R22; §15.1 |

---

## 18. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Exact mapping role weight → staffing seniority | First NOVA Staffing charter (explicitly out of v1) |
| Whether `RL_ECOSYSTEM` splits intent vs deployed occupants in v2 | First ORCA-style dual-domain product through NOVA |
| Machine format for `role_pressure_instance` | Future intake schema |
| Optimal count of role domains (18 vs consolidated) | Operator feedback after 2–3 products |
| Prior Production Model / Taxonomy / Registry markdown in-repo | Human commit of foundation pack |
| Role Records vs Staffing Records layer split | Future charter after Tools design |
| Whether `RS_VACANT` triggers mandatory escalation path | First Production incident through NOVA roles |
| Multi-occupant rules (human + agent same domain) | First Agent Cards charter |
| Overlap with MARS survivability protected zones | NOVA ↔ MARS integration charter |
| AI agent domain boundaries beyond trust/safety/implementation | First `AI_AGENT_CONSOLE` production pilot |
| RACI integration semantics | Future Staffing charter — not Role Reality |

**Non-claims preserved:** this model does not assert staffing system, org chart, job catalog, agent cards, tool ownership, approval automation, role assignment runtime, or automated vacancy detection.

---

## 19. Recommended Next Step

**Single next artifact:** `NOVA TOOL REALITY MODEL v1` (or phased Tools charter) — first layer **after** Role Reality, defining:

- helper taxonomy scoped to `role_type_code × workflow_type_code`
- explicit separation from Agent Cards and Staffing
- tool boundary rules preventing tool-as-domain confusion

**Do not skip to:** Agent Cards, Staffing Records, Org Structure, Approval Systems, Role Assignment automation, Runtime, or Automation until Tools charter approved — or human explicitly charters a different next layer.

**Optional parallel (human choice):** commit full NOVA foundation pack to `projects/nova/foundation/` including this file.

**Prior artifact update (optional):** Workflow Reality Model §18 Recommended Next Step — mark Role Reality as complete; point to Tools as next.

---

## Appendix A — Role Pressure Snapshot template

```markdown
# Role Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| role_type_code | dominance_posture | effective_weight | role_state | source_workflow | coverage_depth |
|----------------|---------------------|------------------|------------|-----------------|----------------|
| RL_INTAKE      |                     |                  |            |                 |                |
| ...            |                     |                  |            |                 |                |

Dominant domains this stage:
Vacant domains (RS_VACANT):
Overextended domains (RS_OVEREXTENDED):
SAFE UNKNOWN domains:
```

---

## Appendix B — RBM layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | Decision Reality Model v1 | Complete |
| Contracts | Contract Reality Model v1 | Complete |
| Workflow | Workflow Reality Model v1 | Complete |
| **Roles** | **Role Reality Model v1** | **This document — vocabulary complete** |
| Tools | — | Not started (recommended next) |
| Agents | — | Not started |
| Automation | — | Not started |

---

**Document status:** v1 design complete — responsibility domain vocabulary for NOVA mobile products. Nothing beyond Role Reality.
