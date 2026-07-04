# ATLAS Corvonero Legal Entity Population v1

**Status:** **documented** — dedicated Legal Entity population pass for Corvonero tranche (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-29  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Parent:** [ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md](ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md) · [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md)  
**Companion:** [ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md) · [ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md)  
**Is not:** runtime, API, database, Foundation change, Organization / Project / Website / Domain population.

**Pass intent:** Enrich **LE-0006** with operator-provided banking and address requisites under **E0** evidence **EV-CORV-OP-REQ-01**; confirm **ORG-0009 → LE-0006** binding without minting new Organization, Project, Website, Domain, or **PER-***.

---

## 1. Current Corvo Nero atlas state

| Class | ID | Canonical label | Lifecycle | Prior attestation | This pass |
|-------|-----|-----------------|-----------|-------------------|-----------|
| Organization | **ORG-0009** | Центр автоматизации «Корво Неро» | **active** | AT-CORV-ORG-01 | **Unchanged** |
| Legal Entity | **LE-0006** | ИП Никифоров Роман Вадимович | **active** *(partial → requisites-enriched)* | AT-CORV-ORG-01 *(identity only)* | **Requisites population** |
| Project | **PRJ-0013** | Корво Неро — Яндекс Директ и посадочные страницы | **active** | AT-CORV-PRJ-01 | **Unchanged** |
| Website | **WEB-CORV-01** | `http://lk.corvonero.ru/` | **active** | AT-CORV-WEB-01 | **Unchanged** |
| Domain | **DOM-CORV-01** | corvonero.ru | **active** | AT-CORV-DOM-01 | **Unchanged** |
| Commercial REL | **REL-0042** | ORG-0009 → ORG-0003 **CLIENT_OF** | **active** | AT-CORV-REL-01 | **Unchanged** |

**Contour summary:** Corvonero ATLAS tranche is **fully registered** for Organization, Project, Website, Domain, and commercial edges. **LE-0006** was minted at organization intake (**2026-06-21**) with identifiers only (INN, OGRNIP, legal name). This pass adds **legal_address**, **actual_address**, and **banking requisites** from operator-provided data — still **E0**; no CC file; no E2 registry extract.

**Website context (informational):** `https://lk.corvonero.ru/` — known advertising / landing surface per **WEB-CORV-01**; legal ownership of site **not** in scope of this pass.

---

## 2. Legal Entity roster

### 2.1 Population target

| legal_entity_id | legal_entity_name | legal_entity_type | org_binding | evidence_tier | lifecycle (target) |
|-----------------|-------------------|-------------------|-------------|---------------|-------------------|
| **LE-0006** | ИП Никифоров Роман Вадимович | **ИП** | **ORG-0009** | **E0** | **active** *(requisites-enriched partial)* |

### 2.2 Field population — LE-0006

| Field | Value | Source |
|-------|-------|--------|
| **legal_entity_id** | LE-0006 | Prior mint — ORG intake 2026-06-21 |
| **legal_entity_name** | ИП Никифоров Роман Вадимович | EV-CORV-OP-REQ-01; corroborates EV-CORVONERO-OP-01 |
| **legal_entity_type** | ИП | EV-CORV-OP-REQ-01 |
| **inn** | 540200831636 | EV-CORV-OP-REQ-01 |
| **kpp** | **N/A** *(ИП)* | Model rule |
| **ogrn_ogrnip** | 324547600100482 | EV-CORV-OP-REQ-01 |
| **registration_date** | 2024-06-14 | EV-CORVONERO-OP-01 *(prior intake — not contradicted)* |
| **legal_address** | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | EV-CORV-OP-REQ-01 |
| **actual_address** | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | EV-CORV-OP-REQ-01 |
| **bank_account** | 40802810023400007687 | EV-CORV-OP-REQ-01 |
| **corr_account** | 30101810600000000774 | EV-CORV-OP-REQ-01 |
| **bik** | 045004774 | EV-CORV-OP-REQ-01 |
| **evidence_tier** | **E0** operator-provided requisites | EV-CORV-OP-REQ-01 |
| **source** | **EV-CORV-OP-REQ-01** | Operator requisites pass 2026-06-29 |

### 2.3 Person candidate queue *(not minted)*

| Candidate name | Role hypothesis | Action |
|----------------|-----------------|--------|
| Никифоров Роман Вадимович | Likely **document_signatory** for ИП | **Queued only** — **no** **PER-*** mint in this pass |

---

## 3. Evidence basis

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-CORV-OP-REQ-01** | Operator-provided requisites — Corvo Nero legal entity pass 2026-06-29 | **E0** | **Primary** — addresses, INN, OGRNIP, bank account, corr account, BIK |
| **EV-CORVONERO-OP-01** | [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | **E0** | Prior identity corroboration — legal name, INN, OGRNIP, registration date, commercial context |
| **EV-CORVONERO-OP-02** | Operator statement — site `http://lk.corvonero.ru/` | **E0** | Website context only — **not** legal-entity proof |

**Evidence discipline:** Requisites fields in §2.2 are recorded **only** where cited on **EV-CORV-OP-REQ-01** or non-contradicted prior **EV-CORVONERO-OP-01**. No fabricated CC path; no E2 registry extract claimed.

---

## 4. Duplicate review

| review_id | signal | verdict | blocking |
|-----------|--------|---------|----------|
| CORV-LE-D-01 | INN 540200831636 vs LE-0001..0005 | **No collision** | No |
| CORV-LE-D-02 | OGRNIP 324547600100482 vs attested roster | **No collision** | No |
| CORV-LE-D-03 | LE-0006 vs Makita LE-0006 candidate slot | **Resolved** — LE-0006 bound to Corvonero ИП since 2026-06-21 | No |
| CORV-LE-D-04 | Legal name vs ORG-0001..0008 legal subjects | **Distinct** | No |
| CORV-LE-D-05 | Second LE mint for ORG-0009 | **None** — single LE binding | No |
| CORV-LE-D-06 | Requisites vs prior LE-0006 partial record | **Consistent extension** — no identifier conflict | No |

**Duplicate review summary:** **Pass**

---

## 5. Organization binding

| org_id | org_canonical_name | legal_entity_id | legal_entity_name | binding_kind | evidence_ref | lifecycle |
|--------|-------------------|-----------------|-------------------|--------------|--------------|-----------|
| **ORG-0009** | Центр автоматизации «Корво Неро» | **LE-0006** | ИП Никифоров Роман Вадимович | **legal_subject** | EV-CORV-OP-REQ-01; EV-CORVONERO-OP-01 | **active** |

**Binding rule:** One Organization → one attested Legal Entity for Corvonero tranche. **ORG-0009** record **not** rewritten in this pass — binding already documented in [ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md](ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md) §2–§3; this pass **confirms** and **enriches** LE-side requisites only.

---

## 6. SAFE UNKNOWN inventory

| id | topic | blocks_this_pass |
|----|-------|------------------|
| SU-CORV-LE-01 | Legal signatory contacts | **No** |
| SU-CORV-LE-02 | EDO participant id / operator | **No** |
| SU-CORV-LE-03 | Bank name | **No** |
| SU-CORV-LE-04 | Phone on requisites artifact | **No** |
| SU-CORV-LE-05 | Email on requisites artifact | **No** |
| SU-CORV-LE-06 | Person role confirmation (signatory vs other) | **No** — PER-* deferred |
| SU-CORV-LE-07 | Domain registrant (corvonero.ru) | **No** — Domain layer |
| SU-CORV-LE-08 | Exact ownership of lk.corvonero.ru | **No** — Website layer |
| SU-CORV-LE-09 | E2 registry extract corroboration | **No** — E0 path sufficient for operator requisites |
| SU-CORV-LE-10 | Counterparty Card file in external storage | **No** — Category B org path |

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
| No new ORG / PRJ / WEB / DOM mint | **Pass** |
| No **PER-*** mint | **Pass** — candidate queued only |
| LE-0006 slot — next after LE-0005 | **Pass** — already minted; not re-minted |
| Requisites fields traceable to EV-CORV-OP-REQ-01 | **Pass** |

---

## 8. Readiness verdict

**CORVO NERO LEGAL ENTITY POPULATION COMPLETE**

| Item | State |
|------|-------|
| LE-0006 requisites population | **Complete** — E0 operator-provided |
| Organization binding ORG-0009 → LE-0006 | **Confirmed** |
| Legal Entity attestation act | **AT-CORV-LE-01** — see [ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md) |
| Canonical register | [ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md) |
| Completeness | **partial** — E0 requisites enriched; bank name, EDO, signatory Person, E2 extract **SAFE UNKNOWN** |

---

*ATLAS Corvonero Legal Entity Population v1 — LE-0006 requisites pass; documentation only.*
