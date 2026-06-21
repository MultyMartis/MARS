# ATLAS Wave 2 Attestation Register v1

**Status:** **attested** — canonical Person roster after Wave 2 attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) · [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md)  
**Is not:** relationship registry, runtime export, database table.

---

## 1. Purpose

Канонический **реестр аттестированных Person** после Wave 2 attestation act. Одна строка — одна attested Person record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested | **13** |
| Status **active** | **13** |
| Status deferred / proposed | **0** |
| Primary org SAFE UNKNOWN | **2** (PER-0002, PER-0003) |

---

## 2. Attested roster — full table

| person_id | canonical_name | primary_organization | population_slice | attestation_basis | evidence_tier | status | notes |
|-----------|----------------|---------------------|------------------|-------------------|---------------|--------|-------|
| PER-0001 | Русецкий Андрей Анатольевич | ORG-0001 Веб-студия «Полигон» | internal | E0 operator-direct + E1 CC (EV-0003) | E0 | **active** | Multi-hat; MetaCode OWNER only Andrey; 2B: OWNER×2 + MANAGER×1 |
| PER-0002 | Фатюткин Сергей Игоревич | **SAFE UNKNOWN** | partner (future) | E0 operator-direct; no MetaCode | E0 | **active** | Person only; 2B deferred; Moscow SERM org not populated |
| PER-0003 | Лиматов Роман Курбанович | **SAFE UNKNOWN** | partner (future) | E0 operator-direct; no MetaCode | E0 | **active** | Person only; 2B deferred; Metallka org not populated |
| PER-0011 | Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | i-SEO agency | E1 `i-seo/requisites.txt` (EV-0004) | E1 | **active** | CC signatory; 2B: OWNER→ORG-0003 |
| PER-0007 | Беслангурова Тамила | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts | E1 | **active** | Primary operational contact ORG-0003; 2B: REPRESENTATIVE/EMPLOYEE |
| PER-0008 | Денис Леонов | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts | E1 | **active** | Patronymic UNKNOWN; 2B: EMPLOYEE |
| PER-0010 | Дягилева Ольга | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts; alias Оля | E1 | **active** | Patronymic UNKNOWN; 2B: EMPLOYEE |
| PER-0012 | Илья Гуренков | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts | E1 | **active** | Patronymic UNKNOWN; 2B: EMPLOYEE |
| PER-0013 | Иван Корольков | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts | E1 | **active** | Alias Ваня; patronymic UNKNOWN; 2B: EMPLOYEE |
| PER-0009 | Антон Кораблёв | ORG-0003 i-SEO Studio | i-SEO agency | E1 CC + contacts | E1 | **active** | Developer; EMPLOYEE vs CONTRACTOR at 2B |
| PER-0004 | Макарова Алеся Леонидовна | ORG-0004 Триумф | client-side | E1 CC (EV-0005) + CC-PER-01 | E1 | **active** | Primary contact ORG-0004; 2B: REPRESENTATIVE |
| PER-0005 | Подзолков Максим | ORG-0004 Триумф | client-side | E1 CC + operator context | E1 | **active** | IT director; patronymic UNKNOWN; 2B: REPRESENTATIVE |
| PER-0006 | Вагин Иван Владимирович | ORG-0004 Триумф | client-side | E1 CC signatory match (EV-0005) | E1 | **active** | General director LE-0003; 2B: REPRESENTATIVE |

---

## 3. Attested roster — by population slice

### 3.1 Internal (1)

| person_id | canonical_name | primary_organization | evidence_tier | status |
|-----------|----------------|---------------------|---------------|--------|
| PER-0001 | Русецкий Андрей Анатольевич | ORG-0001 Полигон | E0 | **active** |

### 3.2 Partner — Person only (2)

| person_id | canonical_name | primary_organization | evidence_tier | status |
|-----------|----------------|---------------------|---------------|--------|
| PER-0002 | Фатюткин Сергей Игоревич | **SAFE UNKNOWN** | E0 | **active** |
| PER-0003 | Лиматов Роман Курбанович | **SAFE UNKNOWN** | E0 | **active** |

### 3.3 i-SEO agency (7)

| person_id | canonical_name | primary_organization | evidence_tier | status |
|-----------|----------------|---------------------|---------------|--------|
| PER-0011 | Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0007 | Беслангурова Тамила | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0008 | Денис Леонов | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0010 | Дягилева Ольга | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0012 | Илья Гуренков | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0013 | Иван Корольков | ORG-0003 i-SEO Studio | E1 | **active** |
| PER-0009 | Антон Кораблёв | ORG-0003 i-SEO Studio | E1 | **active** |

### 3.4 Triumph client-side (3)

| person_id | canonical_name | primary_organization | evidence_tier | status |
|-----------|----------------|---------------------|---------------|--------|
| PER-0004 | Макарова Алеся Леонидовна | ORG-0004 Триумф | E1 | **active** |
| PER-0005 | Подзолков Максим | ORG-0004 Триумф | E1 | **active** |
| PER-0006 | Вагин Иван Владимирович | ORG-0004 Триумф | E1 | **active** |

---

## 4. Deferred register (not in attested set)

| Item | Reason | Target wave |
|------|--------|-------------|
| PER-0002 primary organization | Moscow SERM Organization not populated | Future Organization wave |
| PER-0003 primary organization | Metallka Organization not populated | Future Organization wave |
| All Person ↔ Organization edges | Separate attestation pass | **Wave 2B** |
| REL-0004, REL-0005 Person↔Person | Constraint violation | **Rejected** |
| CLIENT_OF ORG-0004 → ORG-0001 | Out of Wave 2B scope | **Wave 6** |

---

## 5. Evidence index (attestation references)

| Ref | Artifact | Persons supported |
|-----|----------|-------------------|
| E0 operator-direct | Steward / Owner attestation context | PER-0001, 0002, 0003 |
| EV-0003 | `polygon/`, `metacode/` CC (LE-0001) | PER-0001 corroboration |
| EV-0004 | `i-seo/requisites.txt` | PER-0011, 0007, 0008, 0010, 0012, 0013, 0009 |
| EV-0005 | `triumph/…2024.xlsx` | PER-0004, 0005, 0006 |
| PersonContacts sheet | Dataset contacts | i-SEO team corroboration |
| CC-PER-01 | Triumph name-to-CC-row mapping | PER-0004, 0005, 0006 |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 6. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE2-ATTESTATION-SUMMARY-v1.md](ATLAS-WAVE2-ATTESTATION-SUMMARY-v1.md) | Executive summary |
