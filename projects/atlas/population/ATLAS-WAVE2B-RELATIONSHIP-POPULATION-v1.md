# ATLAS Wave 2B Relationship Population v1

**Status:** **documented** — first canonical Person → Organization relationship population plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 3 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation: **COMPLETE**
- Wave 2 Attestation: **COMPLETE**
- Population verdict: **READY FOR WAVE 2B RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** первого набора **Person → Organization** relationships для Wave 2B: состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 2B:**

```text
Person → Organization relationships only
No Person ↔ Person
No Organization ↔ Organization
No new entity types
No new relationship families
```

**Binding operator corrections (carried from Wave 2):**

- MetaCode (ORG-0002) **OWNER** — только PER-0001 Андрей Русецкий.
- PER-0002 Сергей и PER-0003 Роман — **без** Person → Organization edges до future Organization population.
- REL-0004 / REL-0005 Person ↔ Person — **не аттестировать**.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **12** |
| Person endpoints (active) | **11** |
| Organization endpoints (active) | **4** (ORG-0001..0004) |
| Persons excluded by design | **2** (PER-0002, PER-0003) |
| Relationship families used | Person → Organization only |

### 2.1 Summary table

| relationship_id | source_person | target_organization | relationship_type | organization group | attestation readiness |
|-----------------|---------------|---------------------|-------------------|--------------------|-----------------------|
| REL-0001 | PER-0001 Русецкий Андрей Анатольевич | ORG-0001 Веб-студия «Полигон» | **OWNER** | Polygon | **ready** |
| REL-0002 | PER-0001 Русецкий Андрей Анатольевич | ORG-0002 Агентство «МетаКод» | **OWNER** | MetaCode | **ready** |
| REL-0006 | PER-0011 Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | **OWNER** | i-SEO | **ready** |
| REL-0007 | PER-0007 Беслангурова Тамила | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0008 | PER-0008 Денис Леонов | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0009 | PER-0010 Дягилева Ольга | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0010 | PER-0012 Илья Гуренков | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0011 | PER-0013 Иван Корольков | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0012 | PER-0009 Антон Кораблёв | ORG-0003 i-SEO Studio | **EMPLOYEE** | i-SEO | **ready** |
| REL-0013 | PER-0004 Макарова Алеся Леонидовна | ORG-0004 Триумф | **REPRESENTATIVE** | Triumph | **ready** |
| REL-0014 | PER-0005 Подзолков Максим | ORG-0004 Триумф | **EMPLOYEE** | Triumph | **ready** |
| REL-0015 | PER-0006 Вагин Иван Владимирович | ORG-0004 Триумф | **GENERAL_DIRECTOR** | Triumph | **ready** |

---

## 3. Per-relationship analysis

### 3.1 Polygon — REL-0001

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0001 |
| **source_person** | PER-0001 Русецкий Андрей Анатольевич |
| **target_organization** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **OWNER** |
| **attestation_basis** | E0 operator-direct (PER-0001 active); E1 CC corroboration `polygon/ИП Русецкий А. А.pdf` (EV-0003, LE-0001); ORG-0001 Wave 1 active endpoint |
| **evidence_tier** | **E0** (primary); E1 corroboration |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | OWNER, PER-0001 → ORG-0001 |
| **notes** | Multi-hat anchor edge; distinct from ORG-0002 OWNER |

### 3.2 MetaCode — REL-0002

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0002 |
| **source_person** | PER-0001 Русецкий Андрей Анатольевич |
| **target_organization** | ORG-0002 Агентство «МетаКод» |
| **relationship_type** | **OWNER** |
| **attestation_basis** | E0 operator-direct; E1 CC `metacode/ИП Русецкий А. А.pdf` (EV-0003); operator correction: MetaCode **only** Andrey — not PER-0002 / PER-0003 |
| **evidence_tier** | **E0** (primary); E1 corroboration |
| **lifecycle_state** | **active** |
| **slot** | OWNER, PER-0001 → ORG-0002 |
| **notes** | Partner isolation enforced (W2-R-02) |

### 3.3 i-SEO — owner REL-0006

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0006 |
| **source_person** | PER-0011 Шваков Никита Алексеевич |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **OWNER** |
| **attestation_basis** | E1 `i-seo/requisites.txt` (EV-0004); CC signatory = Шваков; PER-0011 and ORG-0003 both **active** |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **slot** | OWNER, PER-0011 → ORG-0003 |
| **notes** | Distinct from any deferred MANAGER edge for PER-0001 |

### 3.4 i-SEO — team REL-0007..0012

#### REL-0007 — PER-0007 Беслангурова Тамила

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0007 |
| **source_person** | PER-0007 Беслангурова Тамила |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts; primary operational contact ORG-0003; operator-approved type **EMPLOYEE** (dataset draft had REPRESENTATIVE — superseded at 2B) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0008 — PER-0008 Денис Леонов

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0008 |
| **source_person** | PER-0008 Денис Леонов |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts (EV-0004) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0009 — PER-0010 Дягилева Ольга

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0009 |
| **source_person** | PER-0010 Дягилева Ольга |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts; alias Оля attested at Wave 2 |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0010 — PER-0012 Илья Гуренков

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0010 |
| **source_person** | PER-0012 Илья Гуренков |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0011 — PER-0013 Иван Корольков

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0011 |
| **source_person** | PER-0013 Иван Корольков |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts; alias Ваня attested at Wave 2 |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0012 — PER-0009 Антон Кораблёв

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0012 |
| **source_person** | PER-0009 Антон Кораблёв |
| **target_organization** | ORG-0003 i-SEO Studio |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + PersonContacts; ME-W2-06 resolved: **EMPLOYEE** (not CONTRACTOR) at operator-approved 2B list |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

### 3.5 Triumph — REL-0013..0015

#### REL-0013 — PER-0004 Макарова Алеся Леонидовна

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0013 |
| **source_person** | PER-0004 Макарова Алеся Леонидовна |
| **target_organization** | ORG-0004 Триумф |
| **relationship_type** | **REPRESENTATIVE** |
| **attestation_basis** | E1 CC `triumph/…2024.xlsx` (EV-0005); CC-PER-01 mapping; primary operational contact ORG-0004 |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0014 — PER-0005 Подзолков Максим

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0014 |
| **source_person** | PER-0005 Подзолков Максим |
| **target_organization** | ORG-0004 Триумф |
| **relationship_type** | **EMPLOYEE** |
| **attestation_basis** | E1 CC + operator context; IT director role; operator-approved type **EMPLOYEE** (dataset draft had REPRESENTATIVE — superseded at 2B) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |

#### REL-0015 — PER-0006 Вагин Иван Владимирович

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0015 |
| **source_person** | PER-0006 Вагин Иван Владимирович |
| **target_organization** | ORG-0004 Триумф |
| **relationship_type** | **GENERAL_DIRECTOR** |
| **attestation_basis** | E1 CC signatory match LE-0003 ООО «Триумф» (EV-0005); генеральный директор / document signatory |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **taxonomy_note** | GENERAL_DIRECTOR ∉ [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) baseline; operator-approved Wave 2B role label. Canonical family: Person → Organization **REPRESENTATIVE** with `role_qualifier: general_director` (see §6). |

---

## 4. Multi-hat discipline — Polygon / MetaCode / i-SEO

```text
PER-0001 ──OWNER──► ORG-0001 Полигон
PER-0001 ──OWNER──► ORG-0002 MetaCode      ← MetaCode ONLY Andrey
PER-0011 ──OWNER──► ORG-0003 i-SEO       ← OWNER distinct from any PER-0001 management role
```

**Deferred (not in approved 2B list):** PER-0001 ──MANAGER──► ORG-0003 (dataset REL-0003) — **not populated** in this package.

---

## 5. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| PER-0002 → any Organization | **Do not create** | Future Organization wave (Moscow SERM) |
| PER-0003 → any Organization | **Do not create** | Future Organization wave (Metallka) |
| REL-0003 PER-0001 MANAGER ORG-0003 | **Deferred** | Not in operator-approved 2B list |
| REL-0004 PER-0002 PARTNER PER-0001 | **Rejected** | Person ↔ Person forbidden |
| REL-0005 PER-0003 PARTNER PER-0001 | **Rejected** | Person ↔ Person forbidden |
| Sergey / Roman → ORG-0002 MetaCode | **Forbidden** | Partner isolation |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** | Wave 6 |
| REL-0017+ Project / Website / Domain edges | **Deferred** | Wave 3+ |

---

## 6. Foundation consistency

| Foundation doc | Wave 2B alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Person→Org directed edges; multi-hat via independent REL records — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 | OWNER, EMPLOYEE, REPRESENTATIVE in baseline — **yes**; GENERAL_DIRECTOR → REPRESENTATIVE family + role qualifier (W2B-TAX-01) |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PER-* / ORG-* active — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active` — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path; dataset draft `active` ≠ canonical — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**No new entity types.** **No new relationship families** (Person → Organization only).

**W2B-TAX-01:** `GENERAL_DIRECTOR` is an operator-approved **role qualifier** for REL-0015; taxonomy canonical type remains **REPRESENTATIVE** per RR-02 until expansion review adds explicit type.

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Person endpoints |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
