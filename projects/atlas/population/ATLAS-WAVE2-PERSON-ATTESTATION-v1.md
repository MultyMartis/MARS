# ATLAS Wave 2 Person Attestation v1

**Status:** **documented** — Wave 2 Person attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-PERSON-PRIORITIES-v1.md](ATLAS-WAVE2-PERSON-PRIORITIES-v1.md)  
**Is not:** attestation runtime, signature platform, automated tier scorer.

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 2 Person, минимальные evidence gates, readiness по каждой персоне, missing evidence, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 2 attestation scope

| In scope | Out of scope |
|----------|--------------|
| Person entity → **proposed** / **active** | Person ↔ Person relationships |
| Evidence tier assignment | Organization population (Wave 1) |
| Alias attestation (short names) | CLIENT_OF org↔org (Wave 6) |
| Wave 2B **queue preparation** | Moscow SERM / Metallka Organization mint |
| Partner isolation enforcement | Cluster entity |

Wave 2B relationship **active** attestation executes in a **separate pass** after Person endpoints and Organization endpoints are **active** (W2B-R01).

---

## 3. Attestation readiness by person

| Draft ID | Person | Target state (Wave 2) | Min tier | Readiness | Blocker |
|----------|--------|----------------------|----------|-----------|---------|
| PER-0001 | Русецкий Андрей Анатольевич | **active** | E0 | **Ready** | — |
| PER-0011 | Шваков Никита Алексеевич | **active** | E1 | **Ready** | — |
| PER-0007 | Беслангурова Тамила | **active** | E1 | **Ready** | — |
| PER-0008 | Денис Леонов | **active** | E1 | **Ready** | — |
| PER-0010 | Дягилева Ольга | **active** | E1 | **Ready** | Alias + patronymic review |
| PER-0012 | Илья Гуренков | **active** | E1 | **Ready** | Patronymic UNKNOWN |
| PER-0013 | Иван Корольков | **active** | E1 | **Ready** | Patronymic UNKNOWN |
| PER-0009 | Антон Кораблёв | **active** | E1 | **Ready** | EMPLOYEE vs CONTRACTOR at 2B |
| PER-0004 | Макарова Алеся Леонидовна | **proposed → active** | E1 | **Conditionally ready** | CC line cite |
| PER-0006 | Вагин Иван Владимирович | **proposed → active** | E1 | **Conditionally ready** | CC signatory match |
| PER-0005 | Подзолков Максим | **proposed → active** | E1 | **Conditionally ready** | CC line + patronymic UNKNOWN |
| PER-0002 | Фатюткин Сергей Игоревич | **active** (Person only) | E0 | **Ready** | No 2B until org wave |
| PER-0003 | Лиматов Роман Курбанович | **active** (Person only) | E0 | **Ready** | No 2B until org wave |

**Readiness legend:**

- **Ready** — steward may attest Person **active** now.
- **Conditionally ready** — attest **active** after CC-PER-01 line mapping (may remain **proposed** during intake).
- **Ready (Person only)** — attest Person without any Wave 2B edge.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W2-01 — Operator anchor

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Duplicate scan U4 — single Andrey in scope | Steward | W2-D-01 |
| 2 | Propose PER-0001 with canonical name | Steward | Dataset + E0 |
| 3 | Assign E0; note E1 CC corroboration | Steward | EV-0003, polygon/metacode CC |
| 4 | Attest Person **active** | Steward (delegated) or Owner | Rationale: operator-direct |
| 5 | Queue 2B: OWNER×2, MANAGER×1 | Steward | [Priorities v1](ATLAS-WAVE2-PERSON-PRIORITIES-v1.md) P0 |

### 4.2 Tranche AT-W2-02 — i-SEO owner

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0003 **active** | Steward | Wave 1 exit |
| 2 | Propose PER-0011 | Steward | i-seo/requisites.txt (EV-0004) |
| 3 | Attest **active** at E1 | Steward | CC signatory = Шваков |
| 4 | Queue 2B OWNER → ORG-0003 | Steward | Distinct from Andrey MANAGER |

### 4.3 Tranche AT-W2-03 — i-SEO team

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Batch propose PER-0007, 0008, 0010, 0012, 0013, 0009 | Steward | EV-0004 + PersonContacts |
| 2 | Alias review: Оля → Ольга; Ваня → Иван | Steward | [ALIAS-MODEL](../foundation/ATLAS-ALIAS-MODEL-v1.md) |
| 3 | Attest **active** at E1 | Steward | Operator + CC context |
| 4 | Queue 2B EMPLOYEE/REPRESENTATIVE/CONTRACTOR edges | Steward | Per relationship review |

### 4.4 Tranche AT-W2-04 — Triumph client-side

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0004 **active** | Steward | Wave 1 W1-B |
| 2 | Propose PER-0004, 0006, 0005 as **proposed** | Steward | EV-0005 |
| 3 | Map each name to CC row (CC-PER-01) | Steward | triumph/…2024.xlsx |
| 4 | Attest **active** at E1 when mapped | Steward | CC + contacts |
| 5 | Queue 2B REPRESENTATIVE → ORG-0004 | Steward | W1-EXEC-04 |

### 4.5 Tranche AT-W2-05 — Partner cluster (isolated)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose PER-0002, PER-0003 | Steward | E0 operator |
| 2 | Confirm **no** primary_org_id to ORG-0002 | Steward | Operator correction |
| 3 | Attest Person **active** at E0 | Owner or Steward | Contacts E1 informal |
| 4 | Record SAFE UNKNOWN for org endpoint | Steward | W2-R-02 |
| 5 | **Do not** queue 2B edges | — | Partner isolation |

### 4.6 Wave 2B pass (after Person + Org active)

Execute per [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) §6 — **not** bundled into Person entity attest steps.

**Explicit exclusions from 2B queue:**

- REL-0004 PER-0002 PARTNER PER-0001 — **reject / do not attest**
- REL-0005 PER-0003 PARTNER PER-0001 — **reject / do not attest**
- Any Sergey or Roman → ORG-0002 MetaCode — **forbidden**

---

## 5. Missing evidence register

| ID | Person / topic | Gap | Severity | Mitigation |
|----|----------------|-----|----------|------------|
| **ME-W2-01** | PER-0010, 0012, 0013, 0009 | Patronymic SAFE UNKNOWN | Low | Optional CC/ID supplement; not blocking E1 team attest |
| **ME-W2-02** | PER-0005 Подзолков | Patronymic SAFE UNKNOWN | Low | CC line cite if present |
| **ME-W2-03** | PER-0004, 0005 | CC row-level cite not in Evidence sheet | Medium | CC-PER-01 mapping during AT-W2-04 |
| **ME-W2-04** | PER-0002 | Moscow SERM Organization not populated | High for 2B only | Defer 2B; Person E0 sufficient |
| **ME-W2-05** | PER-0003 | Metallka Organization not populated | High for 2B only | Defer 2B; Person E0 sufficient |
| **ME-W2-06** | PER-0009 | EMPLOYEE vs CONTRACTOR undecided | Low | Decide at 2B review |
| **ME-W2-07** | Dataset REL-0004/0005 | Person↔Person in draft dataset | Medium | Reject at attestation — not evidence |

---

## 6. Readiness checklist crosswalk

| Check ID | Wave 2 Person package assessment |
|----------|----------------------------------|
| W2-S-01 | Wave 1 duplicate batch — **assumed complete** (operator: Wave 1 complete) |
| W2-S-02 | Homonym review planned — **yes** (W2-D-01) |
| W2-S-03 | Person vs service account — **yes** |
| W2-E-01 | E0 path Andrey, Sergey, Roman — **yes** |
| W2-E-02 | Triumph CC-PER-01 — **planned** in AT-W2-04 |
| W2-E-03 | Email-only mint prohibited — **yes** |
| W2-D-01 | Andrey homonym — **single in scope** |
| W2-D-02 | Triumph name scan — **in dataset** |
| W2-I-03 | Wave 1 orgs proposed/active — **yes** (dataset draft active) |
| W2-R-01 | Andrey edges pre-identified — **yes** |
| W2-R-02 | Sergey/Roman org SAFE UNKNOWN — **declared** |
| W2-R-04 | CLIENT_OF deferred — **yes** |

---

## 7. Final verdict

### 7.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 2 Person intake cannot start |
| **PARTIALLY READY** | Intake may start with documented blockers |
| **READY FOR WAVE 2 ATTESTATION** | Full Person intake plan executable under gates |

### 7.2 Assessment

| Criterion | Status |
|-----------|--------|
| All 13 required persons classified | **Pass** |
| Wave 1 org endpoints available (ORG-0001..0004) | **Pass** (draft + operator confirmation) |
| Operator correction MetaCode / partners enforced | **Pass** |
| Evidence paths documented (E0/E1) | **Pass** |
| Foundation consistency Phase 1–9 | **Pass** — no new entity types |
| Known gaps enumerated | **Pass** — ME-W2-01..07 |
| Partner 2B deferred | **Pass** — by design |

### 7.3 Verdict

```text
READY FOR WAVE 2 ATTESTATION
```

**Conditions:**

1. Wave 1 Organization attestation should complete or receive owner-approved GA-03 defer **before** Wave 2B relationship **active** promotion.
2. Triumph persons (P3) may enter as **proposed** until CC-PER-01 completes — does not block package start.
3. Sergey and Roman attest as **Person only** — no org edges, no MetaCode, no Person↔Person.
4. Draft dataset `active` flags **do not substitute** for steward attestation acts.

---

## 8. Post-Wave 2 exit criteria

| Criterion | Evidence |
|-----------|----------|
| PER-0001 active | Attestation record |
| i-SEO team (7 persons) active | Batch attest log |
| Triumph contacts active or proposed with CC note | AT-W2-04 log |
| Partners active, org UNKNOWN documented | AT-W2-05 log |
| No Person↔Person attested | 2B queue audit |
| Wave 2B core queue prepared | Andrey + i-SEO + Triumph edges listed |
| Gap register ME-W2-* updated | Steward sign-off |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-PERSON-POPULATION-v1.md](ATLAS-WAVE2-PERSON-POPULATION-v1.md) | Canonical roster |
| [ATLAS-WAVE2-PERSON-PRIORITIES-v1.md](ATLAS-WAVE2-PERSON-PRIORITIES-v1.md) | Execution order |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | Person §4.2 |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Source dataset |
