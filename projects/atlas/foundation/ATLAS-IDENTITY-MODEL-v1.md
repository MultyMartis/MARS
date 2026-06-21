# ATLAS Identity Model v1

**Status:** **documented** — Phase 3 Identity Foundation (normative).  
**Program:** ATLAS — **Business Reality Registry**  
**Classification:** Registry Layer · Cross-Cutting Infrastructure  
**Date:** 2026-06-04  
**Is not:** runtime, API, database, storage layout, registry implementation, sequence generator, CRM contact merge, ERP party master, HR employee id system, DNS registrar console, master data management (MDM) platform.

**Foundation chain (Phase 3):** Phase 1 ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) → [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) → [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) → [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)) → Phase 2 ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) → [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md) → [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) → [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md)) → **this document** → [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) → [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) → [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)

**Phase 1–2 constraint:** No changes to approved Phase 1–2 documents unless contradictions are discovered. None identified at Phase 3 authoring.

---

## 1. Mission of the identity layer

| Layer | Question | Phase |
|-------|----------|-------|
| **Entities** | What exists? | Phase 1 |
| **Relationships** | How does it connect? | Phase 2 |
| **Identity** | How is each thing **uniquely** known and distinguished? | Phase 3 (this package) |
| **Registry mechanics** | How is truth stored and served? | Future (Registry Architecture) |

Phase 1 established **what** may exist in business reality. Phase 2 established **how** entities link. Phase 3 establishes **how reality is uniquely identified** so humans and consumers can reference the **same** organization, person, project, website, domain, or relationship record **without** identity drift, silent duplication, or accidental forks.

**Normative mission statement:**

> Preserve **one canonical identity per business entity** — independent of display names, consumer foreign keys, and operational logins — while making **uncertainty explicit** and **history auditable**.

---

## 2. Identity philosophy

### 2.1 Identity serves business reality

Identity exists to answer: **“Which thing in the business graph do we mean?”** — not to optimize search, marketing segmentation, or access control.

| Identity supports | Identity does not replace |
|-------------------|---------------------------|
| Cross-system reference (`ORG-…`, `PER-…`) | CRM pipeline stage |
| Durable audit (“this id always meant Polygon”) | ERP GL posting |
| Alias disambiguation (Полигон vs WSP) | WordPress user login |
| Merge/split history | Task assignee id |

### 2.2 Names are not identity

Display names, trade names, transliterations, and abbreviations **change** and **collide**. Canonical identity is carried by an **opaque stable identifier** assigned once and governed for life ([ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)).

**Exemplar (illustrative):**

```text
Organization id: ORG-00042   (canonical, stable)
  canonical_name: Polygon
  aliases: Полигон · Web Studio Polygon · WSP
```

Consumers must **never** use `Polygon` or `WSP` as the primary key in durable contracts.

### 2.3 Identity before execution (reaffirmed)

Execution systems attach work to **ATLAS ids**. They do not mint parallel business org charts. If a consumer lacks an id, the correct posture is **proposed intake** or **SAFE UNKNOWN** — not a permanent shadow entity ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-10).

### 2.4 Human-supervised canonical identity

| Tier | Meaning | Canonical entity? |
|------|---------|-------------------|
| **attested** | Human confirms this id is the correct business entity | Yes |
| **proposed** | Plausible duplicate or new entity under review | No |
| **uncertain** | Candidates listed; same vs different undecided | No |
| **unknown** | Cannot assert entity boundary | **SAFE UNKNOWN** — no fabricated canonical |

Machines may **propose** entities and aliases in future implementation; **canonical** identity requires **human attestation** ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)).

### 2.5 Prefer explicit uncertainty over false certainty

**Decision (Phase 3):** Identity **may exist in non-canonical form** (proposed, uncertain) without a locked canonical answer. **Canonical active** identity requires attested certainty that **one** entity record is correct for the business subject.

---

## 3. What ATLAS considers identity

### 3.1 Canonical identity (normative)

**Identity** in ATLAS is the combination of:

| Component | Description |
|-----------|-------------|
| **Entity type** | One of six MVP types ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md)) |
| **Stable identifier** | Opaque, permanent, non-reused id per [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) |
| **Identity lifecycle state** | proposed · active · deprecated · merged · split_source · archived · disputed |
| **Attestation record** | Who attested, when, evidence tier (governance doc) |

For **Relationship** entities, identity additionally includes the **relationship_id** and **canonical slot** semantics from Phase 2 ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) §7) — not redefined here.

### 3.2 Same entity (sameness rules)

**Two references denote the same entity** when and only when:

| Rule | Detail |
|------|--------|
| **EIR-01** | They share the **same canonical stable identifier** for the same entity type |
| **EIR-02** | No second canonical active record exists for the same business subject |
| **EIR-03** | Aliases and display names are **equivalent references** to that id, not separate identities ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |
| **EIR-04** | After merge, all former ids **redirect** to survivor id; former ids are not active canonical |
| **EIR-05** | Consumer foreign keys (CRM account id) are **corroboration**, not sameness proof alone |

**Sameness is not inferred from:**

- Similar spelling (MetaCode vs Метакод)
- Shared domain or website
- Shared person name
- Same Business Scope label (future)
- Same project narrative

### 3.3 Identity-bearing vs identity-adjacent

| Identity-bearing (Phase 3) | Identity-adjacent (not primary key) |
|----------------------------|-------------------------------------|
| `ORG-*`, `PER-*`, `PRJ-*`, `WEB-*`, `DOM-*`, `REL-*` | Email, phone (disputed uniqueness → SAFE UNKNOWN) |
| Canonical name + alias set | Logo, brand colors |
| Merge/split lineage | CRM lead score |
| Deprecation / tombstone | Tax id as ERP system of record |
| Historical id redirect | MARS `project_id` program row |

---

## 4. What ATLAS does not consider identity

| Not identity | Belongs to | Rationale |
|--------------|------------|-----------|
| **Business Scope** (`andrey`, `sergey`, `roman`) | Future classification metadata | Scope classifies **existing** entities; must never mint or merge entities ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §7.1) |
| **Relationship type** (OWNER, CLIENT_OF) | Phase 2 relationship record | Type describes **link**, not entity id |
| **Role in sentence** (“Andrey is owner”) | Relationship assertion | Role without `relationship_id` is narrative |
| **Operational login** | WPilot / MARS security | Person ≠ WordPress user |
| **DNS record set** | Hosting ops | Domain **identity** ≠ live DNS state |
| **Deployment environment** | Consumer-local / CI | Rejected as entity Phase 1 |
| **Task, deal, campaign, invoice** | Excluded entities | Workflow objects |
| **Cluster / portfolio / BU** | Deferred / rejected | Not MVP entity |
| **Invented placeholder** (`org-unknown-1`) | Forbidden | CR-10 / SAFE UNKNOWN |

---

## 5. Canonical identity principles

| # | Principle | Normative rule |
|---|-----------|----------------|
| **IDP-01** | **One business subject → one canonical active id** | Duplicate active canonical forbidden |
| **IDP-02** | **Ids are opaque** | No embedded legal name, tax id, or URL in id string |
| **IDP-03** | **Ids are permanent** | Retired ids never reassigned to a different subject |
| **IDP-04** | **Names drift; ids do not** | Rename updates alias/canonical name, not id |
| **IDP-05** | **Uncertainty is explicit** | uncertain / SAFE UNKNOWN beats silent duplicate |
| **IDP-06** | **History is preserved** | Merge, split, rename leave audit trail |
| **IDP-07** | **Identity ≠ relationship** | New org is not created to “fix” a missing link (RR-07) |
| **IDP-08** | **Identity ≠ scope** | Scope tags never determine which org exists |
| **IDP-09** | **Evidence before canonical** | See governance doc tiers |
| **IDP-10** | **Consumer keys are secondary** | CRM id maps to ATLAS id; does not replace it |

---

## 6. Entity identity rules (by type)

Rules apply at **entity** level; relationship ids follow Phase 2 RI-* rules.

### 6.1 Organization

| Rule | Detail |
|------|--------|
| **EIR-O01** | One canonical org per **attested business unit** (legal or operational) |
| **EIR-O02** | DBA / trade names → **aliases**, not sibling orgs |
| **EIR-O03** | “Polygon” and “ООО Полигон” → aliases on **one** org when attested same unit |
| **EIR-O04** | “Web Studio Polygon” as **separate commercial brand** → human decision: alias vs second org |
| **EIR-O05** | Merger of companies → merge governance; successor retains survivor id |
| **EIR-O06** | CRM “Account” ≠ automatic org; import proposes mapping |

### 6.2 Person

| Rule | Detail |
|------|--------|
| **EIR-P01** | One canonical person per **natural person** |
| **EIR-P02** | Homonym names (two “Иван Иванов”) → separate ids unless attested same person |
| **EIR-P03** | Nickname / patronymic variants → aliases |
| **EIR-P04** | Person id stable across org changes; relationships carry org participation |
| **EIR-P05** | MARS operator login ≠ Person unless explicitly attested same human |

### 6.3 Project

| Rule | Detail |
|------|--------|
| **EIR-PR01** | One canonical project per **named initiative identity** |
| **EIR-PR02** | Renamed initiative → alias/former name; same id unless attested **new** initiative |
| **EIR-PR03** | MARS program pack `project_id` ≠ ATLAS Project entity |

### 6.4 Website

| Rule | Detail |
|------|--------|
| **EIR-W01** | One canonical website per **business web property identity** |
| **EIR-W02** | Rebrand same property → alias; same id |
| **EIR-W03** | New property on new domain → new website id (relationship links domains) |
| **EIR-W04** | Staging URL ≠ production website entity (environment not entity) |

### 6.5 Domain

| Rule | Detail |
|------|--------|
| **EIR-D01** | One canonical domain id per **hostname identity** (apex or FQDN policy attested) |
| **EIR-D02** | `www.` prefix policy is attested alias or separate domain — not assumed |
| **EIR-D03** | Domain transfer between orgs → relationship change, not domain id reuse to new org |
| **EIR-D04** | Parked domain without site → domain entity may exist; website optional |

### 6.6 Relationship

| Rule | Detail |
|------|--------|
| **EIR-R01** | Relationship identity = `REL-*` + slot semantics (Phase 2) |
| **EIR-R02** | Endpoint entity ids must be canonical or explicitly proposed — not UNKNOWN endpoints on canonical edge |
| **EIR-R03** | Entity merge triggers relationship endpoint review — not automatic rewrite without governance |

---

## 7. Identity lifecycle

### 7.1 States (entity-level)

| State | Meaning | Consumer may treat as canonical? |
|-------|---------|----------------------------------|
| **proposed** | Intake candidate; duplicate check pending | **No** |
| **active** | Human-attested canonical entity | **Yes** |
| **deprecated** | Retired; successor or merge target documented | **No** (use redirect) |
| **merged_into** | Id absorbed; points to survivor | **No** (follow redirect) |
| **split_from** | Id was source of split; children documented | **No** |
| **disputed** | Competing claims (same name, unclear unit) | **No** |
| **archived** | Historical read-only | **No** |

**Slot for uncertainty:** When entity existence is unclear, registry holds **SAFE UNKNOWN** at subject level — not a permanent `active` placeholder.

### 7.2 Lifecycle transitions (summary)

```text
intake → proposed → (attest) → active
                 → (reject) → archived / no record

active → (rename) → active  [alias history updated]
active → (deprecate) → deprecated → archived
active → (merge) → merged_into [survivor stays active]
active → (split) → deprecated + new active children

any → (dispute raised) → disputed → (resolve) → active | SAFE UNKNOWN
```

Full merge/split/duplicate policy: [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md).

### 7.3 Historical identity

| Concept | Rule |
|---------|------|
| **Former name** | Preserved as alias with `former` role ([ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)) |
| **Former id** | After merge, `merged_into` redirect; id never reused |
| **Former relationships** | Phase 2 lifecycle — deprecated / FORMER_* types |
| **Audit** | Attestation notes + evidence refs; not full document storage |

Consumers referencing a **merged** id must resolve to **survivor** via documented redirect — never silently remap to arbitrary org.

---

## 8. Uniqueness principles

### 8.1 Uniqueness of canonical active entity

| Dimension | Uniqueness rule |
|-----------|-----------------|
| **Identifier** | Globally unique per type prefix within ATLAS registry scope |
| **Business subject** | At most one **active** canonical record per attested subject per type |
| **Alias** | Many aliases → one entity; alias alone does not prove uniqueness |
| **Display** | Display name uniqueness **not required** — collisions expected |

### 8.2 Uniqueness conflicts (classes)

| Class | Example | Default posture |
|-------|---------|-----------------|
| **U1 — Name collision** | Two “Polygon” orgs | Disambiguate via evidence; merge or separate ids |
| **U2 — Transliteration** | MetaCode / Метакод | Alias on one org if same unit |
| **U3 — Abbreviation overlap** | WSP vs unrelated WSP brand | Context + evidence; may be alias or different org |
| **U4 — Homonym person** | Two Andrey | Separate PER ids unless attested same |
| **U5 — Domain similarity** | `polygon.ru` vs `polygon.com` | Separate DOM ids unless attested same asset |
| **U6 — Import duplicate** | Two CRM accounts → one org | Steward merge proposal |

### 8.3 Uniqueness vs relationships

Uniqueness is **entity-level**. Multiple relationships (Andrey → Polygon, Andrey → MetaCode) do **not** violate uniqueness — they express participation ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) §2.2).

---

## 9. Human attestation requirements

| Action | Minimum attestation |
|--------|---------------------|
| Promote **proposed → active** | Steward or program owner; evidence tier per governance |
| Add **canonical alias** | Steward; E0 allowed for operator-known names |
| Declare **same entity** (merge) | Program owner; E1+ typically |
| Declare **different entity** (reject merge) | Steward; document collision rationale |
| Declare **SAFE UNKNOWN** | Steward or owner; no consumer self-serve canonical |
| **Split** entity | Program owner; E2 when legal split |

Aligned with Phase 2 evidence tiers ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §3) — identity governance extends in sibling doc.

---

## 10. Required architectural analysis

### 10.1 What constitutes identity?

**Decision:** Identity = **entity type** + **opaque stable id** + **lifecycle state** + **human attestation** + **governed alias/canonical name set**. It is **not** any single name, foreign key, or relationship edge.

### 10.2 Can identity exist without certainty?

**Decision: YES — with tiered states.**

Canonical **active** identity requires attested certainty. **proposed**, **uncertain**, and **SAFE UNKNOWN** express partial knowledge without inventing duplicate canonicals. Relationship and entity intake may proceed in proposed form; consumers must not treat proposed as canonical ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §7).

### 10.3 How should aliases work?

**Decision:** Aliases are **many-to-one** linguistic references to a single id; governed types (canonical, display, former, alias). Detail: [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md). Aliases **never** mint a second canonical id.

### 10.4 How should duplicate entities be handled?

**Decision:** Detect → block dual canonical → investigate → **merge** (same subject) or **maintain separate** (different subject) or **SAFE UNKNOWN**. Detail: [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) §3.

### 10.5 Can entities be merged?

**Decision: YES — with survivor id, redirect, non-reuse of retired id, relationship review.**

Merge is **governance event**, not delete. Forbidden: merge to eliminate inconvenient history or to absorb CRM duplicates without evidence.

### 10.6 Can entities be split?

**Decision: YES — rare, owner-approved, with new ids for children and deprecated source.**

Split applies when one canonical record **incorrectly combined** distinct subjects. Default correction is **alias fix**, not split.

### 10.7 How should historical identities be preserved?

**Decision:** Retired ids remain in registry with `merged_into` / `deprecated` / alias `former`; relationships use Phase 2 lifecycle; consumers use redirect table conceptually — implementation deferred.

### 10.8 How should future Business Scope classification interact with identity?

**Decision:** Business Scope **must never determine identity.**

| Allowed (future) | Forbidden |
|------------------|-----------|
| Tag **existing** `ORG-*` / `PER-*` / `PRJ-*` for reporting | Create org because scope `andrey` needs one |
| Filter graph views by scope | Merge Polygon + MetaCode because same scope |
| Scope on Person for narrative grouping | Scope as primary key in consumer contract |

Scope classification package is **separate** from Identity Foundation ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) §7.1, [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) §10.5).

---

## 11. Known identity risks (program exemplars)

| Risk pattern | Example strings | Mitigation |
|--------------|-----------------|------------|
| **Multi-name same unit** | Polygon · ООО Полигон · WSP | Aliases on one `ORG-*` |
| **Transliteration** | i-SEO · ISEO · Ай-СЕО | Alias set + attested canonical name |
| **Similar name different unit** | MetaCode vs unrelated “Metacode” vendor | Evidence before merge; separate ids if different |
| **Abbreviation ambiguity** | WSP | Context in intake; do not auto-merge |
| **Uncertain sameness** | Two CRM accounts | proposed + investigation |
| **Historical brand** | Former trade name | `former` alias; same id |

---

## 12. Prohibitions

| # | Prohibition |
|---|-------------|
| **IDM-X01** | Using display name as durable foreign key |
| **IDM-X02** | Reusing retired id for new subject |
| **IDM-X03** | Silent duplicate canonical orgs for pipeline green |
| **IDM-X04** | Business Scope as entity or id minting reason |
| **IDM-X05** | Auto-merge from string similarity alone |
| **IDM-X06** | Deleting merged ids without redirect |
| **IDM-X07** | Identity inference from website content alone |

---

## 13. Phase 3 completion checklist

- [ ] Identity philosophy and sameness rules defined
- [ ] Identifier strategy delegated to [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md)
- [ ] Alias governance delegated to [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md)
- [ ] Duplicate/merge/split delegated to [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)
- [ ] Business Scope interaction: classification only, never identity
- [ ] No implementation, API, or storage claims

---

## 14. Related documents

| Document | Role |
|----------|------|
| [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) | Prefix strategy, stability, retirement |
| [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) | Names, aliases, SAFE UNKNOWN naming |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) | Merge, split, duplicate, evidence |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | A4 naming collision → identity first |

**Next package (recommended):** Registry Architecture Foundation — storage and intake **after** identity semantics are fixed.
