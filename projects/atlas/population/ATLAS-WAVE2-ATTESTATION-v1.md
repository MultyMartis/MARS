# ATLAS Wave 2 Attestation v1

**Status:** **attested** — first official Person attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-PERSON-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, relationship attestation, Wave 2B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation Readiness: **COMPLETE**
- Wave 2 Person Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 2 ATTESTATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** класса **Person** для Wave 2: 13 записей переведены из approved population draft в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Person entity → **active** | Person ↔ Person relationships |
| Evidence tier assignment per person | Organization attestation (Wave 1 — separate) |
| Alias acceptance (short names) | Person ↔ Organization edges (Wave 2B) |
| SAFE UNKNOWN declaration (partners) | Moscow SERM / Metallka Organization mint |
| Partner isolation enforcement | CLIENT_OF org↔org (Wave 6) |
| Wave 2B queue preparation note | Cluster entity |

**Binding operator corrections (enforced):**

- MetaCode (ORG-0002) принадлежит **только** Андрею Русецкому — не партнёрам.
- Сергей Фатюткин и Роман Лиматов — **Person only**; primary organization **SAFE UNKNOWN**.
- Никаких Person↔Person edges; REL-0004 / REL-0005 **не аттестированы**.

---

## 2. Attestation tranches executed

| Tranche | Persons | Basis | Outcome |
|---------|---------|-------|---------|
| **AT-W2-01** | PER-0001 | E0 operator-direct + E1 CC corroboration | **active** |
| **AT-W2-02** | PER-0011 | E1 `i-seo/requisites.txt` (EV-0004) | **active** |
| **AT-W2-03** | PER-0007, 0008, 0010, 0012, 0013, 0009 | E1 CC + PersonContacts | **active** |
| **AT-W2-04** | PER-0004, 0006, 0005 | E1 CC `triumph/…2024.xlsx` (EV-0005) + CC-PER-01 mapping | **active** |
| **AT-W2-05** | PER-0002, 0003 | E0 operator-direct | **active** (Person only) |

---

## 3. Per-person attestation records

### 3.1 Internal

#### PER-0001 — Русецкий Андрей Анатольевич

| Field | Value |
|-------|-------|
| **person_id** | PER-0001 |
| **canonical_name** | Русецкий Андрей Анатольевич |
| **primary_organization** | ORG-0001 Веб-студия «Полигон» *(display primary; multi-org via Wave 2B)* |
| **attestation_basis** | E0 operator-direct; steward confirms single Andrey in scope (W2-D-01 homonym cleared); E1 corroboration `polygon/ИП Русецкий А. А.pdf`, `metacode/ИП Русецкий А. А.pdf` (EV-0003) |
| **evidence_tier** | **E0** |
| **status** | **active** |
| **notes** | Population slice: internal. Document signatory LE-0001. MetaCode OWNER only Andrey — enforced. Wave 2B queue: OWNER→ORG-0001, OWNER→ORG-0002, MANAGER→ORG-0003. |

---

### 3.2 Partner (Person only)

#### PER-0002 — Фатюткин Сергей Игоревич

| Field | Value |
|-------|-------|
| **person_id** | PER-0002 |
| **canonical_name** | Фатюткин Сергей Игоревич |
| **primary_organization** | **SAFE UNKNOWN** |
| **attestation_basis** | E0 operator-direct; steward confirms future Moscow SERM contour — Organization **not** in Wave 1 dataset; **no** attachment to ORG-0002 MetaCode |
| **evidence_tier** | **E0** |
| **status** | **active** |
| **notes** | Population slice: partner (future). Wave 2B **deferred** (W2-R-02). No Person↔Person edges. No inferred organization. |

#### PER-0003 — Лиматов Роман Курбанович

| Field | Value |
|-------|-------|
| **person_id** | PER-0003 |
| **canonical_name** | Лиматов Роман Курбанович |
| **primary_organization** | **SAFE UNKNOWN** |
| **attestation_basis** | E0 operator-direct; steward confirms future Metallka contour — Organization **not** in Wave 1 dataset; **no** attachment to ORG-0002 MetaCode |
| **evidence_tier** | **E0** |
| **status** | **active** |
| **notes** | Population slice: partner (future). Wave 2B **deferred** (W2-R-02). No Person↔Person edges. No inferred organization. |

---

### 3.3 i-SEO agency

#### PER-0011 — Шваков Никита Алексеевич

| Field | Value |
|-------|-------|
| **person_id** | PER-0011 |
| **canonical_name** | Шваков Никита Алексеевич |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 `i-seo/requisites.txt` (EV-0004); CC signatory = Шваков; ORG-0003 Wave 1 endpoint available |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Population slice: i-SEO agency. Document signatory LE-0002. Wave 2B queue: OWNER→ORG-0003 (distinct from Andrey MANAGER). |

#### PER-0007 — Беслангурова Тамила

| Field | Value |
|-------|-------|
| **person_id** | PER-0007 |
| **canonical_name** | Беслангурова Тамила |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts (PersonContacts); primary operational contact ORG-0003 |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Wave 2B queue: REPRESENTATIVE or EMPLOYEE — review at 2B. |

#### PER-0008 — Денис Леонов

| Field | Value |
|-------|-------|
| **person_id** | PER-0008 |
| **canonical_name** | Денис Леонов |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts (PersonContacts) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Alias: Денис. Wave 2B queue: EMPLOYEE. Patronymic SAFE UNKNOWN — not blocking. |

#### PER-0010 — Дягилева Ольга

| Field | Value |
|-------|-------|
| **person_id** | PER-0010 |
| **canonical_name** | Дягилева Ольга |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts; alias **Оля** attested per [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Alias review complete. Patronymic SAFE UNKNOWN — not blocking. Wave 2B queue: EMPLOYEE. |

#### PER-0012 — Илья Гуренков

| Field | Value |
|-------|-------|
| **person_id** | PER-0012 |
| **canonical_name** | Илья Гуренков |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts (PersonContacts) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Alias: Илья. Patronymic SAFE UNKNOWN. Wave 2B queue: EMPLOYEE. |

#### PER-0013 — Иван Корольков

| Field | Value |
|-------|-------|
| **person_id** | PER-0013 |
| **canonical_name** | Иван Корольков |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts (PersonContacts) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Alias: Ваня. Patronymic SAFE UNKNOWN. Wave 2B queue: EMPLOYEE. |

#### PER-0009 — Антон Кораблёв

| Field | Value |
|-------|-------|
| **person_id** | PER-0009 |
| **canonical_name** | Антон Кораблёв |
| **primary_organization** | ORG-0003 i-SEO Studio |
| **attestation_basis** | E1 CC + operator contacts (PersonContacts) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Developer role. EMPLOYEE vs CONTRACTOR — decide at Wave 2B. Patronymic SAFE UNKNOWN. |

---

### 3.4 Triumph client-side

#### PER-0004 — Макарова Алеся Леонидовна

| Field | Value |
|-------|-------|
| **person_id** | PER-0004 |
| **canonical_name** | Макарова Алеся Леонидовна |
| **primary_organization** | ORG-0004 Триумф |
| **attestation_basis** | E1 CC `triumph/…2024.xlsx` (EV-0005); CC-PER-01 name mapping complete; email makarova.a@gktriumph.ru corroboration |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Population slice: client-side. Primary operational contact ORG-0004. Wave 2B queue: REPRESENTATIVE. |

#### PER-0005 — Подзолков Максим

| Field | Value |
|-------|-------|
| **person_id** | PER-0005 |
| **canonical_name** | Подзолков Максим |
| **primary_organization** | ORG-0004 Триумф |
| **attestation_basis** | E1 CC + operator context; CC-PER-01 mapping (IT director role) |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | Patronymic SAFE UNKNOWN. CC line-level cite partial — attested at E1 with operator context. Wave 2B queue: REPRESENTATIVE (IT). |

#### PER-0006 — Вагин Иван Владимирович

| Field | Value |
|-------|-------|
| **person_id** | PER-0006 |
| **canonical_name** | Вагин Иван Владимирович |
| **primary_organization** | ORG-0004 Триумф |
| **attestation_basis** | E1 CC (EV-0005); CC signatory match LE-0003 ООО «Триумф» |
| **evidence_tier** | **E1** |
| **status** | **active** |
| **notes** | General director / document signatory. Wave 2B queue: REPRESENTATIVE. |

---

## 4. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-0004 PER-0002 PARTNER PER-0001 | **Rejected** — not attested |
| REL-0005 PER-0003 PARTNER PER-0001 | **Rejected** — not attested |
| Sergey / Roman → ORG-0002 MetaCode | **Forbidden** — not attested |
| Any Person ↔ Organization edge | **Deferred** — Wave 2B separate pass |
| Moscow SERM Organization | **Deferred** — future Organization wave |
| Metallka Organization | **Deferred** — future Organization wave |
| CLIENT_OF ORG-0004 → ORG-0001 (REL-0016) | **Deferred** — Wave 6 |

---

## 5. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §2 Person | 13 Person records attested — no new entity types |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) U4 homonym | Andrey disambiguated; patronymic gaps flagged UNKNOWN |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) | Short names (Оля, Ваня, Денис) accepted as aliases |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | E0/E1 tiers per §4.3; human attestation act recorded |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; no auto-promote from dataset `active` flags |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | No relationships attested — Person endpoints only |
| [ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) CR-10 | Partner org SAFE UNKNOWN — no `org-unknown-*` mint |

**Foundation modified:** **No**  
**Wave 1 modified:** **No**  
**New entities introduced:** **No**

---

## 6. Attestation verdict

```text
WAVE 2 PERSON ATTESTATION — COMPLETE
13 / 13 persons attested active
0 persons deferred from attestation
Wave 2B relationship population — READY TO START
```

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | Attested roster table |
| [ATLAS-WAVE2-ATTESTATION-SUMMARY-v1.md](ATLAS-WAVE2-ATTESTATION-SUMMARY-v1.md) | Executive summary and Wave 2B readiness |
| [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Source dataset |
