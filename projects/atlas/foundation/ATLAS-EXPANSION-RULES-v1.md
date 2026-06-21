# ATLAS Expansion Rules v1

**Status:** **documented** — Phase 1 governance for entity and scope growth.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) · [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md)  
**Is not:** implemented approval workflow, ticketing integration, or automated gate.

---

## 1. Purpose

Prevent **uncontrolled registry bloat** and **category drift** while allowing ATLAS to evolve deliberately after Phase 1 foundation. Every new entity type, canonical field class, or relationship semantics package requires **explicit human approval** documented in MARS.

---

## 2. Entity admission criteria

A candidate **must satisfy all** to enter canonical taxonomy:

| Criterion | Test |
|-----------|------|
| **A-01 Identity necessity** | Downstream consumers need a **stable business id** not satisfiable by existing MVP entity + Relationship |
| **A-02 Durability** | Expected lifespan months+ — not session-scoped or campaign-scoped |
| **A-03 Boundary cleanliness** | Cannot be classified as excluded domain in [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) §3 |
| **A-04 Human attestability** | Humans can meaningfully confirm “this exists” without machine-only inference |
| **A-05 Consumer plurality** | At least **two** future consumers benefit, **or** one consumer with critical SoT gap |
| **A-06 Non-redundancy** | Not expressible as Relationship between existing types |
| **A-07 Anti-PM/finance** | Does not embed tasks, money, pipeline, or metrics as core semantics |

**Failure of any criterion → reject or defer** (document in expansion log / REPORT).

---

## 3. Review requirements

### 3.1 Minimum review package

Before approving expansion:

| Artifact | Content |
|----------|---------|
| **Proposal** | Problem statement, consumers affected, 12-month horizon |
| **Boundary impact** | Explicit § exclusion check |
| **Taxonomy sketch** | Purpose, examples, non-examples |
| **Overload analysis** | Why not Relationship / metadata on existing entity |
| **Migration** | How non-canonical references convert |
| **Decision record** | Approve / defer / reject with date and owner |

### 3.2 Approval authority

| Phase | Authority |
|-------|-----------|
| Phase 1 (documentation) | Operator / program owner sign-off in REPORT or decision doc |
| Future implementation | Same + amendment to ATLAS-ENTITY-TAXONOMY and BOUNDARIES |

No agent may self-approve expansion.

### 3.3 Cooling period

After **reject**, same candidate may not be resubmitted for **30 days** without new evidence (changed consumer requirement or failed alternative).

---

## 4. Anti-bloat principles

| Principle | Rule |
|-----------|------|
| **Prefer edges over nodes** | Add Relationship type before new entity |
| **Prefer metadata over entity** | Classification labels on existing types before new type |
| **Prefer consumer-local over canonical** | High-churn operational data stays downstream |
| **One graph** | No parallel “shadow” entities for same real-world object |
| **Cardinality discipline** | Document max links per type when taxonomy arrives |
| **Deprecation over proliferation** | Merge duplicates — do not spawn `org-2` |
| **No speculative entities** | “We might need X” is not admission criterion A-01 |

---

## 5. Governance requirements

| Req ID | Requirement |
|--------|-------------|
| **G-01** | Expansion decisions are **written**, not chat-only |
| **G-02** | Approved changes bump taxonomy **version** (v1 → v2) |
| **G-03** | Rejected candidates stay listed as **NOT APPROVED** with rationale |
| **G-04** | Implementation charters reference approved taxonomy version only |
| **G-05** | Boundary doc updated **before** entity taxonomy when exclusions shift |
| **G-06** | MARS `registry/project-registry.md` row for `atlas` added only when operator registers program — **SAFE UNKNOWN** until then |

---

## 6. Field and attribute expansion (on existing entities)

Lower bar than new entity, still governed:

| Change type | Review |
|-------------|--------|
| Display name, alias | Human attestation — light review |
| Optional contact URL | Light review + PII note |
| External system foreign key (CRM id) | Medium — must not import pipeline |
| Status lifecycle on Project | Medium — must not become workflow |
| Financial or task fields | **Forbidden** — boundary violation |

---

## 7. Future candidate handling

Candidates discussed in program request. **All below: NOT APPROVED FOR PHASE 1.**

---

### 7.1 Business Scope

| Attribute | Value |
|-----------|-------|
| **Status** | **NOT APPROVED FOR PHASE 1** |
| **Concept** | Classification metadata grouping business activity (e.g. `andrey`, `sergey`, `roman`) |
| **Examples** | Andrey scope: Polygon, MetaCode, i-SEO client portfolio handled by Andrey |
| **Why not entity** | Not a company, not CRM pipeline, not accounting unit, not org division |
| **Phase 1 allowance** | Mention in narrative and philosophy only |
| **Admission path** | Metadata on Person/Organization/Project **or** tagged Relationship — requires Phase 2 proposal |
| **Risk if rushed** | Second org chart parallel to Organization |

---

### 7.2 Cluster

| Attribute | Value |
|-----------|-------|
| **Status** | **NOT APPROVED FOR PHASE 1** |
| **Concept** | Grouping of websites/domains by similarity or SERP cluster |
| **Why deferred** | Overlaps MIG analytics and marketing segmentation — drift into SEO tool |
| **Admission path** | Only if A-01–A-07 pass **and** boundary proves non-MIG ownership — unlikely |
| **Alternative** | MIG session tags; consumer-local cluster ids |

---

### 7.3 Portfolio

| Attribute | Value |
|-----------|-------|
| **Status** | **NOT APPROVED FOR PHASE 1** |
| **Concept** | Client portfolio under an operator scope |
| **Why deferred** | Collides with Business Scope and CRM “portfolio” language |
| **Admission path** | Merge with Business Scope metadata decision — single review |
| **Alternative** | Project + Organization relationships |

---

### 7.4 Environment

| Attribute | Value |
|-----------|-------|
| **Status** | **NOT APPROVED FOR PHASE 1** |
| **Decision** | **Reject** as Phase 1 entity ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §8.5) |
| **Concept** | staging / production / dev deployment slice |
| **Why rejected** | Deployment topology; pulls ops into registry |
| **Admission path** | Revisit only as **optional metadata** on consumer contracts or Website — not sibling entity |
| **Alternative** | WPilot/OCPilot/CI environment tables |

---

### 7.5 Asset Ownership

| Attribute | Value |
|-----------|-------|
| **Status** | **NOT APPROVED FOR PHASE 1** — **Phase 2 consideration** |
| **Decision** | Likely **relationship taxonomy evolution**, not standalone Asset entity |
| **Concept** | Who owns domain, site, or brand asset |
| **Why deferred** | Premature Asset entity duplicates Domain/Website; invites encumbrance and finance fields |
| **Admission path** | ATLAS-RELATIONSHIP-FOUNDATION defines OWNER / custodian types with effective dates |
| **Alternative** | Typed Relationship Person/Organization ↔ Domain/Website |

---

## 8. Recorded Phase 1 decisions (expansion lens)

| Topic | Decision | Package |
|-------|----------|---------|
| **Project** | **Keep** in MVP | [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §3 |
| **Environment** | **Reject** Phase 1 entity | §7.4 above |
| **Asset Ownership** | **Phase 2** via relationships | §7.5 above |
| **Registry naming** | **ATLAS = Business Reality Registry** | [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §9 |

---

## 9. Relationship taxonomy expansion (pointer)

Relationship **types** (OWNER, PARTNER, EMPLOYEE, CONTRACTOR, MANAGER, REPRESENTATIVE) are **not** Phase 1 deliverables. Admission of typed edges is a **separate package**:

- **Candidate next package:** `ATLAS-RELATIONSHIP-FOUNDATION` (if consumer handoff review shows blocking gaps).

Criteria for that package (preview):

| Criterion | Required |
|-----------|----------|
| Consumer cannot operate with untyped edges | Documented in REPORT |
| Types are structural, not HR/payroll | Boundary check |
| Cardinality rules per type | Included in foundation doc |
| No automatic promotion from imports | Human attestation |

---

## 10. Rejection log template (for future use)

```markdown
## Expansion rejection — <candidate>
- **Date:**
- **Candidate:**
- **Decision:** REJECT | DEFER
- **Failed criteria:** A-0x, ...
- **Rationale:**
- **Alternative:**
- **Resubmit after:**
```

---

## 11. Versioning

| Version | Scope |
|---------|-------|
| **v1** | Six MVP entities, untyped Relationship, no Environment, no Scope entity |
| **v2+** | Requires this expansion process + taxonomy amendment |

---

*ATLAS Expansion Rules v1 — admission, governance, future candidates NOT APPROVED FOR PHASE 1.*
