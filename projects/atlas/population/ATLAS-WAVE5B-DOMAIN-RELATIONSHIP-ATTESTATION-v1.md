# ATLAS Wave 5B Domain Relationship Attestation v1

**Status:** **attested** — first official Domain-family relationship attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, DNS automation, registrar integration, Wave 6 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Wave 5 Domain Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 5B DOMAIN RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** первого набора **Domain-family** relationships для Wave 5B: **4** записи PRIMARY_DOMAIN переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Domain → Website **PRIMARY_DOMAIN** (4) | Organization → Domain **OWNS** |
| Triumph client properties DOM-0001..0004 → WEB-0006..0009 | Organization → Domain **CUSTODIAN** |
| Evidence tier per relationship | **SECONDARY_DOMAIN** (no evidence) |
| Ownership neutrality enforcement | **REDIRECTS_TO** / **POINTS_TO** |
| Singleton PRIMARY_DOMAIN per Website | DNS relationships |
| Wave 6 readiness statement | Registrar relationships |
| | Person ↔ Domain |
| | Runtime / API / database |

**Binding operator modeling decision (enforced):**

- **PRIMARY_DOMAIN** — structural hostname-to-property link; **not** registrant ownership.
- **Website OWNS** (Wave 4B) — attested org-level **web property** ownership; **does not substitute** Domain OWNS.
- **Domain OWNS** — **не создавать** без E1 registrar/registrant evidence; remains **proposed only** / **SAFE UNKNOWN**.
- **SECONDARY_DOMAIN** — **не создавать** без attested alias evidence (`www.gktriumph.ru` deferred).

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W5B-01** | REL-0036 | DOM-0001 **active**; WEB-0006 **active**; co-terminous `gktriumph.ru`; live URL | **active** |
| **AT-W5B-02** | REL-0037 | DOM-0002 **active**; WEB-0007 **active**; separate subdomain FQDN | **active** |
| **AT-W5B-03** | REL-0038 | DOM-0003 **active**; WEB-0008 **active**; landing apex | **active** |
| **AT-W5B-04** | REL-0039 | DOM-0004 **active**; WEB-0009 **active**; landing apex | **active** |

---

## 3. Per-relationship attestation records

### 3.1 REL-0036 — DOM-0001 → WEB-0006 PRIMARY_DOMAIN

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0036 |
| **source_id** | DOM-0001 gktriumph.ru |
| **target_id** | WEB-0006 gktriumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | DOM-0001 **active** (Wave 5); WEB-0006 **active** (Wave 4); E1 co-terminous hostname; live `https://gktriumph.ru`; operator roster; REL-0032 website OWNS context (not domain registrant) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Singleton primary for WEB-0006; `www.gktriumph.ru` not modeled |

### 3.2 REL-0037 — DOM-0002 → WEB-0007 PRIMARY_DOMAIN

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0037 |
| **source_id** | DOM-0002 blog.gktriumph.ru |
| **target_id** | WEB-0007 blog.gktriumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | DOM-0002 **active**; WEB-0007 **active**; E1 FQDN match; distinct from DOM-0001/WEB-0006; REL-0033 website OWNS |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Subdomain entity — not collapsed into apex domain |

### 3.3 REL-0038 — DOM-0003 → WEB-0008 PRIMARY_DOMAIN

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0038 |
| **source_id** | DOM-0003 gruzotaxi-triumph.ru |
| **target_id** | WEB-0008 gruzotaxi-triumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | DOM-0003 **active**; WEB-0008 **active**; E1 co-terminous hostname; live URL; REL-0034 website OWNS; EV-0005 client context |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Standalone landing apex — not gktriumph.ru subdomain |

### 3.4 REL-0039 — DOM-0004 → WEB-0009 PRIMARY_DOMAIN

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0039 |
| **source_id** | DOM-0004 manipulator-triumph.ru |
| **target_id** | WEB-0009 manipulator-triumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | DOM-0004 **active**; WEB-0009 **active**; E1 co-terminous hostname; live URL; REL-0035 website OWNS |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Website Factory delivery context |

---

## 4. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| ORG-0004 → DOM-* **OWNS** | **Excluded** — proposed only; registrar E1 absent |
| ORG-0001 **CUSTODIAN** / **OPERATES** Domain | **Excluded** — SAFE UNKNOWN |
| `www.gktriumph.ru` **SECONDARY_DOMAIN** | **Excluded** — no alias evidence |
| **REDIRECTS_TO** / **POINTS_TO** | **Excluded** — out of 5B scope |
| DNS record relationships | **Excluded** — out of ATLAS scope |
| Registrar relationships | **Excluded** — no implementation |
| REL-0016 **CLIENT_OF** ORG-0004 → ORG-0001 | **Deferred** — Wave 6 |
| Person → Domain / Person → Website | **Excluded** — future expansion |
| Operator org domain edges | **Excluded** — separate tranche |

---

## 5. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §4 | 4 directed Domain→Website edges; singleton PRIMARY_DOMAIN — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7 | PRIMARY_DOMAIN family only — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | All edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | Parallel DOM/WEB ids linked by edge — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship **active** — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.6 | E1 for PRIMARY_DOMAIN — **Pass** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | Domain OWNS not inferred — **Pass** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4–5 | Website vs Domain classes — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; no DNS/registrar ops — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per tranche — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | All source domains **active** | **Pass** |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | All target websites **active** | **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website graph consistent | **Pass** |
| [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) §6.1 | Four candidates match attested set | **Pass** |

**Foundation modified:** **No**  
**Wave 1–5 modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (PRIMARY_DOMAIN only — baseline family)  
**Organization → Domain OWNS created:** **No**  
**DNS / registrar modeling:** **No**

**Important checks:**

| Check | Result |
|-------|--------|
| One PRIMARY_DOMAIN per Website | **Pass** — 4/4 |
| One Domain endpoint per relationship | **Pass** — 4/4 |
| No registrar assumptions | **Pass** |
| No DNS modeling | **Pass** |
| No Org → Domain ownership promotion | **Pass** |
| No new entity families | **Pass** |

---

## 6. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W5B-01** | Domain registrant / registrar for DOM-0001..0004 | Medium | Blocks **active** ORG→Domain OWNS — not blocking PRIMARY_DOMAIN |
| **SU-W5B-02** | `www.gktriumph.ru` hostname policy | Low | Wave 6 SECONDARY_DOMAIN or new DOM |
| **SU-W5B-03** | ORG-0001 technical custodian on DNS/registrar | Low | Not blocking Wave 6 org relationships |
| **SU-W5B-04** | ORG-0001 OPERATES Website/Domain | Low | SU-W4B-01 carries — separate governance |
| **SU-W5B-05** | REL-0016 CLIENT_OF commercial edge | Medium | Wave 6 primary candidate |

---

## 7. Wave 6 readiness assessment

### 7.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 5 Domain entities attested **active** (DOM-0001..0004) | **Pass** |
| Wave 5B PRIMARY_DOMAIN for all Triumph properties | **Pass** — 4/4 attested |
| Singleton PRIMARY_DOMAIN per Website | **Pass** |
| No premature Domain OWNS inferred | **Pass** |
| Registrar posture SAFE UNKNOWN documented | **Pass** |
| No DNS-level modeling | **Pass** |
| Website + Domain + PRIMARY_DOMAIN graph complete for pilot | **Pass** |
| Foundation unchanged | **Pass** |

### 7.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Domain relationship graph insufficient for Wave 6 |
| **PARTIALLY READY** | Wave 6 may start for subset only |
| **READY FOR WAVE 6 RELATIONSHIP POPULATION** | Domain-family anchor complete; remaining relationship pass may proceed |

### 7.3 Verdict

```text
READY FOR WAVE 6 RELATIONSHIP POPULATION
```

**Conditions:**

1. Wave 6 executes as **separate population pass** — org↔org (REL-0016 CLIENT_OF) and proposed Domain OWNS require distinct evidence gates.
2. ORG-0004 → DOM-* **OWNS** remains **proposed only** until registrar/registrant E1 (ME-W5-01 / SU-W5B-01).
3. `www.gktriumph.ru` policy resolved in Wave 6 or later — not blocking Wave 6 org relationship pass.
4. OPERATES / CUSTODIAN for ORG-0001 remains **SAFE UNKNOWN** — not blocking Wave 6.
5. Dataset draft flags **do not substitute** for steward attestation acts.

---

## 8. Attestation verdict

```text
WAVE 5B DOMAIN RELATIONSHIP ATTESTATION — COMPLETE
4 / 4 Domain-family relationships attested active
0 relationships deferred from approved 5B list
0 Organization → Domain OWNS promoted (registrar SAFE UNKNOWN)
Wave 6 relationship population — READY TO START
```

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md) | Domain entity attestation prerequisite |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Website-family prerequisite |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Draft hostname context |
