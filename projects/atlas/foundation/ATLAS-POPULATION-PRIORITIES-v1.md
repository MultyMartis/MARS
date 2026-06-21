# ATLAS Population Priorities v1

**Status:** **documented** — Phase 7 canonical population waves (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) · [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md)  
**Is not:** sprint plan, ticket backlog, data migration ordering, consumer-specific ETL.

**Phase 1–6 constraint:** No changes to approved Phase 1–6 documents unless contradictions discovered. None at Phase 7 authoring.

---

## 1. Purpose

Establish **recommended population waves** across the six MVP entity classes:

```text
Organization · Person · Project · Website · Domain · Relationship
```

**Optimization targets:**

- **Maximum reality stability** — anchors before dependents.
- **Minimum ambiguity** — edges after endpoints; UNKNOWN explicit.

---

## 2. Evaluation criteria

| Criterion | Weight | Meaning |
|-----------|--------|---------|
| **Anchor strength** | High | Later records depend on this class for identity answers |
| **Duplicate risk** | High | Wrong early record poisons many dependents |
| **Consumer handoff need** | Medium | Factory/ORCA/MIG reference urgency |
| **Evidence availability** | Medium | Operator-known vs external/client |
| **Relationship dependency** | High | Edges require stable endpoint ids |
| **Reversibility cost** | Medium | Merge/split pain if wrong |

---

## 3. Per-class analysis

### 3.1 Organization

| Factor | Assessment |
|--------|------------|
| Anchor strength | **Highest** — “which business” for sites, projects, CLIENT_OF |
| Duplicate risk | **High** — homonym brands, CRM double accounts |
| Evidence | Operator orgs: E0–E1; client orgs: E1–E2 |
| Relationships | Target of PERSON↔ORG and ORG↔ORG edges |

**Conclusion:** Populate **first**.

### 3.2 Person

| Factor | Assessment |
|--------|------------|
| Anchor strength | **High** — multi-hat participation needs Person node |
| Duplicate risk | **Medium** — homonyms, CRM contacts |
| Evidence | E0–E1 for known operators; E1 for contractors |
| Relationships | Requires org endpoints for most participation types |

**Conclusion:** Populate **second**, after core Organizations.

### 3.3 Project

| Factor | Assessment |
|--------|------------|
| Anchor strength | **Medium-high** — clusters pilots/packs without owning tasks |
| Duplicate risk | **Medium** — name collision with MARS `project_id` |
| Evidence | E0–E1 structural attest (“this pilot exists”) |
| Relationships | BELONGS_TO / grouping edges need org or website later |

**Conclusion:** Populate **before** Website and Domain — initiative container before web identity.

### 3.4 Website

| Factor | Assessment |
|--------|------------|
| Anchor strength | **Medium** — consumer handoff object |
| Duplicate risk | **Medium** — URL variants, staging vs prod |
| Evidence | E0–E1 internal; E1+ client properties |
| Relationships | Often needs Organization and/or Project endpoints |

**Conclusion:** Populate **after** Project; org link may be **UNKNOWN** at propose stage.

### 3.5 Domain

| Factor | Assessment |
|--------|------------|
| Anchor strength | **Medium** — hostname identity distinct from site |
| Duplicate risk | **Lower** than org — registrar ambiguity still exists |
| Evidence | E1 registrar/DNS intent for PRIMARY_DOMAIN claims |
| Relationships | Links to Website; may exist **before** Website live ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §5) |

**Conclusion:** Populate **after** Website for typical case; **parked** domains may enter in same wave with **proposed** status only.

### 3.6 Relationship

| Factor | Assessment |
|--------|------------|
| Anchor strength | **Low alone** — edges are not anchors |
| Duplicate risk | **High** if early — wrong OWNER poisons graph |
| Evidence | Type-specific E1–E2 ([ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md)) |
| Dependencies | **Requires endpoints** ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) RR-01, EIR-R02) |

**Conclusion:** Populate **last** for bulk canonical graph; **exception slice** after Person (see Wave 2B).

---

## 4. Canonical population waves

```text
Wave 1  ──► Organization (anchor set)
Wave 2  ──► Person
Wave 2B ──► Relationship slice: Person ↔ Organization (participation)
Wave 3  ──► Project
Wave 4  ──► Website
Wave 5  ──► Domain
Wave 6  ──► Relationship (remaining families)
```

### Wave 1 — Organizations

**Scope:** Durable business units the operator attests as registry organizations.

**Illustrative priority tiers (generic):**

| Tier | Examples (illustrative) | Evidence |
|------|-------------------------|----------|
| **W1-A Operator core** | Operator-owned companies (e.g. Polygon, MetaCode, i-SEO) | E0–E1 |
| **W1-B Active client orgs** | Commercial subjects with active delivery | E1 minimum |
| **W1-C Latent / historical** | Former clients, parked brands | E1+; may remain **proposed** |

**Rationale:** Maximizes stability for all downstream classes; answers “which business” first.

**Stop within wave:** Duplicate D1 unresolved; legal merge without E2; boundary smell (CRM Account entity).

---

### Wave 2 — People

**Scope:** Natural persons in the business graph (not WP users, not agents).

**Rationale:** Separates **human identity** from org records; enables multi-hat model before web properties.

**Dependency:** Wave 1 **core operator orgs** at least **proposed** (active preferred for W2B).

**Stop within wave:** Homonym D3 unresolved; Person vs Organization D5.

---

### Wave 2B — Participation relationships (early slice)

**Scope:** Relationship types in family **PERSON ↔ ORGANIZATION** only:

- OWNER, PARTNER, MANAGER, EMPLOYEE, CONTRACTOR, REPRESENTATIVE (and FORMER_* when ending known roles)

**Rationale:** Person + Organization without edges is **incomplete business reality** for consumers ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) exemplar). Waiting until Wave 6 for all edges would leave Wave 1–2 **disconnected**.

**Rules:**

| Rule | Requirement |
|------|-------------|
| **W2B-R01** | Both endpoints **active canonical** (or steward-documented proposed pair pending joint attest) |
| **W2B-R02** | No ORG↔ORG, Website, Domain, Project families in 2B |
| **W2B-R03** | Minimum evidence per type ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md)) |

**This answers “relationships early or late?”:** **Early for participation only; late for full graph.**

---

### Wave 3 — Projects

**Scope:** Named structural containers (pilots, client packs, internal initiatives).

**Rationale:** Projects group work **without** absorbing websites; avoids overloading Organization with “initiative” meaning ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §3).

**Dependency:** Sponsor org usually known — link via Relationship in Wave 6C or **proposed** note if org pending.

**Projects before websites?** **Yes** — normative wave order.

---

### Wave 4 — Websites

**Scope:** Registered web properties (brand site, landing, storefront concept).

**Rationale:** Consumers (Factory, WPilot, ORCA) need `website` identity; depends on org/project context for structural links.

**Can website exist before organization?**

| State | Allowed? |
|-------|----------|
| **proposed** Website, org **SAFE UNKNOWN** | **Yes** — intake captures URL/product identity |
| **active** Website with full structural graph | **Discouraged** without org attest or explicit UNKNOWN policy |
| **active** BELONGS_TO / OWNS to org | **No** until org **active** or dispute resolved |

Aligned with [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) A2.

---

### Wave 5 — Domains

**Scope:** Hostname identity anchors.

**Rationale:** Domains are not interchangeable with Website; PRIMARY_DOMAIN and alias policies need website ids ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md)).

**Ordering vs Website:** Default **after** Website; **parked** domain-only records may be **proposed** in Wave 5 without active site link.

---

### Wave 6 — Remaining relationships (bulk graph)

Sub-waves by taxonomy family:

| Sub-wave | Family | Depends on |
|----------|--------|------------|
| **6A** | ORGANIZATION ↔ ORGANIZATION | Wave 1 org set |
| **6B** | Entity ↔ PROJECT (BELONGS_TO, etc.) | Waves 1–3 |
| **6C** | WEBSITE / DOMAIN families | Waves 4–5 |
| **6D** | Cross-links (PRIMARY_DOMAIN, OWNS, points-to) | 6C + endpoints |

**Can relationship exist before both endpoints canonical?**

| Endpoint state | Relationship state |
|----------------|-------------------|
| Both endpoints **active** | May attest **active** edge |
| One/both **proposed** only | Edge **proposed** only — not active canonical |
| Endpoint **SAFE UNKNOWN** | No **active** edge; **proposed** or no record ([ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) LC-P02) |

**Bulk relationships:** **Wave 6** after entity waves — **maximum stability, minimum ambiguity.**

---

## 5. Wave summary table

| Wave | Entity class | Primary outcome |
|------|--------------|-----------------|
| **1** | Organization | Business anchors |
| **2** | Person | Human anchors |
| **2B** | Relationship (PERSON↔ORG) | Multi-hat structure |
| **3** | Project | Initiative containers |
| **4** | Website | Web property identity |
| **5** | Domain | Hostname identity |
| **6** | Relationship (all other families) | Complete structural graph |

---

## 6. Parallelism rules

| Allowed parallel | Forbidden parallel |
|------------------|-------------------|
| Steward reviews multiple **proposed** in same wave | Active promotion in Wave 6 before Wave 1 anchors |
| W1-B client orgs while W1-A completes | Auto-active import across waves |
| Wave 4 **proposed** websites while Wave 3 active | Bulk OWNER edges before Wave 2B prerequisites |

**POP-PAR-01:** Parallel intake **increases** steward load — stop conditions apply ([ATLAS-POPULATION-GOVERNANCE-v1.md](ATLAS-POPULATION-GOVERNANCE-v1.md)).

---

## 7. First-wave evidence threshold (Wave 1–2)

| Context | Minimum tier at active attest |
|---------|-------------------------------|
| Operator-known org/person | **E0** acceptable with steward note |
| External/client org | **E1** |
| Legal merge / same-subject org | **E2** |
| Import-derived only | **E1 or E3 + human review** — not E0 |

Aligned with [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §4.3 and [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](ATLAS-EVIDENCE-REQUIREMENTS-v1.md).

---

## 8. What must never be bulk-imported automatically

See [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) §10 — summary:

| Prohibited auto action |
|------------------------|
| Set **active** canonical on import |
| Auto-merge duplicate candidates |
| Auto-create Organization from Website hostname |
| Auto-create OWNER / OWNS / CLIENT_OF from CRM alone |
| Mint placeholder org ids |
| Promote MIG SERP rows to canonical org/site |

---

## 9. Consumer wave alignment (conceptual)

| Consumer need | Minimum wave |
|---------------|--------------|
| Reference operator org | Wave 1 |
| Attribute person to org | Wave 2B |
| MIG/Factory pilot cluster | Wave 3 + 4 |
| Domain SSL/DNS handoff (identity only) | Wave 5 |
| Full graph analytics | Wave 6 |

Certification implications: [ATLAS-POPULATION-ROADMAP-v1.md](ATLAS-POPULATION-ROADMAP-v1.md).

---

*ATLAS Population Priorities v1 — Phase 7 Foundation. Documentation only.*
