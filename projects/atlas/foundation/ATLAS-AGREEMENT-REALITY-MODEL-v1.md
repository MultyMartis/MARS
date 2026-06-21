# ATLAS Agreement Reality Model v1

**Status:** **documented** — Wave AGL-01 expansion entity definition (business reality registration only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** AGL-01 — Agreement Layer Foundation  
**Parent:** [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) · [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) · [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md)  
**Is not:** legal document storage, contract management software, accounting system, CRM deal object, runtime schema, API type definition.

---

## 1. Purpose

Define **Agreement** as a minimal business-reality anchor that answers operational questions without storing contract text:

| Question | Agreement field / link |
|----------|------------------------|
| Which agreement covers this client? | `client_org` + `agreement_id` |
| Which agreement covers this project? | `related_projects` |
| Agreement status? | `status` |
| Agreement period? | `start_date`, `end_date` |
| Agreement scope? | `scope_summary`, `agreement_type` |

**Normative ruling:**

> Agreement registers **attested commercial work reality** — not legal clauses, signatures, or payment terms.

**OPS alignment:** Resolves OPS consumer class **C-07 Agreement** per [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md) — structural registration layer; OPS WF-02 may **read** agreement refs; OPS does **not** store canonical agreement roster.

---

## 2. Expansion admission (AGL-01)

| Criterion | Assessment |
|-----------|------------|
| A-01 Identity necessity | OPS WF-01 / WF-02 require agreement scope binding beyond COMMISSIONED_BY alone |
| A-02 Durability | Commercial arrangements persist months+ |
| A-03 Boundary cleanliness | No contract text, signatures, or accounting — within ATLAS boundaries |
| A-04 Human attestability | Operators can confirm scope and parties from delivery evidence |
| A-05 Consumer plurality | OPS (primary), ORCA / Factory (secondary scope context) |
| A-06 Non-redundancy | Not expressible as Relationship alone — period, type, and scope bundle required |
| A-07 Anti-PM/finance | No tasks, amounts, or pipeline |

**Entity class position:** Agreement is **expansion entity #7** — documented in Wave AGL-01; **not** retroactively added to Phase 1 MVP six without expansion review record. Population follows evidence-first discipline in companion population documents.

---

## 3. Agreement entity definition

### 3.1 Purpose

**Business relationship anchor** — links client organization, vendor organization, operational scope, and attested project(s) for a commercial work arrangement.

### 3.2 Minimum fields

| Field | Required | Description |
|-------|----------|-------------|
| **agreement_id** | **Yes** | Stable identifier (`AGR-*` namespace) |
| **status** | **Yes** | Lifecycle posture — see §4 |
| **client_org** | **Yes** | Organization id — commercial purchaser / sponsor |
| **vendor_org** | **Yes** | Organization id — service provider |
| **agreement_type** | **Yes** | Controlled vocabulary — see §5 |
| **start_date** | **Yes*** | ISO date or **SAFE UNKNOWN** |
| **end_date** | **Yes*** | ISO date or **SAFE UNKNOWN** |
| **scope_summary** | **Yes** | Human-readable scope — no legal clause text |
| **related_projects** | **Yes** | One or more attested `PRJ-*` ids |
| **evidence_level** | **Yes** | E0–E3 tier per [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) |
| **notes** | Optional | Attestation rationale, boundary notes, pointer refs |

\*Field is **required on record**; value may be **SAFE UNKNOWN** when evidence insufficient — not omitted.

### 3.3 Explicit exclusions (normative)

| Excluded | Belongs to |
|----------|------------|
| Contract full text | Legal archive / document storage |
| PDF / scan payload | Evidence vault pointer only |
| Signature workflow state | Legal / WF-02 operational tracking |
| Payment terms, amounts, invoices | Accounting / ERP |
| Renewal automation rules | CRM / billing |
| SLA metrics | OPS service catalog |
| Legal clause enumeration | Legal counsel systems |

---

## 4. Agreement status vocabulary

Minimal statuses only — no lifecycle engine complexity.

| Status | Meaning | Typical signal |
|--------|---------|----------------|
| **ACTIVE** | Commercial work arrangement currently in effect or ongoing delivery | Active `PRJ-*` + attested COMMISSIONED_BY / EXECUTES |
| **EXPIRED** | Arrangement concluded; no ongoing delivery under this anchor | Deprecated `PRJ-*` or operator-confirmed closure |
| **PLANNED** | Arrangement approved for future start — not yet in delivery | Intake candidate with parties + scope; no active project |
| **UNKNOWN** | Parties or scope partially known — insufficient to classify ACTIVE / EXPIRED / PLANNED | Hold row in population plan only — **do not register** |

**Rules:**

- **AGR-ST-01:** Do not infer EXPIRED from missing end_date alone — use project lifecycle + operator attestation.
- **AGR-ST-02:** PLANNED requires attested parties + scope; dates may be UNKNOWN.
- **AGR-ST-03:** UNKNOWN is a **population-plan posture**, not a register row status — insufficient evidence → no entity.

---

## 5. Agreement type vocabulary

Minimal controlled vocabulary — expand only via expansion review.

| Type | Meaning | Example scope |
|------|---------|---------------|
| **SEO_RETAINER** | Ongoing SEO services | Monthly SEO on attested website property |
| **PPC_RETAINER** | Paid advertising management | Yandex Direct / context campaigns |
| **DEVELOPMENT** | Web development, build, or platform delivery | Site build, catalog platform, landing |
| **SUPPORT** | Maintenance or support arrangement | Post-launch support retainer |
| **MIXED** | Multiple service lines under one attested anchor | Umbrella when evidence supports single arrangement |
| **OTHER** | Attested commercial scope not matching above | Use with explicit scope_summary |
| **UNKNOWN** | **Not valid on register row** — use SAFE UNKNOWN in population plan |

**Rules:**

- **AGR-TY-01:** Prefer specific type when project scope unambiguous (e.g. PRJ named «SEO …» → SEO_RETAINER).
- **AGR-TY-02:** Do not split type by inferred billing model.
- **AGR-TY-03:** MIXED only when operator attests single arrangement covering multiple service lines.

---

## 6. Relationships to MVP entities

Agreement **references** but does **not replace** MVP graph objects:

```text
Organization (client_org) ──CLIENT_OF──► Organization (vendor_org)     [optional corroboration]
Project (related_projects) ──COMMISSIONED_BY──► Organization (client_org)
Organization (vendor_org) ──EXECUTES──► Project (related_projects)
Agreement (AGR-*) ──covers──► Project(s) + parties                     [this layer]
```

| MVP entity | Role relative to Agreement |
|------------|----------------------------|
| Organization | Party endpoints (`client_org`, `vendor_org`) |
| Project | Scope container (`related_projects`) |
| Relationship | Corroboration — CLIENT_OF, COMMISSIONED_BY, EXECUTES |
| Person | **Not** agreement party — contact context only |
| Website / Domain | **Not** on agreement row — via project linkage |

---

## 7. Evidence discipline

| Tier | Agreement use |
|------|---------------|
| **E0** | Operator attestation of ongoing commercial delivery + structural graph |
| **E1** | Informal commercial document pointer (CC, client spreadsheet ref) — **pointer only** |
| **E2** | Formal contract extract **reference** — dates/type may be attested; text **not stored** |
| **E3** | System corroboration + human review |

**Minimum for register admission** (see [ATLAS-AGREEMENT-ATTESTATION-v1.md](../population/ATLAS-AGREEMENT-ATTESTATION-v1.md)):

1. `client_org` — attested Organization **active**
2. `vendor_org` — attested Organization **active**
3. `scope_summary` — non-empty, evidence-backed
4. `status` — ACTIVE, EXPIRED, or PLANNED (not UNKNOWN)
5. `related_projects` — at least one attested Project id (except PLANNED pre-project intake)
6. Structural corroboration — paired COMMISSIONED_BY + EXECUTES for project-scoped agreements
7. `evidence_level` assigned — no fabricated tier

**Absence of any required element → SAFE UNKNOWN → no register row.**

---

## 8. Identifier model

| Namespace | Pattern | Example |
|-----------|---------|---------|
| Agreement | `AGR-NNNN` | AGR-0001 |

**AGR-ID-01:** Mint ids at population act — not in intake analysis.  
**AGR-ID-02:** One agreement row may cover multiple projects only when attested as single arrangement.  
**AGR-ID-03:** Default Wave AGL-01 granularity: **one agreement per attested project delivery stream** unless operator attests umbrella arrangement.

---

## 9. Anti-patterns

| Anti-pattern | Ruling |
|--------------|--------|
| Store contract PDF in ATLAS repo | **Forbidden** |
| Create agreement from CLIENT_OF alone | **Insufficient** — need scope + project link |
| Create agreement from project name alone | **Insufficient** — need parties + status + evidence |
| Infer agreement dates from project start | **Forbidden** without E1+ date evidence |
| Duplicate CRM «Deal» lifecycle | **Forbidden** |
| Agreement per website without project | **Defer** — bind via Project where possible |

---

## 10. Related documents

| Document | Role |
|----------|------|
| [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](../population/ATLAS-AGREEMENT-POPULATION-PLAN-v1.md) | Client evaluation and readiness |
| [ATLAS-AGREEMENT-REGISTER-v1.md](../population/ATLAS-AGREEMENT-REGISTER-v1.md) | Attested agreement roster |
| [ATLAS-AGREEMENT-ATTESTATION-v1.md](../population/ATLAS-AGREEMENT-ATTESTATION-v1.md) | Attestation methodology |
| [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset attestation act |
| [REPORT-atlas-agreement-layer-foundation-v1.md](../reports/REPORT-atlas-agreement-layer-foundation-v1.md) | Wave AGL-01 pass record |

---

*ATLAS Agreement Reality Model v1 — Wave AGL-01. Business reality registration only. Documentation only.*
