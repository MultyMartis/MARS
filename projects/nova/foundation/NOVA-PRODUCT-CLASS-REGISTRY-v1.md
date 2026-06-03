# NOVA Product Class Registry v1

**Status:** design-only — канонический production registry, не runtime, не схема БД, не folder structure
**Lane:** B · External Systems
**Version:** v1
**Foundation chain:** RBM → NOVA Production Model v1 → NOVA Mobile Product Taxonomy v1 → **this document** → NOVA Mobile Product Lifecycle Model v1
**Non-claims:** no agents, no orchestration, no automated registry enforcement, no database schema, no folder structure

**Основание:** RBM · NOVA Production Model v1 · NOVA Mobile Product Taxonomy v1
**Evidence base:** NOVA Mobile Product Taxonomy v1; Website Factory Site Type Registry v1 pattern; ORCA classification principles

**Recovery note:** Promoted from Cursor transcript `34bc9bde-bbac-4b2e-963d-b90bd8870b20` — faithful recovery pass v1 (2026-06-04).

---

## 1. Executive Summary

NOVA Product Class Registry v1 — **второй слой Production Reality** после таксономии. Таксономия ответила «какие классы существуют»; реестр отвечает **«что каждый класс означает операционно»** и становится единым словарём для будущих систем NOVA.

| Элемент | Содержание |
|---------|------------|
| **15 product classes** | 11 Core + 4 Extended |
| **5 mobile modifiers** | `MLOC`, `MOFF`, `MDEV`, `MPUSH`, `MBG` |
| **1 AI modifier** | `AI_COPILOT` |
| **1 canonical registry row** | 28 полей на класс (§3) |
| **Relationship model** | parent · adjacent · migration |
| **Validation + governance + usage rules** | operational-only, без governance expansion |

**Ключевое различие Taxonomy → Registry:**

| Taxonomy | Registry |
|----------|----------|
| Discovery & classification logic | Operational defaults per class |
| «Would NOVA build differently?» test | Default tier, QA, release, lifecycle emphasis |
| Dimensions, tiers, modifiers as concepts | Allowed combinations, forbidden patterns |
| Classification engine (G0) | Row lookup + validation rules |

**Scope boundary:** только registry layer. Lifecycle Model, Decision System, Contracts, Core Run, Roles, Agents — **не проектируются**.


---

## 2. Registry Philosophy

### 2.1 Purpose

Product Class Registry v1 — **канонический production vocabulary** NOVA для мобильных продуктов. Каждый `product_class_code` несёт операционные defaults: tier, QA emphasis, release posture, lifecycle criticality, allowed modifiers, failure patterns, relationships.

Реестр **не классифицирует** новые проекты (это G0 + taxonomy engine). Реестр **определяет**, что означает уже выбранный код.

### 2.2 Scope

**In scope v1:**

- 11 Core classes
- 4 Extended classes
- 5 mobile modifiers + `AI_COPILOT`
- Validation, governance, usage, anti-chaos rules
- Relationship model

**Out of scope v1:**

- Machine-readable DB / JSON schema / folder tree
- Runtime registry engine
- Lifecycle phases design
- Legal pack content (только posture defaults)
- Geographic store matrix

### 2.3 RBM Role

Registry остаётся в **Reality** — последний committed artifact Reality Layer до Lifecycle:

```
Reality Layer (NOVA v1 maturity)
├── Production Model v1        ← what NOVA is
├── Product Taxonomy v1        ← what classes exist
└── Product Class Registry v1  ← what each class means operationally  ← THIS
```

Machinery (workflow, roles, agents) **читает** registry; registry **не исполняет** machinery.

### 2.4 Relationship to Taxonomy

| Aspect | Taxonomy v1 | Registry v1 |
|--------|-------------|-------------|
| **Question** | What classes exist? How to classify? | What does class X mean for production? |
| **Artifact** | Classification engine, dimensions, tiers | Normalized row per class/modifier |
| **Change trigger** | New product species discovered | Operational defaults refined from evidence |
| **Consumer** | G0 classifier (human) | Lifecycle, Decisions, Contracts, QA, Release (future) |
| **Identity** | Same `product_class_code` | Same codes — **no new codes without governance** |

**Почему registry отдельно от taxonomy:**

1. **Separation of discovery vs definition** — taxonomy evolves by adding species; registry evolves by sharpening operational meaning.
2. **Stable lookup surface** — downstream systems need one row, not entire taxonomy document.
3. **Website Factory precedent** — Site Type Registry v1 отделён от v0 taxonomy drift; mapping docs consume codes.
4. **Anti-chaos** — taxonomy resists category explosion; registry resists default drift and contradictory interpretations.

---

## 3. Registry Structure

### 3.1 Canonical Registry Row — Class Entry

Каждый product class — одна строка реестра со следующими **обязательными полями**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `product_class_code` | code | Yes | Stable identifier; UPPER_SNAKE; immutable after v1 freeze |
| `registry_version` | version | Yes | `v1` |
| `class_group` | enum | Yes | `core` · `extended` |
| `name` | string | Yes | Human-readable name (RU primary) |
| `definition` | prose | Yes | Operational definition — not marketing |
| `primary_user` | string | Yes | Who hires the app |
| `business_objective` | string | Yes | Why the product exists commercially |
| `default_tier` | enum | Yes | `T1` · `T2` · `T3` · `T4` |
| `tier_ceiling` | enum | Yes | Maximum tier without re-classification |
| `allowed_modifiers` | set | Yes | Subset of `{MLOC, MOFF, MDEV, MPUSH, MBG, AI_COPILOT}` |
| `forbidden_modifiers` | set | No | Explicit exclusions |
| `typical_dimensions` | set | Yes | Default dimension values from taxonomy §4 |
| `critical_lifecycle_areas` | ordered list | Yes | Phases where class defaults dominate (conceptual phase names) |
| `qa_priorities` | ordered list | Yes | QA domains in priority order |
| `release_priorities` | ordered list | Yes | Release gates and risks in priority order |
| `default_legal_posture` | enum | Yes | `minimal` · `standard` · `commerce` · `ugc` · `regulated` · `clinical` · `financial` |
| `default_distribution` | enum | Yes | Typical `distribution` dimension |
| `hitl_depth_default` | enum | Yes | `rare` · `selective` · `often` · `mandatory` |
| `architecture_charter_required` | bool | Yes | `false` for Core default path; `true` for Extended |
| `common_failure_patterns` | list | Yes | Known production failures for this class |
| `forbidden_patterns` | list | Yes | Anti-patterns — scope creep signals |
| `related_classes` | struct | Yes | `{parent[], adjacent[], migration[]}` |
| `classification_signals` | list | Yes | How to recognize this class at G0 |
| `status` | enum | Yes | `active` · `deprecated` |
| `notes` | prose | No | Edge cases, evidence links |

### 3.2 Canonical Registry Row — Modifier Entry

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `modifier_code` | code | Yes | `MLOC` · `MOFF` · `MDEV` · `MPUSH` · `MBG` · `AI_COPILOT` |
| `modifier_group` | enum | Yes | `mobile` · `ai` |
| `meaning` | prose | Yes | What the modifier asserts |
| `requires_host_class` | bool | Yes | `true` for `AI_COPILOT` |
| `production_impact` | prose | Yes | What changes in production load |
| `architecture_impact` | prose | Yes | Technical charter additions |
| `qa_impact` | prose | Yes | QA matrix additions |
| `release_impact` | prose | Yes | Store/compliance additions |
| `incompatible_with` | set | No | Classes or modifiers that conflict |
| `max_per_project` | int | Yes | Global cap enforced with AC-2 |
| `status` | enum | Yes | `active` |

### 3.3 Project Binding Record (consumes registry; not stored in registry)

Future systems emit `product_class_record` at G0 — **instance**, not registry row:

`product_class_code` + optional `product_class_secondary` + `complexity_tier` + `dimensions` + `mobile_modifiers[]` + `ai_modifier` + `delivery` + rationale + HITL sign-off.

Registry validates this record; it does not replace it.

---

## 4. Core Class Registry

**Правило Core:** default production target NOVA v1. `architecture_charter_required = false` unless tier bump or modifier stack triggers charter (see validation §9).

---

### `CONVERSION_CLIENT`

| Field | Value |
|-------|-------|
| **code** | `CONVERSION_CLIENT` |
| **definition** | Мобильный клиент для разового или короткого commercial action: заявка, бронь, звонок, калькulator, onboarding в услугу |
| **primary_user** | Prospects, local service seekers, campaign traffic |
| **business_objective** | Конверсия трафика в lead / booking / trial start |
| **default_tier** | T1–T2 |
| **tier_ceiling** | T3 |
| **allowed_modifiers** | `MPUSH`, `MLOC` (contextual) |
| **forbidden_modifiers** | `MOFF` (unless charter), `MDEV`, `AI_COPILOT` without host workflow |
| **critical_lifecycle_areas** | INTAKE → PRODUCT_DEF → DESIGN → QA → RELEASE |
| **qa_priorities** | Conversion path · form a11y · claim honesty · CTA consistency · performance on cold start |
| **release_priorities** | Store metadata accuracy · misleading claims avoidance · fast cadence |
| **common_failure_patterns** | Scope creep into account model · fake urgency copy · form abandonment from over-collection |
| **related_classes** | parent: — · adjacent: `SERVICE_ACCOUNT`, `UTILITY_TOOL` · migration: → `SERVICE_ACCOUNT` when persistent account added |

---

### `SERVICE_ACCOUNT`

| Field | Value |
|-------|-------|
| **code** | `SERVICE_ACCOUNT` |
| **definition** | Постоянные отношения с сервисом: личный кабинет, статусы, документы, поддержка, подписка |
| **primary_user** | Existing customers / subscribers |
| **business_objective** | Retention, self-service, снижение нагрузки на support |
| **default_tier** | T2–T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MPUSH`, `AI_COPILOT`, `MOFF` (limited) |
| **critical_lifecycle_areas** | ARCHITECTURE → BUILD → QA → LEGAL/STORE |
| **qa_priorities** | Auth/session · data privacy · account regression · notification opt-in |
| **release_priorities** | Account lockout prevention · privacy labels · staged rollout |
| **common_failure_patterns** | Weak session recovery · notification spam · billing state desync |
| **related_classes** | parent: — · adjacent: `CONVERSION_CLIENT`, `COMPANION`, `COMMERCE` · migration: ← `CONVERSION_CLIENT`; → `FINTECH_WALLET` if regulated money |

---

### `CONTENT_CONSUMER`

| Field | Value |
|-------|-------|
| **code** | `CONTENT_CONSUMER` |
| **definition** | Потребление контента: статьи, видео, аудио, курсы-as-content, новости |
| **primary_user** | Readers, viewers, learners |
| **business_objective** | Engagement, subscription/ads monetization, brand reach |
| **default_tier** | T2 |
| **tier_ceiling** | T3 |
| **allowed_modifiers** | `MOFF`, `MPUSH` |
| **critical_lifecycle_areas** | DESIGN → BUILD → QA |
| **qa_priorities** | Media performance · offline cache · a11y · copyright compliance |
| **release_priorities** | Region restrictions · content rating · CDN failover |
| **common_failure_patterns** | Paywall confusion · broken offline · autoplay policy violations |
| **related_classes** | adjacent: `COMMUNICATION`, `AI_ASSISTANT` · migration: → `COMMUNICATION` if social graph becomes core |

---

### `COMMERCE`

| Field | Value |
|-------|-------|
| **code** | `COMMERCE` |
| **definition** | Single-vendor shopping: catalog → cart → checkout → order tracking |
| **primary_user** | Buyers of one merchant/brand |
| **business_objective** | Direct product sales |
| **default_tier** | T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MPUSH`, `MLOC` (store locator), `AI_COPILOT` |
| **critical_lifecycle_areas** | ARCHITECTURE → LEGAL/STORE → QA → RELEASE |
| **qa_priorities** | Payment flows · cart edge cases · order state · inventory sync |
| **release_priorities** | Store IAP policy · PCI-adjacent hygiene · rollback on payment failure |
| **common_failure_patterns** | Cart abandonment from UX · tax/shipping miscalculation · double charge |
| **related_classes** | adjacent: `MARKETPLACE`, `SERVICE_ACCOUNT` · migration: → `MARKETPLACE` when multi-seller |

---

### `PRODUCTIVITY_WORKFLOW`

| Field | Value |
|-------|-------|
| **code** | `PRODUCTIVITY_WORKFLOW` |
| **definition** | Выполнение рабочих задач: CRM mobile, approvals, tickets, documents, team coordination |
| **primary_user** | Employees, managers, field office staff |
| **business_objective** | Operational efficiency for knowledge/service workers |
| **default_tier** | T2–T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MOFF`, `MPUSH`, `AI_COPILOT`, `MLOC` (contextual) |
| **critical_lifecycle_areas** | ARCHITECTURE → QA → RELEASE |
| **qa_priorities** | Role permissions · audit trail · sync integrity · integration smoke |
| **release_priorities** | Enterprise auth · data residency · regression on workflows |
| **common_failure_patterns** | Permission leaks · sync conflicts · audit gaps |
| **related_classes** | adjacent: `FIELD_OPERATIONS`, `COMPANION`, `AI_AGENT_CONSOLE` · migration: → `FIELD_OPERATIONS` when physical-world capture dominates |

---

### `FIELD_OPERATIONS`

| Field | Value |
|-------|-------|
| **code** | `FIELD_OPERATIONS` |
| **definition** | Работа исполнителя в физическом мире: inspection, maintenance, audit, inventory count, healthcare visit (non-clinical) |
| **primary_user** | Technicians, inspectors, nurses, auditors |
| **business_objective** | Capture proof-of-work, compliance, dispatch completion |
| **default_tier** | T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MOFF`, `MLOC`, `MDEV`, `MBG` |
| **critical_lifecycle_areas** | ARCHITECTURE → BUILD → QA |
| **qa_priorities** | Offline sync · photo/geo integrity · rugged usage · data loss prevention |
| **release_priorities** | Permission denial handling · offline recovery · device matrix |
| **common_failure_patterns** | Sync data loss · photo upload failures · geo inaccuracy |
| **related_classes** | adjacent: `LOGISTICS_MOBILE`, `HEALTH_MEDICAL`, `DEVICE_CONTROLLER` · migration: → `HEALTH_MEDICAL` if clinical/regulatory |

---

### `LOGISTICS_MOBILE`

| Field | Value |
|-------|-------|
| **code** | `LOGISTICS_MOBILE` |
| **definition** | Courier/driver/restaurant/warehouse movement: routes, pickups, handoffs, real-time status |
| **primary_user** | Drivers, couriers, dispatch-linked operators |
| **business_objective** | Throughput and SLA of physical delivery/logistics |
| **default_tier** | T3–T4 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MLOC`, `MOFF`, `MBG`, `MPUSH` |
| **forbidden_modifiers** | — (all mobile modifiers plausible; max 2 enforced globally) |
| **critical_lifecycle_areas** | ARCHITECTURE → BUILD → QA → RELEASE |
| **qa_priorities** | Background location · battery · realtime · SLA exception paths |
| **release_priorities** | Store location policy · background mode justification · phased geo rollout |
| **common_failure_patterns** | Battery drain · stale routes · background kill by OS |
| **related_classes** | adjacent: `FIELD_OPERATIONS`, `COMMERCE` (delivery apps) · migration: ↔ `FIELD_OPERATIONS` at G0 if movement vs capture unclear |

---

### `COMMUNICATION`

| Field | Value |
|-------|-------|
| **code** | `COMMUNICATION` |
| **definition** | Messaging, calls, communities, feeds with social graph or conversation as core |
| **primary_user** | Consumers, community members |
| **business_objective** | Connection, community retention, communication utility |
| **default_tier** | T3–T4 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MPUSH`, `MBG`, `AI_COPILOT` |
| **critical_lifecycle_areas** | ARCHITECTURE → LEGAL/STORE → QA |
| **qa_priorities** | Moderation · abuse reporting · realtime reliability · privacy |
| **release_priorities** | UGC policy · store content rules · age gating |
| **common_failure_patterns** | Moderation gaps · harassment vectors · notification overload |
| **related_classes** | adjacent: `CONTENT_CONSUMER`, `AI_ASSISTANT` · migration: → `MARKETPLACE` if transactions between users dominate |

---

### `COMPANION`

| Field | Value |
|-------|-------|
| **code** | `COMPANION` |
| **definition** | Мобильное продолжение существующего продукта (web/desktop/SaaS/IoT platform) |
| **primary_user** | Existing product users |
| **business_objective** | Mobile reach; parity or focused subset of parent product |
| **default_tier** | T2–T3 |
| **tier_ceiling** | T4 (inherits parent ceiling) |
| **allowed_modifiers** | `MPUSH`, `MOFF`, `MDEV`, `MLOC`, `AI_COPILOT` (bounded by parent) |
| **critical_lifecycle_areas** | INTAKE → ARCHITECTURE → QA → RELEASE |
| **qa_priorities** | API parity · version coupling · auth bridge · regression vs parent |
| **release_priorities** | Parent API break coordination · feature drift control |
| **common_failure_patterns** | Feature drift from parent · broken auth bridge · stale API contract |
| **related_classes** | parent: external product (not a class) · adjacent: `SERVICE_ACCOUNT`, `PRODUCTIVITY_WORKFLOW` · migration: → native class if >60% standalone value |

---

### `DEVICE_CONTROLLER`

| Field | Value |
|-------|-------|
| **code** | `DEVICE_CONTROLLER` |
| **definition** | Управление физическим устройством: smart home, wearable, BLE gadget, industrial controller |
| **primary_user** | Device owners, installers |
| **business_objective** | Device pairing, control, monitoring, firmware-adjacent UX |
| **default_tier** | T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MDEV`, `MOFF`, `MPUSH`, `MBG` |
| **critical_lifecycle_areas** | ARCHITECTURE → BUILD → QA |
| **qa_priorities** | Pairing matrix · failure recovery · hardware fragmentation · permissions |
| **release_priorities** | Bluetooth/NFC policy · hardware QA matrix · OTA coordination |
| **common_failure_patterns** | Pairing failures · firmware state mismatch · BT permission denial |
| **related_classes** | adjacent: `COMPANION`, `FIELD_OPERATIONS`, `UTILITY_TOOL` · migration: → `COMPANION` if device is extension of cloud platform |

---

### `UTILITY_TOOL`

| Field | Value |
|-------|-------|
| **code** | `UTILITY_TOOL` |
| **definition** | Single-purpose tool: converter, scanner, timer, simple tracker без platform dynamics |
| **primary_user** | Task-focused users |
| **business_objective** | Utility value; ads/subscription optional |
| **default_tier** | T1 |
| **tier_ceiling** | T2 |
| **allowed_modifiers** | `MOFF`, `MDEV` (narrow) |
| **critical_lifecycle_areas** | DESIGN → QA |
| **qa_priorities** | Core task correctness · a11y baseline · narrow device matrix |
| **release_priorities** | Fast cadence · low store risk |
| **common_failure_patterns** | Over-scoping into account/commerce · feature bloat |
| **related_classes** | adjacent: `CONVERSION_CLIENT`, `DEVICE_CONTROLLER` · migration: → `SERVICE_ACCOUNT` when accounts added |

---

### `AI_ASSISTANT` *(Core — AI Registry Layer §7)*

| Field | Value |
|-------|-------|
| **code** | `AI_ASSISTANT` |
| **definition** | Conversational product where chat/voice is the main surface |
| **primary_user** | Users seeking answers, support, tutoring via conversation |
| **business_objective** | Value delivered primarily through AI conversation |
| **default_tier** | T2–T3 |
| **tier_ceiling** | T4 |
| **allowed_modifiers** | `MPUSH`, `MOFF` (limited) |
| **forbidden_modifiers** | `AI_COPILOT` (is the class, not modifier) |
| **critical_lifecycle_areas** | PRODUCT_DEF → QA → LEGAL/STORE |
| **qa_priorities** | Safety · hallucination · escalation paths · content policy |
| **release_priorities** | Harmful output prevention · model fallback · disclosure |
| **common_failure_patterns** | Unsafe advice · no human escalation · opaque AI disclosure |
| **related_classes** | adjacent: `COMMUNICATION`, `CONTENT_CONSUMER` · migration: → `AI_AGENT_CONSOLE` if autonomous tool-use supervision required |

---

## 5. Extended Class Registry

**Правило Extended:** не default production target. `architecture_charter_required = true` always. `default_tier = T4 minimum`. HITL `mandatory` at G0 and pre-release.

### Why Extended exists (general)

Extended classes share: multi-party or regulated domains, platform-scale architecture, compliance gates that **cannot** use Core defaults without adaptation. Website Factory precedent: Extended Types require charter before design freeze.

---

### `MARKETPLACE`

| Field | Value |
|-------|-------|
| **why extended** | Multi-sided economics: buyers + sellers + operators; fraud, disputes, split payments — production path ≠ `COMMERCE` |
| **mandatory architecture charter** | Multi-role domain model · listing/trust/dispute flows · payment split · moderation architecture · seller onboarding |
| **mandatory approval requirements** | G0 HITL · legal review of platform terms · fraud posture sign-off · pre-release multi-role QA sign-off |
| **mandatory QA requirements** | Multi-role journey QA · payment split edge cases · dispute flows · fraud/abuse scenarios · seller verification |

**related_classes:** parent concept: `COMMERCE` · adjacent: `COMMUNICATION`, `FINTECH_WALLET` · migration: ← `COMMERCE`; → `FINTECH_WALLET` if regulated wallet layer

---

### `FINTECH_WALLET`

| Field | Value |
|-------|-------|
| **why extended** | Regulated money movement ≠ merchant checkout; licensing, KYC, audit trails |
| **mandatory architecture charter** | KYC/AML flow · ledger integrity · transaction audit · fraud detection · key management posture |
| **mandatory approval requirements** | Legal/licensing HITL · security review · store financial policy review · geography scope approval |
| **mandatory QA requirements** | KYC edge cases · transaction audit immutability · security regression · penetration-adjacent review |

**related_classes:** adjacent: `COMMERCE`, `MARKETPLACE`, `SERVICE_ACCOUNT` · migration: ← `SERVICE_ACCOUNT` or `COMMERCE` when regulated wallet emerges

---

### `HEALTH_MEDICAL`

| Field | Value |
|-------|-------|
| **why extended** | Clinical validity, patient data, telehealth — regulatory universe ≠ `FIELD_OPERATIONS` |
| **mandatory architecture charter** | Clinical data boundaries · consent model · role separation (patient/clinician) · audit for PHI-class data |
| **mandatory approval requirements** | Regulatory HITL mandatory · clinical advisor sign-off where applicable · geography compliance |
| **mandatory QA requirements** | Consent flows · clinical data handling · role separation QA · audit trail immutability |

**related_classes:** adjacent: `FIELD_OPERATIONS`, `SERVICE_ACCOUNT` · migration: ← `FIELD_OPERATIONS` when clinical/regulatory dominates

---

### `AI_AGENT_CONSOLE`

| Field | Value |
|-------|-------|
| **why extended** | Human supervises autonomous/semi-autonomous agents with tool use — safety, liability, kill-switch |
| **mandatory architecture charter** | Agent action audit · approval gates · kill-switch · escalation protocols · tool-use boundaries |
| **mandatory approval requirements** | AI safety HITL · liability review · operator training acknowledgment · pre-release autonomy limits |
| **mandatory QA requirements** | Kill-switch verification · audit immutability · tool-use safety scenarios · escalation path QA |

**related_classes:** adjacent: `AI_ASSISTANT`, `PRODUCTIVITY_WORKFLOW` · migration: ← `AI_ASSISTANT` when supervision of autonomous action required

---

## 6. Modifier Registry

**Global rule (AC-2):** max **2 mobile modifiers** + optional **1 AI modifier** (`AI_COPILOT`) per project unless charter.

---

### `MLOC` — Mobile Location-Critical

| Impact | Detail |
|--------|--------|
| **meaning** | Core value depends on location: maps, geo-fencing, background tracking |
| **production impact** | Location permission UX, geo accuracy requirements, map SDK integration |
| **architecture impact** | Location service abstraction, background location policy, geo data retention |
| **QA impact** | Permission flows, accuracy edge cases, background behavior, battery interaction |
| **release impact** | Store location justification, privacy label accuracy, geo-phased rollout |

**incompatible_with:** none; conflicts with `PWA_SHELL` when background location required (Decision artifact, not reclassification)

---

### `MOFF` — Mobile Offline-First

| Impact | Detail |
|--------|--------|
| **meaning** | Core workflows must function without connectivity |
| **production impact** | Sync engine, conflict resolution, offline UX states |
| **architecture impact** | Local persistence layer, sync protocol, conflict strategy |
| **QA impact** | Airplane mode suites, sync recovery, data loss scenarios |
| **release impact** | Staged sync rollout, migration of local data on upgrade |

**typical hosts:** `FIELD_OPERATIONS`, `LOGISTICS_MOBILE`, `PRODUCTIVITY_WORKFLOW`

---

### `MDEV` — Mobile Device-Integrated

| Impact | Detail |
|--------|--------|
| **meaning** | Deep hardware: BLE, NFC, sensors, pairing flows |
| **production impact** | Hardware test matrix, pairing UX, firmware-adjacent states |
| **architecture impact** | Device abstraction layer, pairing protocol, hardware capability detection |
| **QA impact** | Multi-device matrix, pairing failure recovery, permission flows |
| **release impact** | Bluetooth/NFC store declarations, hardware-specific release notes |

**typical hosts:** `DEVICE_CONTROLLER`, `FIELD_OPERATIONS`

---

### `MPUSH` — Push-Centric Retention

| Impact | Detail |
|--------|--------|
| **meaning** | Push notifications are primary retention/activation channel |
| **production impact** | Notification strategy, channel configuration, permission UX |
| **architecture impact** | Push provider integration, deep link routing, notification categories |
| **QA impact** | Permission opt-in/out, deep link correctness, notification content policy |
| **release impact** | Store notification disclosure, opt-in compliance |

---

### `MBG` — Background Execution

| Impact | Detail |
|--------|--------|
| **meaning** | Core value requires background tasks: tracking, sync, realtime |
| **production impact** | Battery tradeoffs, OS background limits, foreground service patterns |
| **architecture impact** | Background task scheduler, lifecycle-aware execution |
| **QA impact** | Battery drain tests, OS kill recovery, background state transitions |
| **release impact** | Store background mode justification, battery disclosure |

**typical hosts:** `LOGISTICS_MOBILE`, `FIELD_OPERATIONS`, `COMMUNICATION`

---

## 7. AI Registry Layer

### 7.1 Class vs Modifier Distinction

| Code | Type | Rule |
|------|------|------|
| `AI_ASSISTANT` | **Core class** | Conversation **is** the product |
| `AI_COPILOT` | **Modifier** | AI assists **inside** another class; requires host `product_class_code` |
| `AI_AGENT_CONSOLE` | **Extended class** | Human **supervises** autonomous agent actions |

**Decision test:** Does AI change store/legal/release **class** by itself? If no → modifier. If yes (standalone conversational product) → `AI_ASSISTANT`. If yes (autonomous supervision) → `AI_AGENT_CONSOLE`.

### 7.2 Production Differences

| | AI_ASSISTANT | AI_COPILOT | AI_AGENT_CONSOLE |
|--|--------------|------------|------------------|
| Host class | Self | Required | Self (Extended) |
| Primary surface | Chat/voice | Host workflow | Supervision console |
| Default tier | T2–T3 | Inherits host | T4 minimum |
| Architecture | Model routing, conversation state | Augmentation layer on host | Audit, kill-switch, approval gates |

### 7.3 QA Differences

| | AI_ASSISTANT | AI_COPILOT | AI_AGENT_CONSOLE |
|--|--------------|------------|------------------|
| Dominant QA | Safety, hallucination, escalation | Host QA + AI logging/override | Kill-switch, audit, tool-use safety |
| Human fallback | Required | Required per action class | Required by design |
| Content policy | Primary | Secondary to host | Primary for agent actions |

### 7.4 Safety Differences

| | AI_ASSISTANT | AI_COPILOT | AI_AGENT_CONSOLE |
|--|--------------|------------|------------------|
| Autonomy level | Responsive | Suggestive | Supervised autonomous |
| Liability posture | Content harm | Host bears primary; AI logged | Operator accountability |
| HITL depth | selective–often | selective | mandatory |
| Forbidden pattern | Autonomous tool execution without console | Standalone copilot app | Unsupervised agent release |

**Anti-pattern:** «AI-powered marketplace» → `MARKETPLACE` + optional `AI_COPILOT`, not new class.

---

## 8. Class Relationships

### 8.1 Relationship Types

| Type | Meaning |
|------|---------|
| **parent** | Conceptual specialization (not inheritance); child is stricter superset |
| **adjacent** | Frequently confused at G0; require disambiguation |
| **migration** | Documented re-classification path; requires G0 re-run |

### 8.2 Parent Relationships

```
COMMERCE ──parent──► MARKETPLACE
FIELD_OPERATIONS ──parent──► HEALTH_MEDICAL (when clinical/regulatory)
SERVICE_ACCOUNT ──parent──► FINTECH_WALLET (when regulated money)
AI_ASSISTANT ──parent──► AI_AGENT_CONSOLE (when autonomous supervision)
CONVERSION_CLIENT ──parent──► SERVICE_ACCOUNT (when relationship persists)
UTILITY_TOOL ──parent──► SERVICE_ACCOUNT (when accounts added)
```

### 8.3 Adjacent Relationships

| Pair | Disambiguation |
|------|----------------|
| `COMPANION` ↔ `SERVICE_ACCOUNT` | Parent product exists → `COMPANION`; mobile-native account product → `SERVICE_ACCOUNT` |
| `COMMERCE` ↔ `MARKETPLACE` | Single seller vs multi-sided platform |
| `FIELD_OPERATIONS` ↔ `LOGISTICS_MOBILE` | Job-site capture vs movement under SLA |
| `FIELD_OPERATIONS` ↔ `HEALTH_MEDICAL` | Proof-of-work vs clinical/regulated care |
| `PRODUCTIVITY_WORKFLOW` ↔ `FIELD_OPERATIONS` | Desk/knowledge vs physical-world execution |
| `COMMUNICATION` ↔ `CONTENT_CONSUMER` | Social graph/conversation vs media consumption |
| `DEVICE_CONTROLLER` ↔ `COMPANION` | Device control primary vs cloud product extension |
| `AI_ASSISTANT` ↔ `COMMUNICATION` | AI conversation product vs human social product |
| `COMMERCE` ↔ `FINTECH_WALLET` | Merchant checkout vs regulated wallet/transfers |

### 8.4 Migration Relationships

| From | To | Trigger |
|------|-----|---------|
| `CONVERSION_CLIENT` | `SERVICE_ACCOUNT` | Persistent accounts, billing, history |
| `UTILITY_TOOL` | `SERVICE_ACCOUNT` | Account model introduced |
| `COMMERCE` | `MARKETPLACE` | Multi-seller, disputes, split payments |
| `SERVICE_ACCOUNT` | `FINTECH_WALLET` | Regulated money movement |
| `FIELD_OPERATIONS` | `HEALTH_MEDICAL` | Clinical data, telehealth regulation |
| `AI_ASSISTANT` | `AI_AGENT_CONSOLE` | Autonomous tool-use supervision required |
| `COMPANION` | Native class | >60% standalone value vs parent |
| `MARKETPLACE` | `COMMERCE` | **Downgrade forbidden silently** — G0 + charter only |
| `HEALTH_MEDICAL` | `FIELD_OPERATIONS` | **Downgrade forbidden silently** — G0 + charter only |

---

## 9. Registry Validation Rules

### 9.1 Identity Validation

| Rule ID | Rule | On failure |
|---------|------|------------|
| **VR-1** | `product_class_code` must exist in registry v1 | REJECT — SAFE UNKNOWN + charter proposal |
| **VR-2** | `product_class_code` status must be `active` | REJECT — use successor or G0 review |
| **VR-3** | Modifier code must exist in modifier registry | REJECT |
| **VR-4** | `complexity_tier` must be T1–T4 | REJECT |

### 9.2 Combination Validation

| Rule ID | Rule | On failure |
|---------|------|------------|
| **VR-5** | Extended class → tier ≥ T4 | FORCE tier bump or REJECT |
| **VR-6** | Modifier must be in class `allowed_modifiers` | REJECT or charter |
| **VR-7** | Modifier in class `forbidden_modifiers` | REJECT |
| **VR-8** | Max 2 mobile modifiers (`MLOC`, `MOFF`, `MDEV`, `MPUSH`, `MBG`) | REJECT or tier bump + charter |
| **VR-9** | `AI_COPILOT` requires host class ≠ `AI_ASSISTANT` / `AI_AGENT_CONSOLE` | REJECT |
| **VR-10** | `AI_COPILOT` forbidden standalone (no host) | REJECT |
| **VR-11** | `AI_ASSISTANT` + `AI_COPILOT` simultaneously | REJECT |
| **VR-12** | Extended class requires `architecture_charter_required = true` artifact | BLOCK until charter |
| **VR-13** | `product_class_secondary` must differ from primary and be valid active class | REJECT |
| **VR-14** | Hybrid must include `classification_rationale` | REJECT at G0 |

### 9.3 Contradiction Prevention

| Rule ID | Rule |
|---------|------|
| **VR-15** | `UTILITY_TOOL` at T3+ without charter → REJECT |
| **VR-16** | `FINTECH_WALLET` or `HEALTH_MEDICAL` with `default_legal_posture` below `regulated`/`clinical` → REJECT |
| **VR-17** | `LOGISTICS_MOBILE` + `PWA_SHELL` + `MLOC` background → FLAG Decision review |
| **VR-18** | Marketing-only labels (`AI-powered`, `SuperApp`) as class codes → REJECT (AC-4) |
| **VR-19** | Technology codes (`FLUTTER_APP`, `IOS_APP`) → REJECT (AC-3) |
| **VR-20** | Dimension value used as class code (`INTERNAL_ENTERPRISE`) → REJECT (AC-9) |

### 9.4 Category Explosion Prevention

| Rule ID | Rule |
|---------|------|
| **VR-21** | New class requires merge review + charter; max 15 active classes (AC-1) |
| **VR-22** | Third mobile modifier → tier bump or class split review, not silent accept |
| **VR-23** | New modifier requires production-impact proof across ≥2 classes |

---

## 10. Registry Governance Rules

Operational rules only — **not** governance expansion.

### 10.1 Adding a New Class

1. **Trigger:** G0 encounters repeated SAFE UNKNOWN with same production path (≥2 projects evidence).
2. **Proposal:** charter with build-difference test vs nearest existing class.
3. **Review:** human merge review — can an existing class + modifier absorb it?
4. **Approval:** HITL sign-off; registry version bump (v1.1 doc revision).
5. **Constraint:** total active classes ≤ 15 unless AC-1 amended by explicit human charter.

### 10.2 Deprecating a Class

1. **Trigger:** zero projects in 12 months OR absorbed by modifier + existing class.
2. **Action:** set `status: deprecated`; document `successor_code`.
3. **Rule:** deprecated codes valid for existing projects only; new projects REJECT (VR-2).
4. **Annual pruning:** AC-10 documentation-only review.

### 10.3 Adding a Modifier

1. **Trigger:** recurring production concern across ≥2 classes not covered by dimensions.
2. **Proof:** distinct architecture + QA + release impact vs existing modifiers.
3. **Cap:** prefer dimensions over modifiers when possible.
4. **Approval:** lighter than new class; still requires HITL note in registry changelog.

### 10.4 When Class Split Is Justified

Split is justified **only** when:

- Build-difference test fails between sub-populations **consistently**;
- Default tier, QA, or release posture cannot be expressed as modifier;
- Merge review rejects modifier absorption.

Split is **not** justified for: marketing segments, technology stacks, geography, single client branding.

---

## 11. Registry Usage Rules

Future NOVA systems **must consume** registry; they **must not** invent parallel class vocabularies.

### 11.1 Lifecycle Model (future)

- **Reads:** `critical_lifecycle_areas`, `default_tier`, `class_group`
- **Rule:** phase mandatory/optional matrix keyed by `product_class_code`; registry row is SoT for defaults
- **Must not:** define new classes or rename phases per project ad hoc

### 11.2 Decision System (future)

- **Reads:** `allowed_modifiers`, `forbidden_modifiers`, `tier_ceiling`, Extended charter flags
- **Rule:** PWA allowed?, tier bump?, modifier stack? — decisions reference registry constraints (VR-5–VR-17)
- **Must not:** override Extended → Core without G0

### 11.3 Contracts (future)

- **Reads:** `default_legal_posture`, `qa_priorities`, Extended mandatory requirements
- **Rule:** legal/QA/integration contract packs select templates by `product_class_code` + tier + modifiers
- **Must not:** apply Core commerce legal defaults to Extended/regulated classes

### 11.4 QA (future)

- **Reads:** `qa_priorities`, modifier `qa_impact`, Extended mandatory QA
- **Rule:** QA matrix generation starts from registry ordered priorities
- **Must not:** use generic mobile QA checklist without class anchor

### 11.5 Release (future)

- **Reads:** `release_priorities`, `default_distribution`, modifier `release_impact`
- **Rule:** release gate checklist keyed by class + tier
- **Must not:** fast-track Extended or regulated classes

### 11.6 Future Agents (future)

- **Reads:** full registry for proposal generation
- **Rule:** agents **propose** `product_class_record`; human approves G0; registry validates (VR-*)
- **Must not:** auto-approve classification; auto-add classes (ORCA HITL lesson)

### 11.7 Consumption Contract Summary

```
product_class_record (instance)
        │
        ▼ validate against ──► Product Class Registry v1 (SoT)
        │
        ├──► Lifecycle Model    (phase criticality)
        ├──► Decision System    (constraints)
        ├──► Contracts          (default packs)
        ├──► QA                 (priority matrices)
        ├──► Release            (gate checklists)
        └──► Agents             (proposal only)
```

---

## 12. Anti-Chaos Rules

| ID | Rule | Registry enforcement |
|----|------|---------------------|
| **AC-1** | Max 15 active classes | VR-21 |
| **AC-2** | Max 2 mobile modifiers | VR-8, VR-22 |
| **AC-3** | No stack-driven classes | VR-19 |
| **AC-4** | No marketing classes | VR-18 |
| **AC-5** | Companion for parity apps (>60% mirror parent) | migration rules §8.4 |
| **AC-6** | Copilot never standalone | VR-9, VR-10 |
| **AC-7** | Extended cannot downgrade silently | migration rules §8.4 |
| **AC-8** | Hybrid explicit (primary + secondary + rationale) | VR-13, VR-14 |
| **AC-9** | Dimension ≠ class | VR-20 |
| **AC-10** | Annual pruning review | governance §10.2 |
| **AC-11** | No parallel vocabularies (Website Factory codes in mobile registry) | separate code namespaces |
| **AC-12** | Registry row fields are minimal — no project-specific data in registry | instance record separate |

**Operational principle:** registry stays **small, stable, production-meaningful**. When in doubt — modifier or dimension, not new class.

---

## 13. RBM Mapping

```
REALITY ─────────────────────────────────────────────
  │
  ├─ Production Model v1     … what NOVA is
  ├─ Product Taxonomy v1     … what classes exist; how to classify
  └─ Product Class Registry v1 … what each class MEANS operationally  ◄── HERE
  │
  │   Registry completes Reality vocabulary before any machinery assumes product shape.
  │
LIFECYCLE ── reads critical_lifecycle_areas, default_tier
  │
DECISIONS ── reads allowed/forbidden modifiers, tier_ceiling, Extended flags
  │
CONTRACTS ── reads default_legal_posture, qa_priorities, Extended mandatory reqs
  │
WORKFLOW ── varies stage graph by product_class_code (future)
  │
ROLES ── classifier, architect, QA profiles keyed by class (future)
  │
TOOLS ── helpers lookup registry rows (future)
  │
AGENTS ── propose classification; validate against registry (future)
  │
AUTOMATION ── last; only after stable registry consumption (future)
```

**Why Registry remains in Reality:**

Registry does not execute lifecycle, decide, or contract — it **defines the operational meaning of product classes** discovered by taxonomy. That is Production Reality: shared vocabulary with enforceable defaults. Machinery without this layer reinvents assumptions per project (the failure mode Website Factory addresses via Site Type Registry, and ORCA via evidence-first classification).

**RBM order preserved:** Registry is the **last Reality artifact** before Lifecycle design begins.

---

## 14. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Registry drift from taxonomy codes | High | Same `product_class_code` namespace; joint changelog |
| Registry bloat (too many fields) | Medium | AC-12; instance vs registry separation |
| Core defaults applied to Extended | High | VR-5, VR-12, Extended mandatory requirements |
| Modifier stacking hides class mis-fit | Medium | VR-8, VR-22, tier bump rule |
| AI modifier/class confusion | High | §7 distinction; VR-9–VR-11 |
| Premature machine-readable format | Low | v1 prose/table; format is SAFE UNKNOWN |
| Website Factory code bleed | Medium | AC-11 separate namespaces |
| Downgrade Extended → Core silently | High | AC-7, migration rules |

---

## 15. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| **NOVA Production Model v1 full text in repo** | **UNKNOWN** — approved conceptually; in-repo artifact not found |
| **NOVA Mobile Product Taxonomy v1 committed file** | **UNKNOWN** — design exists from prior session; not committed to repo at registry design time |
| **Exact NOVA lifecycle phase names/count** | **UNKNOWN** — registry uses conceptual phase names from taxonomy matrix |
| **Mobile legal pack scope and templates** | **UNKNOWN** — only `default_legal_posture` enum defined |
| **Store rules by geography** | **UNKNOWN** — release priorities documented; country matrix deferred |
| **Machine-readable registry serialization** | **UNKNOWN** — v1 is documentation registry (Website Factory v0 precedent) |
| **Tier numeric scoring automation** | **UNKNOWN** — tiers remain human-assigned at G0 |
| **PWA_SHELL as formal modifier code** | **UNKNOWN** — taxonomy treats as delivery/architecture; not in modifier registry v1 |
