# ATLAS Wave 2B ZPM Relationship Population v1

**Status:** **documented** — canonical Person → Organization relationship population plan for Wave 2B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 3 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation (ORG-0001..0004): **COMPLETE**
- Wave 1B BZPM Attestation (ORG-0005, LE-0004): **COMPLETE** — AT-W1B-01
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- Wave 2 ZPM Person attestation (PER-0014, PER-0015): **COMPLETE** — AT-W2-ZPM-01..02
- Population verdict: **READY FOR WAVE 2B ZPM RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Person → Organization** relationships для Wave 2B tranche **ZPM** (ORG-0005): состав рёбер, типы, evidence basis, lifecycle intent, explicit exclusions, границы foundation.

**Normative scope Wave 2B ZPM:**

```text
Person → Organization relationships only (2 records)
Target organization: ORG-0005 ЗПМ only
No Person ↔ Person
No Person ↔ Project
No Organization ↔ Organization
No new entity types
No new relationship families
```

**Binding operator decisions (this mission):**

- REL-ZPM-01 — PER-0015 → ORG-0005 **GENERAL_DIRECTOR** (not OWNER despite 100% beneficial owner in CC).
- REL-ZPM-02 — PER-0014 → ORG-0005 **REPRESENTATIVE** (not EMPLOYEE; operator operational contact pattern).
- Diadoc / EDO signer — **SAFE UNKNOWN**; no relationship minted.
- Beneficial ownership — CC fact only; **no** OWNER edge.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Person endpoints (active) | **2** (PER-0014, PER-0015) |
| Organization endpoint (active) | **1** (ORG-0005) |
| Relationship families used | Person → Organization only |

### 2.1 Summary table

| relationship_id | source_person | target_organization | relationship_type | organization group | attestation readiness |
|-----------------|---------------|---------------------|-------------------|--------------------|-----------------------|
| REL-ZPM-01 | PER-0015 Крюков Александр Сергеевич | ORG-0005 ЗПМ | **GENERAL_DIRECTOR** | ZPM / BZPM | **ready** |
| REL-ZPM-02 | PER-0014 Алексей Владимирович Дубинский | ORG-0005 ЗПМ | **REPRESENTATIVE** | ZPM / BZPM | **ready** |

---

## 3. Per-relationship analysis

### 3.1 REL-ZPM-01 — Крюков → ЗПМ (director / signatory)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-01 |
| **source_person** | PER-0015 Крюков Александр Сергеевич |
| **target_organization** | ORG-0005 ЗПМ |
| **relationship_type** | **GENERAL_DIRECTOR** |
| **attestation_basis** | E1 EV-W1B-CC-01 §19–§24 — «Директор Крюков Александр Сергеевич»; LE-0004 `document_signatory` (AT-W1B-01); PER-0015 **active** (AT-W2-ZPM-01); ORG-0005 **active** (AT-W1B-01) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | Director / document signatory, PER-0015 → ORG-0005 |
| **notes** | CC beneficial owner 100% §20 — recorded on Person/LE; **no** OWNER relationship per operator scope. Operator title «Генеральный директор» vs CC «Директор» — CC controls legal signatory field. |

### 3.2 REL-ZPM-02 — Дубинский → ЗПМ (operational contact)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-02 |
| **source_person** | PER-0014 Алексей Владимирович Дубинский |
| **target_organization** | ORG-0005 ЗПМ |
| **relationship_type** | **REPRESENTATIVE** |
| **attestation_basis** | E0 EV-W2-ZPM-OP-01 — operator-direct identity, role signals, multi-channel contacts; primary operational contact for Polygon vendor work on ЗПМ account; PER-0014 **active** (AT-W2-ZPM-02); ORG-0005 **active** |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **slot** | Primary operational contact, PER-0014 → ORG-0005 |
| **notes** | CC silent on Дубинский (EFV-06). Role signals (зам. директора; исп. директор; техн. директор) — operator context only; **not** EMPLOYEE attestation. Main communication channel between Polygon and ZPM. |

---

## 4. Organization anchor graph — ORG-0005

```text
PER-0015 ──GENERAL_DIRECTOR──► ORG-0005 ЗПМ   (E1 CC signatory)
PER-0014 ──REPRESENTATIVE────► ORG-0005 ЗПМ   (E0 operational contact)
```

**Display primary contact (steward):** PER-0014 — primary operational contact; eligible for ORG-0005 `primary_contact_person_id` at attestation.

---

## 5. Explicit exclusions and deferred relationships

| Item | Treatment | Reason |
|------|-----------|--------|
| PER-0015 → ORG-0005 **OWNER** | **Do not create** | Operator scope — beneficial owner CC fact ≠ OWNER edge |
| PER-0014 → ORG-0005 **EMPLOYEE** | **Do not create** | Operator approved REPRESENTATIVE only |
| Diadoc / EDO signer edge | **Do not create** | **SAFE UNKNOWN** — ME-W2-ZPM-05 |
| Person ↔ Person | **Forbidden** | Foundation scope |
| Person ↔ Project | **Forbidden** | Wave 3+ |
| ORG-0005 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| ORG-0005 ↔ ORG-0006 commercial edges | **Deferred** | Wave 6 / COR-W1B-06 |
| New Person / Organization entities | **Forbidden** | Endpoints already active |
| Website / Domain entities | **Deferred** | Wave 4 / 5 |

---

## 6. Foundation consistency

| Foundation doc | Wave 2B ZPM alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Two directed Person→Org edges to single org anchor — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 | REPRESENTATIVE in baseline — **yes**; GENERAL_DIRECTOR → REPRESENTATIVE family + `role_qualifier: general_director` (W2B-ZPM-TAX-01, analog W2B-TAX-01) |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PER-0014/0015 / ORG-0005 **active** — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active` — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Person → Organization only).

**W2B-ZPM-TAX-01:** `GENERAL_DIRECTOR` is an operator-approved **role qualifier** for REL-ZPM-01; taxonomy canonical type remains **REPRESENTATIVE** per RR-02 until expansion review adds explicit type (consistent with REL-0015 Triumph precedent).

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) | Person endpoint prerequisite |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | Organization endpoint prerequisite |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 2B ZPM Relationship Population v1 — documentation only.*
