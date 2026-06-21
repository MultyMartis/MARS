# ATLAS Wave 3 ZPM Project Population v1

**Status:** **documented** — Wave 3 ZPM canonical Project population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004 ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»  
**Parent:** [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) · [ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md](ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md) · [ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md](ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md) · [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Wave 3B-ZPM execution, attested canonical export.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization (ORG-0005): **COMPLETE** — AT-W1B-01
- Wave 2 ZPM Persons (PER-0014, PER-0015): **COMPLETE** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- ZPM Project intake: **COMPLETE** — READY FOR ZPM WAVE 3 PROJECT POPULATION PROPOSAL
- Population verdict (2B-ZPM): **READY FOR WAVE 3 ZPM PROJECT POPULATION**

**Binding operator scope (this tranche):**

- Mint **2** Project records only — catalog platform (active) + historical site (deprecated).
- **No** Website (`WEB-*`), Domain (`DOM-*`), or relationship edges.
- **No** SEO, Context Advertising, AI Automation, or OpenCartPilot Project rows.
- **No** Person ↔ Project edges.
- Commissioning / execution org fields — **display context**; structural edges deferred to Wave 3B-ZPM.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Project** для Wave 3 tranche **ZPM** (ORG-0005): состав, `PRJ-*` mint, классификация, lifecycle, evidence, org context, candidate relationships для Wave 3B-ZPM, границы foundation.

**Normative scope Wave 3 ZPM:**

```text
Project entity intake + attestation plan (2 records)
Wave 3B-ZPM (отдельный пакет): Project ↔ Organization — только после Project endpoints attested
Wave 4 / 4B / 5 / 5B: Website / Domain для bzpm.ru — отдельные транши
```

---

## 2. Evidence pre-check (mandatory)

**Governance:** EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in this population |
|-----|----------|------|-------------------------|
| **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild | **E0** | PRJ-0009 active delivery |
| **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` delivery | **E0** | PRJ-0010 deprecated delivery |
| **EV-ZPM-OP-FUT-01** | Operator statement — future possibilities only | **E0** | Exclusion basis for FUT-01..04 |
| **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` | **E1** | Org anchor; §17 **Bzpm.ru** — indirect hostname corroboration only |
| **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** |
| **AT-W2B-ZPM-01** | [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | attestation | Person endpoints + vendor context ORG-0001 Полигон |

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-02** | SIBCAR/SITE-001, OCPilot audit — **not** used as Project evidence |
| **EFV-03** | Two delivery phases on `bzpm.ru` → **two** Project records; merge forbidden |
| **EFV-04** | CC read; §17 corroborates org website pointer — **not** project boundary substitute |
| **EFV-06** | Each project: claim → evidence ref → operator block |

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Projects sheet — **no** ZPM rows. Mint from intake + operator evidence only.

---

## 3. Population roster (canonical)

**Identifier continuity:** PRJ-0001..0008 occupied by core Wave 3; PRJ-0002/0003 reserved unused. This tranche mints **PRJ-0009**, **PRJ-0010**.

### 3.1 Summary table

| project_id | intake_label | canonical_name | population_slice | lifecycle_state *(target)* | roster_priority | commissioning_org | execution_org | evidence_tier | attestation_readiness |
|------------|--------------|----------------|------------------|------------------------------|-----------------|-------------------|---------------|---------------|----------------------|
| PRJ-0009 | ZPM-INTAKE-CAND-A01 | Каталог-платформа bzpm.ru | **client_delivery** | **active** | **P0** | ORG-0005 ЗПМ | ORG-0001 Полигон | **E0** | **ready** |
| PRJ-0010 | ZPM-INTAKE-CAND-H01 | Сайт bzpm.ru (исходная версия) | **client_delivery** | **deprecated** | **P1** | ORG-0005 ЗПМ | ORG-0001 Полигон | **E0** | **ready** |

**Lifecycle at population:** both records minted as **proposed** pending steward attestation act.

---

## 4. Per-project analysis

### 4.1 PRJ-0009 — Каталог-платформа bzpm.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0009 |
| **intake_label** | ZPM-INTAKE-CAND-A01 |
| **canonical_name** | Каталог-платформа bzpm.ru |
| **population_slice** | **client_delivery** |
| **lifecycle_state (target)** | **active** — ongoing client delivery; residual technical / design / UX refinements (operator narrative; not ATLAS task objects) |
| **roster_priority** | **P0** |
| **commissioning organization** | ORG-0005 ЗПМ |
| **execution organization** | ORG-0001 Веб-студия «Полигон» *(operator: Polygon; active WIP)* |
| **related property** | `bzpm.ru` — **Website candidate** (Wave 4); not Project substitute |
| **goal (operator)** | Full new version; transform into **catalog platform** |
| **delivery state** | Almost complete — active work in progress |
| **technology context** | Polygon delivery *(stack detail — operator narrative; not structural field)* |
| **related people (informational)** | PER-0014 Дубинский (primary operational); PER-0015 Крюков (sometimes) — **no edges minted** |
| **evidence basis** | **E0** EV-ZPM-OP-ACT-01 |
| **CC corroboration** | **None** for project scope |
| **attestation readiness** | **Ready** at **E0** — operator-confirmed ongoing client delivery (analog: PRJ-0005..0008 Triumph) |

**Claim → evidence:**

- «Клиент вернулся на полную новую версию; каталог-платформа; почти завершено; Polygon; active WIP» → **EV-ZPM-OP-ACT-01**

### 4.2 PRJ-0010 — Сайт bzpm.ru (исходная версия)

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0010 |
| **intake_label** | ZPM-INTAKE-CAND-H01 |
| **canonical_name** | Сайт bzpm.ru (исходная версия) |
| **population_slice** | **client_delivery** |
| **lifecycle_state (target)** | **deprecated** — completed delivery; structural retire per LT-P01 |
| **roster_priority** | **P1** |
| **commissioning organization** | ORG-0005 ЗПМ |
| **execution organization** | ORG-0001 Полигон *(operator: Polygon created ~5 years ago)* |
| **related property** | `bzpm.ru` — same hostname as PRJ-0009; **different initiative** |
| **technology context** | WordPress + The7 + Custom development |
| **delivery verdict** | **Completed** — was in production |
| **approximate age** | ~5 years *(operator estimate — not contract-dated)* |
| **evidence basis** | **E0** EV-ZPM-OP-HIST-01 |
| **CC corroboration** | **Indirect only** — EV-W1B-CC-01 §17 names org website **Bzpm.ru**; does not name delivery phase |
| **attestation readiness** | **Ready** at **E0** — steward-known completed client delivery (analog: PRJ-0004 Triumph redesign) |

**Claim → evidence:**

- «Polygon создал сайт ~5 лет назад; завершён; в production; WP + The7 + Custom» → **EV-ZPM-OP-HIST-01**

---

## 5. Lifecycle decisions

| Rule | Application in Wave 3 ZPM |
|------|---------------------------|
| Ongoing client delivery → **active** | **PRJ-0009** — catalog platform WIP |
| Completed delivery → **deprecated**, not `done` / `closed` | **PRJ-0010** — historical site initiative |
| No PM task statuses | Both projects — structural lifecycle only (LC-BAN-01) |
| Deprecated project + live property allowed | **PRJ-0010** deprecated; future **WEB-*** for `bzpm.ru` may remain **active** at Wave 4 |
| Same hostname ≠ single Project | **EFV-03** — PRJ-0009 and PRJ-0010 both valid |
| Attestation ordering | **P0 active first** (AT-W3-ZPM-01), then **P1 deprecated** (AT-W3-ZPM-02) |

---

## 6. Explicit exclusions (not in population set)

### 6.1 Future candidates — hold

| intake_label | description | verdict |
|--------------|-------------|---------|
| ZPM-INTAKE-FUT-01 | SEO (ZPM / bzpm.ru) | **Future Candidate — hold** |
| ZPM-INTAKE-FUT-02 | Контекстная реклама | **Future Candidate — hold** |
| ZPM-INTAKE-FUT-03 | AI automation (ZPM account) | **Future Candidate — hold** |
| ZPM-INTAKE-FUT-04 | OpenCartPilot-assisted maintenance | **Future Candidate — hold** |

**Basis:** EV-ZPM-OP-FUT-01 — possibility only; no approved project / no start evidence.

### 6.2 Rejected candidates

| rejected_label | description | basis |
|----------------|-------------|-------|
| REJ-ZPM-PRJ-01 | BZPM / SITE-001 OpenCart dealership | COR-W1B-03; EFV-02 |
| REJ-ZPM-PRJ-02 | OCPilot read-only audit | MARS program; no ATLAS Project |
| REJ-ZPM-PRJ-03 | MARS `ocpilot`, `ear-runtime`, … | E-17 excluded |
| REJ-ZPM-PRJ-04 | Single merged bzpm.ru Project (hist+current) | EFV-03 |
| REJ-ZPM-PRJ-05 | `bzpm.ru` hostname alone | Website class — Wave 4 |
| REJ-ZPM-PRJ-06 | ORG-0005 as Project | Entity taxonomy §3 |
| REJ-ZPM-PRJ-07 | Dataset v0.4 draft rows | No ZPM Project rows |

### 6.3 Scope exclusions (operator binding)

| Item | Treatment |
|------|-----------|
| Website entities (`WEB-*`) | **Not created** — Wave 4 |
| Domain entities (`DOM-*`) | **Not created** — Wave 5 |
| COMMISSIONED_BY / EXECUTES edges | **Not created** — Wave 3B-ZPM |
| Person ↔ Project edges | **Not created** |
| REL-0016 / CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** — Wave 6 |

---

## 7. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **ZPM-PRJ-D-01** | PRJ-0009 vs PRJ-0010 — same hostname `bzpm.ru` | Sequential client deliveries on one property; Triumph analog PRJ-0004 + ongoing site | **Not duplicate** — two Project records | No |
| **ZPM-PRJ-D-02** | PRJ-0009 vs FUT-01 SEO | SEO not started | **Distinct class** — future vs active | No |
| **ZPM-PRJ-D-03** | ZPM projects vs PRJ-0004..0008 Triumph | Different commissioning org ORG-0005 vs ORG-0004 | **Distinct org context** | No |
| **ZPM-PRJ-D-04** | PRJ-0010 vs future WEB-* | Project vs Website class boundary | **Class boundary** | No |
| **ZPM-PRJ-D-05** | SITE-001 narrative vs PRJ-0009 | SIBCAR context revoked | **Reject SITE-001** — not duplicate of catalog project | No |
| **ZPM-PRJ-D-06** | Canonical name «Сайт bzpm.ru» without suffix | Version suffix applied at population | **Resolved** — «(исходная версия)» | No |
| **ZPM-PRJ-D-07** | PRJ-0009 name vs PRJ-0010 stem | Disambiguated by «Каталог-платформа» vs «исходная версия» | **Pass** | No |

**Duplicate review summary:** **Pass** — two attested-intake projects minted; no merge required.

---

## 8. Candidate relationships for Wave 3B-ZPM

**Not created in Wave 3 ZPM.** Prepared for separate Wave 3B-ZPM population pass after Project attestation.

### 8.1 Project → Organization COMMISSIONED_BY

| Draft rel_id | source_project | target_organization | Notes |
|--------------|----------------|---------------------|-------|
| REL-ZPM-PJ-01 | PRJ-0009 Каталог-платформа bzpm.ru | ORG-0005 ЗПМ | Active project |
| REL-ZPM-PJ-03 | PRJ-0010 Сайт bzpm.ru (исходная версия) | ORG-0005 ЗПМ | Deprecated project — historical structural truth |

### 8.2 Organization → Project EXECUTES

| Draft rel_id | source_organization | target_project | Notes |
|--------------|---------------------|----------------|-------|
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 Каталог-платформа bzpm.ru | Operator: Polygon active WIP |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 Сайт bzpm.ru (исходная версия) | Operator: Polygon historical delivery |

### 8.3 Website → Project BELONGS_TO *(Wave 4B — deferred)*

| Draft rel_id | source_website | target_project | Prerequisite |
|--------------|----------------|----------------|--------------|
| *(TBD)* | WEB-* `bzpm.ru` | PRJ-0009 and/or PRJ-0010 | **WEB-*** mint at Wave 4; steward policy for dual-project hostname — **SU-ZPM-PRJ-03** |

**Wave 3B-ZPM ordering note:** COMMISSIONED_BY + EXECUTES may proceed after Project **active** / **deprecated** attestation; BELONGS_TO requires **active** Website endpoints (Wave 4) or explicit steward policy.

---

## 9. SAFE UNKNOWN review

| ID | Topic | Impact | Posture | Blocks population |
|----|-------|--------|---------|-------------------|
| **SU-ZPM-PRJ-01** | Historical project contract / act dates | Lifecycle precision | **SAFE UNKNOWN** — operator «~5 years» narrative only | **No** |
| **SU-ZPM-PRJ-02** | Historical formal acceptance document | E1 upgrade path | **SAFE UNKNOWN** — E0 sufficient for population | **No** |
| **SU-ZPM-PRJ-03** | Historical vs current deployment (replace vs coexist) | Wave 4 WEB-* / 4B BELONGS_TO | **SAFE UNKNOWN** | **No** |
| **SU-ZPM-PRJ-04** | Exact canonical name refinement | Display only | Steward may refine at attestation | **No** |
| **SU-ZPM-PRJ-05** | OpenCartPilot maintenance scope (FUT-04) | Future intake | **SAFE UNKNOWN** | **No** |
| **SU-ZPM-PRJ-06** | PER-0014 / PER-0015 on Project | Informational only | Deferred — no Person↔Project edges | **No** |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Commercial graph | **Wave 6** | **No** |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Wave 5 DOM-* | **SAFE UNKNOWN** (ME-W1B-03 carry-forward) | **No** |

---

## 10. Foundation consistency

| Foundation doc | Wave 3 ZPM alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project | Initiative container — not PM/tasks — **yes** |
| [ATLAS-BOUNDARIES-v1.md](../foundation/ATLAS-BOUNDARIES-v1.md) E-17 | MARS program ids excluded — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | `active`, `deprecated` only — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0010 deprecated not «done» — **yes** |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) | PRJ-0009/0010 in PRJ-* namespace — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required before **active** — **yes** |
| EFV-01..06 | Intake discipline honored — **yes** |

**No new entity types.** **No foundation modifications.** **No relationship edges created.**

---

## 11. Readiness verdict

```text
READY FOR WAVE 3 ZPM PROJECT ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranches **AT-W3-ZPM-01** (PRJ-0009 **active**) then **AT-W3-ZPM-02** (PRJ-0010 **deprecated**).
2. Wave 3B-ZPM relationship population executes in a **separate pass** — REL-ZPM-PJ-01..04 queued only.
3. Future candidates FUT-01..04 remain **hold** until operator supplies start evidence.
4. SIBCAR/SITE-001 project narratives remain **rejected** per COR-W1B-03.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Canonical project roster table |
| [ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) | Source intake analysis |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster (PRJ-0001..0008) |

---

*ATLAS Wave 3 ZPM Project Population v1 — documentation only; PRJ-0009/0010 minted as **proposed** pending attestation act.*
