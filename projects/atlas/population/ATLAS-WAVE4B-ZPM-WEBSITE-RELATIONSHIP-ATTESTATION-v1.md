# ATLAS Wave 4B ZPM Website Relationship Attestation v1

**Status:** **attested** — official Website-family relationship attestation set for Wave 4B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md)  
**Is not:** runtime, API, database export, Wave 5 execution, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- ZPM Website Model Correction: **EXECUTED** — COR-ZPM-WEB-01..12
- Wave 4 ZPM Website attestation: **COMPLETE** — AT-W4-ZPM-01 (WEB-ZPM-01 **active**)
- Population verdict: **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 4B ZPM Website Relationship Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W4B-ZPM-01** + **AT-W4B-ZPM-02**  
**Promotion:** REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04 — queued → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** набора **Website-family** relationships Wave 4B tranche **ZPM**: **3** записи переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Website → Project **BELONGS_TO** (2) | **OPERATES** Organization → Website |
| Organization → Website **OWNS** (1) | **CLIENT_OF** Organization ↔ Organization |
| ZPM client property WEB-ZPM-01 only | Domain entities |
| Evidence tier per relationship | PRIMARY_DOMAIN / SECONDARY_DOMAIN |
| Multi-project WEB-ZPM-01 case | Person ↔ Website |
| Deprecated PRJ-0010 as BELONGS_TO target | Website ↔ Domain edges |
| Wave 5 ZPM readiness statement | Runtime / API / database |

**Binding operator decisions (enforced):**

- **REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04** — approved list only; no additional edges.
- **REL-ZPM-WB-02** — **cancelled** per COR-ZPM-WEB-06; not attested.
- **OWNS** — structural business ownership (ORG-0005 → WEB-ZPM-01).
- **BELONGS_TO** — initiative grouping (WEB-ZPM-01 → Project); WEB-ZPM-01 belongs to **two** projects — Triumph REL-0027/0028 analog.
- **OPERATES** — **не создавать**; remains **SAFE UNKNOWN** until future governance review.

---

## 2. Pre-check — endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **WEB-ZPM-01** bzpm.ru | **active** | AT-W4-ZPM-01 | **Pass** |
| **PRJ-0009** | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** | **deprecated** | AT-W3-ZPM-02 | **Pass** |
| **REL-ZPM-PJ-01..04** | **active** | AT-W3B-ZPM-01..02 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested before relationship promotion.

---

## 3. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W4B-ZPM-01** | REL-ZPM-WB-01, REL-ZPM-WB-03 | WEB-ZPM-01 **active**; PRJ-0009 **active**, PRJ-0010 **deprecated**; multi-project approved; COR-ZPM-WEB-07/08 | **active** |
| **AT-W4B-ZPM-02** | REL-ZPM-WB-04 | ORG-0005 **active**; WEB-ZPM-01 **active**; COR-ZPM-WEB-09 | **active** |

---

## 4. Per-relationship attestation records

### 4.1 WEB-ZPM-01 — REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04

| Field | REL-ZPM-WB-01 | REL-ZPM-WB-03 | REL-ZPM-WB-04 |
|-------|---------------|---------------|---------------|
| **relationship_id** | REL-ZPM-WB-01 | REL-ZPM-WB-03 | REL-ZPM-WB-04 |
| **source_id** | WEB-ZPM-01 bzpm.ru | WEB-ZPM-01 bzpm.ru | ORG-0005 ЗПМ |
| **target_id** | PRJ-0009 Каталог-платформа bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | WEB-ZPM-01 bzpm.ru |
| **relationship_type** | **BELONGS_TO** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-ZPM-01 **active**; PRJ-0009 **active**; E0 EV-ZPM-OP-ACT-01; REL-ZPM-PJ-01; single-property model | WEB-ZPM-01 **active**; PRJ-0010 **deprecated**; E0 EV-ZPM-OP-HIST-01; LT-P01; Triumph REL-0027 analog; COR-ZPM-WEB-07 | ORG-0005 **active**; WEB-ZPM-01 **active**; E0 EV-ZPM-OP-ACT-01; EV-W1B-CC-01; COR-ZPM-WEB-09 |
| **evidence_tier** | **E0** | **E0** | **E0** |
| **lifecycle_state** | **active** | **active** | **active** |
| **notes** | Ongoing catalog-platform initiative | Multi-project case — historical deliverable container; replaces cancelled REL-ZPM-WB-02 | OPERATES for ORG-0001 not created |

---

## 5. Relationships created — summary

| relationship_id | source_id | target_id | relationship_type | lifecycle_state |
|-----------------|-----------|-----------|-------------------|-----------------|
| REL-ZPM-WB-01 | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | **BELONGS_TO** | **active** |
| REL-ZPM-WB-03 | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | **BELONGS_TO** | **active** |
| REL-ZPM-WB-04 | ORG-0005 ЗПМ | WEB-ZPM-01 bzpm.ru | **OWNS** | **active** |

**Promotion count:** **3 / 3** relationships attested  
**Deferred from approved list:** **0**  
**Cancelled (not attested):** **1** (REL-ZPM-WB-02)

---

## 6. Evidence basis

| Ref | Tier | Role | Relationships |
|-----|------|------|---------------|
| **EV-ZPM-OP-ACT-01** | E0 | Operator — current catalog rebuild; ongoing client property | REL-ZPM-WB-01, REL-ZPM-WB-04 |
| **EV-ZPM-OP-HIST-01** | E0 | Operator — historical `bzpm.ru` site delivery ~5y ago | REL-ZPM-WB-03 |
| **EV-W1B-CC-01** | E1 | `bzpm/Реквизиты.docx` — org anchor; §17 indirect hostname corroboration | Supporting context — REL-ZPM-WB-04 |
| **AT-W4-ZPM-01** | attestation | WEB-ZPM-01 **active** | All edges |
| **AT-W3-ZPM-01** | attestation | PRJ-0009 **active** | REL-ZPM-WB-01 |
| **AT-W3-ZPM-02** | attestation | PRJ-0010 **deprecated** | REL-ZPM-WB-03 |
| **AT-W1B-01** | attestation | ORG-0005 **active** | REL-ZPM-WB-04 |
| **AT-W3B-ZPM-01..02** | attestation | REL-ZPM-PJ-01..04 COMMISSIONED_BY / EXECUTES context | Cross-check only |
| **COR-ZPM-WEB-01..12** | correction | Single Website model; queue correction | REL-ZPM-WB-03 added; REL-ZPM-WB-02 cancelled |
| Triumph REL-0027/0028/0032 | precedent | Multi-project BELONGS_TO + OWNS pattern | Structural analog |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (REL-ZPM-WB-01, REL-ZPM-WB-04)
E0 operator — EV-ZPM-OP-HIST-01 (REL-ZPM-WB-03)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx (org anchor only)
```

---

## 7. Validation results

| Check | Result |
|-------|--------|
| Single Website model (WEB-ZPM-01 only) | **Pass** — WEB-ZPM-02 retired; COR-ZPM-WEB-01 |
| Triumph precedent WEB-0006 → PRJ-0004 + PRJ-0006 | **Pass** — REL-0027/0028 analog → REL-ZPM-WB-01/03 |
| Multi-project Website pattern | **Pass** — WEB-ZPM-01 → PRJ-0009 + PRJ-0010 |
| Deprecated project compatibility (LT-P01) | **Pass** — PRJ-0010 **deprecated** + REL-ZPM-WB-03 **active** |
| OWNS vs BELONGS_TO separation | **Pass** — distinct relationship families |
| No Domain entities | **Pass** |
| No PRIMARY_DOMAIN | **Pass** |
| No CLIENT_OF | **Pass** |
| No OPERATES | **Pass** |
| No Person → Website / Person → Project | **Pass** |
| No Organization → Domain | **Pass** |
| REL-ZPM-WB-02 not attested | **Pass** — COR-ZPM-WEB-06 |
| No conflict with Triumph graph (REL-0027..0035) | **Pass** — distinct org + website namespace |

---

## 8. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| REL-ZPM-WB-02 WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancelled** — COR-ZPM-WEB-06 |
| ORG-0001 OPERATES WEB-ZPM-01 | **Excluded** — SAFE UNKNOWN; separate governance |
| REL-0016 ORG-0005 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| DOM-* `bzpm.ru` | **Excluded** — Wave 5 ZPM |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Excluded** — Wave 5B ZPM |
| Website → Domain | **Excluded** — Wave 5 |
| Person → Website (PER-0014, PER-0015) | **Excluded** — operator scope |
| Person → Project | **Excluded** — operator scope |
| Organization → Domain | **Excluded** — Wave 5 |
| WEB-ZPM-02 | **Retired** — COR-ZPM-WEB-01 |
| Foundation documents | **Not modified** |

---

## 9. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 3 directed Website-family edges — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-ZPM-01 / PRJ-0009/0010 / ORG-0005 attested — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship `active`; PRJ-0010 deprecated valid target — **Pass** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | Deprecated project + active BELONGS_TO — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E0 tier for client property structural path — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; population plan not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |
| EIR-W01 single property model | One Website per `bzpm.ru` — **Pass** |
| EFV-03 two-phase rule | Valid at Project layer — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-01 **active** | **Pass** |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | BELONGS_TO targets exist | **Pass** |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY consistent with grouping | **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Triumph precedent pattern match | **Pass** |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | 4B queue corrected pre-attestation | **Pass** |

**Foundation modified:** **No**  
**Wave 1 / 2 / 2B / 3 / 3B / 4 ZPM modified:** **No**  
**Triumph Wave 4B (REL-0027..0035) modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (BELONGS_TO + OWNS only — baseline families)  
**Domain entities introduced:** **No**  
**Website ↔ Domain edges created:** **No**

---

## 10. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact | Status |
|----|-------|----------|-------------|--------|
| **SU-ZPM-PRJ-01** | Historical contract / act dates (PRJ-0010) | Low | Does not block Wave 5 | **Unchanged** |
| **SU-ZPM-PRJ-02** | Formal acceptance document (E1 upgrade path) | Low | Optional future upgrade | **Unchanged** |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Medium | Wave 6 | **Unchanged** |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Wave 5 ZPM DOM-* | **Open** — Wave 5 |
| **SU-W4-ZPM-01** | Live URL probe for `bzpm.ru` | Low | E0 sufficient | **Unchanged** |
| **SU-W4B-ZPM-01** | ORG-0001 OPERATES WEB-ZPM-01 | Low | Not blocking Wave 5 | **Open** |
| **SU-W4B-ZPM-02** | `www.bzpm.ru` redirect / secondary hostname | Low | Wave 5 hostname policy | **Open** |
| **SU-W3B-ZPM-01** | Dual BELONGS_TO for same hostname | Medium | Wave 4B | **Resolved** — REL-ZPM-WB-01 + REL-ZPM-WB-03 attested |
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence | Medium | Wave 4/4B | **Resolved** — single Website model |
| **SU-W4-ZPM-03** | Single DOM-* vs dual generation | Low | Wave 5 | **Resolved** — DOM-* → WEB-ZPM-01 |
| **ME-W4B-ZPM-01** | PRIMARY_DOMAIN / DOM-* not minted | Low | Wave 5 by design | **Expected** |

**Blocking gaps remaining:** **None**

---

## 11. Candidate Wave 5 ZPM Domain roster

| Candidate | Type | Endpoints | Prerequisite | Notes |
|-----------|------|-----------|--------------|-------|
| **DOM-ZPM-01** *(draft id)* | Domain entity | `bzpm.ru` | Wave 5 ZPM population | Singleton per COR-ZPM-WEB-10; SU-W4-ZPM-03 resolved |
| DOM-ZPM-01 → WEB-ZPM-01 | **PRIMARY_DOMAIN** | apex hostname | Domain attestation + Wave 5B ZPM | Unambiguous target — no WEB-ZPM-02 |
| ORG-0005 → DOM-ZPM-01 | **OWNS** (domain) | registrar / CC evidence | Wave 5; SU-ZPM-PRJ-08 | Distinct from website OWNS (REL-ZPM-WB-04) |
| `www.bzpm.ru` | SECONDARY_DOMAIN or redirect | WEB-ZPM-01 | Wave 5 hostname policy | **SAFE UNKNOWN** — SU-W4B-ZPM-02 |

**Not in Wave 5 candidate roster:** DOM entities for retired WEB-ZPM-02; PRIMARY_DOMAIN to deprecated Website; CLIENT_OF; OPERATES.

---

## 12. Wave 5 ZPM readiness assessment

### 12.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 4 ZPM Website attested **active** (WEB-ZPM-01) | **Pass** — AT-W4-ZPM-01 |
| Wave 4B ZPM BELONGS_TO for WEB-ZPM-01 | **Pass** — 2/2 attested (REL-ZPM-WB-01, REL-ZPM-WB-03) |
| Wave 4B ZPM OWNS ORG-0005 → WEB-ZPM-01 | **Pass** — 1/1 attested (REL-ZPM-WB-04) |
| WEB-ZPM-01 multi-project case resolved | **Pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03 |
| Single Website model honored | **Pass** — WEB-ZPM-02 not minted |
| Deprecated PRJ-0010 BELONGS_TO attested (LT-P01) | **Pass** — REL-ZPM-WB-03 |
| OPERATES correctly excluded | **Pass** |
| No Domain entities prematurely minted | **Pass** |
| PRIMARY_DOMAIN target unambiguous (WEB-ZPM-01 singleton) | **Pass** — COR-ZPM-WEB-10 |
| Foundation unchanged | **Pass** |

### 12.2 Verdict

```text
READY FOR WAVE 5 ZPM DOMAIN POPULATION
```

**Conditions:**

1. Wave 5 ZPM executes as **separate population pass** — Domain entities and Domain-family relationships not bundled into 4B-ZPM.
2. PRIMARY_DOMAIN edges require Domain attestation first, then Wave 5B ZPM cross-links.
3. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking Domain population.
4. REL-0016 CLIENT_OF remains **Wave 6**.
5. Single DOM-* `bzpm.ru` → WEB-ZPM-01 **PRIMARY_DOMAIN** per correction execution — no dual-generation ambiguity.

---

## 13. Attestation verdict

```text
WAVE 4B ZPM WEBSITE RELATIONSHIP ATTESTATION — COMPLETE
3 / 3 Website-family relationships attested active
0 relationships deferred from approved 4B-ZPM list
1 relationship cancelled (REL-ZPM-WB-02 — COR-ZPM-WEB-06)
Wave 5 ZPM Domain population — READY TO START
```

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION** | [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) §12 | **Superseded** — REL-ZPM-WB-01/03/04 now **active** |
| **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIPS** | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) §12 | **Superseded** — 4B-ZPM attestation act complete |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **PARTIALLY READY** | Full approved list attested |
| **READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIP POPULATION** | Superseded — attestation act complete |

---

## 14. Attestation results summary

| relationship_id | source_id | target_id | relationship_type | evidence_tier | tranche | lifecycle_state |
|-----------------|-----------|-----------|-------------------|---------------|---------|-----------------|
| REL-ZPM-WB-01 | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | **BELONGS_TO** | E0 | AT-W4B-ZPM-01 | **active** |
| REL-ZPM-WB-03 | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | **BELONGS_TO** | E0 | AT-W4B-ZPM-01 | **active** |
| REL-ZPM-WB-04 | ORG-0005 ЗПМ | WEB-ZPM-01 bzpm.ru | **OWNS** | E0 | AT-W4B-ZPM-02 | **active** |

**Relationships created:** **3**  
**Domain entities created:** **0**  
**Person ↔ Website edges created:** **0**

---

## 15. Package lineage

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
        ├── Wave 3B ZPM Project Relationship (REL-ZPM-PJ-01..04) ──► AT-W3B-ZPM-01..02 (COMPLETE)
        │
        ├── ZPM Website Model Correction ──► COR-ZPM-WEB-01..12 (EXECUTED)
        │
        ├── Wave 4 ZPM Website (WEB-ZPM-01) ──► AT-W4-ZPM-01 (COMPLETE)
        │
        └── Wave 4B ZPM Website Relationship (REL-ZPM-WB-01/03/04) ──► AT-W4B-ZPM-01..02 (THIS ACT)
                    │
                    └──► Wave 5 ZPM Domain Population (NEXT)
```

---

## 16. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website attestation prerequisite |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Core Wave 4B Triumph precedent |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution basis |

---

*ATLAS Wave 4B ZPM Website Relationship Attestation v1 — documentation only.*
