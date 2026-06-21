# ATLAS Wave 4B Website Relationship Attestation v1

**Status:** **attested** — first official Website relationship attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 5 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 4B WEBSITE RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** первого набора **Website-family** relationships для Wave 4B: **9** записей переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Website → Project **BELONGS_TO** (5) | **OPERATES** Organization → Website |
| Organization → Website **OWNS** (4) | **CLIENT_OF** Organization ↔ Organization |
| Triumph client properties WEB-0006..0009 | Domain entities |
| Evidence tier per relationship | PRIMARY_DOMAIN / SECONDARY_DOMAIN |
| Multi-project WEB-0006 case | Person ↔ Website |
| Deprecated PRJ-0004 as BELONGS_TO target | Website ↔ Domain edges |
| Wave 5 readiness statement | Runtime / API / database |

**Binding operator modeling decision (enforced):**

- **OWNS** — structural business ownership (ORG-0004 → Website).
- **BELONGS_TO** — initiative grouping (Website → Project); WEB-0006 may belong to **two** projects.
- **OPERATES** — **не создавать**; remains **SAFE UNKNOWN** until future governance review.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W4B-01** | REL-0027, REL-0028, REL-0032 | WEB-0006 **active**; PRJ-0004 **deprecated**, PRJ-0006 **active**; ORG-0004 **active**; multi-project approved | **active** |
| **AT-W4B-02** | REL-0029, REL-0033 | WEB-0007 **active**; PRJ-0007 **active**; distinct from WEB-0006 | **active** |
| **AT-W4B-03** | REL-0030, REL-0034 | WEB-0008 **active**; PRJ-0005 **active** | **active** |
| **AT-W4B-04** | REL-0031, REL-0035 | WEB-0009 **active**; PRJ-0008 **active** | **active** |

---

## 3. Per-relationship attestation records

### 3.1 WEB-0006 — REL-0027, REL-0028, REL-0032

| Field | REL-0027 | REL-0028 | REL-0032 |
|-------|----------|----------|----------|
| **relationship_id** | REL-0027 | REL-0028 | REL-0032 |
| **source_id** | WEB-0006 gktriumph.ru | WEB-0006 gktriumph.ru | ORG-0004 ООО «Триумф» |
| **target_id** | PRJ-0004 Редизайн gktriumph.ru | PRJ-0006 SEO gktriumph.ru | WEB-0006 gktriumph.ru |
| **relationship_type** | **BELONGS_TO** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-0006 **active**; PRJ-0004 **deprecated**; E1 dataset + REL-0017; live URL | WEB-0006 **active**; PRJ-0006 **active**; E1 dataset + REL-0021; operator multi-project approval | ORG-0004 **active**; WEB-0006 **active**; E1 + EV-0005; client structural ownership |
| **evidence_tier** | **E1** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** | **active** |
| **notes** | Redesign deliverable container | Resolves SU-W3B-04 — coexists with REL-0027 | OPERATES for ORG-0001 not created |

### 3.2 WEB-0007 — REL-0029, REL-0033

| Field | REL-0029 | REL-0033 |
|-------|----------|----------|
| **relationship_id** | REL-0029 | REL-0033 |
| **source_id** | WEB-0007 blog.gktriumph.ru | ORG-0004 Триумф |
| **target_id** | PRJ-0007 Блог gktriumph.ru | WEB-0007 blog.gktriumph.ru |
| **relationship_type** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-0007 **active**; PRJ-0007 **active**; E1 dataset; REL-0023 | ORG-0004 **active**; WEB-0007 **active**; E1 dataset |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Blog subsite initiative | Org-level property ownership |

### 3.3 WEB-0008 — REL-0030, REL-0034

| Field | REL-0030 | REL-0034 |
|-------|----------|----------|
| **relationship_id** | REL-0030 | REL-0034 |
| **source_id** | WEB-0008 gruzotaxi-triumph.ru | ORG-0004 Триумф |
| **target_id** | PRJ-0005 Грузотакси | WEB-0008 gruzotaxi-triumph.ru |
| **relationship_type** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-0008 **active**; PRJ-0005 **active**; E1 dataset; REL-0019; live URL | ORG-0004 **active**; WEB-0008 **active**; E1 + EV-0005 |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Yandex Direct landing | Client-owned landing |

### 3.4 WEB-0009 — REL-0031, REL-0035

| Field | REL-0031 | REL-0035 |
|-------|----------|----------|
| **relationship_id** | REL-0031 | REL-0035 |
| **source_id** | WEB-0009 manipulator-triumph.ru | ORG-0004 Триумф |
| **target_id** | PRJ-0008 Манипулятор | WEB-0009 manipulator-triumph.ru |
| **relationship_type** | **BELONGS_TO** | **OWNS** |
| **attestation_basis** | WEB-0009 **active**; PRJ-0008 **active**; E1 dataset; REL-0025; live URL | ORG-0004 **active**; WEB-0009 **active**; E1 + EV-0005 |
| **evidence_tier** | **E1** | **E1** |
| **lifecycle_state** | **active** | **active** |
| **notes** | Website Factory / ORCA case | MARS delivery pack ≠ duplicate Project |

---

## 4. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| ORG-0001 OPERATES WEB-0006..0009 | **Excluded** — SAFE UNKNOWN; separate governance |
| REL-0016 ORG-0004 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | **Excluded** — Wave 5 + 6C |
| Website → Domain | **Excluded** — Wave 5 |
| Domain → Website | **Excluded** — Wave 5 |
| Domain entities | **Excluded** — Wave 5 |
| Person → Website | **Excluded** — future expansion |
| WEB-0001..0005 operator org sites | **Excluded** — separate tranche |

---

## 5. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 9 directed Website-family edges — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5–6 | OWNS (Org→Website), BELONGS_TO (Website→Project) — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints WEB-* / PRJ-* / ORG-* attested — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship `active`; PRJ-0004 deprecated valid target — **Pass** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) LT-P01 | Deprecated project + active BELONGS_TO — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E1 tier for structural BELONGS_TO + OWNS — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; dataset draft not substituted — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | All source/target websites **active** | **Pass** |
| [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | All BELONGS_TO targets exist | **Pass** |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY consistent with grouping | **Pass** |
| Wave 1 Organization attestation | ORG-0004 **active** for OWNS source | **Pass** |

**Foundation modified:** **No**  
**Wave 1 / 2 / 2B / 3 / 3B / 4 modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (BELONGS_TO + OWNS only — baseline families)  
**Domain entities introduced:** **No**  
**Website ↔ Domain edges created:** **No**

---

## 6. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W4B-01** | ORG-0001 OPERATES WEB-0006..0009 | Low | Not blocking Wave 5 — separate governance |
| **SU-W4B-02** | REL-0016 CLIENT_OF ORG-0004 → ORG-0001 | Medium for commercial graph | Wave 6 |
| **SU-W4B-03** | PRJ-0001 MARS org edges | Medium for internal graph | Internal governance |
| **SU-W4B-04** | Person → Project / Person → Website participation | Low | Future expansion |
| **SU-W4B-05** | i-SEO subcontractor operational role on PRJ-0006 | Low | EXECUTES remains ORG-0001 (Wave 3B) |
| **SU-W4B-06** | Domain registrant vs org OWNS (website) distinction | Low | Clarified at Wave 5 Domain population |

---

## 7. Wave 5 readiness assessment

### 7.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 4 Websites attested **active** (WEB-0006..0009) | **Pass** |
| Wave 4B BELONGS_TO for all Triumph properties | **Pass** — 5/5 attested |
| Wave 4B OWNS ORG-0004 → WEB-0006..0009 | **Pass** — 4/4 attested |
| WEB-0006 multi-project case resolved | **Pass** — REL-0027 + REL-0028 |
| OPERATES correctly excluded | **Pass** |
| No Domain entities prematurely minted | **Pass** |
| PRIMARY_DOMAIN candidates documented | **Pass** — Wave 5 queue prepared |
| Foundation unchanged | **Pass** |

### 7.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Website graph insufficient for Domain population |
| **PARTIALLY READY** | Domain wave may start for subset only |
| **READY FOR WAVE 5 DOMAIN POPULATION** | Website + Website-family anchor complete for Triumph pilot |

### 7.3 Verdict

```text
READY FOR WAVE 5 DOMAIN POPULATION
```

**Conditions:**

1. Wave 5 executes as **separate population pass** — Domain entities and Domain-family relationships not bundled into 4B.
2. PRIMARY_DOMAIN edges require Domain attestation first, then Wave 6C cross-links.
3. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking Domain population.
4. REL-0016 CLIENT_OF remains **Wave 6**.
5. Dataset draft relationship flags **do not substitute** for steward attestation acts.

---

## 8. Attestation verdict

```text
WAVE 4B WEBSITE RELATIONSHIP ATTESTATION — COMPLETE
9 / 9 Website-family relationships attested active
0 relationships deferred from approved 4B list
Wave 5 Domain population — READY TO START
```

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) | Website attestation prerequisite |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | Prior relationship wave |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Draft REL-* source ids |
