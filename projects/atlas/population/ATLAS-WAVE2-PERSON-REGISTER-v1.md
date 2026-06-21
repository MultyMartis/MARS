# ATLAS Wave 2 Person Register v1

**Status:** **documented** — canonical Person contact roster supplement (Wave 2 attested persons).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07 · **sync:** 2026-06-07 (MNT-PER-0011-01)  
**Parent:** [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md)  
**Companion:** [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) *(ZPM tranche — separate roster)*  
**Is not:** attested registry export, runtime, database table, full Person roster (all fields).

**Scope note:** Full Person population fields remain in [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) and attestation packages. This register tracks **contact rows** for maintenance and steward lookup. ZPM tranche contacts: [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md).

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Persons with contact rows in this register | **1** *(PER-0011 — others deferred to dataset PersonContacts until dedicated pass)* |
| Contact rows — PER-0011 | **4** |
| Maintenance acts applied | **1** — MNT-PER-0011-01 |

---

## 2. Person roster index *(attested — contact supplement only)*

| person_id | canonical_name | primary_organization | lifecycle_state | contact_register |
|-----------|----------------|---------------------|-----------------|------------------|
| PER-0011 | Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | **active** | §4 — **complete** |

*Remaining Wave 2 attested persons (PER-0001..0013 except ZPM tranche): contacts in [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) PersonContacts sheet — full register pass deferred.*

---

## 3. Maintenance log

| maintenance_id | person_id | date | action | record |
|----------------|-----------|------|--------|--------|
| MNT-PER-0011-01 | PER-0011 | 2026-06-07 | Add email `nik.shvakov@mail.ru` (additional, non-primary) | [ATLAS-PER-0011-CONTACT-UPDATE-v1.md](ATLAS-PER-0011-CONTACT-UPDATE-v1.md) |

---

## 4. Contact register

| contact_id | person_id | channel | value | primary | evidence_ref | attestation_state | notes |
|------------|-----------|---------|-------|---------|--------------|-------------------|-------|
| CNT-0024 | PER-0011 | telegram | @niki1man | **yes** | PersonContacts; EV-0004 | **active** | |
| CNT-0025 | PER-0011 | email | nikel007i33@yandex.ru | **yes** | PersonContacts; EV-0004 | **active** | Primary email — preserved |
| CNT-0026 | PER-0011 | phone | +79523014663 | **yes** | PersonContacts; EV-0004 | **active** | |
| CNT-0031 | PER-0011 | email | nik.shvakov@mail.ru | **no** | EV-MNT-PER-0011-01 | **active** | MNT-PER-0011-01 — additional only |

---

## 5. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-PER-0011-CONTACT-UPDATE-v1.md](ATLAS-PER-0011-CONTACT-UPDATE-v1.md) | Maintenance act MNT-PER-0011-01 |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Person attestation index |
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | REL-0006 OWNER edge |

---

*ATLAS Wave 2 Person Register v1 — contact supplement; documentation only.*
