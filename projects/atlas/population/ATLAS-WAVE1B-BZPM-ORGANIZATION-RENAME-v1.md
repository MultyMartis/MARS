# ATLAS Wave 1B BZPM Organization Rename v1

**Status:** **documented** — binding canonical name change (population layer).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Trigger:** Operator directive — align Organization canonical display with CC-backed abbreviation **ЗПМ** before further population work.  
**Parent:** [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) · [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md)  
**Is not:** attestation re-execution, LE amendment, Foundation change, runtime registry write.

---

## 1. Rename act

| Field | Prior (attested 2026-06-06) | Current (2026-06-07) |
|-------|----------------------------|----------------------|
| **org_id** | ORG-0005 | ORG-0005 *(unchanged)* |
| **canonical_name** | BZPM | **ЗПМ** |
| **lifecycle_state** | **active** | **active** *(unchanged)* |
| **wave_tier** | W1-B | W1-B *(unchanged)* |
| **business_role** | CLIENT | CLIENT *(unchanged)* |

**Governance:** [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) IDP-04 (names drift; ids do not) · IDP-06 (history preserved) · §7.2 `active → (rename) → active`.

---

## 2. Fields explicitly unchanged

Per operator requirement — **no modification** to legal entity layer or tax identifiers:

| Entity | Field | Value | Status |
|--------|-------|-------|--------|
| **LE-0004** | legal_entity_id | LE-0004 | **Unchanged** |
| **LE-0004** | legal_entity_name | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | **Unchanged** |
| **LE-0004** | inn | 2221237587 | **Unchanged** |
| **LE-0004** | kpp | 222101001 | **Unchanged** |
| **LE-0004** | ogrn_ogrnip | 1172225049787 | **Unchanged** |
| **LE-0004** | lifecycle_state | **active** | **Unchanged** |
| **ORG-0005** | legal_entity_id binding | LE-0004 | **Unchanged** |

**Evidence basis:** EV-W1B-CC-01 — attested in [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) §2, §7.1.

---

## 3. Identity history (preserved)

| Date | Event | canonical_name | Record |
|------|-------|----------------|--------|
| 2026-06-06 | Wave 1B population proposed | BZPM | [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) |
| 2026-06-06 | Identity correction (COR-W1B-01..06) | BZPM | [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) |
| 2026-06-06 | Active attestation AT-W1B-01 | **BZPM** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) §7.2 |
| 2026-06-07 | Canonical rename RN-W1B-01 | **ЗПМ** | **This document** |

**Rule:** Prior attestation act §7.2 remains **historical truth** for 2026-06-06. Current canonical name is **ЗПМ** per this rename act and updated register.

---

## 4. Alias register (post-rename)

Per [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §2.4 — prior canonical **BZPM** retained as **`former`** alias for searchability and audit trail.

| org_id | alias | alias_role | evidence_ref | state |
|--------|-------|------------|--------------|-------|
| ORG-0005 | **BZPM** | **former** *(prior canonical)* + abbreviation / domain stem | EV-W1B-CC-01 §17 (Bzpm.ru); AT-W1B-01 | **active** |
| ORG-0005 | **Завод Пищевого Машиностроения** | trade / RU display fragment | EV-W1B-CC-01 §1–§2 | **active** |
| ORG-0005 | **ООО ЗПМ** | legal / abbreviation | EV-W1B-CC-01 §1–§2; operator rename directive | **active** |
| ORG-0005 | **ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»** | legal | EV-W1B-CC-01 §1–§2 | **active** |

**Searchability:** **BZPM** remains a valid lookup key via alias index — resolves to ORG-0005 **ЗПМ**.

**Revoked aliases (unchanged from COR-W1B-01):** Автосалон СИБКАР, SIBCAR, СИБКАР — **revoked**; not restored by this rename.

---

## 5. Superseded display references

| Prior reference | Disposition |
|-----------------|-------------|
| Register row `canonical_name: BZPM` | **Superseded** — see [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) §2 (updated) |
| Active attestation §7.2 `canonical_name: BZPM` | **Historical** — valid for 2026-06-06 act only |
| ME-W1B-04 «BZPM acronym expansion (ЗПМ)» | **Resolved** — canonical now **ЗПМ** |

---

## 6. Downstream impact

| Area | Impact |
|------|--------|
| Person / Project / Website / Domain for ORG-0005 | **None yet** — no downstream entities attested |
| Relationship edges involving ORG-0005 | **None yet** — Wave 6+ deferred |
| ORG-0006 SIBCAR distinction | **Unchanged** — distinct INN/OGRN |
| Foundation documents | **Not modified** |

---

*ATLAS Wave 1B BZPM Organization Rename v1 — documentation only.*
