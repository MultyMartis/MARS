# NOVA Contract Reality Model v1

**Status:** design-only — Reality-layer obligation vocabulary, not contract templates, not legal document system, not workflow, not approval gates, not enforcement engine  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → NOVA Mobile Product Lifecycle Model v1 → NOVA Decision Reality Model v1 → **this document**  
**Non-claims:** no agents, no orchestration, no automated contract enforcement, no template library, no legal drafting system, no database schema, no gate automation

**Parent Reality artifacts:**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`
- NOVA Mobile Product Lifecycle Model v1 — temporal state per `lifecycle_state_code`
- NOVA Decision Reality Model v1 — structural choice domains per `decision_type_code`

**Evidence base:** Website Factory production-drift and site-type legal obligations; ORCA semantic-vs-deployed-copy and URL registry sync lessons; MARS survivability handoff/rollback discipline; ADR responsibility concepts adapted as obligation reality (not ADR tooling)

---

## 1. Executive Summary

NOVA Contract Reality Model v1 — **первый contract artifact NOVA**. Он отвечает на вопрос:

> **«Какие обязательства существуют из-за продуктовых решений?»**

Не «как оформить контракт» (Templates), не «кто подписывает» (Roles), не «когда блокировать» (Workflow Gates), не «как хранить» (Contract Records — future).

| Элемент | Содержание |
|---------|------------|
| **18 contract families** | `CTR_EXISTENCE` … `CTR_SUNSET` — derived taxonomy |
| **Canonical contract object** | `contract_type_code` + required reality fields |
| **Contract registry** | 18 rows with obligations, source decisions, failure modes |
| **Decision → Contract mapping** | 17 decision families → obligation crystallization |
| **Lifecycle contract pressure matrix** | Dominant contract families per `LC_*` stage |
| **Product class contract pressure matrix** | 8 focus classes × contract criticality |
| **Contract weight model** | 5 classes: `CW_DESCRIPTIVE` → `CW_BINDING` |
| **Failure patterns + anti-chaos** | Derived from MARS, ORCA, Website Factory lessons |

**Ключевое различие:**

| Dimension | Contract Reality (this doc) | Contract Workflow (NOT this) |
|-----------|----------------------------|------------------------------|
| **Question** | What obligations exist because of decisions? | How are obligations validated and enforced? |
| **Layer** | Reality → Contracts | Workflow / execution machinery (future) |
| **Example** | `CTR_COMPLIANCE` exists when `DEC_COMPLIANCE` is made | Compliance review meeting cadence |
| **Output** | Vocabulary + obligation maps | Templates, gates, sign-offs, automation |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answered:** «Where is the product in its life?» (`lifecycle_state_code`)  
**Decision Reality answered:** «What choices exist?» (`decision_type_code`)  
**Contract Reality answers:** «What must be true because those choices were made?» (`contract_type_code`)

Without contract reality, workflows enforce arbitrary checklists, roles approve documents without obligation context, and hidden commitments survive inside tasks and tickets.

---

## 2. Contract Philosophy

### 2.1 What a contract means inside NOVA

В NOVA **contract** — это **структурное обязательство**, возникающее когда продуктовое решение создаёт commitment, который:

1. **Должен оставаться истинным** — пока решение не пересмотрено через decision domain
2. **Связан с decision domain** — не существует «сам по себе»
3. **Имеет downstream consequence** — если нарушено, страдают users, ops, legal, или product integrity
4. **Может быть проверяем** — в principle, даже если enforcement ещё не спроектирован

Contract — **не документ**. Документ может *выражать* contract; contract существует в **реальности продукта** независимо от того, записан он или нет.

**Website Factory lesson:** legal pages в футере — это **expression** of `CTR_COMPLIANCE` + `CTR_DATA_PRIVACY`, не сами contracts. Отсутствие legal URLs при live form = **obligation violation**, не «missing template» ([`SITE-TYPE-IMPLEMENTATION-RULES-v1.md`](../../workspaces/website-factory-reference-v1/registry/SITE-TYPE-IMPLEMENTATION-RULES-v1.md)).

**ORCA lesson:** semantic pack ≠ deployed page создаёт **dual obligation domains** — intent contract vs deployed-truth contract. PPC export against wrong landing = **contract misalignment**, не exporter bug alone ([`ORCA-LESSONS-LEARNED-v1.md`](../../projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md)).

### 2.2 Why contracts exist

Decisions **выбирают**. Contracts **фиксируют что выбор означает для мира**:

| Decision says | Contract crystallizes |
|---------------|----------------------|
| «Мы commerce product» | Payment/refund obligations exist |
| «Мы pilot with real users» | Support and rollback obligations exist |
| «Мы collect PII» | Privacy and retention obligations exist |
| «Мы sunset in Q3» | Migration and data export obligations exist |

Без contract layer команды **исполняют решения**, не зная **какие обязательства они уже приняли**. Execution drift начинается когда obligations implicit.

**MARS Survivability lesson:** handoff collapse = **operations contract never crystallized** at Production transition — delivery files exist, obligation to maintain survivability does not ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)).

### 2.3 Why contracts come after decisions

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

| Layer | Provides | Without prior layer |
|-------|----------|---------------------|
| **Reality** | Product identity vocabulary | Random obligation labels |
| **Lifecycle** | Stage-appropriate obligation depth | Full legal pack at Concept |
| **Decisions** | Choice domains that create obligations | Generic checklists |
| **Contracts** | Obligation structure per decision × stage × class | Workflow enforces noise |

**Contracts без Decision Reality** — templates without applicability:

- `UTILITY_TOOL` T1 получает payment compliance pack «на всякий случай»
- `LC_CONCEPT` получает Production ops runbook requirement
- `DEC_ARCHITECTURE` never made, but `CTR_ARCHITECTURE` assumed from diagram

Decisions **не исполняются** — они определяют choice space. Contracts **кристаллизуют** consequences of choices into **obligation vocabulary**.

### 2.4 Why contracts are not workflows

| Contract Reality | Workflow (future) |
|------------------|-------------------|
| **What** must be true | **How** truth is verified |
| Obligation exists because decision was made | Gate checks obligation satisfaction |
| Describes structural commitment | Describes process steps |
| Survives team/process change | Resets when workflow changes |
| `CTR_COMPLIANCE` = privacy posture must match declared scope | Compliance review meeting in week 8 |

**Boundary test:** If you remove all humans and process, does the obligation still exist? **Yes** → contract. **No** → workflow artifact.

Examples:

| Artifact | Layer |
|----------|-------|
| «App must not collect location without consent» | `CTR_DATA_PRIVACY` — contract |
| «Legal review scheduled Tuesday» | Workflow — not contract |
| «Rollback tested before public release» | `CTR_RELEASE` — contract |
| «QA sign-off in Jira» | Workflow — not contract |
| «Support responds within 24h during pilot» | `CTR_OPERATIONS` — contract |
| «On-call rotation doc exists» | May express contract; rotation itself is ops execution |

### 2.5 What makes something a contract?

Apply **four tests** before labeling obligation as contract:

1. **Decision-origin test:** Does this obligation trace to a named `decision_type_code` (directly or through decision chain)?
2. **Persistence test:** Must this remain true across time/stages unless decision is explicitly revised?
3. **Consequence test:** Does violation harm users, legal standing, ops survivability, or product integrity?
4. **Verifiability test:** Could an observer determine satisfied/violated without knowing internal process?

**Pass all four** → contract family applies. **Fail any** → likely task, ticket, workflow step, or artifact — not contract.

**ADR parallel (adapted):** Architecture Decision Records document **who decided what and why**. NOVA contracts document **what the product must honor because of that decision** — responsibility without mandating ADR storage format.

---

## 3. Contract Taxonomy

### 3.1 Derivation rationale

Test for each candidate family: *«Does NOVA treat validation depth, ops load, and failure severity differently if this obligation is unmade, undocumented, or violated?»*

**Rejected as standalone contract families:**

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **Feature delivery** | Execution scope inside product boundary | → `CTR_SCOPE` + workflow tasks |
| **Bug fix SLA** | Tactical ops inside existing contract | → `CTR_OPERATIONS` detail |
| **Sprint commitment** | Team scheduling | → Workflow (future) |
| **Code review pass** | Quality gate on implementation | → Workflow; may validate `CTR_ARCHITECTURE` |
| **Legal document** | Expression format | → Template layer (future); `CTR_COMPLIANCE` is obligation |
| **Checklist item** | Process step | → Workflow unless maps to obligation |
| **Approval signature** | Authority act | → Roles + Workflow (future) |
| **QA test case** | Verification artifact | → May evidence `CTR_*`; not contract itself |

### 3.2 Contract families overview

```text
Portfolio layer:     CTR_EXISTENCE · CTR_INVESTMENT
Identity layer:      CTR_PRODUCT · CTR_CLASSIFICATION · CTR_AUDIENCE
Boundary layer:      CTR_SCOPE · CTR_UX
Commitment layer:    CTR_ARCHITECTURE · CTR_DATA_PRIVACY · CTR_COMPLIANCE
                     CTR_COMMERCIAL · CTR_TRUST_SAFETY
Operational layer:   CTR_OPERATIONS · CTR_RELEASE
Temporal layer:      CTR_LIFECYCLE · CTR_EXPANSION · CTR_ECOSYSTEM · CTR_SUNSET
```

**Design choice:** One primary `contract_type_code` per major decision domain (17 decisions → 18 contracts; `CTR_LIFECYCLE` spans transition obligations distinct from existence/investment). Preserves clean Decision → Contract mapping while allowing compound obligations within families.

### 3.3 Family definitions

#### `CTR_EXISTENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations arising from portfolio attention and continuation commitment |
| **Scope** | Resource allocation truth; NOVA track continuity; dependent work authorization |
| **Source decisions** | `DEC_EXISTENCE` |
| **Failure impact** | Zombie products; abandoned users; wasted parallel execution |

---

#### `CTR_PRODUCT`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations to deliver declared value hypothesis and product identity |
| **Scope** | Core job-to-be-done; differentiation claims; kill/pivot criteria honesty |
| **Source decisions** | `DEC_PRODUCT` |
| **Failure impact** | Intent/deployed drift (ORCA lesson); false marketing; scope without thesis |

---

#### `CTR_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations implied by bound `product_class_code`, tier, and modifiers |
| **Scope** | Registry defaults apply; QA/legal/ops depth matches declared class |
| **Source decisions** | `DEC_CLASSIFICATION` |
| **Failure impact** | Wrong-depth validation; Extended treated as Core; tier understatement |

---

#### `CTR_AUDIENCE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations to intended users and distribution reach |
| **Scope** | Cohort representativeness; acquisition honesty; jurisdiction of users reached |
| **Source decisions** | `DEC_AUDIENCE` |
| **Failure impact** | Invalid pilot metrics; wrong compliance jurisdiction; misleading reach |

---

#### `CTR_SCOPE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations within declared in/out boundary for current lifecycle phase |
| **Scope** | Proof charter; pilot charter; growth charter boundaries |
| **Source decisions** | `DEC_SCOPE` |
| **Failure impact** | Perpetual proof; MVP inflation; false validation |

---

#### `CTR_UX`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations to committed interaction model and core journey architecture |
| **Scope** | Cross-screen patterns; accessibility posture; onboarding architecture |
| **Source decisions** | `DEC_UX` |
| **Failure impact** | Journey rework cost; a11y debt; user confusion at scale |

---

#### `CTR_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations to committed technical structure |
| **Scope** | Platform, modules, sync/offline strategy, integration patterns, API shape |
| **Source decisions** | `DEC_ARCHITECTURE` |
| **Failure impact** | Production incidents; migration cost; scalability ceiling |

---

#### `CTR_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations for data collection, storage, retention, export, deletion |
| **Scope** | Data categories; minimization; user rights; residency |
| **Source decisions** | `DEC_DATA_PRIVACY` |
| **Failure impact** | Privacy label mismatch; breach scope expansion; sunset data loss |

---

#### `CTR_COMPLIANCE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations to regulatory, legal, and store-policy posture |
| **Scope** | Jurisdiction; consent model; medical/finance claims; store categories |
| **Source decisions** | `DEC_COMPLIANCE` |
| **Failure impact** | Store rejection; fines; market access loss |

---

#### `CTR_COMMERCIAL`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from monetization and payment model |
| **Scope** | Pricing honesty; payment/refund/subscription mechanics; revenue recognition alignment |
| **Source decisions** | `DEC_COMMERCIAL` |
| **Failure impact** | Chargebacks; fraud; consumer law violation |

---

#### `CTR_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations for safety, abuse prevention, AI autonomy limits |
| **Scope** | Output limits; escalation paths; human-in-loop; content policy |
| **Source decisions** | `DEC_TRUST_SAFETY` |
| **Failure impact** | User harm; store removal; reputational/legal loss |

---

#### `CTR_OPERATIONS`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations for keeping product alive in production |
| **Scope** | Support; monitoring; incident response; handoff survivability; rollback capability |
| **Source decisions** | `DEC_OPERATIONS` |
| **Failure impact** | Handoff collapse; incidents unhandled; delivery-and-forget |

---

#### `CTR_RELEASE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from distribution and rollout posture |
| **Scope** | Channel truth; staged rollout discipline; geo phasing; rollback tested |
| **Source decisions** | `DEC_RELEASE_DISTRIBUTION` |
| **Failure impact** | Wrong audience exposure; untested rollback; URL/registry drift (ORCA) |

---

#### `CTR_LIFECYCLE`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from lifecycle stage claims and transition commitments |
| **Scope** | Stage honesty; evidence before advance; regression when justified |
| **Source decisions** | `DEC_LIFECYCLE_TRANSITION` |
| **Failure impact** | Premature Production; perpetual Pilot; stage mislabeling |

---

#### `CTR_EXPANSION`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from growth charter — what may expand and under what governance |
| **Scope** | Feature/geo/segment expansion boundaries; re-validation triggers |
| **Source decisions** | `DEC_EXPANSION` |
| **Failure impact** | Feature explosion; geo compliance overreach; architecture strain |

---

#### `CTR_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from external coupling — parent, API, platform dependencies |
| **Scope** | Parity semantics; sync rules; vendor boundary; URL/registry alignment |
| **Source decisions** | `DEC_ECOSYSTEM` |
| **Failure impact** | Companion drift; broken integrations; semantic/deployed split |

---

#### `CTR_INVESTMENT`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from resource and attention allocation posture |
| **Scope** | Maintain vs harvest honesty; legacy withdrawal truth |
| **Source decisions** | `DEC_INVESTMENT` |
| **Failure impact** | Neglected products; zombie stability; security rot |

---

#### `CTR_SUNSET`

| Field | Value |
|-------|-------|
| **Purpose** | Obligations from end-of-life path |
| **Scope** | Timeline; migration; export; decommission; user communication |
| **Source decisions** | `DEC_SUNSET` |
| **Failure impact** | Data loss; regulatory retention breach; abrupt shutdown |

---

## 4. Contract Object Model

Canonical contract object describes **an obligation type in context**, not a stored record. Parallel to `product_class_code`, `lifecycle_state_code`, `decision_type_code`.

### 4.1 Core identifier

**`contract_type_code`** — immutable registry key; one of 18 family codes in §3.

### 4.2 Required fields (reality model)

```text
contract_reality_object {
  // Identity
  contract_type_code            // required — e.g. CTR_COMPLIANCE
  contract_family_layer         // required — portfolio | identity | boundary | commitment | operational | temporal

  // Definition
  obligation_subject            // required — short noun phrase: what must remain true
  obligation_statement          // required — canonical must/honor form (not template text)

  // Decision binding (conceptual — not storage)
  source_decision_type_codes[]  // required — which decisions create this contract
  lifecycle_state_codes[]       // required — stages where obligation is structurally active
  product_class_affinity[]      // required — classes where criticality elevates

  // Classification
  default_weight_class          // required — CW_* (see §9)
  default_enforcement_posture   // required — EP_* (see §4.3)

  // Obligation model (descriptive only)
  expected_obligations[]        // required — bullet-level obligation categories (not templates)
  affected_domains[]            // required — legal | ops | ux | data | release | portfolio
  typical_failure_signal        // required — one-line violation indicator

  // Verification posture (expectation level, not workflow)
  verification_expectation_level // required — V0 | V1 | V2 | V3 (see §4.4)

  // Boundaries
  is_legal_document             // required — always false (legal docs express contracts)
  is_workflow_gate              // required — always false for valid contract types
  is_checklist_item             // required — always false for valid contract types
  confusion_cues[]              // optional — what people mistake for this contract
}
```

### 4.3 Enforcement posture (descriptive, not workflow)

| Posture | Meaning |
|---------|---------|
| **EP_HONOR** | Obligation exists; violation is integrity failure even without formal gate |
| **EP_EVIDENCE** | Obligation requires demonstrable evidence at stage boundary |
| **EP_EXTERNAL** | Third party (store, regulator, user contract) can enforce |
| **EP_TERMINAL** | Violation after execution may be irreversible |

### 4.4 Verification expectation levels (not workflow gates)

| Level | Meaning | Example |
|-------|---------|---------|
| **V0** | Self-declaration sufficient for stage | `CTR_EXISTENCE` at Concept |
| **V1** | Documented obligation statement | `CTR_PRODUCT` at Discovery |
| **V2** | Demonstrable alignment (artifact, metric, test) | `CTR_SCOPE` at Proof exit |
| **V3** | Operational proof + HITL for Extended classes | `CTR_COMPLIANCE` at Production |

### 4.5 Instance overlay (future binding, not v1 storage)

When applied to a product instance:

```text
contract_pressure_instance {
  contract_type_code,
  product_class_code,
  complexity_tier,
  lifecycle_state_code,
  source_decision_type_code,     // triggering decision
  effective_weight_class,        // may elevate above default
  pressure_rank,                 // dominant | active | latent | dormant
  obligation_status,             // crystallized | implicit | violated | SAFE UNKNOWN — descriptive only
  class_amplification_notes
}
```

**Non-claims:** no `contract_id`, no `signed_at`, no `signatory`, no `template_ref` — those belong to Contract Records / Templates layers (future), explicitly out of scope.

---

## 5. Contract Registry

Immutable registry rows parallel to decision and lifecycle registries. Codes frozen at v1.

### 5.1 Registry rows

#### `CTR_EXISTENCE`

| Field | Value |
|-------|-------|
| **code** | `CTR_EXISTENCE` |
| **definition** | Product warrants continued portfolio attention and authorized downstream work |
| **source decision families** | `DEC_EXISTENCE` |
| **affected domains** | portfolio, engineering authorization |
| **expected obligations** | Explicit continue/hold/kill posture; no parallel build on kill path; sponsor alignment |
| **typical failure modes** | Stealth continuation after kill decision; resources on abandoned product |

---

#### `CTR_PRODUCT`

| Field | Value |
|-------|-------|
| **code** | `CTR_PRODUCT` |
| **definition** | Delivered product honors declared value hypothesis and identity |
| **source decision families** | `DEC_PRODUCT` |
| **affected domains** | ux, marketing, support narrative, semantic/deployed alignment |
| **expected obligations** | Core job achievable; differentiation claims truthful; pivot criteria documented |
| **typical failure modes** | Semantic ≠ deployed (ORCA); marketing promises beyond product; identity drift without pivot |

---

#### `CTR_CLASSIFICATION`

| Field | Value |
|-------|-------|
| **code** | `CTR_CLASSIFICATION` |
| **definition** | Operational depth matches declared class, tier, and modifiers |
| **source decision families** | `DEC_CLASSIFICATION` |
| **affected domains** | qa, legal, ops, contract depth selection |
| **expected obligations** | Registry defaults honored; Extended path when required; tier-appropriate validation |
| **typical failure modes** | T1 label on T3 product; utility creep to commerce without reclassification |

---

#### `CTR_AUDIENCE`

| Field | Value |
|-------|-------|
| **code** | `CTR_AUDIENCE` |
| **definition** | Product reach matches declared audience and distribution strategy |
| **source decision families** | `DEC_AUDIENCE` |
| **affected domains** | release, compliance jurisdiction, metrics validity |
| **expected obligations** | Pilot cohort representative; geo reach matches legal posture; acquisition honest |
| **typical failure modes** | Internal-only validation claimed as market proof; wrong jurisdiction users |

---

#### `CTR_SCOPE`

| Field | Value |
|-------|-------|
| **code** | `CTR_SCOPE` |
| **definition** | Work and product surface stay within declared phase boundary |
| **source decision families** | `DEC_SCOPE` |
| **affected domains** | engineering, qa, timeline, evidence quality |
| **expected obligations** | In/out list honored; proof ≠ production scope; charter limits respected |
| **typical failure modes** | Perpetual proof; scope inflation; false kill from unbounded MVP |

---

#### `CTR_UX`

| Field | Value |
|-------|-------|
| **code** | `CTR_UX` |
| **definition** | Interaction model and core journey match committed architecture |
| **source decision families** | `DEC_UX` |
| **affected domains** | ux, accessibility, support, development |
| **expected obligations** | Core journey coherent; a11y posture maintained; pattern consistency |
| **typical failure modes** | Journey rework post-adoption; a11y debt; onboarding architecture abandoned |

---

#### `CTR_ARCHITECTURE`

| Field | Value |
|-------|-------|
| **code** | `CTR_ARCHITECTURE` |
| **definition** | Technical implementation honors committed system structure |
| **source decision families** | `DEC_ARCHITECTURE` |
| **affected domains** | engineering, security, ops, vendors |
| **expected obligations** | Stack/modules as declared; sync/offline per decision; integration boundaries respected |
| **typical failure modes** | Diagram ≠ committed architecture; scale surprise; undeclared API surface |

---

#### `CTR_DATA_PRIVACY`

| Field | Value |
|-------|-------|
| **code** | `CTR_DATA_PRIVACY` |
| **definition** | Data handling matches declared collection, retention, and rights posture |
| **source decision families** | `DEC_DATA_PRIVACY` |
| **affected domains** | legal, security, infra, user trust |
| **expected obligations** | Collect only declared categories; retention schedule honored; export/delete paths work |
| **typical failure modes** | Privacy label mismatch; shadow data collection; sunset export failure |

---

#### `CTR_COMPLIANCE`

| Field | Value |
|-------|-------|
| **code** | `CTR_COMPLIANCE` |
| **definition** | Product posture matches declared regulatory and store obligations |
| **source decision families** | `DEC_COMPLIANCE` |
| **affected domains** | legal, store presence, enterprise sales |
| **expected obligations** | Jurisdiction rules honored; consent model implemented; claims within legal boundary |
| **typical failure modes** | «Legal later»; store rejection; medical/finance claims without basis |

---

#### `CTR_COMMERCIAL`

| Field | Value |
|-------|-------|
| **code** | `CTR_COMMERCIAL` |
| **definition** | Monetization behavior matches declared commercial model |
| **source decision families** | `DEC_COMMERCIAL` |
| **affected domains** | finance, support, fraud, user trust |
| **expected obligations** | Pricing honest; refund path works; subscription terms honored |
| **typical failure modes** | Payment in Production without pilot money path; hidden fees; chargeback unpreparedness |

---

#### `CTR_TRUST_SAFETY`

| Field | Value |
|-------|-------|
| **code** | `CTR_TRUST_SAFETY` |
| **definition** | Safety boundaries and escalation match declared trust posture |
| **source decision families** | `DEC_TRUST_SAFETY` |
| **affected domains** | users, brand, legal, platform policy |
| **expected obligations** | AI limits enforced; abuse paths handled; human escalation reachable |
| **typical failure modes** | Autonomy beyond declared limits; no escalation in pilot; harm incident unprepared |

---

#### `CTR_OPERATIONS`

| Field | Value |
|-------|-------|
| **code** | `CTR_OPERATIONS` |
| **definition** | Operational survivability matches declared ops model |
| **source decision families** | `DEC_OPERATIONS` |
| **affected domains** | support, on-call, handoff, monitoring |
| **expected obligations** | Support path exists; monitoring covers core journeys; handoff survivable; incident response defined |
| **typical failure modes** | Handoff collapse (Factory); pilot without support; Production with tribal knowledge only |

---

#### `CTR_RELEASE`

| Field | Value |
|-------|-------|
| **code** | `CTR_RELEASE` |
| **definition** | Distribution and rollout behavior matches declared release posture |
| **source decision families** | `DEC_RELEASE_DISTRIBUTION` |
| **affected domains** | release, users reached, rollback |
| **expected obligations** | Channel truth (internal vs public); staged rollout when declared; rollback tested; URL/registry sync (ORCA) |
| **typical failure modes** | Public exposure without rollback; URL drift across layers; store badge ≠ lifecycle stage |

---

#### `CTR_LIFECYCLE`

| Field | Value |
|-------|-------|
| **code** | `CTR_LIFECYCLE` |
| **definition** | Product lifecycle claims and transitions honor evidence requirements |
| **source decision families** | `DEC_LIFECYCLE_TRANSITION` |
| **affected domains** | all — stage change affects contract depth |
| **expected obligations** | Stage label honest; advance only with evidence; skip paths documented |
| **typical failure modes** | Ship = Production confusion; skip without charter; perpetual Pilot mislabeled |

---

#### `CTR_EXPANSION`

| Field | Value |
|-------|-------|
| **code** | `CTR_EXPANSION` |
| **definition** | Growth activity stays within declared expansion charter |
| **source decision families** | `DEC_EXPANSION` |
| **affected domains** | qa, legal, architecture, support |
| **expected obligations** | Geo/feature expansion pre-cleared; re-validation triggered; capacity acknowledged |
| **typical failure modes** | Undocumented geo launch; feature explosion; compliance overreach |

---

#### `CTR_ECOSYSTEM`

| Field | Value |
|-------|-------|
| **code** | `CTR_ECOSYSTEM` |
| **definition** | External couplings behave per declared integration and parity commitments |
| **source decision families** | `DEC_ECOSYSTEM` |
| **affected domains** | parent products, APIs, vendors, semantic/deployed sync |
| **expected obligations** | Companion parity honored; API contracts stable; registry layers aligned |
| **typical failure modes** | Companion drift; URL registry desync (ORCA); vendor boundary violation |

---

#### `CTR_INVESTMENT`

| Field | Value |
|-------|-------|
| **code** | `CTR_INVESTMENT` |
| **definition** | Resource and maintenance posture matches declared investment level |
| **source decision families** | `DEC_INVESTMENT` |
| **affected domains** | team, roadmap, user expectation, security maintenance |
| **expected obligations** | Harvest/legacy honesty; critical maintenance continues; no false «full product» claim |
| **typical failure modes** | Legacy denial; security rot; zombie product with Production label |

---

#### `CTR_SUNSET`

| Field | Value |
|-------|-------|
| **code** | `CTR_SUNSET` |
| **definition** | End-of-life execution matches declared sunset path |
| **source decision families** | `DEC_SUNSET` |
| **affected domains** | users, legal retention, support, infra |
| **expected obligations** | Timeline communicated; export works; retention schedule honored; store removal planned |
| **typical failure modes** | Abrupt shutdown; data loss; retention breach; missing user notification |

---

## 6. Decision → Contract Mapping

Core mapping: every major decision family **crystallizes** one primary contract family. Secondary contracts may **activate** when decision weight elevates.

### 6.1 Primary mapping (1:1 decision → contract)

| `decision_type_code` | Primary `contract_type_code` | Obligation crystallized |
|----------------------|------------------------------|-------------------------|
| `DEC_EXISTENCE` | `CTR_EXISTENCE` | Portfolio attention and work authorization obligations |
| `DEC_PRODUCT` | `CTR_PRODUCT` | Value hypothesis and identity delivery obligations |
| `DEC_CLASSIFICATION` | `CTR_CLASSIFICATION` | Class/tier-appropriate operational depth obligations |
| `DEC_AUDIENCE` | `CTR_AUDIENCE` | Audience reach and cohort truth obligations |
| `DEC_SCOPE` | `CTR_SCOPE` | Phase boundary honor obligations |
| `DEC_UX` | `CTR_UX` | Journey and interaction model obligations |
| `DEC_ARCHITECTURE` | `CTR_ARCHITECTURE` | Technical structure honor obligations |
| `DEC_DATA_PRIVACY` | `CTR_DATA_PRIVACY` | Data handling obligations |
| `DEC_COMPLIANCE` | `CTR_COMPLIANCE` | Regulatory and store posture obligations |
| `DEC_COMMERCIAL` | `CTR_COMMERCIAL` | Monetization and payment obligations |
| `DEC_TRUST_SAFETY` | `CTR_TRUST_SAFETY` | Safety and escalation obligations |
| `DEC_OPERATIONS` | `CTR_OPERATIONS` | Survivability and support obligations |
| `DEC_RELEASE_DISTRIBUTION` | `CTR_RELEASE` | Distribution and rollout obligations |
| `DEC_LIFECYCLE_TRANSITION` | `CTR_LIFECYCLE` | Stage honesty and evidence obligations |
| `DEC_EXPANSION` | `CTR_EXPANSION` | Growth charter boundary obligations |
| `DEC_ECOSYSTEM` | `CTR_ECOSYSTEM` | External coupling obligations |
| `DEC_INVESTMENT` | `CTR_INVESTMENT` | Maintenance and harvest honesty obligations |
| `DEC_SUNSET` | `CTR_SUNSET` | End-of-life execution obligations |

### 6.2 Secondary activations (decision triggers additional contracts)

| Trigger decision | Also activates | Condition |
|------------------|----------------|-----------|
| `DEC_CLASSIFICATION` → Extended class | `CTR_COMPLIANCE`, `CTR_TRUST_SAFETY` at elevated weight | Extended class binding |
| `DEC_DATA_PRIVACY` + PII | `CTR_COMPLIANCE` | Privacy triggers legal posture |
| `DEC_COMMERCIAL` + real money | `CTR_TRUST_SAFETY`, `CTR_OPERATIONS` | Fraud/chargeback/support load |
| `DEC_LIFECYCLE_TRANSITION` → Production | `CTR_OPERATIONS`, `CTR_COMPLIANCE`, `CTR_RELEASE` at full weight | Production entry |
| `DEC_EXPANSION` + geo | `CTR_COMPLIANCE`, `CTR_DATA_PRIVACY` | Jurisdiction expansion |
| `DEC_ECOSYSTEM` + companion | `CTR_PRODUCT`, `CTR_UX` | Parity semantics |
| `DEC_SUNSET` | `CTR_DATA_PRIVACY` (retention), `CTR_COMPLIANCE` | Terminal data obligations |

### 6.3 Decision weight → contract weight elevation

| Decision weight | Typical contract weight | Notes |
|-----------------|------------------------|-------|
| `DW_NEGLIGIBLE` | `CW_DESCRIPTIVE` | Obligation exists but low verification |
| `DW_LOCAL` | `CW_DESCRIPTIVE` or `CW_OPERATIONAL` | Domain-local honor |
| `DW_STRUCTURAL` | `CW_OPERATIONAL` or `CW_STRUCTURAL` | Multi-domain alignment required |
| `DW_COMMITMENT` | `CW_STRUCTURAL` or `CW_CRITICAL` | External or ops dependency |
| `DW_IRREVERSIBLE` | `CW_CRITICAL` or `CW_BINDING` | Terminal or regulatory binding |

### 6.4 Mapping diagram

```text
DEC_EXISTENCE ──────────────► CTR_EXISTENCE
DEC_PRODUCT ────────────────► CTR_PRODUCT
DEC_CLASSIFICATION ─────────► CTR_CLASSIFICATION ──► (Extended) CTR_COMPLIANCE ↑
DEC_AUDIENCE ───────────────► CTR_AUDIENCE
DEC_SCOPE ──────────────────► CTR_SCOPE
DEC_UX ─────────────────────► CTR_UX
DEC_ARCHITECTURE ───────────► CTR_ARCHITECTURE
DEC_DATA_PRIVACY ───────────► CTR_DATA_PRIVACY ────► CTR_COMPLIANCE (if PII)
DEC_COMPLIANCE ─────────────► CTR_COMPLIANCE
DEC_COMMERCIAL ─────────────► CTR_COMMERCIAL ──────► CTR_TRUST_SAFETY, CTR_OPERATIONS
DEC_TRUST_SAFETY ───────────► CTR_TRUST_SAFETY
DEC_OPERATIONS ─────────────► CTR_OPERATIONS
DEC_RELEASE_DISTRIBUTION ───► CTR_RELEASE
DEC_LIFECYCLE_TRANSITION ───► CTR_LIFECYCLE ────────► CTR_OPERATIONS, CTR_COMPLIANCE, CTR_RELEASE (Production)
DEC_EXPANSION ──────────────► CTR_EXPANSION ────────► CTR_COMPLIANCE (geo)
DEC_ECOSYSTEM ──────────────► CTR_ECOSYSTEM ───────► CTR_PRODUCT, CTR_UX (companion)
DEC_INVESTMENT ─────────────► CTR_INVESTMENT
DEC_SUNSET ─────────────────► CTR_SUNSET ───────────► CTR_DATA_PRIVACY, CTR_COMPLIANCE
```

---

## 7. Lifecycle Contract Pressure Matrix

Dominant contract families per lifecycle stage. **Dominant** = structurally highest obligation pressure if implicit or violated; **Active** = required but secondary; **Latent** = usually dormant; **Dormant** = atypical.

| Stage | Dominant | Active | Latent | Dormant |
|-------|----------|--------|--------|---------|
| **`LC_CONCEPT`** | `CTR_EXISTENCE`, `CTR_PRODUCT` | `CTR_CLASSIFICATION` (hypothesis) | `CTR_AUDIENCE` | `CTR_ARCHITECTURE`, `CTR_COMMERCIAL`, `CTR_OPERATIONS`, `CTR_COMPLIANCE` |
| **`LC_DISCOVERY`** | `CTR_PRODUCT`, `CTR_CLASSIFICATION`, `CTR_AUDIENCE`, `CTR_SCOPE` (hypothesis) | `CTR_UX`, `CTR_DATA_PRIVACY`, `CTR_COMPLIANCE` (hypothesis), `CTR_COMMERCIAL` (if revenue), `CTR_TRUST_SAFETY` (AI/marketplace), `CTR_ECOSYSTEM` (companion) | `CTR_ARCHITECTURE` | `CTR_OPERATIONS`, `CTR_RELEASE` |
| **`LC_PROOF`** | `CTR_SCOPE`, `CTR_LIFECYCLE`, `CTR_UX` (core journey) | `CTR_ARCHITECTURE` (selective), `CTR_PRODUCT` (pivot) | `CTR_DATA_PRIVACY`, `CTR_TRUST_SAFETY` | `CTR_OPERATIONS` (full), `CTR_EXPANSION` |
| **`LC_PILOT`** | `CTR_LIFECYCLE`, `CTR_OPERATIONS` (lite), `CTR_RELEASE`, `CTR_AUDIENCE` (cohort) | `CTR_COMMERCIAL` (real money), `CTR_TRUST_SAFETY`, `CTR_COMPLIANCE`, `CTR_DATA_PRIVACY` | `CTR_ARCHITECTURE` (scale hints) | `CTR_EXPANSION`, `CTR_INVESTMENT` |
| **`LC_PRODUCTION`** | `CTR_LIFECYCLE`, `CTR_OPERATIONS`, `CTR_COMPLIANCE`, `CTR_RELEASE` | `CTR_ARCHITECTURE` (baseline), `CTR_DATA_PRIVACY`, `CTR_COMMERCIAL`, `CTR_TRUST_SAFETY`, `CTR_CLASSIFICATION` | `CTR_EXPANSION` (entry) | `CTR_SUNSET` |
| **`LC_GROWTH`** | `CTR_EXPANSION`, `CTR_LIFECYCLE`, `CTR_ARCHITECTURE` (strain) | `CTR_COMPLIANCE` (geo), `CTR_COMMERCIAL`, `CTR_TRUST_SAFETY` (new domains), `CTR_SCOPE` (expansion boundary) | `CTR_UX` (new surfaces) | `CTR_EXISTENCE` |
| **`LC_MATURE`** | `CTR_INVESTMENT`, `CTR_LIFECYCLE` | `CTR_OPERATIONS`, `CTR_COMPLIANCE` (drift), `CTR_ARCHITECTURE` (debt) | `CTR_EXPANSION` (refresh) | `CTR_PRODUCT` (unless refresh) |
| **`LC_LEGACY`** | `CTR_INVESTMENT`, `CTR_SUNSET` (planning), `CTR_LIFECYCLE` | `CTR_OPERATIONS` (minimal), `CTR_COMPLIANCE`, `CTR_DATA_PRIVACY` | `CTR_ECOSYSTEM` (successor) | `CTR_EXPANSION` |
| **`LC_SUNSET`** | `CTR_SUNSET`, `CTR_DATA_PRIVACY` (retention), `CTR_LIFECYCLE` | `CTR_COMPLIANCE`, `CTR_OPERATIONS` (wind-down), `CTR_RELEASE` (final) | `CTR_ECOSYSTEM` (migration target) | `CTR_COMMERCIAL`, `CTR_EXPANSION` |
| **`LC_HOLD`** | `CTR_EXISTENCE`, `CTR_LIFECYCLE` (resume/kill) | All prior-stage contracts — **staleness review** | — | New `CTR_EXPANSION` |

### 7.1 Stage-critical obligation questions

| Stage | If obligations could only be verified on three contracts |
|-------|----------------------------------------------------------|
| `LC_CONCEPT` | `CTR_EXISTENCE` · `CTR_PRODUCT` · `CTR_CLASSIFICATION` (hypothesis) |
| `LC_DISCOVERY` | `CTR_CLASSIFICATION` · `CTR_PRODUCT` · `CTR_AUDIENCE` |
| `LC_PROOF` | `CTR_SCOPE` · `CTR_UX` · `CTR_LIFECYCLE` (exit honesty) |
| `LC_PILOT` | `CTR_OPERATIONS` (lite) · `CTR_RELEASE` · `CTR_LIFECYCLE` |
| `LC_PRODUCTION` | `CTR_OPERATIONS` · `CTR_COMPLIANCE` · `CTR_RELEASE` |
| `LC_GROWTH` | `CTR_EXPANSION` · `CTR_ARCHITECTURE` · `CTR_COMPLIANCE` |
| `LC_MATURE` | `CTR_INVESTMENT` · `CTR_OPERATIONS` · `CTR_COMPLIANCE` |
| `LC_LEGACY` | `CTR_INVESTMENT` · `CTR_SUNSET` (plan) · `CTR_OPERATIONS` (minimal) |
| `LC_SUNSET` | `CTR_SUNSET` · `CTR_DATA_PRIVACY` · `CTR_COMPLIANCE` |

---

## 8. Product Class Contract Pressure Matrix

Criticality scale: **●** Critical (violation = product failure) · **◐** Elevated · **○** Standard · **—** Rarely material

Rows = contract families · Columns = 8 focus classes from charter

| Contract family | COMMERCE | FIELD_OPERATIONS | AI_ASSISTANT | UTILITY_TOOL | MARKETPLACE | HEALTH_MEDICAL | FINTECH_WALLET | AI_AGENT_CONSOLE |
|-----------------|----------|------------------|--------------|--------------|-------------|----------------|----------------|------------------|
| `CTR_EXISTENCE` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ● | ● |
| `CTR_PRODUCT` | ◐ | ◐ | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `CTR_CLASSIFICATION` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `CTR_AUDIENCE` | ◐ | ◐ | ◐ | ○ | ● | ● | ● | ◐ |
| `CTR_SCOPE` | ◐ | ● | ◐ | ○ | ◐ | ● | ◐ | ◐ |
| `CTR_UX` | ● | ● | ◐ | ○ | ● | ● | ◐ | ◐ |
| `CTR_ARCHITECTURE` | ◐ | ● | ◐ | ○ | ● | ● | ● | ● |
| `CTR_DATA_PRIVACY` | ● | ● | ◐ | ○ | ● | ● | ● | ◐ |
| `CTR_COMPLIANCE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `CTR_COMMERCIAL` | ● | ○ | ○ | ○ | ● | ○ | ● | ○ |
| `CTR_TRUST_SAFETY` | ◐ | ◐ | ● | ○ | ● | ● | ● | ● |
| `CTR_OPERATIONS` | ● | ● | ◐ | ○ | ● | ● | ● | ● |
| `CTR_RELEASE` | ● | ◐ | ◐ | ○ | ● | ● | ● | ● |
| `CTR_LIFECYCLE` | ● | ● | ● | ○ | ● | ● | ● | ● |
| `CTR_EXPANSION` | ● | ◐ | ◐ | — | ● | ● | ● | ◐ |
| `CTR_ECOSYSTEM` | ◐ | ◐ | ◐ | ○ | ● | ◐ | ● | ● |
| `CTR_INVESTMENT` | ◐ | ◐ | ◐ | ○ | ◐ | ◐ | ◐ | ◐ |
| `CTR_SUNSET` | ◐ | ◐ | ◐ | ○ | ● | ● | ● | ● |

### 8.1 Class-specific contract amplifications

| Class | Contracts that become disproportionately critical |
|-------|-----------------------------------------------------|
| **`COMMERCE`** | `CTR_COMMERCIAL`, `CTR_OPERATIONS` (refunds), `CTR_COMPLIANCE` (consumer law), `CTR_UX` (purchase journey) |
| **`FIELD_OPERATIONS`** | `CTR_ARCHITECTURE` (offline/sync), `CTR_SCOPE` (job proof), `CTR_DATA_PRIVACY` (geo/photo), `CTR_OPERATIONS` (data loss) |
| **`AI_ASSISTANT`** | `CTR_TRUST_SAFETY`, `CTR_DATA_PRIVACY`, `CTR_COMPLIANCE` (disclosure), `CTR_OPERATIONS` (escalation) |
| **`UTILITY_TOOL`** | `CTR_SCOPE` (anti-creep), `CTR_CLASSIFICATION` (avoid mis-tier); most at ○ unless monetization/PII trigger |
| **`MARKETPLACE`** | `CTR_TRUST_SAFETY` (multi-sided), `CTR_COMMERCIAL`, `CTR_ECOSYSTEM`, `CTR_COMPLIANCE` (platform liability) |
| **`HEALTH_MEDICAL`** | `CTR_COMPLIANCE`, `CTR_DATA_PRIVACY`, `CTR_TRUST_SAFETY`, `CTR_PRODUCT` (claims boundary) |
| **`FINTECH_WALLET`** | `CTR_COMPLIANCE`, `CTR_COMMERCIAL`, `CTR_TRUST_SAFETY`, `CTR_DATA_PRIVACY`, `CTR_ARCHITECTURE` (ledger/security) |
| **`AI_AGENT_CONSOLE`** | `CTR_TRUST_SAFETY` (autonomy/kill-switch), `CTR_COMPLIANCE`, `CTR_OPERATIONS` (audit), `CTR_ARCHITECTURE` (tool boundaries) |

**Tier modifier (all classes):** T3+ elevates `CTR_ARCHITECTURE`, `CTR_OPERATIONS`, `CTR_LIFECYCLE` to V2/V3; T4 elevates nearly all commitment-layer contracts to ●.

---

## 9. Contract Weight Model

Derived from **impact radius × external enforceability × verification depth** — not from document page count or legal anxiety.

### 9.1 Weight classes

#### `CW_DESCRIPTIVE`

| Field | Value |
|-------|-------|
| **Impact radius** | Internal clarity; minimal external exposure |
| **Validation expectations** | V0–V1; self-declaration or brief documentation |
| **Downstream consequences** | Rework cost low; no user/legal harm if violated briefly |
| **Examples** | `CTR_EXISTENCE` at Concept; `CTR_PRODUCT` hypothesis; `CTR_AUDIENCE` sketch |

---

#### `CW_OPERATIONAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Single domain or journey branch |
| **Validation expectations** | V1–V2; demonstrable alignment |
| **Downstream consequences** | Hours–weeks recovery; limited user impact |
| **Examples** | `CTR_SCOPE` in Proof; `CTR_UX` secondary surfaces; lite `CTR_OPERATIONS` in Pilot |

---

#### `CW_STRUCTURAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Multiple domains; shared infrastructure |
| **Validation expectations** | V2; measured or tested alignment |
| **Downstream consequences** | Weeks–months; coordinated release to fix |
| **Examples** | `CTR_ARCHITECTURE` baseline; `CTR_RELEASE` public rollout; `CTR_EXPANSION` charter |

---

#### `CW_CRITICAL`

| Field | Value |
|-------|-------|
| **Impact radius** | Product-wide; ops/legal/finance/users depend |
| **Validation expectations** | V2–V3; HITL for Extended classes |
| **Downstream consequences** | Months; trust/regulatory/market damage |
| **Examples** | `CTR_COMPLIANCE` Production; `CTR_COMMERCIAL` live money; `CTR_OPERATIONS` Production; `CTR_TRUST_SAFETY` AI live |

---

#### `CW_BINDING`

| Field | Value |
|-------|-------|
| **Impact radius** | External world changed — regulators, stores, user contracts |
| **Validation expectations** | V3 mandatory |
| **Downstream consequences** | Irreversible or impractical to undo without harm |
| **Examples** | `CTR_SUNSET` decommission executed; regulatory filing obligations; mass deletion error |

### 9.2 Default weight by contract family

| Family | Default weight | Elevates to `CW_CRITICAL` when |
|--------|----------------|--------------------------------|
| `CTR_EXISTENCE` | `CW_OPERATIONAL` | Production product kill |
| `CTR_PRODUCT` | `CW_OPERATIONAL` | Post-Production identity claims |
| `CTR_CLASSIFICATION` | `CW_STRUCTURAL` | Extended class or T3+ |
| `CTR_AUDIENCE` | `CW_OPERATIONAL` | Public consumer launch |
| `CTR_SCOPE` | `CW_STRUCTURAL` | Proof/Pilot boundary |
| `CTR_UX` | `CW_STRUCTURAL` | Core journey lock at Proof exit |
| `CTR_ARCHITECTURE` | `CW_STRUCTURAL` | Production baseline; `CW_CRITICAL` at scale |
| `CTR_DATA_PRIVACY` | `CW_STRUCTURAL` | PII; `CW_CRITICAL` regulated |
| `CTR_COMPLIANCE` | `CW_CRITICAL` | Extended classes always |
| `CTR_COMMERCIAL` | `CW_CRITICAL` | Real money |
| `CTR_TRUST_SAFETY` | `CW_CRITICAL` | AI/marketplace live |
| `CTR_OPERATIONS` | `CW_CRITICAL` | Production entry |
| `CTR_RELEASE` | `CW_STRUCTURAL` | Public wide release |
| `CTR_LIFECYCLE` | `CW_STRUCTURAL` | Production transition claim |
| `CTR_EXPANSION` | `CW_CRITICAL` | Geo/compliance expansion |
| `CTR_ECOSYSTEM` | `CW_STRUCTURAL` | Deep platform embed |
| `CTR_INVESTMENT` | `CW_OPERATIONAL` | Legacy declaration |
| `CTR_SUNSET` | `CW_BINDING` | Decommission execution |

---

## 10. Contract Failure Patterns

Derived from Decision Failure Patterns §10, Website Factory drift, ORCA battle, MARS survivability — reframed as **obligation failures**, not execution bugs.

| Pattern | Signal | Root contract failure | Affected contracts |
|---------|--------|----------------------|-------------------|
| **Obligation not documented** | Decision made; no obligation statement | Contract never crystallized from decision | Any — implicit violation |
| **Obligation forgotten** | Production live; Concept-level ops | `CTR_OPERATIONS` never elevated at transition | `CTR_OPERATIONS`, `CTR_LIFECYCLE` |
| **Decision without commitment** | «We decided compliance»; no privacy implementation | `DEC_COMPLIANCE` without `CTR_COMPLIANCE` crystallization | `CTR_COMPLIANCE`, `CTR_DATA_PRIVACY` |
| **Release promise without ops reality** | Store live; no support/rollback | `CTR_RELEASE` without `CTR_OPERATIONS` | `CTR_RELEASE`, `CTR_OPERATIONS`, `CTR_LIFECYCLE` |
| **Semantic ≠ deployed obligation split** | Ads/PPC against draft not live product | `CTR_PRODUCT` intent vs deployed misaligned | `CTR_PRODUCT`, `CTR_ECOSYSTEM`, `CTR_RELEASE` |
| **Classification contract mismatch** | T1 validation on T3 product | `CTR_CLASSIFICATION` violated | `CTR_CLASSIFICATION`, downstream all |
| **Scope contract inflation** | Perpetual Proof; unbounded MVP | `CTR_SCOPE` unenforced | `CTR_SCOPE`, `CTR_LIFECYCLE` |
| **Handoff collapse** | Delivery files; no survivability obligation | `CTR_OPERATIONS` handoff obligations absent | `CTR_OPERATIONS` — Factory analog |
| **URL/registry obligation drift** | Three layers desynced | `CTR_ECOSYSTEM` / `CTR_RELEASE` violated | `CTR_ECOSYSTEM`, `CTR_RELEASE` — ORCA |
| **Legal doc ≠ compliance obligation** | Privacy policy exists; app collects undeclared data | Document expresses but `CTR_DATA_PRIVACY` violated | `CTR_DATA_PRIVACY`, `CTR_COMPLIANCE` |
| **Fake contract** | Checklist marked done; obligation false | Verification theater without honor | Any at `CW_CRITICAL`+ |
| **Hidden commitment** | Strategic obligation in ticket, no contract | Decision laundering → contract gap | Any — disguised |
| **Contract inflation** | Full legal pack on utility T1 | Wrong-depth obligations applied | `CTR_COMPLIANCE`, `CTR_CLASSIFICATION` |
| **Duplicate obligations** | Two docs, conflicting statements | Same contract family, inconsistent crystallization | Same family — chaos |
| **Sunset obligation denial** | Legacy product; no export path | `CTR_SUNSET` / `CTR_INVESTMENT` gap | `CTR_SUNSET`, `CTR_INVESTMENT` |
| **Pilot ops obligation gap** | Real users; no support contract | `CTR_OPERATIONS` lite absent | `CTR_OPERATIONS`, `CTR_TRUST_SAFETY` |
| **Commercial obligation jump** | First payment in Production | `CTR_COMMERCIAL` without pilot path | `CTR_COMMERCIAL`, `CTR_TRUST_SAFETY` |
| **Lifecycle label lie** | Beta badge 2 years; Production ops absent | `CTR_LIFECYCLE` violated | `CTR_LIFECYCLE`, `CTR_RELEASE` |

---

## 11. Contract Anti-Chaos Rules

Human-operated v1 safeguards. **Not** automated enforcement.

| ID | Rule | Prevents |
|----|------|----------|
| **AC-C1** | Every dominant contract of current `lifecycle_state_code` must be crystallized or marked SAFE UNKNOWN | Obligation vacuum |
| **AC-C2** | No `CTR_ARCHITECTURE` at `CW_CRITICAL` before `CTR_CLASSIFICATION` binding | Architecture obligation too early |
| **AC-C3** | Extended class: `CTR_COMPLIANCE` and `CTR_TRUST_SAFETY` cannot remain implicit past `LC_DISCOVERY` | False compliance obligation |
| **AC-C4** | `CTR_LIFECYCLE` Production claim requires named `DEC_LIFECYCLE_TRANSITION` — not inferred from ship | Release = stage obligation confusion |
| **AC-C5** | Same `contract_type_code` at `CW_STRUCTURAL`+ requires lifecycle or tier trigger to reopen | Obligation churn |
| **AC-C6** | Tasks/tickets cannot satisfy contract gaps — name `contract_type_code` | Hidden commitments |
| **AC-C7** | `CTR_SCOPE` must be crystallized before `LC_PROOF` build obligation | Scope obligation inflation |
| **AC-C8** | Weight class must be declared for `CW_CRITICAL` and `CW_BINDING` contracts | Fake contract certainty |
| **AC-C9** | Pilot with real users requires lite `CTR_OPERATIONS` crystallization | Pilot ops obligation gap |
| **AC-C10** | `CTR_PRODUCT` pivot requires `CTR_LIFECYCLE` transition obligation review | Random pivot obligations |
| **AC-C11** | One contract family per obligation event — no mega-contracts bundling unrelated domains | Contract inflation |
| **AC-C12** | `CTR_CLASSIFICATION` re-review on tier bump or payments/PII/regulated feature | Classification obligation drift |
| **AC-C13** | Undocumented `CW_CRITICAL`+ contract = SAFE UNKNOWN in REPORT | Silent critical obligations |
| **AC-C14** | `UTILITY_TOOL` T1 exempt from commercial/compliance contracts until trigger feature | Over-engineering obligations |
| **AC-C15** | Store/public release activates `CTR_RELEASE` + often `CTR_LIFECYCLE` — never implicit | AC-L10 lifecycle analog |
| **AC-C16** | Legal document alone does not satisfy contract — implementation must honor obligation | Doc ≠ obligation confusion |
| **AC-C17** | Every `contract_type_code` must trace to `source_decision_type_code` | Decisionless contracts |
| **AC-C18** | Duplicate obligation statements for same contract family require reconciliation | Duplicated obligations |

---

## 12. Contract Relationships

### 12.1 Dependency chain

```text
┌─────────────────────────────────────────────────────────────┐
│                    REALITY LAYER (NOVA)                      │
├─────────────────────────────────────────────────────────────┤
│  Production Model v1                                         │
│  Product Taxonomy v1                                         │
│  Product Class Registry v1  ──► product_class_code           │
│  Lifecycle Model v1         ──► lifecycle_state_code         │
│  Decision Reality Model v1  ──► decision_type_code           │
│  Contract Reality Model v1  ──► contract_type_code     ◄── HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ obligations ready for validation design
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW (future)                         │
│  Gates · templates · records · enforcement process           │
└───────────────────────────────┬─────────────────────────────┘
                                ▼
                         Roles · Tools · Agents · Automation
```

### 12.2 Why contracts require all previous layers

| Input | Provides | Without it |
|-------|----------|------------|
| **`product_class_code`** | Which contract families are material; default weights | Payment obligations on offline utility |
| **`lifecycle_state_code`** | Which contracts are dominant now; verification depth | Full compliance pack at Concept |
| **`decision_type_code`** | Which choices create obligations | Generic checklist obligations |
| **`contract_type_code`** | The actual obligation domain | Workflow validates wrong things |

**Combined pressure function (conceptual, not algorithm):**

```text
contract_pressure(contract_type_code, product_class_code, lifecycle_state_code, source_decision_type_code, tier)
  → pressure_rank ∈ { dormant, latent, active, dominant }
  → effective_weight_class
  → verification_expectation_level
```

**Examples:**

| Context | Pressure outcome |
|---------|------------------|
| `CTR_COMMERCIAL` + `UTILITY_TOOL` + `LC_PROOF` + T1 | Dormant unless monetization trigger |
| `CTR_COMMERCIAL` + `COMMERCE` + `LC_PILOT` + T3 | Dominant; V2 real transactions |
| `CTR_ARCHITECTURE` + `AI_AGENT_CONSOLE` + `LC_DISCOVERY` + T4 | Active descriptive; not critical until Proof exit |
| `CTR_SUNSET` + `HEALTH_MEDICAL` + `LC_SUNSET` + T4 | Dominant; `CW_BINDING`; V3 retention |

### 12.3 Cross-layer binding (conceptual instance)

```text
nova_obligation_context {
  product_class_code,           // registry
  complexity_tier,              // registry / intake
  lifecycle_state_code,         // lifecycle
  decision_type_code,           // source decision
  contract_type_code,           // crystallized obligation
  effective_weight_class,       // CW_*
  verification_expectation_level // V0–V3
}
```

### 12.4 Cross-contract dependencies (reality, not workflow)

| Upstream contract | Downstream contracts constrained |
|-------------------|----------------------------------|
| `CTR_CLASSIFICATION` | All commitment-layer contracts |
| `CTR_PRODUCT` | `CTR_SCOPE`, `CTR_UX`, `CTR_AUDIENCE` |
| `CTR_SCOPE` | `CTR_ARCHITECTURE` depth, `CTR_UX` surface |
| `CTR_DATA_PRIVACY` | `CTR_COMPLIANCE`, `CTR_SUNSET` |
| `CTR_LIFECYCLE` | Which contracts must be crystallized before stage claim |
| `CTR_EXPANSION` | Re-opens `CTR_COMPLIANCE`, `CTR_ARCHITECTURE`, `CTR_TRUST_SAFETY` |

---

## 13. Contract Reality Boundaries

### 13.1 What is NOT a contract

| Not a contract | Why | Correct layer |
|----------------|-----|---------------|
| **Task** | Execution unit; may fulfill obligation but is not obligation | Workflow / Production Model |
| **Ticket / issue** | Tracking artifact | Tooling — may reference contracts |
| **Feature** | Scoped implementation inside product | Execution inside `CTR_SCOPE` |
| **Bug** | Defect against existing obligation | QA / maintenance |
| **Meeting** | Process | May surface obligations; not contract |
| **Approval** | Authority act | Roles + Workflow (future) |
| **Gate pass/fail** | Workflow enforcement outcome | Workflow — validates contract |
| **Legal document** | Expression of obligation | Templates (future); `CTR_*` is obligation |
| **Checklist item** | Process step | Workflow unless maps to `CTR_*` |
| **QA test case** | Verification artifact | May evidence contract satisfaction |
| **Sprint commitment** | Team scheduling | Workflow |
| **Release build** | Event | May test `CTR_RELEASE`; build is execution |
| **Store submission** | Event | Informs evidence for `CTR_LIFECYCLE` |
| **ADR document** | Decision record format | Future Decision Records; `CTR_ARCHITECTURE` is obligation |
| **Template** | Reusable document pattern | Explicitly NOT this layer |
| **P-phase completion** | Production Model milestone | Orthogonal to contract types |
| **Metric** | Evidence | Feeds verification; not contract |

### 13.2 Boundary tests

Apply before labeling something a contract:

1. **Decision-origin test:** Traces to `decision_type_code`?
2. **Persistence test:** Must remain true until decision revised?
3. **Consequence test:** Violation harms users, legal, ops, or integrity?
4. **Verifiability test:** Satisfied/violated determinable without knowing process?

### 13.3 Common misuse prevention

| Misuse | Correction |
|--------|------------|
| «Legal signed = compliant» | Signature is workflow; `CTR_COMPLIANCE` is obligation honored in product |
| «Checklist complete = contract satisfied» | Checklist validates; contract is what must be true |
| «We have a privacy policy» | Policy expresses; `CTR_DATA_PRIVACY` requires implementation match |
| «Shipped = obligations met» | Ship is event; contracts may still be violated |
| «Template filled = contract exists» | Template is expression; obligation exists from decision |
| «Jira epic = architecture contract» | Epic tracks work; `CTR_ARCHITECTURE` is structural honor |

---

## 14. Contract Weight vs Decision Weight

Decision weight (`DW_*`) and contract weight (`CW_*`) are **related but not identical**. Decisions choose; contracts obligate. Weight models answer different questions.

### 14.1 Relationship model

```text
DECISION (choice)                    CONTRACT (obligation)
     │                                       │
     ▼                                       ▼
 decision_weight_class              contract_weight_class
 (impact of choosing)               (impact of violating)
     │                                       │
     └─────────── typically correlates ──────┘
                 but can diverge
```

### 14.2 Can a high-weight decision create a low-weight contract?

**Yes — in early lifecycle or narrow scope.**

| Example | Decision weight | Contract weight | Why diverge |
|---------|-----------------|-----------------|-------------|
| `DEC_ARCHITECTURE` spike-only at Discovery | `DW_STRUCTURAL` (choice matters) | `CW_DESCRIPTIVE` or `CW_OPERATIONAL` | Obligation is «honor spike conclusions», not production stack |
| `DEC_AUDIENCE` internal-only | `DW_LOCAL` | `CW_DESCRIPTIVE` | Limited external exposure |
| `DEC_EXISTENCE` continue at Concept | `DW_STRUCTURAL` | `CW_OPERATIONAL` | Choice heavy; obligation is portfolio honesty, low external bind |
| `DEC_SCOPE` within Proof phase | `DW_STRUCTURAL` | `CW_OPERATIONAL` | Boundary matters; violation recoverable within phase |

**Rule:** High decision weight + early stage + narrow external surface → contract weight may **lag** decision weight until lifecycle advance crystallizes full obligation.

### 14.3 Can multiple low-weight decisions create a high-weight contract?

**Yes — through accumulation and externalization.**

| Example | Decisions | Combined contract | Why elevate |
|---------|-----------|-------------------|-------------|
| PII collection + store listing + pilot users | `DEC_DATA_PRIVACY` (local) + `DEC_RELEASE` (local) + `DEC_AUDIENCE` (local) | `CTR_DATA_PRIVACY` + `CTR_COMPLIANCE` at `CW_CRITICAL` | Combined external exposure |
| Payment stub + refund policy sketch + pilot money | `DEC_COMMERCIAL` (local) × steps | `CTR_COMMERCIAL` at `CW_CRITICAL` | Real money crystallizes |
| Companion parity + parent API + mobile release | `DEC_ECOSYSTEM` + `DEC_RELEASE` (each moderate) | `CTR_ECOSYSTEM` at `CW_STRUCTURAL`+ | Integration obligations compound |
| Legacy neglect signals | `DEC_INVESTMENT` (low) + `DEC_EXISTENCE` (low) | `CTR_INVESTMENT` + security obligations implicit | Accumulated neglect → `CW_CRITICAL` security debt |

**Rule:** Multiple `DW_LOCAL` decisions in same domain that **externalize** (users, money, regulators) → contract weight **elevates above** any single decision weight.

### 14.4 Weight correspondence table (default)

| Decision weight | Typical contract weight | Divergence trigger |
|-----------------|------------------------|-------------------|
| `DW_NEGLIGIBLE` | `CW_DESCRIPTIVE` | Rare divergence |
| `DW_LOCAL` | `CW_DESCRIPTIVE` – `CW_OPERATIONAL` | Externalization elevates contract |
| `DW_STRUCTURAL` | `CW_OPERATIONAL` – `CW_STRUCTURAL` | Early stage lowers contract |
| `DW_COMMITMENT` | `CW_STRUCTURAL` – `CW_CRITICAL` | Stage advance required for full critical |
| `DW_IRREVERSIBLE` | `CW_CRITICAL` – `CW_BINDING` | Usually aligned |

### 14.5 Anti-confusion

| Confusion | Resolution |
|-----------|------------|
| «Heavy decision = heavy contract always» | Check lifecycle stage and external surface |
| «Light contract = optional obligation» | `CW_DESCRIPTIVE` still exists; low verification ≠ optional honor |
| «Contract weight set by document size» | Weight from impact radius, not pages |
| «Decision reopened = contract auto-reopened» | AC-C5 requires explicit trigger |

---

## 15. RBM Mapping

```text
Reality
├── Production Model v1        … what NOVA is
├── Product Taxonomy v1        … what classes exist
├── Product Class Registry v1  … what each class means operationally
├── Lifecycle Model v1         … where the product is in life
├── Decision Reality Model v1  … what decisions exist in product nature
└── Contract Reality Model v1  … what obligations exist because of decisions  ◄── completes Contracts band vocabulary
        │
        ▼
Workflow                       … how obligations are validated and work executed (future)
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

### 15.1 Why Contract Reality is the final descriptive layer before execution

| Order | Reason |
|-------|--------|
| **Reality before Lifecycle** | Must know product identity before temporal obligation depth |
| **Lifecycle before Decisions** | Stage determines which choices are structurally active |
| **Decisions before Contracts** | Obligations crystallize from choices — not from templates |
| **Contracts before Workflow** | Workflow validates and executes against known obligation structure |
| **Contracts before Roles** | Role assignment requires obligation domain vocabulary |
| **Contracts before Tools** | Helpers assist obligation verification — not invent obligations |
| **Not before Decisions** | Contract without decision origin is fake contract (AC-C17) |

**Completion of descriptive RBM band:** After this artifact, NOVA knows **identity** (registry), **time** (lifecycle), **choice structure** (decisions), and **commitment structure** (contracts). Downstream execution layers can anchor to `{ product_class × lifecycle × decision × contract }` instead of guessing.

**Explicitly NOT in Contracts band:** templates, approval chains, gate automation, contract storage, legal drafting, enforcement engines.

### 15.2 Execution-oriented layers (future — not designed here)

| Layer | Will consume from Contract Reality |
|-------|-------------------------------------|
| **Workflow** | Verification levels V0–V3; gate design per `contract_type_code` |
| **Roles** | Obligation ownership per contract family |
| **Tools** | Helpers for obligation alignment checks |
| **Agents** | Only if human-operated verification insufficient — not assumed |
| **Automation** | Last — only after obligation structure proven stable |

---

## 16. Risks

| Risk | Severity | Mitigation in v1 |
|------|----------|------------------|
| Contract Reality confused with legal template system | High | Scope boundary; §13; AC-C16 |
| Contract Reality confused with workflow gates | High | §2.4; `is_workflow_gate` always false |
| Contract inflation (too many types) | Medium | 18 families with rejection table §3.1; AC-C11 |
| Contract confused with checklist | Medium | §13.1; boundary tests |
| Weight class used as avoidance lever | Medium | Derived criteria §9; AC-C8 |
| Lifecycle-contract conflation | High | Separate codes; AC-C4; matrix §7 |
| Class matrix oversimplification | Medium | Tier modifier §8.1; SAFE UNKNOWN |
| Silent critical obligations | High | AC-C13; failure patterns §10 |
| Decision-contract 1:1 oversimplification | Medium | Secondary activations §6.2 |
| Governance expansion drift | Medium | No Roles/Gates/Templates in v1; RBM §15 |
| Prior foundation files not all in-repo | Medium | Cross-reference existing docs; commit pack optional |
| Human enforcement fatigue | Medium | 18 anti-chaos rules only; not automation pretense |

---

## 17. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Exact numeric mapping contract weight → gate depth | First NOVA Workflow v1 charter |
| Whether `CTR_ECOSYSTEM` splits intent vs deployed in v2 | First companion + ORCA-style dual-domain product |
| Machine format for `contract_pressure_instance` | Future intake schema |
| Regional regulatory sub-contracts under `CTR_COMPLIANCE` | Legal charter per geo |
| Overlap with MARS survivability protected zones | NOVA ↔ MARS integration workflow |
| Optimal count of contract families (18 vs consolidated) | Operator feedback after 2–3 products |
| Prior Production Model / Taxonomy / Registry markdown in-repo | Human commit of foundation pack |
| Contract Records vs Contract Templates layer split | Future charter after Workflow design |
| Whether implicit obligations get formal `obligation_status` enum | First workflow pilot |
| AI agent obligation domains beyond `CTR_TRUST_SAFETY` | First `AI_AGENT_CONSOLE` production pilot |

**Non-claims preserved:** this model does not assert contract storage, template libraries, automated gates, approval chains, legal drafting, or agent enforcement.

---

## 18. Recommended Next Step

**Single next artifact:** `NOVA WORKFLOW REALITY MODEL v1` (or phased Workflow charter) — first execution-oriented layer **after** Contract Reality, defining:

- how obligations at V0–V3 are verified in human-operated process
- gate semantics bound to `contract_type_code × effective_weight_class`
- explicit separation from Contract Templates and Roles

**Do not skip to:** Contract Templates, Approval Systems, Contract Records storage, Roles, Core Run, Agents, or Automation until Workflow charter approved — or human explicitly charters a different next layer.

**Optional parallel (human choice):** commit full NOVA foundation pack to `projects/nova/foundation/`:

- `NOVA-PRODUCTION-MODEL-v1.md`
- `NOVA-MOBILE-PRODUCT-TAXONOMY-v1.md`
- `NOVA-PRODUCT-CLASS-REGISTRY-v1.md`
- `NOVA-MOBILE-PRODUCT-LIFECYCLE-MODEL-v1.md`
- `NOVA-DECISION-REALITY-MODEL-v1.md`
- `NOVA-CONTRACT-REALITY-MODEL-v1.md` (this file)

**Prior artifact update (optional):** Decision Reality Model §17 Recommended Next Step — mark Contract Reality as complete; point to Workflow as next.

---

## Appendix A — Contract Pressure Snapshot template

```markdown
# Contract Pressure Snapshot — [PRODUCT] — [DATE]

product_class_code:
complexity_tier:
lifecycle_state_code:

| contract_type_code | pressure_rank | effective_weight | verification_level | crystallized? |
|--------------------|---------------|------------------|--------------------|---------------|
| CTR_EXISTENCE      |               |                  |                    | Y/N/UNK       |
| ...                |               |                  |                    |               |

Source decisions mapped:
Implicit or violated obligations:
SAFE UNKNOWN contracts:
```

---

## Appendix B — RBM layer completion status (NOVA v1)

| RBM layer | Artifact | Status |
|-----------|----------|--------|
| Reality | Production Model, Taxonomy, Registry, Lifecycle | Substantially established (design sessions) |
| Decisions | Decision Reality Model v1 | Complete |
| **Contracts** | **Contract Reality Model v1** | **This document — vocabulary complete** |
| Workflow | Production Model P0–P12 execution binding | Planned |
| Roles | — | Not started |
| Tools | — | Not started |
| Agents | — | Not started |
| Automation | — | Not started |

---

**Document status:** v1 design complete — Reality-layer contract vocabulary for NOVA mobile products. Nothing beyond Contract Reality.
