# ATLAS Wave 6A Commercial Relationship Attestation v1

**Status:** **attested** — first official Organization ↔ Organization commercial relationship attestation set for ATLAS.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 6B execution, contract registry.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Wave 5 Domain Population: **COMPLETE**
- Wave 5B Domain Relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 6A COMMERCIAL RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** первого набора **Organization ↔ Organization** commercial relationships для Wave 6A: **1** запись переведена в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Organization → Organization **CLIENT_OF** (1) | **VENDOR_OF**, **PARTNER_OF**, **SUPPLIER_OF** |
| ORG-0004 Triumph → ORG-0001 Polygon | Person, Project, Website, Domain edges |
| Evidence tier per relationship | Contract / invoice primary path |
| Direction validation | Runtime / API / database |
| Ownership neutrality enforcement | New entity types |
| Wave 6B readiness statement | Full historical commercial catalog |

**Binding operator corrections (enforced):**

- Triumph (**ORG-0004**) **purchases services from** Polygon (**ORG-0001**).
- Canonical direction: **ORG-0004 ──CLIENT_OF──► ORG-0001** — not reversed.
- **VENDOR_OF** inverse edge — **не создавать** в этом пакете.
- Person **OWNER** / project **EXECUTES** — **не substitute** for org↔org CLIENT_OF.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W6A-01** | REL-0016 | E1 dataset REL-0016; E1 Wave 3B COMMISSIONED_BY/EXECUTES corroboration; EV-0005 / EV-0003; ORG-0001, ORG-0004 **active**; operator commercial reality | **active** |

---

## 3. Per-relationship attestation records

### 3.1 REL-0016 — ORG-0004 → ORG-0001 CLIENT_OF

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0016 |
| **source_id** | ORG-0004 ООО «Триумф» |
| **target_id** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | ORG-0004 **active** (Wave 1 W1-B); ORG-0001 **active** (Wave 1 W1-A); E1 dataset Relationships draft (type CLIENT_OF, note «Клиент Полигона»); E1 Wave 3B: PRJ-0004..0008 **COMMISSIONED_BY** ORG-0004 + **EXECUTES** ORG-0001; EV-0005 Triumph CC; EV-0003 Polygon CC (LE-0001); operator-confirmed: Triumph purchases services from Polygon |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | First canonical org↔org commercial edge; structural — not deal stage or contract value |

---

## 4. Direction validation (attestation record)

| Validation step | Outcome |
|-----------------|---------|
| Identify org pair | ORG-0004 Triumph, ORG-0001 Polygon |
| Business reality: purchaser → provider | Triumph → Polygon **Pass** |
| Taxonomy: subject = client, object = vendor | ORG-0004 → ORG-0001 **Pass** |
| Reject ORG-0001 CLIENT_OF ORG-0004 | **Rejected** — contradicts reality |
| Reject dual CLIENT_OF | **Pass** — single canonical slot |
| VENDOR_OF mirror | **Not attested** — out of scope |
| Project graph consistency | 5 Triumph projects COMMISSIONED_BY + Polygon EXECUTES **Pass** |

Per [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §6.1 conflicting client claims workflow — **no conflict detected**.

---

## 5. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| ORG-0001 → **VENDOR_OF** → ORG-0004 | **Excluded** — not in approved 6A list |
| **PARTNER_OF** / **SUPPLIER_OF** (any pair) | **Excluded** |
| ORG-0002 / ORG-0003 commercial org↔org edges | **Deferred** |
| Person / Project / Website / Domain relationships | **Out of scope** |
| Contract, invoice, deal-stage metadata on edge | **Forbidden** |

---

## 6. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 1 directed Org→Org edge; RP-04 single canonical slot — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §2 | CLIENT_OF in Organization ↔ Organization family — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Edge **active** post attestation; both endpoints active — **Pass** |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | E1 minimum for CLIENT_OF; direction verified — **Pass** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) | Organization endpoints only — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active` — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.6 | E1 tier met for CLIENT_OF — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) | Wave **6A** sub-wave scope — **Pass** |
| [OPS-ATLAS-ALIGNMENT-v1.md](../foundation/OPS-ATLAS-ALIGNMENT-v1.md) §4.2 | OPS Client → Organization + CLIENT_OF — **Pass** |

**Foundation modified:** **No**  
**Prior wave registers modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Organization → Organization only)

---

## 7. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W6A-01** | REL-0016 `effective_from` / `effective_to` dates | Low | Optional future enrichment |
| **SU-W6A-02** | Service line granularity (web, SEO, support) on CLIENT_OF edge | Low | Not encoded per RP-03 — remains UNKNOWN at edge level |
| **SU-W6A-03** | Whether formal E2 contract extract exists externally | Low | Not required for structural E1 attestation |
| **SU-W6A-04** | i-SEO operational participation vs Polygon EXECUTES on SEO projects | Low | Org-level delivery org remains ORG-0001 per Wave 3B |
| **SU-W6A-05** | W1-C latent historical client orgs → ORG-0001 | Medium for graph completeness | Blocks only unpopulated org pairs |
| **SU-W6A-06** | ORG-0001 **OPERATES** Triumph websites | Low | SU-W4B-01 — separate from CLIENT_OF |

---

## 8. Wave 6B readiness assessment

### 8.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 6A priority commercial edge attested (REL-0016) | **Pass** — 1/1 |
| Both org endpoints **active** | **Pass** |
| Direction validated against taxonomy and business reality | **Pass** |
| No disputed CLIENT_OF slot | **Pass** |
| VENDOR_OF / PARTNER / SUPPLIER excluded per scope | **Pass** |
| Project + Website graphs consistent with commercial direction | **Pass** |
| Ownership neutrality enforced | **Pass** |

### 8.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Commercial org↔org graph insufficient for next expansion pass |
| **PARTIALLY READY** | Next pass may start for subset only |
| **READY FOR WAVE 6B COMMERCIAL GRAPH EXPANSION** | Priority Triumph ↔ Polygon commercial anchor complete |

### 8.3 Verdict

```text
READY FOR WAVE 6B COMMERCIAL GRAPH EXPANSION
```

**Conditions:**

1. Wave 6B executes as **separate population pass** — additional org↔org candidates require distinct evidence gates per pair.
2. **VENDOR_OF** mirror for REL-0016 remains **not created** unless operator requests inverse assertion in a future review.
3. W1-C latent clients and unpopulated partner orgs (Moscow SERM, Metallka) remain **deferred** until Organization population.
4. SU-W6A-01..06 do not block Wave 6B candidate intake for other relationship families or additional commercial pairs.

---

## 9. Attestation verdict

```text
WAVE 6A COMMERCIAL RELATIONSHIP ATTESTATION — COMPLETE
1 / 1 Organization ↔ Organization CLIENT_OF relationship attested active
0 relationships deferred from approved 6A list
Wave 6B commercial graph expansion — READY TO START
```

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Attested commercial relationship roster |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Project-level corroboration |
| [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) | Draft REL-0016 source id |
