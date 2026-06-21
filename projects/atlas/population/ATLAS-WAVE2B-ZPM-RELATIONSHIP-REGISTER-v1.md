# ATLAS Wave 2B ZPM Relationship Register v1

**Status:** **attested** — canonical Person → Organization relationship roster after Wave 2B ZPM attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, Person registry, org↔org registry, Wave 2B core register extension.

---

## 1. Purpose

Канонический **реестр аттестированных Person → Organization relationships** Wave 2B tranche **ZPM** (ORG-0005). Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Person → Organization) | **2** |
| Lifecycle **active** | **2** |
| Lifecycle deferred / proposed | **0** |
| Target organization | **ORG-0005 ЗПМ** |
| Relationship families | Person → Organization only |

---

## 2. Attested roster — full table

| relationship_id | source_person | target_organization | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|---------------|---------------------|-------------------|-------------------|---------------|-----------------|-------|
| REL-ZPM-01 | PER-0015 Крюков Александр Сергеевич | ORG-0005 ЗПМ | **GENERAL_DIRECTOR** | E1 EV-W1B-CC-01 §19–§24; LE-0004 signatory AT-W1B-01 | **E1** | **active** | Director / document signatory; W2B-ZPM-TAX-01 |
| REL-ZPM-02 | PER-0014 Алексей Владимирович Дубинский | ORG-0005 ЗПМ | **REPRESENTATIVE** | E0 EV-W2-ZPM-OP-01; primary operational contact Polygon↔ZPM | **E0** | **active** | Not CC signatory; not Diadoc signer |

---

## 3. Attested roster — ORG-0005 ЗПМ

| relationship_id | source_person | relationship_type | evidence_tier | lifecycle_state | role note |
|-----------------|---------------|-------------------|---------------|-----------------|-----------|
| REL-ZPM-01 | PER-0015 Крюков Александр Сергеевич | **GENERAL_DIRECTOR** | E1 | **active** | CC director / LE-0004 signatory |
| REL-ZPM-02 | PER-0014 Алексей Владимирович Дубинский | **REPRESENTATIVE** | E0 | **active** | Primary operational contact |

---

## 4. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **GENERAL_DIRECTOR** | 1 | REL-ZPM-01 *(taxonomy: REPRESENTATIVE + role_qualifier)* |
| **REPRESENTATIVE** | 1 | REL-ZPM-02 |
| **OWNER** | 0 | *(excluded by operator scope)* |
| **EMPLOYEE** | 0 | *(excluded by operator scope)* |

---

## 5. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| PER-0015 → ORG-0005 **OWNER** | Beneficial owner CC fact ≠ OWNER edge | **Forbidden** — operator scope |
| PER-0014 → ORG-0005 **EMPLOYEE** | Operator approved REPRESENTATIVE | **Forbidden** — operator scope |
| Diadoc / EDO signer relationship | **SAFE UNKNOWN** — ME-W2-ZPM-05 | No edge until evidence |
| Person ↔ Person | Wrong family | **Rejected** |
| Person ↔ Project | Wrong wave | **Wave 3+** |
| ORG-0005 CLIENT_OF ORG-0001 | Org ↔ Org out of 2B scope | **Wave 6** |
| ORG-0005 ↔ ORG-0006 commercial edges | COR-W1B-06 | **Wave 6 / separate review** |
| Website / Domain edges | Wrong family / wave | **Wave 4 / 5** |

---

## 6. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| **EV-W1B-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | REL-ZPM-01 — director §19–§24; beneficial owner §20 *(Person/LE only)* |
| **EV-W2-ZPM-OP-01** | Operator mission inputs (2026-06-07) | REL-ZPM-02 — identity, contacts, operational statements |
| **LE-0004** | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» — AT-W1B-01 | REL-ZPM-01 — `document_signatory` crosswalk |
| **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 endpoint **active** |
| **AT-W2-ZPM-01..02** | [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) | PER-0014, PER-0015 endpoints **active** |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 7. Endpoint cross-reference

| Person | Attested org edges | Primary org (display) | Operational role |
|--------|-------------------|----------------------|------------------|
| PER-0014 | REL-ZPM-02 | ORG-0005 | Primary operational contact |
| PER-0015 | REL-ZPM-01 | ORG-0005 | Director / signatory (sometimes operational) |

**Organization display pointer:**

| org_id | primary_contact_person_id | basis |
|--------|---------------------------|-------|
| ORG-0005 | **PER-0014** *(steward-confirmed at 2B)* | REL-ZPM-02 primary operational contact |

---

## 8. Cross-register lineage

| Prior register | Relationship | Disposition |
|----------------|--------------|-------------|
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | REL-0001..0015 (ORG-0001..0004) | **Unchanged** — separate tranche |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) §7 | REL-ZPM-01, REL-ZPM-02 queued | **Superseded** — now **active** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) | Person endpoints |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | Organization endpoint |

---

*ATLAS Wave 2B ZPM Relationship Register v1 — documentation only.*
