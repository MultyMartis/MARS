# ATLAS Relationship Model v1

**Status:** **documented** — Phase 2 Relationship Foundation (normative).  
**Program:** ATLAS — **Business Reality Registry**  
**Classification:** Registry Layer · Cross-Cutting Infrastructure  
**Date:** 2026-06-04  
**Is not:** runtime, API, database, storage layout, registry implementation, CRM, ERP, HR system, workflow engine, automation.

**Foundation chain (Phase 2):** Phase 1 ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) → [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) → [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) → [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)) → **this document** → [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md) → [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) → [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md)

**Phase 1 constraint:** No changes to approved Phase 1 documents unless contradictions are discovered. None identified at Phase 2 authoring.

---

## 1. Mission of the relationship layer

Phase 1 established **what exists** — six MVP entity types and the principle that **Relationship** is first-class.

Phase 2 establishes **how things relate** — a canonical **relationship model** capable of describing business reality across the MARS ecosystem **without introducing new entities**.

| Layer | Question | Phase |
|-------|----------|-------|
| **Entities** | What exists? | Phase 1 |
| **Relationships** | How does it connect? | Phase 2 (this package) |
| **Identity mechanics** | How are ids, aliases, and merges governed? | Future (Identity Foundation) |
| **Registry mechanics** | How is truth stored and served? | Future (Registry Architecture) |

**Normative mission statement:**

> Express **durable, reviewable structural links** between canonical entities so humans and consumers share one **business graph** — ownership, participation, responsibility, representation, and commercial structure — **without** absorbing CRM pipelines, HR records, or financial ledgers.

---

## 2. Relationship philosophy

### 2.1 Structure is not execution

Relationships describe **who is connected to whom in business terms**, not **what work is due**, **what money moved**, or **what stage a deal is in**.

| Relationship answers | Relationship does not answer |
|------------------------|------------------------------|
| Andrey is **owner** of Polygon (structural) | Andrey’s tasks this week |
| Org A is **client of** Org B (structural) | Contract value or payment status |
| Website **belongs to** Project X (grouping) | Last deploy or PageSpeed score |
| Domain **points to** Website Y (identity routing) | DNS A-record operations |

### 2.2 Participation ≠ ownership (carried forward)

Phase 1 principle **CR-parallel**: a **Person** may hold **multiple** relationships to **multiple** **Organizations** with **different types** simultaneously. The relationship layer **must not** collapse participation into a single implicit `owner_id` on Person or Organization.

**Exemplar (illustrative, not canonical data):**

```text
Person: Andrey
  ──OWNER──► Organization: Polygon
  ──OWNER──► Organization: MetaCode
  ──MANAGER──► Organization: i-SEO
```

Each edge is an independent **Relationship** record with its own type, lifecycle, and attestation.

### 2.3 Edges are reality, not implementation detail

Foreign-key coupling hidden inside Website or Person records would make multi-hat models **invisible** and **non-auditable**. Treating **Relationship** as a **first-class reality object** means:

- links are **named** (typed),
- links are **time-bounded** (effective dates),
- links are **attested** (human supervision),
- links are **deprecatable** (history preserved).

### 2.4 Prefer typed edges over new entities

Aligned with [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) anti-bloat: **asset ownership**, **client structure**, and **representation** are expressed as **relationship types**, not new entity classes (Asset, Account, Contact).

### 2.5 Human-supervised truth

Machines may **propose** relationships in future implementation; **canonical** relationships require **human attestation** per [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md). Ambiguity resolves to **SAFE UNKNOWN**, never silent invention.

---

## 3. Why relationships are first-class reality objects

| Reason | Consequence if relationships were only hidden FKs |
|--------|---------------------------------------------------|
| **Multiplicity** | Cannot model Andrey → Polygon AND Andrey → MetaCode with different roles |
| **Semantics** | OWNER vs CONTRACTOR vs REPRESENTATIVE would be indistinguishable |
| **History** | Ownership transfer would overwrite without audit trail |
| **Conflict** | Disputed client claims could not coexist in reviewable form |
| **Deprecation** | Former client / former owner could not be preserved |
| **Consumer contract** | Downstream systems could not reference a stable `relationship_id` |

**Decision:** **Relationship** remains one of the six MVP entities ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §6). Phase 2 adds **normative type vocabulary and governance** — not a seventh entity.

---

## 4. Role of Relationship inside ATLAS

### 4.1 What a Relationship record represents

A **Relationship** is a **canonical or non-canonical assertion** that:

1. **Connects** two MVP entities (subject → object) with defined endpoint types per taxonomy family.
2. **Classifies** the link with exactly one **relationship type** from [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md).
3. **Optionally bounds** the link in time (effective start / end).
4. **Carries** lifecycle state and attestation metadata (see lifecycle doc).
5. **Does not embed** execution, financial, or pipeline semantics.

### 4.2 Relationship vs entity attributes

| Belongs on Relationship | Belongs on entity (if ever) |
|-------------------------|-----------------------------|
| OWNER, CLIENT_OF, REPRESENTS | Legal name, display name |
| effective_from / effective_to | Optional external CRM id (reference only) |
| superseded_by pointer | — |
| dispute flag / resolution notes | — |

**Rule RM-01:** If the fact is “**how A connects to B**,” it is a Relationship. If the fact is “**what A is**,” it is entity-level metadata subject to expansion rules.

### 4.3 Directed vs undirected semantics

All canonical types are **directed**: **subject** → **type** → **object**. Symmetric concepts (PARTNER_OF) are stored **once** with documented direction convention (see taxonomy §2). Inverse queries are a **consumer/view concern**, not duplicate canonical rows.

### 4.4 Cardinality (conceptual)

Cardinality rules are **per relationship type** (defined in taxonomy). Examples:

| Type | Cardinality intent |
|------|-------------------|
| PRIMARY_DOMAIN (Domain → Website) | At most **one canonical active** primary per Website |
| OWNER (Person → Organization) | **Many allowed** (multiple owners) unless human policy caps |
| CLIENT_OF (Org → Org) | **Many allowed**; conflicts resolved via governance |
| REPRESENTS (Person → Organization) | **Many persons** may represent one org; disputes governed |

Implementation enforces cardinality later; Phase 2 **documents intent**.

---

## 5. Relationship principles

| ID | Principle | Normative statement |
|----|-----------|---------------------|
| **RP-01** | **Typed structure only** | Every canonical Relationship has exactly one type from the approved taxonomy |
| **RP-02** | **Endpoint type safety** | Subject and object entity types must match the family’s allowed pair |
| **RP-03** | **No CRM/HR/finance leakage** | Types and notes must not encode deal stage, salary, invoice, or task state |
| **RP-04** | **One canonical slot** | For a defined canonical slot (type + endpoints + overlapping effective window), at most **one** canonical active Relationship |
| **RP-05** | **Non-canonical coexistence** | Proposals, drafts, and disputed records may coexist until human resolution |
| **RP-06** | **History is truth** | Ended relationships remain queryable; no silent delete |
| **RP-07** | **Supersession explicit** | Replacement uses lifecycle states and/or FORMER_* types — not overwrite |
| **RP-08** | **Uncertainty explicit** | Low-confidence links use attestation tier or SAFE UNKNOWN — not fake certainty |
| **RP-09** | **Consumer humility** | Consumers reference `relationship_id`; they do not fork parallel edge registries |
| **RP-10** | **Scope classification is not structure** | Business Scope (future) may tag or filter; it does not replace Relationship |

---

## 6. Canonical relationship rules

| Rule ID | Rule | Violation signal |
|---------|------|------------------|
| **RR-01** | Relationship endpoints must be MVP entity ids | Endpoint type not in Phase 1 set |
| **RR-02** | Relationship type must be in taxonomy v1 | Ad-hoc type string in canonical row |
| **RR-03** | Canonical promotion requires human attestation | Auto-promoted import without review |
| **RR-04** | Conflicting canonical slots require governance resolution | Two canonical OWNER with overlapping dates unresolved |
| **RR-05** | FORMER_* or ended state required when business link ends | Deleted edge with no historical record |
| **RR-06** | Disputed relationships are not canonical until resolved | Canonical flag on disputed row |
| **RR-07** | Relationship does not create entities | “Create org to fix link” automation |
| **RR-08** | Cross-family type reuse forbidden | CLIENT_OF used Person → Organization |
| **RR-09** | Notes are attestations, not contracts | Full contract text in relationship note |
| **RR-10** | Unknown type → SAFE UNKNOWN | Guessed type to unblock export |

---

## 7. Relationship identity rules

### 7.1 Relationship as identifiable object

Each Relationship (when implemented) carries an **opaque stable id** (`relationship_id`) independent of its type or endpoints.

| Rule | Detail |
|------|--------|
| **RI-01** | Ids are not recycled after archive |
| **RI-02** | Display labels for edges are derived (e.g. “Andrey OWNER Polygon”), not primary keys |
| **RI-03** | Changing type or endpoints on a canonical row is **supersession**, not id reuse |
| **RI-04** | Duplicate detection keys on: type + subject_id + object_id + effective_from (canonical policy) |

### 7.2 Canonical slot identity

A **canonical slot** is the logical place one active truth occupies:

```text
slot = (relationship_type, subject_id, object_id, slot_variant?)
```

`slot_variant` is optional — used where taxonomy defines sub-slots (e.g. PRIMARY vs SECONDARY domain role).

**RR-04 restated:** Two canonical Relationships must not occupy the same slot with overlapping effective intervals unless taxonomy explicitly allows multiplicity (e.g. multiple OWNER).

### 7.3 FORMER_* type identity

When a link ends, prefer:

1. **Lifecycle transition** to `deprecated` / `archived` with `effective_to`, **or**
2. **Type migration** to a paired FORMER_* type (e.g. CLIENT_OF → FORMER_CLIENT_OF),

documented in [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md). Both preserve **relationship_id** continuity for audit.

---

## 8. Relationship lifecycle overview

Full state machine: [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md).

| State (summary) | Meaning |
|-----------------|--------|
| **proposed** | Awaiting human review; non-canonical |
| **active** | Canonical, current structural truth |
| **deprecated** | Still visible; no longer authoritative for forward decisions |
| **replaced** | Superseded by another Relationship id |
| **disputed** | Competing claims; not canonical |
| **archived** | Historical record; read-only |

**Effective dating:** `effective_from` / `effective_to` bound **business time**, not record edit time. Record `attested_at` is separate metadata (governance doc).

---

## 9. Relationship conflict principles

### 9.1 Conflict classes

| Class | Example | Resolution posture |
|-------|---------|-------------------|
| **Slot collision** | Two canonical OWNER same Person→Org overlap | Human picks one canonical; other → replaced/disputed |
| **Semantic disagreement** | CLIENT_OF vs “prospect” import | Reject non-taxonomy types; map or UNKNOWN |
| **Multi-representative** | Three persons REPRESENT same org | Allowed if attested; flag overlap of authority in notes only |
| **Ownership unknown** | Domain owner unclear | No canonical OWNER; SAFE UNKNOWN + proposed candidates |
| **Consumer disagreement** | CRM says client; ATLAS says not | ATLAS canonical after reconciliation; else disputed |

### 9.2 Conflict does not imply CRM adjudication

Resolution produces **structural truth** (“who is client in the business graph”), not **commercial outcome** (won deal, revenue recognition).

### 9.3 Disputed coexistence

**Decision (Phase 2):** Multiple **disputed** or **proposed** Relationships **may coexist** for the same slot. Multiple **canonical active** Relationships **must not** occupy the same slot (unless taxonomy allows multiplicity).

---

## 10. Required architectural analysis

### 10.1 Can a relationship exist without certainty?

**Decision: YES — with tiered attestation.**

| Tier | Meaning | Canonical? |
|------|---------|------------|
| **attested** | Human confirms structural truth | Yes (if active) |
| **proposed** | Plausible, under review | No |
| **uncertain** | Known gap; candidates listed | No |
| **unknown** | No reliable type or endpoint | Record **SAFE UNKNOWN**; no fabricated canonical edge |

A Relationship record may exist in **proposed** or **disputed** state expressing **partial** knowledge (“likely CLIENT_OF, evidence pending”). **Canonical active** relationships require **attested** certainty on type and endpoints.

**Prohibition:** Inventing canonical OWNER to unblock Website Factory export when ownership is unknown.

### 10.2 Can multiple conflicting relationships coexist?

**Decision: YES for non-canonical; NO for canonical slot (default).**

| Coexistence | Allowed? |
|-------------|----------|
| proposed A + proposed B (same slot) | Yes — until review |
| disputed A + disputed B | Yes — visible conflict |
| canonical A + canonical B (same slot, overlapping dates) | **No** — governance must resolve |
| canonical OWNER + canonical FORMER_OWNER (sequential dates) | Yes — non-overlapping effective windows |

### 10.3 How should historical relationships be preserved?

**Decision: Immutable history with explicit end and supersession.**

- Set `effective_to` and move to **deprecated** or **archived**, **or** migrate type to **FORMER_*** variant.
- Retain **relationship_id**; link **replaced_by** to successor when applicable.
- **Never** silent delete canonical history.
- Queries for “who owned X in 2024?” use effective-date semantics (implementation later).

### 10.4 How should future Asset Ownership integrate?

**Decision: Relationship taxonomy evolution — no standalone Asset entity.**

| Asset surface | Expression |
|---------------|------------|
| Domain ownership | OWNER / CUSTODIAN / REGISTRANT (Org or Person ↔ Domain) |
| Website ownership | OWNS (Org ↔ Website) or OWNS (Org ↔ Project) chains |
| Brand / IP (future) | New **relationship types** after expansion review — not Asset node |

Aligns with [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §7.5 and [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §8.6.

**Effective dates mandatory** for ownership transfers. Finance encumbrance fields remain **out of scope**.

### 10.5 How should future Business Scope classification interact with relationships?

**Decision: Classification overlay — not a graph edge replacement.**

| Business Scope | Interaction with relationships |
|----------------|-------------------------------|
| **Status** | **NOT APPROVED** as entity ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §7.1) |
| **Future role** | Optional **scope tag** on Person, Organization, Project, or Relationship metadata |
| **Does not replace** | OWNER, CLIENT_OF, COMMISSIONED_BY — structural truth stays typed edges |
| **Example** | Andrey scope may **filter** view to edges touching Person(andrey) — not create “Scope entity → Org” |

**Risk if conflated:** Parallel org chart. Scope tags are **views and filters**, not **structural parents**.

---

## 11. Exemplar graph (illustrative)

Not canonical data — demonstrates **typed** Phase 2 model:

```text
Person(Andrey) ──OWNER──► Organization(Polygon)
Person(Andrey) ──OWNER──► Organization(MetaCode)
Person(Andrey) ──MANAGER──► Organization(i-SEO)

Person(Andrey) ──REPRESENTS──► Organization(ClientX)   [if attested]

Organization(Agency) ──CLIENT_OF──► Organization(ClientX)

Project(Pilot) ──COMMISSIONED_BY──► Organization(ClientX)
Website(Site) ──BELONGS_TO──► Project(Pilot)

Domain(www) ──PRIMARY_DOMAIN──► Website(Site)
```

---

## 12. Phase 2 deliverables and non-deliverables

| Delivered | Not delivered |
|-----------|---------------|
| Relationship model (this doc) | API / GraphQL |
| Relationship taxonomy | Database schema |
| Lifecycle + governance | Registry service |
| Architectural decisions §10 | Automation / n8n |
| | Identity merge mechanics (deferred) |
| | Storage layout (deferred) |

---

## 13. Contradiction check vs Phase 1

| Phase 1 statement | Phase 2 alignment |
|-------------------|-----------------|
| Relationship types deferred | Now specified in taxonomy doc — **not** a Phase 1 edit |
| One canonical fact per claim (§5.4) | Refined as **canonical slot** + RR-04 |
| CR-07 structure only | RR-09, RP-03 enforce |
| Business Scope not entity | §10.5 reaffirmed |
| Asset via relationships | §10.4 operationalized |

**No Phase 1 document amendments required.**

---

*ATLAS Relationship Model v1 — Phase 2 Foundation. Documentation only; no runtime claims.*
