# ATLAS Entity Registry Model v1

**Status:** **documented** — Phase 4 normative model for entity registries (conceptual).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md)  
**Is not:** database schema, table design, API, storage layout, UI forms, sync jobs.

**Phase 1–3 constraint:** No changes to approved Phase 1–3 documents unless contradictions are discovered. None identified at Phase 4 authoring.

---

## 1. Purpose

Define **how entity registries conceptually work** within ATLAS — one registry discipline applied across Organization, Person, Project, Website, Domain, and Relationship — without designing storage or schemas.

---

## 2. Entity registry concept

An **entity registry** is a **logical partition** of ATLAS that:

1. Holds records of **one entity class** (or Relationship as link class);
2. Applies the **same canonical rules** (attestation, lifecycle, identity);
3. Exposes **stable ids** in a defined namespace;
4. Participates in the **single business reality graph**.

Entity registries are **not separate products** — they are **views of one registry system** ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §3).

```text
                    ATLAS Business Reality Registry
                                    │
        ┌───────────┬───────────┬───┴───┬───────────┬───────────┐
        ▼           ▼           ▼       ▼           ▼           ▼
   Organization  Person    Project  Website    Domain   Relationship
     Registry    Registry  Registry Registry  Registry   Registry
```

---

## 3. Registry ownership

### 3.1 Who owns the registry system?

| Owner | Scope |
|-------|-------|
| **ATLAS program** | Registry architecture, taxonomy version, expansion approval |
| **Program owner / operator** | Final attestation, merge/split approval, dispute resolution |
| **Registry steward** | Intake, triage, delegated attestation, evidence review |

Consumers **do not own** any entity registry partition.

### 3.2 What each registry owns

| Registry | Owns (canonical) | Does not own |
|----------|------------------|--------------|
| **Organization** | That a business unit exists as attested org | CRM pipeline, GL, payroll |
| **Person** | That a natural person exists in the graph | HR employee record, WP login |
| **Project** | Structural work container identity | Tasks, sprints, Gantt |
| **Website** | Web property identity | Deploy state, CMS posts |
| **Domain** | Hostname/domain identity anchor | DNS console, SSL ops |
| **Relationship** | Structural edge between entities | Campaign membership execution |

Ownership means **authority to attest canonical records in that partition**, not legal title in the business world. “OWNER” relationship type (Phase 2) expresses **structural** ownership claims — still not financial ledger ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md)).

### 3.3 Rule ER-OWN-01

No consumer may be designated **owner** of an entity registry partition. Consumers hold **operational data** linked by reference.

---

## 4. Canonical records

### 4.1 Record anatomy (conceptual, not schema)

Every entity registry record conceptually includes:

| Facet | Description |
|-------|-------------|
| **Stable id** | Opaque canonical identifier ([ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)) |
| **Entity class** | Organization, Person, etc. |
| **Lifecycle state** | proposed · active · disputed · deprecated (and variants per Phase 2 relationship lifecycle) |
| **Canonical display** | Human-readable primary label (not a substitute for id) |
| **Attestation block** | Who attested, when, evidence tier ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)) |
| **Alias hooks** | Links to alias records where applicable ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |

Forbidden as **core canonical fields**: task status, invoice totals, SERP ranks, deploy hashes, deal values.

### 4.2 Canonical record rules (entity registries)

| Rule ID | Rule |
|---------|------|
| **ER-CR-01** | One **active** canonical record per attested business subject per class |
| **ER-CR-02** | Promotion to active requires human attestation |
| **ER-CR-03** | Ids are not recycled; deprecation uses tombstone semantics ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-08) |
| **ER-CR-04** | Cross-registry references use **ids only**, not display-name joins |
| **ER-CR-05** | Relationship registry records must reference **existing or co-proposed** entity ids |

### 4.3 Non-canonical records

| State | Consumer use |
|-------|----------------|
| **proposed** | May reference for intake; must not treat as SoT for irreversible actions |
| **disputed** | Do not use for new canonical links until resolved |
| **deprecated** | Historical reference only; follow redirect/successor rules when defined |

---

## 5. Lifecycle interaction

Entity registries share a **common lifecycle discipline** aligned with Phase 2 relationship lifecycle and Phase 3 identity events:

```text
Intake (human or consumer proposal)
    → proposed (evidence attached)
    → review (steward / owner)
    → active (canonical)  OR  disputed  OR  SAFE UNKNOWN (hold)
    → deprecated (tombstone; successor links if merge)
```

### 5.1 Lifecycle by registry (high level)

| Registry | Typical intake trigger | Typical deprecation trigger |
|----------|------------------------|----------------------------|
| **Organization** | New client brand, merger | Merger absorbed, duplicate merge |
| **Person** | New participant in graph | Duplicate merge; role end does not delete person |
| **Project** | New initiative container | Initiative closed — structural retire |
| **Website** | New site pack / deploy target | Site retired — id tombstoned |
| **Domain** | New hostname anchor | Domain sold/transferred — update relationships |
| **Relationship** | New structural link attested | Link ended — deprecate edge, not entities |

**Rule ER-LC-01:** Ending a relationship **does not** delete endpoint entities.

**Rule ER-LC-02:** Project closure **does not** delete websites or orgs — only project record lifecycle.

Detailed cross-registry lifecycle packaging is deferred to a future **Registry Lifecycle Foundation** package (see Phase 4 REPORT).

### 5.2 Interaction with relationship lifecycle

Entity promotion may **depend on** required relationships (e.g. Website without owning Organization → gap flagged, not auto-org). Relationship promotion follows [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) and [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md).

---

## 6. Identity interaction

Entity registries **consume** Phase 3 identity rules; they do not redefine them.

| Event | Registry impact |
|-------|-----------------|
| **New id assigned** | Record created in proposed or active per attestation |
| **Alias added** | Same entity id; alias registry facet ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |
| **Merge** | Survivor id retains active; loser deprecated with redirect |
| **Split** | Owner-approved; new ids; relationships re-homed |
| **Identifier correction** | Rare; governed by [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) |

**Rule ER-ID-01:** Entity registry operations **must** use canonical ids in all cross-registry pointers.

**Rule ER-ID-02:** Display-name change **never** implies entity merge.

---

## 7. Entity registry specifications

### 7.1 Organization Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Canonical business units ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §1) |
| **Id namespace** | `ORG-*` (per [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)) |
| **Typical relationships** | OWNER, CLIENT_OF, PARTNER, parent via structural edge |
| **Consumer examples** | Factory client org; ORCA pilot subject; MIG competitor org (reference only) |
| **Common failure** | Creating org from CRM import without attestation |

### 7.2 Person Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Natural persons independent of single org |
| **Id namespace** | `PER-*` |
| **Typical relationships** | EMPLOYEE, CONTRACTOR, REPRESENTATIVE, OWNER (person-org) |
| **Multi-hat** | Multiple active relationships to different orgs allowed |
| **Common failure** | Collapsing person into “contact sub-record” of one org |

### 7.3 Project Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Structural grouping — not PM ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §8.4) |
| **Id namespace** | `PRJ-*` |
| **Typical relationships** | Project ↔ Organization, Project ↔ Website, Person participation |
| **Common failure** | Storing tasks, budgets, or sprint state on project record |

### 7.4 Website Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | Registered web property identity |
| **Id namespace** | `WEB-*` |
| **Typical relationships** | PRIMARY_DOMAIN, operated-by org, belongs-to project |
| **Common failure** | Canonical “last deploy” or PageSpeed score on website record |

### 7.5 Domain Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | DNS/hostname identity anchor — not DNS ops |
| **Id namespace** | `DOM-*` |
| **Typical relationships** | PRIMARY_DOMAIN to Website, OWNS to Organization |
| **Common failure** | MX/TXT live values as canonical fields |

### 7.6 Relationship Registry

| Aspect | Specification |
|--------|---------------|
| **Purpose** | First-class structural edges ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md)) |
| **Id namespace** | `REL-*` (or equivalent — implementation future) |
| **Cardinality** | Per taxonomy rules — one active canonical per kind+pair where required |
| **Common failure** | Encoding CRM deal stage as relationship type |

---

## 8. Cross-registry integrity

| Rule ID | Rule |
|---------|------|
| **ER-X-01** | No active Website without resolvable Organization **or** explicit SAFE UNKNOWN flag on the gap |
| **ER-X-02** | Domain must not be active canonical for two conflicting PRIMARY_DOMAIN targets without dispute |
| **ER-X-03** | Relationship endpoints must reference ids in approved entity classes |
| **ER-X-04** | Merge in one registry triggers **relationship reconciliation** ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) §8) |

---

## 9. Business Scope independence

Entity registries **must not** be sharded or filtered by Business Scope labels. Scope may tag **consumer-side** reporting; it does not partition canonical storage architecture ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §7.3).

---

## 10. Non-deliverables (reaffirmed)

No storage design, schemas, APIs, synchronization, or automation in this document.

---

*ATLAS Entity Registry Model v1 — Phase 4 Foundation. Documentation only.*
