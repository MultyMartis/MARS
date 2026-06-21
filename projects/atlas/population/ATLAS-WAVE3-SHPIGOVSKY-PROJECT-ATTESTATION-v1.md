# ATLAS Wave 3 Shpigovsky Project Attestation v1

**Status:** **attested** — Wave 3 Shpigovsky Project attestation sequence complete; superseded by ACTIVE-ATTESTATION act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md)  
**Is not:** attestation runtime, executed attestation act, relationship attestation, Wave 3B-SHPIG execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — unchanged
- Wave 1C SIBCAR Organization ORG-0006: **active** — unchanged
- Wave 1D Makita Organization ORG-0007: **active** — unchanged
- Wave 1D Shpigovsky Organization ORG-0008: **active** — AT-W1D-SHPIG-01
- Shpigovsky Project intake: **COMPLETE**
- Wave 3 Shpigovsky Population: **COMPLETE** — PRJ-0012 minted **proposed**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 3 Shpigovsky Project (1 record), минимальные evidence gates, readiness по проекту, missing evidence, candidate Wave 3B-SHPIG queue, duplicate review, SAFE UNKNOWN posture, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 3 Shpigovsky attestation scope

| In scope | Out of scope |
|----------|--------------|
| Project entity → **proposed** / **active** (1 record) | COMMISSIONED_BY / EXECUTES edges |
| Evidence tier assignment per project | Website entity attestation (Wave 4) |
| Lifecycle structural state (no PM vocabulary) | BELONGS_TO edges (Wave 4B) |
| Future candidate exclusion enforcement | Domain entities (Wave 5) |
| Wave 3B-SHPIG **queue preparation** | Person creation / Person ↔ Project edges |
| Stack-slice split rejection (SEO, WP, ACF, …) | Foundation amendments |
| Duplicate review sign-off | LE-* mint |
| i-SEO project channel exclusion enforcement | CLIENT_OF commercial edges (Wave 6) |

Wave 3B-SHPIG relationship **active** attestation executes in a **separate pass** after Project endpoint is **active**.

---

## 3. Project roster (attestation set)

| project_id | canonical_name | population_slice | roster_priority | commissioning_org | execution_org | evidence_tier | target lifecycle |
|------------|----------------|------------------|-----------------|-------------------|---------------|---------------|------------------|
| PRJ-0012 | Сайт shpigovsky.ru | **client_delivery** | **P0** | ORG-0008 ООО «Сознание» | ORG-0001 Полигон | **E0/E1** | **active** |

---

## 4. Lifecycle decisions

| project_id | Decision | Rationale | Governance |
|------------|----------|-----------|------------|
| PRJ-0012 | **active** | Ongoing Polygon client delivery; operator describes technical execution roles; Website Factory workflow context | W3-SHPIG-LC-01; analog PRJ-0011 SIBCAR active |

| Rule ID | Rule | Enforcement |
|---------|------|-------------|
| **W3-SHPIG-LC-01** | Ongoing client delivery → **active** | PRJ-0012 |
| **W3-SHPIG-LC-02** | Forbidden: `completed`, `closed`, `done`, task states | PRJ-0012 |
| **W3-SHPIG-LC-03** | Single delivery initiative — no stack-slice Project split | EFV-03 |
| **W3-SHPIG-LC-04** | No historical deprecated twin without second delivery phase evidence | Contrast ZPM PRJ-0010 — not applicable |
| **W3-SHPIG-LC-05** | Delivery phase precision **SAFE UNKNOWN** — does not block **active** at E0/E1 | SU-SHPIG-PRJ-08 |

---

## 5. Evidence basis

| project_id | Evidence ref | Tier | Claim summary |
|------------|--------------|------|---------------|
| PRJ-0012 | EV-SHPIG-OP-01 | **E0** | Polygon client delivery; Olga acquisition/coordination/SEO supervision/acceptance; operator frontend/WP/technical delivery; Website Factory; not i-SEO channel |
| PRJ-0012 | AT-W1D-SHPIG-01 | **E1** *(org anchor)* | ORG-0008 **active** — commissioning org endpoint |
| *(property corroboration)* | EV-SHPIG-WEB-01 | **E2** | Public `shpigovsky.ru` exists — Website class at Wave 4; does not substitute project boundary |
| *(org corroboration)* | EV-SHPIG-WEB-02 | **E2** | Policy operator ООО «Сознание» — org layer only |
| *(prerequisite)* | AT-W1D-SHPIG-01 | attestation | ORG-0008 **active**; ORG-0001 **active** (Wave 1) |

**Evidence sufficiency:** E0 operator-direct path + E1 org anchor sufficient for client_delivery Project at attestation proposal (analog PRJ-0011 E0 SIBCAR; PRJ-0009 E0 ZPM).

**Claim → evidence chain (PRJ-0012):**

1. «Polygon delivers shpigovsky.ru website for client» → EV-SHPIG-OP-01
2. «Commissioning org ООО «Сознание»» → AT-W1D-SHPIG-01 / ORG-0008 **active**
3. «Execution via ORG-0001 Полигон» → EV-SHPIG-OP-01 *(display context; structural edges Wave 3B)*
4. «WordPress / ACF / custom code — single delivery» → EV-SHPIG-OP-01 — EFV-03; **no** per-stack Project split
5. «Public property exists» → EV-SHPIG-WEB-01 — Website class at Wave 4; does not block Project attestation

---

## 6. Attestation readiness by project

| project_id | Project | Target state | Min tier | Readiness | Blocker |
|------------|---------|--------------|----------|-----------|---------|
| PRJ-0012 | Сайт shpigovsky.ru | **active** | E0/E1 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Project to target lifecycle state now.
- PRJ-0012: **Ready** — no conditional blockers for population proposal tier.

---

## 7. Attestation sequence

### 7.1 Tranche AT-W3-SHPIG-01 — Active site delivery (P0)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0008 **active** | Steward | AT-W1D-SHPIG-01 |
| 2 | Verify ORG-0001 **active** (execution context) | Steward | Wave 1 |
| 3 | Verify ORG-0005..0007 **unchanged** (ZPM, SIBCAR, Makita) | Steward | Prior wave registers |
| 4 | Duplicate scan SHPIG-PRJ-D-01..09 | Steward | Register §7 |
| 5 | Confirm EFV-03 — no stack-slice Project split | Steward | Population §6.2 |
| 6 | Confirm i-SEO project channel **excluded** | Steward | EV-SHPIG-OP-01 |
| 7 | Propose PRJ-0012 canonical name **Сайт shpigovsky.ru** | Steward | SHPIGOVSKY-INTAKE-CAND-PRJ-A01 |
| 8 | Assign **E0/E1**; record commissioning ORG-0008, execution ORG-0001 *(display)* | Steward | Operator scope |
| 9 | Attest Project **active** | Steward (delegated) or Owner | Ongoing delivery discipline |
| 10 | Queue 3B-SHPIG: REL-SHPIG-PJ-01, REL-SHPIG-PJ-02 | Steward | Population §8 |

### 7.2 Wave 3B-SHPIG pass (after Project attestation)

Execute in **separate package** — not bundled into steps above.

| Candidate | Type | Prerequisite |
|-----------|------|--------------|
| REL-SHPIG-PJ-01 PRJ-0012 → ORG-0008 | **COMMISSIONED_BY** | PRJ-0012 **active** |
| REL-SHPIG-PJ-02 ORG-0001 → PRJ-0012 | **EXECUTES** | PRJ-0012 **active** |

---

## 8. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| SHPIG-PRJ-D-01 | PRJ-0012 vs ORG-0008 | **Class boundary** | No |
| SHPIG-PRJ-D-02 | PRJ-0012 vs future WEB-* | **Class boundary** | No |
| SHPIG-PRJ-D-03 | vs PRJ-0009..0011 | **Distinct org** | No |
| SHPIG-PRJ-D-04 | vs FUT-01 WP automation | **Distinct** — future held | No |
| SHPIG-PRJ-D-05 | vs FUT-02 SEO program | **Distinct** — future held | No |
| SHPIG-PRJ-D-06 | Single vs multi-project stack slices | **Not duplicate** — EFV-03 | No |
| SHPIG-PRJ-D-07 | vs ORG-0001..0007 | **Distinct** — no merge | No |
| SHPIG-PRJ-D-08 | vs Makita / ZPM / SIBCAR | **Distinct** — integrity pass | No |
| SHPIG-PRJ-D-09 | Historical deprecated twin | **N/A** — no historical Project | No |

**Duplicate review summary:** **Pass**

---

## 9. Candidate Wave 3B relationships

**Not attested in this package.** Full inventory:

| Draft rel_id | source_id | target_id | relationship_type | project | readiness *(3B-SHPIG)* |
|--------------|-----------|-----------|-------------------|---------|------------------------|
| REL-SHPIG-PJ-01 | PRJ-0012 | ORG-0008 ООО «Сознание» | **COMMISSIONED_BY** | PRJ-0012 | **ready** after PRJ-0012 attested |
| REL-SHPIG-PJ-02 | ORG-0001 Полигон | PRJ-0012 | **EXECUTES** | PRJ-0012 | **ready** after PRJ-0012 attested |

**Deferred beyond 3B-SHPIG:**

| Item | Wave |
|------|------|
| WEB-* `shpigovsky.ru` | Wave 4 |
| DOM-* `shpigovsky.ru` | Wave 5 |
| WEB → Project BELONGS_TO | Wave 4B |
| CLIENT_OF ORG-0008 → ORG-0001 | Wave 6 |

---

## 10. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact | Blocks attestation |
|----|-------|----------|-------------|-------------------|
| SU-SHPIG-PRJ-01 | Contract dates | Low | Narrative only | **No** |
| SU-SHPIG-PRJ-02 | Acceptance dates | Low | Narrative only | **No** |
| SU-SHPIG-PRJ-03 | Legal signatory | Low | E1 upgrade path | **No** |
| SU-SHPIG-PRJ-04 | Internal client contacts | Low | Person deferred | **No** |
| SU-SHPIG-PRJ-05 | Future SEO contract | Low | Future intake | **No** |
| SU-SHPIG-PRJ-06 | Future Direct contract | Low | Future intake | **No** |
| SU-SHPIG-PRJ-07 | Future AI automation work | Low | Future intake FUT-01 | **No** |
| SU-SHPIG-PRJ-08 | Delivery phase precision | Low | Narrative only | **No** |
| SU-SHPIG-PRJ-09 | ACF / custom programming scope | Low | Stack detail | **No** |
| SU-SHPIG-PRJ-10 | PER-0010 on Project | Low | No Person↔Project edges | **No** |
| SU-SHPIG-PRJ-11 | CLIENT_OF commercial edge | Medium | Wave 6 | **No** |
| SU-SHPIG-PRJ-12 | Domain registrant | Low | Wave 5 | **No** |

**Future possibilities (FUT-01..02; future SEO / Direct / AI):** **SAFE UNKNOWN** as approved projects; **hold** until start evidence.

**Blocking gaps for Project attestation:** **None**

---

## 11. Missing evidence register

| ID | Project | Gap | Severity | Mitigation |
|----|---------|-----|----------|------------|
| **ME-W3-SHPIG-01** | PRJ-0012 | No contract-dated delivery boundary | Low | Operator role narrative; E0 sufficient |
| **ME-W3-SHPIG-02** | PRJ-0012 | No formal acceptance document | Low | SU-SHPIG-PRJ-02 — E1 upgrade path optional |
| **ME-W3-SHPIG-03** | PRJ-0012 | No CC line for project scope | Low | E0 operator path sufficient |
| **ME-W3-SHPIG-04** | PRJ-0012 | COMMISSIONED_BY / EXECUTES not minted | — | Wave 3B-SHPIG by design |
| **ME-W3-SHPIG-05** | PRJ-0012 | No WEB-* endpoint for `shpigovsky.ru` | Low | Wave 4 |

---

## 12. Readiness checklist crosswalk

| Check ID | Wave 3 Shpigovsky Project package assessment |
|----------|---------------------------------------------|
| W3-SHPIG-S-01 | ORG-0008 **active** | **Pass** — AT-W1D-SHPIG-01 |
| W3-SHPIG-S-02 | ORG-0001 **active** (execution context) | **Pass** — Wave 1 |
| W3-SHPIG-S-03 | ORG-0005..0007 unchanged (ZPM, SIBCAR, Makita) | **Pass** |
| W3-SHPIG-S-04 | Project vs Organization boundary | **Pass** |
| W3-SHPIG-E-01 | E0/E1 structural attest path | **Pass** — PRJ-0012 |
| W3-SHPIG-E-02 | i-SEO project channel excluded | **Pass** — EV-SHPIG-OP-01 |
| W3-SHPIG-E-03 | EFV-03 single-delivery rule | **Pass** |
| W3-SHPIG-D-01 | Duplicate batch complete | **Pass** — SHPIG-PRJ-D-01..09 |
| W3-SHPIG-I-01 | PRJ-0012 mint rules | **Pass** |
| W3-SHPIG-I-02 | Not Jira/PM semantics | **Pass** |
| W3-SHPIG-R-01 | Org edges deferred | **Pass** — Wave 3B-SHPIG queue |
| W3-SHPIG-R-02 | Website/Domain deferred | **Pass** |
| W3-SHPIG-R-03 | Future candidates held | **Pass** — FUT-01..02; future SEO/Direct/AI |
| W3-SHPIG-R-04 | No stack-slice Project split | **Pass** |

---

## 13. Final verdict

### 13.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 3 Shpigovsky Project intake cannot start |
| **PARTIALLY READY** | Subset only; documented blockers |
| **READY FOR WAVE 3 SHPIGOVSKY PROJECT ATTESTATION** | Full Project intake plan executable under gates |
| **READY FOR WAVE 3B SHPIG PROJECT RELATIONSHIP POPULATION** | Project attestation complete; 3B-SHPIG may proceed |

### 13.2 Assessment

| Criterion | Status |
|-----------|--------|
| Required project classified | **Pass** (1/1) |
| ORG-0008 endpoint **active** | **Pass** |
| ORG-0001..0007 integrity (no merge) | **Pass** |
| Makita / ZPM / SIBCAR unchanged | **Pass** |
| Lifecycle state **active** per rules | **Pass** |
| Evidence paths documented (E0/E1) | **Pass** |
| Future candidates not minted | **Pass** |
| Stack-slice split rejected | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Duplicate review **Pass** | **Pass** |
| Wave 3B-SHPIG candidates prepared | **Pass** — REL-SHPIG-PJ-01..02 |
| Known gaps enumerated | **Pass** — ME-W3-SHPIG-01..05; SU-SHPIG-PRJ-01..12 |

### 13.3 Verdict

```text
READY FOR WAVE 3 SHPIGOVSKY PROJECT ATTESTATION
```

**Conditions:**

1. Execute **AT-W3-SHPIG-01** (PRJ-0012 **active**) — single P0 tranche.
2. Wave 3B-SHPIG relationship **active** promotion requires Project attestation act — separate pass.
3. Do **not** mint SEO, Direct, AI automation, or stack-slice Project rows without start evidence.
4. Do **not** mint historical / deprecated twin — no second delivery phase evidenced.
5. Draft register `proposed` flags **do not substitute** for steward attestation acts.

---

## 14. Post-attestation exit criteria *(future act)*

| Criterion | Evidence |
|-----------|----------|
| PRJ-0012 **active** | Attestation record AT-W3-SHPIG-01 |
| No Website / Domain minted | Scope audit |
| No relationship edges minted | Scope audit |
| Wave 3B-SHPIG queue prepared | REL-SHPIG-PJ-01..02 |
| FUT-01..02 and future SEO/Direct/AI remain held | Register §5 |

---

## 15. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md) | Project roster |
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | Intake evidence analysis |
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) | Prerequisite attestation |
| [ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md) | Single-project attestation pattern analog |

---

*ATLAS Wave 3 Shpigovsky Project Attestation v1 — superseded by [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md).*
