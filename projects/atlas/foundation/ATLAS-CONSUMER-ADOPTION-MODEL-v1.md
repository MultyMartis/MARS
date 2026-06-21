# ATLAS Consumer Adoption Model v1

**Status:** **documented** — Phase 6 Consumer Adoption Foundation (normative).  
**Program:** ATLAS — **Business Reality Registry**  
**Classification:** Registry Layer · Cross-Cutting Infrastructure  
**Date:** 2026-06-04  
**Is not:** runtime, API, SDK, database, sync architecture, implementation charter, Business Scope specification.

**Foundation chain (Phase 6):** Phases 1–5 (approved) → **this document** → [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md) → [ATLAS-CONSUMER-MAPPING-RULES-v1.md](ATLAS-CONSUMER-MAPPING-RULES-v1.md) → [ATLAS-CONSUMER-GOVERNANCE-v1.md](ATLAS-CONSUMER-GOVERNANCE-v1.md) → [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)

**Phase 1–5 constraint:** No changes to approved Phase 1–5 documents unless contradictions are discovered. None identified at Phase 6 authoring.

**Extends (does not replace):** [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) — Phase 4 defines *interaction*; Phase 6 defines *adoption*, *interpretation*, and *governance readiness*.

---

## 1. Mission

ATLAS semantic foundations are complete: reality, relationships, identity, registry, lifecycle.

**Remaining risk:** interpretation drift — different consumers assigning different meanings to the same ATLAS vocabulary.

**Phase 6 mission:**

> Define what it means to **adopt** ATLAS as a consumer so that **one reality** is interpreted **the same way** across MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway, and future programs — without semantic forks.

**Normative slogan:**

> **One Reality. Many Consumers. No Semantic Forks.**

---

## 2. Consumer philosophy

### 2.1 ATLAS owns reality; consumers perform work

| ATLAS owns | Consumers own |
|------------|---------------|
| Canonical entity existence | Tasks, tickets, sprints |
| Structural relationships | Deals, pipelines, campaigns |
| Stable identifiers | Operational metrics, content |
| Lifecycle of registry records | Workflow states of work artifacts |
| Attestation outcomes | Approvals of contracts, invoices, deploys |

Consumers **reference** canonical structure to coordinate work. They **do not** become alternate registries.

### 2.2 Adoption is interpretive discipline, not integration

**Adoption** means a consumer program **commits** to:

1. Using ATLAS vocabulary **as defined** (not redefined locally).
2. Separating **canonical truth** from **local operational truth**.
3. Routing structural change through **propose / attest**, not silent overwrite.
4. Measuring readiness via [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md) (documentation-level).

Adoption does **not** require a live ATLAS API in Phase 6. A consumer may adopt **before** implementation exists by charter and mapping discipline.

### 2.3 Consumer-agnostic by design

Phase 6 rules apply **equally** to all consumers. Examples (MIG, Secretary) illustrate patterns; they confer **no special rights**.

### 2.4 Business Scope independence

**Business Scope** (e.g. operator lanes `andrey`, `sergey`, `roman`) is **classification metadata** — not identity, not ownership, not canonical partition ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-BS01).

**Rule CA-BS01:** Consumer adoption **must not** require Business Scope to interpret lifecycle, relationships, or identity.

**Rule CA-BS02:** Business Scope tags on consumer artifacts are **local classification**; they must not alter ATLAS canonical fields.

---

## 3. Adoption goals

| Goal ID | Goal | Success signal |
|---------|------|----------------|
| **CA-G01** | **Semantic unity** | `active`, `CLIENT_OF`, `OWNER` mean the same in every consumer charter |
| **CA-G02** | **No parallel canonical** | No consumer-maintained org/person/site registry marketed as canonical |
| **CA-G03** | **Explicit unknown** | Missing ATLAS facts surface as **SAFE UNKNOWN**, not invented ids |
| **CA-G04** | **Traceable reference** | Durable cross-system keys use ATLAS ids when canonical exists |
| **CA-G05** | **Governed challenge** | Disagreement with ATLAS uses dispute/challenge paths, not silent fork |
| **CA-G06** | **Mapping transparency** | Local statuses documented in mapping tables ([ATLAS-CONSUMER-MAPPING-RULES-v1.md](ATLAS-CONSUMER-MAPPING-RULES-v1.md)) |
| **CA-G07** | **Certifiable readiness** | Consumer self-assesses C0–C3 before claiming production reliance on ATLAS |

---

## 4. What it means to be an ATLAS consumer

A system is an **ATLAS consumer** when it:

| Criterion | Requirement |
|-----------|-------------|
| **C-ADOPT-01** | Declares itself a consumer in program charter or registry row |
| **C-ADOPT-02** | Documents which entity/relationship types it reads and references |
| **C-ADOPT-03** | Accepts [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md) as mandatory interpretation |
| **C-ADOPT-04** | Accepts Phase 4 [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) interaction limits |
| **C-ADOPT-05** | Maintains a published **consumer ↔ ATLAS mapping** where local statuses exist |
| **C-ADOPT-06** | Assigns an adoption owner (role or program lead) for governance contact |

**Non-consumer:** Tools that never reference ATLAS ids and never claim canonical business structure need not adopt — but must not publish conflicting canonical lists.

**Future consumers** (Secretary, Contract, Invoice, Act, Reporting, Administrative systems) adopt under the same criteria when they reference ATLAS structure.

---

## 5. Consumer responsibilities

Extends Phase 4 CR-* obligations with adoption-specific duties:

| Resp ID | Responsibility |
|---------|----------------|
| **CA-R01** | Publish **semantic contract compliance** statement (which SC-* rules apply) |
| **CA-R02** | Never store consumer workflow codes in ATLAS `lifecycle_state` fields |
| **CA-R03** | On read, interpret **merged** / **replaced** / **archived** per Phase 5 — follow redirects |
| **CA-R04** | Treat **disputed** and **proposed** as non-canonical for forward structural decisions |
| **CA-R05** | When local data conflicts with attested ATLAS, follow [ATLAS-CONSUMER-GOVERNANCE-v1.md](ATLAS-CONSUMER-GOVERNANCE-v1.md) §5 |
| **CA-R06** | Refresh or invalidate local cache after governance-notified canonical change (policy local until implementation) |
| **CA-R07** | Participate in certification review when requested (C1+) |

**Should (recommended):**

| Resp ID | Responsibility |
|---------|----------------|
| **CA-R-S01** | Version consumer mapping tables when ATLAS lifecycle docs amend |
| **CA-R-S02** | Log consumer-local “structural assumption” flags when ATLAS is SAFE UNKNOWN |
| **CA-R-S03** | Separate UI labels from persisted ATLAS codes in operator tools |

---

## 6. Consumer limitations

Consumers **may:**

| Permission | Reference |
|------------|-----------|
| Read canonical structure | [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) §3 |
| Reference ATLAS ids in artifacts | CC-01 |
| Classify locally (tags, scope, pilot labels) | CC classify; CA-BS02 |
| Propose structural change | Suggest / propose |
| Maintain **operational** lifecycle | [ATLAS-CONSUMER-MAPPING-RULES-v1.md](ATLAS-CONSUMER-MAPPING-RULES-v1.md) §3 |
| Cache ATLAS reads | CC-CACHE-01 |

Consumers **may not:**

| Prohibition | Rule ID |
|-------------|---------|
| Redefine ATLAS lifecycle vocabulary | CA-P01 |
| Redefine relationship type semantics | CA-P02 |
| Redefine identity or merge rules | CA-P03 |
| Create alternative canonical registries | CA-P04 (extends CC-P04) |
| Auto-attest proposals | CA-P05 (extends CC-P03) |
| Treat consumer cache as canonical on conflict | CA-P06 |
| Use Business Scope as org partition or ownership | CA-P07 |
| Map “work done” to ATLAS **deprecated** without attestation | CA-P08 |

---

## 7. Canonical interpretation requirements

Every consumer **must** interpret the following **exactly** as defined in upstream docs — local synonyms allowed **only** in display layers:

| Domain | Authoritative source | Consumer obligation |
|--------|---------------------|---------------------|
| Lifecycle states | [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Codes §3–§4 only; see Semantic Contract |
| Relationship types | [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md) | No new canonical types without expansion |
| Identity / ids | [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) | Permanent ids; redirect on **merged** |
| Attestation | [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) | **active** implies human attest |
| SAFE UNKNOWN | Reality + Lifecycle + Attestation | Posture, not a fake row |
| Canonical criteria | [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) C-01–C-06 | Forward joins use **active** only |

Detail: [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md).

---

## 8. What consumers must never do

**Absolute prohibitions (semantic fork triggers):**

1. **Rename ATLAS meaning** — e.g. treating consumer `closed` as ATLAS `deprecated` in the canonical store.
2. **Infer ownership** from CRM “account owner” without attested **OWNER** / **CLIENT_OF** relationship.
3. **Promote market discovery to canonical** — MIG competitors remain proposals until attested.
4. **Dual-write canonical** — consumer DB column mirrors ATLAS fields and diverges without dispute flag.
5. **Skip merged redirect** — continuing to use absorbed `ORG-*` as forward canonical.
6. **Invent ids under pressure** — export deadlines do not justify parallel canonical keys.
7. **Collapse SAFE UNKNOWN into `proposed`** — unknown is not “pending review” by default.

Violation handling: [ATLAS-CONSUMER-GOVERNANCE-v1.md](ATLAS-CONSUMER-GOVERNANCE-v1.md) §6.

---

## 9. Required architectural analysis (Phase 6 decisions)

### 9.1 Can consumers define their own lifecycle?

**Decision CA-D01:** **Yes — operational lifecycle only.**

| Layer | Consumer may define? | Examples |
|-------|---------------------|----------|
| **ATLAS registry lifecycle** | **No** | `proposed`, `active`, `deprecated` |
| **Consumer operational lifecycle** | **Yes** | SEO stage, sprint, deploy pipeline, CRM stage |
| **Mapping between layers** | **Yes, documented** | See Mapping Rules — must not overwrite ATLAS |

Consumer lifecycle describes **work progress**; ATLAS lifecycle describes **standing of a business-reality claim**.

### 9.2 Can consumers redefine relationship meaning?

**Decision CA-D02:** **No.**

Consumers may **display** localized labels (“Клиент”, “Владелец”) but **CLIENT_OF** and **OWNER** semantics are fixed by taxonomy. New structural meanings require [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md), not consumer config.

### 9.3 Can consumers maintain local caches?

**Decision CA-D03:** **Yes.**

Cache is **performance and UX** only ([ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) §6.2). On conflict with attested ATLAS, **ATLAS wins** ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §8.3).

### 9.4 Can consumers disagree with ATLAS?

**Decision CA-D04:** **Yes — through governed challenge, not fork.**

Consumers **flag dispute**, submit proposals, and withhold forward canonical reliance until resolution. They **must not** maintain a competing canonical graph.

### 9.5 How should consumers handle SAFE UNKNOWN?

**Decision CA-D05:**

| Situation | Required behavior |
|-----------|-------------------|
| No **active** canonical for needed subject | Mark dependency **SAFE UNKNOWN**; no invented `ORG-*` |
| **proposed** exists but unattested | May reference with **risk flag**; not forward canonical |
| **disputed** slot | Block structural automation; escalate |
| Consumer has local name only | Local foreign key + proposal intake |

See Semantic Contract §6 and Governance §4.

### 9.6 Can consumers maintain local classifications?

**Decision CA-D06:** **Yes.**

Tags (`pilot-2026`, `scope-andrey`, priority, internal portfolio) are **non-canonical**. They must not impersonate entity types, relationship types, or lifecycle states.

### 9.7 What happens when consumer data conflicts with ATLAS?

**Decision CA-D07:**

```text
1. Detect conflict (import, cache refresh, operator report)
2. If ATLAS active + attested (C-01–C-06) → consumer updates local pointers/labels
3. If ATLAS disputed / unknown → consumer stops forward canonical use; flag UNKNOWN
4. If consumer believes ATLAS wrong → challenge path (Governance §3)
5. No auto-merge, no silent dual canonical
```

### 9.8 What is the difference between local truth and canonical truth?

**Decision CA-D08:**

| | **Canonical truth (ATLAS)** | **Local truth (consumer)** |
|--|----------------------------|----------------------------|
| **Definition** | Attested, active structural business reality | Operational state of work and artifacts |
| **Authority** | Human attestation + registry governance | Consumer program owners |
| **Examples** | `ORG-*` exists; `CLIENT_OF` active | Deal stage; SERP pack; deploy hash |
| **Durability** | Slow-changing; audit preserved | High-churn |
| **Cross-system key** | ATLAS id when canonical | Consumer-native ids |
| **On conflict** | Wins for structure | Wins for operations |

---

## 10. Known consumers (reference)

**Current:** MIG · ORCA · Website Factory · WPilot · OCPilot · HomeGateway  

**Future:** Secretary · Contract · Invoice · Act · Reporting · Administrative · future MARS programs

Profiles remain in [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) §8; Phase 6 adds certification targets in [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md).

---

## 11. Phase 6 deliverables and non-deliverables

| Delivered | Not delivered |
|-----------|---------------|
| Adoption model (this doc) | Runtime service |
| Semantic contract | API specification |
| Mapping rules | Sync / cache protocol |
| Consumer governance | Database schema |
| Certification levels (C0–C3) | Automated certification engine |

---

## 12. Open items for downstream packages

| Item | Suggested owner package |
|------|-------------------------|
| Initial canonical population priorities | Registry Population Strategy |
| Steward roster and intake SLA | ATLAS Operational Model |
| Business Scope field standard | Business Scope Foundation |
| Technical read/propose channels | Implementation Planning (when chartered) |

---

*ATLAS Consumer Adoption Model v1 — Phase 6 Foundation. Documentation only.*
