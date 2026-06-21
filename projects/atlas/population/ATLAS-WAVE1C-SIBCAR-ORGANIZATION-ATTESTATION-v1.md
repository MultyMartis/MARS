# ATLAS Wave 1C SIBCAR Organization Attestation v1

**Status:** **documented** — Wave 1C SIBCAR Organization attestation sequence, evidence gates, readiness verdict.  
**Supersession:** Organization lifecycle authority for ORG-0006 / LE-0005 — [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) (**AT-W1C-01**, attested 2026-06-06). This document retains the **sequence plan** for lineage; §4.2 and §10 pre-execution verdict **superseded** for lifecycle state.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md)  
**Is not:** attestation runtime, signature platform, Person population, Wave 2 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1 Attestation: **COMPLETE**
- Wave 1B BZPM (ORG-0005): **proposed** — distinct from SIBCAR per identity correction
- Counterparty Card SIBCAR: **present** at `sibcar\` external folder

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 1C Organization **SIBCAR**, минимальные evidence gates, readiness, missing evidence, downstream queue (Person / Project / Website), и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 1C attestation scope

| In scope | Out of scope |
|----------|--------------|
| Organization ORG-0006 → **proposed** / **active** | Person entities |
| Legal entity LE-0005 proposal linkage | Person ↔ Organization edges (Wave 2C-SIBCAR) |
| CC-backed alias register attestation intent | Project / Website / Domain entities |
| Evidence tier assignment | CLIENT_OF ORG-0006 → ORG-0001 (Wave 6+) |
| Duplicate review sign-off | Foundation amendments |
| Wave 2 SIBCAR **queue preparation** | Runtime / API / database |
| BZPM ↔ SIBCAR relationship edges | **SAFE UNKNOWN** — no CC bridge |

---

## 3. Attestation readiness

| org_id | Organization | Target state | Min tier (W1-C) | Readiness | Blocker |
|--------|--------------|--------------|-----------------|-----------|---------|
| ORG-0006 | SIBCAR | **active** | **E1** (CC path) | **Ready for steward act** | ME-W1C-01 — human attestation pending |
| ORG-0006 | SIBCAR | **proposed** | E1 CC | **Ready** | — *(population complete)* |
| LE-0005 | ООО «СибКар» | **active** | E1 CC | **Ready for steward act** | Human attestation pending |

**Readiness legend:**

- **Ready (proposed)** — CC intake complete; steward may record **proposed** Organization from E1 CC.
- **Ready for steward act (active)** — CC satisfies W1-C E1 gates; **active** attest awaits qualified human act only.
- **Blocked** — not applicable to CC presence; Wave 2 remains blocked until Organization **active**.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W1C-00 — Population record (current state)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify Wave 1 ORG-0001..0004 **active** | Steward | Wave 1 exit | **Done** |
| 2 | Duplicate batch W1C-D-01..06 | Steward | [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | **Done** |
| 3 | CC intake — extract legal entity facts | Steward | EV-W1C-CC-01 | **Done** |
| 4 | Propose ORG-0006 canonical name **SIBCAR** | Steward | EV-W1C-CC-01 §8, §10 | **Done** |
| 5 | Register CC-backed alias rows | Steward | Register §4 | **Done** |
| 6 | Bind LE-0005 from CC | Steward | EV-W1C-CC-01 | **Done** |
| 7 | Record Organization **proposed** at E1 CC | Steward | Population §7 | **Done** |

### 4.2 Tranche AT-W1C-01 — Active attest (pending steward)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Confirm CC path and extraction accuracy | Steward | EV-W1C-CC-01 | **Pending** |
| 2 | Duplicate review sign-off on INN/OGRN | Steward | W1C-D-01..06 | **Pending** |
| 3 | Attest LE-0005 **active** | Steward | LegalEntities discipline | **Pending** |
| 4 | Attest Organization ORG-0006 **active** | Steward (delegated) or Owner | W1-EXEC-04 analog | **Pending** |
| 5 | Queue Wave 2 SIBCAR Person candidates from CC contacts | Steward | CC-PER-01 | **Pending** |

**STOP-W1-04 analog:** W1-C **active** attest **authorized** — E1+ CC present for external client.

---

## 5. Evidence gates

| Gate ID | Rule | ORG-0006 status |
|---------|------|-----------------|
| **W1C-EG-01** | W1-C minimum E1 at **active** | **Pass** — EV-W1C-CC-01 |
| **W1C-EG-02** | CC preferred path when obtainable (OAR-01) | **Pass** — CC placed |
| **W1C-EG-03** | No contract/invoice primary (OAR-BAN-01) | **Pass** |
| **W1C-EG-04** | No hostname-only org (OAR-BAN-03) | **Pass** |
| **W1C-EG-05** | Duplicate batch before **active** (W1-EXEC-01) | **Pass** |
| **W1C-EG-06** | Human attest mandatory (OAR-HUM-01) | **Pending** |
| **W1C-EG-07** | LE critical fields reviewed before org **active** | **Pass** — CC complete |

---

## 6. Missing evidence register

| ID | Topic | Severity | Mitigation |
|----|-------|----------|------------|
| **ME-W1C-01** | Steward **active** attestation act | **Blocking** for **active** / Wave 2 | Execute AT-W1C-01 |
| **ME-W1C-02** | Production public URL | Low | Wave 4 Website population |
| **ME-W1C-03** | EDO / Diadoc participant id | Low | CC update |
| **ME-W1C-04** | Phone on CC | Low | CC update or Wave 2 |
| **ME-W1C-05** | Corporate domain / website on CC | Low | Wave 4 / 5 |

**Blocking gaps for Wave 2:** ME-W1C-01 only.

---

## 7. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** |
| No Foundation modification | **Pass** |
| No Wave 1 record modification | **Pass** |
| W1-C acquisition rules followed | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| EFV-01 alias discipline | **Pass** — CC-backed aliases only |
| SIBCAR ≠ BZPM split honored | **Pass** — [COR-W1B-05](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 8. Downstream readiness (post-attestation)

### 8.1 Wave 2 SIBCAR Person Population

| Prerequisite | Status |
|--------------|--------|
| ORG-0006 **active** | **Not met** — pending AT-W1C-01 |
| CC contact lines for Person proposals | **Partial** — Карандашов Максим Петрович (EV-W1C-CC-01 §22) |
| Duplicate review for named contacts | **Pending** at Person wave |

### 8.2 Wave 3 / 4 / 5 / 6 candidates

| Wave | Candidate | Prerequisite |
|------|-----------|--------------|
| Wave 3 | PRJ-* SITE-001 / SIBCAR OpenCart support | ORG-0006 **active** |
| Wave 4 | WEB-* sibcar / production URL | ORG-0006 **active** |
| Wave 5 | DOM-* production registrant | Wave 4 + registrar E1 |
| Wave 6+ | REL-* CLIENT_OF ORG-0006 → ORG-0001 | ORG-0006 **active** + commercial review |

---

## 9. Verdict options

| Verdict | Meaning |
|---------|---------|
| **NO EVIDENCE FOUND** | CC folder empty or insufficient |
| **NOT READY** | Population or duplicate review failed |
| **PARTIALLY READY** | Population complete; **active** attest and Wave 2 blocked on steward act |
| **READY FOR WAVE 2 SIBCAR PERSON POPULATION** | ORG-0006 **active**; Person queue prepared |

---

## 10. Verdict

```text
PARTIALLY READY
```

**Conditions:**

1. **Proposed** ORG-0006 population, CC intake, and duplicate review — **complete**.
2. E1 Counterparty Card **EV-W1C-CC-01** satisfies legal-entity critical fields — **active** path unblocked except human attestation.
3. Wave 2 SIBCAR Person Population — **not authorized** until AT-W1C-01 completes with Organization **active**.
4. Steward next step: execute AT-W1C-01 — attest LE-0005 and ORG-0006 **active**; queue Person candidate Карандашов Максим Петрович.

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NO EVIDENCE FOUND** | CC present with INN/OGRN/legal name |
| **NOT READY** | Population and duplicate review succeed |
| **READY FOR WAVE 2 SIBCAR PERSON POPULATION** | ORG-0006 remains **proposed** |

---

## 11. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ▼
Wave 1B BZPM (ORG-0005 proposed) ──► Identity correction (SIBCAR split)
        │
        ▼
Wave 1C SIBCAR Population (THIS TRANCHE) ──► proposed ORG-0006
        │
        ▼
Wave 1C SIBCAR Attestation plan (THIS PACKAGE) ──► PARTIALLY READY
        │
        ▼
AT-W1C-01 (PENDING — steward active attest) ──► ORG-0006 active
        │
        ▼
Wave 2 SIBCAR Person Population (FUTURE)
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | Population plan + REPORT |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | Register row |
| [ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md](ATLAS-SIBCAR-EVIDENCE-VERIFICATION-v1.md) | Evidence verification |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Prior split — COR-W1B-05 fulfilled |

---

*ATLAS Wave 1C SIBCAR Organization Attestation v1 — documentation only.*
