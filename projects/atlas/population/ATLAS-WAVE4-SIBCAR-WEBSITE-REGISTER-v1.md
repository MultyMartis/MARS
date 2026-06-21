# ATLAS Wave 4 SIBCAR Website Register v1

**Status:** **documented** — canonical Website roster after Wave 4 SIBCAR population (**proposed**; attestation pending).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR**  
**Parent:** [ATLAS-WAVE4-SIBCAR-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md)  
**Is not:** relationship registry, Domain registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Website population** Wave 4 tranche **SIBCAR**. Одна строка — одна approved Website record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **proposed** *(pending attestation)* | **1** (WEB-SIBCAR-01) |
| Lifecycle target **active** | **1** (WEB-SIBCAR-01) |
| Blocked / not minted | **1** (SIBCAR-INTAKE-WEB-02 — ME-W1C-02) |
| Relationship edges *(Wave 4B queue)* | **2** candidates — REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 |
| Attestation | **Pending** — AT-W4-SIBCAR-01 |

---

## 2. Website roster — full table

| website_id | canonical_name | website_kind | url | environment | primary_org_candidate | primary_project_candidate | evidence_tier | lifecycle_state | attestation_readiness | notes |
|------------|----------------|--------------|-----|-------------|----------------------|---------------------------|---------------|-----------------|----------------------|-------|
| WEB-SIBCAR-01 | sibcar.new-site.space | test_deployment | `https://sibcar.new-site.space/` | **TEST** | ORG-0006 SIBCAR | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **E0** | **proposed** | **ready** | Sole TEST web property; OCPilot SITE-001 crosswalk; intake SIBCAR-INTAKE-WEB-01 |

**Display-only fields** (`primary_org_candidate`, `primary_project_candidate`) — structural edges deferred to Wave 4B-SIBCAR.

**Blocked (not in roster):**

| intake_label | canonical_name | disposition | reason |
|--------------|----------------|-------------|--------|
| SIBCAR-INTAKE-WEB-02 | *(production)* | **rejected / not minted** | ME-W1C-02 — production public URL **SAFE UNKNOWN** |

---

## 3. Website roster — by lifecycle target

### 3.1 Active target (1 — pending attestation)

| website_id | canonical_name | website_kind | evidence_tier | lifecycle_state | attestation_readiness |
|------------|----------------|--------------|---------------|-----------------|----------------------|
| WEB-SIBCAR-01 | sibcar.new-site.space | test_deployment | **E0** | **proposed** → **active** | **ready** |

### 3.2 Deprecated (0)

*No Website entities target **deprecated** lifecycle in SIBCAR Wave 4 model.*

### 3.3 Blocked (1 — not minted)

| intake_label | url | reason |
|--------------|-----|--------|
| SIBCAR-INTAKE-WEB-02 | **SAFE UNKNOWN** | ME-W1C-02; SU-SIBCAR-PRJ-01 |

---

## 4. Single TEST property index

| Hostname | website_id | website lifecycle *(target)* | project_id | project lifecycle | BELONGS_TO *(Wave 4B queue)* |
|----------|------------|------------------------------|------------|-------------------|------------------------------|
| `sibcar.new-site.space` | WEB-SIBCAR-01 | **active** | PRJ-0011 | **active** | REL-SIBCAR-WB-01 *(queued)* |

**Policy:** One Website per TEST hostname property; single active Project (EFV-03). Production property deferred until URL known.

---

## 5. Aliases index (informational — not Wave 4 edges)

| website_id | aliases | alias_type |
|------------|---------|------------|
| WEB-SIBCAR-01 | Автосалон СИБКАР TEST; Автосалон СИБКАР | display / OCPilot site title |

**Disambiguation (W1C-D-05):** «Автосалон СИБКАР» — OCPilot site title / Website display context; **not** attested ORG-0006 alias. «СибКар» — ORG alias via LE-0005 / CC only.

**Organization aliases (not Website):** SIBCAR · СибКар · SibCar · ООО «СибКар» → ORG-0006 per AT-W1C-01.

**OCPilot crosswalk (documentation only):** SITE-001 → WEB-SIBCAR-01 — not a graph edge.

Hostname string `sibcar.new-site.space` attaches to **Domain** entity in Wave 5 — not a substitute for Website canonical_name ([ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4).

---

## 6. Platform metadata (consumer context — non-lifecycle)

| website_id | platform (OCPilot narrative) | consumer_program_refs |
|------------|------------------------------|----------------------|
| WEB-SIBCAR-01 | ocStore 3.0.3.8 (rs.2); baseline `ocstore-3038-rs2`; TEST env | OCPilot SITE-001; [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) |

Platform metadata does **not** substitute for lifecycle attestation.

---

## 7. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| **SIBCAR-INTAKE-WEB-02** | Production URL unknown | Deferred |
| DOM-* `sibcar.new-site.space` | Domain entity class | **Wave 5 SIBCAR** |
| REL-SIBCAR-WB-01 BELONGS_TO | Relationship family | **Wave 4B-SIBCAR** |
| REL-SIBCAR-WB-02 OWNS | Relationship family | **Wave 4B-SIBCAR** |
| PRIMARY_DOMAIN edges | Domain ↔ Website | **Wave 5B SIBCAR** |
| REL-0041 CLIENT_OF ORG-0006 → ORG-0001 | Already attested | **Wave 6B** — not re-minted |
| Person ↔ Website edges | Out of operator scope | Future expansion |
| WEB-ZPM-01 `bzpm.ru` | Distinct org ORG-0005 | ZPM tranche |
| Core Triumph WEB-0006..0009 | Distinct org ORG-0004 | Core Wave 4 |
| BZPM as Organization | Alias only — ORG-0005 **ЗПМ** | Identity rule |

---

## 8. Evidence index (population references)

| Ref | Artifact | Routing |
|-----|----------|---------|
| **EV-W1C-02** | OCPilot site-passport — SITE-001; TEST URL | WEB-SIBCAR-01 |
| **EV-W1C-03** | OCPilot project-access-brief — Business Goal; Planned Work | WEB-SIBCAR-01 · PRJ-0011 context |
| **EV-OCP-01..04** | Intake complete; SITE-001 registry; pilot narrative | WEB-SIBCAR-01 corroboration |
| **EV-W1C-CC-01** | `sibcar/Реквизиты.docx` | ORG-0006 org anchor only — **no** website field |
| **AT-W1C-01** | ORG-0006 **active** | WEB-SIBCAR-01 — org anchor |
| **AT-W3-SIBCAR-01** | PRJ-0011 **active** | WEB-SIBCAR-01 — project pairing |
| **AT-W3B-SIBCAR-01** | REL-SIBCAR-PJ-01..02 **active** | Commissioning / execution context |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only)
```

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 9. Deferred register (Wave 4B+ and future)

| Item | Reason | Target wave |
|------|--------|-------------|
| REL-SIBCAR-WB-01 WEB-SIBCAR-01 → PRJ-0011 **BELONGS_TO** | Website endpoint attestation prerequisite | **Wave 4B-SIBCAR** |
| REL-SIBCAR-WB-02 ORG-0006 **OWNS** WEB-SIBCAR-01 | Website endpoint attestation prerequisite | **Wave 4B-SIBCAR** |
| DOM-* + **PRIMARY_DOMAIN** `sibcar.new-site.space` → WEB-SIBCAR-01 | Hostname identity — hosting subdomain | **Wave 5B SIBCAR** |
| SIBCAR-INTAKE-WEB-02 production Website | Public URL **SAFE UNKNOWN** | **Deferred** — ME-W1C-02 |
| SIBCAR-INTAKE-FUT-03 PROD migration | No distinct boundary evidence yet | **Hold** |

---

## 10. Namespace cross-check

| website_id namespace | Tranche | org anchor | Conflict |
|---------------------|---------|------------|----------|
| WEB-0001..0005 | Core Wave 4 — operator sites | ORG-0001..0003 | **None** — deferred |
| WEB-0006..0009 | Core Wave 4 — Triumph | ORG-0004 | **None** — distinct client |
| WEB-ZPM-01 | ZPM tranche | ORG-0005 ЗПМ | **None** — distinct org / hostname |
| **WEB-SIBCAR-01** | **This register** | **ORG-0006 SIBCAR** | — |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-POPULATION-v1.md) | Per-website analysis and exclusions |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Project ↔ Organization context |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md) | Source intake register |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | ZPM tranche structural precedent |

---

*ATLAS Wave 4 SIBCAR Website Register v1 — WEB-SIBCAR-01 **proposed**; SIBCAR-INTAKE-WEB-02 **blocked / not minted**; attestation pending AT-W4-SIBCAR-01.*
