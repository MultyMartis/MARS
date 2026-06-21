# ATLAS Wave 2C SIBCAR Relationship Population v1

**Status:** **documented** — canonical Person → Organization relationship population plan for Wave 2C SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 3+ execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Attestation (ORG-0006, LE-0005): **COMPLETE** — AT-W1C-01
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- Wave 2 ZPM Person attestation (PER-0014, PER-0015): **COMPLETE**
- Wave 2C SIBCAR Person attestation (PER-0016, PER-0017): **COMPLETE** — AT-W2C-SIBCAR-01..02
- Population verdict: **READY FOR WAVE 2C SIBCAR RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Person → Organization** relationships для Wave 2C tranche **SIBCAR** (ORG-0006): состав рёбер, типы, evidence basis, lifecycle intent, explicit exclusions, границы foundation.

**Normative scope Wave 2C SIBCAR relationships:**

```text
Person → Organization relationships only (2 records)
Target organization: ORG-0006 SIBCAR only
No Person ↔ Person
No Person ↔ Project
No Organization ↔ Organization (commercial)
No new entity types
No new relationship families
```

**Binding operator decisions (this mission):**

- REL-SIBCAR-01 — PER-0016 → ORG-0006 **GENERAL_DIRECTOR** (CC signatory / director anchor).
- REL-SIBCAR-02 — PER-0017 → ORG-0006 **REPRESENTATIVE** (primary operational contact; not EMPLOYEE).
- ORG-0006 `primary_contact_person_id` = **PER-0017** at relationship attestation.
- «Business Owner» (PER-0017) — role signal only; **no** OWNER edge.
- Diadoc / EDO signer — **SAFE UNKNOWN**; no relationship minted.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Person endpoints (active) | **2** (PER-0016, PER-0017) |
| Organization endpoint (active) | **1** (ORG-0006) |
| Relationship families used | Person → Organization only |

### 2.1 Summary table

| relationship_id | source_person | target_organization | relationship_type | organization group | attestation readiness |
|-----------------|---------------|---------------------|-------------------|--------------------|-----------------------|
| REL-SIBCAR-01 | PER-0016 Карандашов Максим Петрович | ORG-0006 SIBCAR | **GENERAL_DIRECTOR** | SIBCAR / W1-C | **ready** |
| REL-SIBCAR-02 | PER-0017 Хаял | ORG-0006 SIBCAR | **REPRESENTATIVE** | SIBCAR / W1-C | **ready** |

---

## 3. Per-relationship analysis

### 3.1 REL-SIBCAR-01 — Карандашов → SIBCAR (director / signatory)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-01 |
| **source_person** | PER-0016 Карандашов Максим Петрович |
| **target_organization** | ORG-0006 SIBCAR |
| **relationship_type** | **GENERAL_DIRECTOR** |
| **attestation_basis** | E1 EV-W1C-CC-01 §21–§24 — «Руководитель Карандашов Максим Петрович»; LE-0005 `document_signatory` (AT-W1C-01); chief accountant same subject §23–§24; PER-0016 **active** (AT-W2C-SIBCAR-01); ORG-0006 **active** (AT-W1C-01) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | Director / document signatory / chief accountant, PER-0016 → ORG-0006 |
| **notes** | Operator title «General Director» vs CC «Руководитель» — CC controls legal signatory field. Exact должность **SAFE UNKNOWN**. |

### 3.2 REL-SIBCAR-02 — Хаял → SIBCAR (operational contact)

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-02 |
| **source_person** | PER-0017 Хаял |
| **target_organization** | ORG-0006 SIBCAR |
| **relationship_type** | **REPRESENTATIVE** |
| **attestation_basis** | E0 EV-W2C-SIBCAR-OP-01 — operator-direct identity, Telegram @Khayal8888, primary operational contact; PER-0017 **active** (AT-W2C-SIBCAR-02); ORG-0006 **active** |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **slot** | Primary operational contact, PER-0017 → ORG-0006 |
| **notes** | CC silent on Хаял (EFV-06). «Business Owner» — operator role signal only; **not** OWNER edge. Full patronymic **SAFE UNKNOWN**. Main communication channel between Polygon and SIBCAR via Telegram. |

---

## 4. Organization anchor graph — ORG-0006

```text
PER-0016 ──GENERAL_DIRECTOR──► ORG-0006 SIBCAR   (E1 CC signatory)
PER-0017 ──REPRESENTATIVE────► ORG-0006 SIBCAR   (E0 operational contact)

ORG-0006.primary_contact_person_id = PER-0017
```

**Display primary contact (steward):** PER-0017 — primary operational contact; attested at Wave 2C SIBCAR relationship pass.

---

## 5. Explicit exclusions and deferred relationships

| Item | Treatment | Reason |
|------|-----------|--------|
| PER-0017 → ORG-0006 **OWNER** | **Do not create** | «Business Owner» operator signal ≠ OWNER edge — ZPM precedent |
| PER-0017 → ORG-0006 **EMPLOYEE** | **Do not create** | Operator approved REPRESENTATIVE only |
| Diadoc / EDO signer edge | **Do not create** | **SAFE UNKNOWN** — ME-W2C-SIBCAR-06 |
| Person ↔ Person | **Forbidden** | Foundation scope |
| Person ↔ Project | **Forbidden** | Already attested Waves 3–5 — no Person edges added |
| ORG-0006 CLIENT_OF ORG-0001 | **Already attested** | REL-0041 — Wave 6B; **do not re-mint** |
| ORG-0006 ↔ ORG-0005 commercial edges | **Deferred** | Wave 6 / separate review |
| New Person / Organization entities | **Forbidden** | Endpoints already active |
| Website / Domain entities | **Out of scope** | Already attested — no modification |

---

## 6. Foundation consistency

| Foundation doc | Wave 2C SIBCAR alignment |
|----------------|--------------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Two directed Person→Org edges to single org anchor — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 | REPRESENTATIVE in baseline — **yes**; GENERAL_DIRECTOR → REPRESENTATIVE family + `role_qualifier: general_director` (W2C-SIBCAR-TAX-01, analog W2B-ZPM-TAX-01) |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PER-0016/0017 / ORG-0006 **active** — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active` — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Person → Organization only).

**W2C-SIBCAR-TAX-01:** `GENERAL_DIRECTOR` is an operator-approved **role qualifier** for REL-SIBCAR-01; taxonomy canonical type remains **REPRESENTATIVE** per RR-02 until expansion review adds explicit type (consistent with REL-ZPM-01 / REL-0015 Triumph precedent).

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) | Person endpoint prerequisite |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Organization endpoint prerequisite |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md) | Parity template |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 2C SIBCAR Relationship Population v1 — documentation only.*
