# ATLAS Wave 1B BZPM Organization Register v1

**Status:** **documented** — canonical Organization roster for Wave 1B BZPM tranche (**active**; canonical renamed **ЗПМ** 2026-06-07).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06 *(population)* · **2026-06-07** *(register sync post-rename + ZPM documentation sync)*  
**Parent:** [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md)  
**Is not:** LegalEntities attested export, runtime registry, database table.

---

## 1. Purpose

Канонический **реестр Organization population** Wave 1B — tranche **BZPM / ЗПМ**. Одна строка — одна approved Organization record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Wave tier W1-B | **1** |
| Lifecycle **active** | **1** |
| Legal entity **active** | **1** (LE-0004) |
| Attestation | **Complete** — AT-W1B-01; rename RN-W1B-01 |

---

## 2. Population roster — full table

| org_id | canonical_name | wave_tier | business_role | legal_entity_id | legal_entity_name | inn | kpp | ogrn_ogrnip | aliases | primary_contact_person_id | primary_website | primary_domain | evidence_tier | lifecycle_state | attestation | notes |
|--------|----------------|-----------|---------------|-----------------|-------------------|-----|-----|-------------|---------|---------------------------|-----------------|----------------|---------------|-----------------|-------------|-------|
| ORG-0005 | **ЗПМ** | **W1-B** | **CLIENT** | **LE-0004** | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | 2221237587 | 222101001 | 1172225049787 | BZPM; Завод Пищевого Машиностроения; ООО ЗПМ; ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | **PER-0014** *(Wave 2B)* | **Bzpm.ru** *(CC §17)* | DOM-ZPM-01 *(active)* | **E1** *(CC)* | **active** | AT-W1B-01; RN-W1B-01 | Renamed from BZPM 2026-06-07; distinct from ORG-0006 SIBCAR |

---

## 3. Legal entity index

| legal_entity_id | legal_entity_name | entity_type | inn | kpp | ogrn_ogrnip | lifecycle | org_binding | attestation_readiness |
|-----------------|-------------------|-------------|-----|-----|-------------|-----------|-------------|----------------------|
| LE-0004 | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | ООО | 2221237587 | 222101001 | 1172225049787 | **active** | ORG-0005 | **complete** |

**Note:** LE-0001..0003 attested in Wave 1 dataset. LE-0004 attested AT-W1B-01. LE-0005 reserved for SIBCAR (ORG-0006).

---

## 4. Alias register (active)

| org_id | alias | alias_role | evidence_ref | attestation_state |
|--------|-------|------------|--------------|-------------------|
| ORG-0005 | **BZPM** | **former** *(prior canonical)* / abbreviation / domain stem | EV-W1B-CC-01 §17; AT-W1B-01; RN-W1B-01 | **active** |
| ORG-0005 | **Завод Пищевого Машиностроения** | trade / RU display | EV-W1B-CC-01 §1–§2 | **active** |
| ORG-0005 | **ООО ЗПМ** | legal / abbreviation | EV-W1B-CC-01 §1–§2; RN-W1B-01 | **active** |
| ORG-0005 | **ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»** | legal | EV-W1B-CC-01 §1–§2 | **active** |

**Revoked (COR-W1B-01 — not restored):** Автосалон СИБКАР, SIBCAR, СИБКАР.

**Primary contact (Wave 2B attestation):** `primary_contact_person_id` = **PER-0014** — attested at [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) §4; basis REL-ZPM-02 primary operational contact.

---

## 5. Cross-reference index (informational — not Wave 1B edges)

| Related artifact | Entity class | Relationship to ORG-0005 | Wave |
|------------------|--------------|----------------------------|------|
| SITE-001 | OCPilot site_id | Engagement context only — not org identity | OCPilot / future Project |
| `sibcar.new-site.space` | Website hostname candidate | Future WEB-* — not ORG-0005 proof | Wave 4 |
| ORG-0006 SIBCAR | Organization | **Distinct** legal subject | Wave 1C |
| ORG-0001 Полигон | Organization | Future **CLIENT_OF** vendor (ORG-0005 → ORG-0001) | Wave 6+ |
| ORG-0004 Триумф | Organization | Separate W1-B client — no merge | Wave 1 |

---

## 6. Evidence index

| Ref | Artifact | Role |
|-----|----------|------|
| EV-W1B-CC-01 | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | **Primary Counterparty Card** |
| EV-W1B-04 | [EAR-CONNECTED-ACQUISITION-v1.md](../../../shared/external-access-runtime/EAR-CONNECTED-ACQUISITION-v1.md) | Operator BZPM codename corroboration *(alias only)* |
| EV-W1B-05 | [EAR-ACQUISITION-TRACKS-v1.md](../../../shared/external-access-runtime/EAR-ACQUISITION-TRACKS-v1.md) | Recurring support context *(alias only)* |

---

## 7. Duplicate review register

| review_id | signal | outcome | blocking |
|-----------|--------|---------|----------|
| W1B-D-01 | BZPM / ЗПМ vs SIBCAR | **Distinct** | No |
| W1B-D-02 | vs ORG-0004 Triumph | **Distinct** | No |
| W1B-D-03 | vs operator orgs | **Distinct** | No |
| W1B-D-04 | SITE-001 class boundary | **Pass** | No |
| W1B-D-05 | Dealership homonym | **Open — low** | No |
| W1B-D-06 | D1 unresolved | **None** | No |
| W1C-D-01 | SIBCAR vs BZPM/ЗПМ | **Distinct** | No |

---

## 8. Readiness summary

| org_id | population | duplicate review | attestation (active) | rename | wave 2B person deps |
|--------|------------|------------------|----------------------|--------|---------------------|
| ORG-0005 | **Complete** | **Pass** | **Complete** — AT-W1B-01 | **Complete** — RN-W1B-01 | **Unblocked** *(org endpoint active)* |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) | Canonical rename act + identity history |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | Active attestation (historical BZPM canonical) |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | COR-W1B-01..06 |
| [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) | Point-in-time registry snapshot |

---

*ATLAS Wave 1B BZPM Organization Register v1 — documentation only.*
