# ATLAS Corvonero Legal Entity Attestation v1

**Status:** **documented** — attestation act for Corvonero Legal Entity requisites population.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-29  
**Register:** [ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md)  
**Population plan:** [ATLAS-CORVONERO-LEGAL-ENTITY-POPULATION-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-POPULATION-v1.md)  
**Is not:** E2 registry extract attestation, CC attestation, runtime activation, Organization re-attestation.

---

## 1. Current Corvo Nero atlas state

| Entity | ID | Pre-pass | Post-pass |
|--------|-----|----------|-----------|
| Organization | ORG-0009 | **active** (AT-CORV-ORG-01) | **Unchanged** |
| Legal Entity | LE-0006 | **active** partial — identity only | **active** requisites-enriched partial (AT-CORV-LE-01) |
| Project | PRJ-0013 | **active** | **Unchanged** |
| Website | WEB-CORV-01 | **active** | **Unchanged** |
| Domain | DOM-CORV-01 | **active** | **Unchanged** |
| Commercial REL | REL-0042 | **active** | **Unchanged** |

**Attestation scope:** Dedicated Legal Entity layer pass — addresses and banking requisites under **EV-CORV-OP-REQ-01**. Does **not** supersede **AT-CORV-ORG-01**; supplements LE completeness within **E0** bounds.

---

## 2. Legal Entity roster

| legal_entity_id | legal_entity_name | legal_entity_type | evidence_tier | lifecycle (attested) | completeness |
|-----------------|-------------------|-------------------|---------------|----------------------|--------------|
| **LE-0006** | ИП Никифоров Роман Вадимович | **ИП** | **E0** | **active** *(requisites-enriched partial)* | Addresses + bank ids recorded; bank name, EDO, signatory Person **SAFE UNKNOWN** |

**Attested requisites subset (EV-CORV-OP-REQ-01):**

| Field | Value | Attested |
|-------|-------|----------|
| inn | 540200831636 | **Yes** |
| ogrn_ogrnip | 324547600100482 | **Yes** |
| legal_address | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | **Yes** |
| actual_address | *(same as legal_address)* | **Yes** |
| bank_account | 40802810023400007687 | **Yes** |
| corr_account | 30101810600000000774 | **Yes** |
| bik | 045004774 | **Yes** |

---

## 3. Evidence basis

| Ref | Tier | Role in attestation |
|-----|------|---------------------|
| **EV-CORV-OP-REQ-01** | **E0** | **Primary** — operator-provided requisites for attested fields in §2 |
| **EV-CORVONERO-OP-01** | **E0** | Corroboration — legal name, INN, OGRNIP consistency with org intake |
| **EV-CORVONERO-OP-02** | **E0** | Out of scope — website context only |

**Tier discipline:** **E0** operator-provided requisites — sufficient for documented population pass per Category B org contour; **not** equivalent to E1 CC or E2 registry extract attestation.

---

## 4. Duplicate review

| review_id | check | result |
|-----------|-------|--------|
| CORV-LE-D-01 | INN uniqueness vs LE-0001..0005 | **Pass** |
| CORV-LE-D-02 | OGRNIP uniqueness | **Pass** |
| CORV-LE-D-03 | No second LE for ORG-0009 | **Pass** |
| CORV-LE-D-04 | Requisites vs prior LE-0006 identity | **Pass** — consistent |

**Duplicate review summary:** **Pass**

---

## 5. Organization binding

| attestation_id | org_id | legal_entity_id | binding | evidence | verdict |
|----------------|--------|-----------------|---------|----------|---------|
| **AT-CORV-LE-01** | **ORG-0009** | **LE-0006** | legal_subject | EV-CORV-OP-REQ-01; EV-CORVONERO-OP-01 | **active** |

**Binding confirmation:** ORG-0009 Центр автоматизации «Корво Неро» → LE-0006 ИП Никифоров Роман Вадимович — **unchanged** from org intake; requisites attestation **does not** alter Organization record.

---

## 6. SAFE UNKNOWN inventory

| id | topic | attestation impact |
|----|-------|-------------------|
| SU-CORV-LE-01 | Legal signatory contacts | Does not block AT-CORV-LE-01 |
| SU-CORV-LE-02 | EDO | Does not block |
| SU-CORV-LE-03 | Bank name | Does not block |
| SU-CORV-LE-04 | Phone | Does not block |
| SU-CORV-LE-05 | Email | Does not block |
| SU-CORV-LE-06 | Person role confirmation | Does not block — **PER-*** deferred; candidate queued |
| SU-CORV-LE-07 | Domain registrant | Out of scope |
| SU-CORV-LE-08 | Exact ownership of lk.corvonero.ru | Out of scope |

---

## 7. Validation

| Gate | Result |
|------|--------|
| ORG-0009 unchanged | **Pass** |
| PRJ-0013 unchanged | **Pass** |
| WEB-CORV-01 unchanged | **Pass** |
| No duplicate Organization | **Pass** |
| No Website changes | **Pass** |
| No Domain changes | **Pass** |
| No commercial relationship changes | **Pass** |
| No Foundation changes | **Pass** |
| No **PER-*** mint | **Pass** |
| LE fields within E0 evidence only | **Pass** |
| No fabricated domain / site owner from requisites | **Pass** |

---

## 8. Readiness verdict

### Attestation act

| attestation_id | entities | evidence | verdict |
|----------------|----------|----------|---------|
| **AT-CORV-LE-01** | LE-0006 | EV-CORV-OP-REQ-01; EV-CORVONERO-OP-01 | **active** *(requisites-enriched partial)* |

### Population verdict

**CORVO NERO LEGAL ENTITY POPULATION COMPLETE**

---

*ATLAS Corvonero Legal Entity Attestation v1 — AT-CORV-LE-01 **complete**.*
