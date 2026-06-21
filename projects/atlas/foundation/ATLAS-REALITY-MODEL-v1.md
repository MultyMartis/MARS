# ATLAS Reality Model v1

**Status:** **documented** — Phase 1 Reality Foundation (approved revision).  
**Program:** ATLAS — **Business Reality Registry**  
**Classification:** Registry Layer · Cross-Cutting Infrastructure  
**Date:** 2026-06-04  
**Is not:** runtime, automation, orchestration, API, database, storage implementation, registry implementation, folder architecture, CRM, ERP, finance, sales, project management, marketing execution.

**Foundation chain (Phase 1):** **this document** → [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) → [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) → [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)

**Related MARS boundary (ecosystem):**

> **ATLAS maintains who exists, what exists, and how things are related.**  
> **Other systems perform work.**

---

## 1. Mission

**ATLAS** exists to maintain **canonical business reality** across the MARS ecosystem — a single, human-supervised **source of truth for identity and structural business facts**, not for operational execution.

| ATLAS answers | ATLAS does not answer |
|---------------|----------------------|
| Who exists (people, organizations) | What tasks are open |
| What exists (projects, websites, domains) | What was spent or invoiced |
| How entities are related (structural links) | How campaigns perform |
| Stable identifiers for cross-system reference | SEO strategy, content, PPC decisions |

**Mission statement (normative):**

> Preserve **durable, reviewable business identity and structure** so downstream programs (MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway, and future secretarial or document systems) can **reference the same reality** without each system inventing its own parallel org chart, site list, or person registry.

---

## 2. Purpose

### 2.1 Why ATLAS exists

MARS spans multiple **lanes** and **products**. Each consumer needs to know:

- which **organization** owns or operates a site;
- which **person** acts in which capacity;
- which **project** groups work without conflating it with a CRM deal;
- which **website** and **domain** correspond to a deployable or documented surface.

Without a registry layer, identity fragments into spreadsheets, chat memory, per-tool settings, and implicit assumptions. ATLAS is the **documented contract** for what “exists” in business terms before any system executes work.

### 2.2 Documentation-first Phase 1

Phase 1 delivers **models, boundaries, and governance rules only**. No implementation claims are made unless future phases add evidenced code under `projects/atlas/` or elsewhere with explicit charter.

### 2.3 Human supervision

All canonical reality is **human-attested** in Phase 1 design:

- machines may **propose** records later; humans **confirm** canonical status.
- ambiguity is **SAFE UNKNOWN**, never silent invention.

---

## 3. Scope

### 3.1 In scope (conceptual ownership)

| Domain | Phase 1 expression |
|--------|-------------------|
| **Organizations** | Legal or operational business units as registry entities |
| **People** | Natural persons as registry entities |
| **Projects** | Named work containers linking orgs, sites, people (not PM execution) |
| **Websites** | Registered web properties as identity objects |
| **Domains** | DNS / hostname identity anchors |
| **Relationships** | Structural links between the above (taxonomy detail deferred) |

### 3.2 Out of scope (explicit non-ownership)

ATLAS does **not** own: SEO, PPC, analytics, finances, invoices, contracts, tasks, campaigns, content production, operational execution, market research evidence (MIG), semantic/campaign interpretation (ORCA), CMS operations (WPilot/OCPilot), or cockpit UI behavior (HomeGateway).

See [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) for the full exclusion matrix.

### 3.3 Cross-cutting placement

```text
                    ┌─────────────────────────────┐
                    │   ATLAS (Registry Layer)    │
                    │  identity · structure · SoT │
                    └──────────────┬──────────────┘
                                   │ consumes (read)
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
      MIG                      ORCA                 Website Factory
   (acquires market          (interprets           (produces sites;
    groundtruth)              reality)              references sites)
         │                         │                         │
         └─────────────────────────┴─────────────────────────┘
                                   │
                    WPilot · OCPilot · HomeGateway · future secretarial systems
```

Consumers **may read** ATLAS reality; ATLAS **must not absorb** their responsibilities.

---

## 4. Boundaries (summary)

| ATLAS is | ATLAS is not |
|----------|--------------|
| Business Reality Registry | CRM pipeline |
| Identity and structure SoT | ERP / accounting |
| Cross-cutting infrastructure | Autonomous runtime |
| Human-supervised canonical model | Task or campaign manager |

Full boundary rules: [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md).

---

## 5. Reality principles

### 5.1 Identity before execution

No downstream system should need to **guess** whether an organization or website “exists.” Execution systems attach **work artifacts** to ATLAS identities; they do not redefine identity.

### 5.2 Participation ≠ ownership

A **person** may participate in multiple **organizations** with different roles. The model must not collapse “owner of Polygon” and “contractor at i-SEO” into a single implicit ownership relation.

**Phase 1:** document role **implications** only; do **not** implement relationship type taxonomy (OWNER, PARTNER, EMPLOYEE, etc.) — reserved for ATLAS-RELATIONSHIP-FOUNDATION (future package).

### 5.3 Stable identifiers

Canonical entities require **opaque, stable ids** in future implementation. Display names may change; ids must not be recycled without explicit human deprecation.

### 5.4 One canonical fact per claim

For each structural claim (“Person X is associated with Organization Y”), ATLAS holds **at most one canonical row** per defined relationship kind once taxonomy exists. Conflicting drafts remain **non-canonical** until human resolution.

### 5.5 Provenance discipline (future-facing)

When implementation exists, every canonical mutation should record **who attested, when, and source** (manual entry, import, consumer proposal). Phase 1 documents the principle only.

### 5.6 Consumer humility

Consumers **reference** ATLAS; they **do not fork** parallel registries for the same entity class without a documented exception and merge plan.

### 5.7 Anti-drift

Features that resemble CRM deals, ledger accounts, or sprint boards are **boundary violations**, not “convenient extensions.” See anti-drift rules in [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md).

---

## 6. Canonical reality rules

| Rule ID | Rule | Violation signal |
|---------|------|------------------|
| **CR-01** | Only MVP entity types in Phase 1 canonical set | New type without expansion review |
| **CR-02** | Canonical record requires human attestation (design) | Auto-promoted records without review |
| **CR-03** | No financial or pipeline fields on core entities | Invoice stage, deal value on Organization |
| **CR-04** | Project = structural container, not task backlog | Tasks, sprints, assignees as Project fields |
| **CR-05** | Website ≠ deployed runtime state | “Last deploy hash” as canonical Website truth |
| **CR-06** | Domain = identity anchor, not DNS ops console | MX change workflow owned by ATLAS |
| **CR-07** | Relationship records structure only | Campaign membership labeled as Relationship |
| **CR-08** | Deprecation explicit; no silent delete | Removed org still referenced without tombstone |
| **CR-09** | Cross-consumer ids stable | Per-tool duplicate person records |
| **CR-10** | Unknown = SAFE UNKNOWN, not filler | Placeholder org invented to unblock export |

---

## 7. SAFE UNKNOWN rules

Aligned with MARS `.cursorrules` and registry introspection discipline.

| Situation | Required behavior |
|-----------|-------------------|
| Entity id referenced but not in canonical set | State **SAFE UNKNOWN**; do not infer attributes |
| Relationship type not yet in taxonomy | Record **link intent** only if charter allows; else UNKNOWN |
| Consumer cache disagrees with ATLAS | ATLAS canonical wins **after** human reconciliation; until then UNKNOWN |
| Historical fact without attestation | **Non-canonical** or UNKNOWN — not promoted for convenience |
| Missing person/org for a website | Do not auto-create; flag gap for human intake |
| Business Scope classification requested | **Not Phase 1** — mention as future metadata only ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)) |

**Prohibition:** Silent resolution of ambiguity to keep pipelines green (e.g. inventing `org-unknown-1` as permanent canonical).

---

## 8. Business reality philosophy

### 8.1 Reality vs work

| Layer | Question | Owner (examples) |
|-------|----------|------------------|
| **Business reality** | What exists in the business graph? | ATLAS |
| **Market reality** | What does the market show (SERP, competitors)? | MIG |
| **Interpretation** | What should we do with evidence? | ORCA |
| **Production** | What site artifact was built? | Website Factory |
| **Operations** | What is deployed / edited on CMS? | WPilot, OCPilot |
| **Personal cockpit** | How does the operator navigate surfaces? | HomeGateway |

ATLAS is the **slow-changing structural layer** underneath faster-moving work layers.

### 8.2 Multi-hat participation (exemplar)

**Andrey** (illustrative, not canonical data):

| Organization | Participation (future taxonomy) | Not assumed |
|--------------|----------------------------------|-------------|
| Polygon | Owner | Sole identity of Andrey |
| MetaCode | Owner | Ownership of all other orgs |
| i-SEO | Contractor / department lead | Employee-only model |

Phase 1 entities must **allow** multiple links Person ↔ Organization without forcing a single `owner_id` on Person.

### 8.3 Business Scope (future metadata only)

Business activity may later be grouped under **Business Scope** labels (e.g. `andrey`, `sergey`, `roman`) for **classification**, not as canonical entities.

**Business Scope is NOT:** company, CRM pipeline, accounting unit, org division, or Phase 1 entity.

**Phase 1:** may appear in narrative and future-candidate sections only. Do **not** introduce Cluster, Portfolio, Business Unit, or Division as entities ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)).

### 8.4 Projects in the reality graph

**Decision (Phase 1):** **Project remains in MVP.**

**Rationale:** Many consumers already speak in **project** terms (Website Factory packs, ORCA pilots, MIG sessions). Project as a **structural container** (“this body of work groups these sites and people under an org”) is distinct from **project management** (tasks, Gantt, resource loading). Removing Project would force awkward overload of Organization or Website and blur “legal entity” vs “initiative.”

**Constraint:** Project fields describe **identity and grouping**, not execution state.

### 8.5 Environment entity

**Decision (Phase 1):** **Reject Environment as entity.**

**Rationale:** “Environment” (staging/production/dev) is **deployment and runtime topology**, owned by execution and ops consumers. Introducing it in Phase 1 invites ATLAS to absorb hosting state and violates identity-before-execution separation. Environment may reappear as **consumer-local** or **relationship metadata** in a later phase — not as a sibling of Organization.

### 8.6 Asset ownership

**Decision:** **Future Phase 2 consideration** — likely via **relationship taxonomy evolution**, not a standalone Phase 1 entity.

**Rationale:** “Who owns this domain/asset” is a **relationship and attestation** problem, not a separate asset class before relationship types exist. Premature **Asset** entity would duplicate Domain/Website and invite financial encumbrance fields.

---

## 9. Registry naming decision

| Decision | Value |
|----------|-------|
| **Program name** | **ATLAS** |
| **Full name** | **Business Reality Registry** |
| **Not called** | “Asset registry,” “CRM hub,” “Master data ERP,” “MARS database” |

**Rationale:**

- **ATLAS** evokes **map of structural truth** without implying financial ledger or sales pipeline.
- **Business Reality Registry** states scope: **business-identified** entities and links, not infrastructure hosts (contrast EAR/MIG “reality” namespaces — see §10).
- Avoids collision with MARS **project registry** (`registry/project-registry.md`), which tracks **MARS program packs**, not customer organizations.

---

## 10. Terminology — “reality” namespaces

| Namespace | Meaning | Example |
|-----------|---------|---------|
| **ATLAS Business Reality** | Canonical org/person/project/site/domain graph | Organization `org-polygon` |
| **MIG Reality Layers** | Market evidence trust stack (R1–R4) | SERP capture fidelity |
| **MARS project registry** | In-repo program `project_id` rows | `mig`, `orca` |
| **NOVA Decision Reality** | Mobile product decision vocabulary | `DEC_EXISTENCE` |

**Rule:** In ATLAS docs, say **“ATLAS business reality”** or **“canonical entity”** when referring to this model. Do not shorten to “the registry” without disambiguation.

---

## 11. Known consumers (reference)

**Current (may consume ATLAS reality when implemented):** MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway.

**Future:** Secretary systems, document generation, contract generation, reporting, administrative assistants.

Consumers remain responsible for their domains; ATLAS supplies **identifiers and structure** only.

---

## 12. Phase 1 deliverables and non-deliverables

| Delivered in Phase 1 | Explicitly not delivered |
|----------------------|---------------------------|
| Reality model (this doc) | Runtime service |
| Entity taxonomy | API specification |
| Boundaries + expansion rules | Database schema |
| Recorded decisions §8.4–8.9 | Relationship type enum |
| | Storage layout |
| | Automation / orchestration |

---

## 13. Open implications for next package

Relationship **types** (OWNER, PARTNER, EMPLOYEE, CONTRACTOR, MANAGER, REPRESENTATIVE) are **named but not specified** in Phase 1. Canonical **Relationship** entity exists; **semantics** require **ATLAS-RELATIONSHIP-FOUNDATION** if Phase 1 review confirms gaps in consumer handoff (see Phase 1 closeout report).

---

*ATLAS Reality Model v1 — Phase 1 Foundation. Documentation only; no runtime claims.*
