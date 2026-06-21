# ATLAS Wave 3 Shpigovsky Project Population v1

**Status:** **documented** — Wave 3 Shpigovsky canonical Project population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) · [ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md](ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md) · [ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md](ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) · [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Wave 3B-SHPIG execution, attested canonical export.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization (ORG-0005): **COMPLETE** — unchanged
- Wave 1C SIBCAR Organization (ORG-0006): **COMPLETE** — unchanged
- Wave 1D Makita Organization (ORG-0007): **COMPLETE** — unchanged
- Wave 1D Shpigovsky Organization (ORG-0008): **COMPLETE** — AT-W1D-SHPIG-01
- Shpigovsky Project intake: **COMPLETE** — SHPIGOVSKY-INTAKE-CAND-PRJ-A01 accepted
- Population verdict: **READY FOR WAVE 3 SHPIGOVSKY PROJECT POPULATION**

**Binding operator scope (this tranche):**

- Mint **1** Project record only — single client delivery for `shpigovsky.ru`.
- **No** Website (`WEB-*`), Domain (`DOM-*`), or relationship edges.
- **No** Person creation; **No** Person ↔ Project edges.
- **No** separate Project rows per stack slice (SEO, Website Factory, WordPress, Frontend, ACF, custom programming).
- **No** historical, deprecated, or secondary Project.
- Commissioning / execution org fields — **display context**; structural edges deferred to Wave 3B-SHPIG.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Project** для Wave 3 tranche **Shpigovsky** (ORG-0008): состав, `PRJ-*` mint, классификация, lifecycle, evidence, org context, candidate relationships для Wave 3B-SHPIG, границы foundation.

**Normative scope Wave 3 Shpigovsky:**

```text
Project entity intake + attestation plan (1 record)
Wave 3B-SHPIG (отдельный пакет): Project ↔ Organization — только после Project endpoint attested
Wave 4 / 4B / 5 / 5B: Website / Domain для shpigovsky.ru — отдельные транши
```

---

## 2. Evidence pre-check (mandatory)

**Governance:** EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in this population |
|-----|----------|------|-------------------------|
| **EV-SHPIG-OP-01** | Operator intake statements (2026-06-10) | **E0** | Polygon delivery channel; role split; stack signals; i-SEO exclusion; Website Factory context |
| **EV-SHPIG-WEB-01** | Live capture `https://shpigovsky.ru/` (2026-06-10) | **E2** | Public property corroboration; brand context — **not** project boundary substitute |
| **EV-SHPIG-WEB-02** | Live capture `https://shpigovsky.ru/policy` (2026-06-10) | **E2** | Legal-operator signal ООО «Сознание» — org corroboration only |
| **AT-W1D-SHPIG-01** | [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) | attestation | ORG-0008 **active** at E1/E2 operational-public |

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-01** | «Шпиговский Дом» — brand notes only; canonical Project name uses hostname |
| **EFV-02** | MARS / Website Factory — operational context; **not** separate Project rows |
| **EFV-03** | Single delivery initiative on `shpigovsky.ru` → **one** Project; stack-slice split forbidden |
| **EFV-04** | CC absent — project boundary from operator delivery narrative; E0 sufficient |
| **EFV-06** | Each claim → evidence ref → operator block |

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Projects sheet — **no** Shpigovsky rows. Mint from intake + operator evidence only.

**Evidence tier (population):** **E0/E1** — E0 operator-direct path + E1 org anchor via ORG-0008 operational-public attestation.

---

## 3. Population roster (canonical)

**Identifier continuity:** PRJ-0001..0011 occupied (core Wave 3 + ZPM + SIBCAR tranches). This tranche mints **PRJ-0012**.

### 3.1 Summary table

| project_id | intake_label | canonical_name | population_slice | lifecycle_state *(target)* | roster_priority | commissioning_org | execution_org | evidence_tier | attestation_readiness |
|------------|--------------|----------------|------------------|------------------------------|-----------------|-------------------|---------------|---------------|----------------------|
| PRJ-0012 | SHPIGOVSKY-INTAKE-CAND-PRJ-A01 | Сайт shpigovsky.ru | **client_delivery** | **active** | **P0** | ORG-0008 ООО «Сознание» | ORG-0001 Полигон | **E0/E1** | **ready** |

**Lifecycle at population:** record minted as **proposed** pending steward attestation act.

---

## 4. Per-project analysis

### 4.1 PRJ-0012 — Сайт shpigovsky.ru

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0012 |
| **intake_label** | SHPIGOVSKY-INTAKE-CAND-PRJ-A01 |
| **canonical_name** | **Сайт shpigovsky.ru** |
| **population_slice** | **client_delivery** |
| **lifecycle_state (target)** | **active** — ongoing Polygon client delivery; operator describes technical execution roles (not ATLAS task objects) |
| **roster_priority** | **P0** |
| **commissioning organization** | ORG-0008 ООО «Сознание» |
| **execution organization** | ORG-0001 Веб-студия «Полигон» *(operator: Polygon delivery channel; display only)* |
| **related property** | `shpigovsky.ru` — **Website candidate** (Wave 4); not Project substitute |
| **goal (operator)** | Website delivery for Polygon client via Website Factory workflows |
| **delivery state** | **SAFE UNKNOWN** — roles and stack defined; completion boundary not stated |
| **technology context** | WordPress; possible ACF; possible custom programming *(operator narrative — not structural split)* |
| **related people (informational)** | PER-0010 Дягилева (acquisition; comms; coordination; SEO supervision; acceptance) — **no edges minted** |
| **evidence basis** | **E0** EV-SHPIG-OP-01; **E1** org anchor AT-W1D-SHPIG-01 |
| **CC corroboration** | **None** |
| **attestation readiness** | **Ready** at **E0/E1** — operator-confirmed ongoing client delivery (analog: PRJ-0011 SIBCAR; PRJ-0009 ZPM active) |

**Claim → evidence:**

- «Polygon client delivery; not i-SEO project channel» → **EV-SHPIG-OP-01**
- «Operator: frontend, WordPress, technical delivery» → **EV-SHPIG-OP-01**
- «Olga Dyagileva: acquisition, comms, coordination, SEO supervision, primary acceptance» → **EV-SHPIG-OP-01**
- «Website Factory / MARS / WordPress / possible ACF / custom code» → **EV-SHPIG-OP-01** — single delivery container; **no** per-stack Project split
- «Commissioning org ООО «Сознание»» → **AT-W1D-SHPIG-01** (ORG-0008 **active**)
- «Public property shpigovsky.ru exists» → **EV-SHPIG-WEB-01** — Website class at Wave 4; does not block Project population

---

## 5. Lifecycle decisions

| Rule | Application in Wave 3 Shpigovsky |
|------|----------------------------------|
| Ongoing client delivery → **active** | **PRJ-0012** — operator describes active technical delivery roles |
| No historical second phase evidenced | **No** deprecated Project — unlike ZPM PRJ-0009 + PRJ-0010 dual-phase model |
| No PM task statuses | PRJ-0012 — structural lifecycle only (LC-BAN-01) |
| Single delivery initiative | **No** split by SEO, Website Factory, WordPress, Frontend, ACF, custom programming |
| Attestation ordering | Single tranche **AT-W3-SHPIG-01** (P0 active) |
| Delivery phase precision | **SAFE UNKNOWN** — does not block **active** population at E0/E1 |

---

## 6. Explicit exclusions (not in population set)

### 6.1 Future candidates — hold

| intake_label | description | verdict |
|--------------|-------------|---------|
| SHPIGOVSKY-INTAKE-FUT-01 | WP automation agents | **Future Candidate — hold** |
| SHPIGOVSKY-INTAKE-FUT-02 | Extended SEO program as separate initiative | **Future Candidate — hold** |
| *(operator scope)* | Future Direct contract | **Future Candidate — hold** |
| *(operator scope)* | Future AI automation work | **Future Candidate — hold** |

**Basis:** EV-SHPIG-OP-01 — possibility / future scope only; no approved separate project / no start evidence.

### 6.2 Rejected candidates

| rejected_label | description | basis |
|----------------|-------------|-------|
| REJ-SHPIG-PRJ-01 | SEO supervision as separate Project | Operator: supervision on delivery ≠ separate approved initiative |
| REJ-SHPIG-PRJ-02 | Website Factory as separate Project | Workflow context — single delivery container |
| REJ-SHPIG-PRJ-03 | WordPress / Frontend / ACF / Custom programming split | EFV-03 — stack slices ≠ Project boundaries |
| REJ-SHPIG-PRJ-04 | `shpigovsky.ru` hostname alone | Website class — Wave 4 |
| REJ-SHPIG-PRJ-05 | ORG-0008 as Project | Entity taxonomy §3 |
| REJ-SHPIG-PRJ-06 | i-SEO project channel classification | EV-SHPIG-OP-01 explicit exclusion |
| REJ-SHPIG-PRJ-07 | Historical site version / redesign twin | No second delivery phase evidenced |

### 6.3 Scope exclusions (operator binding)

| Item | Treatment |
|------|-----------|
| Website entities (`WEB-*`) | **Not created** — Wave 4 |
| Domain entities (`DOM-*`) | **Not created** — Wave 5 |
| COMMISSIONED_BY / EXECUTES edges | **Not created** — Wave 3B-SHPIG |
| Person ↔ Project edges | **Not created** |
| PER-* mint | **Not created** — PER-0010 referenced only |
| LE-* mint | **Not created** — deferred |
| CLIENT_OF ORG-0008 → ORG-0001 | **Deferred** — Wave 6 |

---

## 7. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **SHPIG-PRJ-D-01** | PRJ-0012 vs ORG-0008 | Organization ≠ Project | **Class boundary** | No |
| **SHPIG-PRJ-D-02** | PRJ-0012 vs future WEB-* `shpigovsky.ru` | Project vs Website class boundary | **Class boundary** | No |
| **SHPIG-PRJ-D-03** | PRJ-0012 vs PRJ-0009..0011 | Different commissioning org ORG-0008 vs ORG-0005/0006 | **Distinct org context** | No |
| **SHPIG-PRJ-D-04** | PRJ-0012 vs FUT-01 WP automation | Future not started | **Distinct class** — future vs active | No |
| **SHPIG-PRJ-D-05** | PRJ-0012 vs FUT-02 SEO program | SEO supervision ≠ separate project | **Distinct** — future held | No |
| **SHPIG-PRJ-D-06** | Single vs multi-project on stack slices | WordPress, ACF, custom code — one delivery narrative | **Not duplicate** — EFV-03 single Project | No |
| **SHPIG-PRJ-D-07** | vs ORG-0001..0007 | No merge on hostname or trade name | **Distinct** — W1D-SHPIG-D-01..07 | No |
| **SHPIG-PRJ-D-08** | vs Makita / ZPM / SIBCAR projects | Mission-required integrity | **Distinct** — no collision | No |
| **SHPIG-PRJ-D-09** | Historical deprecated twin | No second delivery phase evidenced | **N/A** — no historical Project minted | No |

**Explicit validations (mission-required):**

| Claim | Verdict | Evidence |
|-------|---------|----------|
| ORG-0008 unchanged | **Confirmed** | Wave 1D attestation — no modification in this package |
| ORG-0001 unchanged | **Confirmed** | Display context only |
| Makita (ORG-0007) intact | **Confirmed** | SHPIG-PRJ-D-07 |
| ZPM (ORG-0005) intact | **Confirmed** | SHPIG-PRJ-D-03 |
| SIBCAR (ORG-0006) intact | **Confirmed** | SHPIG-PRJ-D-03 |
| No merge operations | **Confirmed** | Duplicate review |
| No Website / Domain creation | **Confirmed** | §6.3 |
| No Relationship creation | **Confirmed** | §6.3 |
| No Foundation changes | **Confirmed** | §10 |

**Duplicate review summary:** **Pass** — single attested-intake project minted; no merge required.

---

## 8. Candidate relationships for Wave 3B-SHPIG

**Not created in Wave 3 Shpigovsky.** Prepared for separate Wave 3B-SHPIG population pass after Project attestation.

### 8.1 Project → Organization COMMISSIONED_BY

| Draft rel_id | source_project | target_organization | Notes |
|--------------|----------------|---------------------|-------|
| REL-SHPIG-PJ-01 | PRJ-0012 Сайт shpigovsky.ru | ORG-0008 ООО «Сознание» | Active project |

### 8.2 Organization → Project EXECUTES

| Draft rel_id | source_organization | target_project | Notes |
|--------------|---------------------|----------------|-------|
| REL-SHPIG-PJ-02 | ORG-0001 Полигон | PRJ-0012 Сайт shpigovsky.ru | Operator: Polygon delivery channel |

### 8.3 Website → Project BELONGS_TO *(Wave 4B — deferred)*

| Draft rel_id | source_website | target_project | Prerequisite |
|--------------|----------------|----------------|--------------|
| *(TBD)* | WEB-* `shpigovsky.ru` | PRJ-0012 | **WEB-*** mint at Wave 4 |

**Wave 3B-SHPIG ordering note:** COMMISSIONED_BY + EXECUTES may proceed after PRJ-0012 **active** attestation; BELONGS_TO requires **active** Website endpoint (Wave 4).

---

## 9. SAFE UNKNOWN review

| ID | Topic | Impact | Posture | Blocks population |
|----|-------|--------|---------|-------------------|
| **SU-SHPIG-PRJ-01** | Contract dates | Lifecycle precision | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-02** | Acceptance dates | Lifecycle precision | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-03** | Legal signatory | E1 upgrade path | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-04** | Internal client contacts | Person / comms context | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-05** | Future SEO contract | Future intake | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-06** | Future Direct contract | Future intake | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-07** | Future AI automation work | Future intake FUT-01 | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-08** | Delivery phase (WIP vs complete %) | Narrative precision | **SAFE UNKNOWN** — operator roles only | **No** |
| **SU-SHPIG-PRJ-09** | ACF / custom programming scope approval | Stack detail | **SAFE UNKNOWN** | **No** |
| **SU-SHPIG-PRJ-10** | PER-0010 on Project | Informational only | Deferred — no Person↔Project edges | **No** |
| **SU-SHPIG-PRJ-11** | CLIENT_OF ORG-0008 → ORG-0001 | Commercial graph | **Wave 6** | **No** |
| **SU-SHPIG-PRJ-12** | Domain registrant | Wave 5 DOM-* | **SAFE UNKNOWN** | **No** |

---

## 10. Foundation consistency

| Foundation doc | Wave 3 Shpigovsky alignment |
|----------------|----------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project | Initiative container — not PM/tasks — **yes** |
| [ATLAS-BOUNDARIES-v1.md](../foundation/ATLAS-BOUNDARIES-v1.md) E-17 | MARS program ids excluded as Project rows — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | `active` only in this tranche — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | No deprecated twin without evidence — **yes** |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) | PRJ-0012 in PRJ-* namespace — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required before **active** — **yes** |
| EFV-01..06 | Intake discipline honored — **yes** |

**No new entity types.** **No foundation modifications.** **No relationship edges created.**

---

## 11. Readiness verdict

```text
READY FOR WAVE 3 SHPIGOVSKY PROJECT ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche **AT-W3-SHPIG-01** (PRJ-0012 **active**).
2. Wave 3B-SHPIG relationship population executes in a **separate pass** — REL-SHPIG-PJ-01..02 queued only.
3. Future candidates FUT-01..02 and future SEO / Direct / AI automation scope remain **hold** until operator supplies start evidence.
4. ORG-0001..0008, Makita, ZPM, SIBCAR — **unchanged**; no merge; no Website / Domain / Relationship mint.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md) | Canonical project roster table |
| [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | Source intake analysis |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster (PRJ-0001..0008) |

---

*ATLAS Wave 3 Shpigovsky Project Population v1 — documentation only; PRJ-0012 minted as **proposed** pending attestation act.*
