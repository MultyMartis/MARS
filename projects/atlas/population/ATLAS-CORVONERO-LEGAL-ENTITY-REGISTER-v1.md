# ATLAS Corvonero Legal Entity Register v1

**Status:** **documented** — canonical Legal Entity roster for Corvonero tranche (**active**; requisites-enriched attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-29  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Parent:** [ATLAS-CORVONERO-LEGAL-ENTITY-POPULATION-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-POPULATION-v1.md) · [ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-ATTESTATION-v1.md)  
**Is not:** runtime registry, CRM export, database table, Organization roster (see org register).

---

## 1. Current Corvo Nero atlas state

| Class | ID | Status in contour | Relation to LE-0006 |
|-------|-----|-------------------|---------------------|
| Organization | ORG-0009 | **active** | **Bound** — legal_subject |
| Legal Entity | LE-0006 | **active** *(requisites-enriched partial)* | **This register** |
| Project | PRJ-0013 | **active** | Indirect — same org anchor |
| Website | WEB-CORV-01 | **active** | No LE edge — owner **SAFE UNKNOWN** |
| Domain | DOM-CORV-01 | **active** | No LE edge — registrant **SAFE UNKNOWN** |
| Commercial | REL-0042 | **active** | Org-level only |

**Prior state:** LE-0006 minted **2026-06-21** with identity fields only ([ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md](ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md)). **This register** is the dedicated Legal Entity canonical roster after operator requisites pass **2026-06-29**.

---

## 2. Legal Entity roster

### 2.1 Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** | **1** (LE-0006) |
| Evidence tier **E0** | **1** |
| Attestation | **Complete** — AT-CORV-LE-01 |

### 2.2 Population roster — full table

| legal_entity_id | legal_entity_name | legal_entity_type | jurisdiction | inn | kpp | ogrn_ogrnip | registration_date | legal_address | actual_address | settlement_account | correspondent_account | bik | evidence_tier | source | org_id | lifecycle_state | attestation_ref | completeness |
|-----------------|-------------------|-------------------|--------------|-----|-----|-------------|-------------------|---------------|----------------|--------------------|-----------------------|-----|---------------|--------|--------|-----------------|-----------------|--------------|
| **LE-0006** | ИП Никифоров Роман Вадимович | **individual_entrepreneur** *(ИП)* | **RU** | 540200831636 | **N/A** *(ИП)* | 324547600100482 | 2024-06-14 | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | 40802810023400007687 | 30101810600000000774 | 045004774 | **E0** | EV-CORV-OP-REQ-01 | **ORG-0009** | **active** | AT-CORV-LE-01 | **partial** — E0 operator requisites; bank name, tax system, registration authority, signatory contacts **SAFE UNKNOWN** |

**Field alias map (register ↔ population):** `bank_account` = `settlement_account`; `corr_account` = `correspondent_account`; `ogrn_ogrnip` = `ogrnip` for ИП.

### 2.2a Canonical field verification — LE-0006

| Canonical field | Value | Status |
|-----------------|-------|--------|
| **legal_entity_type** | **individual_entrepreneur** | **Present** |
| **jurisdiction** | **RU** | **Present** |
| **legal_address** | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | **Present** |
| **actual_address** | *(same as legal_address)* | **Present** |
| **inn** | 540200831636 | **Present** |
| **ogrnip** | 324547600100482 | **Present** |
| **bik** | 045004774 | **Present** |
| **settlement_account** | 40802810023400007687 | **Present** |
| **correspondent_account** | 30101810600000000774 | **Present** |
| **bank_name** | — | **SAFE UNKNOWN** |
| **tax_system** | — | **SAFE UNKNOWN** |
| **registration_authority** | — | **SAFE UNKNOWN** |
| **legal_signatory_contact** | — | **SAFE UNKNOWN** |
| **operational_contacts** | — | **SAFE UNKNOWN** |
| **registrar** | — | **SAFE UNKNOWN** *(Domain layer — DOM-CORV-01)* |
| **domain ownership confirmation** | — | **SAFE UNKNOWN** *(Website / Domain layers)* |

**Note:** LE-0001..0005 attested in prior waves. LE-0006 assigned to Corvonero ИП — Makita LE-0006 candidate slot **resolved** (CORV-ORG-D-06).

### 2.3 Person candidate queue *(not in roster)*

| candidate_name | queued_role_hypothesis | per_id | status |
|----------------|------------------------|--------|--------|
| Никифоров Роман Вадимович | document_signatory *(ИП — unconfirmed)* | — | **queued** — no **PER-*** mint |

---

## 3. Evidence basis

| Ref | Artifact | Tier | Fields supported |
|-----|----------|------|------------------|
| **EV-CORV-OP-REQ-01** | Operator-provided requisites — 2026-06-29 | **E0** | legal_entity_name, type, addresses, INN, OGRNIP, bank_account, corr_account, bik |
| **EV-CORVONERO-OP-01** | [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | **E0** | Identity corroboration; registration_date |
| **EV-CORVONERO-OP-02** | Operator statement — lk.corvonero.ru | **E0** | Contextual website only |

---

## 4. Duplicate review

| review_id | pair / signal | verdict | blocking |
|-----------|---------------|---------|----------|
| CORV-LE-D-01 | INN 540200831636 vs LE-0001..0005 | **Distinct** | No |
| CORV-LE-D-02 | OGRNIP 324547600100482 vs attested roster | **Distinct** | No |
| CORV-LE-D-03 | LE-0006 vs duplicate LE for same INN | **None** | No |
| CORV-LE-D-04 | vs ORG-0007 Makita legal deferral | **Distinct subject** | No |
| CORV-LE-D-05 | Requisites re-entry vs org register identifiers | **Consistent** | No |

**Duplicate review summary:** **Pass**

---

## 5. Organization binding

| org_id | canonical_name | legal_entity_id | legal_entity_name | binding_evidence | lifecycle |
|--------|----------------|-----------------|-------------------|------------------|-----------|
| **ORG-0009** | Центр автоматизации «Корво Неро» | **LE-0006** | ИП Никифоров Роман Вадимович | EV-CORV-OP-REQ-01; EV-CORVONERO-OP-01; AT-CORV-ORG-01 | **active** |

**Cross-reference:** Organization roster [ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md](ATLAS-CORVONERO-ORGANIZATION-REGISTER-v1.md) §3 — **org record unchanged**; LE enrichment documented here.

---

## 6. SAFE UNKNOWN inventory

| id | topic | canonical_field | blocks_attestation |
|----|-------|-----------------|-------------------|
| SU-CORV-LE-01 | Legal signatory contacts | **legal_signatory_contact** | **No** |
| SU-CORV-LE-02 | EDO | — | **No** |
| SU-CORV-LE-03 | Bank name | **bank_name** | **No** |
| SU-CORV-LE-04 | Phone | *(operational_contacts)* | **No** |
| SU-CORV-LE-05 | Email | *(operational_contacts)* | **No** |
| SU-CORV-LE-06 | Person role confirmation | **legal_signatory_contact** | **No** |
| SU-CORV-LE-07 | Domain registrant | **registrar** | **No** |
| SU-CORV-LE-08 | Exact ownership of lk.corvonero.ru | **domain ownership confirmation** | **No** |
| SU-CORV-LE-09 | E2 registry extract | — | **No** |
| SU-CORV-LE-10 | CC file in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\corvonero\` | — | **No** |
| SU-CORV-LE-11 | Tax system (НДС / УСН posture) | **tax_system** | **No** |
| SU-CORV-LE-12 | Registration authority (ФНС / registering body) | **registration_authority** | **No** |
| SU-CORV-LE-13 | Operational contacts (phone, email bundle) | **operational_contacts** | **No** |

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
| Single LE-0006 row — no duplicate mint | **Pass** |
| All populated fields evidence-backed | **Pass** |

---

## 8. Readiness verdict

**CORVO NERO LEGAL ENTITY POPULATION COMPLETE**

LE-0006 **active** with operator-provided requisites at **E0**; binding **ORG-0009 → LE-0006** confirmed; attestation **AT-CORV-LE-01** executed.

---

*ATLAS Corvonero Legal Entity Register v1 — LE-0006 **active** (E0 requisites-enriched partial).*
