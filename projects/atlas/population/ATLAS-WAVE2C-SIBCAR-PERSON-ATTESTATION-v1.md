# ATLAS Wave 2C SIBCAR Person Attestation v1

**Status:** **documented** — Wave 2C SIBCAR Person attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** attestation runtime, executed attestation act, Wave 2C relationship attestation.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- Wave 2 ZPM Person attestation (PER-0014, PER-0015): **COMPLETE**
- ORG-0006 SIBCAR Organization: **active** (AT-W1C-01)
- EV-W1C-CC-01: **present** and inventoried (CPV-01)

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 2C SIBCAR Person (2 records), минимальные evidence gates, readiness по каждой персоне, missing evidence, candidate Wave 2C relationship queue, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 2C SIBCAR attestation scope

| In scope | Out of scope |
|----------|--------------|
| Person entity → **proposed** / **active** (2 records) | Person ↔ Person relationships |
| Evidence tier assignment | Organization attestation (ORG-0006 — complete) |
| Wave 2C relationship **queue preparation** | Project / Website / Domain entities |
| Business reality notes (two-person model; Diadoc signer UNKNOWN) | Commercial relationships (Wave 6+) |
| Resolution of discovery OQ-W2C-01, 04, 09, 10, 14 | Person → Organization edge **creation** |

Wave 2C SIBCAR relationship **active** attestation executes in a **separate pass** after both Person endpoints and ORG-0006 are **active**.

---

## 3. Attestation readiness by person

| Draft ID | Person | Target state (Wave 2C SIBCAR) | Min tier | Readiness | Blocker |
|----------|--------|-------------------------------|----------|-----------|---------|
| PER-0016 | Карандашов Максим Петрович | **active** | E1 | **Ready** | — |
| PER-0017 | Хаял | **active** | E0 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Person **active** now under cited tier.
- No **Conditionally ready** rows — operator inputs complete for this tranche scope.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W2C-SIBCAR-01 — CC signatory (legal anchor)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0006 **active** | Steward | AT-W1C-01 |
| 2 | Confirm EV-W1C-CC-01 inventory (CPV-01) | Steward | §1 population package |
| 3 | Duplicate scan W2C-SIBCAR-D-01..06 | Steward | Register §6 |
| 4 | Propose PER-0016 with canonical name | Steward | EV-W1C-CC-01 §21–§24 |
| 5 | Map to LE-0005 `document_signatory` | Steward | Active attestation §7.1 |
| 6 | Assign **E1** | Steward | CC signatory discipline |
| 7 | Attest Person **active** | Steward (delegated) or Owner | CC signatory discipline |
| 8 | Queue 2C rel: GENERAL_DIRECTOR → ORG-0006 | Steward | REL-SIBCAR-01 *(not executed here)* |

### 4.2 Tranche AT-W2C-SIBCAR-02 — Primary operational contact

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose PER-0017 with canonical name Хаял | Steward | EV-W2C-SIBCAR-OP-01 |
| 2 | Record patronymic **SAFE UNKNOWN** | Steward | EFV-06 |
| 3 | Register Telegram contact @Khayal8888 | Steward | EV-W2C-SIBCAR-OP-01 |
| 4 | Confirm **not** CC signatory; «Business Owner» = role signal only — **no** OWNER edge | Steward | ZPM precedent |
| 5 | Confirm Diadoc signer **SAFE UNKNOWN** | Steward | EFV-06 |
| 6 | Assign **E0** | Steward | Operator-direct |
| 7 | Attest Person **active** | Steward | Operational contact pattern |
| 8 | Queue 2C rel: REPRESENTATIVE → ORG-0006 | Steward | REL-SIBCAR-02 *(not executed here)* |

### 4.3 Wave 2C SIBCAR relationship pass (after Person active)

Execute in **separate package** — not bundled into steps above.

| Candidate | Type | Prerequisite |
|-----------|------|--------------|
| REL-SIBCAR-01 PER-0016 → ORG-0006 | **GENERAL_DIRECTOR** | PER-0016 **active** |
| REL-SIBCAR-02 PER-0017 → ORG-0006 | **REPRESENTATIVE** | PER-0017 **active** |

**Explicit exclusion:** Do **not** set ORG-0006 `primary_contact_person_id` until Wave 2C relationship attestation selects operational slot (expected PER-0017 — steward confirms).

---

## 5. Missing evidence register

| ID | Person / topic | Gap | Severity | Mitigation |
|----|----------------|-----|----------|------------|
| **ME-W2C-SIBCAR-01** | PER-0017 | Not named in EV-W1C-CC-01 | Medium *(identity)* | E0 operator attest sufficient for **active** Person; optional future CC supplement |
| **ME-W2C-SIBCAR-02** | PER-0017 | Full patronymic **SAFE UNKNOWN** | Medium | Given name + Telegram sufficient at E0; optional operator supplement |
| **ME-W2C-SIBCAR-03** | PER-0017 | «Business Owner» not CC-backed | Low | Record as operator role signal; **no** OWNER edge |
| **ME-W2C-SIBCAR-04** | PER-0016 | Phone / TG / email **SAFE UNKNOWN** | Low | Not blocking E1 Person attest |
| **ME-W2C-SIBCAR-05** | PER-0016 | Exact director title **SAFE UNKNOWN** | Low | CC «Руководитель» label; operator «General Director» as role signal |
| **ME-W2C-SIBCAR-06** | ORG-0006 | Diadoc / EDO specific signer | Medium *(signatory ops)* | **SAFE UNKNOWN** — do not infer PER-0016 or PER-0017 |
| **ME-W2C-SIBCAR-07** | ORG-0006 | EDO participant id | Low | ME-W1C-03 carry-forward; CC update |
| **ME-W2C-SIBCAR-08** | PER-0017 | Phone / email **SAFE UNKNOWN** | Low | Optional operator supplement |

**Blocking gaps for Person attestation:** **None**

---

## 6. Readiness checklist crosswalk

| Check ID | Wave 2C SIBCAR Person package assessment |
|----------|------------------------------------------|
| W2-S-01 | Duplicate batch for new persons — **yes** (W2C-SIBCAR-D-01..06) |
| W2-S-02 | Homonym review — **yes** — no collision with PER-0001..0015 |
| W2-S-03 | Person vs service account — **yes** — human contacts attested |
| W2-E-01 | E0 path PER-0017 — **yes** |
| W2-E-02 | CC-backed path PER-0016 — **yes** (EV-W1C-CC-01) |
| W2-E-03 | Email-only mint prohibited — **yes** — PER-0017 has name + Telegram |
| W2-I-03 | ORG-0006 endpoint **active** — **yes** |
| W2-R-01 | 2C rel edges pre-identified — **yes** — REL-SIBCAR-01, REL-SIBCAR-02 queued |
| EFV-04 | CC read before conclusions — **yes** |
| CPV-01 | CC inventory cited — **yes** |

---

## 7. Final verdict

### 7.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 2C SIBCAR Person intake cannot start |
| **PARTIALLY READY** | Intake may start with documented blockers |
| **READY FOR WAVE 2C SIBCAR PERSON ATTESTATION** | Full Person intake plan executable under gates |

### 7.2 Assessment

| Criterion | Status |
|-----------|--------|
| Both required persons classified | **Pass** (2/2) |
| ORG-0006 endpoint **active** | **Pass** |
| EV-W1C-CC-01 present and cited | **Pass** |
| Evidence First / Card Presence discipline | **Pass** |
| Operator contacts and statements recorded | **Pass** |
| Diadoc signer not invented | **Pass** — **SAFE UNKNOWN** |
| OWNER edge not invented from «Business Owner» | **Pass** |
| Wave 2C relationships analyzed, not created | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Known gaps enumerated | **Pass** — ME-W2C-SIBCAR-01..08 |

### 7.3 Verdict

```text
READY FOR WAVE 2C SIBCAR PERSON ATTESTATION
```

**Conditions:**

1. Execute **AT-W2C-SIBCAR-01** before **AT-W2C-SIBCAR-02** — CC signatory anchor first.
2. Wave 2C SIBCAR relationship **active** promotion requires both Person records **active** — separate pass.
3. Do **not** attest Diadoc signer without explicit evidence.
4. Do **not** mint OWNER edge from «Business Owner» operator statement.
5. Draft register `proposed` flags **do not substitute** for steward attestation acts.

---

## 8. Post-Wave 2C SIBCAR Person exit criteria

| Criterion | Evidence |
|-----------|----------|
| PER-0016 **active** | Attestation record AT-W2C-SIBCAR-01 |
| PER-0017 **active** | Attestation record AT-W2C-SIBCAR-02 |
| No Person ↔ Person attested | Scope audit |
| Wave 2C relationship queue prepared | REL-SIBCAR-01, REL-SIBCAR-02 listed |
| ME-W2C-SIBCAR-* updated | Steward sign-off |
| ORG-0006 primary_contact | **Deferred** to Wave 2C relationship pass |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) | Canonical roster and analysis |
| [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) | Proposed register rows |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 / LE-0005 active basis |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) | Discovery authority |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | Person §4.2 |

---

*ATLAS Wave 2C SIBCAR Person Attestation v1 — documentation only.*
