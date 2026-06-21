# ATLAS Wave 4 ZPM Website Attestation v1

**Status:** **documented** — Wave 4 ZPM Website attestation sequence, evidence gates, readiness verdict; **synced** with ZPM Website Model Correction 2026-06-07.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ**  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Domain attestation, Wave 4B-ZPM execution, active attestation act (pending steward).

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01; canonical **ЗПМ** — RN-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- ZPM Website Model Correction: **EXECUTED**
- Population verdict: **READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)**

---

# REPORT — ATLAS Wave 4 ZPM Website Attestation Plan

**Plan date:** 2026-06-07  
**Tranche design:** **AT-W4-ZPM-01** only  
**Target promotion:** WEB-ZPM-01 — **proposed** → **active**  
**Blocked tranche:** AT-W4-ZPM-02 — WEB-ZPM-02 retired (COR-ZPM-WEB-05)

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 4 ZPM Website, минимальные evidence gates, readiness по единственному сайту, duplicate review, SAFE UNKNOWN inventory, candidate relationships для Wave 4B-ZPM, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 4 ZPM attestation scope

| In scope | Out of scope |
|----------|--------------|
| Website entity → **proposed** / **active** | BELONGS_TO Website ↔ Project edges |
| Evidence tier assignment per website | OWNS / OPERATES Organization ↔ Website |
| Single-property model on `bzpm.ru` | Domain entities (Wave 5 ZPM) |
| Lifecycle structural state (no CMS/deploy vocabulary) | PRIMARY_DOMAIN / SECONDARY_DOMAIN (Wave 5B ZPM) |
| Alias registration (display/brand) | Person ↔ Website edges |
| Org/project **candidate** context (display) | REL-0016 CLIENT_OF (Wave 6) |
| Wave 4B-ZPM **queue preparation** | Foundation amendments |
| Identity rule — ORG-0005 **ЗПМ**; BZPM alias only | New Organization mint |
| **WEB-ZPM-02 attestation** | **Blocked** — COR-ZPM-WEB-05 |

Wave 4B-ZPM relationship **active** attestation executes in a **separate pass** after Website endpoint is attested.

---

## 3. Identity rule (binding — pre-attestation)

| Check | Result |
|-------|--------|
| ORG-0005 canonical **ЗПМ** honored | **Pass** — RN-W1B-01 |
| BZPM = alias / domain stem — not separate org | **Pass** |
| No new Organization created | **Pass** |
| EIR-W01 — one Website per `bzpm.ru` property | **Pass** — WEB-ZPM-01 only |
| SIBCAR / SITE-001 excluded | **Pass** — COR-W1B-03 |

---

## 4. Pre-check — evidence inventory (mandatory)

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists** (prior inventory AT-W1B-01).

| # | Ref | Source | Tier | Role |
|---|-----|--------|------|------|
| 1 | **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild | **E0** | WEB-ZPM-01 **active** |
| 2 | **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` delivery | **E0** | **PRJ-0010** — not Website mint |
| 3 | **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 | **E1** | Org anchor; indirect hostname corroboration |
| 4 | **AT-W1B-01** | Wave 1B BZPM active attestation | attestation | ORG-0005 **active** |
| 5 | **AT-W3-ZPM-01** | Wave 3 ZPM project active attestation | attestation | PRJ-0009 **active** |
| 6 | **AT-W3-ZPM-02** | Wave 3 ZPM project active attestation | attestation | PRJ-0010 **deprecated** |
| 7 | **AT-W3B-ZPM-01..02** | Wave 3B ZPM relationship attestation | attestation | REL-ZPM-PJ-01..04 **active** |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| Operator evidence refs recorded | **Pass** — EV-ZPM-OP-ACT-01; EV-ZPM-OP-HIST-01 re-routed |
| CC inventory cited (reuse AT-W1B-01) | **Pass** — EV-W1B-CC-01 |
| ORG-0005 endpoint **active** | **Pass** — AT-W1B-01 |
| PRJ-0009 **active**, PRJ-0010 **deprecated** | **Pass** — AT-W3-ZPM-01..02 |
| Wave 3B ZPM prerequisites met | **Pass** — REL-ZPM-PJ-01..04 |
| SIBCAR/SITE-001 not used as Website evidence | **Pass** — EFV-02; COR-W1B-03 |
| EFV-03 two-phase rule at Project layer | **Pass** — one Website; two Projects |

---

## 5. Website roster (attestation targets)

| website_id | canonical_name | website_kind | target lifecycle | primary_org | primary_project | evidence_tier | readiness |
|------------|----------------|--------------|------------------|-------------|-----------------|---------------|-----------|
| WEB-ZPM-01 | bzpm.ru | corporate *(catalog platform)* | **active** | ORG-0005 ЗПМ | PRJ-0009 | **E0** | **Ready** |

**Retired — not in attestation scope:**

| website_id | disposition | reason |
|------------|-------------|--------|
| WEB-ZPM-02 | **Blocked** — COR-ZPM-WEB-05 | No Website entity to attest |

**Readiness legend:** **Ready** — steward may attest WEB-ZPM-01 to **active** now. **No conditional blockers.**

---

## 6. Lifecycle analysis

| Rule ID | Rule | Application |
|---------|------|-------------|
| **W4-ZPM-LC-01** | Ongoing client property → **active** | WEB-ZPM-01 — catalog platform WIP |
| **W4-ZPM-LC-02** | Completed historical delivery → **deprecated Project** | PRJ-0010 — not Website |
| **W4-ZPM-LC-03** | Same hostname · single Website | WEB-ZPM-01 only — Triumph analog |
| **W4-ZPM-LC-04** | Deprecated project + active website allowed | PRJ-0010 **deprecated** + WEB-ZPM-01 **active** |
| **W4-ZPM-LC-05** | Multi-Project BELONGS_TO on active Website | REL-ZPM-WB-01 + REL-ZPM-WB-03 |
| **W4-ZPM-LC-06** | Forbidden: CMS version, deploy id as lifecycle | LC-BAN-01 — all |
| ~~W4-ZPM-LC-07~~ | ~~P0 active before P1 deprecated~~ | **Obviated** — single Website tranche |

**Verdict:** **Pass** — lifecycle aligned with Wave 3 ZPM Project attestation and operator single-property model.

---

## 7. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-WEB-D-01** | WEB-ZPM-01 vs WEB-ZPM-02 — same hostname | **Fail** — WEB-ZPM-02 retired | No *(resolved)* |
| **ZPM-WEB-D-02** | vs single merged `bzpm.ru` Website | **Pass** — one Website minted | No |
| **ZPM-WEB-D-03** | vs Triumph WEB-0006..0009 | **Distinct org** | No |
| **ZPM-WEB-D-04** | vs SITE-001 / SIBCAR | **Reject** — COR-W1B-03 | No |
| **ZPM-WEB-D-05** | BZPM vs ЗПМ org identity | **Resolved** — alias discipline | No |
| **ZPM-WEB-D-06** | Name collision on «bzpm.ru» | **Resolved** — single property | No |
| **ZPM-WEB-D-07** | WEB-ZPM-* vs WEB-0006 namespace | **Pass** — tranche separation | No |

**Verdict:** **Pass** — one Website; WEB-ZPM-02 rejected.

---

## 8. Evidence basis

| Ref | Tier | Role | Routing |
|-----|------|------|---------|
| **EV-ZPM-OP-ACT-01** | E0 | Operator — current catalog-platform property on `bzpm.ru` | WEB-ZPM-01 |
| **EV-ZPM-OP-HIST-01** | E0 | Operator — historical site delivery ~5y ago | **PRJ-0010**; BELONGS_TO context |
| **EV-W1B-CC-01** | E1 | CC §17 **Bzpm.ru** — org website field | WEB-ZPM-01 corroboration |
| **AT-W1B-01** | attestation | ORG-0005 **active** | Org anchor |
| **AT-W3-ZPM-01** | attestation | PRJ-0009 **active** | WEB-ZPM-01 pairing |
| **AT-W3-ZPM-02** | attestation | PRJ-0010 **deprecated** | Project historical line |
| **AT-W3B-ZPM-01..02** | attestation | REL-ZPM-PJ-01..04 commissioning context | Informational |

**Claim → evidence crosswalk:**

| Claim | Evidence |
|-------|----------|
| Current `bzpm.ru` catalog-platform property — active WIP | EV-ZPM-OP-ACT-01 → WEB-ZPM-01 |
| Historical original site delivery — completed ~5y | EV-ZPM-OP-HIST-01 → PRJ-0010 |
| Org lists corporate website hostname | EV-W1B-CC-01 §17 — corroboration for WEB-ZPM-01 |

---

## 9. Attestation sequence

### 9.1 Tranche AT-W4-ZPM-01 — Sole web property (P0)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0005 **active** (canonical **ЗПМ**) | Steward | AT-W1B-01; RN-W1B-01 |
| 2 | Verify PRJ-0009 **active** (Wave 3 ZPM) | Steward | AT-W3-ZPM-01 |
| 3 | Verify PRJ-0010 **deprecated** (Wave 3 ZPM) | Steward | AT-W3-ZPM-02 |
| 4 | Verify REL-ZPM-PJ-01..04 **active** (Wave 3B ZPM) | Steward | AT-W3B-ZPM-01..02 |
| 5 | Duplicate scan ZPM-WEB-D-01..07 | Steward | Population §9 |
| 6 | Confirm WEB-ZPM-02 **not** attested — COR-ZPM-WEB-05 | Steward | Correction execution |
| 7 | Propose WEB-ZPM-01 canonical name **bzpm.ru** | Steward | EV-ZPM-OP-ACT-01 |
| 8 | Assign website_kind **corporate** *(catalog platform)*; aliases | Steward | Register §5 |
| 9 | Assign **E0**; record org/project display candidates | Steward | Population §5.1 |
| 10 | Attest Website **active** | Steward (delegated) | W4-ZPM-LC-01 |
| 11 | Queue 4B-ZPM: REL-ZPM-WB-01 + REL-ZPM-WB-03 | Steward | Population §10.1 |

### 9.2 Tranche AT-W4-ZPM-02 — BLOCKED

| Step | Action | Status |
|------|--------|--------|
| All | WEB-ZPM-02 attestation | **Blocked** — COR-ZPM-WEB-05; entity retired |

**Not executed in this package (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create BELONGS_TO edges | **Excluded** | Wave 4B-ZPM |
| Create OWNS / OPERATES edges | **Excluded** | Wave 4B-ZPM |
| Create PRIMARY_DOMAIN edges | **Excluded** | Wave 5B ZPM |
| Create DOM-* entities | **Excluded** | Wave 5 ZPM |
| Attest WEB-ZPM-02 | **Blocked** | COR-ZPM-WEB-01..05 |

---

## 10. Evidence sufficiency and attestation gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **W4-ZPM-EG-01** | ORG-0005 **active** before Website **active** | **Pass** — AT-W1B-01 |
| **W4-ZPM-EG-02** | PRJ-0009 **active** before WEB-ZPM-01 **active** | **Pass** — AT-W3-ZPM-01 |
| ~~W4-ZPM-EG-03~~ | ~~PRJ-0010 **deprecated** before WEB-ZPM-02 **deprecated**~~ | **Obviated** — no WEB-ZPM-02 |
| **W4-ZPM-EG-04** | Wave 3B ZPM Project↔Org complete | **Pass** — REL-ZPM-PJ-01..04 |
| **W4-ZPM-EG-05** | E0 structural attest path — client property | **Pass** — WEB-ZPM-01 |
| **W4-ZPM-EG-06** | SIBCAR/SITE-001 excluded (EFV-02) | **Pass** — COR-W1B-03 |
| **W4-ZPM-EG-07** | Single Website mint — EIR-W01 | **Pass** — COR-ZPM-WEB-12 |
| **W4-ZPM-EG-08** | Duplicate batch before attestation | **Pass** — ZPM-WEB-D-01..07 |
| **W4-ZPM-EG-09** | Human attest mandatory | **Pass** — pending steward act |
| **W4-ZPM-EG-10** | WEB-ZPM-02 attestation blocked | **Pass** — COR-ZPM-WEB-05 |
| **W4-ZPM-EG-11** | No relationship edges in this package | **Pass** — scope restriction |
| **W4-ZPM-EG-12** | BZPM ≠ separate Organization | **Pass** — identity rule §3 |

**Verdict:** **Pass** — all gates satisfied for single-Website attestation plan.

---

## 11. Missing evidence register

| ID | Website | Gap | Severity | Mitigation |
|----|---------|-----|----------|------------|
| **ME-W4-ZPM-01** | PRJ-0010 | No contract-dated historical completion | Low | Operator «~5 years» narrative; E0 sufficient |
| **ME-W4-ZPM-02** | WEB-ZPM-01 | BELONGS_TO not yet attested | — | Wave 4B-ZPM by design |
| **ME-W4-ZPM-03** | WEB-ZPM-01 | OWNS edge not yet attested | Low | Wave 4B-ZPM queue |
| **ME-W4-ZPM-04** | WEB-ZPM-01 | PRIMARY_DOMAIN / DOM-* not minted | Low | Wave 5 ZPM |
| **ME-W4-ZPM-05** | WEB-ZPM-01 | Live URL probe timestamp optional | Low | E0 operator path sufficient |

**Blocking gaps remaining:** **None**

---

## 12. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence | Medium | **Resolved** — single Website |
| **SU-W3B-ZPM-01** | Dual BELONGS_TO for same hostname | Medium | **Resolved** — REL-ZPM-WB-01 + REL-ZPM-WB-03 |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Wave 5 ZPM DOM-* |
| **SU-ZPM-PRJ-01** | Historical contract / act dates | Low | PRJ-0010 narrative |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | Wave 6 |
| **SU-W4-ZPM-01** | Live URL probe for `bzpm.ru` | Low | E0 sufficient |
| **SU-W4-ZPM-02** | OWNS on deprecated Website | Low | **Obviated** |
| **SU-W4-ZPM-03** | Single DOM-* vs dual generation | Low | **Resolved** — DOM-* → WEB-ZPM-01 |

---

## 13. Wave 4B-ZPM candidate relationships

**Not attested in Wave 4 ZPM.** Prepared for separate Wave 4B-ZPM population pass.

### 13.1 Website → Project BELONGS_TO

| Draft rel_id | source_website | target_project | prerequisite | readiness |
|--------------|----------------|----------------|--------------|-----------|
| **REL-ZPM-WB-01** | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | WEB-ZPM-01 **active**; PRJ-0009 **active** | **ready** after Website attestation |
| **REL-ZPM-WB-03** | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | WEB-ZPM-01 **active**; PRJ-0010 **deprecated** | **ready** after Website attestation |

**Cancelled:**

| Draft rel_id | Reason |
|--------------|--------|
| **REL-ZPM-WB-02** | COR-ZPM-WEB-06 — WEB-ZPM-02 retired |

### 13.2 Organization → Website OWNS *(deferred)*

| Draft rel_id | source_organization | target_website | Type | prerequisite |
|--------------|---------------------|----------------|------|--------------|
| *(TBD)* | ORG-0005 ЗПМ | WEB-ZPM-01 | **OWNS** | Website **active** |

### 13.3 Explicitly approved (corrected)

| Item | Treatment |
|------|-----------|
| WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** (REL-ZPM-WB-03) | **Approved** — analog REL-0027 |
| ORG-0005 **OWNS** WEB-ZPM-01 only | **Approved** — COR-ZPM-WEB-09 |

---

## 14. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 1 Website record |
| No Foundation modification | **Pass** |
| No Wave 1 / 2 / 2B / 3 / 3B record modification | **Pass** |
| ORG-0005 endpoint **active** honored | **Pass** |
| EIR-W01 single property model | **Pass** |
| EFV-03 at Project layer only | **Pass** |
| Triumph multi-Project BELONGS_TO precedent | **Pass** |
| No relationship edges created | **Pass** |
| No Domain minted | **Pass** |

---

## 15. Final verdict

### 15.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 4 ZPM Website intake cannot start |
| **READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)** | Single Website attestation executable |
| **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION** | Website attestation complete; 4B pass may proceed |

### 15.2 Assessment

| Criterion | Status |
|-----------|--------|
| Required Website classified | **Pass** — WEB-ZPM-01 only |
| WEB-ZPM-02 blocked | **Pass** — COR-ZPM-WEB-05 |
| Single-property model documented | **Pass** — Triumph analog |
| Lifecycle target **active** | **Pass** |
| Org endpoint ORG-0005 **ЗПМ** available | **Pass** |
| Project endpoints PRJ-0009/0010 attested | **Pass** |
| Wave 3B ZPM prerequisites met | **Pass** |
| Evidence paths documented | **Pass** |
| Duplicate review **Pass** | **Pass** |
| Foundation consistency | **Pass** |
| Wave 4B-ZPM candidates prepared | **Pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03 |

### 15.3 Verdict

```text
READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)
```

**Conditions:**

1. Steward executes attestation tranche **AT-W4-ZPM-01** (WEB-ZPM-01 **active**) only.
2. **Do not** execute AT-W4-ZPM-02 — WEB-ZPM-02 retired.
3. Wave 4B-ZPM executes as **separate pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03; REL-ZPM-WB-02 cancelled.
4. ORG-0005 canonical **ЗПМ**; **BZPM** remains historical alias.
5. DOM-* `bzpm.ru` → WEB-ZPM-01 **PRIMARY_DOMAIN** at **Wave 5B ZPM**.

**Supersedes prior verdicts:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| READY FOR WAVE 4 ZPM WEBSITE ATTESTATION (2 websites) | Prior §15.3 | **Superseded** — correction |
| Dual-generation policy ZPM-WEB-POL-01 | Population §6 | **Superseded** |

---

## 16. Attestation results summary *(pending steward act)*

| website_id | canonical_name | prior state | target state | evidence_tier | tranche |
|------------|----------------|-------------|--------------|---------------|---------|
| WEB-ZPM-01 | bzpm.ru | **proposed** | **active** | **E0** | AT-W4-ZPM-01 |
| WEB-ZPM-02 | bzpm.ru (исходная версия) | — | *(not attested)* | — | **Blocked** |

**Promotion count (planned):** **1 / 1** Website record  
**Active target:** **1** (WEB-ZPM-01)  
**Deprecated Website target:** **0**  
**Relationships created:** **0**  
**Domain entities created:** **0**

---

## 17. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
        │         └── RN-W1B-01 canonical **ЗПМ**
        │
        ├── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 2B ZPM Relationship (REL-ZPM-01..02) ──► AT-W2B-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 3 ZPM Project (PRJ-0009, PRJ-0010) ──► AT-W3-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 3B ZPM Project Relationship (REL-ZPM-PJ-01..04) ──► AT-W3B-ZPM-01..02 (COMPLETE)
        │
        ├── ZPM Website Model Correction ──► COR-ZPM-WEB-01..12 (EXECUTED)
        │
        └── Wave 4 ZPM Website (WEB-ZPM-01 only) ──► AT-W4-ZPM-01 (THIS PLAN)
                    │
                    └──► Wave 4B-ZPM Website Relationship Population (NEXT — after attestation act)
```

---

## 18. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Website roster |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution |
| [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | Project prerequisite |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Triumph REL-0027/0028 precedent |

---

*ATLAS Wave 4 ZPM Website Attestation v1 — documentation only; attestation act pending steward execution; corrected 2026-06-07.*
