# OPS — ATLAS Alignment v1

**Status:** **documented** — Phase 8 ecosystem ontology alignment (normative for ATLAS interpretation).  
**Programs:** ATLAS (Business Reality Registry) · OPS (Business Operations Domain)  
**Date:** 2026-06-05  
**Parent:** [ATLAS-OPERATIONAL-MODEL-v1.md](ATLAS-OPERATIONAL-MODEL-v1.md) · [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) · [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md)  
**Related OPS doc:** [../../ops/foundation/OPS-ATLAS-RELATIONSHIP-v1.md](../../ops/foundation/OPS-ATLAS-RELATIONSHIP-v1.md)  
**Resolves:** Audit finding R-ATLAS-P1-001, GAP-09, CON-03 — OPS entity class names vs ATLAS MVP taxonomy.

**Is not:** OPS document amendment (optional follow-up), sync protocol, API mapping, field-level ETL.

---

## 1. Purpose

Analyze and resolve **OPS operational concepts** versus **ATLAS MVP canonical concepts** — prevent ontology drift where OPS vocabulary is mistaken for ATLAS entity classes.

**Normative ruling:**

> **Clients, Contacts, Services, Agreements, Requisites** in OPS are **logical operational views** for reporting and workflow context — **not** ATLAS entity classes.  
> ATLAS MVP remains: **Organization · Person · Project · Website · Domain · Relationship**.

---

## 2. Architectural decision summary

**Decision (Architectural Analysis #8):** OPS and ATLAS **coexist** by strict separation:

| Layer | Owns |
|-------|------|
| **ATLAS** | Structural business reality — who/what exists, structural links |
| **OPS** | Operational work — reports, approvals, cycle status, drafts |

OPS **reads** ATLAS for identity context; OPS **does not** define ATLAS taxonomy.

When [OPS-ATLAS-RELATIONSHIP-v1.md](../../ops/foundation/OPS-ATLAS-RELATIONSHIP-v1.md) lists C-01–C-08 as “ATLAS consumer classes,” interpret per **this document** — logical views mapped to MVP entities and relationships.

---

## 3. ATLAS MVP reference (canonical)

From [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md):

```text
Organization · Person · Project · Website · Domain · Relationship
```

Explicitly **not** MVP entities: Client, Contact, Service, Agreement, Requisite, Account, Deal, Task.

---

## 4. OPS concept mapping

### 4.1 Summary table

| OPS concept (OPS C-xx) | Maps to ATLAS? | ATLAS expression | Mapping type |
|------------------------|----------------|------------------|--------------|
| **Client** (C-01) | **Partial — logical view** | **Organization** + **CLIENT_OF** relationship | M-DISP / M-SUGG |
| **Contact** (C-02) | **Partial — logical view** | **Person** + **REPRESENTATIVE** / **EMPLOYEE** / role relationships | M-DISP / M-SUGG |
| **Organization** (C-03) | **Yes — direct** | **Organization** entity | Direct |
| **Project** (C-04) | **Yes — direct** | **Project** entity | Direct |
| **Website** (C-05) | **Yes — direct** | **Website** entity | Direct |
| **Service** (C-06) | **No — not MVP entity** | Consumer-local or future attested metadata / expansion | M-NONE / expansion only |
| **Agreement** (C-07) | **No — not MVP entity** | Consumer-local + pointers; structural sponsor via **COMMISSIONED_BY** | M-NONE |
| **Requisites** (C-08) | **No — not MVP entity** | Attested **optional fields** on Organization (expansion) or consumer-local until expansion | M-NONE / field expansion |
| **Relationships** (C-09) | **Yes — direct** | **Relationship** entity instances | Direct |

### 4.2 Client (OPS C-01)

| Aspect | Ruling |
|--------|--------|
| **OPS meaning** | Report recipient, contractual counterparty in operational narrative |
| **ATLAS meaning** | An **Organization** structurally linked via **CLIENT_OF** (agency → client org) or **COMMISSIONED_BY** (project sponsor) |
| **Maps?** | **Yes — as Organization + Relationship**, not as entity class “Client” |
| **Does not map** | CRM “Customer” stage, pipeline status, revenue tier |
| **Boundary** | E-26 — no CRM Account clone |

**Example:** “Client Триумф” in OPS report → ATLAS **Organization** (Триумф) + **CLIENT_OF** from agency org — attested.

**Anti-pattern:** Creating ATLAS entity class **Client** — **rejected** (audit declined seventh entity).

### 4.3 Contact (OPS C-02)

| Aspect | Ruling |
|--------|--------|
| **OPS meaning** | Billing contact, technical contact named in report |
| **ATLAS meaning** | **Person** with structural relationship to Organization (**REPRESENTATIVE**, **EMPLOYEE**, **CONTRACTOR** per taxonomy) |
| **Maps?** | **Yes — as Person + Relationship** |
| **Does not map** | Contact channel alone (email without person attest); CRM Contact object with lifecycle |
| **Boundary** | Primary Contact may be **M-SUGG** only ([ATLAS-CONSUMER-MAPPING-RULES-v1.md](ATLAS-CONSUMER-MAPPING-RULES-v1.md)) |

**Anti-pattern:** ATLAS entity class **Contact** separate from Person — **rejected**.

### 4.4 Service (OPS C-06)

| Aspect | Ruling |
|--------|--------|
| **OPS meaning** | Service line described in reporting period (SEO, support, dev) |
| **ATLAS meaning** | **Not** an MVP entity — operational catalog |
| **Maps?** | **No direct entity map** |
| **Allowed** | OPS-local service taxonomy; optional future **attested metadata** on Project via expansion review |
| **Remains outside ATLAS** | Service pricing, SLA, delivery status, hours |

**Operational rule OPS-ALN-01:** OPS reports cite **Project** + OPS-local service labels — not ATLAS “Service” entity.

### 4.5 Agreement (OPS C-07)

| Aspect | Ruling |
|--------|--------|
| **OPS meaning** | Active agreement scope reference for report narrative |
| **ATLAS meaning** | **Not** MVP entity — legal/contractual artifact |
| **Maps?** | **No entity map** |
| **Structural link** | **COMMISSIONED_BY** (Project → Organization) may reflect sponsor — not contract text |
| **Remains outside ATLAS** | Contract text, legal status, signature workflow, renewal dates as canonical fields |

**Boundary:** E-11–E-13 — finance/legal not ATLAS MVP.

### 4.6 Requisites (OPS C-08)

| Aspect | Ruling |
|--------|--------|
| **OPS meaning** | Invoicing/payment details in client report |
| **ATLAS meaning** | **Not** MVP entity — potential **attested optional fields** on Organization (future field expansion) |
| **Maps?** | **No entity map today** |
| **Until expansion** | OPS uses ATLAS-attested org identity + **SAFE UNKNOWN** for missing bank fields, or consumer-local copy with AD-06 compliance |
| **Remains outside ATLAS (default)** | Bank details as standalone registry objects |

**OPS AD-06 reaffirmed:** Requisites in report **must** match ATLAS-attested values or explicit **SAFE UNKNOWN**.

### 4.7 Direct maps (C-03, C-04, C-05, C-09)

| OPS | ATLAS | Notes |
|-----|-------|-------|
| Organization | Organization | 1:1 entity |
| Project | Project | Structural container — not PM tasks |
| Website | Website | Identity object — not CMS state |
| Relationships | Relationship | Typed edges per Phase 2 taxonomy |

---

## 5. What maps — decision matrix

| Question | Answer |
|----------|--------|
| Does OPS “Client” create an ATLAS entity? | **No** — use Organization + CLIENT_OF |
| Does OPS “Contact” create an ATLAS entity? | **No** — use Person + role relationship |
| Can OPS reference ATLAS ids for org/project/website? | **Yes** — required when ids exist (AD-01) |
| Can OPS store canonical client list? | **No** — D-01 forbidden |
| Can OPS edit canonical fields locally? | **No** — AD-02 |
| Does ATLAS store agreement PDF? | **No** — pointer/evidence ref at most |
| Does ATLAS store service catalog? | **No** — OPS-local |

---

## 6. What does not map — remains outside ATLAS

| OPS / operational domain | Stays in |
|--------------------------|----------|
| Report drafts and delivery records | OPS |
| Workflow stage (reviewer, approval timestamp) | OPS |
| Service line catalog and pricing | OPS / finance consumers |
| Agreement text and legal interpretation | Legal / Secretary (future) |
| Bank requisites (until field expansion) | OPS with UNKNOWN discipline |
| Monthly reporting cycle status | OPS workflow |
| Operator notes (non-canonical) | OPS |

---

## 7. Read vs write alignment

Reaffirms [OPS-ATLAS-RELATIONSHIP-v1.md](../../ops/foundation/OPS-ATLAS-RELATIONSHIP-v1.md) §5:

| Direction | Rule |
|-----------|------|
| ATLAS → OPS | Read structural context for reports |
| OPS → ATLAS | **Propose only** via intake — no canonical write |
| OPS working copy → ATLAS | **Forbidden** as promotion path (AD-03) |
| Disagreement | ATLAS wins for identity/structure (AD-04) |

---

## 8. Operational governance implications

| Scenario | ATLAS operational response |
|----------|---------------------------|
| OPS requests “Client entity” for reporting | **Reject** at intake — offer Org + CLIENT_OF proposal |
| OPS imports contact spreadsheet as entities | **Proposed** only — Person + relationship review |
| OPS needs requisites on org | **Defer** until field expansion OR **UNKNOWN** |
| OPS treats C-06 Service as ATLAS class | **Boundary review** — consumer mapping correction |
| New entity discovered during reporting | **Intake to ATLAS** (AD-05) — not OPS-only creation |

Stewards use [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) §10.4.

---

## 9. Recommended OPS document amendment (non-blocking)

Optional follow-up for OPS maintainers — **not** part of ATLAS foundation amendment:

| OPS section | Suggested change |
|-------------|------------------|
| §2 C-01–C-08 table | Add column “ATLAS MVP map” referencing this document |
| C-01 Client | Label “logical view → Organization + CLIENT_OF” |
| C-02 Contact | Label “logical view → Person + relationship” |
| C-06–C-08 | Label “not ATLAS entity — see OPS-ATLAS-ALIGNMENT-v1” |

ATLAS-side alignment is **complete** with this document; OPS doc amendment reduces reader confusion.

---

## 10. Consumer certification note

OPS certification against [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md) **requires**:

- Published mapping document using §4 tables
- No shadow master lists (D-01)
- AD-01–AD-06 compliance in workflows

---

## 11. Related documents

| Document | Link |
|----------|------|
| ATLAS boundaries E-26 | [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) |
| Consumer semantic contract | [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md) |
| Mapping rules | [ATLAS-CONSUMER-MAPPING-RULES-v1.md](ATLAS-CONSUMER-MAPPING-RULES-v1.md) |
| Audit risk R-ATLAS-P1-001 | [../audit/ATLAS-FOUNDATION-RISK-REGISTER-v1.md](../audit/ATLAS-FOUNDATION-RISK-REGISTER-v1.md) |
| Foundation index | [ATLAS-FOUNDATION-INDEX-v1.md](ATLAS-FOUNDATION-INDEX-v1.md) |

---

*OPS — ATLAS Alignment v1 — Phase 8 Foundation. Documentation only.*
