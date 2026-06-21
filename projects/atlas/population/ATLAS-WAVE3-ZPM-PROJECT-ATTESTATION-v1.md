# ATLAS Wave 3 ZPM Project Attestation v1

**Status:** **documented** — Wave 3 ZPM Project attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** attestation runtime, executed attestation act, relationship attestation, Wave 3B-ZPM execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- ZPM Project intake: **COMPLETE**
- Wave 3 ZPM Population: **COMPLETE** — PRJ-0009, PRJ-0010 minted **proposed**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 3 ZPM Project (2 records), минимальные evidence gates, readiness по каждому проекту, missing evidence, candidate Wave 3B-ZPM queue, duplicate review, SAFE UNKNOWN posture, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 3 ZPM attestation scope

| In scope | Out of scope |
|----------|--------------|
| Project entity → **proposed** / **active** / **deprecated** (2 records) | COMMISSIONED_BY / EXECUTES edges |
| Evidence tier assignment per project | Website entity attestation (Wave 4) |
| Lifecycle structural state (no PM vocabulary) | BELONGS_TO edges (Wave 4B) |
| Future candidate exclusion enforcement | Domain entities (Wave 5) |
| Wave 3B-ZPM **queue preparation** | Person ↔ Project edges |
| SIBCAR/SITE-001 rejection enforcement | Foundation amendments |
| Duplicate review sign-off | SEO / advertising / AI / OCPilot Project rows |

Wave 3B-ZPM relationship **active** attestation executes in a **separate pass** after Project endpoints are **active** or **deprecated** (structural retire — still valid endpoint for historical edges).

---

## 3. Project roster (attestation set)

| project_id | canonical_name | population_slice | roster_priority | commissioning_org | execution_org | evidence_tier | target lifecycle |
|------------|----------------|------------------|-----------------|-------------------|---------------|---------------|------------------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **client_delivery** | **P0** | ORG-0005 ЗПМ | ORG-0001 Полигон | **E0** | **active** |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **client_delivery** | **P1** | ORG-0005 ЗПМ | ORG-0001 Полигон | **E0** | **deprecated** |

---

## 4. Lifecycle decisions

| project_id | Decision | Rationale | Governance |
|------------|----------|-----------|------------|
| PRJ-0009 | **active** | Ongoing catalog-platform delivery; almost complete; residual refinements (operator narrative) | W3-ZPM-LC-01; analog PRJ-0005..0008 |
| PRJ-0010 | **deprecated** | Completed historical delivery ~5 years ago; was in production | W3-ZPM-LC-02; LT-P01; analog PRJ-0004 |

| Rule ID | Rule | Enforcement |
|---------|------|-------------|
| **W3-ZPM-LC-01** | Ongoing client delivery → **active** | PRJ-0009 |
| **W3-ZPM-LC-02** | Completed delivery → **deprecated** | PRJ-0010 |
| **W3-ZPM-LC-03** | Forbidden: `completed`, `closed`, `done`, task states | Both |
| **W3-ZPM-LC-04** | Same hostname — two sequential Projects allowed | PRJ-0009 + PRJ-0010 — EFV-03 |
| **W3-ZPM-LC-05** | Deprecated project + live property allowed | PRJ-0010 + future WEB-* |

---

## 5. Evidence basis

| project_id | Evidence ref | Tier | Claim summary |
|------------|--------------|------|---------------|
| PRJ-0009 | EV-ZPM-OP-ACT-01 | **E0** | Client returned for full new version; catalog platform goal; almost complete; Polygon active WIP |
| PRJ-0010 | EV-ZPM-OP-HIST-01 | **E0** | Polygon created site ~5 years ago; WP + The7 + Custom; completed; in production |
| *(org anchor)* | EV-W1B-CC-01 §17 | **E1** | Indirect — org website **Bzpm.ru**; does not substitute project boundaries |
| *(prerequisite)* | AT-W1B-01, AT-W2B-ZPM-01 | attestation | ORG-0005 **active**; vendor context ORG-0001; Persons **active** |

**Evidence sufficiency:** E0 operator-direct path sufficient for both client_delivery Project records at population proposal (analog PRJ-0001 E0; PRJ-0004 E1 upgrade optional for PRJ-0010 — not blocking).

---

## 6. Attestation readiness by project

| project_id | Project | Target state | Min tier | Readiness | Blocker |
|------------|---------|--------------|----------|-----------|---------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **active** | E0 | **Ready** | — |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | E0 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Project to target lifecycle state now.
- Both projects: **Ready** — no conditional blockers.

---

## 7. Attestation sequence

### 7.1 Tranche AT-W3-ZPM-01 — Active catalog platform (P0)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0005 **active** | Steward | AT-W1B-01 |
| 2 | Verify ORG-0001 **active** (execution context) | Steward | Wave 1 |
| 3 | Duplicate scan ZPM-PRJ-D-01..07 | Steward | Register §7 |
| 4 | Confirm EFV-03 — no merge with PRJ-0010 | Steward | Intake analysis §7 |
| 5 | Propose PRJ-0009 canonical name | Steward | EV-ZPM-OP-ACT-01 |
| 6 | Assign **E0**; record commissioning ORG-0005, execution ORG-0001 *(display)* | Steward | Operator scope |
| 7 | Attest Project **active** | Steward (delegated) or Owner | Ongoing delivery discipline |
| 8 | Queue 3B-ZPM: REL-ZPM-PJ-01, REL-ZPM-PJ-02 | Steward | Population §8 |

### 7.2 Tranche AT-W3-ZPM-02 — Historical site (P1)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose PRJ-0010 with version suffix disambiguation | Steward | EV-ZPM-OP-HIST-01 |
| 2 | Confirm completed delivery — **deprecated** not `done` | Steward | LT-P01 |
| 3 | Assign **E0** | Steward | Operator historical block |
| 4 | Attest Project **deprecated** | Steward | Triumph PRJ-0004 analog |
| 5 | Queue 3B-ZPM: REL-ZPM-PJ-03, REL-ZPM-PJ-04 | Steward | Population §8 |

### 7.3 Wave 3B-ZPM pass (after Project attestation)

Execute in **separate package** — not bundled into steps above.

| Candidate | Type | Prerequisite |
|-----------|------|--------------|
| REL-ZPM-PJ-01 PRJ-0009 → ORG-0005 | **COMMISSIONED_BY** | PRJ-0009 **active** |
| REL-ZPM-PJ-02 ORG-0001 → PRJ-0009 | **EXECUTES** | PRJ-0009 **active** |
| REL-ZPM-PJ-03 PRJ-0010 → ORG-0005 | **COMMISSIONED_BY** | PRJ-0010 **deprecated** |
| REL-ZPM-PJ-04 ORG-0001 → PRJ-0010 | **EXECUTES** | PRJ-0010 **deprecated** |

---

## 8. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| ZPM-PRJ-D-01 | PRJ-0009 vs PRJ-0010 — `bzpm.ru` | **Not duplicate** — sequential deliveries | No |
| ZPM-PRJ-D-02 | PRJ-0009 vs FUT-01 SEO | **Distinct** — future held | No |
| ZPM-PRJ-D-03 | vs Triumph PRJ-0004..0008 | **Distinct org** ORG-0005 vs ORG-0004 | No |
| ZPM-PRJ-D-04 | vs future WEB-* | **Class boundary** | No |
| ZPM-PRJ-D-05 | vs SITE-001 / SIBCAR | **Reject** — COR-W1B-03 | No |
| ZPM-PRJ-D-06 | Name collision | **Resolved** — «(исходная версия)» | No |
| ZPM-PRJ-D-07 | Catalog vs site stem | **Pass** | No |

**Duplicate review summary:** **Pass**

---

## 9. Candidate Wave 3B relationships

**Not attested in this package.** Full inventory:

| Draft rel_id | source_id | target_id | relationship_type | project | readiness *(3B-ZPM)* |
|--------------|-----------|-----------|-------------------|---------|----------------------|
| REL-ZPM-PJ-01 | PRJ-0009 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0009 | **ready** after PRJ-0009 attested |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 | **EXECUTES** | PRJ-0009 | **ready** after PRJ-0009 attested |
| REL-ZPM-PJ-03 | PRJ-0010 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0010 | **ready** after PRJ-0010 attested |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 | **EXECUTES** | PRJ-0010 | **ready** after PRJ-0010 attested |

**Deferred beyond 3B-ZPM:**

| Item | Wave |
|------|------|
| WEB-* `bzpm.ru` | Wave 4 |
| DOM-* `bzpm.ru` | Wave 5 |
| WEB → Project BELONGS_TO | Wave 4B — **SU-ZPM-PRJ-03** |
| CLIENT_OF ORG-0005 → ORG-0001 | Wave 6 |

---

## 10. SAFE UNKNOWN review

| ID | Topic | Severity | Wave impact | Blocks attestation |
|----|-------|----------|-------------|-------------------|
| SU-ZPM-PRJ-01 | Historical contract / act dates | Low | Narrative only | **No** |
| SU-ZPM-PRJ-02 | Formal acceptance document (E1 path) | Low | Optional upgrade PRJ-0010 | **No** |
| SU-ZPM-PRJ-03 | Deployment replace vs coexistence | Medium | Wave 4 WEB / 4B BELONGS_TO | **No** |
| SU-ZPM-PRJ-04 | Canonical name refinement | Low | Display | **No** |
| SU-ZPM-PRJ-05 | OpenCartPilot scope (FUT-04) | Low | Future intake | **No** |
| SU-ZPM-PRJ-06 | PER-0014 / PER-0015 on Project | Low | No Person↔Project edges | **No** |
| SU-ZPM-PRJ-07 | CLIENT_OF commercial edge | Medium | Wave 6 | **No** |
| SU-ZPM-PRJ-08 | Domain registrant | Low | Wave 5 | **No** |

**Future possibilities (FUT-01..04):** SEO, контекстная реклама, AI automation, OpenCartPilot maintenance — **SAFE UNKNOWN** as approved projects; **hold** until start evidence.

**Blocking gaps for Project attestation:** **None**

---

## 11. Missing evidence register

| ID | Project | Gap | Severity | Mitigation |
|----|---------|-----|----------|------------|
| **ME-W3-ZPM-01** | PRJ-0010 | No contract-dated completion | Low | Operator «~5 years» narrative; E0 sufficient |
| **ME-W3-ZPM-02** | PRJ-0010 | No formal acceptance doc | Low | E1 upgrade path optional |
| **ME-W3-ZPM-03** | PRJ-0009 | No CC line for catalog rebuild | Low | E0 operator path sufficient |
| **ME-W3-ZPM-04** | Both | COMMISSIONED_BY / EXECUTES not minted | — | Wave 3B-ZPM by design |
| **ME-W3-ZPM-05** | Both | No WEB-* endpoint for `bzpm.ru` | Low | Wave 4 |

---

## 12. Readiness checklist crosswalk

| Check ID | Wave 3 ZPM Project package assessment |
|----------|---------------------------------------|
| W3-ZPM-S-01 | ORG-0005 **active** | **Pass** — AT-W1B-01 |
| W3-ZPM-S-02 | Wave 2 ZPM Persons **active** | **Pass** — PER-0014, PER-0015 |
| W3-ZPM-S-03 | Wave 2B ZPM relationships **active** | **Pass** — AT-W2B-ZPM-01 |
| W3-ZPM-S-04 | Project vs Organization boundary | **Pass** |
| W3-ZPM-E-01 | E0 structural attest path | **Pass** — both projects |
| W3-ZPM-E-02 | SIBCAR/SITE-001 excluded | **Pass** — COR-W1B-03 |
| W3-ZPM-E-03 | EFV-03 two-phase rule | **Pass** |
| W3-ZPM-D-01 | Duplicate batch complete | **Pass** — ZPM-PRJ-D-01..07 |
| W3-ZPM-I-01 | PRJ-0009/0010 mint rules | **Pass** |
| W3-ZPM-I-02 | Not Jira/PM semantics | **Pass** |
| W3-ZPM-R-01 | Org edges deferred | **Pass** — Wave 3B-ZPM queue |
| W3-ZPM-R-02 | Website/Domain deferred | **Pass** |
| W3-ZPM-R-03 | Future candidates held | **Pass** — FUT-01..04 |

---

## 13. Final verdict

### 13.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 3 ZPM Project intake cannot start |
| **PARTIALLY READY** | Subset only; documented blockers |
| **READY FOR WAVE 3 ZPM PROJECT ATTESTATION** | Full Project intake plan executable under gates |
| **READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION** | Project attestation complete; 3B-ZPM may proceed |

### 13.2 Assessment

| Criterion | Status |
|-----------|--------|
| Both required projects classified | **Pass** (2/2) |
| ORG-0005 endpoint **active** | **Pass** |
| Wave 2B ZPM prerequisites met | **Pass** |
| MARS / SIBCAR / SITE-001 exclusions enforced | **Pass** |
| Lifecycle states per LT-P01 | **Pass** |
| Evidence paths documented (E0) | **Pass** |
| Future candidates not minted | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Duplicate review **Pass** | **Pass** |
| Wave 3B-ZPM candidates prepared | **Pass** — REL-ZPM-PJ-01..04 |
| Known gaps enumerated | **Pass** — ME-W3-ZPM-01..05; SU-ZPM-PRJ-01..08 |

### 13.3 Verdict

```text
READY FOR WAVE 3 ZPM PROJECT ATTESTATION
```

**Conditions:**

1. Execute **AT-W3-ZPM-01** (PRJ-0009 **active**) before **AT-W3-ZPM-02** (PRJ-0010 **deprecated**) — current operational truth first.
2. Wave 3B-ZPM relationship **active** promotion requires Project attestation act — separate pass.
3. Do **not** mint SEO, advertising, AI automation, or OpenCartPilot Project rows without start evidence.
4. Do **not** merge PRJ-0009 and PRJ-0010 — EFV-03 enforced.
5. Draft register `proposed` flags **do not substitute** for steward attestation acts.

---

## 14. Post-attestation exit criteria *(future act)*

| Criterion | Evidence |
|-----------|----------|
| PRJ-0009 **active** | Attestation record AT-W3-ZPM-01 |
| PRJ-0010 **deprecated** | Attestation record AT-W3-ZPM-02 |
| No Website / Domain minted | Scope audit |
| No relationship edges minted | Scope audit |
| Wave 3B-ZPM queue prepared | REL-ZPM-PJ-01..04 |
| FUT-01..04 remain held | Register §5 |

---

## 15. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Project roster |
| [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) | Intake evidence analysis |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Prerequisite attestation |
| [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) | Core Wave 3 attestation pattern |

---

*ATLAS Wave 3 ZPM Project Attestation v1 — documentation only; attestation act not yet executed.*
