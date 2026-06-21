# ATLAS Wave 3 SIBCAR Project Population v1

**Status:** **documented** — Wave 3 SIBCAR canonical Project population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005 ООО «СибКар»  
**Parent:** [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md) · [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) · [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Wave 3B-SIBCAR execution, attested canonical export.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization (ORG-0006): **COMPLETE** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **COMPLETE** — AT-W6B-02
- SIBCAR operational slice audit: **COMPLETE** — SIBCAR-INTAKE-CAND-A01 accepted
- Population verdict (operational slice audit): **PARTIALLY READY** → ready for Wave 3 **proposal**

**Binding operator scope (this tranche):**

- Mint **1** Project record only — OpenCart dealership engagement.
- **No** Website (`WEB-*`), Domain (`DOM-*`), or relationship edges.
- **No** Person creation; **No** Person ↔ Project edges.
- **No** separate Project rows per planned-work checkbox (SEO, Yandex, theme, …).
- Commissioning / execution org fields — **display context**; structural edges deferred to Wave 3B-SIBCAR.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Project** для Wave 3 tranche **SIBCAR** (ORG-0006): состав, `PRJ-*` mint, классификация, lifecycle, evidence, org context, candidate relationships для Wave 3B-SIBCAR, границы foundation.

**Normative scope Wave 3 SIBCAR:**

```text
Project entity intake + attestation plan (1 record)
Wave 3B-SIBCAR (отдельный пакет): Project ↔ Organization — только после Project endpoint attested
Wave 4 / 4B / 5 / 5B: Website / Domain для sibcar.new-site.space — отдельные транши
```

---

## 2. Evidence pre-check (mandatory)

**Governance:** EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in this population |
|-----|----------|------|-------------------------|
| **EV-W1C-02** | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | **E0** | Engagement context; SITE-001; TEST URL; ocStore 3.0.3.8 |
| **EV-W1C-03** | OCPilot [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | **E0** | Business Goal; Planned Work; active WIP narrative |
| **EV-OCP-01** | [INTAKE-COMPLETE.md](../../../projects/ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | **E0** | Engagement corroboration |
| **EV-OCP-02** | [AUDIT-CHARTER.md](../../../projects/ocpilot/sites/site-001/AUDIT-CHARTER.md) | **E0** | Read-only audit scope — **not** Atlas Project substitute |
| **EV-OCP-03** | [project-site-registry.md](../../../projects/ocpilot/project-site-registry.md) | **E0** | SITE-001 registration row |
| **EV-OCP-04** | project-access-brief § Business Goal | **E0** | First combat OCPilot pilot narrative |
| **EV-W1C-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | **E1** | Org anchor ORG-0006 / LE-0005 only — **no** website on CC |
| **AT-W1C-01** | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0006 **active** |
| **AT-W6B-02** | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | attestation | REL-0041 **active** — vendor context ORG-0001 Полигон *(informational for display)* |

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-01** | «Автосалон СИБКАР» — OCPilot site title; **not** attested ORG alias (W1C-D-05) |
| **EFV-02** | OCPilot Run 5 / EAR program artifacts — engagement **context**, not separate Atlas Project rows |
| **EFV-03** | Single engagement narrative in EV-W1C-03 → **one** Project; per-checkbox split forbidden |
| **EFV-04** | CC read for org anchor; does not substitute project boundary |
| **EFV-06** | Each claim → evidence ref → operator/OCPilot block |

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Projects sheet — **no** SIBCAR rows. Mint from operational slice audit + OCPilot evidence only.

---

## 3. Project roster (canonical)

**Identifier continuity:** PRJ-0001..0010 occupied (core Wave 3 + ZPM tranche). This tranche mints **PRJ-0011**.

### 3.1 Summary table

| project_id | intake_label | canonical_name | population_slice | lifecycle_state *(target)* | roster_priority | commissioning_org | execution_org | evidence_tier | attestation_readiness |
|------------|--------------|----------------|------------------|------------------------------|-----------------|-------------------|---------------|---------------|----------------------|
| PRJ-0011 | SIBCAR-INTAKE-CAND-A01 | Автосалон СИБКАР — OpenCart dealership | **client_delivery** | **active** | **P0** | ORG-0006 SIBCAR | ORG-0001 Полигон | **E0** | **ready** |

**Lifecycle at population:** record minted as **proposed** pending steward attestation act.

**OCPilot crosswalk (documentation only — not graph edge):** SITE-001 → PRJ-0011.

---

## 4. Lifecycle analysis

### 4.1 PRJ-0011 — Автосалон СИБКАР — OpenCart dealership

| Field | Value |
|-------|-------|
| **project_id** | PRJ-0011 |
| **intake_label** | SIBCAR-INTAKE-CAND-A01 |
| **canonical_name** | Автосалон СИБКАР — OpenCart dealership |
| **population_slice** | **client_delivery** |
| **lifecycle_state (target)** | **active** — ongoing client delivery; rebranding, catalog import, SEO prep, OpenCart development (operator/OCPilot narrative; not ATLAS task objects) |
| **roster_priority** | **P0** |
| **commissioning organization** | ORG-0006 SIBCAR |
| **execution organization** | ORG-0001 Веб-студия «Полигон» *(REL-0041 + OCPilot operator context; display only)* |
| **related property** | `sibcar.new-site.space` — **Website candidate** (Wave 4 TEST); not Project substitute |
| **OCPilot crosswalk** | SITE-001 — engagement container; **distinct entity class** from Project |
| **current phase (OCPilot)** | INTAKE COMPLETE — Run 5 not authorized *(program state — not Atlas lifecycle)* |
| **technology context** | ocStore 3.0.3.8 (rs.2); TEST environment |
| **evidence basis** | **E0** EV-W1C-02, EV-W1C-03, EV-OCP-01..04 |
| **CC corroboration** | **None** for project scope — EV-W1C-CC-01 org anchor only |
| **commercial corroboration** | REL-0041 **active** — does not substitute project boundary |
| **attestation readiness** | **Ready** at **E0** — documented engagement narrative (analog PRJ-0009 ZPM active delivery) |

**Claim → evidence:**

- «OpenCart dealership engagement for SIBCAR client; rebranding; catalog; SEO prep; Yandex Direct prep; OpenCart dev» → **EV-W1C-03** Business Goal + Planned Work
- «Polygon vendor context» → **REL-0041** + AT-W6B-02 attestation basis
- «TEST deployment property» → **EV-W1C-02** test URL — Website class at Wave 4, not auto-Project (EFV-03)
- «First combat OCPilot pilot for audit/baseline workflow» → **EV-OCP-04** — program context; engagement container is PRJ-0011, not Run 5 program row

### 4.2 Lifecycle rules applied

| Rule | Application in Wave 3 SIBCAR |
|------|------------------------------|
| Ongoing client delivery → **active** | **PRJ-0011** — WIP per EV-W1C-03 |
| No PM task statuses | PRJ-0011 — structural lifecycle only (LC-BAN-01) |
| No historical second phase | **No** deprecated Project — unlike ZPM PRJ-0009 + PRJ-0010; no second delivery phase evidenced |
| INTAKE ≠ deprecated | OCPilot INTAKE phase is program vocabulary — Atlas target remains **active** WIP |
| Attestation ordering | Single tranche **AT-W3-SIBCAR-01** (P0 active) |

---

## 5. Evidence basis

| project_id | Primary evidence | Tier | Claim summary |
|------------|------------------|------|---------------|
| PRJ-0011 | EV-W1C-03 | **E0** | Rebranding ready dealership; catalog import; SEO + Yandex Direct prep; OpenCart development; OCPilot pilot context |
| PRJ-0011 | EV-W1C-02 | **E0** | SITE-001; «Автосалон СИБКАР»; TEST URL; ocStore baseline |
| PRJ-0011 | EV-OCP-01..03 | **E0** | Intake complete; SITE-001 registered; audit charter scope |
| *(org anchor)* | EV-W1C-CC-01 | **E1** | ORG-0006 / LE-0005 identity — **not** project boundary proof |
| *(commercial)* | AT-W6B-02 / REL-0041 | attestation | ORG-0006 **CLIENT_OF** ORG-0001 — vendor context only |
| *(prerequisite)* | AT-W1C-01 | attestation | ORG-0006 **active** |

**Evidence sufficiency:** E0 OCPilot + operator engagement path sufficient for client_delivery Project at population proposal (analog PRJ-0009 E0; PRJ-0005..0008 Triumph E1 optional upgrade path — not blocking).

---

## 6. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **SIBCAR-PRJ-D-01** | PRJ-0011 vs SITE-001 site_id | site_id = OCPilot engagement container; Project = client delivery initiative | **Class boundary** — crosswalk only | No |
| **SIBCAR-PRJ-D-02** | PRJ-0011 vs ORG-0006 SIBCAR | Organization ≠ Project | **Class boundary** | No |
| **SIBCAR-PRJ-D-03** | PRJ-0011 vs ORG-0005 BZPM / SITE-001 on BZPM | COR-W1B-03 identity pollution guard | **Distinct** — SIBCAR engagement belongs to ORG-0006 only | No |
| **SIBCAR-PRJ-D-04** | PRJ-0011 vs PRJ-0009 ZPM catalog | Different commissioning org ORG-0006 vs ORG-0005 | **Distinct org context** | No |
| **SIBCAR-PRJ-D-05** | Single vs multi-project on planned-work checkboxes | SEO, Yandex, theme — one engagement narrative | **Not duplicate** — EFV-03 single Project | No |
| **SIBCAR-PRJ-D-06** | «Автосалон СИБКАР» vs «СибКар» CC alias | Site title vs org alias | **Open — low** — W1C-D-05; Website intake note at Wave 4 | No |
| **SIBCAR-PRJ-D-07** | OCPilot Run 5 audit vs PRJ-0011 | MARS program activity | **Distinct** — Run 5 not minted as Project (REJ-SIBCAR-PRJ-01) | No |
| **SIBCAR-PRJ-D-08** | REL-0041 vs future COMMISSIONED_BY | Org commercial vs project structural | **Complementary** — not duplicate | No |

**Duplicate review summary:** **Pass** — single attested-intake project minted; no merge required; no second Project candidate evidenced.

---

## 7. Candidate Wave 3B relationships

**Not created in Wave 3 SIBCAR.** Prepared for separate Wave 3B-SIBCAR population pass after Project attestation.

### 7.1 Project → Organization COMMISSIONED_BY

| Draft rel_id | source_project | target_organization | Notes |
|--------------|----------------|---------------------|-------|
| REL-SIBCAR-PJ-01 | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | ORG-0006 SIBCAR | Active project |

### 7.2 Organization → Project EXECUTES

| Draft rel_id | source_organization | target_project | Notes |
|--------------|---------------------|----------------|-------|
| REL-SIBCAR-PJ-02 | ORG-0001 Полигон | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | REL-0041 + EV-W1C-03; ZPM analog REL-ZPM-PJ-02 |

### 7.3 Website → Project BELONGS_TO *(Wave 4B — deferred)*

| Draft rel_id | source_website | target_project | Prerequisite |
|--------------|----------------|----------------|--------------|
| REL-SIBCAR-WB-01 *(draft)* | WEB-* TEST `sibcar.new-site.space` | PRJ-0011 | **WEB-*** mint at Wave 4 |

**Wave 3B-SIBCAR ordering note:** COMMISSIONED_BY + EXECUTES may proceed after PRJ-0011 **active** attestation; BELONGS_TO requires **active** Website endpoint (Wave 4).

---

## 8. SAFE UNKNOWN inventory

| ID | Topic | Impact | Posture | Blocks population |
|----|-------|--------|---------|-------------------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Wave 4 production WEB | **SAFE UNKNOWN** — ME-W1C-02 | **No** |
| **SU-SIBCAR-PRJ-02** | Contract / SOW artifact | E1 upgrade path | **SAFE UNKNOWN** — E0 sufficient at population | **No** |
| **SU-SIBCAR-PRJ-03** | Formal project acceptance document | Lifecycle precision | **SAFE UNKNOWN** | **No** |
| **SU-SIBCAR-PRJ-04** | Canonical name refinement | Display only | Steward may refine at attestation | **No** |
| **SU-SIBCAR-PRJ-05** | Custom module development scope | Future intake FUT-02 | **SAFE UNKNOWN** — not started | **No** |
| **SU-SIBCAR-PRJ-06** | PROD migration / launch phase | Future intake FUT-03 | **SAFE UNKNOWN** | **No** |
| **SU-SIBCAR-PRJ-07** | Person contacts on CC (Карандашов) | Wave 2C optional | **SAFE UNKNOWN** — no Person creation in Wave 3 | **No** |
| **SU-W6B-04** | Project-level COMMISSIONED_BY / EXECUTES corroboration | Wave 3B readiness | **Closes at Wave 3** — population supplies PRJ-0011 endpoint | **No** |
| **SU-SIBCAR-PRJ-08** | EAR published snapshot for SITE-001 | OCPilot Run 5 — cross-program | **BLOCKED** on EAR path — not Atlas Project blocker | **No** |
| **SU-SIBCAR-PRJ-09** | Credential channel confirmation | EAR / OCPilot execution | **SAFE UNKNOWN** — EV-OCP-GAP-01 | **No** |

---

## 9. Explicit exclusions (not in population set)

### 9.1 Future candidates — hold

| intake_label | description | verdict |
|--------------|-------------|---------|
| SIBCAR-INTAKE-FUT-01 | Standalone Yandex Direct campaign | **Future Candidate — hold** |
| SIBCAR-INTAKE-FUT-02 | Custom module development | **Future Candidate — hold** |
| SIBCAR-INTAKE-FUT-03 | Production launch / PROD migration | **Future Candidate — hold** |

**Basis:** EV-W1C-03 checkboxes — components of single engagement; separate Project boundaries not evidenced.

### 9.2 Rejected candidates

| rejected_label | description | basis |
|----------------|-------------|-------|
| REJ-SIBCAR-PRJ-01 | OCPilot Run 5 read-only audit | MARS program — E-17; REJ-ZPM-PRJ-02 analog |
| REJ-SIBCAR-PRJ-02 | SITE-001 site_id as Project row | Class boundary — site_id ≠ Project |
| REJ-SIBCAR-PRJ-03 | ORG-0005 / BZPM engagement | Identity pollution — COR-W1B-03 |
| REJ-SIBCAR-PRJ-04 | Per-checkbox split (SEO, theme, …) | EFV-03 inference |
| REJ-SIBCAR-PRJ-05 | `sibcar.new-site.space` hostname alone | Website class — Wave 4 |
| REJ-SIBCAR-PRJ-06 | ORG-0006 as Project | Entity taxonomy §3 |
| REJ-SIBCAR-PRJ-07 | EAR acquisition program as Project | Cross-program — not client delivery container |

### 9.3 Scope exclusions (operator binding)

| Item | Treatment |
|------|-----------|
| Website entities (`WEB-*`) | **Not created** — Wave 4 |
| Domain entities (`DOM-*`) | **Not created** — Wave 5 |
| COMMISSIONED_BY / EXECUTES edges | **Not created** — Wave 3B-SIBCAR |
| Person entities / Person ↔ Project edges | **Not created** |
| REL-0041 CLIENT_OF | **Already attested** — Wave 6B; not re-minted |
| Production Website / Domain | **Deferred** — ME-W1C-02 |

---

## 10. Foundation consistency

| Foundation doc | Wave 3 SIBCAR alignment |
|----------------|-------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project | Initiative container — not PM/tasks — **yes** |
| [ATLAS-BOUNDARIES-v1.md](../foundation/ATLAS-BOUNDARIES-v1.md) E-17 | MARS program ids excluded as Project rows — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | `active` only in this tranche — **yes** |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) | PRJ-0011 in PRJ-* namespace — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required before **active** — **yes** |
| EFV-01..06 | Operational slice audit discipline honored — **yes** |

**No new entity types.** **No foundation modifications.** **No relationship edges created.**

---

## 11. Readiness assessment

```text
READY FOR WAVE 3 SIBCAR PROJECT ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche **AT-W3-SIBCAR-01** (PRJ-0011 **active**).
2. Wave 3B-SIBCAR relationship population executes in a **separate pass** — REL-SIBCAR-PJ-01..02 queued only.
3. Future candidates FUT-01..03 remain **hold** until operator supplies distinct delivery boundary evidence.
4. Do **not** mint OCPilot Run 5, EAR acquisition, or per-checkbox Project rows without start evidence.
5. SITE-001 remains **crosswalk documentation** — not a Project entity substitute.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Canonical project roster table |
| [ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Source expansion audit |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | Core Wave 3 roster (PRJ-0001..0008) |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | ZPM tranche precedent (PRJ-0009..0010) |

---

*ATLAS Wave 3 SIBCAR Project Population v1 — documentation only; PRJ-0011 minted as **proposed** pending attestation act.*
