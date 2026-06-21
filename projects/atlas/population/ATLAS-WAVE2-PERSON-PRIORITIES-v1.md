# ATLAS Wave 2 Person Priorities v1

**Status:** **documented** — Wave 2 Person population priority and tranche plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md)  
**Is not:** scheduler, queue implementation, SLA contract.

---

## 1. Purpose

Определить **порядок population и attestation** для 13 persons Wave 2, группы приоритетов, зависимости Wave 1 / Wave 2B, stop conditions.

---

## 2. Priority principles

| Principle | Application |
|-----------|-------------|
| **Operator anchor first** | Андрей Русецкий unlocks core Wave 2B edges |
| **Org endpoint required for 2B** | Person↔Organization only when ORG **active** (W2B-R01) |
| **Partner isolation** | Sergey / Roman — Person intake **without** org edges until future Organization wave |
| **Client corroboration** | Triumph contacts — CC-PER-01 proposed discipline before active |
| **No Person↔Person** | Partner links to Andrey **not** in Wave 2 scope |
| **No MetaCode for partners** | Sergey, Roman **excluded** from ORG-0002 endpoints |

---

## 3. Priority groups

### W2-P0 — Operator anchor (internal)

| Order | Draft ID | Person | Rationale | Min evidence | Wave 2B deps |
|-------|----------|--------|-----------|--------------|--------------|
| **1** | PER-0001 | Русецкий Андрей Анатольевич | Program operator; OWNER Polygon + MetaCode; MANAGER i-SEO | E0 | ORG-0001, ORG-0002, ORG-0003 active |

**Exit gate P0:** Person PER-0001 attested **active**; homonym U4 cleared.

---

### W2-P1 — Agency owner (i-SEO)

| Order | Draft ID | Person | Rationale | Min evidence | Wave 2B deps |
|-------|----------|--------|-----------|--------------|--------------|
| **2** | PER-0011 | Шваков Никита Алексеевич | Legal owner/signatory i-SEO; OWNER edge | E1 | ORG-0003 active |

**Exit gate P1:** OWNER PER-0011 → ORG-0003 queued for 2B (distinct from Andrey MANAGER).

---

### W2-P2 — i-SEO operational and team

| Order | Draft ID | Person | Role in intake | Min evidence | Wave 2B type (review) |
|-------|----------|--------|----------------|--------------|------------------------|
| **3** | PER-0007 | Беслангурова Тамила | Primary operational contact | E1 | REPRESENTATIVE / EMPLOYEE |
| **4** | PER-0008 | Денис Леонов | SEO team | E1 | EMPLOYEE |
| **5** | PER-0010 | Дягилева Ольга | SEO team | E1 | EMPLOYEE |
| **6** | PER-0012 | Илья Гуренков | SEO team | E1 | EMPLOYEE |
| **7** | PER-0013 | Иван Корольков | SEO team | E1 | EMPLOYEE |
| **8** | PER-0009 | Антон Кораблёв | Developer | E1 | EMPLOYEE / CONTRACTOR |

**Batch rule:** P2 persons may attest in parallel **after** P0 + P1; 2B edges batch after all P2 Person records **active**.

---

### W2-P3 — Triumph client-side

| Order | Draft ID | Person | Role in intake | Min evidence | Wave 2B type (review) |
|-------|----------|--------|----------------|--------------|------------------------|
| **9** | PER-0004 | Макарова Алеся Леонидовна | Primary client operational contact | E1 CC | REPRESENTATIVE |
| **10** | PER-0006 | Вагин Иван Владимирович | General director / signatory | E1 CC | REPRESENTATIVE |
| **11** | PER-0005 | Подзолков Максим | IT operational contact | E1 | REPRESENTATIVE |

**CC-PER-01:** Intake as **proposed** if CC line cite incomplete; promote to **active** after steward maps name to CC row (W2-E-02).

**Dependency:** ORG-0004 Триумф **active** (Wave 1 W1-B).

---

### W2-P4 — Partner cluster (future, isolated)

| Order | Draft ID | Person | Rationale | Min evidence | Wave 2B |
|-------|----------|--------|-----------|--------------|---------|
| **12** | PER-0002 | Фатюткин Сергей Игоревич | Future Moscow SERM contour | E0 | **None** — org SAFE UNKNOWN |
| **13** | PER-0003 | Лиматов Роман Курбанович | Future Metallka contour | E0 | **None** — org SAFE UNKNOWN |

**Isolation rules:**

- No link to ORG-0002 MetaCode.
- No Person ↔ Person relationship to PER-0001 or each other.
- No Organization mint for Moscow SERM / Metallka in Wave 2 Person package.
- Wave 2B edges **deferred** until dedicated Organization population (future wave).

---

## 4. Recommended Wave 2 execution order

```text
Phase A — Prerequisites
  └─ Wave 1 org attest complete (ORG-0001..0004 minimum proposed; W1-A active preferred)

Phase B — Person intake (sequential core, parallel team)
  1. PER-0001  Andrey          [P0]
  2. PER-0011  Nikita           [P1]
  3–8. PER-0007..0013 i-SEO     [P2 batch]
  9–11. PER-0004,0006,0005      [P3 Triumph]
  12–13. PER-0002,0003          [P4 partners — Person only]

Phase C — Wave 2B (separate attestation pass)
  C1. Andrey → Polygon, MetaCode, i-SEO
  C2. Nikita → i-SEO OWNER
  C3. i-SEO team → i-SEO
  C4. Triumph contacts → Triumph
  C5. Partners — SKIP (no endpoint)
```

---

## 5. Stop conditions (Wave 2 Person)

| STOP ID | Trigger | Action |
|---------|---------|--------|
| **STOP-W2-01** | Wave 1 org endpoints not at least **proposed** | Halt Person intake (W2-I-03) |
| **STOP-W2-02** | Unresolved Andrey homonym D3 | Halt P0 |
| **STOP-W2-03** | Attempt to link Sergey/Roman to MetaCode | Reject — operator correction |
| **STOP-W2-04** | Person mint from email/phone only | Reject (W2-E-03) |
| **STOP-W2-05** | Person ↔ Person relationship attest in Wave 2 | Reject — defer |
| **STOP-W2-06** | Triumph Person **active** without E1 CC line | Remain **proposed** |

Aligns with [ATLAS-POPULATION-GOVERNANCE-v1.md](../foundation/ATLAS-POPULATION-GOVERNANCE-v1.md).

---

## 6. Dependency matrix

| Person group | Requires Wave 1 | Blocks Wave 2B for |
|--------------|-------------------|----------------------|
| P0 Andrey | ORG-0001, ORG-0002, ORG-0003 | Core operator edges |
| P1 Nikita | ORG-0003 | i-SEO OWNER |
| P2 i-SEO team | ORG-0003 + P1 optional | Team edges |
| P3 Triumph | ORG-0004 | Client representative edges |
| P4 Partners | None (E0 only) | Nothing — intentionally isolated |

---

## 7. Population slice × priority map

| Slice | Persons | Priority | 2B in Wave 2? |
|-------|---------|----------|---------------|
| **internal** | PER-0001 | P0 | **Yes** |
| **i-SEO agency** | PER-0011, 0007, 0008, 0010, 0012, 0013, 0009 | P1–P2 | **Yes** |
| **client-side** | PER-0004, 0006, 0005 | P3 | **Yes** (after CC review) |
| **partner (future)** | PER-0002, 0003 | P4 | **No** — deferred |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) | Full roster analysis |
| [ATLAS-WAVE2-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-PERSON-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W2 checklist |
