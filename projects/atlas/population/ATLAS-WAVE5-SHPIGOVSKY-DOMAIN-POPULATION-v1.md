# ATLAS Wave 5 Shpigovsky Domain Population v1

**Status:** **documented** — Wave 5 Shpigovsky canonical Domain population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE4B-SHPIGOVSKY-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SHPIGOVSKY-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, DNS operations, registrar integration, relationship attestation, Wave 5B-SHPIG execution.

**Prerequisites (operator-confirmed):**

- Wave 1D Shpigovsky Organization ORG-0008: **active** — AT-W1D-SHPIG-01
- Wave 4 Shpigovsky Website attestation: **COMPLETE** — AT-W4-SHPIG-01 (WEB-SHPIG-01 **active**)
- Wave 4B Shpigovsky Website Relationships: **COMPLETE** — AT-W4B-SHPIG-01..02
- Population verdict: **READY FOR WAVE 5 SHPIGOVSKY DOMAIN POPULATION**

**Binding operator discipline (Wave 5 Shpigovsky):**

- **Approved roster only:** **DOM-SHPIG-01** (`shpigovsky.ru`) — singleton apex hostname anchor.
- **Single-domain model** — one Domain entity for `shpigovsky.ru`.
- **Domain population now. Domain relationships later** (Wave 5B-SHPIG).
- **No** PRIMARY_DOMAIN, OWNS Organization→Domain, or other domain-family edges in Wave 5 Shpigovsky.
- **Registrar / registrant ownership** remains **SAFE UNKNOWN** — not inferred from Website OWNS, Project context, or policy page.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Domain** для Wave 5 tranche **Shpigovsky** (ORG-0008): hostname anchor, lifecycle, evidence, candidate relationships для Wave 5B-SHPIG.

**Modeling rule (enforced):**

> Domain = **hostname identity anchor**. Website = **web property identity**.  
> Co-terminous hostname on WEB-SHPIG-01 and DOM-SHPIG-01 are **parallel identities**, linked via **future** PRIMARY_DOMAIN — not merged records.

---

## 2. Domain roster (canonical)

### 2.1 Summary table

| domain_id | canonical_name | lifecycle_state *(target)* | primary_org_candidate | primary_website_candidate | evidence_tier | registrar status | attestation readiness |
|-----------|----------------|------------------------------|----------------------|---------------------------|---------------|------------------|----------------------|
| **DOM-SHPIG-01** | shpigovsky.ru | **active** | ORG-0008 ООО «Сознание» *(display only)* | WEB-SHPIG-01 shpigovsky.ru | **E0/E2** | **SAFE UNKNOWN** | **ready** |

**Lifecycle at population:** DOM-SHPIG-01 minted as **proposed** pending steward attestation act AT-W5-SHPIG-01.

---

## 3. Per-domain analysis — DOM-SHPIG-01

| Field | Value |
|-------|-------|
| **domain_id** | DOM-SHPIG-01 |
| **canonical_name** | shpigovsky.ru |
| **hostname_class** | apex |
| **lifecycle_state (target)** | **active** |
| **primary_org_candidate** | ORG-0008 ООО «Сознание» *(display only — not domain registrant attestation)* |
| **primary_website_candidate** | WEB-SHPIG-01 shpigovsky.ru |
| **evidence_tier** | **E0/E2** |
| **evidence_sources** | EV-SHPIG-OP-01; EV-SHPIG-WEB-01; WEB-SHPIG-01 **active** (AT-W4-SHPIG-01) |
| **ownership confidence** | **context only — not attested** |
| **registrar status** | **SAFE UNKNOWN** |
| **attestation readiness** | **Ready** |

---

## 4. Candidate Wave 5B relationships

| Draft rel_id | source_id | target_id | relationship_type | prerequisite |
|--------------|-----------|-----------|-------------------|--------------|
| REL-SHPIG-DM-01 | DOM-SHPIG-01 shpigovsky.ru | WEB-SHPIG-01 shpigovsky.ru | **PRIMARY_DOMAIN** | DOM-SHPIG-01 **active** |

**Explicitly excluded from Wave 5B (operator binding):**

| Item | Treatment |
|------|-----------|
| ORG-0008 → DOM-SHPIG-01 **OWNS** | **DO NOT CREATE** — registrar evidence absent; SAFE UNKNOWN |

---

## 5. Explicit exclusions (Wave 5)

| Item | Treatment |
|------|-----------|
| ORG-0008 → DOM-SHPIG-01 OWNS | **Excluded** — registrar evidence absent |
| PRIMARY_DOMAIN | **Deferred** — Wave 5B |
| Person ↔ Domain | **Excluded** |
| DNS record modeling | **Excluded** |

---

*ATLAS Wave 5 Shpigovsky Domain Population v1 — documentation only.*
