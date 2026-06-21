# ATLAS Wave 2C SIBCAR Person Register v1

**Status:** **documented** — canonical Person roster for Wave 2C SIBCAR tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md)  
**Is not:** attested registry export, runtime, database table, Wave 2C relationship register.

---

## 1. Purpose

Канонический **реестр Person population** Wave 2C tranche **SIBCAR** (ORG-0006). Одна строка — одна approved Person record after steward attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **2** |
| Population slice **client-side** | **2** |
| Lifecycle **active** | **2** |
| Evidence **E1** (CC-backed) | **1** (PER-0016) |
| Evidence **E0** (operator-direct) | **1** (PER-0017) |
| Attestation | **Complete** — AT-W2C-SIBCAR-01, AT-W2C-SIBCAR-02 |

---

## 2. Population roster — full table

| person_id | canonical_name | primary_organization *(2C rel)* | population_slice | role_signals | operational_contact | document_signatory | contacts | evidence_tier | evidence_ref | lifecycle_state | attestation_readiness | notes |
|-----------|----------------|----------------------------------|------------------|--------------|---------------------|--------------------|----------|---------------|--------------|-----------------|----------------------|-------|
| PER-0016 | Карандашов Максим Петрович | ORG-0006 SIBCAR | **client-side** | General Director *(operator)*; Руководитель *(CC)*; Главный бухгалтер *(CC)* | **no** | **yes** — LE-0005 | phone/TG/email: **SAFE UNKNOWN** | **E1** | EV-W1C-CC-01 §21–§24 | **active** | **complete** | AT-W2C-SIBCAR-01; REL-SIBCAR-01 GENERAL_DIRECTOR |
| PER-0017 | Хаял | ORG-0006 SIBCAR | **client-side** | Primary Operational Contact; Business Owner *(operator signal)* | **yes** — primary | **no** | TG: @Khayal8888; phone/email: **SAFE UNKNOWN** | **E0** | EV-W2C-SIBCAR-OP-01; **not in CC** | **active** | **complete** | AT-W2C-SIBCAR-02; REL-SIBCAR-02 REPRESENTATIVE; ORG-0006 primary_contact |

---

## 3. Alias register (proposed)

| person_id | alias | alias_type | evidence_ref | attestation_state |
|-----------|-------|------------|--------------|-------------------|
| PER-0016 | — | — | — | — |
| PER-0017 | — | — | — | — |

---

## 4. Contact register (proposed)

| person_id | channel | value | evidence_ref | attestation_state | notes |
|-----------|---------|-------|--------------|-------------------|-------|
| PER-0017 | telegram | @Khayal8888 | E0 EV-W2C-SIBCAR-OP-01 | **active** | Primary messaging channel |
| PER-0017 | phone | **SAFE UNKNOWN** | — | — | |
| PER-0017 | email | **SAFE UNKNOWN** | — | — | |
| PER-0016 | phone | **SAFE UNKNOWN** | — | — | |
| PER-0016 | telegram | **SAFE UNKNOWN** | — | — | |
| PER-0016 | email | **SAFE UNKNOWN** | — | — | |

**Org CC contact (informational — not Person contact rows):**

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Org email | info_sibcar@mail.ru | EV-W1C-CC-01 §16 |
| Org phone / fax | **SAFE UNKNOWN** | ME-W1C-04 |

---

## 5. Evidence index

| Ref | Artifact | Role |
|-----|----------|------|
| EV-W1C-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | **Primary Counterparty Card** — PER-0016 identity, signatory, chief accountant |
| EV-W2C-SIBCAR-OP-01 | Operator mission inputs (2026-06-07) | PER-0017 identity (Хаял), Telegram, operational role; two-person model |
| EV-W1C-01 | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) §2, §7.1 | LE-0005 signatory crosswalk |

---

## 6. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W2C-SIBCAR-D-01 | vs Wave 2 attested roster PER-0001..0015 | **Distinct** | No |
| W2C-SIBCAR-D-02 | PER-0016 vs LE-0005 signatory | **Same subject — bind intended** | No |
| W2C-SIBCAR-D-03 | PER-0017 vs CC person lines | **Distinct — CC silent on Хаял** | No |
| W2C-SIBCAR-D-04 | PER-0016 vs PER-0017 | **Distinct persons** | No |
| W2C-SIBCAR-D-05 | info_sibcar@mail.ru vs Person rows | **No identity merge** | No |

---

## 7. Wave 2C relationship index *(attested — see Wave 2C SIBCAR relationship register)*

| relationship_id | source_person | target_organization | relationship_type | lifecycle | attestation |
|-----------------|---------------|---------------------|-------------------|-----------|-------------|
| REL-SIBCAR-01 | PER-0016 | ORG-0006 SIBCAR | **GENERAL_DIRECTOR** | **active** | Wave 2C SIBCAR relationship pass |
| REL-SIBCAR-02 | PER-0017 | ORG-0006 SIBCAR | **REPRESENTATIVE** | **active** | Wave 2C SIBCAR relationship pass |

---

## 8. Readiness summary

| person_id | population | duplicate review | evidence sufficient | attestation (active) | wave 2C rel deps |
|-----------|------------|------------------|---------------------|----------------------|------------------|
| PER-0016 | **Complete** | **Pass** | **Pass** — E1 CC | **Complete** — AT-W2C-SIBCAR-01 | REL-SIBCAR-01 **active** ✓ |
| PER-0017 | **Complete** | **Pass** | **Pass** — E0 operator | **Complete** — AT-W2C-SIBCAR-02 | REL-SIBCAR-02 **active** ✓ |

**Package attestation readiness:** see [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) §7.

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) | Per-person analysis |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) | Attestation sequence |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Parity template |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) | Prior discovery state |

---

*ATLAS Wave 2C SIBCAR Person Register v1 — PER-0016/0017 **active**; synced 2026-06-07 per attestation acts AT-W2C-SIBCAR-01..02.*
