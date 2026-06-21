# ATLAS Wave 4B SIBCAR Website Relationship Attestation v1

**Status:** **attested** — official Website-family relationship attestation set for Wave 4B SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 5 execution, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project PRJ-0011: **attested** — AT-W3-SIBCAR-01
- Wave 3B SIBCAR Project ↔ Organization: **COMPLETE** — AT-W3B-SIBCAR-01
- Wave 4 SIBCAR Website attestation: **COMPLETE** — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 **active**)
- Population verdict: **READY FOR WAVE 4B SIBCAR WEBSITE RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 4B SIBCAR Website Relationship Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W4B-SIBCAR-01** + **AT-W4B-SIBCAR-02**  
**Promotion:** REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 — queued → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** набора **Website-family** relationships Wave 4B tranche **SIBCAR**: **2** записи переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Website → Project **BELONGS_TO** (1) | **OPERATES** Organization → Website |
| Organization → Website **OWNS** (1) | **CLIENT_OF** Organization ↔ Organization |
| SIBCAR TEST property WEB-SIBCAR-01 only | Domain entities |
| Evidence tier per relationship | PRIMARY_DOMAIN / SECONDARY_DOMAIN |
| TEST deployment posture unchanged | Person ↔ Website |
| Wave 5 SIBCAR readiness statement | Website ↔ Domain edges |
| | Runtime / API / database |
| | Production Website mint (SIBCAR-INTAKE-WEB-02) |

**Binding operator decisions (enforced):**

- **REL-SIBCAR-WB-01, REL-SIBCAR-WB-02** — approved list only; no additional edges.
- **OWNS** — structural business ownership (ORG-0006 → WEB-SIBCAR-01).
- **BELONGS_TO** — initiative grouping (WEB-SIBCAR-01 → PRJ-0011); single Project on TEST hostname — EFV-03.
- **OPERATES** — **не создавать**; remains **SAFE UNKNOWN** until future governance review.
- **TEST posture** — WEB-SIBCAR-01 **test_deployment** and environment **TEST** unchanged by this act.

---

## 2. Pre-check — endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0006** SIBCAR | **active** | AT-W1C-01 | **Pass** |
| **WEB-SIBCAR-01** sibcar.new-site.space | **active** | AT-W4-SIBCAR-01 | **Pass** |
| **PRJ-0011** | **active** | AT-W3-SIBCAR-01 | **Pass** |
| **REL-SIBCAR-PJ-01..02** | **active** | AT-W3B-SIBCAR-01 | **Pass** |
| **REL-0041** CLIENT_OF | **active** *(unchanged)* | AT-W6B-02 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested before relationship promotion.

---

## 3. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W4B-SIBCAR-01** | REL-SIBCAR-WB-01 | WEB-SIBCAR-01 **active**; PRJ-0011 **active**; EFV-03 single engagement; E0 OCPilot path | **active** |
| **AT-W4B-SIBCAR-02** | REL-SIBCAR-WB-02 | ORG-0006 **active**; WEB-SIBCAR-01 **active**; E0 OCPilot + org anchor | **active** |

---

## 4. Per-relationship attestation records

### 4.1 WEB-SIBCAR-01 — REL-SIBCAR-WB-01, REL-SIBCAR-WB-02

| Field | REL-SIBCAR-WB-01 | REL-SIBCAR-WB-02 |
|-------|------------------|------------------|
| **relationship_id** | REL-SIBCAR-WB-01 | REL-SIBCAR-WB-02 |
| **source_id** | WEB-SIBCAR-01 sibcar.new-site.space | ORG-0006 SIBCAR |
| **target_id** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | WEB-SIBCAR-01 sibcar.new-site.space |
| **relationship_type** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-SIBCAR-01 **active**; PRJ-0011 **active**; E0 EV-W1C-02..03, EV-OCP-01..04; REL-SIBCAR-PJ-01..02 context; resolves SU-W3B-SIBCAR-01 | ORG-0006 **active**; WEB-SIBCAR-01 **active**; E0 EV-W1C-02..03; EV-W1C-CC-01 org anchor; operator TEST narrative — not production registrant proof |
| **evidence_tier** | **E0** | **E0** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Sole TEST property under PRJ-0011; TEST posture unchanged | OPERATES for ORG-0001 not created; CC silent on website — E0 sufficient |

---

## 5. Relationships created — summary

| relationship_id | source_id | target_id | relationship_type | lifecycle_state |
|-----------------|-----------|-----------|-------------------|-----------------|
| REL-SIBCAR-WB-01 | WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **BELONGS_TO** | **active** |
| REL-SIBCAR-WB-02 | ORG-0006 SIBCAR | WEB-SIBCAR-01 sibcar.new-site.space | **OWNS** | **active** |

**Promotion count:** **2 / 2** relationships attested  
**Deferred from approved list:** **0**

**Attested structural graph:**

```text
ORG-0006 SIBCAR
    └── OWNS (REL-SIBCAR-WB-02)
        ▼
WEB-SIBCAR-01 sibcar.new-site.space  [test_deployment · TEST]
    └── BELONGS_TO (REL-SIBCAR-WB-01)
        ▼
PRJ-0011 Автосалон СИБКАР — OpenCart dealership
```

**Verdict:** **Pass** — OWNS + BELONGS_TO pair consistent with Wave 4B structural model; TEST Website posture unchanged.

---

## 6. Evidence basis

| Ref | Tier | Role | Relationships |
|-----|------|------|---------------|
| **EV-W1C-02** | E0 | OCPilot site-passport — SITE-001; TEST URL `sibcar.new-site.space`; ocStore baseline; env **TEST** | REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 |
| **EV-W1C-03** | E0 | OCPilot project-access-brief — Business Goal; Planned Work; active WIP | REL-SIBCAR-WB-01 |
| **EV-OCP-01..04** | E0 | Intake complete; SITE-001 registry; pilot narrative | REL-SIBCAR-WB-01, REL-SIBCAR-WB-02 |
| **EV-W1C-CC-01** | E1 | `sibcar/Реквизиты.docx` — org anchor; **no** website field on CC | Supporting context — REL-SIBCAR-WB-02 |
| **AT-W4-SIBCAR-01** | attestation | WEB-SIBCAR-01 **active** | Both edges |
| **AT-W3-SIBCAR-01** | attestation | PRJ-0011 **active** | REL-SIBCAR-WB-01 |
| **AT-W1C-01** | attestation | ORG-0006 **active** | REL-SIBCAR-WB-02 |
| **AT-W3B-SIBCAR-01** | attestation | REL-SIBCAR-PJ-01..02 COMMISSIONED_BY / EXECUTES context | Cross-check only |
| **AT-W6B-02** | attestation | REL-0041 **active** — vendor context | Informational — not re-minted |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only)
```

**Commercial complement (not re-minted):**

| relationship_id | family | status | note |
|-----------------|--------|--------|------|
| REL-0041 | ORG-0006 → ORG-0001 **CLIENT_OF** | **active** (Wave 6B) | Complementary to structural Website edges — SIBCAR-4B-D-07 |

---

## 7. Validation results

| Check | Result |
|-------|--------|
| Single TEST Website model (WEB-SIBCAR-01 only) | **Pass** — SIBCAR-INTAKE-WEB-02 not minted |
| Single-project BELONGS_TO (EFV-03) | **Pass** — WEB-SIBCAR-01 → PRJ-0011 only |
| OWNS vs BELONGS_TO separation | **Pass** — distinct relationship families |
| TEST deployment posture unchanged | **Pass** — `test_deployment`; environment **TEST** |
| No new entities | **Pass** |
| No Domain entities | **Pass** |
| No PRIMARY_DOMAIN | **Pass** |
| No CLIENT_OF | **Pass** |
| No OPERATES | **Pass** |
| No Person → Website / Person → Project | **Pass** |
| No Organization → Domain | **Pass** |
| REL-0041 not duplicated / not re-minted | **Pass** |
| No conflict with Triumph graph (REL-0027..0035) | **Pass** — distinct org + website namespace |
| No conflict with ZPM graph (REL-ZPM-WB-01..04) | **Pass** — distinct org ORG-0006 vs ORG-0005 |
| No Foundation changes | **Pass** |
| No graph redesign | **Pass** |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| ORG-0001 OPERATES WEB-SIBCAR-01 | **Excluded** — SAFE UNKNOWN; separate governance |
| REL-0041 ORG-0006 CLIENT_OF ORG-0001 | **Already attested** — Wave 6B; not re-minted |
| DOM-* `sibcar.new-site.space` | **Excluded** — Wave 5 SIBCAR |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Excluded** — Wave 5B SIBCAR |
| Website → Domain | **Excluded** — Wave 5 |
| Person → Website | **Excluded** — operator scope |
| Person → Project | **Excluded** — operator scope |
| Organization → Domain | **Excluded** — Wave 5 |
| SIBCAR-INTAKE-WEB-02 production Website | **Blocked** — ME-W1C-02 |
| SIBCAR-INTAKE-FUT-03 PROD migration / launch | **Held** |
| Foundation documents | **Not modified** |

---

## 9. Foundation consistency review

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 2 directed Website-family edges — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Both edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-SIBCAR-01 / PRJ-0011 / ORG-0006 attested — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship `active` — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E0 tier for TEST structural path — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; population plan not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |
| EIR-W01 single property model | One Website for TEST hostname — **Pass** |
| EFV-03 single engagement rule | One Project on TEST property — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | WEB-SIBCAR-01 **active** | **Pass** |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | BELONGS_TO target PRJ-0011 exists | **Pass** |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY / EXECUTES consistent | **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | OWNS + BELONGS_TO structural precedent | **Pass** |

**Foundation modified:** **No**  
**Wave 1 / 1C / 3 / 3B / 4 SIBCAR / Wave 6B modified:** **No**  
**Triumph Wave 4B (REL-0027..0035) modified:** **No**  
**ZPM Wave 4B (REL-ZPM-WB-01..04) modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (BELONGS_TO + OWNS only — baseline families)  
**Domain entities introduced:** **No**  
**Website ↔ Domain edges created:** **No**  
**Graph redesign:** **No**

---

## 10. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact | Status |
|----|-------|----------|-------------|--------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Medium | SIBCAR-INTAKE-WEB-02 blocked | **Unchanged** |
| **ME-W1C-02** *(carry-forward)* | Production public URL | Medium | No production Website minted | **Unchanged** |
| **ME-W1C-05** *(carry-forward)* | Corporate domain not on CC | Low | Wave 5 DOM-* | **Open** — Wave 5 |
| **W1C-D-05** *(carry-forward)* | «Автосалон СИБКАР» vs «СибКар» CC alias | Low | Display disambiguation | **Unchanged** |
| **SU-SIBCAR-PRJ-06** | PROD migration (FUT-03) | Medium | Future production WEB | **Unchanged** |
| **SU-SIBCAR-PRJ-08** | EAR published snapshot for SITE-001 | Medium | OCPilot Run 5 — cross-program | **Unchanged** |
| **SU-W4-SIBCAR-01** | Live URL probe for TEST hostname | Low | E0 OCPilot sufficient | **Unchanged** |
| **SU-W4-SIBCAR-02** | TEST subdomain registrant ORG-0006 | Low | Wave 5 SIBCAR DOM-* | **Open** — Wave 5 |
| **SU-W4-SIBCAR-03** | OWNS without registrar E1 | Low | Operator TEST narrative | **Acknowledged** — REL-SIBCAR-WB-02 attested at E0 |
| **EV-OCP-GAP-01** | Credential channel confirmation | Low | EAR / OCPilot execution | **Unchanged** |

**Closed by this act:**

| ID | Topic | Disposition |
|----|-------|-------------|
| **SU-W3B-SIBCAR-01** | WEB-* BELONGS_TO policy for TEST hostname | **Closed** — REL-SIBCAR-WB-01 **active** |
| **ME-W4-SIBCAR-01** | BELONGS_TO not yet attested | **Closed** — REL-SIBCAR-WB-01 **active** |
| **ME-W4-SIBCAR-02** | OWNS edge not yet attested | **Closed** — REL-SIBCAR-WB-02 **active** |

**Missing evidence register (non-blocking):**

| ID | Gap | Severity | Mitigation |
|----|-----|----------|------------|
| **ME-W4B-SIBCAR-01** | PRIMARY_DOMAIN / DOM-* not minted | Low | Wave 5 / 5B by design |
| **ME-W4B-SIBCAR-02** | No CC website field | Low | E0 OCPilot path sufficient |
| **ME-W4B-SIBCAR-03** | ORG-0001 OPERATES not attested | Low | Separate governance — not blocking Wave 5 |

**Blocking gaps remaining:** **None**

---

## 11. Readiness verdict

### 11.1 Wave 5 SIBCAR readiness assessment

| Criterion | Status |
|-----------|--------|
| Wave 4 SIBCAR Website attested **active** (WEB-SIBCAR-01) | **Pass** — AT-W4-SIBCAR-01 |
| Wave 4B SIBCAR BELONGS_TO WEB-SIBCAR-01 → PRJ-0011 | **Pass** — 1/1 attested (REL-SIBCAR-WB-01) |
| Wave 4B SIBCAR OWNS ORG-0006 → WEB-SIBCAR-01 | **Pass** — 1/1 attested (REL-SIBCAR-WB-02) |
| TEST deployment posture unchanged | **Pass** — `test_deployment` on operator TEST hostname |
| SIBCAR-INTAKE-WEB-02 not minted | **Pass** — ME-W1C-02 honored |
| No Domain entities prematurely minted | **Pass** |
| PRIMARY_DOMAIN target unambiguous (WEB-SIBCAR-01 singleton) | **Pass** |
| REL-0041 not re-minted | **Pass** |
| Foundation unchanged | **Pass** |

### 11.2 Verdict

```text
READY FOR WAVE 5 SIBCAR DOMAIN POPULATION
```

**Conditions:**

1. Wave 5 SIBCAR executes as **separate population pass** — Domain entities and Domain-family relationships not bundled into 4B-SIBCAR.
2. PRIMARY_DOMAIN edges require Domain attestation first, then Wave 5B SIBCAR cross-links to WEB-SIBCAR-01.
3. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking Domain population.
4. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
5. Production Website (SIBCAR-INTAKE-WEB-02) remains **blocked** until public URL evidence arrives (ME-W1C-02).
6. TEST Website posture on WEB-SIBCAR-01 **unchanged** — relationship attestation does not imply production registrant proof.

### 11.3 Attestation verdict

```text
WAVE 4B SIBCAR WEBSITE RELATIONSHIP ATTESTATION — COMPLETE
2 / 2 Website-family relationships attested active
0 relationships deferred from approved 4B-SIBCAR list
Wave 5 SIBCAR Domain population — READY TO START
```

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 4B SIBCAR WEBSITE RELATIONSHIP POPULATION** | [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) §5.3 | **Superseded** — REL-SIBCAR-WB-01..02 now **active** |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **PARTIALLY READY** | Full approved list attested |
| **READY FOR WAVE 4B SIBCAR WEBSITE RELATIONSHIP POPULATION** | Superseded — attestation act complete |

---

## 12. Attestation results summary

| relationship_id | source_id | target_id | relationship_type | evidence_tier | tranche | lifecycle_state |
|-----------------|-----------|-----------|-------------------|---------------|---------|-----------------|
| REL-SIBCAR-WB-01 | WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **BELONGS_TO** | E0 | AT-W4B-SIBCAR-01 | **active** |
| REL-SIBCAR-WB-02 | ORG-0006 SIBCAR | WEB-SIBCAR-01 sibcar.new-site.space | **OWNS** | E0 | AT-W4B-SIBCAR-02 | **active** |

**Relationships created:** **2**  
**New entities created:** **0**  
**Domain entities created:** **0**  
**Person ↔ Website edges created:** **0**  
**CLIENT_OF edges created:** **0**

---

## 13. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1C SIBCAR (ORG-0006, LE-0005) ──► AT-W1C-01 (COMPLETE)
        │
        ├── Wave 6B Commercial (REL-0041) ──► AT-W6B-02 (COMPLETE)
        │
        ├── Wave 3 SIBCAR Project (PRJ-0011) ──► AT-W3-SIBCAR-01 (COMPLETE)
        │
        ├── Wave 3B SIBCAR Project Relationship (REL-SIBCAR-PJ-01..02) ──► AT-W3B-SIBCAR-01 (COMPLETE)
        │
        ├── Wave 4 SIBCAR Website (WEB-SIBCAR-01 TEST) ──► AT-W4-SIBCAR-01 (COMPLETE)
        │
        └── Wave 4B SIBCAR Website Relationship (REL-SIBCAR-WB-01..02) ──► AT-W4B-SIBCAR-01..02 (THIS ACT)
                    │
                    └──► Wave 5 SIBCAR Domain Population (NEXT)
```

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website attestation prerequisite |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | ZPM tranche structural precedent |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 active basis |

---

*ATLAS Wave 4B SIBCAR Website Relationship Attestation v1 — documentation only.*
