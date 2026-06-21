# ATLAS Wave 2 ZPM Person Active Attestation v1

**Status:** **attested** — first official Person active attestation for Wave 2 ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, database export, Wave 2B relationship attestation, Project / Website / Domain entities, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- ORG-0005 ЗПМ Organization: **active** (AT-W1B-01)
- LE-0004 legal entity: **active** (AT-W1B-01)
- Wave 2 ZPM Person Population: **COMPLETE**
- Wave 2 ZPM Person attestation plan verdict: **READY FOR WAVE 2 ZPM PERSON ATTESTATION**

---

# REPORT — ATLAS Wave 2 ZPM Person Active Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W2-ZPM-01** + **AT-W2-ZPM-02** — Active attest  
**Promotion:** PER-0015, PER-0014 — **proposed** → **active**

---

## 1. Pre-check — evidence inventory (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01..03 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04..06.

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists** (filesystem check 2026-06-07).

| # | Filename | Format | Role |
|---|----------|--------|------|
| 1 | `Реквизиты.docx` | DOCX | **Primary Counterparty Card** → **EV-W1B-CC-01** |

**Operator evidence:**

| Ref | Source | Role |
|-----|--------|------|
| **EV-W2-ZPM-OP-01** | Operator mission inputs (2026-06-07) | PER-0014 identity, contacts, operational statements; PER-0015 phone; work acceptance; EDO note |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| CC folder exists | **Pass** |
| Primary Counterparty Card cited | **Pass** — `Реквизиты.docx` → **EV-W1B-CC-01** |
| Operator inputs recorded | **Pass** — **EV-W2-ZPM-OP-01** |
| ORG-0005 endpoint **active** | **Pass** — AT-W1B-01 |
| Reuse prior CC inventory (no new CC required) | **Pass** — CPV-01 satisfied at AT-W1B-01 |

**Primary evidence path:**

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx
```

---

## 2. Identity review — PER-0015 (CC signatory anchor)

**Source:** EV-W1B-CC-01 §19–§24; cross-check LE-0004 `document_signatory`; operator phone EV-W2-ZPM-OP-01.

| Field | Expected (population) | EV-W1B-CC-01 / LE-0004 | Match |
|-------|----------------------|------------------------|-------|
| **Canonical name** | Крюков Александр Сергеевич | §19, §24 — «Директор Крюков Александр Сергеевич»; LE-0004 `document_signatory` identical | **Match** |
| **Role (CC)** | Директор | §19, §24 | **Match** |
| **Role (operator signal)** | Генеральный директор | EV-W2-ZPM-OP-01 | Recorded — CC «Директор» controls legal signatory field |
| **Beneficial owner** | 100% | §20 — Крюков Александр Сергеевич, ИНН 222304520613 (100%) | **Match** |
| **Chief accountant / responsible** | Same subject | §21–§22 | **Match** |
| **Document signatory** | **yes** — LE-0004 | LE-0004 attested AT-W1B-01 | **Match** |
| **Phone (operator)** | +79039573236 | Not in CC org phone block | E0 operator — not blocking |
| **Email / Telegram** | **SAFE UNKNOWN** | Not in CC | No inference |

**Discrepancies:** **None** on identity. Operator title «Генеральный директор» vs CC «Директор» — CC controls legal signatory; operator title recorded as role signal only.

**Verdict:** **Pass** — PER-0015 identity consistent with CC and LE-0004 signatory bind (W2-ZPM-D-02).

---

## 3. Identity review — PER-0014 (operational contact)

**Source:** EV-W2-ZPM-OP-01 only. CC person block silent on Дубинский (EFV-06).

| Field | Expected (population) | EV-W2-ZPM-OP-01 | Match |
|-------|----------------------|-----------------|-------|
| **Canonical name** | Алексей Владимирович Дубинский | Operator-direct full patronymic | **Match** |
| **Aliases** | Алексей Дубинский; Дубинский | Operator short forms | **Accepted** |
| **Role signals (operator)** | зам. директора; исп. директор; техн. директор | Operator statements | Recorded — not employment attestation |
| **Operational contact** | **yes** — primary | «Всю работу веду через него» | **Match** |
| **Document signatory** | **no** | CC names only Крюков | **Match** |
| **Diadoc signer** | **SAFE UNKNOWN** | Operator EDO note — no named signer | No inference |
| **Telegram** | @scrash86 | Operator-confirmed | **Match** |
| **Phone** | +7 913 099 0747 | Operator-confirmed | **Match** |
| **Email** | dav@assum.ru | Operator-confirmed | **Match** — contact pointer only (EFV-01) |
| **CC corroboration** | **None** | EV-W1B-CC-01 — person absent | E0 path sufficient |

**Discrepancies:** **None** on operator-provided identity. CC absence documented — not blocking at E0.

**Verdict:** **Pass** — PER-0014 attested at **E0** operator-direct pattern (analog PER-0004 Triumph operational contact).

---

## 4. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **W2-ZPM-D-01** | vs Wave 2 attested roster PER-0001..0013 | **Distinct** | No |
| **W2-ZPM-D-02** | PER-0015 vs LE-0004 signatory | **Same subject — bind confirmed** | No |
| **W2-ZPM-D-03** | PER-0014 vs CC person lines | **Distinct — CC silent on Дубинский** | No |
| **W2-ZPM-D-04** | PER-0014 vs PER-0015 | **Distinct persons** | No |
| **W2-ZPM-D-05** | Email `dav@assum.ru` vs org CC email `zakaz@bzmp.ru` | **No identity merge** | No |

**Verdict:** **Pass** — duplicate review complete; no blocking duplicates.

---

## 5. Evidence sufficiency and attestation gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **W2-ZPM-EG-01** | ORG-0005 endpoint **active** before Person **active** | **Pass** — AT-W1B-01 |
| **W2-ZPM-EG-02** | CC-backed path PER-0015 — E1 minimum | **Pass** — EV-W1B-CC-01 §19–§24 |
| **W2-ZPM-EG-03** | E0 path PER-0014 — operator identity + multi-channel contacts | **Pass** — EV-W2-ZPM-OP-01 |
| **W2-ZPM-EG-04** | Email-only mint prohibited (W2-E-03) | **Pass** — full name + TG + phone + email |
| **W2-ZPM-EG-05** | Duplicate batch before **active** | **Pass** — W2-ZPM-D-01..05 |
| **W2-ZPM-EG-06** | Human attest mandatory | **Pass** — this act |
| **W2-ZPM-EG-07** | CC signatory anchor before operational contact (AT-W2-ZPM-01 before AT-W2-ZPM-02) | **Pass** — sequence honored |
| **W2-ZPM-EG-08** | Diadoc signer not invented | **Pass** — **SAFE UNKNOWN** |
| **W2-ZPM-EG-09** | Employment status not inferred | **Pass** — role signals only; 2B type review deferred |
| **STOP-EFV-04** | Active while CC contradicts proposal | **Pass** — no contradiction |
| **STOP-CPV-01..03** | Inventory before attest | **Pass** — §1 |

**Readiness checklist crosswalk:**

| Check ID | Assessment |
|----------|------------|
| W2-S-01 | Duplicate batch — **Pass** |
| W2-S-02 | Homonym review — **Pass** |
| W2-S-03 | Person vs service account — **Pass** |
| W2-E-01 | E0 path PER-0014 — **Pass** |
| W2-E-02 | CC-backed path PER-0015 — **Pass** |
| W2-E-03 | Email-only mint prohibited — **Pass** |
| W2-I-03 | ORG-0005 endpoint **active** — **Pass** |
| W2-R-01 | 2B edges pre-identified — **Pass** — queued, not created |
| EFV-04 | CC read before conclusions — **Pass** |
| CPV-01 | CC inventory cited — **Pass** |

**Verdict:** **Pass** — all gates satisfied for Person **active** promotion.

---

## 6. Attestation tranches executed

### 6.1 AT-W2-ZPM-01 — CC signatory (legal anchor)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify ORG-0005 **active** | Steward | AT-W1B-01 | **Done** |
| 2 | Confirm EV-W1B-CC-01 inventory (CPV-01) | Steward | §1 | **Done** |
| 3 | Duplicate scan W2-ZPM-D-01..05 | Steward | §4 | **Done** |
| 4 | Propose PER-0015 with canonical name | Steward | EV-W1B-CC-01 §19–§24 | **Done** |
| 5 | Map to LE-0004 `document_signatory` | Steward | AT-W1B-01 §7.1 | **Done** |
| 6 | Assign **E1**; record operator phone E0 | Steward | EV-W2-ZPM-OP-01 | **Done** |
| 7 | Attest Person **active** | Steward (delegated) | CC signatory discipline | **Done** |
| 8 | Queue 2B: GENERAL_DIRECTOR → ORG-0005 | Steward | REL-ZPM-01 *(not executed here)* | **Queued** |

### 6.2 AT-W2-ZPM-02 — Primary operational contact

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Propose PER-0014 with full patronymic | Steward | EV-W2-ZPM-OP-01 | **Done** |
| 2 | Accept aliases: Алексей Дубинский; Дубинский | Steward | [ALIAS-MODEL](../foundation/ATLAS-ALIAS-MODEL-v1.md) | **Done** |
| 3 | Register contacts (TG, phone, email) | Steward | EV-W2-ZPM-OP-01 | **Done** |
| 4 | Confirm **not** CC signatory; Diadoc signer **SAFE UNKNOWN** | Steward | EFV-06 | **Done** |
| 5 | Assign **E0** | Steward | Operator-direct | **Done** |
| 6 | Attest Person **active** | Steward | Operational contact pattern | **Done** |
| 7 | Queue 2B: REPRESENTATIVE → ORG-0005 | Steward | REL-ZPM-02 *(not executed here)* | **Queued** |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create Person ↔ Organization edges | **Excluded** | Wave 2B-ZPM — separate pass |
| Set ORG-0005 `primary_contact_person_id` | **Excluded** | Deferred to Wave 2B |
| Assign Diadoc signer | **Excluded** | **SAFE UNKNOWN** — no evidence |
| Infer employment status | **Excluded** | Operator scope |
| Create Project / Website / Domain | **Excluded** | Operator scope |
| Create new entities | **Excluded** | Operator scope |

---

## 7. Attested entity records

### 7.1 PER-0015 — Крюков Александр Сергеевич

| Field | Value |
|-------|-------|
| **person_id** | PER-0015 |
| **canonical_name** | Крюков Александр Сергеевич |
| **primary_organization** | ORG-0005 ЗПМ *(display primary; relationship deferred — Wave 2B)* |
| **population_slice** | **client-side** |
| **role_signals** | Генеральный директор *(operator)*; Директор *(CC)* |
| **operational_contact** | **sometimes** — work acceptance alongside PER-0014 |
| **document_signatory** | **yes** — LE-0004 CC signatory |
| **contacts** | phone: +79039573236 *(E0 operator)*; email, telegram: **SAFE UNKNOWN** |
| **attestation_basis** | E1 EV-W1B-CC-01 §19–§24; LE-0004 signatory bind W2-ZPM-D-02; beneficial owner 100% §20; duplicate review **Pass** |
| **evidence_tier** | **E1** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | CC beneficial owner 100%; chief accountant same subject §21–§22. Wave 2B queue: REL-ZPM-01 GENERAL_DIRECTOR → ORG-0005. |

### 7.2 PER-0014 — Алексей Владимирович Дубинский

| Field | Value |
|-------|-------|
| **person_id** | PER-0014 |
| **canonical_name** | Алексей Владимирович Дубинский |
| **primary_organization** | ORG-0005 ЗПМ *(display primary; relationship deferred — Wave 2B)* |
| **population_slice** | **client-side** |
| **role_signals** | зам. директора; исп. директор; техн. директор *(operator — not employment attestation)* |
| **operational_contact** | **yes** — primary for Polygon vendor work on ЗПМ account |
| **document_signatory** | **no** |
| **contacts** | TG: @scrash86; phone: +7 913 099 0747; email: dav@assum.ru |
| **attestation_basis** | E0 EV-W2-ZPM-OP-01; operator-direct identity + multi-channel contacts; **not** named in EV-W1B-CC-01; duplicate review **Pass** |
| **evidence_tier** | **E0** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Diadoc signer **SAFE UNKNOWN**. Email domain assum.ru — contact only. Wave 2B queue: REL-ZPM-02 REPRESENTATIVE → ORG-0005 *(EMPLOYEE review at 2B)*. |

### 7.3 Alias disposition (proposed → active)

| person_id | alias | alias_type | evidence_ref | prior state | attested state |
|-----------|-------|------------|--------------|-------------|----------------|
| PER-0014 | Алексей Дубинский | short / informal | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |
| PER-0014 | Дубинский | surname fragment | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |
| PER-0015 | — | — | — | — | — |

### 7.4 Contact disposition (proposed → active)

| person_id | channel | value | evidence_ref | prior state | attested state |
|-----------|---------|-------|--------------|-------------|----------------|
| PER-0014 | telegram | @scrash86 | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |
| PER-0014 | phone | +7 913 099 0747 | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |
| PER-0014 | email | dav@assum.ru | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |
| PER-0015 | phone | +79039573236 | E0 EV-W2-ZPM-OP-01 | **proposed** | **active** |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-ZPM-01 PER-0015 → ORG-0005 GENERAL_DIRECTOR | **Queued** — Wave 2B-ZPM |
| REL-ZPM-02 PER-0014 → ORG-0005 REPRESENTATIVE | **Queued** — Wave 2B-ZPM |
| ORG-0005 `primary_contact_person_id` | **Deferred** — Wave 2B |
| Diadoc / EDO specific signer | **SAFE UNKNOWN** — not inferred |
| Employment status (EMPLOYEE vs REPRESENTATIVE) | **Deferred** — Wave 2B type review |
| Person ↔ Person edges | **Not created** |
| Project / Website / Domain entities | **Not created** |
| Commercial relationships (Wave 6+) | **Not created** |
| Foundation documents | **Not modified** |
| New entities | **Not created** |

---

## 9. Residual gaps (non-blocking)

| ID | Person / topic | Gap | Severity | Mitigation |
|----|----------------|-----|----------|------------|
| **ME-W2-ZPM-01** | PER-0014 | Not named in EV-W1B-CC-01 | Medium *(identity)* | E0 operator attest **sufficient** — **active** achieved; optional future CC supplement |
| **ME-W2-ZPM-02** | PER-0014 | Role titles not CC-backed | Low | Record as operator role signals; decide EMPLOYEE vs REPRESENTATIVE at 2B |
| **ME-W2-ZPM-03** | PER-0015 | Phone +79039573236 not in CC | Low | E0 operator contact — attested |
| **ME-W2-ZPM-04** | PER-0015 | Email, Telegram **SAFE UNKNOWN** | Low | Optional operator supplement |
| **ME-W2-ZPM-05** | ORG-0005 | Diadoc / EDO specific signer | Medium *(signatory ops)* | **SAFE UNKNOWN** — do not infer PER-0014 or PER-0015 |
| **ME-W2-ZPM-06** | ORG-0005 | EDO participant id | Low | ME-W1B-05 carry-forward; CC update |
| **ME-W2-ZPM-07** | PER-0014 | Email domain assum.ru vs org bzpm.ru | Low | Contact pointer only — EFV-01 |

**Blocking gaps remaining:** **None**

---

## 10. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 2 Person records only |
| No Foundation modification | **Pass** |
| No Wave 1 / Wave 2 core record modification | **Pass** |
| ORG-0005 endpoint **active** honored | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| EFV-01 alias discipline | **Pass** |
| CPV-01 inventory discipline | **Pass** |
| Diadoc signer not invented | **Pass** |
| Employment status not inferred | **Pass** |
| No Person ↔ Organization edges created | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 11. Attestation verdict

```text
READY FOR WAVE 2B ZPM RELATIONSHIP POPULATION
```

**Conditions met:**

1. PER-0015 **active** — CC signatory anchor attested at **E1** under EV-W1B-CC-01; bound to LE-0004 `document_signatory`.
2. PER-0014 **active** — operational contact attested at **E0** under EV-W2-ZPM-OP-01.
3. Aliases (2 rows) and contacts (4 rows) promoted to **active**.
4. Pre-check inventory, identity review, duplicate review, and evidence gates — **all Pass**.
5. Wave 2B candidates REL-ZPM-01, REL-ZPM-02 **queued** — prerequisites now satisfied (both Person endpoints **active**; ORG-0005 **active**).

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 2 ZPM PERSON ATTESTATION** | [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) §7 | **Superseded** — both Person records now **active** |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **PARTIALLY READY** | Both persons attested — no deferrals |
| **NO EVIDENCE FOUND** | EV-W1B-CC-01 and EV-W2-ZPM-OP-01 present |

**Downstream:** Execute Wave 2B-ZPM relationship population in a **separate pass** — REL-ZPM-01, REL-ZPM-02.

---

## 12. Attestation results summary

| person_id | canonical_name | prior state | attested state | evidence_tier | tranche |
|-----------|----------------|-------------|----------------|---------------|---------|
| PER-0015 | Крюков Александр Сергеевич | **proposed** | **active** | **E1** | AT-W2-ZPM-01 |
| PER-0014 | Алексей Владимирович Дубинский | **proposed** | **active** | **E0** | AT-W2-ZPM-02 |

**Promotion count:** **2 / 2** Person records → **active**  
**Relationships created:** **0**  
**New entities created:** **0**

---

## 13. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
        │
        ├── Wave 2 Person (PER-0001..0013) ──► AT-W2-01..05 (COMPLETE)
        │
        └── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (THIS ACT)
                    │
                    └──► Wave 2B-ZPM Relationship Population (NEXT)
```

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Proposed register rows |
| [ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ATTESTATION-v1.md) | Attestation sequence (superseded §7 verdict) |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 / LE-0004 active basis |
| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | EV-W1B-CC-01 extraction |
| [ATLAS-WAVE2-ATTESTATION-v1.md](ATLAS-WAVE2-ATTESTATION-v1.md) | Prior Wave 2 core Person attestation pattern |

---

*ATLAS Wave 2 ZPM Person Active Attestation v1 — documentation only.*
