# ATLAS Entity Taxonomy v1

**Status:** **documented** — Phase 1 canonical MVP entity set.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md)  
**Is not:** database schema, API types, UI forms, relationship type enumeration (deferred).

**Phase 1 canonical set (normative):**

```text
Organization · Person · Project · Website · Domain · Relationship
```

**Explicitly excluded from Phase 1 entity set:** Environment, Business Scope, Cluster, Portfolio, Business Unit, Division, Asset (standalone), Campaign, Task, Deal, Account (financial).

---

## 0. Taxonomy principles

| Principle | Application |
|-----------|-------------|
| **Minimal sufficient set** | Six entities cover identity + grouping + web presence + linking |
| **Entity ≠ workflow object** | No tasks, deals, or tickets as entities |
| **Entity ≠ metric** | No rankings, spend, or traffic as core fields |
| **Names are not ids** | Display names change; stable ids are mandatory in implementation |
| **Relationship is first-class** | Links are not hidden foreign keys only on Website |

---

## 1. Organization

### Purpose

Represent a **durable business unit** that can own, operate, or sponsor projects, websites, and domains — whether incorporated, sole proprietorship, or informally named operating group **when humans attest it as a registry organization**.

### Rationale

Organizations anchor **legal and operational identity** in the graph. Consumers need a stable answer to “**which business** is this site or project under?” without importing CRM account objects or ERP company codes.

### Examples (illustrative)

| Example | Why canonical |
|---------|----------------|
| Polygon (company) | Distinct org with its own sites and people |
| MetaCode | Separate org; same person may link to both Polygon and MetaCode |
| i-SEO (agency) | Org employing/contracting people; client orgs are separate entities |
| Client brand “Триумф” as commercial subject | Org node for Factory/ORCA references |

### Non-examples

| Non-example | Belongs to |
|-------------|------------|
| CRM “Account” with pipeline stage | CRM / sales tooling |
| General ledger company code with fiscal year | ERP / accounting |
| Google Ads customer id | ORCA / ads platform |
| MARS `project_id` row (`orca`, `mig`) | `registry/project-registry.md` |
| Business Scope label `andrey` | Future classification metadata — **not** Organization |
| Department “SEO отдел” without attested org status | Future structure or Relationship — not auto-org |

### Future considerations

- Jurisdiction / legal form fields (optional, attested).
- Parent org **via Relationship**, not nested ERP trees in Phase 1.
- DBA / trade names as aliases, not duplicate orgs.
- Merger: deprecation + successor link (Relationship), not id reuse.

---

## 2. Person

### Purpose

Represent a **natural person** who participates in the business graph — independent of any single organization or role.

### Rationale

People are **not sub-records of Organization**. Multi-hat participation (owner here, contractor there) requires Person at the top level with **multiple** relationships to organizations and projects.

### Examples (illustrative)

| Example | Why canonical |
|---------|----------------|
| Andrey (individual) | One Person linked to Polygon, MetaCode, i-SEO with different roles (future types) |
| Sergey, Roman | Persons within respective business scope narratives |
| External contractor | Person even if not employee of consumer org |

### Non-examples

| Non example | Belongs to |
|-------------|------------|
| User account in WordPress | WPilot operational identity |
| n8n service account | Automation platform |
| “Team” alias without person | Use Organization or future group policy — not Person |
| Bot / agent persona | MARS agent catalog — not business Person |
| CRM contact with lead score | CRM |

### Future considerations

- Preferred name vs legal name.
- Contact channels as **non-canonical** or attested optional attributes (email uniqueness disputes → SAFE UNKNOWN).
- Person ≠ MARS operator login (separate security domain).

---

## 3. Project

### Purpose

Represent a **named structural container** for related work — grouping people, organizations, websites, and domains around an initiative **without** owning task execution or delivery state.

### Rationale (**Phase 1 decision: keep in MVP**)

| Factor | Conclusion |
|--------|------------|
| Consumer language | MIG sessions, ORCA pilots, Factory packs already use “project” |
| Overload risk if removed | Would force Website or Organization to mean “initiative,” blurring legal entity vs campaign |
| PM distinction | Project in ATLAS has **no** tasks, sprints, or % complete — boundary in [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) |
| Graph need | Links “грузотакси Краснодар pilot” to org Триумф and specific sites/domains |

**Normative:** Project answers **“under which initiative identity do we cluster these entities?”** not **“what is due this week?”**

### Examples (illustrative)

| Example | Why canonical |
|---------|----------------|
| Triumph gruzotaxi Krasnodar pilot | Structural MIG/ORCA/Factory cluster |
| Website Factory production pack for a client site | Pack references project container |
| Internal tooling initiative “HomeGateway v4” | Cross-org if needed; still structural |

### Non-examples

| Non-example | Belongs to |
|-------------|------------|
| Jira project with backlog | Task / PM system |
| CRM opportunity | Sales pipeline |
| MARS program pack only | `project-registry.md` — meta, not customer Project |
| Single webpage URL | Website entity |
| “Campaign Q2 2026” | Marketing execution — not ATLAS Project |

### Future considerations

- Project lifecycle (proposed → active → closed) as **status metadata**, not workflow engine.
- Optional project **type** label (client delivery, internal, research) — enum in expansion review.
- 1:N Project ↔ Organization (joint ventures) via Relationship.

---

## 4. Website

### Purpose

Represent a **registered web property** as a business identity object — the conceptual site product consumers reference (brand site, landing, storefront), not the deployment artifact alone.

### Rationale

Website Factory, WPilot, OCPilot, and ORCA all need a **stable website identity** distinct from:

- a **domain** (hostname),
- a **deployed build** (ops),
- a **URL path** (page-level, usually out of scope).

### Examples (illustrative)

| Example | Why canonical |
|---------|----------------|
| polygon.ru corporate site | Primary brand property |
| Client landing for Триумф | Factory/ORCA handoff reference |
| OpenCart storefront instance (conceptual) | Website linked to org; CMS state in OCPilot |

### Non-examples

| Non-example | Belongs to |
|-------------|------------|
| Single landing A/B variant URL only | Consumer experiment tracking |
| PageSpeed score | Analytics |
| WordPress theme version | WPilot ops |
| SERP snapshot URL | MIG evidence |
| Figma file | Design tool |

### Future considerations

- Website ↔ Domain primary/alias mapping via Relationship.
- Website **kind** (corporate, landing, shop) — classification field, not new entity.
- Locale variants as related websites or metadata — expansion review if needed.

---

## 5. Domain

### Purpose

Represent a **hostname / domain name identity anchor** in the business graph — what the business recognizes as its domain asset for routing and reference.

### Rationale

Domains are **not interchangeable with Website**: one site may use multiple domains; one domain may redirect or park without a full site. ATLAS holds **identity**, not DNS operations.

### Examples (illustrative)

| Example | Why canonical |
|---------|----------------|
| `polygon.ru` | Primary domain linked to Website |
| `www.polygon.ru` | May be separate Domain node or alias policy (implementation choice later) |
| Parked domain awaiting launch | Domain exists before Website goes live |

### Non-examples

| Non-example | Belongs to |
|-------------|------------|
| DNS A/CNAME record management | Hosting / DNS ops |
| SSL certificate expiry workflow | Ops / security tooling |
| Domain registrar billing | Finance — not ATLAS |
| Subpath `example.com/blog` | URL routing — consumer scope |

### Future considerations

- Internationalized domain names (IDN).
- Expiry date as **optional attested metadata** — not payment workflow.
- Transfer between orgs → Relationship + human attestation, not automatic.

---

## 6. Relationship

### Purpose

Represent a **structural link** between two (or more, if later chartered) canonical entities — the explicit edge of the business reality graph.

### Rationale

Foreign-key-style coupling only inside Website or Person records **hides** participation semantics and blocks multi-hat models. **Relationship** as first-class entity keeps edges visible, reviewable, and deprecatable.

### Examples (illustrative — **types not normative in Phase 1**)

| Plain-language link | Endpoint entities |
|-------------------|-----------------|
| Andrey ↔ Polygon | Person ↔ Organization |
| Andrey ↔ MetaCode | Person ↔ Organization |
| Andrey ↔ i-SEO | Person ↔ Organization |
| Project ↔ Organization | Project ↔ Organization |
| Website ↔ Organization | Website ↔ Organization |
| Domain ↔ Website | Domain ↔ Website |
| Person ↔ Project | Person ↔ Project |

**Phase 1 constraint:** record **that** a link exists and **endpoints**; **relationship type** vocabulary (OWNER, PARTNER, EMPLOYEE, CONTRACTOR, MANAGER, REPRESENTATIVE) is **documented as future** in [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) §8.2 — **not implemented** in taxonomy v1.

### Non-examples

| Non-example | Belongs to |
|-------------|------------|
| “Member of ad group X” | ORCA / ads |
| “Assigned to task 1042” | PM / task system |
| “Invoice billed to” | Accounting |
| “Similar web cluster SERP” | MIG analytics |
| Asset ownership ledger entry | Phase 2+ relationship evolution |

### Future considerations

- Typed edges with effective dates and attestation.
- Cardinality rules per type (one primary org per Website, etc.).
- **Asset ownership** likely expressed as Relationship, not Asset entity ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)).
- Prohibition of contradictory canonical types for same endpoints once taxonomy exists.

---

## 7. Entity relationship sketch (Phase 1)

```text
                    ┌──────────────┐
                    │ Organization │
                    └──────┬───────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
    ┌─────────┐      ┌──────────┐      ┌─────────┐
    │ Person  │◄────►│ Project  │◄────►│ Website │
    └─────────┘      └──────────┘      └────┬────┘
         │                 │                 │
         └────────┬────────┴────────┬────────┘
                  │   Relationship   │
                  └────────┬─────────┘
                           ▼
                      ┌─────────┐
                      │ Domain  │
                      └─────────┘
```

All connections are **mediated by Relationship** (conceptual); implementation may optimize storage but must not lose edge auditability.

---

## 8. Rejected Phase 1 entity: Environment

**Decision:** **Not admitted** in Phase 1.

| Reason | Detail |
|--------|--------|
| Ops collision | Staging/production/dev is deployment topology |
| Boundary drift | Would pull hosting state into registry |
| Alternative | Consumers keep environment locally; optional future **metadata** on Website or consumer contract |

See [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) — Environment listed as future candidate **NOT APPROVED FOR PHASE 1**.

---

## 9. Deferred entities (not in taxonomy v1)

|Mention only in expansion doc| Status |
|-----------------------------|--------|
| Business Scope | Future classification metadata |
| Cluster, Portfolio, Business Unit, Division | **NOT APPROVED FOR PHASE 1** |
| Asset (standalone) | Phase 2+ via relationships |
| Campaign, Task, Deal | Permanent exclusions |

---

*ATLAS Entity Taxonomy v1 — six MVP entities. Relationship types deferred.*
