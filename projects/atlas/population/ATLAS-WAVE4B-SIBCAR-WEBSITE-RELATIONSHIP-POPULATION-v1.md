# ATLAS Wave 4B SIBCAR Website Relationship Population v1

**Status:** **documented** — canonical Website-family relationship population plan for Wave 4B SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005  
**Parent:** [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 5 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project PRJ-0011: **attested** — AT-W3-SIBCAR-01
- Wave 3B SIBCAR Project ↔ Organization: **COMPLETE** — AT-W3B-SIBCAR-01
- Wave 4 SIBCAR Website attestation: **COMPLETE** — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 **active**)
- Population verdict: **READY FOR WAVE 4B SIBCAR WEBSITE RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 4B SIBCAR Website Relationship Population

**Population date:** 2026-06-07  
**Tranche:** **POP-W4B-SIBCAR-01**

---

## 1. Purpose

Зафиксировать **канонический план population** набора **Website-family** relationships для Wave 4B tranche **SIBCAR** (ORG-0006): состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 4B SIBCAR:**

```text
Website → Project BELONGS_TO (REL-SIBCAR-WB-01)
Organization → Website OWNS (REL-SIBCAR-WB-02)
SIBCAR TEST property WEB-SIBCAR-01 only (single Website model)
No OPERATES in this pass
No Domain entities
No Website ↔ Domain edges
No Person ↔ Website
No Organization ↔ Organization CLIENT_OF
No new entity types
No new relationship families
No Foundation modifications
TEST Website posture unchanged — test_deployment on operator TEST hostname
```

**Binding operator modeling decision:**

- **OWNS** (Organization → Website) — structural business ownership of web property identity (ORG-0006 → WEB-SIBCAR-01).
- **BELONGS_TO** (Website → Project) — initiative grouping; single active Project (PRJ-0011) on sole TEST property — EFV-03.
- **OPERATES** — **не создавать**; deferred to separate governance review.
- **TEST deployment posture** — WEB-SIBCAR-01 remains **test_deployment**; relationship edges do not upgrade environment or registrant proof.

---

## 2. Approved state (operator-confirmed)

| Entity class | id | canonical_name | lifecycle_state |
|--------------|-----|----------------|-----------------|
| Organization | **ORG-0006** | SIBCAR | **active** |
| Website | **WEB-SIBCAR-01** | sibcar.new-site.space | **active** |
| Project | **PRJ-0011** | Автосалон СИБКАР — OpenCart dealership | **active** |

---

## 3. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Website endpoints | **1** (WEB-SIBCAR-01) |
| Project endpoints (BELONGS_TO targets) | **1** (PRJ-0011 **active**) |
| Organization endpoints (OWNS source) | **1** (ORG-0006 SIBCAR) |
| Relationship types used | **BELONGS_TO**, **OWNS** |
| Multi-project websites | **0** — single Project on TEST hostname (EFV-03) |

### 3.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-SIBCAR-WB-01 | WEB-SIBCAR-01 sibcar.new-site.space | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **BELONGS_TO** | **ready** |
| REL-SIBCAR-WB-02 | ORG-0006 SIBCAR | WEB-SIBCAR-01 sibcar.new-site.space | **OWNS** | **ready** |

---

## 4. Per-relationship analysis

### 4.1 WEB-SIBCAR-01 sibcar.new-site.space — REL-SIBCAR-WB-01, REL-SIBCAR-WB-02

#### REL-SIBCAR-WB-01 — BELONGS_TO

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-WB-01 |
| **source_id** | WEB-SIBCAR-01 sibcar.new-site.space |
| **target_id** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership |
| **relationship_type** | **BELONGS_TO** |
| **attestation_basis** | E0 EV-W1C-02..03, EV-OCP-01..04; WEB-SIBCAR-01 **active** (AT-W4-SIBCAR-01); PRJ-0011 **active** (AT-W3-SIBCAR-01); REL-SIBCAR-PJ-01..02 COMMISSIONED_BY / EXECUTES context; EFV-03 single engagement on TEST hostname; display fields from Wave 4 population |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Sole TEST web property grouped under ongoing OpenCart dealership Project; resolves SU-W3B-SIBCAR-01; TEST posture unchanged |

#### REL-SIBCAR-WB-02 — OWNS

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-WB-02 |
| **source_id** | ORG-0006 SIBCAR |
| **target_id** | WEB-SIBCAR-01 sibcar.new-site.space |
| **relationship_type** | **OWNS** |
| **attestation_basis** | E0 EV-W1C-02..03; ORG-0006 **active** (AT-W1C-01); WEB-SIBCAR-01 **active** (AT-W4-SIBCAR-01); EV-W1C-CC-01 org anchor; client org owns TEST web property identity at structural layer; operator TEST narrative — not production registrant proof (SU-W4-SIBCAR-03) |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Structural business ownership — distinct from Polygon EXECUTES on PRJ-0011; OPERATES for ORG-0001 **not created**; CC silent on website — E0 OCPilot path sufficient |

---

## 5. Structural graph — SIBCAR (post 4B-SIBCAR)

```text
ORG-0006 SIBCAR ──OWNS──► WEB-SIBCAR-01 sibcar.new-site.space (test_deployment)

WEB-SIBCAR-01 ──BELONGS_TO──► PRJ-0011 Автосалон СИБКАР — OpenCart dealership (active)

(Prior Wave 3B SIBCAR — unchanged)
PRJ-0011 ──COMMISSIONED_BY──► ORG-0006 SIBCAR   (REL-SIBCAR-PJ-01)
ORG-0001 Полигон ──EXECUTES──► PRJ-0011         (REL-SIBCAR-PJ-02)

(Prior Wave 6B — unchanged)
ORG-0006 SIBCAR ──CLIENT_OF──► ORG-0001 Полигон (REL-0041 — not re-minted)
```

**Not in this pass:** ORG-0001 ──OPERATES──► WEB-SIBCAR-01 — deferred; DOM-* / PRIMARY_DOMAIN — Wave 5 / 5B.

---

## 6. Single TEST property analysis — WEB-SIBCAR-01

| Question | Resolution |
|----------|------------|
| May one website BELONGS_TO multiple projects? | **Not applicable** — EFV-03: single engagement → one Project (PRJ-0011) on TEST hostname |
| Should WEB-SIBCAR-01 normalize to one project? | **Yes** — sole BELONGS_TO target PRJ-0011 |
| OWNS vs BELONGS_TO overlap? | **No conflict** — OWNS is org-level property identity; BELONGS_TO is project initiative grouping |
| Does attestation change TEST posture? | **No** — `website_kind` **test_deployment** unchanged; environment **TEST** per EV-W1C-02 |
| Production Website SIBCAR-INTAKE-WEB-02? | **Not minted** — ME-W1C-02 honored |

**ZPM / Triumph cross-reference (distinct tranche):**

| Tranche | Website | Pattern |
|---------|---------|---------|
| Triumph | WEB-0006 → PRJ-0004 + PRJ-0006 | Multi-project — distinct org ORG-0004 |
| ZPM | WEB-ZPM-01 → PRJ-0009 + PRJ-0010 | Multi-project — distinct org ORG-0005 |
| **SIBCAR** | **WEB-SIBCAR-01 → PRJ-0011 only** | **Single-project TEST case** — ORG-0006 |

---

## 7. Validation review

### 7.1 Endpoint lifecycle verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0006** SIBCAR | **active** | AT-W1C-01 | **Pass** |
| **WEB-SIBCAR-01** sibcar.new-site.space | **active** | AT-W4-SIBCAR-01 | **Pass** |
| **PRJ-0011** | **active** | AT-W3-SIBCAR-01 | **Pass** |
| **REL-SIBCAR-PJ-01..02** | **active** | AT-W3B-SIBCAR-01 | **Pass** |

### 7.2 TEST posture verification

| Check | Source | Verified |
|-------|--------|----------|
| WEB-SIBCAR-01 **test_deployment** unchanged | AT-W4-SIBCAR-01 §3.1 | **Pass** |
| Environment **TEST** — not production | EV-W1C-02 | **Pass** |
| SIBCAR-INTAKE-WEB-02 **not minted** | ME-W1C-02 | **Pass** |
| Relationship edges do not imply production URL | Operator scope | **Pass** |
| EIR-W01 single TEST property | Wave 4 SIBCAR population | **Pass** |

### 7.3 Duplicate edge review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **SIBCAR-4B-D-01** | REL-SIBCAR-WB-01 vs REL-SIBCAR-WB-02 — same Website endpoint | **Not duplicate** — distinct relationship families | No |
| **SIBCAR-4B-D-02** | vs Wave 3B REL-SIBCAR-PJ-01..02 | **Distinct family** Project↔Org vs Website↔Project | No |
| **SIBCAR-4B-D-03** | vs Triumph REL-0027..0035 | **Distinct org** ORG-0006 vs ORG-0004 | No |
| **SIBCAR-4B-D-04** | vs ZPM REL-ZPM-WB-01..04 | **Distinct org** ORG-0006 vs ORG-0005 | No |
| **SIBCAR-4B-D-05** | Duplicate BELONGS_TO WEB-SIBCAR-01 → PRJ-0011 | **None** — single edge | No |
| **SIBCAR-4B-D-06** | OWNS vs BELONGS_TO type collision | **None** — distinct relationship families | No |
| **SIBCAR-4B-D-07** | vs REL-0041 CLIENT_OF | **Not duplicate** — Org↔Org commercial vs structural Website edges | No |

**Duplicate review summary:** **Pass**

### 7.4 Exclusion verification

| Check | Result |
|-------|--------|
| No new entities | **Pass** |
| No DOM-* entities | **Pass** |
| No PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Pass** |
| No CLIENT_OF | **Pass** |
| No OPERATES | **Pass** |
| No Person → Website | **Pass** |
| No Person → Project | **Pass** |
| No Organization → Domain | **Pass** |
| No Foundation changes | **Pass** |
| No graph redesign | **Pass** |

---

## 8. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| ORG-0001 OPERATES WEB-SIBCAR-01 | **Do not create** | SAFE UNKNOWN — separate governance |
| REL-0041 ORG-0006 CLIENT_OF ORG-0001 | **Already attested** | Wave 6B — not re-minted |
| DOM-* `sibcar.new-site.space` | **Do not create** | Wave 5 SIBCAR |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Do not create** | Wave 5B SIBCAR |
| Website → Domain | **Do not create** | Wave 5 |
| Person → Website | **Do not create** | Operator scope |
| Person → Project | **Do not create** | Operator scope |
| Organization → Domain | **Do not create** | Wave 5 |
| SIBCAR-INTAKE-WEB-02 production Website | **Blocked** | ME-W1C-02 — URL **SAFE UNKNOWN** |
| SIBCAR-INTAKE-FUT-03 PROD migration | **Held** | Future intake |

---

## 9. Candidate relationships for Wave 5 SIBCAR

| Candidate | Type | Endpoints | Prerequisite |
|-----------|------|-----------|--------------|
| DOM-* `sibcar.new-site.space` | Domain entity | — | Wave 5 SIBCAR Domain population |
| DOM-* → WEB-SIBCAR-01 | **PRIMARY_DOMAIN** | TEST hostname | Domain attestation + Wave 5B SIBCAR |
| ORG-0006 → DOM-* | **OWNS** (domain) | registrar / hosting evidence | Wave 5; SU-W4-SIBCAR-02 |

---

## 10. Foundation consistency

| Foundation doc | Wave 4B SIBCAR alignment |
|----------------|--------------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Directed Website→Project and Org→Website edges — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) in baseline — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-SIBCAR-01 / PRJ-0011 / ORG-0006 attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship `active` — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4 | E0 structural path for TEST client property — **yes** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward attestation path — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**Cross-wave validation:**

| Prior wave doc | Endpoint check |
|----------------|----------------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | WEB-SIBCAR-01 **active** — **Pass** |
| [ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-REGISTER-v1.md) | PRJ-0011 endpoint — **Pass** |
| [ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-SIBCAR-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY / EXECUTES consistent — **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Structural OWNS + BELONGS_TO precedent — **Pass** |

**No new entity types.** **No new relationship families.** **No Foundation modifications.**

---

## 11. SAFE UNKNOWN inventory

| ID | Topic | Severity | Blocks 4B-SIBCAR |
|----|-------|----------|------------------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Medium | **No** — SIBCAR-INTAKE-WEB-02 blocked |
| **ME-W1C-02** *(carry-forward)* | Production public URL | Medium | **No** — ME-W1C-02 honored |
| **ME-W1C-05** *(carry-forward)* | Corporate domain not on CC | Low | **No** — Wave 5 DOM-* |
| **W1C-D-05** *(carry-forward)* | «Автосалон СИБКАР» vs «СибКар» CC alias | Low | **No** — display disambiguation |
| **SU-W3B-SIBCAR-01** | WEB-* BELONGS_TO policy for TEST hostname | Medium | **Resolved** — REL-SIBCAR-WB-01 in scope |
| **SU-W4-SIBCAR-02** | TEST subdomain registrant ORG-0006 | Low | **No** — Wave 5 SIBCAR DOM-* |
| **SU-W4-SIBCAR-03** | OWNS without registrar E1 | Low | **No** — operator TEST narrative |
| **SU-W4-SIBCAR-01** | Live URL probe for TEST hostname | Low | **No** — E0 OCPilot sufficient |

**Blocking gaps remaining:** **None**

---

## 12. Readiness verdict

```text
READY FOR WAVE 4B SIBCAR WEBSITE RELATIONSHIP ATTESTATION
```

**Conditions:**

1. Both approved relationships pass endpoint, TEST posture, duplicate, and exclusion checks.
2. Attestation executes as **separate act** — population plan ≠ canonical until AT-W4B-SIBCAR-01..02.
3. Domain entities and PRIMARY_DOMAIN remain **Wave 5 / 5B SIBCAR**.
4. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
5. OPERATES, Person↔Website, and production Website mint remain **excluded**.
6. TEST deployment posture on WEB-SIBCAR-01 **unchanged**.

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website endpoint prerequisite |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | ZPM tranche structural precedent |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 4B SIBCAR Website Relationship Population v1 — documentation only.*
