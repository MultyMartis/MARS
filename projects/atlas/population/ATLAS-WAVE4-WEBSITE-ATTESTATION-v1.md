# ATLAS Wave 4 Website Attestation v1

**Status:** **documented** — Wave 4 Website attestation sequence, evidence gates, readiness verdict.  
**Attestation authority note (FINDING-INT-03):** Core Triumph Website lifecycle (WEB-0006..0009) is **active** in population registers and attested as relationship endpoints in [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md). No standalone `*-ACTIVE-ATTESTATION-v1.md` was filed for this tranche. **SAFE UNKNOWN:** whether discrete steward acts AT-W4-01..03 were executed as separate human steps before Wave 4B — not separately documented.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Domain attestation, Wave 4B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Population verdict: **READY FOR WAVE 4 WEBSITE POPULATION**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 4 Website, минимальные evidence gates, readiness по каждому сайту, missing evidence, candidate relationships для Wave 4B, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 4 attestation scope

| In scope | Out of scope |
|----------|--------------|
| Website entity → **proposed** / **active** / **deprecated** | BELONGS_TO Website ↔ Project edges |
| Evidence tier assignment per website | OWNS / OPERATES Organization ↔ Website |
| Lifecycle structural state (no CMS/deploy vocabulary) | Domain entities (Wave 5) |
| Alias registration (display/brand) | PRIMARY_DOMAIN / SECONDARY_DOMAIN (Wave 5/6C) |
| Org/project **candidate** context (display) | Person ↔ Website edges |
| Wave 4B **queue preparation** | Foundation amendments |
| Operator org sites WEB-0001..0005 | Separate future tranche |

Wave 4B relationship **active** attestation executes in a **separate pass** after Website endpoints are **active**.

---

## 3. Attestation readiness by website

| website_id | Website | Target state | Min tier | Readiness | Blocker |
|------------|---------|--------------|----------|-----------|---------|
| WEB-0006 | gktriumph.ru | **active** | E1 | **Ready** | — |
| WEB-0007 | blog.gktriumph.ru | **active** | E1 | **Ready** | — |
| WEB-0008 | gruzotaxi-triumph.ru | **active** | E1 | **Ready** | — |
| WEB-0009 | manipulator-triumph.ru | **active** | E1 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Website to target lifecycle state now.
- All four websites: **Ready** — no conditional blockers.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W4-01 — Main corporate site

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify ORG-0004 **active** (Wave 1) | Steward | Wave 1 exit |
| 2 | Verify PRJ-0004 **deprecated**, PRJ-0006 **active** (Wave 3) | Steward | Wave 3 register |
| 3 | Propose WEB-0006 canonical name **gktriumph.ru** | Steward | Dataset + live URL |
| 4 | Register aliases; assign website_kind **corporate** | Steward | Population §3.1 |
| 5 | Assign E1; note PRJ-0004 deliverable + PRJ-0006 SEO context | Steward | Dataset + REL-0017/0021 |
| 6 | Attest Website **active** | Steward (delegated) or Owner | W4-LC-01 |
| 7 | Queue 4B: REL-0027; PRJ-0006 BELONGS_TO review | Steward | Population §6.1 |

### 4.2 Tranche AT-W4-02 — Blog subsite

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose WEB-0007 canonical name **blog.gktriumph.ru** | Steward | Dataset + live URL |
| 2 | Confirm distinct property from WEB-0006 (EIR-W01) | Steward | Hostname identity |
| 3 | Assign E1; website_kind **blog** | Steward | Dataset platform WordPress |
| 4 | Attest Website **active** | Steward | REL-0023 context |
| 5 | Queue 4B: REL-0028 | Steward | Population §6.1 |

### 4.3 Tranche AT-W4-03 — Triumph landings (batch)

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Propose WEB-0008, WEB-0009 | Steward | Dataset Websites sheet |
| 2 | Verify PRJ-0005, PRJ-0008 **active** | Steward | Wave 3 |
| 3 | Assign E1 per landing | Steward | Live URLs + EV-0005 |
| 4 | Attest **active** — WEB-0008, WEB-0009 | Steward | website_kind **landing** |
| 5 | Queue 4B: REL-0029, REL-0030; OWNS candidates | Steward | Population §6.2 |

---

## 5. Lifecycle attestation rules (Wave 4)

| Rule ID | Rule | Enforcement |
|---------|------|-------------|
| **W4-LC-01** | Live production client property → **active** | WEB-0006..0009 |
| **W4-LC-02** | Deprecated project + active website allowed | PRJ-0004 + WEB-0006 |
| **W4-LC-03** | Forbidden: CMS version, deploy id, PageSpeed as lifecycle | All |
| **W4-LC-04** | Staging hostname ≠ Website entity | No staging in roster |
| **W4-LC-05** | Hostname on Domain in Wave 5 — not Website alias substitute | Alias model §6.4 |

---

## 6. Missing evidence register

| ID | Website | Gap | Severity | Mitigation |
|----|---------|-----|----------|------------|
| **ME-W4-01** | WEB-0006 | Dual BELONGS_TO (PRJ-0004 vs PRJ-0006) | Low | Steward resolves at Wave 4B — both may coexist |
| **ME-W4-02** | WEB-0006..0009 | OWNS edges not yet attested | Low | Wave 4B queue |
| **ME-W4-03** | WEB-0006..0009 | PRIMARY_DOMAIN not minted | Low | Wave 5 Domain + Wave 6C |
| **ME-W4-04** | WEB-0008 | MIG pilot not fully executed | Low | E1 live site sufficient; MIG = support only |
| **ME-W4-05** | All Triumph | Contract/registrar primary path | — | OAR-BAN-01 — structural E1 sufficient |

**No blocking gaps.**

---

## 7. Readiness checklist crosswalk

| Check ID | Wave 4 Website package assessment |
|----------|-----------------------------------|
| W4-S-01 | Org anchor stable (ORG-0004 **active**) | **Pass** |
| W4-S-02 | Project endpoints available (PRJ-0004..0008) | **Pass** |
| W4-S-03 | Website vs Domain boundary | **Pass** — DOM deferred Wave 5 |
| W4-S-04 | Website vs Project boundary | **Pass** — PRJ-0006 not separate site |
| W4-E-01 | E1 client property attest path | **Pass** |
| W4-E-02 | Live URL evidence for all four | **Pass** |
| W4-E-03 | MIG / MARS packs = support only | **Pass** |
| W4-I-01 | WEB-* mint rules reviewed | **Pass** |
| W4-I-02 | Hostname ≠ opaque id semantics | **Pass** — canonical_name is display label |
| W4-R-01 | BELONGS_TO / OWNS deferred | **Pass** — Wave 4B queue |
| W4-R-02 | PRIMARY_DOMAIN deferred | **Pass** — Wave 5 |
| W4-R-03 | Operator sites WEB-0001..0005 excluded | **Pass** |

---

## 8. Wave 4B readiness assessment

### 8.1 Candidate relationship inventory

| Family | Count | Draft rel_ids | Endpoint prerequisite |
|--------|-------|---------------|----------------------|
| Website → Project **BELONGS_TO** | 4 (+1 candidate) | REL-0027..0030; PRJ-0006 TBD | Website **active** + Project **active/deprecated** |
| Organization → Website **OWNS** | 4 (TBD ids) | — | ORG-0004 **active** + Website **active** |
| Organization → Website **OPERATES** | 0–4 (steward choice) | — | ORG-0001 execution context |

### 8.2 Wave 4B prerequisites

| Prerequisite | Status |
|--------------|--------|
| ORG-0004 active (Wave 1) | **Met** |
| PRJ-0004..0008 attested (Wave 3) | **Met** (population package) |
| COMMISSIONED_BY edges (Wave 3B) | **Met** — REL-0017..0025 |
| Website population defined (Wave 4) | **Met** (this package) |
| Website attestation act executed | **Pending steward** — gates pass |
| Domain endpoints for PRIMARY_DOMAIN | **Not met** — Wave 5 (does not block BELONGS_TO / OWNS) |

---

## 9. Final verdict

### 9.1 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Wave 4 Website intake cannot start |
| **PARTIALLY READY** | Subset only; documented blockers |
| **READY FOR WAVE 4 WEBSITE ATTESTATION** | Full Website intake plan executable |
| **READY FOR WAVE 4B WEBSITE RELATIONSHIP POPULATION** | Website population complete; 4B relationship pass may proceed |

### 9.2 Assessment

| Criterion | Status |
|-----------|--------|
| All 4 required websites classified | **Pass** |
| Operator org sites excluded from roster | **Pass** |
| Lifecycle states — all **active** | **Pass** |
| Org endpoint ORG-0004 available | **Pass** |
| Project endpoints available | **Pass** |
| Evidence paths documented (E1) | **Pass** |
| Foundation consistency — no new entity types | **Pass** |
| Known gaps enumerated (ME-W4-01..05) | **Pass** — none blocking |
| Wave 4B candidates prepared | **Pass** — REL-0027..0030 + OWNS queue |

### 9.3 Verdict

```text
READY FOR WAVE 4B WEBSITE RELATIONSHIP POPULATION
```

**Conditions:**

1. Steward executes attestation tranches AT-W4-01..03 to promote four websites from population draft to canonical **active** before Wave 4B **active** relationship promotion.
2. Wave 4B **Phase A** (BELONGS_TO REL-0027..0030) may start immediately after Website attestation act.
3. Wave 4B **Phase B** (ORG-0004 OWNS WEB-0006..0009) follows same prerequisite; OPERATES for ORG-0001 is steward choice.
4. PRJ-0006 → WEB-0006 BELONGS_TO remains **review candidate** — not in dataset draft (SU-W3B-04).
5. Domain entities and PRIMARY_DOMAIN remain **Wave 5 / 6C** — not bundled into 4B.
6. Draft dataset lifecycle flags **do not substitute** for steward attestation acts.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website roster |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Prior wave prerequisite |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W4 check IDs |
| [ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md](ATLAS-WAVE3-PROJECT-ATTESTATION-v1.md) | Project attestation context |
