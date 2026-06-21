# ATLAS Wave 2 ZPM Person Register v1

**Status:** **documented** — canonical Person roster for Wave 2 ZPM tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07 · **sync:** 2026-06-07 (ZPM documentation sync)  
**Parent:** [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md)  
**Is not:** attested registry export, runtime, database table, Wave 2B relationship register.

---

## 1. Purpose

Канонический **реестр Person population** Wave 2 tranche **ZPM** (ORG-0005). Одна строка — одна approved Person draft record pending steward attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **2** |
| Population slice **client-side** | **2** |
| Lifecycle **active** | **2** |
| Evidence **E1** (CC-backed) | **1** (PER-0015) |
| Evidence **E0** (operator-direct) | **1** (PER-0014) |
| Attestation | **Complete** — AT-W2-ZPM-01, AT-W2-ZPM-02 |

---

## 2. Population roster — full table

| person_id | canonical_name | primary_organization *(2B)* | population_slice | role_signals | operational_contact | document_signatory | contacts | evidence_tier | evidence_ref | lifecycle_state | attestation_readiness | notes |
|-----------|----------------|------------------------------|------------------|--------------|---------------------|--------------------|----------|---------------|--------------|-----------------|----------------------|-------|
| PER-0015 | Крюков Александр Сергеевич | ORG-0005 ЗПМ | **client-side** | Генеральный директор *(operator)*; Директор *(CC)* | sometimes | **yes** — LE-0004 | phone: +79039573236; other: **SAFE UNKNOWN** | **E1** | EV-W1B-CC-01 §19–§24; E0 phone | **active** | **complete** | AT-W2-ZPM-01; REL-ZPM-01 GENERAL_DIRECTOR |
| PER-0014 | Алексей Владимирович Дубинский | ORG-0005 ЗПМ | **client-side** | зам. директора; исп. директор; техн. директор | **yes** — primary | **no** | TG: @scrash86; phone: +7 913 099 0747; email: dav@assum.ru | **E0** | operator-direct; **not in CC** | **active** | **complete** | AT-W2-ZPM-02; REL-ZPM-02 REPRESENTATIVE; ORG-0005 primary_contact |

---

## 3. Alias register (proposed)

| person_id | alias | alias_type | evidence_ref | attestation_state |
|-----------|-------|------------|--------------|-------------------|
| PER-0014 | Алексей Дубинский | short / informal | E0 operator | **proposed** |
| PER-0014 | Дубинский | surname fragment | E0 operator | **proposed** |
| PER-0015 | — | — | — | — |

---

## 4. Contact register (proposed)

| person_id | channel | value | evidence_ref | attestation_state | notes |
|-----------|---------|-------|--------------|-------------------|-------|
| PER-0014 | telegram | @scrash86 | E0 operator | **proposed** | Primary messaging channel |
| PER-0014 | phone | +7 913 099 0747 | E0 operator | **proposed** | |
| PER-0014 | email | dav@assum.ru | E0 operator | **proposed** | Domain **assum.ru** — contact only; not org identity proof |
| PER-0015 | phone | +79039573236 | E0 operator | **proposed** | Not in CC org phone block |
| PER-0015 | email | **SAFE UNKNOWN** | — | — | |
| PER-0015 | telegram | **SAFE UNKNOWN** | — | — | |

**Org CC contact (informational — not Person contact rows):**

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Org phone / fax | +7 (3852) 72-18-90 | EV-W1B-CC-01 §17 |
| Org email | zakaz@bzmp.ru | EV-W1B-CC-01 §17, §18 |

---

## 5. Evidence index

| Ref | Artifact | Role |
|-----|----------|------|
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | **Primary Counterparty Card** — PER-0015 identity, director, signatory |
| EV-W2-ZPM-OP-01 | Operator mission inputs (2026-06-07) | PER-0014 identity, contacts, operational statements; PER-0015 phone; work acceptance; EDO note |
| EV-W2-ZPM-OP-02 | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) §2, §7.1 | LE-0004 signatory crosswalk |

---

## 6. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W2-ZPM-D-01 | vs Wave 2 attested roster PER-0001..0013 | **Distinct** | No |
| W2-ZPM-D-02 | PER-0015 vs LE-0004 signatory | **Same subject — bind intended** | No |
| W2-ZPM-D-03 | PER-0014 vs CC person lines | **Distinct — CC silent on Дубинский** | No |
| W2-ZPM-D-04 | assum.ru contact vs bzpm org email | **No identity merge** | No |

---

## 7. Wave 2B relationship index *(attested — see Wave 2B ZPM register)*

| relationship_id | source_person | target_organization | relationship_type | lifecycle | attestation |
|-----------------|---------------|---------------------|-------------------|-----------|-------------|
| REL-ZPM-01 | PER-0015 | ORG-0005 ЗПМ | **GENERAL_DIRECTOR** | **active** | Wave 2B ZPM |
| REL-ZPM-02 | PER-0014 | ORG-0005 ЗПМ | **REPRESENTATIVE** | **active** | Wave 2B ZPM |

---

## 8. Readiness summary

| person_id | population | duplicate review | evidence sufficient | attestation (active) | wave 2B deps |
|-----------|------------|------------------|---------------------|----------------------|--------------|
| PER-0015 | **Complete** | **Pass** | **Pass** — E1 CC | **Complete** — AT-W2-ZPM-01 | REL-ZPM-01 **active** ✓ |
| PER-0014 | **Complete** | **Pass** | **Pass** — E0 operator | **Complete** — AT-W2-ZPM-02 | REL-ZPM-02 **active** ✓ |

**Package attestation readiness:** see [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) §7.

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) | Per-person analysis |
| [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) | Attestation sequence |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Prior Wave 2 core roster (PER-0001..0013) |

---

*ATLAS Wave 2 ZPM Person Register v1 — PER-0014/0015 **active**; synced 2026-06-07 per attestation acts AT-W2-ZPM-01..02.*
