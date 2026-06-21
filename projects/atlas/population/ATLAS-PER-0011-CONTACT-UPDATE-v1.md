# ATLAS PER-0011 Contact Update v1

**Status:** **documented** — Person contact maintenance (population layer).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Trigger:** Steward directive — add additional email for PER-0011 without replacing existing contacts.  
**Parent:** [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) · [ATLAS-WAVE2-PERSON-REGISTER-v1.md](ATLAS-WAVE2-PERSON-REGISTER-v1.md)  
**Is not:** Person attestation re-execution, relationship change, Foundation change, runtime registry write.

---

## 1. Maintenance act

| Field | Value |
|-------|-------|
| **person_id** | PER-0011 *(unchanged)* |
| **canonical_name** | Шваков Никита Алексеевич *(unchanged)* |
| **primary_organization** | ORG-0003 i-SEO Studio *(unchanged)* |
| **lifecycle_state** | **active** *(unchanged)* |
| **maintenance_id** | **MNT-PER-0011-01** |

**Action:** Register **additional** email contact — do **not** replace or demote existing contacts.

| New contact | Value | primary | evidence |
|-------------|-------|---------|----------|
| email | `nik.shvakov@mail.ru` | **no** | **E0** EV-MNT-PER-0011-01 |

---

## 2. Fields explicitly unchanged

| Item | Status |
|------|--------|
| Person identity (PER-0011) | **Unchanged** — no new Person minted |
| Existing email `nikel007i33@yandex.ru` (CNT-0025) | **Unchanged** — remains **primary** |
| Existing telegram `@niki1man` (CNT-0024) | **Unchanged** |
| Existing phone `+79523014663` (CNT-0026) | **Unchanged** |
| REL-0006 PER-0011 **OWNER** → ORG-0003 | **Unchanged** |
| Document signatory LE-0002 ИП Шваков Н. А. | **Unchanged** |
| Evidence tier (Person) | **E1** — EV-0004 *(unchanged)* |

---

## 3. Contact register (post-update)

Source baseline: [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) PersonContacts sheet; CC phone from EV-0004.

| contact_id | person_id | channel | value | primary | evidence_ref | attestation_state | notes |
|------------|-----------|---------|-------|---------|--------------|-------------------|-------|
| CNT-0024 | PER-0011 | telegram | @niki1man | **yes** | PersonContacts / EV-0004 | **active** | Prior |
| CNT-0025 | PER-0011 | email | nikel007i33@yandex.ru | **yes** | PersonContacts / EV-0004 | **active** | Prior — **not replaced** |
| CNT-0026 | PER-0011 | phone | +79523014663 | **yes** | PersonContacts / EV-0004 | **active** | Prior |
| **CNT-0031** | PER-0011 | email | **nik.shvakov@mail.ru** | **no** | **EV-MNT-PER-0011-01** | **active** | **Added MNT-PER-0011-01** |

**Informational (CC / requisites — not Person contact row):**

| Field | Value | evidence_ref |
|-------|-------|--------------|
| CC phone (requisites) | 8 (999) 879-10-83 | EV-0004 `i-seo/requisites.txt` |

**Rule:** `@mail.ru` domain — contact pointer only; not org identity proof (EFV-01 analog for Person contacts).

---

## 4. Evidence index

| Ref | Artifact | Role |
|-----|----------|------|
| EV-0004 | `i-seo/requisites.txt` | Prior Person attestation; signatory; CC phone |
| EV-MNT-PER-0011-01 | Steward maintenance directive (2026-06-07) | Additional email `nik.shvakov@mail.ru` |
| PersonContacts sheet | ATLAS-WAVE1-DATASET-v0.4.xlsx | Prior CNT-0024..0026 |

---

## 5. Relationship preservation

| relationship_id | edge | status |
|-----------------|------|--------|
| REL-0006 | PER-0011 **OWNER** → ORG-0003 i-SEO Studio | **active** — **unchanged** |

No Wave 2B re-attestation required — contact maintenance only.

---

## 6. Register sync

| Register | Update |
|----------|--------|
| [ATLAS-WAVE2-PERSON-REGISTER-v1.md](ATLAS-WAVE2-PERSON-REGISTER-v1.md) | §4 Contact register — CNT-0031 added |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | **No change** — Person attestation basis unchanged |

---

*ATLAS PER-0011 Contact Update v1 — maintenance only.*
