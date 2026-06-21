# ATLAS Wave 3 ZPM Project Active Attestation v1

**Status:** **attested** — first official Project active attestation for Wave 3 ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, database export, Wave 3B-ZPM relationship attestation, Website / Domain entities, Person ↔ Project edges, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Project Population: **COMPLETE** — PRJ-0009, PRJ-0010 minted **proposed**
- Wave 3 ZPM Project attestation plan verdict: **READY FOR WAVE 3 ZPM PROJECT ATTESTATION**

---

# REPORT — ATLAS Wave 3 ZPM Project Active Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W3-ZPM-01** + **AT-W3-ZPM-02**  
**Promotion:** PRJ-0009 — **proposed** → **active**; PRJ-0010 — **proposed** → **deprecated**

---

## 1. Pre-check — evidence inventory (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-02..06.

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists** (prior inventory AT-W1B-01).

| # | Ref | Source | Tier | Role |
|---|-----|--------|------|------|
| 1 | **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild | **E0** | PRJ-0009 active delivery |
| 2 | **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` delivery | **E0** | PRJ-0010 deprecated delivery |
| 3 | **EV-ZPM-OP-FUT-01** | Operator statement — future possibilities only | **E0** | Exclusion basis FUT-01..04 |
| 4 | **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` | **E1** | Org anchor; §17 indirect hostname corroboration only |
| 5 | **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** |
| 6 | **AT-W2-ZPM-01..02** | [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) | attestation | PER-0014, PER-0015 **active** |
| 7 | **AT-W2B-ZPM-01..02** | [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | attestation | Person → Org vendor context |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| Operator evidence refs recorded | **Pass** — EV-ZPM-OP-ACT-01, EV-ZPM-OP-HIST-01 |
| CC inventory cited (reuse AT-W1B-01) | **Pass** — EV-W1B-CC-01 |
| ORG-0005 endpoint **active** | **Pass** — AT-W1B-01 |
| PER-0014, PER-0015 **active** | **Pass** — AT-W2-ZPM-01..02 |
| Wave 2B ZPM prerequisites met | **Pass** — AT-W2B-ZPM-01 |
| SIBCAR/SITE-001 not used as Project evidence | **Pass** — EFV-02; COR-W1B-03 |
| EFV-03 two-phase rule honored | **Pass** — two Project records, no merge |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (PRJ-0009)
E0 operator — EV-ZPM-OP-HIST-01 (PRJ-0010)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx (org anchor only)
```

---

## 2. Prerequisite endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **ORG-0001** Полигон | **active** *(execution context)* | Wave 1 attestation | **Pass** |
| **PER-0014** Дубинский | **active** | AT-W2-ZPM-02 | **Pass** |
| **PER-0015** Крюков | **active** | AT-W2-ZPM-01 | **Pass** |
| **LE-0004** | **active** | AT-W1B-01 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested **active** before Project promotion.

---

## 3. Historical / current separation review

| Check | Analysis | Verdict |
|-------|----------|---------|
| **EFV-03** — two delivery phases on `bzpm.ru` | PRJ-0009 = ongoing catalog platform; PRJ-0010 = completed historical site (~5y) | **Pass** — two records; merge forbidden |
| Same hostname ≠ single Project | Triumph analog PRJ-0004 (deprecated) + PRJ-0005..0008 (active) on `gktriumph.ru` | **Pass** |
| PRJ-0009 operational truth first | P0 attested before P1 deprecated | **Pass** — AT-W3-ZPM-01 before AT-W3-ZPM-02 |
| Deprecated project + live property | PRJ-0010 **deprecated**; future WEB-* for `bzpm.ru` may remain **active** at Wave 4 | **Pass** — W3-ZPM-LC-05 |
| PM task vocabulary absent | Structural lifecycle only — LC-BAN-01 | **Pass** |
| PRJ-0010 not `done` / `closed` | **deprecated** per LT-P01 | **Pass** |

**Verdict:** **Pass** — historical/current separation valid; operator narrative and governance rules aligned.

---

## 4. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-PRJ-D-01** | PRJ-0009 vs PRJ-0010 — same hostname `bzpm.ru` | **Not duplicate** — sequential deliveries | No |
| **ZPM-PRJ-D-02** | PRJ-0009 vs FUT-01 SEO | **Distinct** — future held | No |
| **ZPM-PRJ-D-03** | vs Triumph PRJ-0004..0008 | **Distinct org** ORG-0005 vs ORG-0004 | No |
| **ZPM-PRJ-D-04** | vs future WEB-* | **Class boundary** | No |
| **ZPM-PRJ-D-05** | vs SITE-001 / SIBCAR | **Reject** — COR-W1B-03 | No |
| **ZPM-PRJ-D-06** | Name collision | **Resolved** — «(исходная версия)» | No |
| **ZPM-PRJ-D-07** | Catalog vs site stem | **Pass** | No |

**PRJ-0001..0010 namespace cross-check:**

| project_id | Status | Conflict with ZPM tranche |
|------------|--------|---------------------------|
| PRJ-0001 | Core Wave 3 — MARS internal | **None** — distinct slice |
| PRJ-0002, PRJ-0003 | Reserved — not minted | **None** — namespace free |
| PRJ-0004..0008 | Core Wave 3 — Triumph client_delivery | **None** — ORG-0004 vs ORG-0005 |
| PRJ-0009 | **This act** — ZPM catalog platform | — |
| PRJ-0010 | **This act** — ZPM historical site | — |

**Verdict:** **Pass** — no duplicate projects; no conflict with existing PRJ-0001..0010 roster.

---

## 5. Evidence sufficiency and attestation gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **W3-ZPM-EG-01** | ORG-0005 **active** before Project **active** | **Pass** — AT-W1B-01 |
| **W3-ZPM-EG-02** | Wave 2 ZPM Persons **active** | **Pass** — PER-0014, PER-0015 |
| **W3-ZPM-EG-03** | Wave 2B ZPM Person→Org complete | **Pass** — AT-W2B-ZPM-01 |
| **W3-ZPM-EG-04** | E0 structural attest path — client_delivery | **Pass** — both projects |
| **W3-ZPM-EG-05** | SIBCAR/SITE-001 excluded (EFV-02) | **Pass** — COR-W1B-03 |
| **W3-ZPM-EG-06** | EFV-03 — no merge PRJ-0009 + PRJ-0010 | **Pass** |
| **W3-ZPM-EG-07** | Duplicate batch before attestation | **Pass** — ZPM-PRJ-D-01..07 |
| **W3-ZPM-EG-08** | Human attest mandatory | **Pass** — this act |
| **W3-ZPM-EG-09** | P0 active before P1 deprecated | **Pass** — sequence honored |
| **W3-ZPM-EG-10** | No PM vocabulary at lifecycle | **Pass** — LC-BAN-01 |
| **W3-ZPM-EG-11** | Future candidates not minted | **Pass** — FUT-01..04 held |
| **W3-ZPM-EG-12** | No relationship edges in this package | **Pass** — scope restriction |

**Readiness checklist crosswalk:**

| Check ID | Assessment |
|----------|------------|
| W3-ZPM-S-01 | ORG-0005 **active** | **Pass** |
| W3-ZPM-S-02 | Wave 2 ZPM Persons **active** | **Pass** |
| W3-ZPM-S-03 | Wave 2B ZPM relationships **active** | **Pass** |
| W3-ZPM-S-04 | Project vs Organization boundary | **Pass** |
| W3-ZPM-E-01 | E0 structural attest path | **Pass** |
| W3-ZPM-E-02 | SIBCAR/SITE-001 excluded | **Pass** |
| W3-ZPM-E-03 | EFV-03 two-phase rule | **Pass** |
| W3-ZPM-D-01 | Duplicate batch complete | **Pass** |
| W3-ZPM-I-01 | PRJ-0009/0010 mint rules | **Pass** |
| W3-ZPM-I-02 | Not Jira/PM semantics | **Pass** |
| W3-ZPM-R-01 | Org edges deferred | **Pass** — Wave 3B-ZPM queue |
| W3-ZPM-R-02 | Website/Domain deferred | **Pass** |
| W3-ZPM-R-03 | Future candidates held | **Pass** |

**Verdict:** **Pass** — all gates satisfied for Project lifecycle promotion.

---

## 6. Attestation tranches executed

### 6.1 AT-W3-ZPM-01 — Active catalog platform (P0)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify ORG-0005 **active** | Steward | AT-W1B-01 | **Done** |
| 2 | Verify ORG-0001 **active** (execution context) | Steward | Wave 1 | **Done** |
| 3 | Verify PER-0014, PER-0015 **active** | Steward | AT-W2-ZPM-01..02 | **Done** |
| 4 | Duplicate scan ZPM-PRJ-D-01..07 | Steward | Register §7 | **Done** |
| 5 | Confirm EFV-03 — no merge with PRJ-0010 | Steward | Population §7 | **Done** |
| 6 | Propose PRJ-0009 canonical name | Steward | EV-ZPM-OP-ACT-01 | **Done** |
| 7 | Assign **E0**; record commissioning ORG-0005, execution ORG-0001 *(display)* | Steward | Operator scope | **Done** |
| 8 | Attest Project **active** | Steward (delegated) | Ongoing delivery discipline | **Done** |
| 9 | Queue 3B-ZPM: REL-ZPM-PJ-01, REL-ZPM-PJ-02 | Steward | Population §8 | **Queued** |

### 6.2 AT-W3-ZPM-02 — Historical site (P1)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Propose PRJ-0010 with version suffix disambiguation | Steward | EV-ZPM-OP-HIST-01 | **Done** |
| 2 | Confirm completed delivery — **deprecated** not `done` | Steward | LT-P01 | **Done** |
| 3 | Assign **E0** | Steward | Operator historical block | **Done** |
| 4 | Attest Project **deprecated** | Steward | Triumph PRJ-0004 analog | **Done** |
| 5 | Queue 3B-ZPM: REL-ZPM-PJ-03, REL-ZPM-PJ-04 | Steward | Population §8 | **Queued** |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create COMMISSIONED_BY edges | **Excluded** | Wave 3B-ZPM — separate pass |
| Create EXECUTES edges | **Excluded** | Wave 3B-ZPM — separate pass |
| Create BELONGS_TO edges | **Excluded** | Wave 4B |
| Create Person ↔ Project edges | **Excluded** | Operator scope |
| Create Website entities (`WEB-*`) | **Excluded** | Wave 4 |
| Create Domain entities (`DOM-*`) | **Excluded** | Wave 5 |
| Mint SEO / Advertising / AI / OCPilot Project rows | **Excluded** | FUT-01..04 held |
| Create CLIENT_OF ORG-0005 → ORG-0001 | **Excluded** | Wave 6 |

---

## 7. Attested entity records

### 7.1 PRJ-0009 — Каталог-платформа bzpm.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0009 |
| **intake_label** | ZPM-INTAKE-CAND-A01 |
| **canonical_name** | Каталог-платформа bzpm.ru |
| **population_slice** | **client_delivery** |
| **roster_priority** | **P0** |
| **commissioning organization** | ORG-0005 ЗПМ *(display; edge deferred Wave 3B-ZPM)* |
| **execution organization** | ORG-0001 Веб-студия «Полигон» *(display; edge deferred Wave 3B-ZPM)* |
| **related property** | `bzpm.ru` — **Website candidate** (Wave 4); not Project substitute |
| **related people (informational)** | PER-0014, PER-0015 — no edges minted |
| **attestation_basis** | E0 EV-ZPM-OP-ACT-01; ongoing catalog-platform delivery; almost complete; Polygon active WIP; duplicate review **Pass**; EFV-03 separation from PRJ-0010 |
| **evidence_tier** | **E0** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Residual technical/design/UX refinements — operator narrative; not ATLAS task objects. Wave 3B queue: REL-ZPM-PJ-01 COMMISSIONED_BY, REL-ZPM-PJ-02 EXECUTES. |

### 7.2 PRJ-0010 — Сайт bzpm.ru (исходная версия)

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0010 |
| **intake_label** | ZPM-INTAKE-CAND-H01 |
| **canonical_name** | Сайт bzpm.ru (исходная версия) |
| **population_slice** | **client_delivery** |
| **roster_priority** | **P1** |
| **commissioning organization** | ORG-0005 ЗПМ *(display; edge deferred Wave 3B-ZPM)* |
| **execution organization** | ORG-0001 Полигон *(display; edge deferred Wave 3B-ZPM)* |
| **related property** | `bzpm.ru` — same hostname as PRJ-0009; **different initiative** |
| **technology context** | WordPress + The7 + Custom development *(operator narrative)* |
| **related people (informational)** | PER-0014, PER-0015 — no edges minted |
| **attestation_basis** | E0 EV-ZPM-OP-HIST-01; completed delivery ~5 years ago; was in production; duplicate review **Pass**; LT-P01 **deprecated** not `done` |
| **evidence_tier** | **E0** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **deprecated** |
| **notes** | CC §17 indirect hostname corroboration only — does not name delivery phase. Wave 3B queue: REL-ZPM-PJ-03 COMMISSIONED_BY, REL-ZPM-PJ-04 EXECUTES. |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-ZPM-PJ-01 PRJ-0009 → ORG-0005 **COMMISSIONED_BY** | **Queued** — Wave 3B-ZPM |
| REL-ZPM-PJ-02 ORG-0001 → PRJ-0009 **EXECUTES** | **Queued** — Wave 3B-ZPM |
| REL-ZPM-PJ-03 PRJ-0010 → ORG-0005 **COMMISSIONED_BY** | **Queued** — Wave 3B-ZPM |
| REL-ZPM-PJ-04 ORG-0001 → PRJ-0010 **EXECUTES** | **Queued** — Wave 3B-ZPM |
| WEB-* `bzpm.ru` | **Not created** — Wave 4 |
| DOM-* `bzpm.ru` | **Not created** — Wave 5 |
| WEB → Project **BELONGS_TO** | **Deferred** — Wave 4B; SU-ZPM-PRJ-03 |
| Person ↔ Project edges | **Not created** |
| ZPM-INTAKE-FUT-01 SEO | **Held** — no start evidence |
| ZPM-INTAKE-FUT-02 Контекстная реклама | **Held** |
| ZPM-INTAKE-FUT-03 AI automation | **Held** |
| ZPM-INTAKE-FUT-04 OpenCartPilot maintenance | **Held** |
| REL-0016 CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** — Wave 6 |
| BZPM / SITE-001 OpenCart dealership | **Rejected** — COR-W1B-03 |
| Foundation documents | **Not modified** |

---

## 9. Residual gaps (non-blocking)

| ID | Project / topic | Gap | Severity | Mitigation |
|----|-----------------|-----|----------|------------|
| **ME-W3-ZPM-01** | PRJ-0010 | No contract-dated completion | Low | Operator «~5 years» narrative; E0 sufficient |
| **ME-W3-ZPM-02** | PRJ-0010 | No formal acceptance doc | Low | E1 upgrade path optional |
| **ME-W3-ZPM-03** | PRJ-0009 | No CC line for catalog rebuild | Low | E0 operator path sufficient |
| **ME-W3-ZPM-04** | Both | COMMISSIONED_BY / EXECUTES not minted | — | Wave 3B-ZPM by design |
| **ME-W3-ZPM-05** | Both | No WEB-* endpoint for `bzpm.ru` | Low | Wave 4 |
| **SU-ZPM-PRJ-01** | PRJ-0010 | Historical contract / act dates | Low | Narrative only |
| **SU-ZPM-PRJ-02** | PRJ-0010 | Formal acceptance document (E1 path) | Low | Optional upgrade |
| **SU-ZPM-PRJ-03** | Both | Deployment replace vs coexistence | Medium | Wave 4 WEB / 4B BELONGS_TO |
| **SU-ZPM-PRJ-04** | Both | Canonical name refinement | Low | Display only |
| **SU-ZPM-PRJ-05** | FUT-04 | OpenCartPilot scope if approved | Low | Future intake |
| **SU-ZPM-PRJ-06** | Both | PER-0014 / PER-0015 on Project | Low | No Person↔Project edges |
| **SU-ZPM-PRJ-07** | ORG-0005 | CLIENT_OF commercial edge | Medium | Wave 6 |
| **SU-ZPM-PRJ-08** | ORG-0005 | Production domain registrant | Low | Wave 5; ME-W1B-03 carry-forward |

**Blocking gaps remaining:** **None**

---

## 10. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 2 Project records only |
| No Foundation modification | **Pass** |
| No Wave 1 / Wave 2 / Wave 2B record modification | **Pass** |
| ORG-0005 endpoint **active** honored | **Pass** |
| Project vs Organization boundary | **Pass** |
| LT-P01 — PRJ-0010 **deprecated** not `done` | **Pass** |
| EFV-03 two-phase rule | **Pass** |
| SAFE UNKNOWN — no invented identifiers | **Pass** |
| No relationship edges created | **Pass** |
| No Website / Domain minted | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

---

## 11. Attestation verdict

```text
READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION
```

**Conditions met:**

1. PRJ-0009 **active** — ongoing catalog-platform client delivery attested at **E0** under EV-ZPM-OP-ACT-01.
2. PRJ-0010 **deprecated** — completed historical site delivery attested at **E0** under EV-ZPM-OP-HIST-01; LT-P01 honored.
3. Pre-check inventory, prerequisite endpoints, historical/current separation, duplicate review, and evidence gates — **all Pass**.
4. Wave 3B-ZPM candidates REL-ZPM-PJ-01..04 **queued** — Project endpoints now attested (**active** / **deprecated**).
5. FUT-01..04 remain **hold**; SEO / advertising / AI / OCPilot Project rows **not minted**.

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 3 ZPM PROJECT ATTESTATION** | [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) §13 | **Superseded** — both Project records now attested |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **PARTIALLY READY** | Both projects attested — no deferrals |
| **READY FOR WAVE 3 ZPM PROJECT ATTESTATION** | Superseded — attestation act complete |

**Downstream:** Execute Wave 3B-ZPM relationship population in a **separate pass** — REL-ZPM-PJ-01..04 (COMMISSIONED_BY + EXECUTES only).

---

## 12. Attestation results summary

| project_id | canonical_name | prior state | attested state | evidence_tier | tranche |
|------------|----------------|-------------|----------------|---------------|---------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **proposed** | **active** | **E0** | AT-W3-ZPM-01 |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **proposed** | **deprecated** | **E0** | AT-W3-ZPM-02 |

**Promotion count:** **2 / 2** Project records attested  
**Active promoted:** **1** (PRJ-0009)  
**Deprecated promoted:** **1** (PRJ-0010)  
**Relationships created:** **0**  
**Website / Domain entities created:** **0**  
**Person ↔ Project edges created:** **0**

---

## 13. Wave 3B-ZPM queue (post-attestation)

| Draft rel_id | source_id | target_id | relationship_type | prerequisite | readiness |
|--------------|-----------|-----------|-------------------|--------------|-----------|
| REL-ZPM-PJ-01 | PRJ-0009 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0009 **active** | **ready** |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 | **EXECUTES** | PRJ-0009 **active** | **ready** |
| REL-ZPM-PJ-03 | PRJ-0010 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | PRJ-0010 **deprecated** | **ready** |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 | **EXECUTES** | PRJ-0010 **deprecated** | **ready** |

---

## 14. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
        │
        ├── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 2B ZPM Relationship (REL-ZPM-01..02) ──► AT-W2B-ZPM-01..02 (COMPLETE)
        │
        └── Wave 3 ZPM Project (PRJ-0009, PRJ-0010) ──► AT-W3-ZPM-01..02 (THIS ACT)
                    │
                    └──► Wave 3B-ZPM Project Relationship Population (NEXT)
```

---

## 15. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Proposed register rows |
| [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) | Attestation sequence (superseded §13 verdict) |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 active basis |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Person→Org prerequisite |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster PRJ-0001..0008 |

---

*ATLAS Wave 3 ZPM Project Active Attestation v1 — documentation only.*
