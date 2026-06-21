# ATLAS Wave 2 ZPM Person Population v1

**Status:** **documented** — Wave 2 ZPM canonical Person population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, attested registry export, Wave 2B relationship edges.

**Organization anchor:** ORG-0005 **ЗПМ** — lifecycle **active** (AT-W1B-01; rename RN-W1B-01).

**Operator inputs (binding for this tranche):**

- Primary Counterparty Card: **EV-W1B-CC-01** (`bzpm/Реквизиты.docx`)
- Operator-confirmed contacts and operational statements (this mission)
- Business reality: work acceptance via Дубинский; sometimes via Крюков; org uses EDO; **Diadoc signer — SAFE UNKNOWN**

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Person** для Wave 2 tranche **ZPM** (ORG-0005): состав, классификация, evidence basis, зависимости Wave 2B, границы foundation.

**Normative scope Wave 2 ZPM:**

```text
Person entity intake + attestation plan (2 records)
Wave 2B-ZPM (отдельный пакет): Person ↔ Organization — только после Person + ORG endpoints active
```

**Explicit exclusions (this package):**

- Person → Organization relationships — **not created** (Wave 2B-ZPM)
- Project / Website / Domain / Commercial Relationship entities — **excluded**

---

## 2. Evidence pre-check (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01..03 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04..06.

**Folder (prior inventory — AT-W1B-01):** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\`

| # | Filename | Format | Role |
|---|----------|--------|------|
| 1 | `Реквизиты.docx` | DOCX | **Primary Counterparty Card** → **EV-W1B-CC-01** |

**Inventory verdict:** **Pass** — CC present; prior ME-W1B-01 cleared. Person intake **reuses** org CC inventory; no new CC file required for this tranche.

**CC person lines extracted (EV-W1B-CC-01):**

| Person signal | CC section | In CC |
|---------------|------------|-------|
| Крюков Александр Сергеевич — Директор | §19, §24 | **Yes** |
| Крюков Александр Сергеевич — beneficial owner 100% | §20 | **Yes** |
| Крюков Александр Сергеевич — chief accountant / responsible | §21–§22 | **Yes** |
| Алексей Владимирович Дубинский | — | **No** |
| Mobile +79039573236 | — | **No** |
| Telegram / personal email for either person | — | **No** |

---

## 3. Population roster (canonical)

Draft-id — **не** canonical registry id до attestation.

### 3.1 Summary table

| Draft ID | Canonical name | Aliases | Target org *(2B only)* | Population slice | Operational contact | Document signatory | Evidence (Person) | Attestation readiness |
|----------|----------------|---------|--------------------------|-------------------|---------------------|--------------------|-------------------|----------------------|
| PER-0014 | Алексей Владимирович Дубинский | Алексей Дубинский; Дубинский | ORG-0005 ЗПМ | **client-side** | **yes** — primary for Polygon vendor work | **no** *(Diadoc signer UNKNOWN)* | **E0** operator + contacts | **ready (E0)** |
| PER-0015 | Крюков Александр Сергеевич | — | ORG-0005 ЗПМ | **client-side** | **sometimes** — work acceptance | **yes** — LE-0004 CC signatory | **E1** CC + E0 phone | **ready (E1)** |

**Population slice** — intake classification; not a new entity type.  
**Operational contact** — operator role signal; not OPS Contact entity.

---

## 4. Per-person analysis

### 4.1 PER-0014 — Алексей Владимирович Дубинский

| Field | Value |
|-------|-------|
| **Canonical name** | Алексей Владимирович Дубинский |
| **Aliases** | Алексей Дубинский; Дубинский |
| **Primary organization** | ORG-0005 ЗПМ *(relationship deferred — Wave 2B)* |
| **Population slice** | **client-side** |
| **Role signals (operator)** | заместитель директора; исполнительный директор; технический директор |
| **Operational contact** | **yes** — primary operational contact for Polygon vendor work on ЗПМ account |
| **Operator statement** | «Всю работу веду через него. Все вопросы решаются через него.» |
| **Document signatory** | **no** — org uses EDO; specific Diadoc signer **SAFE UNKNOWN** |
| **Contacts (operator-confirmed)** | Telegram `@scrash86`; phone `+7 913 099 0747`; email `dav@assum.ru` |
| **Evidence level** | **E0** — operator-direct identity, role signals, contacts; **not** named in EV-W1B-CC-01 |
| **CC corroboration** | **None** — person absent from CC person block |
| **Population priority** | **W2-ZPM-P1** — primary operational contact |
| **Expected relationship family (Wave 2B — queue only)** | **REPRESENTATIVE** → ORG-0005 *(review: EMPLOYEE vs REPRESENTATIVE given role signals)* |
| **Attestation readiness** | **Ready** at **E0** — operator-known external contact pattern (analog: Triumph operator contacts) |
| **Constraints** | Do **not** infer Diadoc signer; do **not** mint alias from email domain `assum.ru` |

### 4.2 PER-0015 — Крюков Александр Сергеевич

| Field | Value |
|-------|-------|
| **Canonical name** | Крюков Александр Сергеевич |
| **Aliases** | — |
| **Primary organization** | ORG-0005 ЗПМ *(relationship deferred — Wave 2B)* |
| **Population slice** | **client-side** |
| **Role (operator)** | Генеральный директор |
| **Role (CC)** | Директор — EV-W1B-CC-01 §19, §24 |
| **Operational contact** | **sometimes** — work acceptance alongside PER-0014 |
| **Document signatory** | **yes** — LE-0004 `document_signatory` (CC §19–§24); beneficial owner 100% (§20) |
| **Contacts (operator-confirmed)** | Phone `+79039573236` |
| **Contacts not otherwise evidenced** | **SAFE UNKNOWN** — email, Telegram, other channels |
| **Evidence level** | **E1** — identity and director/signatory from EV-W1B-CC-01; phone **E0** operator |
| **Population priority** | **W2-ZPM-P0** — CC signatory first (legal anchor) |
| **Expected relationship family (Wave 2B — queue only)** | **GENERAL_DIRECTOR** → ORG-0005 *(CC signatory + 100% beneficial owner; analog PER-0006 Triumph)* |
| **Attestation readiness** | **Ready** at **E1** — CC line match |
| **Title note** | Operator «Генеральный директор» vs CC «Директор» — CC controls legal signatory field; operator title recorded as role signal only |

---

## 5. Business reality notes (operator-confirmed)

| Topic | Record |
|-------|--------|
| Work acceptance | Primary: **Алексей Дубинский**; secondary: **Крюков Александр Сергеевич** (sometimes) |
| Contracts and acts | Organization uses **EDO** |
| Diadoc signer | **SAFE UNKNOWN** — do not infer; do not invent |
| ORG-0005 primary_contact_person_id | **Deferred** — populate at Wave 2B after Person **active** *(likely PER-0014 operational; steward confirms at 2B)* |

---

## 6. Relationship analysis (Wave 2B candidates — not created)

**Scope boundary:** Wave 2 only. Relationships belong to **Wave 2B-ZPM**. No REL-* rows minted in this package.

| Candidate rel_id | source_person | target_organization | relationship_type *(review)* | attestation_basis | readiness *(2B)* |
|------------------|---------------|---------------------|-------------------------------|-------------------|------------------|
| REL-ZPM-01 *(draft)* | PER-0015 Крюков Александр Сергеевич | ORG-0005 ЗПМ | **GENERAL_DIRECTOR** | E1 EV-W1B-CC-01 §19–§24; LE-0004 signatory | **ready** after PER-0015 **active** |
| REL-ZPM-02 *(draft)* | PER-0014 Алексей Владимирович Дубинский | ORG-0005 ЗПМ | **REPRESENTATIVE** *(EMPLOYEE review)* | E0 operator operational contact; role signals | **ready** after PER-0014 **active** |

**Prerequisite (W2B-R01):** ORG-0005 **active** ✓; both Person records **active** after Wave 2 ZPM attestation.

---

## 7. Duplicate and homonym review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **W2-ZPM-D-01** | Крюков vs Wave 2 roster PER-0001..0013 | **Distinct** — not in prior Wave 2 set | No |
| **W2-ZPM-D-02** | Дубинский vs Wave 2 roster PER-0001..0013 | **Distinct** | No |
| **W2-ZPM-D-03** | Крюков vs LE-0004 signatory field | **Same subject** — intended bind PER-0015 ↔ LE-0004 signatory | No |
| **W2-ZPM-D-04** | Дубинский vs CC signatory Крюков | **Distinct persons** — CC names only Крюков | No |
| **W2-ZPM-D-05** | Email `dav@assum.ru` vs org CC email `zakaz@bzmp.ru` | **No merge** — contact pointer only; EFV-01 | No |

---

## 8. Foundation consistency

| Foundation doc | Wave 2 ZPM alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §2 Person | Two PER records; org link via future Relationship — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Full patronymic for PER-0014 operator-provided; PER-0015 CC-backed — **yes** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) | Short-name aliases for PER-0014 — steward review at intake |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | E0/E1 tiers assigned; no auto-promote |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.2 Person | E0 operator-known + E1 CC signatory paths — **yes** |
| EFV-04 / CPV-01 | CC read before person conclusions; CC overrides org assumptions — **honored** |

**No new entity types.** No Person ↔ Person edges.

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Proposed Person register rows |
| [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | EV-W1B-CC-01 extraction |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 2 ZPM Person Population v1 — documentation only.*
