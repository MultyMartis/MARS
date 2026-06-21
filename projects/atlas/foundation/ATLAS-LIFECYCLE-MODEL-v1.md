# ATLAS Lifecycle Model v1

**Status:** **documented** — Phase 5 normative lifecycle model for all ATLAS reality objects.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Foundation chain (Phase 5):** Phases 1–4 (approved) → **this document** → [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) → [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md) → [ATLAS-LIFECYCLE-GOVERNANCE-v1.md](ATLAS-LIFECYCLE-GOVERNANCE-v1.md) → [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md)  
**Is not:** workflow engine, PM tool, CRM pipeline, ticket system, cron, state-machine implementation, HR offboarding automation.

**Phase 1–4 constraint:** No changes to approved Phase 1–4 documents unless contradictions are discovered. Conflicts are reconciled in [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md); prior phase docs remain authoritative for domain detail; Phase 5 is the **unifying lifecycle vocabulary**.

---

## 1. Purpose

Establish **one canonical answer** to:

> **What state is this reality object in?**

Lifecycle semantics were previously distributed across entity registries, relationships, identity, attestation, and registry architecture. Phase 5 unifies them into a **single lifecycle language** for:

- Organization · Person · Project · Website · Domain  
- Relationship (structural edge)  
- Registry records (entity and relationship partitions)  
- Identity-bearing records (stable id + registry row)

Consumers (MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway, Secretary Systems, Document Systems, and future programs) **must not** invent parallel lifecycle meanings.

---

## 2. Lifecycle philosophy

### 2.1 Reality, not work

**Lifecycle** in ATLAS describes **the standing of a business-reality claim** in the registry — whether it is candidate, authoritative, contested, ended, superseded, or stored for audit.

| Lifecycle describes | Lifecycle does not describe |
|---------------------|----------------------------|
| Whether an org **exists** in canonical form | Whether a migration **task** is done |
| Whether a structural link **is current** | Whether a deal is **won** |
| Whether an id **is authoritative** | Whether a deploy **succeeded** |
| Whether a claim **is disputed** | Whether content is **in review** |

**Normative sentence:**

> Lifecycle is **epistemic and structural** — it states how ATLAS treats a record as knowledge of business reality, not how operators execute work.

### 2.2 Human-supervised evolution

Reality changes **slowly** and **explicitly**:

- Machines and consumers may **propose**; humans **attest** canonical promotion ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)).
- Ambiguity becomes **disputed** or **SAFE UNKNOWN**, never silent dual canonical ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md)).
- History is **preserved** — ended reality is deprecated, merged, replaced, or archived; not erased.

### 2.3 One vocabulary, facet extensions

All registry records share a **core universal state set** (see [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)).

Some object kinds require **facet terminal states** that refine universal semantics without breaking consumer mental models:

| Facet extension | Applies to | Universal meaning |
|-----------------|------------|---------------------|
| **replaced** | Relationship only | Superseded structural link (successor id required) |
| **merged** | Entity / identity record | Absorbed id; redirect to survivor |
| **split_source** | Entity / identity record | Source id after split; children documented |

Extensions are **not** separate lifecycles — they are normative refinements of **deprecated** / terminal history.

---

## 3. Lifecycle principles

| ID | Principle | Normative rule |
|----|-----------|----------------|
| **LC-P-01** | **Reality only** | No task, ticket, deal, or pipeline stage in lifecycle enum |
| **LC-P-02** | **Record-bound** | Lifecycle attaches to **registry records**, not aliases, evidence blobs, or consumer caches |
| **LC-P-03** | **Canonical clarity** | Only **active** (and attested historical terminals) ground irreversible consumer structural actions |
| **LC-P-04** | **Dispute blocks promotion** | **disputed** is never canonical; parallel **active** forbidden in contested slots |
| **LC-P-05** | **No silent delete** | Canonical rows end via deprecated / merged / replaced / archived — not purge |
| **LC-P-06** | **Id permanence** | Lifecycle end does not recycle ids ([ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)) |
| **LC-P-07** | **Attestation gates promotion** | proposed → active requires human attestation ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)) |
| **LC-P-08** | **SAFE UNKNOWN is valid** | Absence of active canonical is explicit — not invented placeholder |
| **LC-P-09** | **Cross-facet consistency** | Same state **name** means same **canonical posture** across entity and relationship registries |
| **LC-P-10** | **Operational isolation** | Consumer job status may mirror ATLAS only by **mapping table**, never by redefining ATLAS states |

---

## 4. What lifecycle means in ATLAS

### 4.1 Definition

**Lifecycle** is the **declared state** of a registry record that answers:

1. May consumers treat this record as **canonical structural truth** now?  
2. Is the claim **contested**?  
3. Has the claim **ended** or been **superseded**?  
4. Is the record **read-only historical**?

Lifecycle works together with:

| Companion concept | Role |
|-------------------|------|
| **Attestation** | Provenance and permission to promote or materially change state |
| **Effective dates** | When structural truth held (especially relationships) |
| **Identity redirect** | Survivor id after merge (`merged` + redirect) |
| **SAFE UNKNOWN** | Explicit gap when no active canonical exists for a subject/slot |

### 4.2 Lifecycle object scope

| Object | Lifecycle carrier | Notes |
|--------|-------------------|-------|
| Organization, Person, Project, Website, Domain | Entity registry **record** | Same state on record as identity lifecycle |
| Relationship | Relationship registry **record** | Adds **replaced** facet; effective dates required |
| Identity (conceptual) | **Not separate** from entity record | Phase 3 identity lifecycle = entity record lifecycle |
| Alias | No independent lifecycle | Alias validity follows parent entity state |
| Attestation event | Not a lifecycle state | Evidence for transitions |
| Consumer foreign key map | Not ATLAS lifecycle | Consumer-local until attested |

**Rule LC-OBJ-01:** Ask lifecycle on **`registry_record.lifecycle_state`**, not on display name, alias string, or CRM status.

### 4.3 Canonical posture matrix

| Lifecycle state | Canonical for forward structure? | Historical truth? |
|-----------------|----------------------------------|-------------------|
| **proposed** | No | No |
| **active** | Yes (if attested + slot rules satisfied) | Current |
| **disputed** | No | No (contest only) |
| **deprecated** | No (default joins) | Yes |
| **merged** | No (follow redirect) | Yes |
| **split_source** | No | Yes |
| **replaced** | No (follow successor) | Yes |
| **archived** | No (read-only) | Yes |

---

## 5. What lifecycle does not mean

### 5.1 Forbidden lifecycle thinking (operational)

These **must not** appear as ATLAS lifecycle states or registry enums:

| Forbidden term | Belongs to | ATLAS equivalent (if any) |
|----------------|------------|---------------------------|
| To Do · In Progress · Waiting | Task / PM tools | No lifecycle mapping |
| Completed · Closed (ticket) | Ticketing | No mapping |
| Lead · Opportunity · Won · Lost | CRM pipeline | Relationship end → **deprecated** / FORMER_* |
| Onboarding · PerformanceReview | HR workflows | Relationship type change / end |
| Draft · Published · Scheduled | Content/CMS ops | Consumer-local |
| Deployed · Failed · Rolling | CI/CD | Consumer-local |
| Churn score · Health score | Analytics | Consumer-local |

**Rule LC-BAN-01:** If the state answers “**where is the work?**” it is **not** ATLAS lifecycle.

### 5.2 Non-lifecycle metadata (allowed elsewhere)

| Metadata | Example | Storage |
|----------|---------|---------|
| Project closure note | “Initiative complete 2025” | Attestation note or consumer — not `lifecycle = completed` |
| Website “live” flag | DNS/probe | Consumer or optional non-canonical facet — not substitute for **active** |
| Person employment end | | **Relationship** FORMER_EMPLOYEE / deprecated edge |

Phase 1 warned: Project status lifecycle must not become workflow ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)). Phase 5 reaffirms: **closed project** → entity **deprecated** (structural retire), not “Completed” task state.

---

## 6. Lifecycle ownership

| Concern | Owner |
|---------|-------|
| Lifecycle vocabulary (states, transitions) | Phase 5 docs (this package) |
| Lifecycle transition execution | Registry steward / program owner ([ATLAS-LIFECYCLE-GOVERNANCE-v1.md](ATLAS-LIFECYCLE-GOVERNANCE-v1.md)) |
| Relationship slot + supersession detail | Phase 2 [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) — specialized rules, unified states |
| Merge / split / duplicate | Phase 3 [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) |
| Attestation tiers for promotion | [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) |
| Document amendments to lifecycle | Program owner + REPORT ([ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md)) |

**Rule LC-OWN-01:** Consumers **read** lifecycle; they **do not define** it.

---

## 7. Lifecycle boundaries

### 7.1 Internal boundaries

```text
┌─────────────────────────────────────────────────────────────┐
│  Lifecycle (Phase 5) — state of reality claim               │
├─────────────────────────────────────────────────────────────┤
│  Attestation (Phase 4) — trust to change state              │
├─────────────────────────────────────────────────────────────┤
│  Identity / Identifier (Phase 3) — stable id + redirect   │
├─────────────────────────────────────────────────────────────┤
│  Relationship semantics (Phase 2) — type, slot, dates       │
├─────────────────────────────────────────────────────────────┤
│  Reality / Taxonomy (Phase 1) — what may exist              │
└─────────────────────────────────────────────────────────────┘
```

**Rule LC-BND-01:** Lifecycle may not contradict Phase 1 boundaries ([ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md)).

**Rule LC-BND-02:** Upper layers reference Phase 5 state names; they do not introduce conflicting state enums.

### 7.2 External boundaries (consumers)

| Allowed | Forbidden |
|---------|-----------|
| Read `lifecycle_state` on canonical ids | Map CRM stage → ATLAS **active** without attestation |
| Cache lifecycle with TTL | Treat cache lifecycle as SoT over ATLAS |
| Propose transition to **proposed** | Auto **active** on import |
| Display human labels for states | Rename states in consumer UI enums (use mapping table) |

### 7.3 Business Scope

Business Scope (`andrey`, `sergey`, `roman`, etc.) **does not** define lifecycle partition or state ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-BS01).

---

## 8. Lifecycle invariants

| ID | Invariant |
|----|-----------|
| **LC-INV-01** | At most one **active** canonical entity record per attested business subject per entity class |
| **LC-INV-02** | At most one **active** canonical relationship per defined slot (Phase 2 RR-04) unless taxonomy allows multiplicity |
| **LC-INV-03** | **disputed** ∧ **active** on same record is forbidden |
| **LC-INV-04** | **merged** record must carry redirect to survivor; survivor may be **active** |
| **LC-INV-05** | **replaced** relationship must carry `replaced_by` successor id |
| **LC-INV-06** | **archived** records accept metadata correction only — not type/endpoint resurrection |
| **LC-INV-07** | Id in **merged** / **deprecated** / **archived** state is never reassigned to a new subject |
| **LC-INV-08** | **proposed** without attestation is never canonical for irreversible consumer actions |
| **LC-INV-09** | Ending relationship lifecycle does not delete endpoint entities |
| **LC-INV-10** | SAFE UNKNOWN at slot/subject level is not a lifecycle state — it is explicit absence of **active** canonical |

---

## 9. Architectural analysis (Phase 5 decisions)

### 9.1 What lifecycle states are truly universal?

**Decision:** Six **core** states are universal for all registry records:

`proposed` · `active` · `disputed` · `deprecated` · `archived`

Plus three **facet terminals** with universal semantics:

`merged` (entity) · `split_source` (entity) · `replaced` (relationship)

See [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) for evaluation of candidate list (PROPOSED, ACTIVE, DISPUTED, DEPRECATED, MERGED, ARCHIVED).

### 9.2 Can every entity use the same states?

**Decision:** **Yes** for core six. Entities use **merged** and **split_source**; relationships use **replaced** instead of merge. Project, Website, Domain, Organization, Person share identical core semantics.

### 9.3 Can a relationship be archived?

**Decision:** **Yes.** Phase 2 **archived** is affirmed as universal terminal read-only ([ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) §8).

### 9.4 Can a merged entity become active again?

**Decision:** **No** for the absorbed id. The **merged** id is permanently non-canonical; consumers follow redirect. Error correction is **governance reversal** (documented rare path), not casual `merged → active`. A **survivor** id remains or returns to **active** — that is not “reviving” the merged id.

### 9.5 Can archived records return?

**Decision:** **Generally no** to **active** for the same structural claim. **archived → active** is forbidden except **owner-approved error correction** (wrong archive) with audit ([ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md)). **deprecated → active** (“reactivation”) is allowed only when business subject was wrongly ended — requires re-attestation ([ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) §3.1).

### 9.6 How should disputes interact with active reality?

**Decision:** On a **contested record**, state is **disputed** — not **active**. On a **contested slot** (e.g. two OWNER claims), **no active canonical** in that slot until resolution; other facets of the same entities may remain **active** if unattested dispute does not apply.

### 9.7 Lifecycle attachment: entity, identity, relationship, or registry?

**Decision:** Primary attachment = **registry record** (entity or relationship row). Identity lifecycle **is** entity record lifecycle for MVP types. Relationships carry their own record lifecycle. “Registry” is the system; lifecycle is per **record**.

### 9.8 Relationship between lifecycle and attestation

**Decision:**

| Lifecycle | Attestation |
|-----------|-------------|
| **What** state the claim is in | **Why** the registry trusts a transition |
| Drives consumer canonical posture | Gates proposed → active and material changes |
| Includes disputed / deprecated | Includes evidence tier E0–E3 |

Promotion to **active** requires attestation block. **disputed** may be entered with lighter attest (flag). Resolution returns to attested **active** or **SAFE UNKNOWN**.

---

## 10. Consumer interpretation rule

When a consumer displays or branches on lifecycle:

1. Load **ATLAS canonical** `lifecycle_state` (not inferred from ops).  
2. Map to consumer UI labels via **local mapping table** — keys are ATLAS state codes only.  
3. If ATLAS is **disputed** or subject is **SAFE UNKNOWN**, consumer must not invent compensating canonical ids.  
4. If ATLAS is **merged** / **replaced**, resolve redirect / successor before structural writes.

Detail: future [Consumer Adoption Framework] package; contracts baseline in [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md).

---

## 11. Compliance checklist

- [ ] State is from Phase 5 registry, not ops vocabulary?
- [ ] Lifecycle queried on registry record, not alias?
- [ ] proposed / disputed excluded from irreversible canonical use?
- [ ] Merge uses **merged** + redirect, not delete?
- [ ] Relationship supersession uses **replaced**, not in-place type mutate?
- [ ] SAFE UNKNOWN used instead of placeholder entity?

---

*ATLAS Lifecycle Model v1 — unified philosophy. Documentation only.*
