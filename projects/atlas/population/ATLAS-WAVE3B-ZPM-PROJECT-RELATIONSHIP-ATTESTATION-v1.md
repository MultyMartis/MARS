# ATLAS Wave 3B ZPM Project Relationship Attestation v1

**Status:** **attested** — official Project ↔ Organization relationship attestation set for Wave 3B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 4 execution, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Project attestation: **COMPLETE** — AT-W3-ZPM-01..02
- Population verdict: **READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 3B ZPM Project Relationship Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W3B-ZPM-01** + **AT-W3B-ZPM-02**  
**Promotion:** REL-ZPM-PJ-01..04 — queued → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** набора **Project ↔ Organization** relationships Wave 3B tranche **ZPM**: **4** записи переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Project ↔ Organization → **active** | Person ↔ Project |
| COMMISSIONED_BY + EXECUTES only | Organization ↔ Organization |
| ZPM client delivery (PRJ-0009, PRJ-0010) | Website / Domain entities |
| Evidence tier per relationship | Website ↔ Project BELONGS_TO |
| Deprecated PRJ-0010 historical edges (LT-P01) | Person ↔ Person |
| Wave 4 ZPM readiness statement | Runtime / API / database |

**Binding operator decisions (enforced):**

- **REL-ZPM-PJ-01..04** — approved list only; no additional edges.
- **PRJ-0010 deprecated** — COMMISSIONED_BY / EXECUTES **active** per LT-P01 historical pattern (Triumph REL-0017/0018 analog).
- **REL-0016** CLIENT_OF — **не аттестирован**; Wave 6.
- Person → Project — **не создавать**.
- Website / Domain — **не создавать**.

---

## 2. Pre-check — endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **ORG-0001** Полигон | **active** | Wave 1 attestation | **Pass** |
| **PRJ-0009** | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** | **deprecated** | AT-W3-ZPM-02 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested before relationship promotion.

---

## 3. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W3B-ZPM-01** | REL-ZPM-PJ-01, REL-ZPM-PJ-02 | E0 EV-ZPM-OP-ACT-01; PRJ-0009 **active**; ORG-0001, ORG-0005 **active** | **active** |
| **AT-W3B-ZPM-02** | REL-ZPM-PJ-03, REL-ZPM-PJ-04 | E0 EV-ZPM-OP-HIST-01; PRJ-0010 **deprecated**; LT-P01 historical edges | **active** |

---

## 4. Per-relationship attestation records

### 4.1 PRJ-0009 — REL-ZPM-PJ-01, REL-ZPM-PJ-02

| Field | REL-ZPM-PJ-01 | REL-ZPM-PJ-02 |
|-------|---------------|---------------|
| **relationship_id** | REL-ZPM-PJ-01 | REL-ZPM-PJ-02 |
| **source_id** | PRJ-0009 Каталог-платформа bzpm.ru | ORG-0001 Полигон |
| **target_id** | ORG-0005 ЗПМ | PRJ-0009 Каталог-платформа bzpm.ru |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0009 **active** (AT-W3-ZPM-01); ORG-0005 **active** (AT-W1B-01); E0 EV-ZPM-OP-ACT-01; commissioning org from Wave 3 population display | ORG-0001 **active** (Wave 1); PRJ-0009 **active**; E0 EV-ZPM-OP-ACT-01; operator: Polygon active WIP |
| **evidence_tier** | **E0** | **E0** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Ongoing catalog-platform client commissioning | Polygon delivery org; PER-0014 operational contact — no Person→Project edge |

### 4.2 PRJ-0010 — REL-ZPM-PJ-03, REL-ZPM-PJ-04

| Field | REL-ZPM-PJ-03 | REL-ZPM-PJ-04 |
|-------|---------------|---------------|
| **relationship_id** | REL-ZPM-PJ-03 | REL-ZPM-PJ-04 |
| **source_id** | PRJ-0010 Сайт bzpm.ru (исходная версия) | ORG-0001 Полигон |
| **target_id** | ORG-0005 ЗПМ | PRJ-0010 Сайт bzpm.ru (исходная версия) |
| **relationship_type** | **COMMISSIONED_BY** | **EXECUTES** |
| **attestation_basis** | PRJ-0010 **deprecated** (AT-W3-ZPM-02); ORG-0005 **active**; E0 EV-ZPM-OP-HIST-01; LT-P01 historical structural truth | ORG-0001 **active**; PRJ-0010 **deprecated**; E0 EV-ZPM-OP-HIST-01; operator: Polygon historical delivery |
| **evidence_tier** | **E0** | **E0** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Historical commissioning — completed delivery ~5y ago; Triumph REL-0017 analog | Historical execution — WP + The7 + Custom; Triumph REL-0018 analog |

---

## 5. Relationships created — summary

| relationship_id | source_id | target_id | relationship_type | lifecycle_state |
|-----------------|-----------|-----------|-------------------|-----------------|
| REL-ZPM-PJ-01 | PRJ-0009 Каталог-платформа bzpm.ru | ORG-0005 ЗПМ | **COMMISSIONED_BY** | **active** |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 Каталог-платформа bzpm.ru | **EXECUTES** | **active** |
| REL-ZPM-PJ-03 | PRJ-0010 Сайт bzpm.ru (исходная версия) | ORG-0005 ЗПМ | **COMMISSIONED_BY** | **active** |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 Сайт bzpm.ru (исходная версия) | **EXECUTES** | **active** |

**Promotion count:** **4 / 4** relationships attested  
**Deferred from approved list:** **0**

---

## 6. Evidence basis

| Ref | Tier | Role | Relationships |
|-----|------|------|---------------|
| **EV-ZPM-OP-ACT-01** | E0 | Operator — current catalog rebuild; ongoing client delivery | REL-ZPM-PJ-01, REL-ZPM-PJ-02 |
| **EV-ZPM-OP-HIST-01** | E0 | Operator — historical `bzpm.ru` site delivery ~5y ago | REL-ZPM-PJ-03, REL-ZPM-PJ-04 |
| **EV-W1B-CC-01** | E1 | `bzpm/Реквизиты.docx` — org anchor; §17 indirect hostname corroboration | Supporting context only |
| **AT-W1B-01** | attestation | ORG-0005 **active** | All COMMISSIONED_BY endpoints |
| **AT-W3-ZPM-01** | attestation | PRJ-0009 **active** | REL-ZPM-PJ-01, REL-ZPM-PJ-02 |
| **AT-W3-ZPM-02** | attestation | PRJ-0010 **deprecated** | REL-ZPM-PJ-03, REL-ZPM-PJ-04 |
| Wave 1 attestation | attestation | ORG-0001 **active** | REL-ZPM-PJ-02, REL-ZPM-PJ-04 |
| **AT-W2B-ZPM-01..02** | attestation | Person→Org vendor context (informational) | Does not substitute Project edge evidence |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (PRJ-0009 edges)
E0 operator — EV-ZPM-OP-HIST-01 (PRJ-0010 edges)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx (org anchor only)
```

---

## 7. Validation results

| Check | Result |
|-------|--------|
| ORG-0005 **active** | **Pass** — AT-W1B-01 |
| ORG-0001 **active** | **Pass** — Wave 1 |
| PRJ-0009 **active** | **Pass** — AT-W3-ZPM-01 |
| PRJ-0010 **deprecated** | **Pass** — AT-W3-ZPM-02 |
| Historical project relationships (LT-P01) | **Pass** — REL-ZPM-PJ-03/04 on deprecated endpoint |
| No duplicate edges (ZPM-3B-D-01..06) | **Pass** |
| No conflict with Triumph graph (REL-0017..0026) | **Pass** — distinct org + project namespace |
| Website / Domain not created | **Pass** |
| BELONGS_TO / CLIENT_OF / OWNS not created | **Pass** |
| Person→Project not created | **Pass** |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| WEB-* `bzpm.ru` | **Excluded** — Wave 4 |
| DOM-* `bzpm.ru` | **Excluded** — Wave 5 |
| WEB → Project **BELONGS_TO** | **Deferred** — Wave 4B |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| ORG-0005 **OWNS** / **PRIMARY_DOMAIN** | **Excluded** |
| Person → Project (PER-0014, PER-0015) | **Excluded** — operator scope |
| Person ↔ Person | **Rejected** |
| Organization → Website / Domain | **Excluded** — Waves 4–5 |
| ZPM-INTAKE-FUT-01..04 | **Held** — no start evidence |
| Foundation documents | **Not modified** |

---

## 9. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 4 directed Project↔Org edges; paired COMMISSIONED_BY + EXECUTES — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §3 | COMMISSIONED_BY, EXECUTES in baseline — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PRJ-0009/0010 / ORG-0001/0005 attested — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active`; deprecated PRJ-0010 valid endpoint — **Pass** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | PRJ-0010 deprecated — historical edges valid — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; population plan not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |
| EFV-02 / EFV-03 | SIBCAR/SITE-001 excluded; two-phase bzpm.ru projects honored — **Pass** |

**Foundation modified:** **No**  
**Wave 1 / Wave 2 / Wave 2B / Wave 3 ZPM modified:** **No**  
**Triumph Wave 3B (REL-0017..0026) modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Organization ↔ Project only)

---

## 10. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-ZPM-PRJ-01** | Historical contract / act dates (PRJ-0010) | Low | Does not block Wave 4 |
| **SU-ZPM-PRJ-02** | Formal acceptance document (E1 upgrade path) | Low | Optional future upgrade |
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence on `bzpm.ru` | Medium | Wave 4 WEB / 4B BELONGS_TO policy |
| **SU-ZPM-PRJ-06** | PER-0014 / PER-0015 on Project | Low | No Person→Project edges |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | Wave 6 |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Wave 5 |
| **SU-W3B-ZPM-01** | WEB-* single vs dual BELONGS_TO for same hostname | Medium | Wave 4B steward policy |
| **SU-W3B-ZPM-02** | E0-only evidence tier for all 4 edges | Low | Operator path sufficient |

**Blocking gaps remaining:** **None**

---

## 11. Wave 4 ZPM readiness assessment

### 11.1 Criteria

| Criterion | Status |
|-----------|--------|
| ORG-0005 Organization **active** | **Pass** — AT-W1B-01 |
| Wave 3 ZPM Projects attested (PRJ-0009, PRJ-0010) | **Pass** — AT-W3-ZPM-01..02 |
| Wave 3B ZPM COMMISSIONED_BY + EXECUTES | **Pass** — 4/4 attested |
| Project endpoints available for BELONGS_TO targets | **Pass** — PRJ-0009 **active**, PRJ-0010 **deprecated** |
| Historical deprecated project edges attested (LT-P01) | **Pass** — REL-ZPM-PJ-03/04 |
| No Person→Project attested | **Pass** |
| No conflict with Triumph graph | **Pass** |
| Website entities not yet attested | **Expected** — Wave 4 scope |

### 11.2 Verdict

```text
READY FOR WAVE 4 ZPM WEBSITE POPULATION
```

**Conditions:**

1. Wave 4 ZPM executes as **separate population pass** — Website entities (`WEB-*` for `bzpm.ru`) not bundled into 3B-ZPM.
2. BELONGS_TO edges require **active** Website endpoints (Wave 4) and steward policy for dual-project hostname (**SU-W3B-ZPM-01** / **SU-ZPM-PRJ-03**).
3. REL-0016 CLIENT_OF remains **Wave 6**.
4. DOM-* `bzpm.ru` remains **Wave 5**.
5. FUT-01..04 Project candidates remain **hold**.

---

## 12. Attestation verdict

```text
WAVE 3B ZPM PROJECT RELATIONSHIP ATTESTATION — COMPLETE
4 / 4 Project ↔ Organization relationships attested active
0 relationships deferred from approved 3B-ZPM list
Wave 4 ZPM Website population — READY TO START
```

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION** | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) §11 | **Superseded** — REL-ZPM-PJ-01..04 now **active** |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **PARTIALLY READY** | Full approved list attested |
| **READY FOR WAVE 3B ZPM PROJECT RELATIONSHIP POPULATION** | Superseded — attestation act complete |

---

## 13. Attestation results summary

| relationship_id | source_id | target_id | relationship_type | evidence_tier | tranche | lifecycle_state |
|-----------------|-----------|-----------|-------------------|---------------|---------|-----------------|
| REL-ZPM-PJ-01 | PRJ-0009 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | E0 | AT-W3B-ZPM-01 | **active** |
| REL-ZPM-PJ-02 | ORG-0001 Полигон | PRJ-0009 | **EXECUTES** | E0 | AT-W3B-ZPM-01 | **active** |
| REL-ZPM-PJ-03 | PRJ-0010 | ORG-0005 ЗПМ | **COMMISSIONED_BY** | E0 | AT-W3B-ZPM-02 | **active** |
| REL-ZPM-PJ-04 | ORG-0001 Полигон | PRJ-0010 | **EXECUTES** | E0 | AT-W3B-ZPM-02 | **active** |

**Relationships created:** **4**  
**Website / Domain entities created:** **0**  
**Person ↔ Project edges created:** **0**

---

## 14. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
        │
        ├── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 2B ZPM Relationship (REL-ZPM-01..02) ──► AT-W2B-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 3 ZPM Project (PRJ-0009, PRJ-0010) ──► AT-W3-ZPM-01..02 (COMPLETE)
        │
        └── Wave 3B ZPM Project Relationship (REL-ZPM-PJ-01..04) ──► AT-W3B-ZPM-01..02 (THIS ACT)
                    │
                    └──► Wave 4 ZPM Website Population (NEXT)
```

---

## 15. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | Project attestation prerequisite |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Core Wave 3B Triumph precedent |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Person→Org prerequisite |

---

*ATLAS Wave 3B ZPM Project Relationship Attestation v1 — documentation only.*
