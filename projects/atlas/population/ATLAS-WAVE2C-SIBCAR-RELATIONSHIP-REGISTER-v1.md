# ATLAS Wave 2C SIBCAR Relationship Register v1

**Status:** **attested** — canonical Person → Organization relationship roster after Wave 2C SIBCAR attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Person registry, org↔org registry, Wave 2B core register extension.

---

## 1. Purpose

Канонический **реестр аттестированных Person → Organization relationships** Wave 2C tranche **SIBCAR** (ORG-0006). Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Person → Organization) | **2** |
| Lifecycle **active** | **2** |
| Lifecycle deferred / proposed | **0** |
| Target organization | **ORG-0006 SIBCAR** |
| Relationship families | Person → Organization only |

---

## 2. Attested roster — full table

| relationship_id | source_person | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|---------------|---------------------|-------------------|-------------------|---------------|-----------------|-------|
| REL-SIBCAR-01 | PER-0016 Карандашов Максим Петрович | ORG-0006 SIBCAR | **GENERAL_DIRECTOR** | E1 EV-W1C-CC-01 §21–§24; LE-0005 signatory AT-W1C-01 | **E1** | **active** | Director / signatory / chief accountant; W2C-SIBCAR-TAX-01 |
| REL-SIBCAR-02 | PER-0017 Хаял | ORG-0006 SIBCAR | **REPRESENTATIVE** | E0 EV-W2C-SIBCAR-OP-01; primary operational contact Polygon↔SIBCAR | **E0** | **active** | Not CC signatory; not Diadoc signer; not OWNER |

---

## 3. Attested roster — ORG-0006 SIBCAR

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state | role note |
|-----------------|---------------|-------------------|---------------|-----------------|-----------|
| REL-SIBCAR-01 | PER-0016 Карандашов Максим Петрович | **GENERAL_DIRECTOR** | E1 | **active** | CC signatory / LE-0005; chief accountant same subject |
| REL-SIBCAR-02 | PER-0017 Хаял | **REPRESENTATIVE** | E0 | **active** | Primary operational contact |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **GENERAL_DIRECTOR** | 1 | REL-SIBCAR-01 *(taxonomy: REPRESENTATIVE + role_qualifier)* |
| **REPRESENTATIVE** | 1 | REL-SIBCAR-02 |
| **OWNER** | 0 | *(excluded — «Business Owner» operator signal only)* |
| **EMPLOYEE** | 0 | *(excluded by operator scope)* |

---

## 5. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| PER-0017 → ORG-0006 **OWNER** | «Business Owner» operator signal ≠ OWNER edge | **Forbidden** — operator scope |
| PER-0017 → ORG-0006 **EMPLOYEE** | Operator approved REPRESENTATIVE | **Forbidden** — operator scope |
| Diadoc / EDO signer relationship | **SAFE UNKNOWN** — ME-W2C-SIBCAR-06 | No edge until evidence |
| Person ↔ Person | Wrong family | **Rejected** |
| Person ↔ Project | Wrong family — PRJ-0011 attested without Person edges | **Rejected** |
| ORG-0006 CLIENT_OF ORG-0001 | Already attested REL-0041 | **Not re-minted** — Wave 6B |
| ORG-0006 ↔ ORG-0005 commercial edges | Out of 2C scope | **Wave 6 / separate review** |
| Website / Domain edges | Already attested — no Person edges | **Out of scope** |

---

## 6. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| **EV-W1C-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | REL-SIBCAR-01 — signatory §21–§24; chief accountant §23–§24 |
| **EV-W2C-SIBCAR-OP-01** | Operator mission inputs (2026-06-07) | REL-SIBCAR-02 — identity, Telegram, operational contact |
| **LE-0005** | ООО «СибКар» — AT-W1C-01 | REL-SIBCAR-01 — `document_signatory` crosswalk |
| **AT-W1C-01** | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 endpoint **active** |
| **AT-W2C-SIBCAR-01..02** | [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) | PER-0016, PER-0017 endpoints **active** |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Endpoint cross-reference

| Person | Attested org edges | Primary org (display) | Operational role |
|--------|-------------------|----------------------|------------------|
| PER-0016 | REL-SIBCAR-01 | ORG-0006 | Director / signatory |
| PER-0017 | REL-SIBCAR-02 | ORG-0006 | Primary operational contact |

**Organization display pointer:**

| org_id | primary_contact_person_id | basis |
|--------|---------------------------|-------|
| ORG-0006 | **PER-0017** *(steward-confirmed at 2C)* | REL-SIBCAR-02 primary operational contact |

---

## 8. Cross-register lineage

| Prior register | Relationship | Disposition |
|----------------|--------------|-------------|
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | REL-ZPM-01, REL-ZPM-02 (ORG-0005) | **Unchanged** — separate tranche |
| [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) §7 | REL-SIBCAR-01, REL-SIBCAR-02 queued | **Superseded** — now **active** |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) §4.1 | REL-SIBCAR-01, REL-SIBCAR-02 **missing** | **Superseded** — now **active** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) | Person endpoints |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Organization endpoint |

---

*ATLAS Wave 2C SIBCAR Relationship Register v1 — documentation only.*
