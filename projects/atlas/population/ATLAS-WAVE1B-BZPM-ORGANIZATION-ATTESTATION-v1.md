# ATLAS Wave 1B BZPM Organization Attestation v1

**Status:** **documented** — Wave 1B BZPM Organization attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md)  
**Is not:** attestation runtime, signature platform, Person population, Wave 2B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Population verdict: **PARTIALLY READY** (proposed ORG-0005 documented; CC pending)

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 1B Organization **BZPM**, минимальные evidence gates, readiness, missing evidence, downstream queue (Person / Project / Website), и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 1B attestation scope

| In scope | Out of scope |
|----------|--------------|
| Organization ORG-0005 → **proposed** / **active** | Person entities |
| Legal entity LE-0004 proposal linkage | Person ↔ Organization edges (Wave 2B-BZPM) |
| Alias register attestation intent | Project / Website / Domain entities |
| Evidence tier assignment | CLIENT_OF ORG-0005 → ORG-0001 (Wave 6+) |
| Duplicate review sign-off | Foundation amendments |
| Wave 2 BZPM **queue preparation** | Counterparty Card file creation |
| Second-client model validation | Runtime / API / database |

---

## 3. Attestation readiness

| org_id | Organization | Target state | Min tier (W1-B) | Readiness | Blocker |
|--------|--------------|--------------|-----------------|-----------|---------|
| ORG-0005 | BZPM | **active** | **E1** (CC path) | **Not ready** | ME-W1B-01, ME-W1B-02 |
| ORG-0005 | BZPM | **proposed** | E1 operational | **Ready** | — *(population-only)* |

**Readiness legend:**

- **Ready (proposed)** — steward may record **proposed** Organization from operational E1 corroboration.
- **Not ready (active)** — W1-B **active** attest blocked until CC intake and legal entity field review.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W1B-00 — Population record (current state)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify Wave 1 ORG-0001..0004 **active** | Steward | Wave 1 exit | **Done** |
| 2 | Duplicate batch W1B-D-01..06 | Steward | Population §8 | **Done** |
| 3 | Propose ORG-0005 canonical name **BZPM** | Steward | EV-W1B-04, EV-W1B-05 | **Done** |
| 4 | Register alias cluster (SIBCAR, Автосалон СИБКАР) | Steward | EV-W1B-01..03 | **Done** |
| 5 | Bind LE-0004 placeholder — fields SAFE UNKNOWN | Steward | ME-W1B-02 | **Done** |
| 6 | Record Organization **proposed** at E1 operational | Steward | Population §7 | **Done** |

### 4.2 Tranche AT-W1B-01 — Active attest (blocked — pending operator)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Obtain Counterparty Card — `bzpm\` external folder | Operator | [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | **Pending** |
| 2 | CC intake → extract legal name, INN, OGRN | Steward | CC model §5 | **Pending** |
| 3 | Duplicate review on legal name / INN | Steward | Identity governance | **Pending** |
| 4 | Propose / attest LE-0004 fields from CC | Steward | LegalEntities discipline | **Pending** |
| 5 | Assign E1 CC tier; resolve ME-W1B-01..02 | Steward | OAR-01 | **Pending** |
| 6 | Attest Organization **active** | Steward (delegated) or Owner | W1-EXEC-04 analog | **Pending** |
| 7 | Queue Wave 2 BZPM Person candidates from CC contacts | Steward | CC-PER-01 | **Pending** |

**STOP-W1-04 analog:** Do **not** attest ORG-0005 **active** without E1+ CC evidence for W1-B external client.

---

## 5. Evidence gates

| Gate ID | Rule | ORG-0005 status |
|---------|------|-----------------|
| **W1B-EG-01** | W1-B minimum E1 at **active** | **Fail** — CC absent |
| **W1B-EG-02** | CC preferred path when obtainable (OAR-01) | **Fail** — CC not placed |
| **W1B-EG-03** | No contract/invoice primary (OAR-BAN-01) | **Pass** |
| **W1B-EG-04** | No hostname-only org (OAR-BAN-03) | **Pass** |
| **W1B-EG-05** | Duplicate batch before **active** (W1-EXEC-01) | **Pass** |
| **W1B-EG-06** | Human attest mandatory (OAR-HUM-01) | **Pending** active tranche |
| **W1B-EG-07** | LE critical fields reviewed before org **active** | **Fail** |

---

## 6. Missing evidence register

| ID | Topic | Severity | Mitigation |
|----|-------|----------|------------|
| **ME-W1B-01** | Counterparty Card absent | **Blocking** | Operator places CC in external `bzpm\` folder |
| **ME-W1B-02** | Legal entity requisites unknown | **Blocking** | CC intake → LE-0004 |
| **ME-W1B-03** | Production public URL | Low | Wave 4 Website population |
| **ME-W1B-04** | BZPM acronym expansion | Low | Steward note at CC review |
| **ME-W1B-05** | EDO / Diadoc participant id | Low | CC or expansion wave |

**Blocking gaps:** ME-W1B-01, ME-W1B-02.

---

## 7. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** |
| No Foundation modification | **Pass** |
| No Wave 1 record modification | **Pass** |
| W1-B acquisition rules followed | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| Alias model — no parallel org from SIBCAR | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 8. Downstream readiness (post-attestation)

### 8.1 Wave 2 BZPM Person Population

| Prerequisite | Status |
|--------------|--------|
| ORG-0005 **active** | **Not met** |
| CC contact lines for Person proposals | **Not met** |
| Duplicate review for named contacts | **Pending** |

### 8.2 Wave 3 / 4 / 5 / 6 candidates

| Wave | Candidate | Prerequisite |
|------|-----------|--------------|
| Wave 3 | PRJ-* BZPM / SITE-001 support | ORG-0005 **active** |
| Wave 4 | WEB-* sibcar / production URL | ORG-0005 **active** |
| Wave 5 | DOM-* production registrant | Wave 4 + registrar E1 |
| Wave 6+ | REL-* CLIENT_OF ORG-0005 → ORG-0001 | ORG-0005 **active** + commercial review |

---

## 9. Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Population or duplicate review failed |
| **PARTIALLY READY** | Population complete; **active** attest and Wave 2 blocked on CC |
| **READY FOR WAVE 2 BZPM PERSON POPULATION** | ORG-0005 **active**; Person queue prepared |

---

## 10. Verdict

```text
PARTIALLY READY
```

**Conditions:**

1. **Proposed** ORG-0005 population and duplicate review — **complete**; second-client model validation **succeeded**.
2. **Active** attestation — **not executed**; blocked on ME-W1B-01 (Counterparty Card) and ME-W1B-02 (legal entity).
3. Wave 2 BZPM Person Population — **not authorized** until AT-W1B-01 completes with Organization **active**.
4. Operator action required: place BZPM Counterparty Card in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\`; notify steward.

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | Population objective met; no D1 duplicate; model fits existing Organization class |
| **READY FOR WAVE 2 BZPM PERSON POPULATION** | ORG-0005 remains **proposed**; no attested Person endpoints |

---

## 11. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ▼
Wave 1B BZPM Population (COMPLETE — proposed ORG-0005)
        │
        ▼
Wave 1B BZPM Attestation plan (THIS PACKAGE) ──► PARTIALLY READY
        │
        ▼
AT-W1B-01 (PENDING — CC intake) ──► ORG-0005 active
        │
        ▼
Wave 2 BZPM Person Population (FUTURE)
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) | Population plan + REPORT |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | Register row |
| [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) | W1-B Triumph exemplar |
| [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) | W1-B CC path |

---

*ATLAS Wave 1B BZPM Organization Attestation v1 — documentation only.*
