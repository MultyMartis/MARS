# ATLAS Wave 2 Person Population v1

**Status:** **documented** — Wave 2 canonical Person population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, automation, database schema, attested registry export.

**Wave 1 prerequisite:** Organizations Wave 1 complete — status **READY FOR WAVE 1 ATTESTATION** (operator, 2026-06-06).

**Operator correction (binding for Wave 2):**

- **MetaCode** принадлежит только **Андрею Русецкому** (OWNER).
- **Сергей Фатюткин** и **Роман Лиматов** — будущие независимые партнёрские контуры; **не** связывать с MetaCode.
- Контуры Sergey / Moscow SERM и Roman / Metallka остаются **изолированными** до отдельной population соответствующих Organization.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Person** для Wave 2: состав, классификация, evidence, зависимости Wave 2B, границы foundation.

**Normative scope Wave 2:**

```text
Person entity intake + attestation plan
Wave 2B (отдельный пакет): Person ↔ Organization — только после active endpoints
```

---

## 2. Population roster (canonical)

Источник: [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) (лист `Persons`, `PersonContacts`, `Organizations`, `LegalEntities`, `Evidence`).  
Draft-id в dataset — **не** canonical registry id до attestation.

### 2.1 Summary table

| Draft ID | Canonical name | Aliases | Primary organization | Population slice | Operational contact | Document signatory | Evidence (Person) | Attestation readiness |
|----------|----------------|---------|----------------------|------------------|---------------------|--------------------|-------------------|----------------------|
| PER-0001 | Русецкий Андрей Анатольевич | Андрей | ORG-0001 Полигон *(multi-hat)* | **internal** | yes (ORG-0001, ORG-0002) | yes (LE-0001) | **E0** + E1 CC | **ready** |
| PER-0002 | Фатюткин Сергей Игоревич | Сергей | **SAFE UNKNOWN** | **partner** (future) | no | no | **E0** | **ready (Person only)** |
| PER-0003 | Лиматов Роман Курбанович | Роман | **SAFE UNKNOWN** | **partner** (future) | no | no | **E0** | **ready (Person only)** |
| PER-0011 | Шваков Никита Алексеевич | Никита | ORG-0003 i-SEO Studio | i-SEO agency | no | yes (LE-0002) | **E1** CC | **ready** |
| PER-0007 | Беслангурова Тамила | Тамила | ORG-0003 i-SEO Studio | i-SEO agency | yes (ORG-0003) | no | **E1** CC + contacts | **ready** |
| PER-0008 | Денис Леонов | Денис | ORG-0003 i-SEO Studio | i-SEO agency | no | no | **E1** CC + contacts | **ready** |
| PER-0010 | Дягилева Ольга *(dataset: Оля Дягилева)* | Оля | ORG-0003 i-SEO Studio | i-SEO agency | no | no | **E1** CC + contacts | **ready** *(alias review)* |
| PER-0012 | Илья Гуренков | Илья | ORG-0003 i-SEO Studio | i-SEO agency | no | no | **E1** CC + contacts | **ready** |
| PER-0013 | Иван Корольков | Ваня | ORG-0003 i-SEO Studio | i-SEO agency | no | no | **E1** CC + contacts | **ready** |
| PER-0009 | Антон Кораблёв | Антон | ORG-0003 i-SEO Studio | i-SEO agency | no | no | **E1** CC + contacts | **ready** |
| PER-0004 | Макарова Алеся Леонидовна | Алеся | ORG-0004 Триумф | **client-side** | yes (ORG-0004) | no | **E1** CC | **proposed → active** |
| PER-0006 | Вагин Иван Владимирович | Иван Вагин | ORG-0004 Триумф | **client-side** | no | yes (LE-0003) | **E1** CC | **proposed → active** |
| PER-0005 | Подзолков Максим | Максим | ORG-0004 Триумф | **client-side** | no | no | **E1** CC + operator | **proposed → active** |

**Population slice** — классификация intake (не новый тип entity).  
**Operational contact** / **document signatory** — операционные роли из CC и dataset; не OPS Contact entity ([ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) W1-EXEC-04).

---

## 3. Per-person analysis

### 3.1 Internal — Андрей Русецкий (PER-0001)

| Field | Value |
|-------|-------|
| **Canonical name** | Русецкий Андрей Анатольевич |
| **Aliases** | Андрей; ignis.martis@mail.ru; @ignismartis *(contact — not alias id)* |
| **Primary organization** | ORG-0001 Веб-студия «Полигон» *(display primary; multi-org via relationships)* |
| **Population slice** | internal — operator / Program Owner context |
| **Operational contact** | Primary for ORG-0001, ORG-0002 |
| **Document signatory** | LE-0001 (ИП Русецкий А. А.) — Polygon, MetaCode |
| **Evidence level** | **E0** operator-direct; corroboration **E1** `polygon/ИП Русецкий А. А.pdf`, `metacode/ИП Русецкий А. А.pdf` |
| **Population priority** | **W2-P0** — anchor person |
| **Expected relationship family (Wave 2B)** | Person ↔ Organization: **OWNER** → ORG-0001; **OWNER** → ORG-0002; **MANAGER** → ORG-0003 |
| **Attestation readiness** | **Ready** — homonym U4 checked (single Andrey in scope) |
| **Constraints** | MetaCode OWNER **only** Andrey; MANAGER i-SEO **not** OWNER |

### 3.2 Partner cluster (future) — Сергей Фатюткин (PER-0002)

| Field | Value |
|-------|-------|
| **Canonical name** | Фатюткин Сергей Игоревич |
| **Aliases** | Сергей; @serg778 |
| **Primary organization** | **SAFE UNKNOWN** — future Moscow SERM contour *(Organization not in Wave 1 dataset)* |
| **Population slice** | partner (future independent cluster) |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E0** operator-direct; contacts E1 informal |
| **Population priority** | **W2-P4** — after core operator + agency + client contacts |
| **Expected relationship family (Wave 2B)** | **Deferred** — no Person ↔ Organization edge until Moscow SERM Organization populated and active |
| **Attestation readiness** | **Ready for Person entity only**; Wave 2B **blocked** (W2-R-02) |
| **Constraints** | **Do NOT** link to ORG-0002 MetaCode; **Do NOT** attest Person ↔ Person edges; **Do NOT** mint Cluster entity |

### 3.3 Partner cluster (future) — Роман Лиматов (PER-0003)

| Field | Value |
|-------|-------|
| **Canonical name** | Лиматов Роман Курбанович |
| **Aliases** | Роман; info@metallka.ru *(domain contact — not org attest)* |
| **Primary organization** | **SAFE UNKNOWN** — future Metallka contour *(Organization not in Wave 1 dataset)* |
| **Population slice** | partner (future independent cluster) |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E0** operator-direct; contacts E1 informal |
| **Population priority** | **W2-P4** (joint with PER-0002) |
| **Expected relationship family (Wave 2B)** | **Deferred** — until Metallka Organization populated |
| **Attestation readiness** | **Ready for Person entity only**; Wave 2B **blocked** |
| **Constraints** | Same isolation as PER-0002; **no MetaCode** |

### 3.4 i-SEO agency — PER-0011 Шваков Никита Алексеевич

| Field | Value |
|-------|-------|
| **Canonical name** | Шваков Никита Алексеевич |
| **Aliases** | Никита |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency (agency-side participant) |
| **Operational contact** | no *(signatory, not primary contact)* |
| **Document signatory** | LE-0002 ИП Шваков Н. А. |
| **Evidence level** | **E1** `i-seo/requisites.txt` (EV-0004) |
| **Population priority** | **W2-P1** |
| **Expected relationship family** | **OWNER** → ORG-0003 |
| **Attestation readiness** | **Ready** |

### 3.5 i-SEO agency — PER-0007 Беслангурова Тамила

| Field | Value |
|-------|-------|
| **Canonical name** | Беслангурова Тамила |
| **Aliases** | Тамила; @tamilabesl |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | yes — primary contact ORG-0003 |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + operator contacts |
| **Population priority** | **W2-P2a** |
| **Expected relationship family** | **REPRESENTATIVE** or **EMPLOYEE** *(review at 2B — assistant role)* |
| **Attestation readiness** | **Ready** |

### 3.6 i-SEO agency — PER-0008 Денис Леонов

| Field | Value |
|-------|-------|
| **Canonical name** | Денис Леонов |
| **Aliases** | Денис |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + contacts |
| **Population priority** | **W2-P2b** |
| **Expected relationship family** | **EMPLOYEE** |
| **Attestation readiness** | **Ready** |

### 3.7 i-SEO agency — PER-0010 Дягилева Ольга

| Field | Value |
|-------|-------|
| **Canonical name** | Дягилева Ольга *(preferred; dataset short form «Оля»)* |
| **Aliases** | Оля; @Ola4seo |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + contacts |
| **Population priority** | **W2-P2b** |
| **Expected relationship family** | **EMPLOYEE** |
| **Attestation readiness** | **Ready** — alias attestation at intake |
| **Gap** | Patronymic **SAFE UNKNOWN** — not in dataset |

### 3.8 i-SEO agency — PER-0012 Илья Гуренков

| Field | Value |
|-------|-------|
| **Canonical name** | Илья Гуренков |
| **Aliases** | Илья; @iGuron89 |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + contacts |
| **Population priority** | **W2-P2b** |
| **Expected relationship family** | **EMPLOYEE** |
| **Attestation readiness** | **Ready** |
| **Gap** | Patronymic **SAFE UNKNOWN** |

### 3.9 i-SEO agency — PER-0013 Иван Корольков

| Field | Value |
|-------|-------|
| **Canonical name** | Иван Корольков |
| **Aliases** | Ваня |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + contacts |
| **Population priority** | **W2-P2b** |
| **Expected relationship family** | **EMPLOYEE** |
| **Attestation readiness** | **Ready** |
| **Gap** | Patronymic **SAFE UNKNOWN** |

### 3.10 i-SEO agency — PER-0009 Антон Кораблёв

| Field | Value |
|-------|-------|
| **Canonical name** | Антон Кораблёв |
| **Aliases** | Антон |
| **Primary organization** | ORG-0003 i-SEO Studio |
| **Population slice** | i-SEO agency |
| **Operational contact** | no |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + contacts |
| **Population priority** | **W2-P2b** |
| **Expected relationship family** | **EMPLOYEE** or **CONTRACTOR** *(developer — review at 2B)* |
| **Attestation readiness** | **Ready** |
| **Gap** | Patronymic **SAFE UNKNOWN** |

### 3.11 Triumph client-side — PER-0004 Макарова Алеся Леонидовна

| Field | Value |
|-------|-------|
| **Canonical name** | Макарова Алеся Леонидовна |
| **Aliases** | Алеся; @Alesya_Diz |
| **Primary organization** | ORG-0004 Триумф |
| **Population slice** | **client-side** |
| **Operational contact** | yes — primary contact ORG-0004 |
| **Document signatory** | no |
| **Evidence level** | **E1** CC `triumph/…2024.xlsx` (EV-0005) + email makarova.a@gktriumph.ru |
| **Population priority** | **W2-P3a** |
| **Expected relationship family** | **REPRESENTATIVE** → ORG-0004 |
| **Attestation readiness** | **Proposed path** (W2-E-02 CC-PER-01) → active after CC line review |

### 3.12 Triumph client-side — PER-0006 Вагин Иван Владимирович

| Field | Value |
|-------|-------|
| **Canonical name** | Вагин Иван Владимирович |
| **Aliases** | Иван Вагин |
| **Primary organization** | ORG-0004 Триумф |
| **Population slice** | **client-side** |
| **Operational contact** | no |
| **Document signatory** | yes — LE-0003 ООО «Триумф» |
| **Evidence level** | **E1** CC (EV-0005) |
| **Population priority** | **W2-P3a** |
| **Expected relationship family** | **REPRESENTATIVE** *(general director)* → ORG-0004 |
| **Attestation readiness** | **Proposed path** → active after CC signatory line match |

### 3.13 Triumph client-side — PER-0005 Подзолков Максим

| Field | Value |
|-------|-------|
| **Canonical name** | Подзолков Максим |
| **Aliases** | Максим |
| **Primary organization** | ORG-0004 Триумф |
| **Population slice** | **client-side** |
| **Operational contact** | no *(IT director — operational, not CC primary)* |
| **Document signatory** | no |
| **Evidence level** | **E1** CC + operator context |
| **Population priority** | **W2-P3b** |
| **Expected relationship family** | **REPRESENTATIVE** *(IT)* → ORG-0004 |
| **Attestation readiness** | **Proposed path** |
| **Gap** | Patronymic **SAFE UNKNOWN**; CC line-level cite **SAFE UNKNOWN** |

---

## 4. Multi-hat discipline — Андрей Русецкий

```text
PER-0001 ──OWNER──► ORG-0001 Полигон
PER-0001 ──OWNER──► ORG-0002 MetaCode      ← MetaCode ONLY Andrey
PER-0001 ──MANAGER──► ORG-0003 i-SEO       ← NOT OWNER
```

Согласовано с [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md), [ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) §multi-hat.

---

## 5. Dataset reconciliation notes

| Item | Treatment in Wave 2 |
|------|---------------------|
| Dataset lifecycle `active` on Persons sheet | **Draft only** — re-attest under Wave 2 governance |
| REL-0004, REL-0005 Person ↔ Person PARTNER | **Do not attest** — violates Wave 2 constraint; defer or reject at 2B review |
| Moscow SERM, Metallka CC folders | Evidence storage pointers only — **not** Organization entities until separate wave |
| CLIENT_OF ORG-0004 → ORG-0001 (REL-0016) | **Wave 6** — not Wave 2B ([ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) W1-EXEC-05) |

---

## 6. Foundation consistency

| Foundation doc | Wave 2 alignment |
|----------------|------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §2 Person | One PER, many ORG via Relationship — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) U4 homonym | Andrey disambiguated; patronymics flagged UNKNOWN where missing |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) | Short names (Оля, Ваня) → alias review at intake |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | E0/E1 tiers assigned per §4.2 Person |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path; no auto-promote |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Person↔Org family only in 2B; no Person↔Person in scope |

**No new entity types.** Population slice labels are intake classification, not taxonomy expansion.

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-PERSON-PRIORITIES-v1.md](ATLAS-WAVE2-PERSON-PRIORITIES-v1.md) | Priority tranches and execution order |
| [ATLAS-WAVE2-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-PERSON-ATTESTATION-v1.md) | Attestation sequence and gates |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W2 checks |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
