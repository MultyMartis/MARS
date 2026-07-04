# ATLAS Corvonero Organization Register v1

**Status:** **documented** — canonical Organization roster for Corvonero tranche (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Parent:** [ATLAS-CORVONERO-ORGANIZATION-ATTESTATION-v1.md](ATLAS-CORVONERO-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md)  
**Upstream intake:** [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md)  
**Is not:** runtime registry, CRM export, relationship register.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Wave tier CORV | **1** |
| Classification i-SEO client | **1** |
| Lifecycle **active** | **1** (ORG-0009) |
| Legal entity **active** *(E0 requisites-enriched)* | **1** (LE-0006) |
| Attestation | **Complete** — AT-CORV-ORG-01; LE requisites **AT-CORV-LE-01** |

---

## 2. Population roster — full table

| org_id | canonical_name | wave_tier | classification | business_role | legal_entity_id | legal_entity_name | inn | kpp | ogrn_ogrnip | aliases | primary_website | primary_domain | evidence_tier | lifecycle_state | attestation_ref | notes |
|--------|----------------|-----------|----------------|---------------|-----------------|-------------------|-----|-----|-------------|---------|-----------------|----------------|---------------|-----------------|-----------------|-------|
| ORG-0009 | **Центр автоматизации «Корво Неро»** | **CORV** | **i-SEO client** | **CLIENT** | **LE-0006** | ИП Никифоров Роман Вадимович | 540200831636 | **N/A** *(ИП)* | 324547600100482 | Корво Неро; Corvo Nero; corvonero | lk.corvonero.ru *(display)* | corvonero.ru *(display)* | **E0** | **active** | AT-CORV-ORG-01 | Category B i-SEO channel; base region Новосибирск; CC **SAFE UNKNOWN** |

---

## 3. Legal entity index

| legal_entity_id | legal_name | legal_form | jurisdiction | inn | kpp | ogrn_ogrnip | registration_date | legal_address | actual_address | settlement_account | correspondent_account | bik | lifecycle_state | org_id | evidence_tier | attestation_ref | completeness |
|-----------------|------------|------------|--------------|-----|-----|-------------|-------------------|---------------|----------------|--------------------|-----------------------|-----|-----------------|--------|---------------|-----------------|--------------|
| LE-0006 | ИП Никифоров Роман Вадимович | **ИП** *(individual_entrepreneur)* | **RU** | 540200831636 | **N/A** *(ИП)* | 324547600100482 | 2024-06-14 | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | г. Новосибирск, Новосибирская обл., улица Дачная, д. 23/5, кв./оф. 224 | 40802810023400007687 | 30101810600000000774 | 045004774 | **active** | ORG-0009 | **E0** | AT-CORV-ORG-01; **AT-CORV-LE-01** | **partial** — E0 requisites enriched (addresses + banking); bank name, tax system, registration authority, signatory contacts **SAFE UNKNOWN** |

**Note:** LE-0001..0005 attested in prior waves. LE-0006 minted for Corvonero at org intake **2026-06-21** (**AT-CORV-ORG-01**); requisites enriched **2026-06-29** (**AT-CORV-LE-01**, **EV-CORV-OP-REQ-01**). Canonical LE roster: [ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-REGISTER-v1.md).

---

## 4. Alias register

| org_id | alias | alias_kind | evidence_ref | lifecycle_state |
|--------|-------|------------|--------------|-----------------|
| ORG-0009 | **Корво Неро** | trade / RU display | EV-CORVONERO-OP-01 | **active** |
| ORG-0009 | **Corvo Nero** | trade / EN display | EV-CORVONERO-OP-01 | **active** |
| ORG-0009 | **corvonero** | intake slug | EV-CORVONERO-OP-01 | **active** |
| ORG-0009 | ИП Никифоров Роман Вадимович | legal *(via LE-0006)* | EV-CORVONERO-OP-01 | **active** |

---

## 5. Duplicate review register

| review_id | pair | verdict | blocking |
|-----------|------|---------|----------|
| CORV-ORG-D-01 | vs ORG-0001..0008 | **Distinct** | No |
| CORV-ORG-D-02 | INN 540200831636 vs attested roster | **No collision** | No |
| CORV-ORG-D-03 | OGRNIP 324547600100482 vs attested roster | **No collision** | No |
| CORV-ORG-D-04 | vs ORG-0003 i-SEO | **Distinct** — vendor ≠ client | No |
| CORV-ORG-D-05 | vs ORG-0007 Makita | **Distinct** | No |
| CORV-ORG-D-06 | «Makita» LE-0006 candidate slot | **Resolved** — LE-0006 assigned to Corvonero IP | No |

**Duplicate review summary:** **Pass**

---

## 6. SAFE UNKNOWN index

| id | topic | blocks_attestation |
|----|-------|-------------------|
| SU-CORV-ORG-01 | Counterparty Card files | **No** — Category B |
| SU-CORV-ORG-02 | EDO | **No** |
| SU-CORV-ORG-03 | Legal signatory Person | **No** |
| SU-CORV-ORG-04 | primary_contact_person_id | **No** |
| SU-CORV-ORG-05 | Domain registrant | **No** — Wave 5 |
| SU-CORV-ORG-06 | Website / Tilda account owner | **No** |
| SU-CORV-ORG-07 | НДС posture | **No** |
| SU-CORV-ORG-08 | E2 registry extract corroboration | **No** — E0 sufficient for intake path |

---

## 7. Explicit exclusions

| Item | Status |
|------|--------|
| ORG-0009 → ORG-0001 **CLIENT_OF** | **Not created** — operator restriction |
| CRM / contracts / finance entities | **Excluded** |
| PER-* mint for client contacts | **Excluded** |
| Runtime claims | **Excluded** |

---

## 8. Evidence index

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-CORVONERO-OP-01** | [CORVONERO-BUSINESS-INTAKE-v1.md](../../../workspaces/corvonero-yandex-direct/CORVONERO-BUSINESS-INTAKE-v1.md) | **E0** | Identity, INN, OGRNIP, geography, commercial context, i-SEO client |
| **EV-CORVONERO-OP-02** | Operator statement — Tilda site `http://lk.corvonero.ru/` | **E0** | Website candidate corroboration |

**CC storage path (not verified):** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\corvonero\` — **SAFE UNKNOWN**

---

*ATLAS Corvonero Organization Register v1 — ORG-0009 **active**; LE-0006 **active** (E0 requisites-enriched partial; AT-CORV-LE-01).*
