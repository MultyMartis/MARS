# ATLAS Wave 6B Commercial Relationship Attestation v1

**Status:** **attested** — Wave 6B Organization ↔ Organization commercial relationship attestation set (ZPM + SIBCAR).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Foundation amendment, new entity creation.

**Prerequisites (operator-confirmed):**

- Wave 6A Commercial Relationships: **COMPLETE** (REL-0016 **active**)
- Wave 1B ZPM: **COMPLETE** — ORG-0005 **active**
- Wave 1C SIBCAR: **COMPLETE** — ORG-0006 **active**
- Wave 3B ZPM Project Relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 6B COMMERCIAL RELATIONSHIP POPULATION**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** Wave 6B: **2** новых **Organization ↔ Organization** commercial relationships переведены в **active** canonical state, расширяя commercial graph с 1 до **3** CLIENT_OF рёбер к ORG-0001 Полигон.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Organization → Organization **CLIENT_OF** (2 new) | **VENDOR_OF**, **PARTNER_OF**, **SUPPLIER_OF** |
| ORG-0005 ЗПМ → ORG-0001 Полигон (REL-0040) | New Organizations, Legal Entities, Persons |
| ORG-0006 SIBCAR → ORG-0001 Полигон (REL-0041) | New Projects, Websites, Domains |
| Evidence tier per relationship | Contract / invoice primary path |
| Direction validation vs REL-0016 | Runtime / API / database |
| Duplicate review | Foundation amendments |
| Ownership neutrality enforcement | Invented documentary evidence |

**Binding operator corrections (enforced):**

- ЗПМ (**ORG-0005**) **purchases services from** Polygon (**ORG-0001**).
- SIBCAR (**ORG-0006**) **purchases services from** Polygon (**ORG-0001**).
- Canonical direction: **CLIENT ──CLIENT_OF──► VENDOR** — identical to **REL-0016**.
- **VENDOR_OF** inverse edges — **не создавать** в этом пакете.
- Person / project **EXECUTES** — **не substitute** for org↔org CLIENT_OF.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W6B-01** | REL-0040 | E1 EV-W1B-CC-01; E1 Wave 3B-ZPM REL-ZPM-PJ-01..04; Wave 4B REL-ZPM-WB-04; ORG-0005, ORG-0001 **active**; operator commercial reality | **active** |
| **AT-W6B-02** | REL-0041 | E1 EV-W1C-CC-01; ORG-0006 **business_role CLIENT**; Polygon Category A channel; ORG-0006, ORG-0001 **active**; operator commercial reality | **active** |

---

## 3. Per-relationship attestation records

### 3.1 REL-0040 — ORG-0005 → ORG-0001 CLIENT_OF

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0040 |
| **source_id** | ORG-0005 ЗПМ |
| **target_id** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | ORG-0005 **active** (AT-W1B-01); ORG-0001 **active** (Wave 1 W1-A); E1 EV-W1B-CC-01; E1 Wave 3B-ZPM: PRJ-0009 **COMMISSIONED_BY** ORG-0005 + **EXECUTES** ORG-0001; PRJ-0010 historical pair; E0 EV-ZPM-OP-ACT-01 / EV-ZPM-OP-HIST-01; Wave 4B REL-ZPM-WB-04; operator-confirmed: ЗПМ purchases services from Polygon |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Strongest Wave 6B candidate; full ZPM stack corroboration; replaces erroneous prior «REL-0016» placeholder label |

### 3.2 REL-0041 — ORG-0006 → ORG-0001 CLIENT_OF

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0041 |
| **source_id** | ORG-0006 SIBCAR |
| **target_id** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | ORG-0006 **active** (AT-W1C-01); ORG-0001 **active** (Wave 1 W1-A); E1 EV-W1C-CC-01; W1-C **CLIENT** business role; Polygon channel Category A (`sibcar\` CC path); operator-confirmed: SIBCAR purchases services from Polygon; OCPilot SITE-001 *(informational — not sole proof)* |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Project COMMISSIONED_BY/EXECUTES corroboration **absent** — attested on CC + CLIENT role + channel discipline; see SU-W6B-04 |

---

## 4. Direction validation (attestation record)

### 4.1 Per-edge validation

| Validation step | REL-0040 | REL-0041 | Outcome |
|-----------------|----------|----------|---------|
| Identify org pair | ORG-0005, ORG-0001 | ORG-0006, ORG-0001 | **Pass** |
| Business reality: purchaser → provider | ЗПМ → Polygon | SIBCAR → Polygon | **Pass** |
| Taxonomy: subject = client, object = vendor | ORG-0005 → ORG-0001 | ORG-0006 → ORG-0001 | **Pass** |
| Reject reversed CLIENT_OF | **Rejected** | **Rejected** | **Pass** |
| Reject dual CLIENT_OF | Single canonical slot each | Single canonical slot each | **Pass** |
| VENDOR_OF mirror | **Not attested** | **Not attested** | **Pass** |

### 4.2 Cross-check vs REL-0016 (mandatory)

| client_org | relationship_id | direction vs REL-0016 | Outcome |
|------------|-----------------|-------------------------|---------|
| ORG-0004 Триумф | REL-0016 | **Reference** (Wave 6A) | **active** |
| ORG-0005 ЗПМ | REL-0040 | **Identical** CLIENT_OF → ORG-0001 | **Pass** |
| ORG-0006 SIBCAR | REL-0041 | **Identical** CLIENT_OF → ORG-0001 | **Pass** |

```text
Business fact:  Each client org purchases services from Polygon
Taxonomy rule:  Subject (client) ──CLIENT_OF──► Object (vendor)

ORG-0004 ──CLIENT_OF──► ORG-0001   ✓  REL-0016
ORG-0005 ──CLIENT_OF──► ORG-0001   ✓  REL-0040
ORG-0006 ──CLIENT_OF──► ORG-0001   ✓  REL-0041
```

Per [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §6.1 conflicting client claims workflow — **no conflict detected**.

---

## 5. Duplicate review (attestation sign-off)

| review_id | signal | outcome |
|-----------|--------|---------|
| W6B-D-01 | REL-0040 vs REL-0016 | **Distinct client endpoints** |
| W6B-D-02 | REL-0041 vs REL-0016 / REL-0040 | **Distinct client endpoints** |
| W6B-D-03 | ORG-0005 vs ORG-0006 identity | **Distinct** — prior W1B/W1C duplicate review |
| W6B-D-04 | Duplicate CLIENT_OF slot same pair | **None** |
| W6B-D-05 | REL-0016 id collision with ZPM placeholder | **Resolved** — REL-0040 assigned |

---

## 6. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| ORG-0001 → **VENDOR_OF** → clients | **Excluded** |
| **PARTNER_OF** / **SUPPLIER_OF** (any pair) | **Excluded** |
| ORG-0007 Makita → ORG-0003 i-SEO **CLIENT_OF** | **Deferred** |
| Moscow SERM / Metallka commercial edges | **Deferred** |
| New Organizations / Persons / Projects / Websites / Domains | **Excluded** |
| Person / Project / Website / Domain new edges | **Out of scope** |
| Contract, invoice, deal-stage metadata on edge | **Forbidden** |
| Invented contracts / invoices / acceptance acts | **Forbidden** |

---

## 7. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 2 new directed Org→Org edges; RP-04 single canonical CLIENT_OF slot per pair — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §2 | CLIENT_OF in Organization ↔ Organization family — **Pass** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Edges **active** post attestation; all endpoints active — **Pass** |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | E1 minimum for CLIENT_OF; direction verified — **Pass** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) | Organization endpoints only — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active` — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E1 tier met for CLIENT_OF — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship — **Pass** |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | REL-0016 precedent honored — **Pass** |
| [OPS-ATLAS-ALIGNMENT-v1.md](../foundation/OPS-ATLAS-ALIGNMENT-v1.md) §4.2 | OPS Client → Organization + CLIENT_OF — **Pass** |

**Foundation modified:** **No**  
**Prior wave registers modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Organization → Organization only)

---

## 8. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W6B-01** | REL-0040 / REL-0041 `effective_from` / `effective_to` | Low | Optional enrichment |
| **SU-W6B-02** | Service line granularity on CLIENT_OF edges | Low | Not encoded per RP-03 |
| **SU-W6B-03** | Formal E2 contract extract existence (external) | Low | Not required for structural E1 |
| **SU-W6B-04** | SIBCAR project-level COMMISSIONED_BY / EXECUTES | Medium | Does **not** invalidate REL-0041 |
| **SU-W6B-05** | SIBCAR production Website / Domain stack | Medium | Future Waves 3–5 SIBCAR — separate from CLIENT_OF |
| **SU-W6A-01..06** | Carried from Wave 6A | Low | Unchanged — do not block post-6B expansion |

---

## 9. Updated commercial graph summary

```text
Before Wave 6B:
  ORG-0004 Триумф ──CLIENT_OF──► ORG-0001 Полигон   [REL-0016]

After Wave 6B:
  ORG-0004 Триумф ──CLIENT_OF──► ORG-0001 Полигон   [REL-0016]
  ORG-0005 ЗПМ    ──CLIENT_OF──► ORG-0001 Полигон   [REL-0040]
  ORG-0006 SIBCAR ──CLIENT_OF──► ORG-0001 Полигон   [REL-0041]
```

| Metric | Value |
|--------|-------|
| Total attested CLIENT_OF to ORG-0001 | **3** |
| Wave 6B additions | **2** |
| Direction consistency (ORG-0004, 0005, 0006) | **Identical** |
| Polygon vendor inbound edges | REL-0016, REL-0040, REL-0041 |

---

## 10. Readiness assessment

### 10.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 6A anchor (REL-0016) attested | **Pass** |
| ORG-0005, ORG-0006 endpoints **active** | **Pass** |
| E1 evidence minimum met (both edges) | **Pass** |
| Direction validated vs REL-0016 | **Pass** |
| Duplicate review complete | **Pass** |
| No disputed CLIENT_OF slot | **Pass** |
| Evidence First — no invented documents | **Pass** |
| Foundation unchanged | **Pass** |

### 10.2 Verdict

```text
WAVE 6B COMMERCIAL RELATIONSHIP ATTESTATION — COMPLETE
2 / 2 new Organization ↔ Organization CLIENT_OF relationships attested active
3 / 3 total Polygon client commercial edges in canonical graph
0 relationships deferred from approved 6B list
```

### 10.3 Post-6B conditions

1. **VENDOR_OF** mirror edges remain **not created** unless operator requests in future review.
2. SIBCAR downstream stack (Project, Website, Domain, Person edges) remains **separate** future waves — REL-0041 does not imply those entities exist.
3. ORG-0007 Makita / channel-specific commercial edges follow **separate** evidence gates (C-03).
4. SU-W6B-04 (SIBCAR project corroboration) should be **closed** when SIBCAR Wave 3 population executes — does not retroactively dispute REL-0041.

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Attested commercial relationship roster |
| [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Prior graph (REL-0016 only) |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | ZPM project corroboration |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | SIBCAR org anchor |
