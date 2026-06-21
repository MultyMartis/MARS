# ATLAS Wave 2C SIBCAR Person Active Attestation v1

**Status:** **attested** — first official Person active attestation for Wave 2C SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, database export, Wave 2C relationship attestation, Project / Website / Domain entities, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 2 core Person attestation (PER-0001..0013): **COMPLETE**
- Wave 2 ZPM Person attestation (PER-0014, PER-0015): **COMPLETE**
- ORG-0006 SIBCAR Organization: **active** (AT-W1C-01)
- LE-0005 legal entity: **active** (AT-W1C-01)
- Wave 2C SIBCAR Person Population: **COMPLETE**
- Wave 2C SIBCAR Person attestation plan verdict: **READY FOR WAVE 2C SIBCAR PERSON ATTESTATION**

---

# REPORT — ATLAS Wave 2C SIBCAR Person Active Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W2C-SIBCAR-01** + **AT-W2C-SIBCAR-02** — Active attest  
**Promotion:** PER-0016, PER-0017 — **proposed** → **active**

---

## 1. Pre-check — evidence inventory (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01..03 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04..06.

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\` — **exists** (filesystem check 2026-06-07).

| # | Filename | Format | Role |
|---|----------|--------|------|
| 1 | `Реквизиты.docx` | DOCX | **Primary Counterparty Card** → **EV-W1C-CC-01** |

**Operator evidence:**

| Ref | Source | Role |
|-----|--------|------|
| **EV-W2C-SIBCAR-OP-01** | Operator mission inputs (2026-06-07) | PER-0017 identity (Хаял), Telegram @Khayal8888, operational role; two-person model |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| CC folder exists | **Pass** |
| Primary Counterparty Card cited | **Pass** — `Реквизиты.docx` → **EV-W1C-CC-01** |
| Operator inputs recorded | **Pass** — **EV-W2C-SIBCAR-OP-01** |
| ORG-0006 endpoint **active** | **Pass** — AT-W1C-01 |
| Reuse prior CC inventory (no new CC required) | **Pass** — CPV-01 satisfied at AT-W1C-01 |

**Primary evidence path:**

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx
```

---

## 2. Identity review — PER-0016 (CC signatory anchor)

**Source:** EV-W1C-CC-01 §21–§24; cross-check LE-0005 `document_signatory`.

| Field | Expected (population) | EV-W1C-CC-01 / LE-0005 | Match |
|-------|----------------------|------------------------|-------|
| **Canonical name** | Карандашов Максим Петрович | §22 — signatory; §24 — chief accountant | **Match** |
| **Role (CC)** | Руководитель; Главный бухгалтер | §21–§24 | **Match** |
| **Role (operator signal)** | General Director | EV-W2C-SIBCAR-OP-01 *(implicit via CC role)* | Recorded — CC «Руководитель» controls legal signatory field |
| **Document signatory** | **yes** — LE-0005 | LE-0005 attested AT-W1C-01 | **Match** |
| **Operational contact** | **no** | PER-0017 is primary | **Match** |
| **Phone / TG / email** | **SAFE UNKNOWN** | Not in CC | No inference |

**Discrepancies:** **None** on identity. Operator title «General Director» vs CC «Руководитель» — CC controls legal signatory; operator title recorded as role signal only.

**Verdict:** **Pass** — PER-0016 identity consistent with CC and LE-0005 signatory bind (W2C-SIBCAR-D-03).

---

## 3. Identity review — PER-0017 (operational contact)

**Source:** EV-W2C-SIBCAR-OP-01 only. CC person block silent on Хаял (EFV-06).

| Field | Expected (population) | EV-W2C-SIBCAR-OP-01 | Match |
|-------|----------------------|---------------------|-------|
| **Canonical name** | Хаял | Operator-direct given name | **Match** |
| **Full patronymic / surname** | **SAFE UNKNOWN** | Not provided | Documented — not blocking |
| **Role signals (operator)** | Primary Operational Contact; Business Owner | Operator statements | Recorded — **no** OWNER edge |
| **Operational contact** | **yes** — primary | Operator confirmation | **Match** |
| **Document signatory** | **no** | CC names only Карандашов | **Match** |
| **Diadoc signer** | **SAFE UNKNOWN** | No named signer | No inference |
| **Telegram** | @Khayal8888 | Operator-confirmed | **Match** |
| **Phone / email** | **SAFE UNKNOWN** | Not provided | No inference |
| **CC corroboration** | **None** | EV-W1C-CC-01 — person absent | E0 path sufficient |

**Discrepancies:** **None** on operator-provided identity. CC absence documented — not blocking at E0.

**Verdict:** **Pass** — PER-0017 attested at **E0** operator-direct pattern (analog PER-0014 ZPM operational contact).

---

## 4. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **W2C-SIBCAR-D-01** | vs Wave 2 attested roster PER-0001..0015 | **Distinct** | No |
| **W2C-SIBCAR-D-02** | Хаял vs Wave 2 roster | **Distinct** | No |
| **W2C-SIBCAR-D-03** | PER-0016 vs LE-0005 signatory | **Same subject — bind confirmed** | No |
| **W2C-SIBCAR-D-04** | PER-0017 vs CC person lines | **Distinct — CC silent on Хаял** | No |
| **W2C-SIBCAR-D-05** | PER-0016 vs PER-0017 | **Distinct persons** | No |
| **W2C-SIBCAR-D-06** | info_sibcar@mail.ru vs Person rows | **No identity merge** | No |

**Verdict:** **Pass** — duplicate review complete; no blocking duplicates.

---

## 5. Evidence sufficiency and attestation gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **W2C-SIBCAR-EG-01** | ORG-0006 endpoint **active** before Person **active** | **Pass** — AT-W1C-01 |
| **W2C-SIBCAR-EG-02** | CC-backed path PER-0016 — E1 minimum | **Pass** — EV-W1C-CC-01 §21–§24 |
| **W2C-SIBCAR-EG-03** | E0 path PER-0017 — operator identity + Telegram | **Pass** — EV-W2C-SIBCAR-OP-01 |
| **W2C-SIBCAR-EG-04** | Email-only mint prohibited (W2-E-03) | **Pass** — given name + Telegram |
| **W2C-SIBCAR-EG-05** | Duplicate batch before **active** | **Pass** — W2C-SIBCAR-D-01..06 |
| **W2C-SIBCAR-EG-06** | Human attest mandatory | **Pass** — this act |
| **W2C-SIBCAR-EG-07** | CC signatory anchor before operational contact | **Pass** — AT-W2C-SIBCAR-01 before AT-W2C-SIBCAR-02 |
| **W2C-SIBCAR-EG-08** | Diadoc signer not invented | **Pass** — **SAFE UNKNOWN** |
| **W2C-SIBCAR-EG-09** | OWNER edge not invented from «Business Owner» | **Pass** |
| **W2C-SIBCAR-EG-10** | Employment status not inferred | **Pass** — role signals only; 2C rel type deferred |
| **STOP-EFV-04** | Active while CC contradicts proposal | **Pass** — no contradiction |
| **STOP-CPV-01..03** | Inventory before attest | **Pass** — §1 |

**Verdict:** **Pass** — all gates satisfied for Person **active** promotion.

---

## 6. Attestation tranches executed

### 6.1 AT-W2C-SIBCAR-01 — CC signatory (legal anchor)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify ORG-0006 **active** | Steward | AT-W1C-01 | **Done** |
| 2 | Confirm EV-W1C-CC-01 inventory (CPV-01) | Steward | §1 | **Done** |
| 3 | Duplicate scan W2C-SIBCAR-D-01..06 | Steward | §4 | **Done** |
| 4 | Propose PER-0016 with canonical name | Steward | EV-W1C-CC-01 §21–§24 | **Done** |
| 5 | Map to LE-0005 `document_signatory` | Steward | AT-W1C-01 §2.1 | **Done** |
| 6 | Assign **E1** | Steward | CC signatory discipline | **Done** |
| 7 | Attest Person **active** | Steward (delegated) | CC signatory discipline | **Done** |
| 8 | Queue 2C rel: GENERAL_DIRECTOR → ORG-0006 | Steward | REL-SIBCAR-01 *(not executed here)* | **Queued** |

### 6.2 AT-W2C-SIBCAR-02 — Primary operational contact

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Propose PER-0017 with canonical name Хаял | Steward | EV-W2C-SIBCAR-OP-01 | **Done** |
| 2 | Record patronymic **SAFE UNKNOWN** | Steward | EFV-06 | **Done** |
| 3 | Register Telegram @Khayal8888 | Steward | EV-W2C-SIBCAR-OP-01 | **Done** |
| 4 | Confirm **not** CC signatory; «Business Owner» = role signal only | Steward | ZPM precedent | **Done** |
| 5 | Assign **E0** | Steward | Operator-direct | **Done** |
| 6 | Attest Person **active** | Steward | Operational contact pattern | **Done** |
| 7 | Queue 2C rel: REPRESENTATIVE → ORG-0006 | Steward | REL-SIBCAR-02 *(not executed here)* | **Queued** |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create Person ↔ Organization edges | **Excluded** | Wave 2C SIBCAR relationship pass — separate package |
| Set ORG-0006 `primary_contact_person_id` | **Excluded** | Deferred to Wave 2C relationship attestation |
| Mint OWNER edge | **Excluded** | Operator scope — «Business Owner» is role signal only |
| Assign Diadoc signer | **Excluded** | **SAFE UNKNOWN** — no evidence |
| Create Project / Website / Domain | **Excluded** | Operator scope |
| Create new entities beyond PER-0016/0017 | **Excluded** | Operator scope |

---

## 7. Attested entity records

### 7.1 PER-0016 — Карандашов Максим Петрович

| Field | Value |
|-------|-------|
| **person_id** | PER-0016 |
| **canonical_name** | Карандашов Максим Петрович |
| **primary_organization** | ORG-0006 SIBCAR *(display primary; relationship deferred — Wave 2C relationship pass)* |
| **population_slice** | **client-side** |
| **role_signals** | General Director *(operator)*; Руководитель *(CC)*; Главный бухгалтер *(CC)* |
| **operational_contact** | **no** — PER-0017 is primary |
| **document_signatory** | **yes** — LE-0005 CC signatory |
| **contacts** | phone / TG / email: **SAFE UNKNOWN** |
| **attestation_basis** | E1 EV-W1C-CC-01 §21–§24; LE-0005 signatory bind W2C-SIBCAR-D-03; chief accountant §23–§24; duplicate review **Pass** |
| **evidence_tier** | **E1** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Wave 2C rel queue: REL-SIBCAR-01 GENERAL_DIRECTOR → ORG-0006. |

### 7.2 PER-0017 — Хаял

| Field | Value |
|-------|-------|
| **person_id** | PER-0017 |
| **canonical_name** | Хаял |
| **primary_organization** | ORG-0006 SIBCAR *(display primary; relationship deferred — Wave 2C relationship pass)* |
| **population_slice** | **client-side** |
| **role_signals** | Primary Operational Contact; Business Owner *(operator signal — not OWNER edge)* |
| **operational_contact** | **yes** — primary for Polygon vendor work on SIBCAR account |
| **document_signatory** | **no** |
| **contacts** | TG: @Khayal8888; phone / email: **SAFE UNKNOWN** |
| **attestation_basis** | E0 EV-W2C-SIBCAR-OP-01; operator-direct identity + Telegram; **not** named in EV-W1C-CC-01; duplicate review **Pass** |
| **evidence_tier** | **E0** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Full patronymic **SAFE UNKNOWN**. Diadoc signer **SAFE UNKNOWN**. Wave 2C rel queue: REL-SIBCAR-02 REPRESENTATIVE → ORG-0006. |

### 7.3 Contact disposition (proposed → active)

| person_id | channel | value | evidence_ref | prior state | attested state |
|-----------|---------|-------|--------------|-------------|----------------|
| PER-0017 | telegram | @Khayal8888 | E0 EV-W2C-SIBCAR-OP-01 | **proposed** | **active** |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-SIBCAR-01 PER-0016 → ORG-0006 GENERAL_DIRECTOR | **Queued** — Wave 2C SIBCAR relationship pass |
| REL-SIBCAR-02 PER-0017 → ORG-0006 REPRESENTATIVE | **Queued** — Wave 2C SIBCAR relationship pass |
| ORG-0006 `primary_contact_person_id` | **Deferred** — Wave 2C relationship attestation |
| PER-0017 → ORG-0006 **OWNER** | **Excluded** — «Business Owner» is role signal only |
| Diadoc / EDO specific signer | **SAFE UNKNOWN** — not inferred |
| Person ↔ Person edges | **Not created** |
| Project / Website / Domain entities | **Not created** |
| Commercial relationships | **Not created** |
| Foundation documents | **Not modified** |

---

## 9. Residual gaps (non-blocking)

| ID | Person / topic | Gap | Severity | Mitigation |
|----|----------------|-----|----------|------------|
| **ME-W2C-SIBCAR-01** | PER-0017 | Not named in EV-W1C-CC-01 | Medium *(identity)* | E0 operator attest **sufficient** — **active** achieved |
| **ME-W2C-SIBCAR-02** | PER-0017 | Full patronymic **SAFE UNKNOWN** | Medium | Optional operator supplement |
| **ME-W2C-SIBCAR-04** | PER-0016 | Person contacts absent | Low | Optional operator supplement |
| **ME-W2C-SIBCAR-05** | PER-0016 | Exact director title **SAFE UNKNOWN** | Low | CC «Руководитель» label |
| **ME-W2C-SIBCAR-06** | ORG-0006 | Diadoc / EDO specific signer | Medium *(signatory ops)* | **SAFE UNKNOWN** |
| **ME-W2C-SIBCAR-08** | PER-0017 | Phone / email **SAFE UNKNOWN** | Low | Optional operator supplement |

**Blocking gaps remaining:** **None**

---

## 10. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 2 Person records only |
| No Foundation modification | **Pass** |
| No Wave 1 / Wave 2 / Wave 2 ZPM record modification | **Pass** |
| ORG-0006 endpoint **active** honored | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| OWNER edge not invented | **Pass** |
| No Person ↔ Organization edges created | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 11. Attestation verdict

```text
READY FOR WAVE 2C SIBCAR RELATIONSHIP POPULATION
```

**Conditions met:**

1. PER-0016 **active** — CC signatory anchor attested at **E1** under EV-W1C-CC-01; bound to LE-0005 `document_signatory`.
2. PER-0017 **active** — operational contact attested at **E0** under EV-W2C-SIBCAR-OP-01.
3. Contact row (1) promoted to **active**.
4. Pre-check inventory, identity review, duplicate review, and evidence gates — **all Pass**.
5. Wave 2C candidates REL-SIBCAR-01, REL-SIBCAR-02 **queued** — prerequisites now satisfied (both Person endpoints **active**; ORG-0006 **active**).

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 2C SIBCAR PERSON ATTESTATION** | [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) §7 | **Superseded** — both Person records now **active** |

**Downstream:** Execute Wave 2C SIBCAR relationship population in a **separate pass** — REL-SIBCAR-01, REL-SIBCAR-02.

---

## 12. Attestation results summary

| person_id | canonical_name | prior state | attested state | evidence_tier | tranche |
|-----------|----------------|-------------|----------------|---------------|---------|
| PER-0016 | Карандашов Максим Петрович | **proposed** | **active** | **E1** | AT-W2C-SIBCAR-01 |
| PER-0017 | Хаял | **proposed** | **active** | **E0** | AT-W2C-SIBCAR-02 |

**Promotion count:** **2 / 2** Person records → **active**  
**Relationships created:** **0**  
**New entities created:** **0**

---

## 13. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1C SIBCAR (ORG-0006, LE-0005) ──► AT-W1C-01 (COMPLETE)
        │
        ├── Wave 2 Person (PER-0001..0013) ──► AT-W2-01..05 (COMPLETE)
        │
        ├── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (COMPLETE)
        │
        └── Wave 2C SIBCAR Person (PER-0016, PER-0017) ──► AT-W2C-SIBCAR-01..02 (THIS ACT)
                    │
                    └──► Wave 2C SIBCAR Relationship Population (NEXT)
```

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-REGISTER-v1.md) | Register rows |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ATTESTATION-v1.md) | Attestation sequence (superseded §7 verdict) |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 / LE-0005 active basis |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | EV-W1C-CC-01 extraction |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) | Discovery authority |

---

*ATLAS Wave 2C SIBCAR Person Active Attestation v1 — documentation only.*
