# ATLAS Wave 4 ZPM Website Active Attestation v1

**Status:** **attested** — first official Website active attestation for Wave 4 ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, database export, Wave 4B-ZPM relationship attestation, Domain entities, Person ↔ Website edges, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01; canonical **ЗПМ** — RN-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- ZPM Website Model Correction: **EXECUTED** — COR-ZPM-WEB-01..12
- Wave 4 ZPM Website attestation plan verdict: **READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)**

---

# REPORT — ATLAS Wave 4 ZPM Website Active Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W4-ZPM-01**  
**Promotion:** WEB-ZPM-01 — **proposed** → **active**  
**Blocked tranche:** AT-W4-ZPM-02 — WEB-ZPM-02 retired (COR-ZPM-WEB-05)

---

## 1. Attestation result

| website_id | canonical_name | prior state | attested state | evidence_tier | tranche | result |
|------------|----------------|-------------|----------------|---------------|---------|--------|
| **WEB-ZPM-01** | bzpm.ru | **proposed** | **active** | **E0** | AT-W4-ZPM-01 | **Attested** |
| WEB-ZPM-02 | bzpm.ru (исходная версия) | — | *(not attested)* | — | AT-W4-ZPM-02 | **Blocked** — COR-ZPM-WEB-05 |

**Promotion count:** **1 / 1** Website record attested  
**Active promoted:** **1** (WEB-ZPM-01)  
**Deprecated Website promoted:** **0**  
**Relationships created:** **0**  
**Domain entities created:** **0**

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1): steward attestation under documented evidence discipline — **satisfied** for WEB-ZPM-01.

---

## 2. Pre-check — evidence inventory (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-02..06.

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists**.

| # | Ref | Source | Tier | Role |
|---|-----|--------|------|------|
| 1 | **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild | **E0** | WEB-ZPM-01 **active** |
| 2 | **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` delivery | **E0** | **PRJ-0010** — not Website mint |
| 3 | **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 | **E1** | Org anchor; indirect hostname corroboration |
| 4 | **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** |
| 5 | **AT-W3-ZPM-01** | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | attestation | PRJ-0009 **active** |
| 6 | **AT-W3-ZPM-02** | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | attestation | PRJ-0010 **deprecated** |
| 7 | **AT-W3B-ZPM-01..02** | [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | attestation | REL-ZPM-PJ-01..04 **active** |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| Operator evidence refs recorded | **Pass** — EV-ZPM-OP-ACT-01; EV-ZPM-OP-HIST-01 re-routed to PRJ-0010 |
| CC inventory cited (reuse AT-W1B-01) | **Pass** — EV-W1B-CC-01 |
| ORG-0005 endpoint **active** | **Pass** — AT-W1B-01 |
| PRJ-0009 **active**, PRJ-0010 **deprecated** | **Pass** — AT-W3-ZPM-01..02 |
| Wave 3B ZPM prerequisites met | **Pass** — REL-ZPM-PJ-01..04 |
| SIBCAR/SITE-001 not used as Website evidence | **Pass** — EFV-02; COR-W1B-03 |
| EFV-03 two-phase rule at Project layer | **Pass** — one Website; two Projects |
| ZPM Website Model Correction executed | **Pass** — COR-ZPM-WEB-01..12 |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (WEB-ZPM-01)
E0 operator — EV-ZPM-OP-HIST-01 (PRJ-0010 — Project layer only)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx
```

---

## 3. Prerequisite endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **PRJ-0009** Каталог-платформа bzpm.ru | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** Сайт bzpm.ru (исходная версия) | **deprecated** | AT-W3-ZPM-02 | **Pass** |
| **REL-ZPM-PJ-01..04** | **active** | AT-W3B-ZPM-01..02 | **Pass** |
| **LE-0004** | **active** | AT-W1B-01 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested before Website promotion.

---

## 4. Website model correction verification

| Check | Source | Verified |
|-------|--------|----------|
| WEB-ZPM-02 **retired** — not minted | COR-ZPM-WEB-01 | **Pass** |
| AT-W4-ZPM-02 **blocked** | COR-ZPM-WEB-05 | **Pass** |
| REL-ZPM-WB-02 **cancelled** | COR-ZPM-WEB-06 | **Pass** |
| REL-ZPM-WB-03 **queued** | COR-ZPM-WEB-07 | **Pass** |
| Single-property model — Triumph analog | COR-ZPM-WEB-03; Decision §4 | **Pass** |
| Operator decision **PASS WITH CORRECTION** | [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) | **Pass** |
| Correction execution complete | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | **Pass** |

**Verdict:** **Pass** — website model correction executed; attestation proceeds on corrected single-Website roster only.

---

## 5. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-WEB-D-01** | WEB-ZPM-01 vs WEB-ZPM-02 — same hostname | **Fail** — WEB-ZPM-02 retired | No *(resolved)* |
| **ZPM-WEB-D-02** | vs single merged `bzpm.ru` Website | **Pass** — one Website minted | No |
| **ZPM-WEB-D-03** | vs Triumph WEB-0006..0009 | **Distinct org** ORG-0005 vs ORG-0004 | No |
| **ZPM-WEB-D-04** | vs SITE-001 / SIBCAR | **Reject** — COR-W1B-03 | No |
| **ZPM-WEB-D-05** | BZPM vs ЗПМ org identity | **Resolved** — alias discipline | No |
| **ZPM-WEB-D-06** | Name collision on «bzpm.ru» | **Resolved** — single property | No |
| **ZPM-WEB-D-07** | WEB-ZPM-* vs WEB-0006 namespace | **Pass** — tranche separation | No |

**Hostname conflict cross-check:**

| Hostname | website_id | org anchor | Conflict |
|----------|------------|------------|----------|
| `gktriumph.ru` | WEB-0006 *(Triumph)* | ORG-0004 | **None** — distinct client |
| `bzpm.ru` | **WEB-ZPM-01** *(this act)* | ORG-0005 ЗПМ | — |
| `bzpm.ru` | WEB-ZPM-02 | — | **Retired** — not minted |

**Verdict:** **Pass** — no duplicate Website entities; no hostname conflicts across attested or proposed roster.

---

## 6. Verification gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **W4-ZPM-EG-01** | ORG-0005 **active** before Website **active** | **Pass** — AT-W1B-01 |
| **W4-ZPM-EG-02** | PRJ-0009 **active** before WEB-ZPM-01 **active** | **Pass** — AT-W3-ZPM-01 |
| **W4-ZPM-EG-04** | Wave 3B ZPM Project↔Org complete | **Pass** — REL-ZPM-PJ-01..04 |
| **W4-ZPM-EG-05** | E0 structural attest path — client property | **Pass** — WEB-ZPM-01 |
| **W4-ZPM-EG-06** | SIBCAR/SITE-001 excluded (EFV-02) | **Pass** — COR-W1B-03 |
| **W4-ZPM-EG-07** | Single Website mint — EIR-W01 | **Pass** — COR-ZPM-WEB-12 |
| **W4-ZPM-EG-08** | Duplicate batch before attestation | **Pass** — ZPM-WEB-D-01..07 |
| **W4-ZPM-EG-09** | Human attest mandatory | **Pass** — this act |
| **W4-ZPM-EG-10** | WEB-ZPM-02 attestation blocked | **Pass** — COR-ZPM-WEB-05 |
| **W4-ZPM-EG-11** | No relationship edges in this package | **Pass** — scope restriction |
| **W4-ZPM-EG-12** | BZPM ≠ separate Organization | **Pass** — identity rule |
| **W4-ZPM-VG-01** | PRJ-0010 **deprecated** *(context)* | **Pass** — AT-W3-ZPM-02 |
| **W4-ZPM-VG-02** | Website model correction executed | **Pass** — correction execution |
| **W4-ZPM-VG-03** | No duplicate Website entities | **Pass** — single mint |
| **W4-ZPM-VG-04** | No hostname conflicts | **Pass** — §5 |
| **W4-ZPM-VG-05** | No Domain entities yet | **Pass** — DOM-* deferred Wave 5 |

**Readiness checklist crosswalk:**

| Check ID | Assessment |
|----------|------------|
| W4-ZPM-S-01 | ORG-0005 **active** | **Pass** |
| W4-ZPM-S-02 | PRJ-0009 **active** | **Pass** |
| W4-ZPM-S-03 | PRJ-0010 **deprecated** | **Pass** |
| W4-ZPM-S-04 | Wave 3B ZPM relationships **active** | **Pass** |
| W4-ZPM-E-01 | E0 structural attest path | **Pass** |
| W4-ZPM-E-02 | SIBCAR/SITE-001 excluded | **Pass** |
| W4-ZPM-D-01 | Duplicate batch complete | **Pass** |
| W4-ZPM-I-01 | Single Website mint rule | **Pass** |
| W4-ZPM-I-02 | WEB-ZPM-02 blocked | **Pass** |
| W4-ZPM-R-01 | BELONGS_TO deferred | **Pass** — Wave 4B-ZPM |
| W4-ZPM-R-02 | OWNS / OPERATES deferred | **Pass** — Wave 4B-ZPM |
| W4-ZPM-R-03 | DOM-* / PRIMARY_DOMAIN deferred | **Pass** — Wave 5 / 5B |

**Verdict:** **Pass** — all gates satisfied for Website lifecycle promotion.

---

## 7. Attestation tranche executed

### 7.1 AT-W4-ZPM-01 — Sole web property

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify ORG-0005 **active** (canonical **ЗПМ**) | Steward | AT-W1B-01; RN-W1B-01 | **Done** |
| 2 | Verify PRJ-0009 **active** (Wave 3 ZPM) | Steward | AT-W3-ZPM-01 | **Done** |
| 3 | Verify PRJ-0010 **deprecated** (Wave 3 ZPM) | Steward | AT-W3-ZPM-02 | **Done** |
| 4 | Verify REL-ZPM-PJ-01..04 **active** (Wave 3B ZPM) | Steward | AT-W3B-ZPM-01..02 | **Done** |
| 5 | Duplicate scan ZPM-WEB-D-01..07 | Steward | Register §10 | **Done** |
| 6 | Confirm WEB-ZPM-02 **not** attested — COR-ZPM-WEB-05 | Steward | Correction execution | **Done** |
| 7 | Confirm website model correction complete | Steward | COR-ZPM-WEB-01..12 | **Done** |
| 8 | Propose WEB-ZPM-01 canonical name **bzpm.ru** | Steward | EV-ZPM-OP-ACT-01 | **Done** |
| 9 | Assign website_kind **corporate** *(catalog platform)*; aliases | Steward | Register §5 | **Done** |
| 10 | Assign **E0**; record org/project display candidates | Steward | Population §5.1 | **Done** |
| 11 | Attest Website **active** | Steward (delegated) | W4-ZPM-LC-01 | **Done** |
| 12 | Queue 4B-ZPM: REL-ZPM-WB-01 + REL-ZPM-WB-03 | Steward | Population §10.1 | **Queued** |

### 7.2 AT-W4-ZPM-02 — BLOCKED

| Step | Action | Status |
|------|--------|--------|
| All | WEB-ZPM-02 attestation | **Blocked** — COR-ZPM-WEB-05; entity retired |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create BELONGS_TO edges | **Excluded** | Wave 4B-ZPM |
| Create OWNS / OPERATES edges | **Excluded** | Wave 4B-ZPM |
| Create PRIMARY_DOMAIN edges | **Excluded** | Wave 5B ZPM |
| Create DOM-* entities | **Excluded** | Wave 5 ZPM |
| Create CLIENT_OF ORG-0005 → ORG-0001 | **Excluded** | Wave 6 |
| Create Person ↔ Website edges | **Excluded** | Operator scope |
| Attest WEB-ZPM-02 | **Blocked** | COR-ZPM-WEB-01..05 |

---

## 8. Entity promotion summary

### 8.1 WEB-ZPM-01 — bzpm.ru

| Field | Value |
|-------|-------|
| **website_id** | WEB-ZPM-01 |
| **canonical_name** | bzpm.ru |
| **website_kind** | corporate *(catalog platform)* |
| **url** | `https://bzpm.ru` |
| **primary organization** *(display)* | ORG-0005 ЗПМ |
| **project bindings** *(display)* | PRJ-0009 Каталог-платформа bzpm.ru; PRJ-0010 Сайт bzpm.ru (исходная версия) |
| **aliases** | Сайт ЗПМ; Каталог bzpm.ru; Bzpm.ru |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; ongoing catalog-platform property on `bzpm.ru`; single-property model per operator decision; duplicate review **Pass**; Triumph analog WEB-0006 |
| **evidence_tier** | **E0** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Historical delivery held by PRJ-0010 at Project layer — not separate Website. Wave 4B queue: REL-ZPM-WB-01 BELONGS_TO PRJ-0009; REL-ZPM-WB-03 BELONGS_TO PRJ-0010. |

### 8.2 Promotion ledger

| Entity class | id | prior | attested | count |
|--------------|-----|-------|----------|-------|
| Website | WEB-ZPM-01 | **proposed** | **active** | 1 |
| Website | WEB-ZPM-02 | — | *(not minted)* | 0 |
| Organization | ORG-0005 | **active** | **active** *(unchanged)* | — |
| Project | PRJ-0009 | **active** | **active** *(unchanged)* | — |
| Project | PRJ-0010 | **deprecated** | **deprecated** *(unchanged)* | — |
| Domain | DOM-* | — | *(not created)* | 0 |
| Relationship | REL-ZPM-WB-* | — | *(not created)* | 0 |

---

## 9. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-ZPM-WB-01 WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** | **Queued** — Wave 4B-ZPM |
| REL-ZPM-WB-03 WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** | **Queued** — Wave 4B-ZPM |
| REL-ZPM-WB-02 WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancelled** — COR-ZPM-WEB-06 |
| ORG-0005 **OWNS** WEB-ZPM-01 | **Queued** — Wave 4B-ZPM |
| ORG-0001 **OPERATES** WEB-ZPM-01 | **Queued** — Wave 4B-ZPM *(steward choice)* |
| DOM-* `bzpm.ru` | **Not created** — Wave 5 ZPM |
| PRIMARY_DOMAIN `bzpm.ru` → WEB-ZPM-01 | **Not created** — Wave 5B ZPM |
| REL-0016 CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** — Wave 6 |
| Person ↔ Website edges | **Not created** |
| Organization → Website structural edges | **Not created** — Wave 4B-ZPM |
| WEB-ZPM-02 | **Retired** — COR-ZPM-WEB-01 |
| Foundation documents | **Not modified** |

---

## 10. Remaining SAFE UNKNOWN

| ID | Topic | Severity | Wave impact | Status |
|----|-------|----------|-------------|--------|
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence | Medium | **Resolved** — single Website |
| **SU-W3B-ZPM-01** | Dual BELONGS_TO for same hostname | Medium | **Resolved** — REL-ZPM-WB-01 + REL-ZPM-WB-03 queued |
| **SU-W4-ZPM-03** | Single DOM-* vs dual generation | Low | **Resolved** — DOM-* → WEB-ZPM-01 |
| **SU-W4-ZPM-02** | OWNS on deprecated Website | Low | **Obviated** — no deprecated Website |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Wave 5 ZPM DOM-* |
| **SU-ZPM-PRJ-01** | Historical contract / act dates | Low | PRJ-0010 narrative |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | Wave 6 |
| **SU-W4-ZPM-01** | Live URL probe for `bzpm.ru` | Low | E0 sufficient; optional upgrade |
| **ME-W4-ZPM-02** | BELONGS_TO not yet attested | — | Wave 4B-ZPM by design |
| **ME-W4-ZPM-03** | OWNS edge not yet attested | Low | Wave 4B-ZPM queue |
| **ME-W4-ZPM-04** | PRIMARY_DOMAIN / DOM-* not minted | Low | Wave 5 ZPM |
| **ME-W4-ZPM-05** | Live URL probe timestamp optional | Low | E0 operator path sufficient |

**Blocking gaps remaining:** **None**

---

## 11. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 1 Website record attested |
| No Foundation modification | **Pass** |
| No Wave 1 / 2 / 2B / 3 / 3B record modification | **Pass** |
| ORG-0005 endpoint **active** honored | **Pass** |
| EIR-W01 single property model | **Pass** |
| EFV-03 at Project layer only | **Pass** |
| Triumph multi-Project BELONGS_TO precedent | **Pass** — REL-0027/0028 analog |
| No relationship edges created | **Pass** |
| No Domain minted | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 12. Readiness verdict

```text
READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION
```

**Conditions met:**

1. WEB-ZPM-01 **active** — sole real web property for `bzpm.ru` attested at **E0** under EV-ZPM-OP-ACT-01.
2. Pre-check inventory, prerequisite endpoints, website model correction verification, duplicate review, and evidence gates — **all Pass**.
3. WEB-ZPM-02 **not** attested — retired per COR-ZPM-WEB-01; AT-W4-ZPM-02 **blocked**.
4. Wave 4B-ZPM candidates REL-ZPM-WB-01 + REL-ZPM-WB-03 **ready** — Website endpoint now attested **active**; REL-ZPM-WB-02 **cancelled**.
5. No BELONGS_TO, OWNS, PRIMARY_DOMAIN, DOM-*, CLIENT_OF, or Person↔Website edges created in this package.

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)** | [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) §15 | **Superseded** — WEB-ZPM-01 now attested **active** |
| **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIPS** *(pre-attestation)* | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) §12 | **Superseded** — Website attestation act now complete |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **READY FOR WAVE 4 ZPM WEBSITE ATTESTATION** | Superseded — attestation act complete |
| **READY FOR WAVE 5 ZPM DOMAIN POPULATION** | Wave 4B-ZPM relationships must precede Domain layer |

**Downstream:** Execute Wave 4B-ZPM Website relationship population in a **separate pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03 (BELONGS_TO only); ORG-0005 **OWNS** WEB-ZPM-01 queued.

---

## 13. Wave 4B-ZPM queue (post-attestation)

| Draft rel_id | source_id | target_id | relationship_type | prerequisite | readiness |
|--------------|-----------|-----------|-------------------|--------------|-----------|
| REL-ZPM-WB-01 | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | **BELONGS_TO** | WEB-ZPM-01 **active**; PRJ-0009 **active** | **ready** |
| REL-ZPM-WB-03 | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | **BELONGS_TO** | WEB-ZPM-01 **active**; PRJ-0010 **deprecated** | **ready** |
| *(TBD)* | ORG-0005 ЗПМ | WEB-ZPM-01 | **OWNS** | Website **active** | **ready** |

**Cancelled:**

| Draft rel_id | Reason |
|--------------|--------|
| REL-ZPM-WB-02 | COR-ZPM-WEB-06 — WEB-ZPM-02 retired |

---

## 14. Package lineage

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
        └── Wave 4 ZPM Website (WEB-ZPM-01 only) ──► AT-W4-ZPM-01 (THIS ACT)
                    │
                    └──► Wave 4B-ZPM Website Relationship Population (NEXT)
```

---

## 15. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Website roster |
| [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) | Attestation sequence (superseded §15 verdict) |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution |
| [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) | Operator decision record |
| [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | Project prerequisite |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Triumph REL-0027/0028 precedent |

---

*ATLAS Wave 4 ZPM Website Active Attestation v1 — documentation only.*
