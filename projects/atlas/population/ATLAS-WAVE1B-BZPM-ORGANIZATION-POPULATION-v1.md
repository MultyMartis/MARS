# ATLAS Wave 1B BZPM Organization Population v1

**Status:** **documented** — Wave 1B canonical Organization population plan for second real client (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md)  
**Companion:** [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md)  
**Is not:** runtime, API, automation, database schema, attested registry export, Counterparty Card file.

**Wave 1 prerequisite:** Organizations Wave 1 (ORG-0001..0004) — status **COMPLETE** (operator, 2026-06-06).

**Wave 1B intent:**

Validate that a **second real client** organization can be populated using the **existing Organization model** — without Foundation changes, without new entity classes, mirroring W1-B (Triumph) discipline for **BZPM**.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Organization** для Wave 1B tranche **BZPM**: identity, legal entity linkage, aliases, website/domain candidates, evidence, duplicate review, attestation readiness, и downstream candidates (Person, Project, Website, Domain).

**Normative scope Wave 1B:**

```text
Organization entity intake + attestation plan (single org: BZPM)
Wave 2B-BZPM (future): Person ↔ Organization — только после active ORG-0005
Wave 3+ (future): Project / Website / Domain — только после org anchor
Wave 6+ (future): CLIENT_OF ORG-0005 → ORG-0001 — только после org active + commercial review
```

**Binding operator context:**

- **BZPM** — operator project codename for active dealership / OpenCart support engagement ([EAR-CONNECTED-ACQUISITION-v1.md](../../../shared/external-access-runtime/EAR-CONNECTED-ACQUISITION-v1.md), [EAR-ACQUISITION-TRACKS-v1.md](../../../shared/external-access-runtime/EAR-ACQUISITION-TRACKS-v1.md)).
- **SITE-001** — OCPilot managed site **Автосалон СИБКАР** ([projects/ocpilot/sites/site-001/site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md)) — **Website / project context**, not a separate Organization.
- **ORG-0005** — proposed canonical Organization id (next after ORG-0004 Триумф).

---

## 2. Population roster (canonical)

Источник: operator-approved Wave 1B tranche; OCPilot SITE-001 operational docs; EAR Phase 2E architecture references.  
**Не** в [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) — Wave 1B — post-dataset expansion tranche.

### 2.1 Summary table

| org_id | canonical_name | wave_tier | business_role | legal_entity_id | lifecycle (target) | evidence_tier (population) | attestation readiness |
|--------|----------------|-----------|---------------|-----------------|-------------------|---------------------------|----------------------|
| ORG-0005 | BZPM | **W1-B** | **CLIENT** | **LE-0004** *(proposed)* | **proposed** | **E1** *(operational corroboration)* | **partially ready** |

**Wave tier:** W1-B — active client / third-party organization ([ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) §2.1).

---

## 3. Organization identity analysis

### 3.1 ORG-0005 — BZPM

| Field | Value |
|-------|-------|
| **org_id** | ORG-0005 |
| **canonical_name** | BZPM |
| **lifecycle_state (population)** | **proposed** |
| **wave_tier** | W1-B |
| **business_role** | **CLIENT** — commercial counterparty receiving Polygon delivery / OCPilot support |
| **legal_entity_id** | **LE-0004** *(proposed placeholder — see §4)* |
| **primary_contact_person_id** | **SAFE UNKNOWN** |
| **primary_website (display candidate)** | **SAFE UNKNOWN** (production); TEST: `sibcar.new-site.space` |
| **primary_domain (display candidate)** | **SAFE UNKNOWN** (production); candidate subdomain context: `new-site.space` |
| **edo_enabled** | **SAFE UNKNOWN** |
| **notes** | Second real client validation tranche; CC not yet in external storage; SITE-001 ≠ Organization |

### 3.2 Identity disambiguation

| Signal | Resolution |
|--------|------------|
| **BZPM** vs **Автосалон СИБКАР** | **Same Organization** — BZPM = operator codename; SIBCAR = client trade / site brand → **aliases**, not second org |
| **BZPM** vs **SITE-001** | **Different entity classes** — SITE-001 = OCPilot `site_id` / future ATLAS Website; ORG-0005 = business counterparty |
| **BZPM** vs **Triumph (ORG-0004)** | **Distinct clients** — no merge; separate W1-B records |
| **BZPM** vs **Polygon / MetaCode / i-SEO** | **Distinct** — operator orgs remain ORG-0001..0003 |
| **sibcar** hostname | **Website candidate** (Wave 4+) — [OAR-BAN-03](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) — hostname does not create Organization |

---

## 4. Legal entity analysis

### 4.1 Proposed LE-0004

| Field | Value |
|-------|-------|
| **legal_entity_id** | LE-0004 *(proposed — not attested)* |
| **legal_entity_name** | **SAFE UNKNOWN** |
| **entity_type** | **SAFE UNKNOWN** (ООО / ИП / other — pending CC) |
| **inn** | **SAFE UNKNOWN** |
| **ogrn_ogrnip** | **SAFE UNKNOWN** |
| **kpp** | **SAFE UNKNOWN** |
| **legal_address** | **SAFE UNKNOWN** |
| **document_signatory** | **SAFE UNKNOWN** |
| **lifecycle** | **proposed** |
| **notes** | No LegalEntities row in Wave 1 dataset; LE-0004 reserved for BZPM org binding at CC intake |

### 4.2 Legal entity readiness

| Check | Result |
|-------|--------|
| CC provides legal name + INN/OGRN | **Fail** — CC not present in repo or listed external storage |
| Registry extract alternate (E2) | **Not attempted** — no steward rationale on file |
| Operator E0-only path for W1-B | **Prohibited** — W1-B requires E1+ ([ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) §3.2) |
| LE-0004 may attest **active** without org CC | **No** — legal entity fields require CC or E2 extract |

**Gap register:**

| Gap ID | Topic | Severity |
|--------|-------|----------|
| **ME-W1B-01** | No Counterparty Card in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` | **Blocking** for **active** attest |
| **ME-W1B-02** | Legal entity name / INN / OGRN unknown | **Blocking** for **active** attest |
| **ME-W1B-03** | Production public URL unknown | Low — non-blocking for org **proposed** |
| **ME-W1B-04** | BZPM acronym expansion not documented | Low — alias register only |

---

## 5. Aliases

Per [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) — aliases attach to **one** ORG-0005; do not mint parallel orgs.

| Alias | Type | Evidence | Attestation state |
|-------|------|----------|-------------------|
| BZPM | Operator codename / canonical | EAR Phase 2E docs; operator context | **proposed** |
| Автосалон СИБКАР | RU trade / site brand | OCPilot SITE-001 passport | **proposed** |
| SIBCAR | Latin trade / hostname stem | `sibcar.new-site.space` | **proposed** |
| СИБКАР | Cyrillic abbreviation | Same as SIBCAR | **proposed** |
| SITE-001 | **Rejected as org alias** | OCPilot site id — wrong entity class | **Not registered** |

**Alias duplicate review:** No alias in scope collides with ORG-0001..0004 canonical names or primary aliases at D1 level.

---

## 6. Website and domain candidates (future waves)

**Not populated in Wave 1B.** Display candidates only — for Wave 4 / Wave 5 planning.

### 6.1 Candidate websites

| Candidate | Hostname / URL | website_kind (candidate) | org_candidate | evidence | wave |
|-----------|----------------|--------------------------|---------------|----------|------|
| WEB-* TBD | `https://sibcar.new-site.space/` | **corporate** *(dealership)* | ORG-0005 | OCPilot access brief; TEST environment | Wave 4 |
| WEB-* TBD | Public production URL | **corporate** | ORG-0005 | **SAFE UNKNOWN** | Wave 4 |

### 6.2 Candidate domains

| Candidate | FQDN | domain_kind (candidate) | org_candidate | evidence | wave |
|-----------|------|-------------------------|---------------|----------|------|
| DOM-* TBD | `sibcar.new-site.space` | subdomain FQDN | ORG-0005 *(indirect)* | TEST URL only — not production registrant proof | Wave 5 |
| DOM-* TBD | Production apex | apex | ORG-0005 | **SAFE UNKNOWN** | Wave 5 |

**Discipline:** Website hostname corroborates org context only after ORG-0005 **active**; Domain OWNS requires registrar E1 per Wave 5 / 5B gates ([ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md)).

---

## 7. Evidence review

### 7.1 Evidence inventory

| Ref | Artifact | Tier | Role for ORG-0005 |
|-----|----------|------|-------------------|
| EV-W1B-01 | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) — SITE-001 Автосалон СИБКАР | E1 | Operational corroboration — client identity context |
| EV-W1B-02 | OCPilot [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | E1 | TEST URL; environment; access inventory |
| EV-W1B-03 | [INTAKE-COMPLETE.md](../../../projects/ocpilot/sites/site-001/materials/INTAKE-COMPLETE.md) | E1 | Operator intake closure marker |
| EV-W1B-04 | EAR [EAR-CONNECTED-ACQUISITION-v1.md](../../../shared/external-access-runtime/EAR-CONNECTED-ACQUISITION-v1.md) — BZPM example | E1 | Operator codename corroboration |
| EV-W1B-05 | EAR [EAR-ACQUISITION-TRACKS-v1.md](../../../shared/external-access-runtime/EAR-ACQUISITION-TRACKS-v1.md) | E1 | Managed project / recurring support context |
| EV-W1B-06 | PILOT-001 / SITE-001 SFTP charter docs | E1 | Connected acquisition pilot binding |
| EV-W1B-CC | Counterparty Card `bzpm/` external folder | **Absent** | **Required primary** for W1-B **active** |

### 7.2 Evidence tier assignment (population)

| Tier | Assignment | Implication |
|------|------------|-------------|
| **E1** | Operational docs (EV-W1B-01..06) | Sufficient for **proposed** Organization + alias register intent |
| **E1 CC minimum** | **Not met** | **Blocks** steward **active** attest per W1-EXEC-04 analog and OAR-01 |
| **E2** | Not used | — |

### 7.3 Prohibited paths (verified not used)

| Path | Status |
|------|--------|
| Contract / invoice primary intake | **Not used** — OAR-BAN-01 |
| OPS Agreement mint | **Not used** — OAR-BAN-02 |
| Hostname-only org mint | **Not used** — OAR-BAN-03 |
| MIG / SERP pack primary | **Not used** — AT-E-03 |

---

## 8. Duplicate review

Pre-seed batch per W1-EXEC-01 — complete before any **active** attest.

| Review ID | Signal | Entities | Class | Outcome |
|-----------|--------|----------|-------|---------|
| **W1B-D-01** | BZPM / SIBCAR / СИБКАР | ORG-0005 | **Alias cluster** — single org | **Pass** |
| **W1B-D-02** | BZPM vs Triumph client brands | ORG-0005 vs ORG-0004 | **Distinct org** | **Pass** |
| **W1B-D-03** | SIBCAR vs gktriumph / triumph | ORG-0005 vs ORG-0004 aliases | **No collision** | **Pass** |
| **W1B-D-04** | SITE-001 as org homonym | ORG-0005 vs OCPilot site id | **Class boundary** — not duplicate org | **Pass** |
| **W1B-D-05** | Dealership homonym (generic «автосалон») | ORG-0005 | **U-homonym watch** — disambiguation note required at CC intake | **Open — low** |
| **W1B-D-06** | Unresolved D1 duplicate | — | None detected | **Pass** |

**STOP-W1-01 analog:** No unresolved D1 — duplicate batch **clear for proposed state**. **Active** attest still blocked on ME-W1B-01.

---

## 9. Attestation readiness

| Gate | Requirement | Status |
|------|-------------|--------|
| W1B-S-01 | Wave 1 ORG-0001..0004 stable | **Pass** |
| W1B-S-02 | Duplicate batch complete | **Pass** (proposed tier) |
| W1B-S-03 | W1-B E1+ evidence for **active** | **Fail** — CC absent |
| W1B-S-04 | Legal entity critical fields reviewed | **Fail** — LE-0004 SAFE UNKNOWN |
| W1B-S-05 | Human steward attest path documented | **Pass** — see Attestation doc |
| W1B-S-06 | No Foundation modification | **Pass** |
| W1B-S-07 | No new entity classes | **Pass** |

**Population readiness:** **Ready** — proposed register row may be recorded.  
**Attestation readiness (active):** **Not ready** — ME-W1B-01, ME-W1B-02.

---

## 10. Future person population candidates (Wave 2 BZPM)

**Not in Wave 1B scope.** Informational queue for future Wave 2 BZPM tranche.

| Candidate | Source | Role hint | Evidence | Readiness |
|-----------|--------|-----------|----------|-----------|
| Primary contact | CC `document_signatory` / contact lines | REPRESENTATIVE or EMPLOYEE | CC required | **Not ready** |
| Operational contact | CC contact block | REPRESENTATIVE | CC required | **Not ready** |
| OCPilot access brief signatory | Not named in repo | **SAFE UNKNOWN** | — | **Not ready** |

**W1-EXEC-04 analog:** Contacts on card → **proposed** Person each — not bundled **active** with Organization.

**Prerequisite:** ORG-0005 **active** before Wave 2B-BZPM Person → Organization edges.

---

## 11. Future project population candidates (Wave 3 BZPM)

**Not in Wave 1B scope.** Informational — not MARS program registry rows.

| Candidate | Description | commissioning_org | execution_org (candidate) | Evidence | Wave |
|-----------|-------------|-------------------|---------------------------|----------|------|
| PRJ-* TBD | BZPM / SITE-001 OpenCart dealership support | ORG-0005 | ORG-0001 Полигон | OCPilot charter; EAR Connected track | Wave 3 |
| PRJ-* TBD | OCPilot read-only audit (Run 5+) | ORG-0005 | ORG-0001 | SITE-001 reports | Wave 3 |
| `ocpilot`, `ear-runtime` | MARS programs | — | — | **Excluded** — E-17 |

**Distinction:**

| Concept | Entity class | Wave |
|---------|--------------|------|
| BZPM as **client business** | Organization | **Wave 1B** *(this package)* |
| SITE-001 OpenCart **engagement** | Project | Wave 3 |
| Connected acquisition **pilot** | EAR/OCPilot program context | Not ATLAS Project |

---

## 12. Foundation consistency

| Check | Result |
|-------|--------|
| Organization class only — no new entity types | **Pass** |
| No Foundation document modification | **Pass** |
| Existing Wave 1–6A rules applied | **Pass** |
| Identifier model ORG-0005 / LE-0004 | **Pass** — next slots after Wave 1 |
| Alias model — no alias→org mint | **Pass** |
| CC-first acquisition rules referenced | **Pass** |
| SAFE UNKNOWN used — no invented INN/OGRN | **Pass** |
| Documentation only — no runtime/API/DB | **Pass** |

---

## 13. Package lineage

```text
Wave 1 (ORG-0001..0004) ──COMPLETE──► Wave 1 Attestation ──COMPLETE
        │
        ▼
Wave 1B BZPM Organization Population (THIS PACKAGE) ──► proposed ORG-0005
        │
        ▼
Wave 1B BZPM Organization Attestation (NEXT) ──► blocked on CC
        │
        ▼
Wave 2 BZPM Person Population (FUTURE) ──► after ORG-0005 active
```

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | Canonical register row |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External CC path — `bzpm\` folder to be added by operator |
| [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) | W1-B Triumph exemplar methodology |

---

# REPORT — ATLAS Wave 1B BZPM Organization Population

**Date:** 2026-06-06  
**Scope:** Documentation-only validation — second real client Organization population using existing model.

---

## 1. Organization populated

| org_id | canonical_name | wave_tier | lifecycle (population) | register |
|--------|----------------|-----------|------------------------|----------|
| ORG-0005 | BZPM | W1-B CLIENT | **proposed** | [Register v1](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) |

**Validation outcome:** Existing Organization model accommodates BZPM as W1-B client without schema or Foundation changes. Proposed register row is structurally complete; **active** canonical state deferred to attestation pass.

---

## 2. Legal entity analysis

| Item | Finding |
|------|---------|
| Proposed LE-0004 | Placeholder bound to ORG-0005 |
| Legal name | **SAFE UNKNOWN** |
| INN / OGRN / KPP | **SAFE UNKNOWN** |
| Entity type (ООО / ИП) | **SAFE UNKNOWN** |
| Signatory | **SAFE UNKNOWN** |
| CC path | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **not present** at authoring |

**Conclusion:** Legal entity layer cannot progress beyond **proposed** until Counterparty Card or documented E2 registry extract.

---

## 3. Evidence basis

| Tier | Sources | Sufficiency |
|------|---------|-------------|
| E1 operational | OCPilot SITE-001 passport, access brief, intake marker; EAR BZPM references; PILOT-001 charter | **Proposed org** — yes |
| E1 CC | Absent | **Active org** — no |
| E0 | Not used for W1-B | Correct per acquisition rules |

**Primary gap:** ME-W1B-01 — Counterparty Card required for W1-B **active** attest.

---

## 4. Duplicate review

| Result | Detail |
|--------|--------|
| **Pass** | BZPM / SIBCAR / Автосалон СИБКАР → single org alias cluster |
| **Pass** | Distinct from ORG-0004 Triumph and operator orgs |
| **Pass** | SITE-001 remains site id — not second Organization |
| **Open (low)** | Generic dealership homonym watch — resolve at CC intake |

No D1 blocker for **proposed** population.

---

## 5. Candidate Persons

| Candidate | Status |
|-----------|--------|
| Primary contact | **SAFE UNKNOWN** — pending CC |
| Document signatory | **SAFE UNKNOWN** — pending CC |
| Named contacts in repo | **None** |

Wave 2 BZPM Person Population — **not ready** (no CC contact extraction; org not **active**).

---

## 6. Candidate Projects

| Candidate | Status |
|-----------|--------|
| BZPM / SITE-001 OpenCart support engagement | **Future Wave 3** — ORG-0005 → COMMISSIONED_BY candidate |
| OCPilot Run 5 audit container | **Future Wave 3** — client_delivery slice |
| MARS programs (ocpilot, ear) | **Excluded** |

---

## 7. Candidate Websites

| Candidate | URL | Status |
|-----------|-----|--------|
| TEST dealership site | `https://sibcar.new-site.space/` | Wave 4 candidate — TEST only |
| Production site | **SAFE UNKNOWN** | Wave 4 candidate |

---

## 8. Candidate Domains

| Candidate | FQDN | Status |
|-----------|------|--------|
| TEST subdomain | `sibcar.new-site.space` | Wave 5 candidate — not registrant proof |
| Production domain | **SAFE UNKNOWN** | Wave 5 candidate |

---

## 9. Readiness assessment

| Dimension | Assessment |
|-----------|------------|
| Organization model fit | **Validated** — second client populates cleanly |
| Population package complete | **Yes** — proposed ORG-0005 documented |
| Duplicate review | **Clear** for proposed tier |
| Attestation (**active**) | **Blocked** — CC + legal identifiers |
| Wave 2 BZPM Person Population | **Blocked** — org endpoint not **active** |

### Verdict

```text
PARTIALLY READY
```

**Meaning:**

1. Wave 1B **population** objective met — BZPM fits existing Organization model as W1-B **proposed** record.
2. **Active** attestation and Wave 2 BZPM Person Population remain **blocked** until Counterparty Card intake (ME-W1B-01) and legal entity review (ME-W1B-02).
3. Operator next step: place BZPM Counterparty Card in external storage `bzpm\` folder; notify steward for attestation tranche AT-W1B-01.

**Not selected:**

| Verdict | Why not |
|---------|---------|
| **NOT READY** | Population and duplicate review succeed — model validation goal achieved |
| **READY FOR WAVE 2 BZPM PERSON POPULATION** | ORG-0005 not **active**; no Person evidence |

---

**Changed files:** `projects/atlas/population/ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md` (this file), register, attestation  
**Git:** no commit, no push  
**UNKNOWN:** BZPM acronym expansion; production URL; legal entity requisites; client contact persons — verify via Counterparty Card  
**SECURITY RISK:** None — no credentials recorded; TEST URL only from existing OCPilot docs

---

*ATLAS Wave 1B BZPM Organization Population v1 — documentation only.*
