# NOVA Decision Reality Model v1

**Status:** design-only — Reality-layer decision vocabulary, not workflow, not decision engine, not governance system, not decision record storage  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → **this document**  
**Non-claims:** no agents, no orchestration, no automated decision enforcement, no ADR database, no approval gates, no database schema

**Parent Reality artifacts (conceptually approved; prior design sessions):**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`

**Evidence base:** Website Factory production-drift and site-type classification lessons; ORCA semantic-vs-deployed-copy and human-authority gates; MARS survivability freeze/rollback discipline; ADR concepts adapted as decision reality (not ADR tooling)

---

## 1. Executive Summary

NOVA Decision Reality Model v1 — **первый decision artifact NOVA**. Он отвечает на вопрос:

> **«Какие решения существуют в реальности мобильного продукта?»**

Не «как принимать решения» (Workflow), не «кто утверждает» (Roles), не «как фиксировать» (Decision Records — future), не «когда блокировать» (Gates — future Contracts layer).

| Элемент | Содержание |
|---------|------------|
| **17 decision families** | `DEC_EXISTENCE` … `DEC_SUNSET` — derived taxonomy |
| **Canonical decision object** | `decision_type_code` + required reality fields |
| **Decision registry** | 17 rows with definition, appearance, consequences, reversibility |
| **Lifecycle pressure matrix** | Dominant families per `LC_*` stage |
| **Product class pressure matrix** | 8 focus classes × decision criticality |
| **Weight model** | 5 classes: `DW_NEGLIGIBLE` → `DW_IRREVERSIBLE` |
| **Reversibility model** | 5 classes: `REV_INSTANT` → `REV_TERMINAL` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Decision Reality (this doc) | Decision Workflow (NOT this) |
|-----------|----------------------------|------------------------------|
| **Question** | What kinds of decisions exist? | How and when are they made? |
| **Layer** | Reality → Decisions | Workflow / execution machinery (future) |
| **Example** | `DEC_ARCHITECTURE` exists at Proof exit | Architecture review meeting cadence |
| **Output** | Vocabulary + pressure maps | Templates, gates, records, automation |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answers:** «What decisions are structurally part of this product's existence?» (`decision_type_code`)

Without decision reality, contracts become generic checklists, workflows invent decisions ad hoc, and critical commitments hide inside tasks and tickets.

---

## 2. Decision Philosophy

### 2.1 Why decisions exist

Mobile products **не существуют без выбора**. Даже «мы ничего не решили» — решение отложить. В реальности продукта постоянно присутствуют **структурные развилки**:

- **Existence:** строить ли, продолжать ли, убивать ли
- **Identity:** что это за продукт и для кого
- **Commitment:** какие технические, legal и operational обязательства принимаются
- **Transition:** когда продукт меняет фазу жизни
- **Exit:** как продукт завершает существование

Decisions — **не задачи**. Задача «написать экран оплаты» исполняет уже принятое commercial решение. Decision Reality фиксирует **классы выбора**, которые **должны произойти** до того, как execution имеет смысл.

**Website Factory lesson:** drift начинается, когда **classification** (`site_type_code`) не зафиксирован, и команда строит «универсальный сайт» ([`SITE-TYPE-IMPLEMENTATION-RULES-v1.md`](../../workspaces/website-factory-reference-v1/registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md)). Аналог в NOVA: без `DEC_CLASSIFICATION` и `DEC_SCOPE` execution раздувается.

**ORCA lesson:** semantic pack ≠ deployed copy — это **не баг**, а **два разных decision domains** (intent vs deployed truth). Смешение domain'ов порождает PPC export против неверной landing reality ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

### 2.2 Why RBM requires decisions before contracts

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | What it fixes | Without prior layer |
|-------|---------------|---------------------|
| **Reality** | What exists (class, lifecycle vocabulary) | Random product labels |
| **Lifecycle** | Where in life (temporal pressure) | Same contract depth everywhere |
| **Decisions** | What choices structurally exist | Contracts invent obligations without context |
| **Contracts** | What must be true after choices | Workflow executes uncommitted assumptions |

**Contracts без Decision Reality** описывают *шаблоны обязательств*, не зная *какие обязательства вообще применимы*:

- `LC_CONCEPT` не нуждается в production legal pack — нуждается в `DEC_EXISTENCE`
- `HEALTH_MEDICAL` + `LC_PILOT` требует `DEC_TRUST_SAFETY` и `DEC_COMPLIANCE` до QA contract depth
- `UTILITY_TOOL` T1 может never need `DEC_COMMERCIAL` — contract templates must not assume payments

Decisions **не исполняются** — они **определяют пространство выбора**. Contracts **кристаллизуют** уже осознанные decision domains в enforceable obligations (future layer).

### 2.3 Relationship to lifecycle

| Lifecycle | Decision Reality |
|-----------|------------------|
| Describes **state** of product in world | Describes **choice domains** active in that state |
| `lifecycle_state_code` changes over time | Same `decision_type_code` may appear at multiple stages with different weight |
| Transition requires evidence (future workflow) | Transition **is** a decision family (`DEC_LIFECYCLE_TRANSITION`) |
| Pressure map (Lifecycle §8) | Expanded into full taxonomy + matrices in this doc |

**Interaction examples:**

| Stage | Lifecycle says | Decision Reality adds |
|-------|----------------|----------------------|
| `LC_CONCEPT` | Very high uncertainty; no QA | `DEC_EXISTENCE` dominant; `DEC_ARCHITECTURE` usually premature |
| `LC_PROOF` | Core hypothesis testing | `DEC_SCOPE` boundary critical; `DEC_ARCHITECTURE` selective |
| `LC_PILOT` | Controlled real-world learning | `DEC_OPERATIONS`, `DEC_RELEASE_DISTRIBUTION` become real |
| `LC_PRODUCTION` | Operational baseline | `DEC_COMPLIANCE`, `DEC_OPERATIONS` at commitment weight |
| `LC_SUNSET` | Terminal | `DEC_SUNSET`, `DEC_DATA_PRIVACY` (retention) dominant |

Lifecycle **не заменяет** decisions: продукт может быть в `LC_PILOT` и одновременно нуждаться в `DEC_ARCHITECTURE` (pivot) и `DEC_LIFECYCLE_TRANSITION` (advance/hold).

### 2.4 Relationship to registry

| Registry | Decision Reality |
|----------|------------------|
| `product_class_code` — stable identity | Class **amplifies** which decision families matter |
| `critical_lifecycle_areas` — class-specific pressure zones | Maps to decision family criticality per class |
| `qa_priorities`, `release_priorities` | **Consequences** of decisions, not decisions themselves |
| `common_failure_patterns` | Inform decision failure patterns (§10) |
| `default_tier` (T1–T4) | Modulates decision weight and evidence expectations |

**Binding logic (conceptual instance, not storage):**

```text
decision_pressure_context {
  product_class_code,      // from registry
  complexity_tier,         // from registry / intake
  lifecycle_state_code,    // from lifecycle
  modifiers[]              // hybrid class, companion, regulated overlay
}
```

Same `DEC_COMPLIANCE` decision type exists for all classes; **weight and evidence** differ: negligible for `UTILITY_TOOL` T1 offline, `DW_COMMITMENT` for `FINTECH_WALLET` T4.

### 2.5 Why Decision Reality is a distinct layer

Decision Reality is **not** a subset of Lifecycle because:

1. **Many decisions are not lifecycle transitions** — architecture, UX model, data retention policy persist across stages
2. **Same stage, different decision pressure by class** — `LC_DISCOVERY` for `AI_ASSISTANT` vs `UTILITY_TOOL` shares stage code, not decision set
3. **Decisions precede contract crystallization** — lifecycle tells *when* pressure peaks; decision taxonomy tells *what* is being pressured
4. **Anti-confusion with execution** — tasks, sprints, P-phases are not decisions (see §13)

Decision Reality is **not** Workflow because it describes **what choices exist in product nature**, not **how teams process them**.

Decision Reality is **not** Governance because it does **not** assign authority, approval chains, or enforcement — only **vocabulary of structural choice**.

---

## 3. Decision Taxonomy

### 3.1 Derivation rationale

Test for each candidate family: *«Does NOVA treat evidence, contracts, and ops differently if this choice is unmade or wrongly made?»*

**Rejected as standalone decision families:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Feature** | Implementation scope inside product boundary | → `DEC_SCOPE` + execution tasks |
| **Bug fix approach** | Tactical execution | → Not a decision (§13) |
| **Sprint commitment** | Team scheduling | → Workflow (future) |
| **Ticket priority** | Work queue | → Not a decision |
| **Code review outcome** | Quality gate on execution | → Contract/Workflow (future) |
| **ADR** (as family) | Record format for architecture decisions | → `DEC_ARCHITECTURE` is the reality; ADR is future record pattern |
| **Approval** | Authority action | → Roles + Workflow (future) |

### 3.2 Decision families overview

```text
Portfolio layer:     DEC_EXISTENCE · DEC_INVESTMENT
Identity layer:      DEC_PRODUCT · DEC_CLASSIFICATION · DEC_AUDIENCE
Boundary layer:      DEC_SCOPE · DEC_UX
Commitment layer:    DEC_ARCHITECTURE · DEC_DATA_PRIVACY · DEC_COMPLIANCE
                     DEC_COMMERCIAL · DEC_TRUST_SAFETY
Operational layer:   DEC_OPERATIONS · DEC_RELEASE_DISTRIBUTION
Temporal layer:      DEC_LIFECYCLE_TRANSITION · DEC_EXPANSION · DEC_ECOSYSTEM · DEC_SUNSET
```

### 3.3 Family definitions

#### `DEC_EXISTENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Determine whether product attention, resources, and NOVA track are warranted |
| **Scope** | Portfolio / product line / single product instance |
| **Lifecycle relevance** | Dominant `LC_CONCEPT`; persists as undercurrent through `LC_HOLD`, kill paths |
| **Risk level** | High when wrong continue; High when wrong kill (opportunity cost) |

---

#### `DEC_PRODUCT`

| Field | Value |
|-------|-------|
| **Purpose** | Define what the product **is** — value hypothesis, core job, differentiation |
| **Scope** | Product identity; survives class rebinding with revision |
| **Lifecycle relevance** | `LC_CONCEPT`–`LC_DISCOVERY`; revisited at pivot (`LC_PROOF`→`LC_DISCOVERY`) and `DEC_EXPANSION` |
| **Risk level** | High early; Medium after Production if stable |

---

#### `DEC_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **Purpose** | Bind `product_class_code`, `complexity_tier`, modifiers to product instance |
| **Scope** | NOVA operational identity; drives registry defaults |
| **Lifecycle relevance** | Mandatory before `LC_PROOF`; re-triggered on tier bump or hybrid reclassification |
| **Risk level** | High — misclassification cascades to wrong contracts and QA depth |

---

#### `DEC_AUDIENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Choose target users, contexts of use, acquisition/distribution strategy |
| **Scope** | Market and deployment audience; distinct from UX detail |
| **Lifecycle relevance** | `LC_DISCOVERY`–`LC_PILOT`; expansion revisits in `LC_GROWTH` |
| **Risk level** | Medium–High in consumer; Medium in internal/MDM |

---

#### `DEC_SCOPE`

| Field | Value |
|-------|-------|
| **Purpose** | Draw boundary of what is **in** and **out** for current lifecycle phase |
| **Scope** | Phase-specific: proof scope, pilot scope, growth charter scope |
| **Lifecycle relevance** | Critical at `LC_PROOF`, `LC_PILOT`, `LC_GROWTH`; anti-pattern if absent in Concept |
| **Risk level** | High when inflated (perpetual proof); Medium when too narrow (false kill) |

---

#### `DEC_UX`

| Field | Value |
|-------|-------|
| **Purpose** | Commit to interaction model, journey architecture, accessibility posture |
| **Scope** | Cross-screen patterns; not individual screen polish |
| **Lifecycle relevance** | `LC_DISCOVERY` (model) → `LC_PROOF` (core journey) → stable with incremental change |
| **Risk level** | Medium early; High after Production if core journey rework |

---

#### `DEC_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Commit to technical structure — platform, modules, integration style, offline/sync strategy |
| **Scope** | System shape; ADR-worthy commitments without mandating ADR storage |
| **Lifecycle relevance** | Pressure rises `LC_DISCOVERY`→`LC_PROOF` exit; `LC_GROWTH` strain |
| **Risk level** | High — too early wastes; too late causes production incidents |

---

#### `DEC_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **Purpose** | Decide what data is collected, stored, retained, exported, deleted |
| **Scope** | Data categories, residency, minimization, user rights |
| **Lifecycle relevance** | Declared `LC_DISCOVERY`; binding before `LC_PILOT` if PII; sunset retention at `LC_SUNSET` |
| **Risk level** | Low without PII; Critical with health/finance/children data |

---

#### `DEC_COMPLIANCE`

| Field | Value |
|-------|-------|
| **Purpose** | Determine regulatory, store-policy, and legal posture applicable to product |
| **Scope** | Jurisdiction, consent model, medical/finance claims, store categories |
| **Lifecycle relevance** | Hypothesis `LC_DISCOVERY`; baseline before `LC_PRODUCTION`; expansion per geo in `LC_GROWTH` |
| **Risk level** | Class-dependent: Critical for Extended classes |

---

#### `DEC_COMMERCIAL`

| Field | Value |
|-------|-------|
| **Purpose** | Monetization model — pricing, payments, refunds, subscriptions, marketplace take rate |
| **Scope** | Revenue and payment mechanics |
| **Lifecycle relevance** | `LC_DISCOVERY` for model; `LC_PROOF` happy path; `LC_PILOT` real money |
| **Risk level** | Critical for `COMMERCE`, `MARKETPLACE`, `FINTECH_WALLET` |

---

#### `DEC_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **Purpose** | Safety boundaries — AI output limits, abuse prevention, escalation, human-in-loop |
| **Scope** | User harm, fraud, autonomy limits, content policy |
| **Lifecycle relevance** | Early for `AI_ASSISTANT`, `AI_AGENT_CONSOLE`, `MARKETPLACE`; pilot proof mandatory |
| **Risk level** | Critical for AI and multi-sided trust; Medium elsewhere |

---

#### `DEC_OPERATIONS`

| Field | Value |
|-------|-------|
| **Purpose** | Operational model — support, monitoring, incident response, survivability, handoff |
| **Scope** | How product is kept alive in production |
| **Lifecycle relevance** | Lite at `LC_PILOT`; full commitment at `LC_PRODUCTION` entry |
| **Risk level** | High at Production transition; Medium in Mature |

---

#### `DEC_RELEASE_DISTRIBUTION`

| Field | Value |
|-------|-------|
| **Purpose** | Distribution and rollout **posture** — channels, staged rollout, MDM vs store, geo phasing |
| **Scope** | Strategy; individual release events are execution |
| **Lifecycle relevance** | None until `LC_PROOF` internal; controlled at `LC_PILOT`; governed at `LC_PRODUCTION`+ |
| **Risk level** | Medium–High when public; Low internal-only |

---

#### `DEC_LIFECYCLE_TRANSITION`

| Field | Value |
|-------|-------|
| **Purpose** | Advance, hold, regress, or kill across `lifecycle_state_code` |
| **Scope** | Stage transitions per Lifecycle Model v1 |
| **Lifecycle relevance** | At every stage boundary; `LC_HOLD` overlay |
| **Risk level** | High on forward skip; Medium on justified regression |

---

#### `DEC_EXPANSION`

| Field | Value |
|-------|-------|
| **Purpose** | What to expand — features, segments, geographies, monetization depth |
| **Scope** | Growth charter content; distinct from scope creep inside current stage |
| **Lifecycle relevance** | Dominant `LC_GROWTH`; entry decision from `LC_PRODUCTION` |
| **Risk level** | High — feature/geo explosion without charter |

---

#### `DEC_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **Purpose** | Coupling to parent products, third-party APIs, platform dependencies, companion parity |
| **Scope** | External system boundaries and sync semantics |
| **Lifecycle relevance** | `LC_DISCOVERY` for `COMPANION`; ongoing at Production for integrations |
| **Risk level** | High for companion drift; Medium for optional integrations |

---

#### `DEC_INVESTMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Resource and attention allocation — build vs maintain vs harvest |
| **Scope** | Portfolio and team capacity; not sprint planning |
| **Lifecycle relevance** | `LC_MATURE` (refresh vs harvest); `LC_LEGACY` entry |
| **Risk level** | Medium — neglect masked as stability |

---

#### `DEC_SUNSET`

| Field | Value |
|-------|-------|
| **Purpose** | End-of-life path — timeline, migration, data export, store removal |
| **Scope** | Terminal product decisions |
| **Lifecycle relevance** | `LC_LEGACY`→`LC_SUNSET`; execution throughout `LC_SUNSET` |
| **Risk level** | Critical — abrupt exit, data loss, regulatory retention breach |

---

## 4. Decision Object Model

Canonical decision object describes **a decision type in context**, not a stored record. Parallel to `product_class_code` and `lifecycle_state_code`.

### 4.1 Core identifier

**`decision_type_code`** — immutable registry key; one of 17 family codes in §3.

### 4.2 Required fields (reality model)

```text
decision_reality_object {
  // Identity
  decision_type_code          // required — e.g. DEC_ARCHITECTURE
  decision_family_layer       // required — portfolio | identity | boundary | commitment | operational | temporal

  // Definition
  decision_subject            // required — short noun phrase: what is being chosen
  decision_question           // required — canonical question form (not workflow prompt)

  // Context binding (conceptual — not storage)
  lifecycle_state_codes[]     // required — stages where this decision type is structurally active
  product_class_affinity[]    // required — classes where criticality elevates (may be ALL)
  tier_modifier_notes         // required — how T1–T4 shifts weight/evidence

  // Classification
  default_weight_class        // required — DW_* (see §8)
  default_reversibility_class // required — REV_* (see §9)

  // Consequence model (descriptive only)
  typical_stakeholders[]      // required — who is affected (roles named conceptually, not assigned)
  typical_downstream_domains[] // required — which future contract domains consume this
  typical_failure_signal      // required — one-line wrong-decision indicator

  // Evidence posture (expectation level, not workflow)
  evidence_expectation_level  // required — E0 | E1 | E2 | E3 (see §4.3)

  // Boundaries
  is_lifecycle_transition     // required — boolean
  is_execution_task           // required — always false for valid decision types
  confusion_cues[]            // optional — what people mistake for this decision
}
```

### 4.3 Evidence expectation levels (not workflow gates)

| Level | Meaning | Example |
|-------|---------|---------|
| **E0** | Judgment / sponsor intent sufficient | `DEC_EXISTENCE` at Concept |
| **E1** | Documented hypothesis + rationale | `DEC_PRODUCT` at Discovery |
| **E2** | Measured or demonstrated evidence | `DEC_SCOPE` exit at Proof |
| **E3** | Operational proof + HITL for regulated | `DEC_COMPLIANCE` at Production for Extended |

### 4.4 Instance overlay (future binding, not v1 storage)

When applied to a product instance:

```text
decision_pressure_instance {
  decision_type_code,
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  effective_weight_class,      // may elevate above default
  effective_reversibility_class,
  pressure_rank,               // dominant | active | latent | dormant
  class_amplification_notes
}
```

**Non-claims:** no `decision_id`, no `decided_at`, no `approver`, no `status` — those belong to Decision Records layer (future), explicitly out of scope.

---

## 5. Decision Registry

Immutable registry rows parallel to lifecycle and class registries. Codes frozen at v1.

### 5.1 Registry rows

#### `DEC_EXISTENCE`

| Field | Value |
|-------|-------|
| **code** | `DEC_EXISTENCE` |
| **definition** | Whether product warrants continued existence in portfolio and NOVA attention |
| **when it appears** | `LC_CONCEPT` entry; kill/hold evaluation any stage; sponsor loss |
| **who is affected** | Product owner, sponsor, NOVA operator, dependent teams |
| **typical consequences** | Resource allocation; NOVA track on/off; downstream work authorized or halted |
| **reversibility level** | `REV_MODERATE` (revive killed product costly); hold is `REV_LOW_COST` |

---

#### `DEC_PRODUCT`

| Field | Value |
|-------|-------|
| **code** | `DEC_PRODUCT` |
| **definition** | Core value hypothesis and product identity commitment |
| **when it appears** | `LC_CONCEPT`–`LC_DISCOVERY`; pivot; major `LC_GROWTH` thesis change |
| **who is affected** | Users, product team, marketing, support narrative |
| **typical consequences** | Scope direction; differentiation; kill/pivot criteria |
| **reversibility level** | `REV_MODERATE` pre-Production; `REV_COSTLY` post-Production rebrand/reposition |

---

#### `DEC_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **code** | `DEC_CLASSIFICATION` |
| **definition** | Binding of `product_class_code`, tier, modifiers to product |
| **when it appears** | Before `LC_PROOF`; tier bump; hybrid reclassification |
| **who is affected** | NOVA operator, QA depth, legal template selection, contract templates |
| **typical consequences** | Registry defaults apply; skip rules; Extended vs Core path |
| **reversibility level** | `REV_MODERATE` early; `REV_COSTLY` after Production ops calibrated to wrong class |

---

#### `DEC_AUDIENCE`

| Field | Value |
|-------|-------|
| **code** | `DEC_AUDIENCE` |
| **definition** | Target users and distribution/acquisition strategy |
| **when it appears** | `LC_DISCOVERY`; pilot cohort selection; geo expansion |
| **who is affected** | Users reached; support load; store listing strategy |
| **typical consequences** | Pilot representativeness; compliance jurisdiction; metrics validity |
| **reversibility level** | `REV_LOW_COST` pre-Production; `REV_MODERATE` with live user base |

---

#### `DEC_SCOPE`

| Field | Value |
|-------|-------|
| **code** | `DEC_SCOPE` |
| **definition** | In/out boundary for current lifecycle phase effort |
| **when it appears** | Proof charter; pilot charter; growth charter; anti-scope-creep |
| **who is affected** | Engineering, QA, timeline, evidence quality |
| **typical consequences** | MVP inflation or false kill; proof validity |
| **reversibility level** | `REV_LOW_COST` within phase; `REV_MODERATE` across phase boundary |

---

#### `DEC_UX`

| Field | Value |
|-------|-------|
| **code** | `DEC_UX` |
| **definition** | Interaction model and core journey architecture commitment |
| **when it appears** | `LC_DISCOVERY` model; `LC_PROOF` journey lock; major redesign |
| **who is affected** | End users, accessibility, support (confusion), dev implementation |
| **typical consequences** | Rework cost; a11y debt; onboarding friction |
| **reversibility level** | `REV_LOW_COST` pre-Production core; `REV_COSTLY` post-adoption |

---

#### `DEC_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **code** | `DEC_ARCHITECTURE` |
| **definition** | Technical structure — stack, modules, sync, integration patterns |
| **when it appears** | Discovery feasibility; Proof exit; Growth strain; tech-debt crisis |
| **who is affected** | Engineering, ops, security, third-party vendors |
| **typical consequences** | Scalability ceiling; incident rate; migration cost |
| **reversibility level** | `REV_LOW_COST` spike-only; `REV_COSTLY` committed stack; `REV_TERMINAL` public API shape |

---

#### `DEC_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **code** | `DEC_DATA_PRIVACY` |
| **definition** | Data collection, storage, retention, export, deletion posture |
| **when it appears** | Discovery if any user data; mandatory pre-Pilot with PII; Sunset retention |
| **who is affected** | Users, legal, security, infra cost |
| **typical consequences** | Privacy labels; breach scope; sunset export obligations |
| **reversibility level** | `REV_MODERATE` pre-launch; `REV_COSTLY` with production data; retention at sunset `REV_TERMINAL` |

---

#### `DEC_COMPLIANCE`

| Field | Value |
|-------|-------|
| **code** | `DEC_COMPLIANCE` |
| **definition** | Regulatory, legal, and app-store compliance posture |
| **when it appears** | Discovery hypothesis; Production baseline; Growth per geo |
| **who is affected** | Legal, users, store presence, enterprise buyers |
| **typical consequences** | Store rejection; fines; market access |
| **reversibility level** | `REV_MODERATE` pre-filing; `REV_COSTLY` post-certification; some filings `REV_TERMINAL` |

---

#### `DEC_COMMERCIAL`

| Field | Value |
|-------|-------|
| **code** | `DEC_COMMERCIAL` |
| **definition** | Monetization and payment/refund/subscription model |
| **when it appears** | Discovery for revenue products; Pilot with real transactions |
| **who is affected** | Users, finance, support, fraud ops |
| **typical consequences** | Chargebacks; revenue recognition; refund policy load |
| **reversibility level** | `REV_COSTLY` after live pricing; payment rails `REV_TERMINAL` without migration |

---

#### `DEC_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **code** | `DEC_TRUST_SAFETY` |
| **definition** | Safety, abuse, fraud, AI autonomy and escalation boundaries |
| **when it appears** | Discovery for AI/marketplace; Pilot monitoring proof; Growth new domains |
| **who is affected** | Users, brand, legal, platform policy |
| **typical consequences** | Harm incidents; store removal; reputational loss |
| **reversibility level** | `REV_MODERATE` policy tuning; autonomy expansion `REV_COSTLY`; incident history `REV_TERMINAL` |

---

#### `DEC_OPERATIONS`

| Field | Value |
|-------|-------|
| **code** | `DEC_OPERATIONS` |
| **definition** | Support, monitoring, incident, handoff, survivability model |
| **when it appears** | Pilot lite playbook; Production full ops; Legacy minimal |
| **who is affected** | Support team, on-call, NOVA operator, client handoff |
| **typical consequences** | Incidents unhandled; handoff collapse (Factory lesson) |
| **reversibility level** | `REV_LOW_COST` lite ops; `REV_MODERATE` embedded ops model |

---

#### `DEC_RELEASE_DISTRIBUTION`

| Field | Value |
|-------|-------|
| **code** | `DEC_RELEASE_DISTRIBUTION` |
| **definition** | Channel and rollout posture — store, MDM, staged, geo |
| **when it appears** | Proof internal track; Pilot controlled; Production governed |
| **who is affected** | Users reached, release team, rollback capability |
| **typical consequences** | Wrong audience exposure; rollback failure |
| **reversibility level** | `REV_INSTANT`–`REV_LOW_COST` pre-public; `REV_MODERATE` after wide release |

---

#### `DEC_LIFECYCLE_TRANSITION`

| Field | Value |
|-------|-------|
| **code** | `DEC_LIFECYCLE_TRANSITION` |
| **definition** | Advance, hold, regress, or kill across lifecycle stages |
| **when it appears** | Every stage boundary; tier bump re-validation; AC-L rules trigger |
| **who is affected** | All domains — changes evidence and contract depth |
| **typical consequences** | Premature Production; perpetual Pilot; justified regression |
| **reversibility level** | Forward skip `REV_COSTLY` to reverse; kill `REV_TERMINAL`; hold `REV_LOW_COST` |

---

#### `DEC_EXPANSION`

| Field | Value |
|-------|-------|
| **code** | `DEC_EXPANSION` |
| **definition** | Growth charter — what expands (feature, geo, segment, monetization) |
| **when it appears** | `LC_PRODUCTION`→`LC_GROWTH`; within Growth |
| **who is affected** | QA load, legal per geo, architecture, support |
| **typical consequences** | Feature explosion; compliance overreach |
| **reversibility level** | `REV_MODERATE` feature flags; geo `REV_COSTLY`; market exit `REV_COSTLY` |

---

#### `DEC_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **code** | `DEC_ECOSYSTEM` |
| **definition** | Parent/child, API, third-party, platform coupling decisions |
| **when it appears** | `COMPANION` Discovery; integration commitments; parent version coupling |
| **who is affected** | Parent product team, API vendors, mobile parity |
| **typical consequences** | Companion drift; vendor lock; broken integrations |
| **reversibility level** | `REV_MODERATE` optional API; `REV_COSTLY` deep platform embed |

---

#### `DEC_INVESTMENT`

| Field | Value |
|-------|-------|
| **code** | `DEC_INVESTMENT` |
| **definition** | Continue investing vs harvest vs legacy withdrawal |
| **when it appears** | `LC_MATURE`; plateau; org budget cycles |
| **who is affected** | Team assignment, roadmap, user expectation |
| **typical consequences** | Neglect; zombie product; missed refresh window |
| **reversibility level** | `REV_LOW_COST` reallocation; legacy declaration `REV_MODERATE` |

---

#### `DEC_SUNSET`

| Field | Value |
|-------|-------|
| **code** | `DEC_SUNSET` |
| **definition** | End-of-life timeline, migration, export, decommission |
| **when it appears** | `LC_LEGACY` planning; `LC_SUNSET` execution |
| **who is affected** | Remaining users, legal retention, support, infra |
| **typical consequences** | Data loss; regulatory breach; user harm |
| **reversibility level** | `REV_TERMINAL` after decommission; planning phase `REV_MODERATE` |

---

## 6. Lifecycle Decision Pressure Matrix

Dominant decision families per lifecycle stage. **Dominant** = structurally highest pressure if unmade; **Active** = required but secondary; **Latent** = usually dormant; **Dormant** = atypical to open.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `DEC_EXISTENCE`, `DEC_PRODUCT` | `DEC_CLASSIFICATION` (hypothesis) | `DEC_AUDIENCE` | `DEC_ARCHITECTURE`, `DEC_COMMERCIAL`, `DEC_OPERATIONS` |
| **`LC_DISCOVERY`** | `DEC_PRODUCT`, `DEC_CLASSIFICATION`, `DEC_AUDIENCE`, `DEC_SCOPE` (hypothesis) | `DEC_UX`, `DEC_DATA_PRIVACY`, `DEC_COMPLIANCE` (hypothesis), `DEC_COMMERCIAL` (if revenue), `DEC_TRUST_SAFETY` (AI/marketplace), `DEC_ECOSYSTEM` (companion) | `DEC_ARCHITECTURE` (feasibility only) | `DEC_OPERATIONS`, `DEC_RELEASE_DISTRIBUTION` |
| **`LC_PROOF`** | `DEC_SCOPE`, `DEC_LIFECYCLE_TRANSITION`, `DEC_UX` (core journey) | `DEC_ARCHITECTURE` (selective), `DEC_PRODUCT` (pivot) | `DEC_DATA_PRIVACY`, `DEC_TRUST_SAFETY` | `DEC_OPERATIONS` (full), `DEC_EXPANSION` |
| **`LC_PILOT`** | `DEC_LIFECYCLE_TRANSITION`, `DEC_OPERATIONS` (lite), `DEC_RELEASE_DISTRIBUTION`, `DEC_AUDIENCE` (cohort validity) | `DEC_COMMERCIAL` (real money), `DEC_TRUST_SAFETY`, `DEC_COMPLIANCE`, `DEC_DATA_PRIVACY` | `DEC_ARCHITECTURE` (scale hints) | `DEC_EXPANSION`, `DEC_INVESTMENT` |
| **`LC_PRODUCTION`** | `DEC_LIFECYCLE_TRANSITION`, `DEC_OPERATIONS`, `DEC_COMPLIANCE`, `DEC_RELEASE_DISTRIBUTION` | `DEC_ARCHITECTURE` (baseline record), `DEC_DATA_PRIVACY`, `DEC_COMMERCIAL`, `DEC_TRUST_SAFETY` | `DEC_EXPANSION` (entry) | `DEC_SUNSET` |
| **`LC_GROWTH`** | `DEC_EXPANSION`, `DEC_LIFECYCLE_TRANSITION`, `DEC_ARCHITECTURE` (strain) | `DEC_COMPLIANCE` (geo), `DEC_COMMERCIAL`, `DEC_TRUST_SAFETY` (new domains), `DEC_SCOPE` (expansion boundary) | `DEC_UX` (new surfaces) | `DEC_EXISTENCE` |
| **`LC_MATURE`** | `DEC_INVESTMENT`, `DEC_LIFECYCLE_TRANSITION` | `DEC_OPERATIONS`, `DEC_COMPLIANCE` (drift), `DEC_ARCHITECTURE` (debt) | `DEC_EXPANSION` (refresh) | `DEC_PRODUCT` (unless refresh) |
| **`LC_LEGACY`** | `DEC_INVESTMENT`, `DEC_SUNSET` (planning), `DEC_LIFECYCLE_TRANSITION` | `DEC_OPERATIONS` (minimal), `DEC_COMPLIANCE`, `DEC_DATA_PRIVACY` | `DEC_ECOSYSTEM` (successor) | `DEC_EXPANSION` |
| **`LC_SUNSET`** | `DEC_SUNSET`, `DEC_DATA_PRIVACY` (retention), `DEC_LIFECYCLE_TRANSITION` | `DEC_COMPLIANCE`, `DEC_OPERATIONS` (wind-down), `DEC_RELEASE_DISTRIBUTION` (final) | `DEC_ECOSYSTEM` (migration target) | `DEC_COMMERCIAL`, `DEC_EXPANSION` |
| **`LC_HOLD`** | `DEC_EXISTENCE`, `DEC_LIFECYCLE_TRANSITION` (resume/kill) | All prior-stage decisions — **staleness review** | — | New `DEC_EXPANSION` |

### 6.1 Stage-critical questions (canonical)

| Stage | If you could only answer three decision questions |
|-------|---------------------------------------------------|
| `LC_CONCEPT` | Worth tracking? · What job? · Rough class hypothesis? |
| `LC_DISCOVERY` | For whom? · What class/tier? · Build or kill? |
| `LC_PROOF` | What is in scope? · Hypothesis supported? · Architecture sufficient for proof exit? |
| `LC_PILOT` | Real users justify ops? · Metrics met? · Advance, extend, or retreat? |
| `LC_PRODUCTION` | Ops survivable? · Compliance baseline true? · Distribution posture correct? |
| `LC_GROWTH` | What expands? · Architecture holds? · Geo/legal cleared? |
| `LC_MATURE` | Invest or harvest? · Legacy soon? · Compliance/security drift? |
| `LC_LEGACY` | When sunset? · Successor? · Minimal ops sustainable? |
| `LC_SUNSET` | Migration path? · Retention schedule? · User comms truthful? |

---

## 7. Product Class Decision Pressure Matrix

Criticality scale: **●** Critical (wrong decision class = product failure) · **◐** Elevated · **○** Standard · **—** Rarely material

Rows = decision families · Columns = 8 focus classes from charter

| Decision family | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-----------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `DEC_EXISTENCE` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `DEC_PRODUCT` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `DEC_CLASSIFICATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `DEC_AUDIENCE` | ◐ | ◐ | ◐ | ○ | ● | ● | ● | ◐ |
| `DEC_SCOPE` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `DEC_UX` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `DEC_ARCHITECTURE` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `DEC_DATA_PRIVACY` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `DEC_COMPLIANCE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `DEC_COMMERCIAL` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `DEC_TRUST_SAFETY` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `DEC_OPERATIONS` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `DEC_RELEASE_DISTRIBUTION` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `DEC_LIFECYCLE_TRANSITION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `DEC_EXPANSION` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `DEC_ECOSYSTEM` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `DEC_INVESTMENT` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `DEC_SUNSET` | ◐ | ◐ | ◐ | ○ | ● | ● | ● | ● |

### 7.1 Class-specific decision amplifications

| Class | Decisions that become disproportionately critical |
|-------|-----------------------------------------------------|
| **`COMMERCE`** | `DEC_COMMERCIAL`, `DEC_OPERATIONS` (refunds/chargebacks), `DEC_COMPLIANCE` (consumer law), `DEC_UX` (purchase journey) |
| **`FIELD_OPERATIONS`** | `DEC_ARCHITECTURE` (offline/sync), `DEC_SCOPE` (job completion proof), `DEC_DATA_PRIVACY` (geo/photo), `DEC_OPERATIONS` (data loss) |
| **`AI_ASSISTANT`** | `DEC_TRUST_SAFETY`, `DEC_DATA_PRIVACY`, `DEC_COMPLIANCE` (disclosure), `DEC_OPERATIONS` (escalation) |
| **`UTILITY_TOOL`** | `DEC_SCOPE` (anti-creep), `DEC_CLASSIFICATION` (avoid mis-tier); most families at ○ unless monetization added |
| **`MARKETPLACE`** | `DEC_TRUST_SAFETY` (multi-sided), `DEC_COMMERCIAL`, `DEC_ECOSYSTEM`, `DEC_COMPLIANCE` (platform liability) |
| **`HEALTH_MEDICAL`** | `DEC_COMPLIANCE`, `DEC_DATA_PRIVACY`, `DEC_TRUST_SAFETY`, `DEC_PRODUCT` (claims boundary) |
| **`FINTECH_WALLET`** | `DEC_COMPLIANCE`, `DEC_COMMERCIAL`, `DEC_TRUST_SAFETY`, `DEC_DATA_PRIVACY`, `DEC_ARCHITECTURE` (ledger/security) |
| **`AI_AGENT_CONSOLE`** | `DEC_TRUST_SAFETY` (autonomy/kill-switch), `DEC_COMPLIANCE`, `DEC_OPERATIONS` (audit), `DEC_ARCHITECTURE` (tool boundaries) |

**Tier modifier (all classes):** T3+ elevates `DEC_ARCHITECTURE`, `DEC_OPERATIONS`, `DEC_LIFECYCLE_TRANSITION` evidence to E2/E3; T4 elevates nearly all commitment-layer families to ●.

---

## 8. Decision Weight Model

Derived from **impact radius × rollback difficulty × evidence expectation** — not from team anxiety or executive volume.

### 8.1 Weight classes

#### `DW_NEGLIGIBLE`

| Field | Value |
|-------|-------|
| **Impact radius** | Single UI surface; no data; no external coupling |
| **Rollback difficulty** | Minutes; no user-visible persistence |
| **Evidence expectations** | E0 acceptable |
| **Examples** | Copy tweak inside established UX; internal label change |

---

#### `DW_LOCAL`

| Field | Value |
|-------|-------|
| **Impact radius** | One feature domain or journey branch |
| **Rollback difficulty** | Hours–days; limited user impact |
| **Evidence expectations** | E1 minimum |
| **Examples** | Secondary screen flow; optional integration stub |

---

#### `DW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Multiple journeys; shared components; moderate data touch |
| **Rollback difficulty** | Weeks; requires coordinated release |
| **Evidence expectations** | E2 minimum |
| **Examples** | Core UX model change; offline sync strategy; pilot scope boundary |

---

#### `DW_COMMITMENT`

| Field | Value |
|-------|-------|
| **Impact radius** | Product-wide; ops/legal/finance depend on it |
| **Rollback difficulty** | Months; user/data/contracts affected |
| **Evidence expectations** | E2–E3; HITL for Extended classes |
| **Examples** | Payment model live; compliance baseline; Production ops model; public API |

---

#### `DW_IRREVERSIBLE`

| Field | Value |
|-------|-------|
| **Impact radius** | External world changed — users, regulators, stores |
| **Rollback difficulty** | Impractical or impossible without harm |
| **Evidence expectations** | E3 mandatory |
| **Examples** | Store removal wrong; regulatory filing; mass data deletion error; kill after user dependency |

### 8.2 Default weight by decision family

| Family | Default weight | Elevates to `DW_COMMITMENT` when |
|--------|----------------|----------------------------------|
| `DEC_EXISTENCE` | `DW_STRUCTURAL` | Kill Production product |
| `DEC_PRODUCT` | `DW_STRUCTURAL` | Post-Production reposition |
| `DEC_CLASSIFICATION` | `DW_STRUCTURAL` | Extended class or T3+ |
| `DEC_AUDIENCE` | `DW_LOCAL` | Public consumer launch |
| `DEC_SCOPE` | `DW_STRUCTURAL` | Proof/Pilot boundary |
| `DEC_UX` | `DW_STRUCTURAL` | Core journey lock at Proof exit |
| `DEC_ARCHITECTURE` | `DW_STRUCTURAL` | Production baseline; `DW_COMMITMENT` at scale |
| `DEC_DATA_PRIVACY` | `DW_STRUCTURAL` | PII; `DW_COMMITMENT` regulated |
| `DEC_COMPLIANCE` | `DW_COMMITMENT` | Extended classes always |
| `DEC_COMMERCIAL` | `DW_COMMITMENT` | Real money |
| `DEC_TRUST_SAFETY` | `DW_COMMITMENT` | AI/marketplace live |
| `DEC_OPERATIONS` | `DW_COMMITMENT` | Production entry |
| `DEC_RELEASE_DISTRIBUTION` | `DW_STRUCTURAL` | Public wide release |
| `DEC_LIFECYCLE_TRANSITION` | `DW_STRUCTURAL` | Forward skip; `DW_COMMITMENT` to Production |
| `DEC_EXPANSION` | `DW_COMMITMENT` | Geo/compliance expansion |
| `DEC_ECOSYSTEM` | `DW_STRUCTURAL` | Deep platform embed |
| `DEC_INVESTMENT` | `DW_STRUCTURAL` | Legacy declaration |
| `DEC_SUNSET` | `DW_IRREVERSIBLE` | Decommission execution |

---

## 9. Decision Reversibility Model

Reversibility describes **cost of undo in product reality**, not git revert.

### 9.1 Reversibility classes

| Class | Definition | Typical rollback cost |
|-------|------------|----------------------|
| **`REV_INSTANT`** | Toggle, config, feature flag off | Minutes |
| **`REV_LOW_COST`** | Redeploy; limited users affected | Hours–days |
| **`REV_MODERATE`** | Migration script; comms; partial user impact | Weeks |
| **`REV_COSTLY`** | Major rework; market trust damage; contract renegotiation | Months |
| **`REV_TERMINAL`** | Cannot restore prior state without unacceptable harm | Permanent |

### 9.2 Family → reversibility map (default)

| Family | Default | Often becomes `REV_TERMINAL` |
|--------|---------|------------------------------|
| `DEC_EXISTENCE` | `REV_MODERATE` | Kill after dependency |
| `DEC_PRODUCT` | `REV_MODERATE` | Brand promise to market |
| `DEC_CLASSIFICATION` | `REV_MODERATE` | Wrong Extended class in Production |
| `DEC_AUDIENCE` | `REV_LOW_COST` | Mass market pivot |
| `DEC_SCOPE` | `REV_LOW_COST` | — |
| `DEC_UX` | `REV_MODERATE` | Core journey post-adoption |
| `DEC_ARCHITECTURE` | `REV_COSTLY` | Public client API |
| `DEC_DATA_PRIVACY` | `REV_COSTLY` | Retention/deletion executed |
| `DEC_COMPLIANCE` | `REV_COSTLY` | Filed/regulated status |
| `DEC_COMMERCIAL` | `REV_COSTLY` | Live pricing/payment rails |
| `DEC_TRUST_SAFETY` | `REV_MODERATE` | Published autonomy policy |
| `DEC_OPERATIONS` | `REV_LOW_COST` | — |
| `DEC_RELEASE_DISTRIBUTION` | `REV_LOW_COST` | Wide public botched launch |
| `DEC_LIFECYCLE_TRANSITION` | `REV_MODERATE` | Skip to Production |
| `DEC_EXPANSION` | `REV_MODERATE` | Geo exit |
| `DEC_ECOSYSTEM` | `REV_MODERATE` | Vendor embed |
| `DEC_INVESTMENT` | `REV_LOW_COST` | — |
| `DEC_SUNSET` | `REV_TERMINAL` | Post-decommission |

---

## 10. Decision Failure Patterns

Derived from Lifecycle §13, Website Factory drift, ORCA battle, MARS survivability — reframed as **decision mistakes**, not execution bugs.

| Pattern | Signal | Root decision failure | Affected families |
|---------|--------|----------------------|-------------------|
| **Architecture too early** | Stack debates in Concept; P6 artifacts before class binding | `DEC_ARCHITECTURE` opened before `DEC_CLASSIFICATION`/`DEC_SCOPE` | `DEC_ARCHITECTURE`, `DEC_LIFECYCLE_TRANSITION` |
| **Architecture too late** | Production incidents; unplanned migrations | `DEC_ARCHITECTURE` deferred past Proof exit on T3+ | `DEC_ARCHITECTURE`, `DEC_OPERATIONS` |
| **False compliance assumption** | «We'll add legal later»; store rejection | `DEC_COMPLIANCE` treated as latent in Discovery for Extended class | `DEC_COMPLIANCE`, `DEC_DATA_PRIVACY` |
| **Release without evidence** | Store live; no ops/compliance baseline | `DEC_LIFECYCLE_TRANSITION` conflated with release event | `DEC_LIFECYCLE_TRANSITION`, `DEC_OPERATIONS`, `DEC_RELEASE_DISTRIBUTION` |
| **Semantic ≠ deployed confusion** | Ads/PPC against draft intent not live product | `DEC_PRODUCT` (intent) not distinguished from deployed truth domain | `DEC_PRODUCT`, `DEC_UX`, `DEC_ECOSYSTEM` |
| **Classification drift** | T1 label on T3 product; utility creep to commerce | `DEC_CLASSIFICATION` not revisited on scope change | `DEC_CLASSIFICATION`, `DEC_SCOPE` |
| **Scope inflation** | Perpetual Proof; MVP never bounded | `DEC_SCOPE` absent or unenforced | `DEC_SCOPE`, `DEC_LIFECYCLE_TRANSITION` |
| **Pilot without ops decision** | Controlled users; no support/rollback | `DEC_OPERATIONS` latent during Pilot | `DEC_OPERATIONS`, `DEC_TRUST_SAFETY` |
| **Commercial without pilot money path** | Payment in Production first touch | `DEC_COMMERCIAL` jumped to Production | `DEC_COMMERCIAL`, `DEC_TRUST_SAFETY` |
| **Fake certainty** | Decision recorded as fact without E-level evidence | Weight class understated | All — weight model violation |
| **Decision laundering** | Strategic choice hidden inside task ticket | Boundary violation (§13) | Any — disguised as execution |
| **Endless reconsideration** | Same `DEC_ARCHITECTURE` reopened without lifecycle trigger | Missing anti-chaos AC-D rules | `DEC_ARCHITECTURE`, `DEC_PRODUCT` |
| **Random pivot** | `DEC_PRODUCT` change without lifecycle regression | No `DEC_LIFECYCLE_TRANSITION` pairing | `DEC_PRODUCT`, `DEC_LIFECYCLE_TRANSITION` |
| **Companion drift** | Mobile diverges from parent without `DEC_ECOSYSTEM` | Ecosystem decision avoided | `DEC_ECOSYSTEM`, `DEC_UX` |
| **Sunset denial** | Legacy product; no `DEC_SUNSET` | `DEC_INVESTMENT`/`DEC_EXISTENCE` avoided | `DEC_SUNSET`, `DEC_INVESTMENT` |
| **Handoff without ops reality** | Delivery complete; no survivability decision | `DEC_OPERATIONS` never at Production weight | `DEC_OPERATIONS` — Factory handoff-collapse analog |

---

## 11. Decision Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-D1** | Every product instance must have implicit or explicit answer for dominant decisions of current `lifecycle_state_code` | Decision vacuum |
| **AC-D2** | No `DEC_ARCHITECTURE` at `DW_COMMITMENT` before `DEC_CLASSIFICATION` binding | Architecture too early |
| **AC-D3** | Extended class: `DEC_COMPLIANCE` and `DEC_TRUST_SAFETY` cannot remain latent past `LC_DISCOVERY` | False compliance |
| **AC-D4** | `DEC_LIFECYCLE_TRANSITION` forward requires named decision — not inferred from ship date | Release = stage confusion |
| **AC-D5** | Same `decision_type_code` at `DW_STRUCTURAL`+ requires lifecycle or tier trigger to reopen | Endless reconsideration |
| **AC-D6** | Tasks/tickets cannot close strategic gaps — if gap is structural, name the `decision_type_code` | Decision laundering |
| **AC-D7** | `DEC_SCOPE` must exist in writing before `LC_PROOF` build commitment | Scope inflation |
| **AC-D8** | Weight class must be declared for `DW_COMMITMENT` and `DW_IRREVERSIBLE` decisions | Fake certainty |
| **AC-D9** | Pilot with real users requires lite `DEC_OPERATIONS` answer | Pilot without ops |
| **AC-D10** | `DEC_PRODUCT` pivot requires paired `DEC_LIFECYCLE_TRANSITION` consideration | Random pivot |
| **AC-D11** | One decision family per decision event — no «mega-decisions» bundling unrelated families | Decision inflation |
| **AC-D12** | `DEC_CLASSIFICATION` re-review on tier bump or payments/PII/regulated feature addition | Classification drift |
| **AC-D13** | Undocumented `DW_COMMITMENT`+ decision = SAFE UNKNOWN in REPORT | Silent critical decisions |
| **AC-D14** | `UTILITY_TOOL` T1 exempt from commercial/compliance families until trigger feature added | Over-engineering utility |
| **AC-D15** | Store/public release is `DEC_RELEASE_DISTRIBUTION` + often `DEC_LIFECYCLE_TRANSITION` — never implicit | AC-L10 lifecycle analog |

---

## 12. Decision Relationships

### 12.1 Dependency chain

```text
┌─────────────────────────────────────────────────────────────┐
│                    REALITY LAYER (NOVA)                      │
├─────────────────────────────────────────────────────────────┤
│  Production Model v1                                         │
│  Product Taxonomy v1                                         │
│  Product Class Registry v1  ──► product_class_code           │
│  Lifecycle Model v1         ──► lifecycle_state_code         │
│  Decision Reality Model v1  ──► decision_type_code     ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ pressure = f(class, lifecycle, tier)
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    CONTRACTS (future)                        │
│  Obligations crystallized per decision domain × stage        │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
                         Workflow · Roles · Tools · Agents
```

### 12.2 Why decisions depend on both class and lifecycle

| Input | Provides | Without it |
|-------|----------|------------|
| **`product_class_code`** | Which decision families are material; default weights; Extended vs Core | Same compliance depth for utility and fintech |
| **`lifecycle_state_code`** | Which families are dominant now; evidence level; latent vs active | Architecture debate in Concept; no ops in Production |
| **`complexity_tier`** | Evidence elevation; skip forbidden paths | T1 evidence on T4 marketplace |
| **`decision_type_code`** | The actual choice domain | Contracts attach to wrong obligation set |

**Combined pressure function (conceptual, not algorithm):**

```text
decision_pressure(decision_type_code, product_class_code, lifecycle_state_code, tier)
  → pressure_rank ∈ { dormant, latent, active, dominant }
  → effective_weight_class
  → evidence_expectation_level
```

**Examples:**

| Context | Pressure outcome |
|---------|------------------|
| `DEC_COMMERCIAL` + `UTILITY_TOOL` + `LC_PROOF` + T1 | Latent unless monetization trigger |
| `DEC_COMMERCIAL` + `COMMERCE` + `LC_PILOT` + T3 | Dominant; E2 real transactions |
| `DEC_ARCHITECTURE` + `AI_AGENT_CONSOLE` + `LC_DISCOVERY` + T4 | Active feasibility; not commitment until Proof exit |
| `DEC_SUNSET` + `HEALTH_MEDICAL` + `LC_SUNSET` + T4 | Dominant; `DW_IRREVERSIBLE`; E3 retention |

### 12.3 Cross-family dependencies (reality, not workflow)

| Upstream decision | Downstream decisions constrained |
|-------------------|----------------------------------|
| `DEC_CLASSIFICATION` | All commitment-layer families |
| `DEC_PRODUCT` | `DEC_SCOPE`, `DEC_UX`, `DEC_AUDIENCE` |
| `DEC_SCOPE` | `DEC_ARCHITECTURE` depth, `DEC_UX` surface |
| `DEC_DATA_PRIVACY` | `DEC_COMPLIANCE`, `DEC_SUNSET` |
| `DEC_LIFECYCLE_TRANSITION` | Which families must be answered before stage change |
| `DEC_EXPANSION` | Re-opens `DEC_COMPLIANCE`, `DEC_ARCHITECTURE`, `DEC_TRUST_SAFETY` |

---

## 13. Decision Reality Boundaries

### 13.1 What is NOT a decision

| Not a decision | Why | Correct layer |
|----------------|-----|---------------|
| **Task** | Execution unit with assigned work | Workflow / Production Model P-phases |
| **Bug** | Defect against existing commitment | QA / maintenance execution |
| **Feature** (as ticket) | Implementation of scoped product | Execution inside `DEC_SCOPE` boundary |
| **Ticket / issue** | Tracking artifact | Tooling — may *reference* decisions, not replace |
| **Sprint** | Time-boxed team commitment | Workflow |
| **Story point estimate** | Planning metric | Workflow |
| **Code review comment** | Quality feedback on implementation | Execution |
| **Release build** | Event | `DEC_RELEASE_DISTRIBUTION` is posture; build is execution |
| **Store submission** | Event | May inform `DEC_LIFECYCLE_TRANSITION` evidence — not the decision itself |
| **ADR document** | Record format | Future Decision Records; `DEC_ARCHITECTURE` is the underlying decision type |
| **Approval signature** | Authority act | Roles + Workflow (future) |
| **Gate pass/fail** | Contract enforcement outcome | Contracts layer (future) |
| **P-phase completion** | Production Model execution milestone | Orthogonal to decision types |
| **Design mockup** | Artifact | Informs `DEC_UX`; not the decision |
| **Metric measurement** | Evidence | Feeds decisions; not a decision |
| **Meeting** | Process | May surface decisions; not a decision type |

### 13.2 Boundary tests

Apply before labeling something a decision:

1. **Structural test:** Does this choice constrain multiple future domains (legal, ops, architecture)?
2. **Reversibility test:** Would undoing this cost more than a sprint?
3. **Evidence test:** Would NOVA ask for different evidence levels by class/tier/stage?
4. **Contract test:** Will a future contract need to know this was chosen? (If yes → likely decision; if no → likely task)

### 13.3 Common misuse prevention

| Misuse | Correction |
|--------|------------|
| «We decided in standup» | Standup is not a decision layer — name `decision_type_code` |
| «The sprint goal is the decision» | Sprint goal executes `DEC_SCOPE` — scope decision precedes sprint |
| «Shipped = decided Production» | Ship is release event; `DEC_LIFECYCLE_TRANSITION` is separate |
| «Legal doc = compliance decided» | Doc is contract artifact (future); `DEC_COMPLIANCE` is the reality choice |
| «Architecture diagram = decided» | Diagram may be spike; commitment weight requires Proof/lifecycle context |

---

## 14. RBM Mapping

```text
Reality
├── Production Model v1        … what NOVA is
├── Product Taxonomy v1        … what classes exist
├── Product Class Registry v1  … what each class means operationally
├── Lifecycle Model v1         … where the product is in life
└── Decision Reality Model v1  … what decisions exist in product nature  ◄── completes Decisions band vocabulary
        │
        ▼
Contracts                      … what must be true after choices (future)
        │
        ▼
Workflow                       … Production Model P0–P12 execution (future)
        │
        ▼
Roles                          … who decides / approves (future)
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

### 14.1 Why Decision Reality comes after Lifecycle and before Contracts

| Order | Reason |
|-------|--------|
| **Lifecycle before Decisions** | Stage determines which decision families are dominant vs dormant; without lifecycle, all decisions appear equally urgent |
| **Decisions before Contracts** | Contracts crystallize **obligations per decision domain** — without knowing decision types, contracts become generic checklists or wrong-depth templates |
| **Decisions before Workflow** | Workflow routes work; Decision Reality defines **what must be chosen** before work is meaningful |
| **Decisions before Roles** | Roles assign authority over decision domains — authority without domain vocabulary is politics |
| **Not before Registry** | Class determines which decision families matter at all — fintech without `DEC_COMMERCIAL` reality is incoherent |

**Completion of Decisions band (vocabulary only):** After this artifact, NOVA knows **identity** (registry), **time** (lifecycle), and **choice structure** (decision families + pressure). Contracts can now bind to `{ product_class × lifecycle × decision_domain }` instead of guessing.

**Explicitly NOT in Decisions band:** how decisions are recorded, routed, approved, or enforced.

---

## 15. Risks

| Risk | Severity | Mitigation in v1 |
|------|----------|------------------|
| Decision Reality confused with Decision Workflow | High | Scope boundary in header; §13 boundaries; no approval vocabulary |
| Decision inflation (too many types) | Medium | 17 families with rejection table §3.1; AC-D11 |
| Decision Reality confused with ADR tooling | Medium | `DEC_ARCHITECTURE` ≠ ADR storage; §13.1 |
| Weight class used as political lever | Medium | Derived criteria §8; AC-D8 |
| Lifecycle-decision conflation | High | Separate codes; AC-D4; matrix §6 |
| Class matrix oversimplification | Medium | Tier modifier §7.1; SAFE UNKNOWN for pilots |
| Silent critical decisions | High | AC-D13; failure pattern table §10 |
| Governance expansion drift | Medium | No Roles/Gates in v1; RBM §14 |
| Prior foundation files not in-repo | Medium | Cross-reference lifecycle doc; commit pack optional |
| Human enforcement fatigue | Medium | 15 anti-chaos rules only; not automation pretense |

---

## 16. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Exact numeric mapping weight → contract depth | First NOVA Contracts v1 charter |
| Whether `DEC_ECOSYSTEM` splits for `COMPANION` in v2 | First companion product through NOVA |
| Machine format for `decision_pressure_instance` | Future intake schema — not Decision Records |
| Regional regulatory sub-families under `DEC_COMPLIANCE` | Legal charter per geo |
| Overlap with MARS `registry/project-registry.md` | NOVA pack integration workflow |
| Optimal count of decision families (17 vs consolidated) | Operator feedback after 2–3 products |
| Prior Production Model / Taxonomy / Registry markdown in-repo | Human commit of foundation pack |
| Whether `LC_HOLD` stale review opens new decision types | Pilot operator feedback |
| AI agent decision domains beyond `DEC_TRUST_SAFETY` | First `AI_AGENT_CONSOLE` production pilot |

**Non-claims preserved:** this model does not assert decision tracking, automated gates, approval chains, or agent decision-making.

---

## 17. Recommended Next Step

**Single next artifact:** `NOVA CONTRACT REALITY MODEL v1` — first layer **after** Decision Reality, defining:

- contract domains mapped to `decision_type_code` families
- obligation depth as function of `product_class_code × lifecycle_state_code × effective_weight_class`
- explicit **non-enforcement** boundaries (not workflow gates)

**Do not skip to:** Decision Records, Decision Workflow, Approval Gates, Roles, Core Run, Agents, or full Workflow until Contract Reality charter approved.

**Optional parallel (human choice):** commit full NOVA foundation pack to `projects/nova/foundation/`:

- `NOVA-PRODUCTION-MODEL-v1.md`
- `NOVA-MOBILE-PRODUCT-TAXONOMY-v1.md`
- `NOVA-PRODUCT-CLASS-REGISTRY-v1.md`
- `NOVA-MOBILE-PRODUCT-LIFECYCLE-MODEL-v1.md`
- `NOVA-DECISION-REALITY-MODEL-v1.md` (this file)

**Lifecycle doc update (optional):** replace §18 «Decision Pressure System» pointer with reference to this artifact.

---

## Appendix A — Decision × Lifecycle × Class binding template

```markdown
# Decision Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| decision_type_code | pressure_rank | effective_weight | evidence_level | answered? |
|--------------------|---------------|------------------|----------------|-----------|
| DEC_EXISTENCE      |               |                  |                | Y/N/UNK   |
| ...                |               |                  |                |           |

SAFE UNKNOWN decisions:
Regression triggers:
```

---

## Appendix B — RBM layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | **Decision Reality Model v1** | **This document — vocabulary complete** |
| Contracts | — | Not started (recommended next) |
| Workflow | Production Model P0–P12 execution binding | Planned |
| Roles | — | Not started |
| Tools | — | Not started |
| Agents | — | Not started |
| Automation | — | Not started |

---

**Document status:** v1 design complete — Reality-layer decision vocabulary for NOVA mobile products. Nothing beyond Decision Reality.
