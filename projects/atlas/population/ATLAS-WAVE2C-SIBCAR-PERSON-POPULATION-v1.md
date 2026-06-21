# ATLAS Wave 2C SIBCAR Person Population v1

**Status:** **documented** — Wave 2C SIBCAR canonical Person population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) · [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, attested registry export, Wave 2C relationship edges.

**Organization anchor:** ORG-0006 **SIBCAR** — lifecycle **active** (AT-W1C-01).

**Operator inputs (binding for this tranche):**

- Primary Counterparty Card: **EV-W1C-CC-01** (`sibcar/Реквизиты.docx`)
- Operator-confirmed Person B identity, role, and Telegram contact (this mission)
- Business reality: two-person model — CC signatory Карандашов; operational contact Хаял; **Diadoc signer — SAFE UNKNOWN**

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Person** для Wave 2C tranche **SIBCAR** (ORG-0006): состав, классификация, evidence basis, зависимости Wave 2C relationship pass, границы foundation.

**Normative scope Wave 2C SIBCAR Person:**

```text
Person entity intake + attestation plan (2 records)
Wave 2C relationship pass (отдельный пакет): Person ↔ Organization — только после Person + ORG endpoints active
```

**Explicit exclusions (this package):**

- Person → Organization relationships — **not created** (Wave 2C relationship pass)
- Project / Website / Domain / Commercial Relationship entities — **excluded**

---

## 2. Evidence pre-check (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01..03 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04..06.

**Folder (prior inventory — AT-W1C-01):** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\`

| # | Filename | Format | Role |
|---|----------|--------|------|
| 1 | `Реквизиты.docx` | DOCX | **Primary Counterparty Card** → **EV-W1C-CC-01** |

**Inventory verdict:** **Pass** — CC present; prior ME-W1C-01 cleared. Person intake **reuses** org CC inventory; no new CC file required for this tranche.

**CC person lines extracted (EV-W1C-CC-01):**

| Person signal | CC section | In CC |
|---------------|------------|-------|
| Карандашов Максим Петрович — Руководитель | §21–§22 | **Yes** |
| Карандашов Максим Петрович — Главный бухгалтер | §23–§24 | **Yes** |
| Exact должность string (director title) | §21 | **No** — «Руководитель (должность, ФИО)» without explicit title |
| Хаял | — | **No** |
| Telegram @Khayal8888 | — | **No** |
| Phone / email for either person | — | **No** |

---

## 3. Population roster (canonical)

Draft-id — **не** canonical registry id до attestation.

### 3.1 Summary table

| Draft ID | Canonical name | Aliases | Target org *(2C rel only)* | Population slice | Operational contact | Document signatory | Evidence (Person) | Attestation readiness |
|----------|----------------|---------|----------------------------|------------------|---------------------|--------------------|-------------------|----------------------|
| PER-0016 | Карандашов Максим Петрович | — | ORG-0006 SIBCAR | **client-side** | **no** — signatory role; operational contact is PER-0017 | **yes** — LE-0005 §22 | **E1** CC | **ready (E1)** |
| PER-0017 | Хаял | — | ORG-0006 SIBCAR | **client-side** | **yes** — primary operational contact | **no** | **E0** operator + TG | **ready (E0)** |

**Population slice** — intake classification; not a new entity type.  
**Operational contact** — operator role signal; not OPS Contact entity.

---

## 4. Per-person analysis

### 4.1 PER-0016 — Карандашов Максим Петрович

| Field | Value |
|-------|-------|
| **Canonical name** | Карандашов Максим Петрович |
| **Aliases** | — |
| **Primary organization** | ORG-0006 SIBCAR *(relationship deferred — Wave 2C relationship pass)* |
| **Population slice** | **client-side** |
| **Role (operator)** | General Director |
| **Role (CC)** | Руководитель — EV-W1C-CC-01 §21–§22; Главный бухгалтер §23–§24 |
| **Operational contact** | **no** — PER-0017 is primary operational contact |
| **Document signatory** | **yes** — LE-0005 `document_signatory` (CC §22); chief accountant same subject §23–§24 |
| **Contacts** | phone / TG / email: **SAFE UNKNOWN** |
| **Evidence level** | **E1** — identity, signatory, chief accountant from EV-W1C-CC-01 |
| **Population priority** | **W2C-SIBCAR-P0** — CC signatory first (legal anchor) |
| **Expected relationship family (Wave 2C — queue only)** | **GENERAL_DIRECTOR** → ORG-0006 *(analog REL-ZPM-01)* |
| **Attestation readiness** | **Ready** at **E1** — CC line match |
| **Title note** | Operator «General Director» vs CC «Руководитель» — CC omits exact должность; operator title recorded as role signal only |

### 4.2 PER-0017 — Хаял

| Field | Value |
|-------|-------|
| **Canonical name** | Хаял |
| **Aliases** | — |
| **Full patronymic / surname** | **SAFE UNKNOWN** |
| **Primary organization** | ORG-0006 SIBCAR *(relationship deferred — Wave 2C relationship pass)* |
| **Population slice** | **client-side** |
| **Role signals (operator)** | Primary Operational Contact; Business Owner *(operator statement — not OWNER edge)* |
| **Operational contact** | **yes** — primary operational contact for Polygon vendor work on SIBCAR account |
| **Document signatory** | **no** — CC names only Карандашов |
| **Contacts (operator-confirmed)** | Telegram `@Khayal8888` |
| **Contacts not otherwise evidenced** | **SAFE UNKNOWN** — phone, email, other channels |
| **Evidence level** | **E0** — operator-direct identity (given name), role signals, Telegram; **not** named in EV-W1C-CC-01 |
| **CC corroboration** | **None** — person absent from CC person block |
| **Population priority** | **W2C-SIBCAR-P1** — primary operational contact |
| **Expected relationship family (Wave 2C — queue only)** | **REPRESENTATIVE** → ORG-0006 *(analog REL-ZPM-02)* |
| **Attestation readiness** | **Ready** at **E0** — operator-known external contact pattern (analog PER-0014 ZPM) |
| **Constraints** | Do **not** mint **OWNER** edge from «Business Owner» statement; do **not** infer Diadoc signer |

---

## 5. Business reality notes (operator-confirmed)

| Topic | Record |
|-------|--------|
| Person model | **Two-person** — CC signatory Карандашов (PER-0016); operational contact Хаял (PER-0017) |
| Work acceptance / communication | Primary: **Хаял** via Telegram `@Khayal8888` |
| Contracts and acts | **SAFE UNKNOWN** — EDO usage not stated for SIBCAR in this mission |
| Diadoc signer | **SAFE UNKNOWN** — do not infer; do not invent |
| ORG-0006 primary_contact_person_id | **Deferred** — populate at Wave 2C relationship attestation *(PER-0017 — steward confirms at relationship pass)* |
| «Business Owner» (PER-0017) | Operator role signal only — **no** OWNER relationship per ZPM precedent |

---

## 6. Relationship analysis (Wave 2C candidates — not created)

**Scope boundary:** Wave 2C Person only. Relationships belong to **Wave 2C SIBCAR relationship pass**. No REL-* rows minted in this package.

| Candidate rel_id | source_person | target_organization | relationship_type | attestation_basis | readiness *(2C rel)* |
|------------------|---------------|---------------------|-------------------|-------------------|----------------------|
| REL-SIBCAR-01 | PER-0016 Карандашов Максим Петрович | ORG-0006 SIBCAR | **GENERAL_DIRECTOR** | E1 EV-W1C-CC-01 §21–§24; LE-0005 signatory | **ready** after PER-0016 **active** |
| REL-SIBCAR-02 | PER-0017 Хаял | ORG-0006 SIBCAR | **REPRESENTATIVE** | E0 EV-W2C-SIBCAR-OP-01; primary operational contact | **ready** after PER-0017 **active** |

**Prerequisite (W2C-R01):** ORG-0006 **active** ✓; both Person records **active** after Wave 2C SIBCAR Person attestation.

---

## 7. Duplicate and homonym review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **W2C-SIBCAR-D-01** | Карандашов vs Wave 2 roster PER-0001..0015 | **Distinct** — not in prior Wave 2 set | No |
| **W2C-SIBCAR-D-02** | Хаял vs Wave 2 roster PER-0001..0015 | **Distinct** | No |
| **W2C-SIBCAR-D-03** | Карандашов vs LE-0005 signatory field | **Same subject** — intended bind PER-0016 ↔ LE-0005 signatory | No |
| **W2C-SIBCAR-D-04** | Хаял vs CC signatory Карандашов | **Distinct persons** — CC names only Карандашов | No |
| **W2C-SIBCAR-D-05** | PER-0017 given name only vs W2-E-03 | **Pass** — name + Telegram channel; not email-only mint | No |
| **W2C-SIBCAR-D-06** | info_sibcar@mail.ru vs Person contacts | **No merge** — org email §16; not Person identity proof | No |

---

## 8. Foundation consistency

| Foundation doc | Wave 2C SIBCAR alignment |
|----------------|--------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §2 Person | Two PER records; org link via future Relationship — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Full patronymic PER-0016 CC-backed; PER-0017 given name only — **yes** with SAFE UNKNOWN note |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) | No aliases proposed — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | E0/E1 tiers assigned; no auto-promote |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.2 Person | E0 operator-known + E1 CC signatory paths — **yes** |
| EFV-04 / CPV-01 | CC read before person conclusions; CC overrides org assumptions — **honored** |

**No new entity types.** No Person ↔ Person edges.

---

## 9. Discovery register resolution

| Discovery OQ | Prior state | Resolution (this mission) |
|--------------|-------------|---------------------------|
| OQ-W2C-01 | Single vs two-person model | **Two-person** — PER-0016 + PER-0017 |
| OQ-W2C-04 | PER-0016 assignment | **Confirmed** — PER-0016 for Карандашов |
| OQ-W2C-09 | Second E0 person | **Yes** — PER-0017 Хаял |
| OQ-W2C-10 | Second person identity | **Partial** — given name Хаял; patronymic **SAFE UNKNOWN** |
| OQ-W2C-14 | Model selection | **ZPM two-person parity** |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) | Proposed Person register rows |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | EV-W1C-CC-01 extraction |
| [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) | Parity template |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 2C SIBCAR Person Population v1 — documentation only.*
