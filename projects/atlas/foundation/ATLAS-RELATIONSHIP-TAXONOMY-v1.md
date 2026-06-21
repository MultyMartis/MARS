# ATLAS Relationship Taxonomy v1

**Status:** **documented** — Phase 2 normative relationship type vocabulary.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md)  
**Is not:** database enum DDL, API schema, UI picklists, HR job codes, CRM stage mapping.

**MVP entities (unchanged):** Organization · Person · Project · Website · Domain · Relationship

**Rule:** Do **not** introduce new MVP entities. All types below are **Relationship.type** values connecting existing entities.

---

## 0. Taxonomy conventions

### 0.1 Naming

| Convention | Rule |
|------------|------|
| **Case** | `SCREAMING_SNAKE` type codes |
| **Direction** | `SUBJECT ──TYPE──► OBJECT` |
| **Verb form** | Active voice where possible (`CLIENT_OF`, not `IS_CLIENT`) |
| **Former types** | Prefix `FORMER_` for ended structural roles (lifecycle doc) |

### 0.2 Family

A **family** is the allowed **(subject entity type, object entity type)** pair. Types outside a family’s pair are **forbidden** (RR-08).

### 0.3 Type admission

New types require [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) review. This document is **v1** baseline.

### 0.4 Boundary check (all families)

Types must **not** encode: payroll, performance review, deal stage, invoice, task assignment, campaign membership, SERP cluster, or DNS operational state.

---

## 1. Family: PERSON ↔ ORGANIZATION

**Pair:** `Person` → `Organization` (unless noted; inverse not stored separately).

**Purpose:** Participation, ownership, employment-like structure, and representation — **without** becoming an HR system.

| Type code | Meaning | Canonical slot notes |
|-----------|---------|----------------------|
| **OWNER** | Person has ownership stake or ultimate control attested for the org | Multiple OWNER allowed if attested |
| **PARTNER** | Person is business partner (equity or partnership), not employee | Distinct from OWNER when roles differ |
| **EMPLOYEE** | Person is employed by org (structural, not payroll) | Does not imply compensation data |
| **CONTRACTOR** | Person provides services under contract to org | Not timesheet / deliverable tracking |
| **MANAGER** | Person holds management responsibility for org or division | Not headcount reporting |
| **REPRESENTATIVE** | Person authorized to act or speak for org externally | Multiple representatives allowed |
| **FORMER_OWNER** | Ownership ended; historical | Use after OWNER ends or via lifecycle |
| **FORMER_EMPLOYEE** | Employment link ended; historical | Paired with EMPLOYEE supersession |
| **FORMER_CONTRACTOR** | Contract link ended; historical | Paired with CONTRACTOR supersession |

**Exemplar requirements (from program request):**

```text
Andrey ──OWNER──► Polygon
Andrey ──OWNER──► MetaCode
Andrey ──MANAGER──► i-SEO
Person ──REPRESENTS──► Organization   → use REPRESENTATIVE
```

**Normative mapping:** Program text “REPRESENTS” → type **REPRESENTATIVE** (direction Person → Organization).

### 1.1 Non-types (reject as canonical)

| Rejected label | Reason |
|----------------|--------|
| REPORTS_TO | Org chart / HR reporting |
| PERFORMANCE_MANAGER | HR review |
| LEAD_SCORE_CONTACT | CRM |

---

## 2. Family: ORGANIZATION ↔ ORGANIZATION

**Pair:** `Organization` → `Organization`

**Purpose:** Commercial structure between business units — **not** a sales pipeline.

| Type code | Meaning | Canonical slot notes |
|-----------|---------|----------------------|
| **CLIENT_OF** | Subject org is client of object org (service relationship) | Many clients per vendor allowed |
| **PARTNER_OF** | Peer partnership between orgs | Store once; document which org is subject |
| **VENDOR_OF** | Subject provides vendor services to object | Inverse commercial direction of CLIENT_OF |
| **SUPPLIER_OF** | Subject supplies goods/materials to object | Structural supply chain link only |
| **FORMER_CLIENT_OF** | Client relationship ended | After CLIENT_OF ends |
| **FORMER_PARTNER_OF** | Partnership ended | Historical |

**Exemplar:**

```text
Organization(A) ──CLIENT_OF──► Organization(B)
```

**Symmetry note:** `A CLIENT_OF B` implies commercial direction. Do **not** also store `B CLIENT_OF A` unless dual role is attested (rare). **VENDOR_OF** may be used when vendor direction is the clearer assertion.

### 2.1 Parent / subsidiary

**Decision (Phase 2):** No **PARENT_OF** in v1 baseline — defer to expansion review to avoid ERP group trees.

**Alternative:** Optional future type or **PARTNER_OF** + notes. **SAFE UNKNOWN** if group structure unclear.

---

## 3. Family: ORGANIZATION ↔ PROJECT

**Pair:** bidirectional types — direction matters.

### 3.1 Organization → Project

| Type code | Meaning |
|-----------|---------|
| **OWNS** | Organization owns the project initiative (structural) |
| **EXECUTES** | Organization performs delivery work (structural identity, not PM) |
| **SPONSORS** | Organization funds or charters without day-to-day execution |

### 3.2 Project → Organization

| Type code | Meaning |
|-----------|---------|
| **COMMISSIONED_BY** | Project commissioned by client or sponsor org |

**Exemplar:**

```text
Project(Pilot) ──COMMISSIONED_BY──► Organization(ClientX)
Organization(Agency) ──EXECUTES──► Project(Pilot)
```

**Program mapping:** “COMMISSIONED” → **COMMISSIONED_BY** (Project → Organization).

### 3.3 Non-types

| Rejected | Reason |
|----------|--------|
| SPRINT_OF | PM |
| BILLABLE_TO | Finance |

---

## 4. Family: PERSON ↔ PROJECT

**Pair:** `Person` → `Project`

**Purpose:** Structural participation in an initiative — not task assignment.

| Type code | Meaning |
|-----------|---------|
| **LEADS** | Person structurally leads project |
| **CONTRIBUTES_TO** | Person participates without sole lead |
| **FORMER_LEADS** | Historical lead |

**Note:** Task assignees remain in PM tools. Link Person/Project here only for **business graph** visibility.

---

## 5. Family: ORGANIZATION ↔ WEBSITE

**Pair:** `Organization` → `Website`

| Type code | Meaning |
|-----------|---------|
| **OWNS** | Organization owns web property identity |
| **OPERATES** | Organization operates site without ownership claim |
| **FORMER_OWNS** | Ownership ended |

**Distinction:** **OWNS** (org ↔ website) is org-level property. **BELONGS_TO** (website ↔ project) is initiative grouping.

---

## 6. Family: PROJECT ↔ WEBSITE

**Pair:** `Website` → `Project` (primary); optional `Project` → `Website` only if expansion approves reverse types.

| Type code | Meaning | Direction |
|-----------|---------|-----------|
| **BELONGS_TO** | Website grouped under project | Website → Project |

**Exemplar:**

```text
Website(Site) ──BELONGS_TO──► Project(Pilot)
```

**Program mapping:** “Website BELONGS_TO Project” — normative.

### 6.1 Optional reverse (deferred)

| Type | Status |
|------|--------|
| **HAS_WEBSITE** (Project → Website) | **NOT in v1** — use BELONGS_TO with query inversion |

---

## 7. Family: WEBSITE ↔ DOMAIN

**Pair:** `Domain` → `Website` (domain points at site identity)

| Type code | Meaning | Cardinality |
|-----------|---------|-------------|
| **PRIMARY_DOMAIN** | Primary hostname for site | ≤1 canonical active per Website |
| **SECONDARY_DOMAIN** | Alias / additional hostname | Many allowed |
| **REDIRECTS_TO** | Domain redirects to site (or via site) | Many; document redirect target in notes if needed |
| **POINTS_TO** | General pointer when PRIMARY/SECONDARY insufficient | Use sparingly; prefer specific types |

**Exemplar:**

```text
Domain(example.ru) ──PRIMARY_DOMAIN──► Website(Site)
Domain(www.example.ru) ──SECONDARY_DOMAIN──► Website(Site)
Domain(old.example.ru) ──REDIRECTS_TO──► Website(Site)
```

**Program mapping:** “Domain POINTS_TO Website” → prefer **PRIMARY_DOMAIN** / **SECONDARY_DOMAIN**; **POINTS_TO** retained as general fallback.

### 7.1 Domain without website

Domain may exist **without** Website ([ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) §5). **No** Relationship to Website until attested.

---

## 8. Family: ORGANIZATION ↔ DOMAIN

**Pair:** `Organization` → `Domain`

**Purpose:** Asset ownership integration ([ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) §10.4).

| Type code | Meaning |
|-----------|---------|
| **OWNS** | Organization owns domain identity |
| **CUSTODIAN** | Organization holds domain in custody (registrar account) without ownership claim |
| **FORMER_OWNS** | Historical ownership |

**Person ↔ Domain** mirror (expansion candidate): **OWNER**, **CUSTODIAN** on Person → Domain — **approved in v1** for personal domain ownership.

---

## 9. Family: PERSON ↔ DOMAIN

**Pair:** `Person` → `Domain`

| Type code | Meaning |
|-----------|---------|
| **OWNS** | Person owns domain (individual registrant) |
| **CUSTODIAN** | Person holds technical custody |
| **FORMER_OWNS** | Historical |

---

## 10. Family: PERSON ↔ WEBSITE

**Pair:** `Person` → `Website`

| Type code | Meaning |
|-----------|---------|
| **OWNS** | Person owns site identity (sole proprietor) |
| **OPERATES** | Person operates site |
| **FORMER_OWNS** | Historical |

---

## 11. Cross-family reference matrix

Allowed **primary** families in v1:

| Subject type | → | Object type | Families |
|--------------|---|-------------|----------|
| Person | → | Organization | §1 |
| Person | → | Project | §4 |
| Person | → | Domain | §9 |
| Person | → | Website | §10 |
| Organization | → | Organization | §2 |
| Organization | → | Project | §3.1 |
| Organization | → | Website | §5 |
| Organization | → | Domain | §8 |
| Project | → | Organization | §3.2 |
| Website | → | Project | §6 |
| Domain | → | Website | §7 |

**Not in v1:** Entity-to-self; Relationship-to-Relationship; more than two endpoints (hyperedges deferred).

---

## 12. Type summary table (quick index)

| Family | Types |
|--------|-------|
| Person → Organization | OWNER, PARTNER, EMPLOYEE, CONTRACTOR, MANAGER, REPRESENTATIVE, FORMER_* |
| Organization → Organization | CLIENT_OF, PARTNER_OF, VENDOR_OF, SUPPLIER_OF, FORMER_* |
| Organization → Project | OWNS, EXECUTES, SPONSORS |
| Project → Organization | COMMISSIONED_BY |
| Person → Project | LEADS, CONTRIBUTES_TO, FORMER_LEADS |
| Organization → Website | OWNS, OPERATES, FORMER_OWNS |
| Website → Project | BELONGS_TO |
| Domain → Website | PRIMARY_DOMAIN, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO |
| Organization → Domain | OWNS, CUSTODIAN, FORMER_OWNS |
| Person → Domain | OWNS, CUSTODIAN, FORMER_OWNS |
| Person → Website | OWNS, OPERATES, FORMER_OWNS |

---

## 13. Illustrative ecosystem subgraph

```text
                    ┌──────────────┐
                    │ Organization │
                    └──────┬───────┘
           CLIENT_OF │      │ OWNS
                    ▼      ▼
              ┌──────────┐ ┌─────────┐
              │ Org (B)  │ │ Project │
              └──────────┘ └────┬────┘
                                │ COMMISSIONED_BY (reverse arrow to Org)
     OWNER                      │
 Person ───────────────► Org    │
     │                          │
     REPRESENTATIVE             │
     └──────────► Org           │
                                ▼
                          ┌─────────┐     PRIMARY_DOMAIN   ┌────────┐
                          │ Website │◄─────────────────────│ Domain │
                          └─────────┘                      └────────┘
                                │
                                │ BELONGS_TO
                                ▼
                          ┌─────────┐
                          │ Project │
                          └─────────┘
```

---

## 14. Rejected relationship types (v1)

| Type | Reason |
|------|--------|
| DEAL_WITH | CRM |
| INVOICES | Accounting |
| ASSIGNED_TASK | PM |
| MEMBER_OF_CAMPAIGN | Marketing execution |
| SERP_COMPETITOR_OF | MIG analytics |
| HOSTED_ON | Environment / ops |
| PARENT_ORG | Deferred ERP-tree risk |
| SCOPE_OVER | Business Scope is not entity — no SCOPE_* edge in v1 |

---

## 15. Versioning

| Version | Content |
|---------|---------|
| **v1** | Families §1–§10; FORMER_* pairs; no PARENT_ORG; no hyperedges |
| **v2+** | Expansion process; may add types, not entities, without expansion approval |

---

*ATLAS Relationship Taxonomy v1 — normative types only. No implementation schema.*
