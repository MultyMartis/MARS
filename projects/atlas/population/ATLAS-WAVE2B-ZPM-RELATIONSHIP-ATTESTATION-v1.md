# ATLAS Wave 2B ZPM Relationship Attestation v1

**Status:** **attested** — official Person → Organization relationship attestation set for Wave 2B ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 3 execution, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation: **COMPLETE**
- Wave 1B BZPM Attestation (ORG-0005): **COMPLETE** — AT-W1B-01
- Wave 2 core Person attestation: **COMPLETE**
- Wave 2 ZPM Person attestation (PER-0014, PER-0015): **COMPLETE** — AT-W2-ZPM-01..02
- Population verdict: **READY FOR WAVE 2B ZPM RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 2B ZPM Relationship Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W2B-ZPM-01** + **AT-W2B-ZPM-02**  
**Promotion:** REL-ZPM-01, REL-ZPM-02 — queued → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** набора **Person → Organization** relationships Wave 2B tranche **ZPM**: **2** записи переведены в **active** canonical state.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Person → Organization → **active** (ORG-0005) | Person ↔ Person |
| Evidence tier per relationship | New Person / Organization entities |
| Type assignment per approved 2B-ZPM list | Organization ↔ Organization |
| ORG-0005 primary contact pointer | Project / Website / Domain edges |
| Wave 3 ZPM readiness statement | Runtime / API / database |
| OWNER / EMPLOYEE / Diadoc signer exclusions | Foundation amendment |

**Binding operator decisions (enforced):**

- REL-ZPM-01 — **GENERAL_DIRECTOR** only; **no** OWNER edge despite CC 100% beneficial owner.
- REL-ZPM-02 — **REPRESENTATIVE** only; **no** EMPLOYEE edge.
- Diadoc signer — **SAFE UNKNOWN**; no relationship minted.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W2B-ZPM-01** | REL-ZPM-01 | E1 EV-W1B-CC-01 §19–§24; LE-0004 signatory; PER-0015 + ORG-0005 **active** | **active** |
| **AT-W2B-ZPM-02** | REL-ZPM-02 | E0 EV-W2-ZPM-OP-01; PER-0014 + ORG-0005 **active**; primary operational contact | **active** |

---

## 3. Per-relationship attestation records

### 3.1 REL-ZPM-01 — PER-0015 → ORG-0005

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-01 |
| **source_person** | PER-0015 Крюков Александр Сергеевич |
| **target_organization** | ORG-0005 ЗПМ |
| **relationship_type** | **GENERAL_DIRECTOR** |
| **attestation_basis** | PER-0015 **active** (AT-W2-ZPM-01); ORG-0005 **active** (AT-W1B-01); E1 EV-W1B-CC-01 §19–§24 — «Директор Крюков Александр Сергеевич»; LE-0004 `document_signatory` identical string; duplicate review W2-ZPM-D-02 **Pass** |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Director / document signatory. CC beneficial owner 100% §20 — on Person/LE only; **no** OWNER relationship. |

**REL-ZPM-01 taxonomy alignment (W2B-ZPM-TAX-01):** Operator label **GENERAL_DIRECTOR**; canonical taxonomy family **REPRESENTATIVE** (Person → Organization) with `role_qualifier: general_director` per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 and RR-02 — consistent with REL-0015 Triumph precedent.

### 3.2 REL-ZPM-02 — PER-0014 → ORG-0005

| Field | Value |
|-------|-------|
| **relationship_id** | REL-ZPM-02 |
| **source_person** | PER-0014 Алексей Владимирович Дубинский |
| **target_organization** | ORG-0005 ЗПМ |
| **relationship_type** | **REPRESENTATIVE** |
| **attestation_basis** | PER-0014 **active** (AT-W2-ZPM-02); ORG-0005 **active**; E0 EV-W2-ZPM-OP-01 — operator-direct identity, contacts (TG, phone, email), operational statements; CC silent on Дубинский (EFV-06); primary operational contact for Polygon vendor work |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Main communication channel between Polygon and ZPM. Not document signatory. Diadoc signer **SAFE UNKNOWN**. EMPLOYEE type **not** selected per operator scope. |

---

## 4. Organization pointer update

| Field | Prior | Attested |
|-------|-------|----------|
| ORG-0005 `primary_contact_person_id` | **SAFE UNKNOWN** | **PER-0014** |
| Basis | — | REL-ZPM-02 primary operational contact; steward confirmed at 2B attestation |

---

## 5. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PER-0015 → ORG-0005 **OWNER** | **Excluded** — operator scope |
| PER-0014 → ORG-0005 **EMPLOYEE** | **Excluded** — operator approved REPRESENTATIVE |
| Diadoc / EDO signer relationship | **Excluded** — **SAFE UNKNOWN** |
| Person ↔ Person edges | **Rejected** |
| Person ↔ Project edges | **Deferred** — Wave 3+ |
| ORG-0005 CLIENT_OF ORG-0001 | **Deferred** — Wave 6 |
| ORG-0005 ↔ ORG-0006 commercial edges | **Deferred** |
| New entities | **Not created** |
| Foundation documents | **Not modified** |

---

## 6. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 2 directed Person→Org edges to ORG-0005 — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) | REPRESENTATIVE in baseline — **Pass**; GENERAL_DIRECTOR via W2B-ZPM-TAX-01 — **Pass with note** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Both edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PER-0014/0015 / ORG-0005 attested active — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active` — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; no draft substitution — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |
| EFV-01 / EFV-06 / CPV-01 | CC read before PER-0015 conclusions; CC silence honored for PER-0014 — **Pass** |

**Foundation modified:** **No**  
**Wave 1 / Wave 2 / Wave 2 ZPM Person modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Person → Organization only)

---

## 7. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W2B-ZPM-01** | Diadoc / EDO specific signer (ORG-0005) | Medium *(signatory ops)* | Does not block Wave 3 — no edge minted |
| **SU-W2B-ZPM-02** | PER-0014 not named in EV-W1B-CC-01 | Medium *(identity corroboration)* | E0 attestation sufficient; optional future CC supplement |
| **SU-W2B-ZPM-03** | PER-0014 role titles (зам./исп./тех. директор) — operator signals only | Low | Not employment attestation |
| **SU-W2B-ZPM-04** | GENERAL_DIRECTOR taxonomy explicit type | Low | W2B-ZPM-TAX-01 role qualifier sufficient |
| **SU-W2B-ZPM-05** | ORG-0005 CLIENT_OF ORG-0001 | Medium *(commercial graph)* | Wave 6 |
| **SU-W2B-ZPM-06** | ORG-0005 ↔ ORG-0006 commercial relationship | Medium | COR-W1B-06; Wave 6 |
| **SU-W2B-ZPM-07** | EDO participant id (ME-W1B-05 carry-forward) | Low | CC update |
| **SU-W2B-ZPM-08** | Production domain registrant ORG-0005 | Low | Wave 5 |

**Blocking gaps remaining:** **None**

---

## 8. Wave 3 ZPM readiness assessment

### 8.1 Criteria

| Criterion | Status |
|-----------|--------|
| ORG-0005 Organization **active** | **Pass** — AT-W1B-01 |
| LE-0004 legal entity **active** | **Pass** — AT-W1B-01 |
| Wave 2 ZPM Persons **active** (PER-0014, PER-0015) | **Pass** — AT-W2-ZPM-01..02 |
| Wave 2B ZPM Person→Org edges | **Pass** — 2/2 attested |
| No false OWNER / EMPLOYEE / Diadoc edges | **Pass** |
| No Person↔Person attested | **Pass** |
| Primary operational contact bound | **Pass** — PER-0014 via REL-ZPM-02 |
| Director / signatory bound | **Pass** — PER-0015 via REL-ZPM-01 |
| Project edges deferred correctly | **Pass** |

### 8.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Structural graph insufficient for ZPM Project population |
| **PARTIALLY READY** | Wave 3 ZPM may start for subset only |
| **READY FOR WAVE 3 ZPM PROJECT POPULATION** | Org + Person + Person→Org anchor complete for ZPM |

### 8.3 Verdict

```text
READY FOR WAVE 3 ZPM PROJECT POPULATION
```

**Conditions:**

1. Wave 3 ZPM executes as **separate population pass** — Project entities and Project-family relationships not bundled into 2B-ZPM.
2. Diadoc signer remains **SAFE UNKNOWN** — no inferred relationship.
3. CLIENT_OF and commercial org↔org edges remain **Wave 6**.
4. W2B-ZPM-TAX-01 (GENERAL_DIRECTOR) does not block Project intake.

---

## 9. Attestation verdict

```text
WAVE 2B ZPM RELATIONSHIP ATTESTATION — COMPLETE
2 / 2 Person → Organization relationships attested active
0 relationships deferred from approved 2B-ZPM list
Wave 3 ZPM Project population — READY TO START
```

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 2B ZPM RELATIONSHIP POPULATION** | [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) §11 | **Superseded** — REL-ZPM-01, REL-ZPM-02 now **active** |

---

## 10. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
        │
        ├── Wave 2 Person (PER-0001..0013) ──► AT-W2-01..05 (COMPLETE)
        │
        ├── Wave 2 ZPM Person (PER-0014, PER-0015) ──► AT-W2-ZPM-01..02 (COMPLETE)
        │
        └── Wave 2B ZPM Relationship (REL-ZPM-01..02) ──► AT-W2B-ZPM-01..02 (THIS ACT)
                    │
                    └──► Wave 3 ZPM Project Population (NEXT)
```

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2-ZPM-PERSON-ACTIVE-ATTESTATION-v1.md) | Person attestation prerequisite |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | Organization attestation prerequisite |
| [ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-RELATIONSHIP-ATTESTATION-v1.md) | Prior core 2B attestation (ORG-0001..0004) |

---

*ATLAS Wave 2B ZPM Relationship Attestation v1 — documentation only.*
