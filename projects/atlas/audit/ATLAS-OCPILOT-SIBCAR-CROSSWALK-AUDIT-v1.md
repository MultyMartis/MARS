# ATLAS ↔ OCPilot SIBCAR Crosswalk Audit v1

**Status:** **documented** — cross-system identity and scope audit (audit only).  
**Program:** ATLAS — Business Reality Registry · OCPilot — operational execution layer  
**Audit date:** 2026-06-07  
**Auditor posture:** Registry Steward review (documentation-level)  
**Parent:** [ATLAS-OCPILOT-SIBCAR-CROSSWALK-REGISTER-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-REGISTER-v1.md) · [ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md)  
**Is not:** population, attestation, entity creation, relationship creation, Foundation amendment, registry modification, runtime export, git commit.

**Restrictions observed:** No new entities. No relationships. No lifecycle changes. No attestation. No population. No Foundation changes. No graph mutations.

---

# REPORT — Atlas ↔ OCPilot SIBCAR Crosswalk Audit

## 0. Goal and scope

**Goal:** Verify that the Atlas SIBCAR slice and OCPilot **SITE-001** represent the same business reality without duplication, drift, identity conflicts, or ownership ambiguity.

**Atlas entities in scope:**

| Class | ID | Lifecycle (authority) |
|-------|-----|----------------------|
| Organization | ORG-0006 SIBCAR | **active** — AT-W1C-01 |
| Legal Entity | LE-0005 ООО «СибКар» | **active** — AT-W1C-01 |
| Project | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **active** — AT-W3-SIBCAR-01 |
| Website | WEB-SIBCAR-01 `sibcar.new-site.space` | **active** — AT-W4-SIBCAR-01 |
| Domain | DOM-SIBCAR-01 `sibcar.new-site.space` | **proposed** — AT-W5-SIBCAR-01 pending |

**OCPilot object in scope:** **SITE-001** — Автосалон СИБКАР (slug `site-001`).

**Boundary model (enforced):**

```text
Atlas     = business reality (Organization, Legal Entity, Project, Website, Domain)
OCPilot   = operational execution (site workspace, audit runs, access brief, snapshots)
Crosswalk = documentation linkage only — not graph edges
```

---

## 1. Authority sources reviewed

### 1.1 Atlas

| Document | Role |
|----------|------|
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006, LE-0005 **active** |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | Organization roster + SITE-001 cross-ref §5 |
| [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | PRJ-0011 **active**; SITE-001 crosswalk |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](../population/ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | Project roster + OCPilot index §4 |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](../population/ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | REL-SIBCAR-PJ-01..02 **active** |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-SIBCAR-01 **active** |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](../population/ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | Website roster + SITE-001 crosswalk §5 |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](../population/ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | REL-SIBCAR-WB-01..02 **active** |
| [ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md](../population/ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md) | DOM-SIBCAR-01 **proposed** |

### 1.2 OCPilot

| Document | Role |
|----------|------|
| [site-passport.md](../../ocpilot/sites/site-001/site-passport.md) | Site identity, TEST URL, platform |
| [project-access-brief.md](../../ocpilot/sites/site-001/project-access-brief.md) | Access inventory, Business Goal, Planned Work |
| [AUDIT-CHARTER.md](../../ocpilot/sites/site-001/AUDIT-CHARTER.md) | Read-only audit authorization |
| [project-site-registry.md](../../ocpilot/project-site-registry.md) | Canonical OCPilot site registry |
| [materials/INTAKE-COMPLETE.md](../../ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | Intake closure attestation |
| [README.md](../../ocpilot/sites/site-001/README.md) | Container map and Run 5 gate |
| [OCPILOT-STATE.md](../../ocpilot/OCPILOT-STATE.md) | Program-level SITE-001 state |
| [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) | Atlas LE-0005 reference (execution layer) |
| [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) | Phase 1 authorization — NOT AUTHORIZED |

### 1.3 EAR references (informational — cross-program)

| Document | Role |
|----------|------|
| [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](../../../shared/external-access-runtime/EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) | Acquisition workflow example |
| [PILOT-001-SITE-001-SFTP-READONLY/](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/) | EAR pilot charter for SITE-001 |

**Evidence boundary:** External CC at `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\` referenced via Atlas attestation acts; not re-verified on filesystem in this pass. OCPilot external storage at `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` referenced but not inspected.

---

## 2. Crosswalk matrix

| Atlas entity | OCPilot object | Crosswalk type | Match | Notes |
|--------------|----------------|----------------|-------|-------|
| **ORG-0006** SIBCAR | SITE-001 client context | **documentation** | **Pass** | Same client; OCPilot uses trade title «Автосалон СИБКАР» — not org_id |
| **LE-0005** ООО «СибКар» | SITE-001 *(no LE row)* | **absent in OCPilot intake** | **Pass — expected** | Legal identifiers only in Atlas + change-auth reports |
| **PRJ-0011** | SITE-001 engagement | **documentation** | **Pass** | Same single OpenCart dealership delivery |
| **WEB-SIBCAR-01** | SITE-001 deployment | **documentation** | **Pass** | Same hostname, TEST env, ocStore 3.0.3.8 (rs.2) |
| **DOM-SIBCAR-01** | SITE-001 hostname string | **documentation** | **Partial** | Hostname match; Atlas Domain **proposed** — attestation pending |
| REL-SIBCAR-PJ-01..02 | *(not modeled in OCPilot)* | **n/a** | **Pass** | Org↔Project edges — Atlas only |
| REL-SIBCAR-WB-01..02 | *(not modeled in OCPilot)* | **n/a** | **Pass** | Website-family edges — Atlas only |

---

## 3. Required checks

### 3.1 Organization crosswalk — ORG-0006 vs SITE-001 client identity

| Field | Atlas ORG-0006 | OCPilot SITE-001 | Result |
|-------|----------------|------------------|--------|
| **Legal name** | ООО «СибКар» via LE-0005 | Not in passport/registry | **Pass — class boundary** |
| **Business identity** | SIBCAR (canonical); aliases SIBCAR · СибКар · SibCar | «Автосалон СИБКАР» site/project title | **Pass with note** — W1C-D-05 |
| **Client role** | **CLIENT** (W1-C) | Implicit client engagement | **Pass** |
| **Ownership consistency** | ORG-0006 owns business client identity | SITE-001 = operational container | **Pass** — no inversion |

**Reasoning:** OCPilot correctly treats SITE-001 as an **operational site_id**, not an Organization entity. Atlas attestation explicitly excludes SITE-001 from org identity proof (W1C-D-04 **Pass**). Trade title «Автосалон СИБКАР» is documented as OCPilot display context only — excluded from ORG alias register per EFV-01.

**Verdict:** **Pass**

---

### 3.2 Legal entity crosswalk — LE-0005 vs OCPilot client references

| Field | Atlas LE-0005 | OCPilot SITE-001 core docs | Result |
|-------|---------------|------------------------------|--------|
| **INN** | 5405512542 | **Absent** in passport, access brief, registry | **Pass — expected** |
| **OGRN** | 1265400004220 | **Absent** | **Pass — expected** |
| **KPP** | 540501001 | **Absent** | **Pass — expected** |
| **Legal name** | ООО «СибКар» | **Absent** in intake trio | **Pass — expected** |
| **Duplicate LE in OCPilot** | — | None minted | **Pass** |

**Supplementary OCPilot reference:** [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) cites **LE-0005 / EV-W1C-CC-01** for legal-block drafting — correct downstream consumption of Atlas authority, not a duplicate LE record.

**INN collision check:** INN 5405512542 unique in Atlas roster — no collision with ORG-0001..0005 (AT-W1C-01 §2.3).

**Verdict:** **Pass** — no duplicate legal entity in OCPilot; identifiers correctly centralized in Atlas.

---

### 3.3 Project crosswalk — PRJ-0011 vs SITE-001 engagement

| Criterion | Assessment |
|-----------|------------|
| Same project? | **Yes** — single ongoing OpenCart dealership client delivery |
| Different project? | **No** |
| Partial overlap? | **No** — EFV-03 single engagement rule honored |

**Evidence alignment:**

| Signal | Atlas PRJ-0011 | OCPilot SITE-001 |
|--------|----------------|------------------|
| Canonical name | Автосалон СИБКАР — OpenCart dealership | Project name / Site Name: Автосалон СИБКАР |
| Scope narrative | Rebranding, catalog import, SEO, OpenCart dev | Business Goal + Planned Work checkboxes (project-access-brief § Business Goal) |
| Technology | ocStore 3.0.3.8 (rs.2); TEST | Platform ocStore 3.0.3.8 (rs.2); Environment TEST |
| Crosswalk field | `ocpilot_crosswalk: SITE-001` | No `PRJ-0011` back-link in passport |
| Class boundary | SITE-001 ≠ Project entity (REJ-SIBCAR-PRJ-02) | SITE-001 is site workspace — not a second project |

**Reasoning:** Atlas and OCPilot describe **one engagement** at different abstraction layers. Atlas PRJ-0011 is the attested business Project; SITE-001 is the OCPilot operational container for that engagement. Run 5 read-only audit and EAR pilot are **explicitly excluded** from Project minting (REJ-SIBCAR-PRJ-01).

**Verdict:** **Pass** — same project; class boundaries preserved.

---

### 3.4 Website crosswalk — WEB-SIBCAR-01 vs SITE-001 deployment

| Field | Atlas WEB-SIBCAR-01 | OCPilot SITE-001 | Result |
|-------|---------------------|------------------|--------|
| **Hostname / URL** | `https://sibcar.new-site.space/` | Test URL: `https://sibcar.new-site.space/` | **Match** |
| **Environment** | **TEST** | **TEST** | **Match** |
| **Purpose** | test_deployment — OpenCart dealership WIP | ocStore dealership; first combat OCPilot pilot | **Match** |
| **Deployment identity** | WEB-SIBCAR-01; ocStore 3.0.3.8 (rs.2) | SITE-001; ocStore 3.0.3.8 (rs.2); baseline `ocstore-3038-rs2` | **Match** |
| **Public production URL** | **SAFE UNKNOWN** (SIBCAR-INTAKE-WEB-02 blocked) | Public URL **SAFE UNKNOWN** | **Match** |

**Verdict:** **Pass** — deployment facts consistent; no second Website implied by OCPilot.

---

### 3.5 Domain crosswalk — DOM-SIBCAR-01 vs SITE-001 hostname

| Field | Atlas DOM-SIBCAR-01 | OCPilot SITE-001 | Result |
|-------|---------------------|------------------|--------|
| **Hostname** | sibcar.new-site.space | sibcar.new-site.space (Test URL) | **Match** |
| **Environment** | **TEST** | **TEST** | **Match** |
| **Deployment** | hosting_subdomain on operator namespace | Same TEST deployment context | **Match** |
| **Lifecycle** | **proposed** → target **active** | N/A — OCPilot has no Domain class | **Partial** — Atlas W5 pending |
| **Registrar / ownership** | **SAFE UNKNOWN** | Hosting **SAFE UNKNOWN** | **Match — both unknown** |

**Note:** Parallel Website (WEB-SIBCAR-01 **active**) and Domain (DOM-SIBCAR-01 **proposed**) identities on the same hostname string is **by Atlas design** — linked only via future PRIMARY_DOMAIN at Wave 5B. Not a crosswalk conflict with OCPilot.

**Verdict:** **Pass with note** — hostname alignment confirmed; Domain attestation is Atlas-internal pending item.

---

### 3.6 Duplicate risk review

| Risk class | Check | Outcome |
|------------|-------|---------|
| Duplicate client representations | ORG-0006 vs SITE-001 as second org | **None** — class boundary enforced |
| Duplicate project identities | PRJ-0011 vs SITE-001 as Project | **None** — REJ-SIBCAR-PRJ-02 |
| Duplicate deployment identities | WEB-SIBCAR-01 vs SITE-001 as Website | **None** — SIBCAR-WEB-D-01 |
| Duplicate website concepts | Second hostname for SIBCAR in OCPilot | **None** — single TEST URL |
| SIBCAR vs BZPM pollution | ORG-0005 vs ORG-0006 | **Distinct** — COR-W1B-05 |
| Per-checkbox Project split | SEO / theme / Direct as separate projects | **None** — EFV-03 |

**Verdict:** **Pass** — no duplicate identities across systems.

---

### 3.7 Ownership boundary review

| Boundary | Expected | Observed | Result |
|----------|----------|----------|--------|
| Atlas = business reality | ORG, LE, PRJ, WEB, DOM canonical records | All SIBCAR entities attested or proposed under Atlas waves | **Pass** |
| OCPilot = operational execution | Site workspace, runs, access, snapshots | SITE-001 container + Run 5 / Phase 1 governance | **Pass** |
| No ownership inversion | OCPilot must not mint org/legal identity | OCPilot uses trade title only; LE refs via Atlas in auth reports | **Pass** |
| No identity conflicts | Single client, single engagement, single TEST deployment | Consistent across authority chain | **Pass** |
| REL-0041 vs project edges | Commercial CLIENT_OF complementary to COMMISSIONED_BY/EXECUTES | Documented in Wave 3B attestation | **Pass** |

**Verdict:** **Pass** — ownership boundaries respected; no inversion detected.

---

### 3.8 Drift review

| ID | Topic | Severity | System | Candidate sync action |
|----|-------|----------|--------|----------------------|
| **XW-SIBCAR-D-01** | OCPilot passport lacks Atlas crosswalk IDs (ORG-0006, PRJ-0011, WEB-SIBCAR-01) | Low | OCPilot | Add informational crosswalk block to site-passport |
| **XW-SIBCAR-D-02** | OCPilot project-site-registry lacks Atlas back-links | Low | OCPilot | Append crosswalk column or Notes link |
| **XW-SIBCAR-D-03** | OCPilot internal Run 5 status inconsistent across files | Medium | OCPilot | Reconcile passport vs access-brief vs README vs OCPILOT-STATE |
| **XW-SIBCAR-D-04** | «Автосалон СИБКАР» vs «СибКар» / SIBCAR naming | Low | Both | Document display policy (W1C-D-05) in OCPilot passport Notes |
| **XW-SIBCAR-D-05** | DOM-SIBCAR-01 **proposed** while WEB-SIBCAR-01 **active** | Low | Atlas | Complete Wave 5 attestation when ready — not OCPilot blocker |
| **XW-SIBCAR-D-06** | Production public URL unknown both sides | Medium | Both | ME-W1C-02 / SU-SIBCAR-PRJ-01 — hold until evidence |
| **XW-SIBCAR-D-07** | project-access-brief § Run 5 Readiness stale vs passport «READY FOR RUN 5» | Medium | OCPilot | Update access-brief gates after operator confirmation |
| **XW-SIBCAR-D-08** | EAR snapshot path not executed — Run 5 paused | Medium | OCPilot/EAR | Cross-program; SU-SIBCAR-PRJ-08 |

**Legacy names:** No legacy hostname or client alias conflicts found beyond documented W1C-D-05 trade-title variant.

**Stale references:** project-access-brief.md header still says «Run 5 not authorized» while site-passport.md and AUDIT-CHARTER.md say «READY FOR RUN 5»; OCPILOT-STATE.md reconciles to **paused** — authoritative for execution but intake trio remains inconsistent.

**Verdict:** **Findings present** — documentation drift only; no business-identity contradiction.

---

## 4. Finding list

| finding_id | Severity | Category | Summary | Blocking |
|------------|----------|----------|---------|----------|
| **FINDING-XW-SIBCAR-01** | Low | Crosswalk linkage | Atlas → OCPilot links exist; OCPilot core intake lacks Atlas ID back-references | No |
| **FINDING-XW-SIBCAR-02** | Medium | OCPilot doc drift | Run 5 authorization status inconsistent across SITE-001 intake documents | No |
| **FINDING-XW-SIBCAR-03** | Low | Naming | Trade title «Автосалон СИБКАР» vs CC legal «СибКар» — W1C-D-05 open | No |
| **FINDING-XW-SIBCAR-04** | Low | Atlas lifecycle | DOM-SIBCAR-01 **proposed** — Domain layer not yet attested | No |
| **FINDING-XW-SIBCAR-05** | Medium | SAFE UNKNOWN | Production public URL unknown on both sides — ME-W1C-02 | No |
| **FINDING-XW-SIBCAR-06** | Info | Cross-program | EAR Run 5 paused — operational bottleneck, not identity conflict | No |

**No blocking findings.**

---

## 5. Synchronization recommendations

| Priority | ID | Recommendation | Owner layer | Mutates graph? |
|----------|-----|----------------|-------------|----------------|
| **P1** | SYNC-XW-01 | Reconcile SITE-001 Run 5 status: align site-passport, project-access-brief, README, OCPILOT-STATE to single canonical gate narrative | OCPilot | **No** |
| **P2** | SYNC-XW-02 | Add Atlas crosswalk block to site-passport.md: ORG-0006 · PRJ-0011 · WEB-SIBCAR-01 · DOM-SIBCAR-01 *(proposed)* | OCPilot | **No** |
| **P2** | SYNC-XW-03 | Extend project-site-registry.md Notes with Atlas crosswalk pointer | OCPilot | **No** |
| **P3** | SYNC-XW-04 | Document W1C-D-05 site-title policy in OCPilot passport Notes (display vs legal vs org alias) | OCPilot | **No** |
| **P3** | SYNC-XW-05 | On Wave 5 SIBCAR Domain attestation completion, verify DOM-SIBCAR-01 register header sync | Atlas | **No** — doc sync only |
| **Hold** | SYNC-XW-06 | Production URL crosswalk — defer until operator supplies public URL evidence | Both | **No** |

**Explicitly not recommended in this audit:** minting entities, creating relationships, attestation acts, or merging SITE-001 into Atlas as an Organization/Project/Website record.

---

## 6. Risk assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Operator treats SITE-001 as legal client identity | Low | Medium | Class boundary documented; LE-0005 only in Atlas |
| Duplicate Project mint from OCPilot checkbox list | Low | Medium | EFV-03 enforced; REJ-SIBCAR-PRJ-01/02 |
| TEST hostname assumed as production domain | Low | High | Both systems mark TEST; production blocked ME-W1C-02 |
| Crosswalk treated as graph edge | Low | Medium | All crosswalk fields labeled documentation-only |
| OCPilot status drift causes premature Run 5 | Medium | Medium | SYNC-XW-01 reconciliation; OCPILOT-STATE as program authority |
| Name variant causes brand/legal block error | Low | Low | W1C-D-05 + change-auth review already flags |

**Overall risk posture:** **Low** — structural alignment strong; open items are documentation and SAFE UNKNOWN, not identity conflicts.

---

## 7. Readiness assessment

| Criterion | Status |
|-----------|--------|
| Same business client (ORG-0006 ↔ SITE-001 context) | **Ready** |
| Same engagement (PRJ-0011 ↔ SITE-001) | **Ready** |
| Same TEST deployment (WEB-SIBCAR-01 ↔ SITE-001) | **Ready** |
| Hostname alignment (DOM-SIBCAR-01 ↔ SITE-001) | **Ready** *(Domain attestation pending)* |
| No duplicate identities | **Ready** |
| Ownership boundaries clear | **Ready** |
| Bidirectional crosswalk documentation | **Partial** — Atlas complete; OCPilot intake incomplete |
| OCPilot operational doc consistency | **Partial** — FINDING-XW-SIBCAR-02 |
| Production URL crosswalk | **Not ready** — correctly deferred |

**Crosswalk readiness for downstream work:**

| Downstream | Prerequisite | Status |
|------------|--------------|--------|
| OCPilot Run 5 read-only audit | Charter + EAR path + consistent gates | **Blocked operationally** — not crosswalk |
| Atlas Wave 5 Domain attestation | Independent of OCPilot crosswalk | **Ready to proceed** |
| Phase 1 brand replacement (OCPilot) | Change-auth checklist | **NOT AUTHORIZED** — separate from crosswalk |
| Future production Website (SIBCAR-INTAKE-WEB-02) | Public URL evidence | **Blocked** — ME-W1C-02 |

---

## 8. Validation

| Check | Result |
|-------|--------|
| No new entities created | **Pass** |
| No relationships created | **Pass** |
| No lifecycle changes | **Pass** |
| No attestation executed | **Pass** |
| No population executed | **Pass** |
| No Foundation changes | **Pass** |
| No graph mutations | **Pass** |
| No git commit | **Pass** |

---

## 9. Final verdict

```text
PASS WITH FINDINGS
```

**Conditions:**

1. Atlas SIBCAR slice and OCPilot SITE-001 represent **the same business reality** — one client (SIBCAR / ООО «СибКар»), one engagement (OpenCart dealership), one TEST deployment (`sibcar.new-site.space`).
2. **No duplicate** client, project, or deployment identities across systems.
3. **No ownership inversion** — Atlas holds canonical business identity; OCPilot holds operational execution context.
4. **No identity conflicts** — INN/OGRN/KPP centralized in Atlas LE-0005; OCPilot does not mint competing legal records.
5. **Findings are non-blocking** — primarily missing OCPilot→Atlas back-links, OCPilot internal status drift, and open SAFE UNKNOWN items (production URL, Domain attestation pending).

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **PASS** | Documentation drift and partial bidirectional crosswalk prevent clean pass |
| **PARTIAL** | Core identity alignment is complete — drift is doc-level, not structural |
| **FAIL** | No contradictions in business facts, hostnames, or class boundaries |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-OCPILOT-SIBCAR-CROSSWALK-REGISTER-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-REGISTER-v1.md) | Crosswalk matrix and finding register |
| [ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-SUMMARY-v1.md) | Executive summary |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](../population/ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Prior Atlas expansion audit |
| [EAR-OCPILOT-INTEGRATION-v1.md](../../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md) | Cross-program integration model |

---

*ATLAS ↔ OCPilot SIBCAR Crosswalk Audit v1 — documentation only.*
