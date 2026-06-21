# ATLAS Wave 2 ZPM Person Attestation v1

**Status:** **documented** — Wave 2 ZPM Person attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** attestation runtime, executed attestation act, Wave 2B relationship attestation.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- ORG-0005 ЗПМ Organization: **active** (AT-W1B-01)
- EV-W1B-CC-01: **present** and inventoried (CPV-01)

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 2 ZPM Person (2 records), минимальные evidence gates, readiness по каждой персоне, missing evidence, candidate Wave 2B queue, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 2 ZPM attestation scope

| In scope | Out of scope |
|----------|--------------|
| Person entity → **proposed** / **active** (2 records) | Person ↔ Person relationships |
| Evidence tier assignment | Organization attestation (ORG-0005 — complete) |
| Alias attestation (PER-0014 short names) | Project / Website / Domain entities |
| Wave 2B-ZPM **queue preparation** | Commercial relationships (Wave 6+) |
| Business reality notes (EDO; Diadoc signer UNKNOWN) | Person → Organization edge **creation** |

Wave 2B-ZPM relationship **active** attestation executes in a **separate pass** after both Person endpoints and ORG-0005 are **active**.

---

## 3. Attestation readiness by person

| Draft ID | Person | Target state (Wave 2 ZPM) | Min tier | Readiness | Blocker |
|----------|--------|---------------------------|----------|-----------|---------|
| PER-0015 | Крюков Александр Сергеевич | **active** | E1 | **Ready** | — |
| PER-0014 | Алексей Владимирович Дубинский | **active** | E0 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Person **active** now under cited tier.
- No **Conditionally ready** rows — operator inputs complete for this tranche scope.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W2-ZPM-01 — CC signatory (legal anchor)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0005 **active** | Steward | AT-W1B-01 |
| 2 | Confirm EV-W1B-CC-01 inventory (CPV-01) | Steward | §1 population package |
| 3 | Duplicate scan W2-ZPM-D-01..05 | Steward | Register §6 |
| 4 | Propose PER-0015 with canonical name | Steward | EV-W1B-CC-01 §19–§24 |
| 5 | Map to LE-0004 `document_signatory` | Steward | Active attestation §7.1 |
| 6 | Assign **E1**; record operator phone E0 | Steward | EV-W2-ZPM-OP-01 |
| 7 | Attest Person **active** | Steward (delegated) or Owner | CC signatory discipline |
| 8 | Queue 2B: GENERAL_DIRECTOR → ORG-0005 | Steward | REL-ZPM-01 *(not executed here)* |

### 4.2 Tranche AT-W2-ZPM-02 — Primary operational contact

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose PER-0014 with full patronymic | Steward | EV-W2-ZPM-OP-01 |
| 2 | Accept aliases: Алексей Дубинский; Дубинский | Steward | [ALIAS-MODEL](../foundation/ATLAS-ALIAS-MODEL-v1.md) |
| 3 | Register contacts (TG, phone, email) | Steward | EV-W2-ZPM-OP-01 |
| 4 | Confirm **not** CC signatory; Diadoc signer **SAFE UNKNOWN** | Steward | EFV-06 |
| 5 | Assign **E0** | Steward | Operator-direct |
| 6 | Attest Person **active** | Steward | Operational contact pattern |
| 7 | Queue 2B: REPRESENTATIVE → ORG-0005 | Steward | REL-ZPM-02 *(not executed here)* |

### 4.3 Wave 2B-ZPM pass (after Person active)

Execute in **separate package** — not bundled into steps above.

| Candidate | Type *(review)* | Prerequisite |
|-----------|-----------------|--------------|
| REL-ZPM-01 PER-0015 → ORG-0005 | **GENERAL_DIRECTOR** | PER-0015 **active** |
| REL-ZPM-02 PER-0014 → ORG-0005 | **REPRESENTATIVE** | PER-0014 **active** |

**Explicit exclusion:** Do **not** set ORG-0005 `primary_contact_person_id` until Wave 2B attestation selects operational slot (expected PER-0014 — steward confirms).

---

## 5. Missing evidence register

| ID | Person / topic | Gap | Severity | Mitigation |
|----|----------------|-----|----------|------------|
| **ME-W2-ZPM-01** | PER-0014 | Not named in EV-W1B-CC-01 | Medium *(identity)* | E0 operator attest sufficient for **active** Person; optional future CC supplement |
| **ME-W2-ZPM-02** | PER-0014 | Role titles (зам./исп./тех. директор) not CC-backed | Low | Record as operator role signals; decide EMPLOYEE vs REPRESENTATIVE at 2B |
| **ME-W2-ZPM-03** | PER-0015 | Phone +79039573236 not in CC | Low | E0 operator contact; not blocking E1 Person attest |
| **ME-W2-ZPM-04** | PER-0015 | Email, Telegram **SAFE UNKNOWN** | Low | Optional operator supplement |
| **ME-W2-ZPM-05** | ORG-0005 | Diadoc / EDO specific signer | Medium *(signatory ops)* | **SAFE UNKNOWN** — do not infer PER-0014 or PER-0015 as Diadoc signer |
| **ME-W2-ZPM-06** | ORG-0005 | EDO participant id | Low | ME-W1B-05 carry-forward; CC update |
| **ME-W2-ZPM-07** | PER-0014 | Email domain assum.ru vs org bzpm.ru | Low | Contact pointer only — EFV-01 |

**Blocking gaps for Person attestation:** **None**

---

## 6. Readiness checklist crosswalk

| Check ID | Wave 2 ZPM Person package assessment |
|----------|---------------------------------------|
| W2-S-01 | Duplicate batch for new persons — **yes** (W2-ZPM-D-01..05) |
| W2-S-02 | Homonym review — **yes** — no collision with PER-0001..0013 |
| W2-S-03 | Person vs service account — **yes** — human contacts attested |
| W2-E-01 | E0 path PER-0014 — **yes** |
| W2-E-02 | CC-backed path PER-0015 — **yes** (EV-W1B-CC-01) |
| W2-E-03 | Email-only mint prohibited — **yes** — PER-0014 has name + multi-channel contacts |
| W2-I-03 | ORG-0005 endpoint **active** — **yes** |
| W2-R-01 | 2B edges pre-identified — **yes** — REL-ZPM-01, REL-ZPM-02 queued |
| EFV-04 | CC read before conclusions — **yes** |
| CPV-01 | CC inventory cited — **yes** |

---

## 7. Final verdict

### 7.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 2 ZPM Person intake cannot start |
| **PARTIALLY READY** | Intake may start with documented blockers |
| **READY FOR WAVE 2 ZPM PERSON ATTESTATION** | Full Person intake plan executable under gates |

### 7.2 Assessment

| Criterion | Status |
|-----------|--------|
| Both required persons classified | **Pass** (2/2) |
| ORG-0005 endpoint **active** | **Pass** |
| EV-W1B-CC-01 present and cited | **Pass** |
| Evidence First / Card Presence discipline | **Pass** |
| Operator contacts and statements recorded | **Pass** |
| Diadoc signer not invented | **Pass** — **SAFE UNKNOWN** |
| Wave 2B relationships analyzed, not created | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Known gaps enumerated | **Pass** — ME-W2-ZPM-01..07 |

### 7.3 Verdict

```text
READY FOR WAVE 2 ZPM PERSON ATTESTATION
```

**Conditions:**

1. Execute **AT-W2-ZPM-01** before **AT-W2-ZPM-02** — CC signatory anchor first.
2. Wave 2B-ZPM relationship **active** promotion requires both Person records **active** — separate pass.
3. Do **not** attest Diadoc signer without explicit evidence.
4. Draft register `proposed` flags **do not substitute** for steward attestation acts.

---

## 8. Post-Wave 2 ZPM exit criteria

| Criterion | Evidence |
|-----------|----------|
| PER-0015 **active** | Attestation record AT-W2-ZPM-01 |
| PER-0014 **active** | Attestation record AT-W2-ZPM-02 |
| Aliases PER-0014 accepted | Register §3 |
| No Person ↔ Person attested | Scope audit |
| Wave 2B-ZPM queue prepared | REL-ZPM-01, REL-ZPM-02 listed |
| ME-W2-ZPM-* updated | Steward sign-off |
| ORG-0005 primary_contact | **Deferred** to Wave 2B |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) | Canonical roster and analysis |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Proposed register rows |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 / LE-0004 active basis |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | Person §4.2 |

---

*ATLAS Wave 2 ZPM Person Attestation v1 — documentation only.*
