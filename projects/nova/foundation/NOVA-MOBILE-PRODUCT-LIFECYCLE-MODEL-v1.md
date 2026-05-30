# NOVA Mobile Product Lifecycle Model v1

**Status:** design-only — Reality-layer lifecycle vocabulary, not runtime, not workflow engine, not decision system  
**Lane:** B · External Systems  
**Version:** v1  
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → NOVA Product Class Registry v1 → **this document**  
**Non-claims:** no agents, no orchestration, no automated lifecycle enforcement, no database schema, no folder structure

**Parent Reality artifacts (conceptually approved; prior design sessions):**

- NOVA Production Model v1 — execution phases P0–P12 (orthogonal to this model)
- NOVA Mobile Product Taxonomy v1 — classification vocabulary
- NOVA Product Class Registry v1 — operational defaults per `product_class_code`

**Evidence base:** Website Factory delivery-survivability and production-readiness patterns; ORCA artifact lifecycle and approval gates; MARS survivability freeze/rollback discipline

---

## 1. Executive Summary

NOVA Mobile Product Lifecycle Model v1 — **первый lifecycle artifact NOVA**. Он отвечает на вопрос:

> **«Где продукт находится в своей жизни?»**

Не «как мы его строим» (Production Model P0–P12), не «какой sprint идёт», не «как агент работает».

| Элемент | Содержание |
|---------|------------|
| **9 canonical lifecycle stages** | `LC_CONCEPT` → `LC_SUNSET` |
| **8 forward transitions** | С evidence, approvals, failure modes |
| **9 lifecycle state registry rows** | `lifecycle_state_code` + maturity, uncertainty, doc/QA/release posture |
| **Class impact matrix** | 15 product classes × lifecycle behavior |
| **Tier impact rules** | T1–T4 influence duration, validation depth, skip rules |
| **Decision pressure map** | Critical decisions per stage (future Decision System consumes) |
| **Evolution models** | Documentation · QA · Release progression |
| **Anti-chaos + failure patterns** | Operational safeguards derived from MARS lessons |

**Ключевое различие:**

| Dimension | Product Lifecycle (this doc) | Production Model (P0–P12) |
|-----------|------------------------------|---------------------------|
| **Question** | Where is the product in its market/operational life? | How does NOVA execute the next production step? |
| **Layer** | Reality → Lifecycle | Workflow / execution machinery (future) |
| **Example state** | `LC_PILOT` — controlled real-user learning | `P10` — validation & device QA |
| **Orthogonal** | One product in `LC_PROOF` may be in `P9` build | One product in `LC_PRODUCTION` may be in `P12` evolution |

**Registry answered:** «What is the product?» (`product_class_code`)  
**Lifecycle answers:** «Where is the product in its life?» (`lifecycle_state_code`)

Without lifecycle, decisions become random, contracts generic, QA unfocused, releases inconsistent.

---

## 2. Lifecycle Philosophy

### 2.1 Why lifecycle exists

Mobile products **не рождаются в Production** и **не умирают мгновенно**. Они проходят фазы, где:

- uncertainty снижается постепенно;
- documentation depth растёт по необходимости, не «всё сразу»;
- QA focus меняется (assumption → usability → regression → compliance);
- release posture эволюционирует (none → controlled → public → governed).

Lifecycle — **shared temporal vocabulary** для product owner, NOVA operator, legal, QA и future contracts. Без него «MVP», «production», «pilot» становятся **субъективными ярлыками**.

### 2.2 Why RBM requires lifecycle before Decisions

RBM chain:

```text
Reality → Lifecycle → Decisions → Contracts → Workflow → Roles → Tools → Agents → Automation
```

**Reality Layer** фиксирует *что существует*:

1. Production Model — что такое NOVA
2. Taxonomy — какие классы продуктов существуют
3. Registry — что каждый класс означает операционно
4. **Lifecycle** — в какой фазе жизни находится конкретный продукт

**Decisions** без lifecycle не знают **pressure context**:

- в `LC_CONCEPT` критично «строить ли вообще»;
- в `LC_PILOT` критично «продолжать ли масштабирование»;
- в `LC_PRODUCTION` критично «готовы ли к compliance expansion».

Lifecycle — **не execution artifact**, потому что описывает **состояние продукта в мире**, а не **действие команды**. Команда может быть в P8 freeze, пока продукт всё ещё в `LC_PILOT`.

### 2.3 Relationship to taxonomy

| Taxonomy | Lifecycle |
|----------|-----------|
| Static classification vocabulary | Dynamic temporal state |
| «What species is this product?» | «How mature is this product's existence?» |
| `product_class_code` stable across life | `lifecycle_state_code` changes over time |
| Defines *different* production defaults by class | Defines *different* expectations at each life stage |
| Hybrid: primary + secondary class | One primary lifecycle state; optional overlay flags |

**Interaction:** один `COMMERCE` T3 продукт проходит те же lifecycle stages, что и `UTILITY_TOOL` T1, но **duration, evidence, QA depth и skip rules** differ (see §6–§7).

### 2.4 Relationship to registry

Registry row `critical_lifecycle_areas` (conceptual phase names from registry design) **map to lifecycle pressure zones**, not lifecycle stages themselves:

| Registry field | Lifecycle consumption |
|----------------|----------------------|
| `critical_lifecycle_areas` | Which transitions need class-specific evidence |
| `qa_priorities` | Weight QA evolution model per stage |
| `release_priorities` | Weight release evolution model per stage |
| `common_failure_patterns` | Inform lifecycle failure patterns |
| `default_tier` | Inform tier impact rules |

**Binding record (future):** `product_class_record` + `lifecycle_state_record` — instance, not registry row.

### 2.5 Why lifecycle is Reality, not execution

| Reality artifact | Execution artifact (NOT this) |
|------------------|-------------------------------|
| Describes product state independent of team activity | Describes tasks, sprints, pipelines |
| Survives team change | Resets when project restarts |
| Answers «where in life» | Answers «what to do next» |
| Required before decision rules | Consumed by workflow after decisions |

**Website Factory lesson:** production-readiness drift occurs when **delivery state** (`done`, `frozen`) is confused with **product survivability state** ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)). Lifecycle prevents the same confusion for mobile: **store submission ≠ product maturity**.

**ORCA lesson:** artifact states (`draft` → `approved` → `factory-ready`) govern **handoff readiness**, not **market maturity** ([`artifact-lifecycle-v0.md`](../../orca/content-packs/artifact-lifecycle-v0.md)). NOVA lifecycle is the product-side analogue at a higher abstraction.

---

## 3. Canonical Lifecycle Stages

### 3.1 Derivation rationale

Startup frameworks (Concept → MVP → PMF → Scale) **over-index on venture growth** and **under-specify**:

- enterprise/internal products that never «grow»;
- companion apps entering mid-life;
- regulated products requiring proof before pilot;
- utilities that reach production quickly without pilot.

**Derived stages** test: *«Does NOVA treat QA, release, and documentation differently at this point?»*

Rejected as standalone stages:

| Rejected | Reason | Placement |
|----------|--------|-----------|
| **MVP** (as stage name) | Ambiguous — means artifact, scope, and stage simultaneously | → `LC_PROOF` stage; «MVP» = scope label inside Proof |
| **Development** | Execution, not product life | → Production Model P9 |
| **Architecture** | Execution milestone | → Production Model P6; pressure in `LC_DISCOVERY`/`LC_PROOF` |
| **Store Review** | Release event | → Release evolution within stage |
| **PMF** | Outcome metric, not operable stage | → exit evidence for `LC_PILOT` → `LC_PRODUCTION` |

### 3.2 Stage overview

```text
LC_CONCEPT → LC_DISCOVERY → LC_PROOF → LC_PILOT → LC_PRODUCTION
                                                      ↓
                              LC_GROWTH ↔ LC_MATURE → LC_LEGACY → LC_SUNSET
```

**Lateral state (not a forward stage):** `LC_HOLD` — product intentionally paused; may resume at same or earlier stage with re-validation charter.

---

### 3.3 Stage definitions

#### `LC_CONCEPT`

| Field | Value |
|-------|-------|
| **Purpose** | Capture product intent before commitment of definition resources |
| **Entry condition** | Stakeholder articulates a product idea worth tracking |
| **Exit condition** | Product hypothesis charter drafted; decision to investigate (`→ LC_DISCOVERY`) or abandon |
| **Primary risks** | Solution-first thinking; hidden executive mandate; class misguess |
| **Typical duration** | Days–4 weeks |
| **Typical objectives** | Name the problem; identify candidate class; reject or advance |

---

#### `LC_DISCOVERY`

| Field | Value |
|-------|-------|
| **Purpose** | Validate problem, audience, feasibility, and class/tier before build commitment |
| **Entry condition** | Charter to investigate; G0-equivalent product owner intent (future Decision System) |
| **Exit condition** | Product definition hypothesis + class/tier binding + build/no-build recommendation |
| **Primary risks** | Analysis paralysis; skipping class binding; competitive copy without differentiation |
| **Typical duration** | 2–8 weeks |
| **Typical objectives** | User/market evidence; distribution strategy sketch; tier estimate; kill or advance to Proof |

---

#### `LC_PROOF`

| Field | Value |
|-------|-------|
| **Purpose** | Test **core product hypothesis** with minimum credible product artifact |
| **Entry condition** | Approved product definition boundary; scope labeled «proof» not «production» |
| **Exit condition** | Hypothesis supported/refuted with evidence; advance to Pilot, iterate Proof, or kill |
| **Primary risks** | Proof scope inflation; fake validation (internal-only cheerleading); architecture for scale too early |
| **Typical duration** | 3–12 weeks (class/tier dependent) |
| **Typical objectives** | Demonstrate core value path; measure task completion; expose fatal UX/tech blockers |

**Terminology:** «MVP» may describe **scope** inside Proof; it is **not** a lifecycle stage code.

---

#### `LC_PILOT`

| Field | Value |
|-------|-------|
| **Purpose** | Learn from **controlled real-world use** with explicit success/fail criteria |
| **Entry condition** | Proof evidence; pilot charter (audience, geography, duration, metrics, rollback) |
| **Exit condition** | Pilot metrics evaluated; advance to Production, extend pilot, or retreat to Proof |
| **Primary risks** | Endless pilot; pilot audience unrepresentative; production ops disguised as pilot |
| **Typical duration** | 4–16 weeks (often 1–3 release cycles) |
| **Typical objectives** | Adoption signal; operational friction discovery; support load; compliance gaps |

---

#### `LC_PRODUCTION`

| Field | Value |
|-------|-------|
| **Purpose** | Product serves **intended audience** at operational baseline — not experimental posture |
| **Entry condition** | Pilot success evidence **or** class-valid skip path (see §6–§7); operational readiness |
| **Exit condition** | Deliberate expansion charter (`→ LC_GROWTH`) **or** stabilization without growth (`→ LC_MATURE`) |
| **Primary risks** | Premature production (no proof); fake production (pilot with store badge); ops debt |
| **Typical duration** | Months–years (stable state until expansion or decay) |
| **Typical objectives** | Reliable core journeys; supportability; baseline compliance; survivable release cadence |

---

#### `LC_GROWTH`

| Field | Value |
|-------|-------|
| **Purpose** | Active expansion — users, markets, monetization, surface area — under governance |
| **Entry condition** | Explicit growth charter; Production baseline stable; capacity for increased QA/release load |
| **Exit condition** | Growth KPIs plateau; shift to optimization (`→ LC_MATURE`) or failed expansion retreat |
| **Primary risks** | Feature explosion; geographic/compliance overreach; architecture strain |
| **Typical duration** | 6 months–3 years |
| **Typical objectives** | Acquisition/retention; market expansion; monetization depth; platform leverage |

**Note:** Internal/enterprise products may **never enter** Growth — valid path: `LC_PRODUCTION` → `LC_MATURE`.

---

#### `LC_MATURE`

| Field | Value |
|-------|-------|
| **Purpose** | Stable product; incremental improvement; efficiency over novelty |
| **Entry condition** | Growth plateau **or** Production stable without growth intent |
| **Exit condition** | Strategic refresh (`→ LC_GROWTH` with charter) **or** investment withdrawal (`→ LC_LEGACY`) |
| **Primary risks** | Stagnation masked as stability; security/compliance drift; team neglect |
| **Typical duration** | Years |
| **Typical objectives** | Retention; reliability; cost efficiency; selective enhancement |

---

#### `LC_LEGACY`

| Field | Value |
|-------|-------|
| **Purpose** | Maintenance-only; no active product investment; compatibility preserved |
| **Entry condition** | Explicit legacy declaration; successor named or N/A documented |
| **Exit condition** | Sunset charter (`→ LC_SUNSET`) or unexpected revival (requires re-discovery) |
| **Primary risks** | Silent legacy (no owner); security rot; store policy violations unaddressed |
| **Typical duration** | Months–years |
| **Typical objectives** | Critical bugfixes; OS compatibility; data export; user communication |

---

#### `LC_SUNSET`

| Field | Value |
|-------|-------|
| **Purpose** | Intentional end-of-life with user/data migration path |
| **Entry condition** | Sunset decision; timeline; migration/export plan |
| **Exit condition** | Decommission complete; archives per retention policy |
| **Primary risks** | Abrupt shutdown; data loss; regulatory retention violation |
| **Typical duration** | 1–6 months (regulated: longer) |
| **Typical objectives** | User notification; data export; store removal; support wind-down |

---

## 4. Stage Transition Model

### 4.1 Transition principles

1. **Forward transitions require evidence** — not enthusiasm.
2. **Skip transitions require class + tier validated path** — documented waiver.
3. **Backward transitions are allowed** — with explicit regression charter (ORCA freeze lesson: rollback is discipline, not failure).
4. **Hold is lateral** — `LC_HOLD` pauses clock; re-entry requires stale-evidence review.
5. **Production Model phases run inside lifecycle stages** — completing P11 ≠ automatic `LC_PRODUCTION`.

### 4.2 Transition matrix

| From → To | Required evidence | Required approvals | Common failure modes |
|-----------|-------------------|------------------|----------------------|
| **CONCEPT → DISCOVERY** | Problem statement; sponsor; rough class hypothesis | Product owner intent | Pet project without sponsor |
| **DISCOVERY → PROOF** | Product definition hypothesis; `product_class_record` draft; tier estimate; distribution sketch | Product owner + NOVA operator | Build before class binding |
| **DISCOVERY → HOLD/KILL** | Kill/hold rationale documented | Product owner | Endless discovery |
| **PROOF → PILOT** | Core hypothesis test results; critical journey demo; known gaps list | Product owner + QA lead (conceptual) | Demo ≠ proof |
| **PROOF → DISCOVERY** | Hypothesis refuted; pivot scope | Product owner | Ego-driven iteration |
| **PROOF → KILL** | Evidence product should not exist | Product owner | Sunk-cost continuation |
| **PILOT → PRODUCTION** | Pilot metrics vs charter; ops readiness; support path; compliance baseline | Product owner + release authority | Pilot forever; vanity metrics |
| **PILOT → PROOF** | Fundamental hypothesis failure; major pivot | Product owner | Band-aid on wrong product |
| **PRODUCTION → GROWTH** | Stable core metrics; growth charter; capacity plan | Product owner + stakeholder | Feature factory without baseline |
| **PRODUCTION → MATURE** | No growth intent; stable ops | Product owner | Skipping straight to neglect |
| **GROWTH → MATURE** | KPI plateau; strategic shift to efficiency | Product owner | Denial of plateau |
| **MATURE → GROWTH** | Refresh charter; new market/feature thesis | Product owner + stakeholder | Zombie growth |
| **MATURE → LEGACY** | Investment withdrawal decision | Product owner + exec | Accidental legacy |
| **LEGACY → SUNSET** | Sunset plan; user comms draft; data handling | Product owner + legal (if regulated) | Store abandonment without notice |
| **ANY → HOLD** | Hold reason; re-entry conditions | Product owner | Stealth pause |
| **HOLD → prior stage** | Staleness review; evidence still valid | Product owner | Stale assumptions |

### 4.3 High-risk transitions (extra gates)

#### `LC_PROOF → LC_PRODUCTION` (skip pilot)

**Default:** **forbidden** unless skip path validated.

| Skip allowed when | Extra evidence |
|-------------------|----------------|
| `UTILITY_TOOL` T1, single-user, no PII | Usability validation report; device smoke |
| `COMPANION` with production parent | Parent product already in Production; parity charter |
| Internal enterprise `PRODUCTIVITY_WORKFLOW` MDM-only | Security review; MDM deployment proof |

**Always forbidden skip:** `COMMERCE`, `MARKETPLACE`, `FINTECH_WALLET`, `HEALTH_MEDICAL`, `AI_AGENT_CONSOLE`, any T4.

#### `LC_PILOT → LC_PRODUCTION`

| Evidence type | Minimum content |
|---------------|-----------------|
| **Adoption** | Real users (not team) completed core journey at agreed rate |
| **Operations** | Support path, monitoring, rollback tested |
| **Compliance** | Privacy labels, permissions, legal posture for class |
| **Quality** | No open critical/blocker on core journeys |
| **Survivability** | Handoff/onboarding docs exist (Factory delivery-survivability lesson) |

#### `LC_PRODUCTION → LC_GROWTH`

| Evidence type | Minimum content |
|---------------|-----------------|
| **Stability** | N release cycles without core regression |
| **Charter** | What expands (geo, features, segments) |
| **Capacity** | QA/release/legal load acknowledged |

### 4.4 Wishful progression prevention

| Anti-pattern | Guard |
|--------------|-------|
| «We shipped to store» = Production | Store presence is release event; Production requires ops evidence |
| «It's MVP» after 12 months | Scope label ≠ lifecycle; re-classify or advance stage |
| «Pilot» with full marketing spend | Pilot charter caps acquisition; excess → Production claim audit |
| Executive demo → Production | Demo audience ≠ pilot audience |

---

## 5. Lifecycle State Registry

Canonical codes parallel to `product_class_code`. Immutable after v1 freeze.

### 5.1 Registry rows

#### `LC_CONCEPT`

| Field | Value |
|-------|-------|
| **code** | `LC_CONCEPT` |
| **definition** | Product intent exists; no committed investigation or build |
| **maturity_level** | 0 |
| **expected_uncertainty** | Very high |
| **expected_documentation_depth** | Idea brief (1–3 pages); no architecture |
| **expected_qa_depth** | None on product; assumption listing only |
| **expected_release_posture** | None |

---

#### `LC_DISCOVERY`

| Field | Value |
|-------|-------|
| **code** | `LC_DISCOVERY` |
| **definition** | Active investigation of problem, audience, feasibility, class |
| **maturity_level** | 1 |
| **expected_uncertainty** | High |
| **expected_documentation_depth** | Discovery brief; class hypothesis; competitor/feasibility notes |
| **expected_qa_depth** | Assumption validation; no product QA matrix |
| **expected_release_posture** | None |

---

#### `LC_PROOF`

| Field | Value |
|-------|-------|
| **code** | `LC_PROOF` |
| **definition** | Minimum product testing core hypothesis |
| **maturity_level** | 2 |
| **expected_uncertainty** | Medium–high |
| **expected_documentation_depth** | Proof scope doc; journey map (core path); known gaps |
| **expected_qa_depth** | Core journey functional; usability spot-check; device smoke |
| **expected_release_posture** | Internal/test track only; no public store unless chartered test |

---

#### `LC_PILOT`

| Field | Value |
|-------|-------|
| **code** | `LC_PILOT` |
| **definition** | Controlled real-world deployment with learning posture |
| **maturity_level** | 3 |
| **expected_uncertainty** | Medium |
| **expected_documentation_depth** | Pilot charter; metrics definition; support playbook (lite) |
| **expected_qa_depth** | Core + pilot-scope regression; pilot-specific edge cases |
| **expected_release_posture** | Controlled release (TestFlight, closed track, MDM cohort, geo fence) |

---

#### `LC_PRODUCTION`

| Field | Value |
|-------|-------|
| **code** | `LC_PRODUCTION` |
| **definition** | Full operational deployment for intended audience |
| **maturity_level** | 4 |
| **expected_uncertainty** | Low–medium |
| **expected_documentation_depth** | Operational docs; runbooks; legal baseline; architecture record |
| **expected_qa_depth** | Full class QA matrix; regression suite; release candidate gate |
| **expected_release_posture** | Public or full intended distribution; rollback plan required |

---

#### `LC_GROWTH`

| Field | Value |
|-------|-------|
| **code** | `LC_GROWTH` |
| **definition** | Active expansion under governance |
| **maturity_level** | 5 |
| **expected_uncertainty** | Medium (expansion zones) |
| **expected_documentation_depth** | Growth charter; expansion runbooks; updated legal per geo/feature |
| **expected_qa_depth** | Regression + expansion domain QA; load/abuse where applicable |
| **expected_release_posture** | Staged rollout; feature flags; geo-phased where required |

---

#### `LC_MATURE`

| Field | Value |
|-------|-------|
| **code** | `LC_MATURE` |
| **definition** | Stable product; incremental evolution |
| **maturity_level** | 6 |
| **expected_uncertainty** | Low |
| **expected_documentation_depth** | Maintained operational corpus; change log discipline |
| **expected_qa_depth** | Regression-focused; selective exploratory for changes |
| **expected_release_posture** | Governed cadence; predictable release windows |

---

#### `LC_LEGACY`

| Field | Value |
|-------|-------|
| **code** | `LC_LEGACY` |
| **definition** | Maintenance-only; no feature investment |
| **maturity_level** | 6 (declining) |
| **expected_uncertainty** | Low (scope frozen) |
| **expected_documentation_depth** | Legacy notice; minimal change log; successor pointer |
| **expected_qa_depth** | OS compatibility; critical security only |
| **expected_release_posture** | Emergency-only releases; store presence maintained or sunset planned |

---

#### `LC_SUNSET`

| Field | Value |
|-------|-------|
| **code** | `LC_SUNSET` |
| **definition** | Intentional end-of-life in progress |
| **maturity_level** | 7 (terminal) |
| **expected_uncertainty** | Low (scope = shutdown) |
| **expected_documentation_depth** | Sunset comms; data export guide; retention schedule |
| **expected_qa_depth** | Migration/export paths; shutdown smoke |
| **expected_release_posture** | Final releases only; store removal scheduled |

---

#### `LC_HOLD` (lateral overlay)

| Field | Value |
|-------|-------|
| **code** | `LC_HOLD` |
| **definition** | Intentional pause; not forward progress |
| **maturity_level** | Inherits prior stage |
| **expected_uncertainty** | Inherits + staleness risk |
| **expected_documentation_depth** | Hold reason; re-entry conditions; stale-evidence date |
| **expected_qa_depth** | Frozen — no release unless hold lifted |
| **expected_release_posture** | Frozen |

---

## 6. Product Class Impact Matrix

Lifecycle stages are **shared**; **path, duration, skip rules, and evidence** differ by class.

**Legend:** ● = typical required path · ○ = optional/skip allowed with charter · — = rarely applicable · ✗ = skip forbidden

### 6.1 Stage path matrix (Core classes)

| Class | CONCEPT | DISCOVERY | PROOF | PILOT | PRODUCTION | GROWTH | Typical terminal path |
|-------|---------|-----------|-------|-------|------------|--------|----------------------|
| `CONVERSION_CLIENT` | ● | ● | ● | ○ | ● | ● | MATURE → LEGACY |
| `SERVICE_ACCOUNT` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |
| `CONTENT_CONSUMER` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |
| `COMMERCE` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |
| `PRODUCTIVITY_WORKFLOW` | ● | ● | ● | ○ | ● | ○ | MATURE → LEGACY |
| `FIELD_OPERATIONS` | ● | ● | ● | ● | ● | ○ | MATURE → LEGACY |
| `LOGISTICS_MOBILE` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |
| `COMMUNICATION` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |
| `COMPANION` | ○ | ○ | ○ | ○ | ● | ○ | Tied to parent |
| `DEVICE_CONTROLLER` | ● | ● | ● | ● | ● | ○ | LEGACY common |
| `UTILITY_TOOL` | ● | ○ | ● | ○ | ● | ✗ | LEGACY → SUNSET |
| `AI_ASSISTANT` | ● | ● | ● | ● | ● | ● | MATURE → LEGACY |

### 6.2 Extended classes

All Extended classes: **Pilot mandatory**; **Proof → Production skip forbidden**; **T4 minimum**; legal HITL at Production entry.

| Class | Pilot emphasis | Production extra gate |
|-------|----------------|----------------------|
| `MARKETPLACE` | Multi-role pilot (buyer + seller minimum) | Fraud/dispute ops ready |
| `FINTECH_WALLET` | Limited geo + transaction cap | Licensing/compliance sign-off |
| `HEALTH_MEDICAL` | Clinical advisor review in pilot | Regulatory evidence bundle |
| `AI_AGENT_CONSOLE` | Autonomy limits enforced in pilot | Kill-switch + audit proof |

### 6.3 Class-specific lifecycle behavior (deep dive)

#### `COMMERCE`

- **Discovery focus:** payment model, catalog source, returns policy sketch
- **Proof:** single happy-path purchase; no full catalog required
- **Pilot:** real payments in controlled catalog; refund path tested
- **Production:** PCI-adjacent hygiene; order-state regression mandatory
- **Growth:** geo expansion triggers legal re-review per region
- **Never skip:** Pilot (payment failures destroy trust)

#### `UTILITY_TOOL`

- **Discovery:** often minimal (1–2 weeks) if task obvious
- **Proof:** core task works on target devices
- **Pilot:** optional for T1; recommended if monetization or data collection
- **Production:** may arrive fast from Proof with T1 skip charter
- **Growth:** usually N/A — path to MATURE directly from Production
- **Risk:** scope creep into `SERVICE_ACCOUNT`

#### `FIELD_OPERATIONS`

- **Discovery:** offline/connectivity strategy mandatory
- **Proof:** single job completion with capture (photo/geo)
- **Pilot:** field users in real conditions; sync failure scenarios
- **Production:** data loss prevention proven; rugged device matrix
- **Growth:** optional — new job types vs new markets
- **Never skip:** Proof (field assumptions fail in office)

#### `AI_ASSISTANT`

- **Discovery:** safety boundary definition early
- **Proof:** conversation core + escalation path stub
- **Pilot:** harmful output monitoring; human escalation tested
- **Production:** disclosure, fallback model, content policy enforced
- **Growth:** new domains = new safety review (not just features)
- **Never skip:** Pilot (safety failures are reputational/legal)

#### `COMPANION`

- **Entry:** may enter at `LC_PRODUCTION` if parent product operational and mobile scope is parity subset
- **Proof/Pilot:** required when mobile introduces **new** value, not parity
- **Lifecycle coupling:** parent major version may force mobile regression cycle without lifecycle regression

---

## 7. Complexity Tier Impact

Tiers describe **production load**, not product quality. They modulate lifecycle **duration**, **validation depth**, and **skip eligibility**.

### 7.1 Tier rules summary

| Rule | T1 | T2 | T3 | T4 |
|------|----|----|----|-----|
| **Typical minimum path** | CONCEPT→PROOF→PRODUCTION | + DISCOVERY; Pilot recommended | Full path; Pilot mandatory | Full path; Extended gates |
| **Discovery duration** | 1–2 weeks | 2–4 weeks | 4–8 weeks | 8+ weeks |
| **Proof duration** | 2–4 weeks | 3–8 weeks | 6–12 weeks | 8–16 weeks |
| **Pilot duration** | Optional | 4–8 weeks | 6–12 weeks | 12+ weeks |
| **Proof→Production skip** | Allowed (class permitting) | Rare; charter | Forbidden | Forbidden |
| **Architecture charter** | Waiver common | Selective | Required at Proof exit | Required at Discovery exit |
| **QA depth at Production** | Baseline | + regression | + domain matrices | + compliance/abuse |
| **Release at Production** | Simple cadence | Store standard | Staged rollout | Phased geo + legal |

### 7.2 Specific questions answered

**Does T1 utility reach Production faster?**  
Yes — with valid skip path: `UTILITY_TOOL` T1 may move `LC_PROOF → LC_PRODUCTION` after usability validation + device smoke, bypassing `LC_PILOT`. Documentation and QA depth remain per registry row `LC_PRODUCTION`; they are lighter but **not zero**.

**Does T4 marketplace require additional validation?**  
Yes — `MARKETPLACE` T4 requires: multi-role pilot; fraud/dispute evidence; legal sign-off before `LC_PRODUCTION`; no stage skips; minimum pilot duration 12 weeks unless HITL waiver with documented risk acceptance.

**Tier bump mid-life:**  
If `complexity_tier` increases (e.g. T2→T3 with payments), product **does not automatically regress** lifecycle stage, but triggers **re-validation charter**: minimum return to `LC_PROOF` for new domain **or** `LC_PILOT` for operational learning — decision in future Decision System; lifecycle records overlay `tier_change_revalidation_required`.

---

## 8. Decision Pressure Model

Maps **what decisions become critical** at each stage. Does **not** define Decision System.

| Stage | Critical decision domains | Pressure description |
|-------|--------------------------|----------------------|
| `LC_CONCEPT` | Exist / not exist | Is this a product worth any NOVA attention? |
| `LC_DISCOVERY` | Problem · class · tier · distribution | What are we building for whom, and under what load? |
| `LC_PROOF` | Scope boundary · kill/pivot/continue | Is core hypothesis worth pilot investment? |
| `LC_PILOT` | Scale / fix / kill | Does real-world use justify production ops? |
| `LC_PRODUCTION` | Ops model · compliance · support | Are we ready to be depended upon? |
| `LC_GROWTH` | Expansion scope · architecture · geo | What do we expand without breaking baseline? |
| `LC_MATURE` | Invest / harvest / legacy | Do we refresh or begin withdrawal? |
| `LC_LEGACY` | Sunset timing · successor | When and how do we exit? |
| `LC_SUNSET` | Data retention · user migration | How do we exit responsibly? |
| `LC_HOLD` | Resume / kill | Is stale evidence still valid? |

### 8.1 Class amplifications

| Class | Amplified decision pressure |
|-------|----------------------------|
| `COMMERCE` | Payment/refund policy at Discovery; chargeback ops at Production |
| `FIELD_OPERATIONS` | Offline strategy at Discovery; data loss tolerance at Pilot |
| `AI_ASSISTANT` | Safety boundaries at Discovery; escalation at Pilot |
| `MARKETPLACE` | Multi-sided trust model at Discovery; fraud at Pilot |
| `COMPANION` | Parity vs differentiation at Discovery; parent coupling at Production |

---

## 9. Documentation Evolution Model

| Stage | Required artifacts | Optional artifacts | Anti-pattern |
|-------|-------------------|-------------------|--------------|
| `LC_CONCEPT` | Idea brief | Stakeholder map | Full PRD |
| `LC_DISCOVERY` | Discovery brief; class/tier hypothesis; distribution sketch | Competitive notes; user interview summaries | Architecture spec |
| `LC_PROOF` | Proof scope doc; core journey map; known gaps log | Technical spike notes | Complete ops runbook |
| `LC_PILOT` | Pilot charter; success metrics; support playbook (lite) | Weekly pilot reports | Full legal pack (unless commerce/regulated) |
| `LC_PRODUCTION` | Operational index; architecture record; legal baseline; release runbook | Full QA matrix archive | Undocumented «tribal knowledge» |
| `LC_GROWTH` | Growth charter; expansion checklists | Per-market addenda | Undocumented geo launches |
| `LC_MATURE` | Maintained changelog; dependency audit cadence | Retirement planning notes | Frozen docs from year 1 |
| `LC_LEGACY` | Legacy status notice; owner; critical contact | Successor migration guide | Silent abandonment |
| `LC_SUNSET` | Sunset comms; data export guide; retention schedule | Archive manifest | Missing user notification |

**Website Factory lesson:** handoff collapse when delivery lacks source, risk, freeze, validation ([`production-drift-taxonomy.md`](../../mars-website-factory/production-drift-taxonomy.md)). **Production entry requires** operational documentation depth per `LC_PRODUCTION` registry row — not post-hoc.

**MARS Survivability lesson:** snapshot manifest before major transitions (conceptual parallel to [`snapshot-manifest-standard-v1.md`](../../mars-survivability/protocols/snapshot-manifest-standard-v1.md)) — recommended at `LC_PILOT → LC_PRODUCTION` and tier bumps.

---

## 10. QA Evolution Model

| Stage | QA mode | Primary focus | Exit QA gate |
|-------|---------|---------------|--------------|
| `LC_CONCEPT` | None | Assumption list review | N/A |
| `LC_DISCOVERY` | Assumption validation | Problem/evidence quality | Discovery review |
| `LC_PROOF` | Core journey QA | Task completion; fatal defects | Proof validation report |
| `LC_PILOT` | Pilot regression | Real-world friction; pilot metrics | Pilot evaluation report |
| `LC_PRODUCTION` | Full class matrix | Regression + class priorities from registry | Release candidate gate |
| `LC_GROWTH` | Regression + expansion | New surface abuse; perf under load | Expansion release gate |
| `LC_MATURE` | Regression-focused | Stability; security patches | Standard release gate |
| `LC_LEGACY` | Compatibility | OS updates; critical CVEs | Emergency release only |
| `LC_SUNSET` | Migration | Export paths; shutdown flows | Decommission checklist |

### 10.1 Class QA emphasis by stage (examples)

| Class | Proof QA | Pilot QA | Production QA |
|-------|----------|----------|---------------|
| `COMMERCE` | Happy-path purchase | Refund; inventory edge | Payment regression matrix |
| `FIELD_OPERATIONS` | Single job offline/online | Sync conflict; photo integrity | Data loss scenarios |
| `UTILITY_TOOL` | Core task correctness | Optional | Baseline + a11y |
| `AI_ASSISTANT` | Safety spot-check | Harm monitoring; escalation | Policy regression + red-team sample |

**ORCA lesson:** validation CLI green ≠ approved ([`artifact-lifecycle-v0.md`](../../orca/content-packs/artifact-lifecycle-v0.md)). Same for lifecycle: **QA pass ≠ stage advance** without evidence bundle.

---

## 11. Release Evolution Model

| Stage | Release expectation | Distribution | Rollback |
|-------|--------------------|--------------|---------| 
| `LC_CONCEPT` | None | — | — |
| `LC_DISCOVERY` | None | — | — |
| `LC_PROOF` | Internal/test only | Dev build; internal track | Redeploy |
| `LC_PILOT` | Controlled | TestFlight; closed track; MDM cohort; geo fence | Mandatory plan |
| `LC_PRODUCTION` | Full intended | Store public / enterprise MDM full | Mandatory tested |
| `LC_GROWTH` | Staged expansion | Feature flags; geo phases | Per expansion |
| `LC_MATURE` | Governed cadence | Regular windows | Standard |
| `LC_LEGACY` | Emergency only | Maintenance releases | Documented |
| `LC_SUNSET` | Final | Removal scheduled | N/A |

### 11.1 Release vs lifecycle anti-confusion

| Confusion | Resolution |
|-----------|------------|
| First store submission | Release **event** inside `LC_PILOT` or `LC_PRODUCTION` — stage determined by ops evidence |
| Hotfix in Production | Release cadence event; lifecycle stays `LC_PRODUCTION` |
| Beta label in store 2 years | Lifecycle audit — likely `LC_PILOT` mislabeled |

---

## 12. Lifecycle Anti-Chaos Rules

| ID | Rule | Enforcement (human-operated v1) |
|----|------|--------------------------------|
| **AC-L1** | No stage skip without documented skip path (§4.3, §7) | Transition rejected in review |
| **AC-L2** | `LC_PRODUCTION` requires ops evidence bundle | No production claim in REPORT without bundle |
| **AC-L3** | «MVP» is scope label inside `LC_PROOF`, not lifecycle stage | Terminology correction in intake |
| **AC-L4** | Pilot max duration without review: 16 weeks (Core), 24 weeks (Extended) | Forced hold or kill decision |
| **AC-L5** | Tier T3+ cannot skip `LC_PILOT` | Charter waiver requires HITL |
| **AC-L6** | Extended classes cannot enter `LC_PRODUCTION` without legal HITL | Block transition |
| **AC-L7** | Lifecycle state must be recorded alongside `product_class_record` | Incomplete binding = SAFE UNKNOWN |
| **AC-L8** | `LC_GROWTH` requires explicit charter — never inferred from feature count | Stage correction |
| **AC-L9** | Documentation depth must match registry row minimum before forward transition | Evidence gap flagged |
| **AC-L10** | Store/public release ≠ automatic stage advance | Separate release log and lifecycle log |
| **AC-L11** | Backward transition requires regression charter, not shame | Documented retreat allowed |
| **AC-L12** | `LC_HOLD` > 90 days triggers stale-evidence review before resume | Forced DISCOVERY touch |

---

## 13. Lifecycle Failure Patterns

| Pattern | Signal | Typical cause | Response |
|---------|--------|---------------|----------|
| **Perpetual Proof** | `LC_PROOF` > 6 months; scope keeps expanding | MVP inflation; no kill criteria | Force pilot/kill decision |
| **Pilot forever** | Metrics undefined; «just one more cohort» | Validation avoidance | AC-L4 review |
| **Premature Production** | Store live; no support/rollback | Executive pressure; competitor panic | Regression to Pilot or HOLD |
| **Fake Production** | Full marketing; pilot-quality ops | Mislabeled stage | Lifecycle audit |
| **Architecture too early** | P6 artifacts in Discovery | Technology-first | Hold build; complete Discovery |
| **Architecture too late** | Production incidents from tech debt | Skipped Proof learning | Re-validation charter |
| **Feature explosion in Growth** | No growth charter; backlog chaos | Org politics | HOLD + charter |
| **Validation avoidance** | No metrics; qualitative only | Fear of kill | Require pilot metrics |
| **Companion drift** | Mobile diverges from parent silently | Independent roadmap | Coupling review |
| **Legacy denial** | No owner; no updates; still «Production» | Org neglect | Force LEGACY or SUNSET |
| **Documentation collapse** | Production with Concept-level docs | Delivery pressure | Block expansion; doc sprint |
| **Tier understatement** | T1 label on T3 product | Intake optimism | Re-tier + re-validation |

---

## 14. Lifecycle Relationship Mapping

```text
┌─────────────────────────────────────────────────────────────┐
│                    REALITY LAYER (NOVA)                      │
├─────────────────────────────────────────────────────────────┤
│  Production Model v1                                         │
│  Product Taxonomy v1                                         │
│  Product Class Registry v1  ──► product_class_code           │
│  Lifecycle Model v1         ──► lifecycle_state_code   ◄── YOU ARE HERE
└───────────────────────────────┬─────────────────────────────┘
                                │ consumes class + tier
                                ▼
┌─────────────────────────────────────────────────────────────┐
│              LIFECYCLE LAYER (same Reality band)             │
│  lifecycle_state_code + transition evidence                  │
└───────────────────────────────┬─────────────────────────────┘
                                │ informs pressure
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                 DECISION SYSTEM (future)                     │
│  Stage-appropriate decisions; kill/continue/expand           │
└───────────────────────────────┬─────────────────────────────┘
                                │ produces commitments
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                    CONTRACTS (future)                        │
│  Legal · QA · Integration · Release · AI safety              │
│  Depth bound by class × lifecycle stage                      │
└───────────────────────────────┬─────────────────────────────┘
                                │ governs execution
                                ▼
┌─────────────────────────────────────────────────────────────┐
│              EXECUTION SYSTEMS (future)                      │
│  Production Model P0–P12 · Workflow · Roles · Tools        │
└─────────────────────────────────────────────────────────────┘
```

### 14.1 Dependency rules

| Upstream | Downstream | Dependency |
|----------|------------|------------|
| Registry | Lifecycle | Class determines path variants and evidence |
| Lifecycle | Decisions | Stage determines decision pressure |
| Lifecycle + Registry | Contracts | Class × stage determines contract depth |
| Contracts | Workflow | Execution must satisfy committed contracts |
| Production Model | Workflow | P-phases operationalize build — **orthogonal** to lifecycle stage |

**Instance binding (future):**

```text
nova_product_record {
  product_class_code,
  complexity_tier,
  modifiers[],
  lifecycle_state_code,
  lifecycle_entered_at,
  transition_evidence_ref
}
```

---

## 15. RBM Mapping

```text
Reality
├── Production Model v1     … what NOVA is
├── Product Taxonomy v1     … what classes exist
├── Product Class Registry  … what each class means
└── Lifecycle Model v1      … where the product is in life  ◄── completes Reality band
        │
        ▼
Lifecycle (as RBM layer name — same artifact family, consumed by downstream)
        │
        ▼
Decisions    … what to decide now (future)
        │
        ▼
Contracts    … what must be true (future)
        │
        ▼
Workflow     … Production Model P0–P12 execution (future)
        │
        ▼
Roles        … who (future)
        │
        ▼
Tools        … helpers (future)
        │
        ▼
Agents       … only if proven necessary (future)
        │
        ▼
Automation   … last, if ever (future)
```

### 15.1 Why Lifecycle is next after Registry

| Order | Reason |
|-------|--------|
| Registry before Lifecycle | Must know **what** the product is before **where** it is in life; class defines path variants |
| Lifecycle before Decisions | Decisions without life-stage context are random («build microservices» in Concept) |
| Lifecycle before Contracts | Contract depth varies by stage — Concept needs idea brief, Production needs legal pack |
| Lifecycle before Workflow | Same P9 build phase means different things in Proof vs Production QA posture |

**Completion of Reality band:** After Lifecycle v1, NOVA Reality Layer has **identity** (taxonomy + registry) and **temporal state** (lifecycle). Downstream layers can now anchor to stable vocabulary.

---

## 16. Risks

| Risk | Severity | Mitigation in v1 |
|------|----------|------------------|
| Lifecycle confused with P0–P12 | High | Explicit orthogonality table (§1); terminology in AC-L10 |
| Stage inflation (everything Production) | High | AC-L2, AC-L5; evidence bundles |
| Startup framework reintroduction | Medium | Derived stages with MARS-specific skip rules |
| Extended class treated as Core path | High | AC-L6; §6.2 mandatory pilot |
| Companion inherits parent lifecycle incorrectly | Medium | §6.3 coupling rules |
| Tier bump without re-validation | High | §7.2 tier bump rule |
| Governance expansion drift | Medium | Scope boundary: no Decision System in v1 |
| No in-repo NOVA files yet | Medium | This file starts foundation tree; prior sessions design-only |
| Human enforcement fatigue | Medium | Minimal rule set AC-L1–L12; not automation pretense |

---

## 17. SAFE UNKNOWN

| Unknown | What would resolve |
|---------|-------------------|
| Exact machine format for `lifecycle_state_record` | Future NOVA intake schema design |
| Numeric pilot metric thresholds per class | Evidence from first NOVA pilots |
| Whether `LC_HOLD` becomes formal overlay vs stage | Operator feedback after first products |
| Geographic regulatory impact on stage duration | Legal charter per region |
| Parent-child lifecycle coupling rules for `COMPANION` | First companion product through NOVA |
| Integration with MARS `registry/project-registry.md` | NOVA pack creation workflow (future) |
| Prior taxonomy/registry markdown files in-repo | Human decision to commit foundation pack |

**Non-claims preserved:** this model does not assert runtime tracking, automated gates, or agent enforcement.

---

## 18. Recommended Next Step

**Single next artifact:** `NOVA DECISION PRESSURE SYSTEM v1` (or `NOVA DECISION MODEL v1`) — first machinery-adjacent layer **after** Lifecycle, converting §8 decision pressure map into:

- decision types per `lifecycle_state_code × product_class_code`
- kill/continue/expand decision templates
- HITL trigger matrix
- explicit **non-automation** boundaries

**Do not skip to:** Contracts, Core Run, Roles, Agents, or Workflow until Decision layer charter approved.

**Optional parallel (human choice):** commit NOVA foundation pack to `projects/nova/foundation/`:

- `NOVA-PRODUCTION-MODEL-v1.md` (from prior session)
- `NOVA-MOBILE-PRODUCT-TAXONOMY-v1.md`
- `NOVA-PRODUCT-CLASS-REGISTRY-v1.md`
- `NOVA-MOBILE-PRODUCT-LIFECYCLE-MODEL-v1.md` (this file)

---

## Appendix A — Lifecycle × Production Model cross-reference

| Lifecycle stage | Typical Production Model phases active | Notes |
|-----------------|----------------------------------------|-------|
| `LC_CONCEPT` | P0 (exploration) | May not enter NOVA formally |
| `LC_DISCOVERY` | P0–P3 | Classification at P2 |
| `LC_PROOF` | P1–P10 (compressed) | P5 skippable for utilitarian |
| `LC_PILOT` | P9–P11 (iterative) | Releases are controlled |
| `LC_PRODUCTION` | P10–P12 | P11 was initial production release |
| `LC_GROWTH` | P12 (+ selective P1–P3 for expansion) | New scope = partial definition |
| `LC_MATURE` | P12 maintenance | |
| `LC_LEGACY` | P12 emergency only | |
| `LC_SUNSET` | Decommission workflow (future) | Not P-phase mapped yet |

---

## Appendix B — Transition evidence checklist template

```markdown
# Lifecycle Transition Evidence — [PRODUCT] — [FROM] → [TO]

- [ ] Product class record current
- [ ] Complexity tier validated
- [ ] Stage-specific artifacts present (§9)
- [ ] QA gate passed for target stage (§10)
- [ ] Release posture aligned (§11)
- [ ] Class skip rules checked (§6)
- [ ] Tier skip rules checked (§7)
- [ ] Approvals recorded
- [ ] SAFE UNKNOWN items listed
- [ ] Regression charter (if backward transition)
```

---

**Document status:** v1 design complete — Reality Layer lifecycle artifact for NOVA mobile products.
