# ATLAS Wave 4 Shpigovsky Website Population v1

**Status:** **documented** — Wave 4 Shpigovsky canonical Website population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Domain population, Wave 4B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1D Shpigovsky Organization ORG-0008: **active** — AT-W1D-SHPIG-01
- Wave 3 Shpigovsky Project PRJ-0012: **attested** — AT-W3-SHPIG-01
- Wave 3B Shpigovsky Project ↔ Organization: **COMPLETE** — AT-W3B-SHPIG-01
- Population verdict: **READY FOR WAVE 4 SHPIGOVSKY WEBSITE POPULATION**

**Binding operator scope (this tranche):**

- Mint **1** Website record only — **WEB-SHPIG-01** `shpigovsky.ru` (**active**).
- **One hostname → one Website** (EIR-W01).
- **No** Domain (`DOM-*`), relationship edges, or Person→Website edges.
- Org/project fields — **display candidates**; structural edges deferred to Wave 4B-SHPIG.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Website** для Wave 4 tranche **Shpigovsky** (ORG-0008): состав, `WEB-SHPIG-01` mint, lifecycle, evidence, candidate relationships для Wave 4B-SHPIG.

---

## 2. Evidence pre-check (mandatory)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-SHPIG-OP-01** | Operator intake statements (2026-06-10) | **E0** | Polygon delivery; ongoing property |
| **EV-SHPIG-WEB-01** | Live capture `https://shpigovsky.ru/` | **E2** | Public property corroboration |
| **EV-SHPIG-WEB-02** | Live capture `https://shpigovsky.ru/policy` | **E2** | Org corroboration ООО «Сознание» |
| **AT-W1D-SHPIG-01** | Wave 1D Organization attestation | attestation | ORG-0008 **active** |
| **AT-W3-SHPIG-01** | Wave 3 Project attestation | attestation | PRJ-0012 **active** |
| **AT-W3B-SHPIG-01** | Wave 3B relationship attestation | attestation | REL-SHPIG-PJ-01..02 **active** |

**Evidence tier (population):** **E0/E2** — E0 operator path + E2 public property corroboration.

---

## 3. Population roster (canonical)

**Identifier scheme:** `WEB-SHPIG-01` — Shpigovsky tranche namespace.

### 3.1 Summary table

| website_id | canonical_name | website_kind | lifecycle_state *(target)* | roster_priority | primary_org_candidate | primary_project_candidate | evidence_tier | attestation_readiness |
|------------|----------------|--------------|------------------------------|-----------------|----------------------|---------------------------|---------------|----------------------|
| WEB-SHPIG-01 | shpigovsky.ru | **corporate_website** | **active** | **P0** | ORG-0008 ООО «Сознание» | PRJ-0012 Сайт shpigovsky.ru | **E0/E2** | **ready** |

**Lifecycle at population:** WEB-SHPIG-01 minted as **proposed** pending steward attestation act AT-W4-SHPIG-01.

---

## 4. Per-website analysis — WEB-SHPIG-01

| Field | Value |
|-------|-------|
| **website_id** | WEB-SHPIG-01 |
| **intake_label** | SHPIGOVSKY-INTAKE-WEB-01 |
| **canonical_name** | shpigovsky.ru |
| **website_kind** | **corporate_website** — client corporate web property |
| **url** | `https://shpigovsky.ru/` |
| **environment** | **production** — public live property |
| **roster_priority** | **P0** |
| **primary_org_candidate** | ORG-0008 ООО «Сознание» |
| **primary_project_candidate** | PRJ-0012 Сайт shpigovsky.ru |
| **display aliases** | «Шпиговский Дом» *(brand — not separate org)* |
| **platform context** | WordPress; possible ACF; custom programming |
| **evidence basis** | E0 EV-SHPIG-OP-01; E2 EV-SHPIG-WEB-01..02; PRJ-0012 **active**; REL-SHPIG-PJ-01..02 **active** |
| **attestation readiness** | **Ready** at **E0/E2** |

---

## 5. Candidate Wave 4B relationships

| Draft rel_id | source_id | target_id | relationship_type | prerequisite |
|--------------|-----------|-----------|-------------------|--------------|
| REL-SHPIG-WB-01 | WEB-SHPIG-01 shpigovsky.ru | PRJ-0012 Сайт shpigovsky.ru | **BELONGS_TO** | WEB-SHPIG-01 **active** |
| REL-SHPIG-WB-02 | ORG-0008 ООО «Сознание» | WEB-SHPIG-01 shpigovsky.ru | **OWNS** | WEB-SHPIG-01 **active** |

---

## 6. Explicit exclusions

| Item | Treatment |
|------|-----------|
| DOM-* `shpigovsky.ru` | **Deferred** — Wave 5 |
| PRIMARY_DOMAIN | **Deferred** — Wave 5B |
| Person ↔ Website | **Excluded** |
| CLIENT_OF | **Deferred** — Wave 6 |
| Foundation documents | **Not modified** |

---

*ATLAS Wave 4 Shpigovsky Website Population v1 — documentation only.*
