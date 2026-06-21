# ATLAS Wave 4 SIBCAR Website Population v1

**Status:** **documented** — Wave 4 SIBCAR canonical Website population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005 ООО «СибКар»  
**Parent:** [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Domain population, Wave 4B execution, attested canonical export, active Website attestation act.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project PRJ-0011: **attested** — AT-W3-SIBCAR-01
- Wave 3B SIBCAR Project ↔ Organization: **COMPLETE** — AT-W3B-SIBCAR-01
- SIBCAR operational slice audit: **COMPLETE** — SIBCAR-INTAKE-WEB-01 accepted
- Population verdict (3B-SIBCAR): **READY FOR WAVE 4 SIBCAR WEBSITE POPULATION**

**Binding operator scope (this tranche):**

- Mint **1** Website record only — **WEB-SIBCAR-01** `sibcar.new-site.space` (**TEST** deployment).
- **Single Website model** — one TEST property; no production Website mint.
- **No** Domain (`DOM-*`), relationship edges, or Organization→Website / Person→Website edges.
- Org/project fields — **display candidates**; structural edges deferred to Wave 4B-SIBCAR / Wave 5 / Wave 5B.
- Treat `sibcar.new-site.space` as **TEST Website** — not production registrant proof.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Website** для Wave 4 tranche **SIBCAR** (ORG-0006): состав, `WEB-SIBCAR-01` mint, lifecycle, evidence, org/project context, candidate relationships для Wave 4B-SIBCAR, границы foundation.

**Normative scope Wave 4 SIBCAR:**

```text
Website entity intake + attestation plan (1 record — WEB-SIBCAR-01 TEST)
Wave 4B-SIBCAR (отдельный пакет): Website ↔ Project BELONGS_TO + ORG OWNS — только после Website endpoint attested
Wave 5 SIBCAR: Domain entities + PRIMARY_DOMAIN family для sibcar.new-site.space → WEB-SIBCAR-01
```

---

## 2. Identity rule (binding)

| Rule | Application |
|------|-------------|
| **ORG-0006 canonical name** | **SIBCAR** — per AT-W1C-01 |
| **Hostname `sibcar.new-site.space`** | TEST deployment property; operator/hosting namespace subdomain — **not** corporate production domain |
| **«Автосалон СИБКАР»** | OCPilot site title / display alias — **not** attested ORG alias (W1C-D-05; EFV-01) |
| **SITE-001** | OCPilot engagement crosswalk — documentation linkage; **not** Website entity substitute |
| **Do not create** any new Organization | ORG-0006 only |
| **EIR-W01** | One canonical website per business web property identity — **one** Website for TEST hostname |
| **No production Website assumptions** | SIBCAR-INTAKE-WEB-02 **BLOCKED** until public URL known (ME-W1C-02) |

---

## 3. Evidence pre-check (mandatory)

**Governance:** EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in this population |
|-----|----------|------|-------------------------|
| **EV-W1C-02** | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) | **E0** | SITE-001; TEST URL; ocStore 3.0.3.8; env **TEST** |
| **EV-W1C-03** | OCPilot [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | **E0** | Same TEST URL; business goal; planned work |
| **EV-OCP-01** | [INTAKE-COMPLETE.md](../../../projects/ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | **E0** | Engagement corroboration |
| **EV-OCP-02** | [AUDIT-CHARTER.md](../../../projects/ocpilot/sites/site-001/AUDIT-CHARTER.md) | **E0** | Read-only audit scope — not Website mint substitute |
| **EV-OCP-03** | [project-site-registry.md](../../../projects/ocpilot/project-site-registry.md) | **E0** | SITE-001 registry row |
| **EV-OCP-04** | project-access-brief § Business Goal | **E0** | First combat OCPilot pilot narrative |
| **EV-W1C-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx` | **E1** | Org anchor ORG-0006 / LE-0005 only — **no** website on CC |
| **AT-W1C-01** | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0006 **active** |
| **AT-W3-SIBCAR-01** | [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | attestation | PRJ-0011 **active** |
| **AT-W3B-SIBCAR-01** | [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | attestation | REL-SIBCAR-PJ-01..02 **active** |

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-01** | «Автосалон СИБКАР» — OCPilot site title; display alias on Website only — not ORG alias |
| **EFV-02** | ZPM / `bzpm.ru` — **not** used as SIBCAR Website evidence |
| **EFV-03** | Single engagement on TEST hostname → **one** Project (PRJ-0011) + **one** Website (WEB-SIBCAR-01) |
| **EFV-04** | CC silent on website — does not block TEST Website at E0 OCPilot path |
| **EFV-06** | Each website: claim → evidence ref → OCPilot block |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work; same TEST URL)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only — no website field)
```

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Websites sheet — **no** SIBCAR rows. Mint from Wave 3 SIBCAR attestation chain + OCPilot evidence only.

---

## 4. Website roster (canonical)

**Identifier scheme:** `WEB-SIBCAR-01` — SIBCAR tranche namespace (distinct from core Wave 4 Triumph roster WEB-0006..0009 and ZPM tranche WEB-ZPM-01).

### 4.1 Summary table

| website_id | canonical_name | website_kind | lifecycle_state *(target)* | roster_priority | primary_org_candidate | primary_project_candidate | evidence_tier | attestation_readiness |
|------------|----------------|--------------|------------------------------|-----------------|----------------------|---------------------------|---------------|----------------------|
| WEB-SIBCAR-01 | sibcar.new-site.space | **test_deployment** | **active** | **P0** | ORG-0006 SIBCAR | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **E0** | **ready** |

**Lifecycle at population:** WEB-SIBCAR-01 minted as **proposed** pending steward attestation act AT-W4-SIBCAR-01.

**OCPilot crosswalk (documentation only — not graph edge):** SITE-001 → WEB-SIBCAR-01.

**Intake label crosswalk:** SIBCAR-INTAKE-WEB-01 → WEB-SIBCAR-01.

---

## 5. Per-website analysis

### 5.1 WEB-SIBCAR-01 — sibcar.new-site.space (sole TEST web property)

| Field | Value |
|-------|-------|
| **website_id** | WEB-SIBCAR-01 |
| **intake_label** | SIBCAR-INTAKE-WEB-01 |
| **canonical_name** | sibcar.new-site.space |
| **website_kind** | **test_deployment** — operator TEST environment; ocStore 3.0.3.8 (rs.2) |
| **url** | `https://sibcar.new-site.space/` |
| **environment** | **TEST** — explicitly declared in EV-W1C-02; not production public URL |
| **lifecycle_state (target)** | **active** — ongoing TEST deployment for OpenCart dealership client delivery |
| **roster_priority** | **P0** |
| **primary_org_candidate** | ORG-0006 SIBCAR |
| **primary_project_candidate** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership |
| **display aliases** | «Автосалон СИБКАР TEST»; «Автосалон СИБКАР» *(OCPilot site title — W1C-D-05 note)* |
| **platform context** | ocStore 3.0.3.8 (rs.2); baseline `ocstore-3038-rs2`; OCPilot SITE-001 |
| **ocpilot_crosswalk** | SITE-001 — documentation linkage; **not** a graph edge |
| **evidence basis** | **E0** EV-W1C-02, EV-W1C-03, EV-OCP-01..04; PRJ-0011 **active** (AT-W3-SIBCAR-01); REL-SIBCAR-PJ-01..02 **active** (AT-W3B-SIBCAR-01) |
| **CC corroboration** | **None** for website — EV-W1C-CC-01 org anchor only; CC silent on domain (ME-W1C-05) |
| **attestation readiness** | **Ready** at **E0** — TEST URL corroborated in OCPilot package; not registrant / production proof |

**Claim → evidence:**

- «TEST deployment at `sibcar.new-site.space` for SIBCAR OpenCart engagement» → **EV-W1C-02** site-passport; **EV-W1C-03** project-access-brief
- «Single project on TEST hostname» → **PRJ-0011** **active**; EFV-03 single engagement rule
- «Org anchor SIBCAR» → **ORG-0006** **active** (AT-W1C-01); CC org anchor only
- «Not production public URL» → EV-W1C-03 public URL **SAFE UNKNOWN**; ME-W1C-02 — production Website deferred

### 5.2 SIBCAR-INTAKE-WEB-02 — production (not minted)

| Field | Value |
|-------|-------|
| **intake_label** | SIBCAR-INTAKE-WEB-02 |
| **url** | **SAFE UNKNOWN** |
| **disposition** | **Rejected / not minted** — ME-W1C-02 |
| **reason** | No production public URL in repo, CC, or OCPilot package |
| **target wave** | Deferred until URL evidence arrives |

---

## 6. Website policy — single TEST property model

**Operator-approved pattern:**

```text
same TEST hostname (sibcar.new-site.space)
one Website entity (WEB-SIBCAR-01 — active target)
one Project (PRJ-0011 active)
no production Website until URL known
```

| Layer | TEST delivery | Production delivery |
|-------|---------------|---------------------|
| **Project** | PRJ-0011 **active** | *(future intake — FUT-03 PROD migration)* |
| **Website** | WEB-SIBCAR-01 **active** *(target)* | **None minted** — SIBCAR-INTAKE-WEB-02 **BLOCKED** |

| Check | Verdict |
|-------|---------|
| Mint production Website without URL | **Rejected** — ME-W1C-02 |
| Merge SITE-001 into WEB-SIBCAR-01 | **N/A** — class boundary; crosswalk only |
| Single TEST hostname = single Website | **Pass** — EIR-W01 |
| TEST Website + active Project on same hostname | **Pass** — single engagement (EFV-03) |
| BELONGS_TO at Wave 4B | **Queued** — REL-SIBCAR-WB-01 |

**Attestation ordering:** **AT-W4-SIBCAR-01 only** — single TEST Website tranche.

---

## 7. Lifecycle analysis

| Rule ID | Rule | Application |
|---------|------|-------------|
| **W4-SIBCAR-LC-01** | Ongoing TEST deployment for active client delivery → **active** | **WEB-SIBCAR-01** — OpenCart WIP on TEST env |
| **W4-SIBCAR-LC-02** | Production property without URL → **not minted** | SIBCAR-INTAKE-WEB-02 **BLOCKED** |
| **W4-SIBCAR-LC-03** | Same TEST hostname · single Website | **WEB-SIBCAR-01** only |
| **W4-SIBCAR-LC-04** | TEST env explicitly declared — not production lifecycle | EV-W1C-02 env **TEST** |
| **W4-SIBCAR-LC-05** | Single-Project BELONGS_TO on TEST Website | REL-SIBCAR-WB-01 *(Wave 4B queue)* |
| **W4-SIBCAR-LC-06** | Forbidden: CMS version, deploy id as lifecycle | LC-BAN-01 — all |
| **W4-SIBCAR-LC-07** | Website without attested org at **active** | **Not applicable** — ORG-0006 **active** (AT-W1C-01) |
| **W4-SIBCAR-LC-08** | Hostname on Domain in Wave 5 | `sibcar.new-site.space` → **DOM-*** → WEB-SIBCAR-01 **PRIMARY_DOMAIN** |

**Verdict:** **Pass** — lifecycle aligned with Wave 3 SIBCAR Project attestation and TEST-only operator scope.

---

## 8. Explicit exclusions (not in population set)

### 8.1 Relationship and edge exclusions (operator binding)

| Item | Treatment |
|------|-----------|
| Website → Project **BELONGS_TO** | **Not created** — Wave 4B-SIBCAR |
| Organization → Website **OWNS** | **Not created** — Wave 4B-SIBCAR |
| Domain → Website **PRIMARY_DOMAIN** / **SECONDARY_DOMAIN** | **Not created** — Wave 5 / 5B |
| Domain entities (`DOM-*`) | **Not created** — Wave 5 SIBCAR |
| REL-0041 **CLIENT_OF** ORG-0006 → ORG-0001 | **Already attested** — Wave 6B; not re-minted |
| Person ↔ Website edges | **Not created** |
| **SIBCAR-INTAKE-WEB-02** production mint | **Forbidden** — ME-W1C-02 |

### 8.2 Rejected candidates

| rejected_label | description | basis |
|----------------|-------------|-------|
| REJ-SIBCAR-WEB-01 | Production Website without URL | ME-W1C-02; SU-SIBCAR-PRJ-01 |
| REJ-SIBCAR-WEB-02 | SITE-001 site_id as Website row substitute | Class boundary — site_id ≠ Website entity |
| REJ-SIBCAR-WEB-03 | `sibcar.new-site.space` as Organization | Entity taxonomy §3 |
| REJ-SIBCAR-WEB-04 | BZPM / ORG-0005 engagement property | COR-W1B-03; EFV-02 |
| REJ-SIBCAR-WEB-05 | Dataset v0.4 draft Website rows | No SIBCAR Website rows |
| REJ-SIBCAR-WEB-06 | Second TEST Website on same hostname | EIR-W01 |
| REJ-SIBCAR-WEB-07 | «Автосалон СИБКАР» as ORG alias mint | EFV-01; W1C-D-05 |

### 8.3 Future candidates — hold

| intake_label | description | verdict |
|--------------|-------------|---------|
| SIBCAR-INTAKE-FUT-03 | PROD migration / launch | **Hold** — production URL SAFE UNKNOWN |

---

## 9. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **SIBCAR-WEB-D-01** | WEB-SIBCAR-01 vs SITE-001 | Website vs OCPilot site_id class boundary | **Class boundary** — crosswalk only | No |
| **SIBCAR-WEB-D-02** | WEB-SIBCAR-01 vs PRJ-0011 | Website vs Project class boundary | **Class boundary** — complementary; BELONGS_TO at 4B | No |
| **SIBCAR-WEB-D-03** | WEB-SIBCAR-01 vs ORG-0006 | Website vs Organization class boundary | **Class boundary** — OWNS at 4B | No |
| **SIBCAR-WEB-D-04** | vs Triumph WEB-0006..0009 | Different org ORG-0006 vs ORG-0004 | **Distinct org context** | No |
| **SIBCAR-WEB-D-05** | vs WEB-ZPM-01 `bzpm.ru` | Different org ORG-0006 vs ORG-0005 | **Distinct org / hostname** | No |
| **SIBCAR-WEB-D-06** | «Автосалон СИБКАР» vs «СибКар» CC name | Display vs legal alias | **Open — low** — W1C-D-05 | No |
| **SIBCAR-WEB-D-07** | vs ORG-0005 BZPM | Identity pollution check | **Distinct** — COR-W1B-03 | No |
| **SIBCAR-WEB-D-08** | Merge with core WEB-0001..0005 namespace | Distinct tranche ids WEB-SIBCAR-* | **Pass** — namespace separation | No |
| **SIBCAR-WEB-D-09** | TEST vs production dual Website | Production URL unknown | **Pass** — single TEST mint only | No |

**Duplicate review summary:** **Pass** — one Website record; production candidate rejected.

---

## 10. Candidate relationships for Wave 4B-SIBCAR

**Not created in Wave 4 SIBCAR.** Prepared for separate Wave 4B-SIBCAR population pass after Website attestation.

### 10.1 Website → Project BELONGS_TO

| Draft rel_id | source_website | target_project | Prerequisite | Notes |
|--------------|----------------|----------------|--------------|-------|
| **REL-SIBCAR-WB-01** | WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | WEB-SIBCAR-01 **active**; PRJ-0011 **active** | Single-project single-property case |

### 10.2 Organization → Website OWNS *(deferred — not in Wave 4)*

| Draft rel_id | source_organization | target_website | Type | Notes |
|--------------|---------------------|----------------|------|-------|
| **REL-SIBCAR-WB-02** | ORG-0006 SIBCAR | WEB-SIBCAR-01 | **OWNS** | Operator TEST deployment; CC silent on domain |

### 10.3 Domain → Website PRIMARY_DOMAIN *(Wave 5 prerequisite)*

| Hostname | target_website | Type | Wave |
|----------|----------------|------|------|
| sibcar.new-site.space | WEB-SIBCAR-01 | **PRIMARY_DOMAIN** | **Wave 5B SIBCAR** — hosting subdomain policy |

**Wave 4B-SIBCAR ordering note:** BELONGS_TO + OWNS may proceed after Website attestation; PRIMARY_DOMAIN requires **DOM-*** mint at Wave 5 SIBCAR.

---

## 11. SAFE UNKNOWN inventory

| ID | Topic | Impact | Posture | Blocks population |
|----|-------|--------|---------|-------------------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Wave 4 production WEB | **SAFE UNKNOWN** — ME-W1C-02 | **No** — TEST path sufficient |
| **ME-W1C-02** *(carry-forward)* | Production public URL | SIBCAR-INTAKE-WEB-02 | **SAFE UNKNOWN** | **No** |
| **ME-W1C-05** *(carry-forward)* | Corporate domain not on CC | Domain OWNS / registrant | **SAFE UNKNOWN** | **No** |
| **W1C-D-05** *(carry-forward)* | «Автосалон СИБКАР» vs «СибКар» CC alias | Website display disambiguation | **Open — low** | **No** |
| **SU-W3B-SIBCAR-01** | WEB-* BELONGS_TO policy for TEST hostname | Wave 4B steward policy | **Resolved structurally** — REL-SIBCAR-WB-01 queued | **No** |
| **SU-SIBCAR-PRJ-06** | PROD migration (FUT-03) | Future production WEB | **Hold** | **No** |
| **SU-SIBCAR-PRJ-08** | EAR published snapshot for SITE-001 | OCPilot Run 5 — cross-program | **SAFE UNKNOWN** | **No** — not Website mint blocker |
| **EV-OCP-GAP-01** | Credential channel confirmation | EAR Run 5 execution | **SAFE UNKNOWN** | **No** |
| **SU-W4-SIBCAR-01** | Live URL probe timestamp for TEST hostname | E1 upgrade optional | **SAFE UNKNOWN** — E0 OCPilot path sufficient | **No** |
| **SU-W4-SIBCAR-02** | TEST subdomain registrant ORG-0006 | Wave 5 DOM-* OWNS defer | **SAFE UNKNOWN** — ZPM analog | **No** |
| **SU-W4-SIBCAR-03** | OWNS edge without registrar E1 | Wave 4B REL-SIBCAR-WB-02 | **Partial** — operator TEST deployment narrative | **No** |

**Blocking gaps remaining:** **None**

---

## 12. Foundation consistency

| Foundation doc | Wave 4 SIBCAR alignment |
|----------------|-------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4 Website | Web property identity — not deploy/CMS — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-W01..W04 | One property per TEST hostname — **yes** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4 | Brand titles as display aliases; hostname on DOM — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **active** TEST Website + **active** Project — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E0 OCPilot structural path — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) | Wave 4 after Project; org context available — **yes** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Single-Project BELONGS_TO allowed — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |
| EFV-01 | Site title ≠ org alias — **yes** |

**No new entity types.** **No foundation modifications.** **No relationship edges created.**

---

## 13. Readiness verdict

```text
READY FOR WAVE 4 SIBCAR WEBSITE ATTESTATION — SINGLE TEST WEBSITE (WEB-SIBCAR-01 ONLY)
```

**Conditions:**

1. Steward executes attestation tranche **AT-W4-SIBCAR-01** (WEB-SIBCAR-01 **active**) only.
2. **Do not** mint SIBCAR-INTAKE-WEB-02 — production URL **SAFE UNKNOWN** (ME-W1C-02).
3. Wave 4B-SIBCAR relationship population executes in a **separate pass** — REL-SIBCAR-WB-01 + REL-SIBCAR-WB-02 queued.
4. ORG-0006 canonical **SIBCAR**; «Автосалон СИБКАР» remains display alias on Website — not ORG alias (W1C-D-05).
5. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
6. DOM-* `sibcar.new-site.space` → WEB-SIBCAR-01 **PRIMARY_DOMAIN** at **Wave 5B SIBCAR**.
7. FUT-03 PROD migration remains **hold** until production URL evidence arrives.

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | Canonical website roster table |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY / EXECUTES context |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Source expansion audit §4 |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 4 SIBCAR Website Population v1 — documentation only; WEB-SIBCAR-01 minted as **proposed** pending attestation act.*
