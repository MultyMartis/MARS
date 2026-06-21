# ATLAS Wave 2C SIBCAR Relationship Attestation v1

**Status:** **attested** — official Person → Organization relationship attestation set for Wave 2C SIBCAR tranche (ORG-0006).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md) · [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 3+ execution, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Attestation: **COMPLETE**
- Wave 1C SIBCAR Attestation (ORG-0006): **COMPLETE** — AT-W1C-01
- Wave 2 core Person attestation: **COMPLETE**
- Wave 2 ZPM Person attestation: **COMPLETE**
- Wave 2C SIBCAR Person attestation (PER-0016, PER-0017): **COMPLETE** — AT-W2C-SIBCAR-01..02
- Population verdict: **READY FOR WAVE 2C SIBCAR RELATIONSHIP POPULATION**

---

# REPORT — ATLAS Wave 2C SIBCAR Relationship Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W2C-SIBCAR-REL-01** + **AT-W2C-SIBCAR-REL-02**  
**Promotion:** REL-SIBCAR-01, REL-SIBCAR-02 — queued → **active**

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** набора **Person → Organization** relationships Wave 2C tranche **SIBCAR**: **2** записи переведены в **active** canonical state; ORG-0006 `primary_contact_person_id` установлен.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Person → Organization → **active** (ORG-0006) | Person ↔ Person |
| Evidence tier per relationship | New Person / Organization entities |
| Type assignment per approved 2C-SIBCAR list | Organization ↔ Organization commercial |
| ORG-0006 primary contact pointer = PER-0017 | Project / Website / Domain edges |
| SIBCAR Person layer completion statement | Runtime / API / database |
| OWNER / EMPLOYEE / Diadoc signer exclusions | Foundation amendment |

**Binding operator decisions (enforced):**

- REL-SIBCAR-01 — **GENERAL_DIRECTOR** only.
- REL-SIBCAR-02 — **REPRESENTATIVE** only; **no** EMPLOYEE edge.
- ORG-0006 `primary_contact_person_id` = **PER-0017**.
- «Business Owner» — **no** OWNER edge.
- Diadoc signer — **SAFE UNKNOWN**; no relationship minted.

---

## 2. Attestation tranches executed

| Tranche | Relationships | Basis | Outcome |
|---------|---------------|-------|---------|
| **AT-W2C-SIBCAR-REL-01** | REL-SIBCAR-01 | E1 EV-W1C-CC-01 §21–§24; LE-0005 signatory; PER-0016 + ORG-0006 **active** | **active** |
| **AT-W2C-SIBCAR-REL-02** | REL-SIBCAR-02 | E0 EV-W2C-SIBCAR-OP-01; PER-0017 + ORG-0006 **active**; primary operational contact | **active** |

---

## 3. Per-relationship attestation records

### 3.1 REL-SIBCAR-01 — PER-0016 → ORG-0006

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-01 |
| **source_person** | PER-0016 Карандашов Максим Петрович |
| **target_organization** | ORG-0006 SIBCAR |
| **relationship_type** | **GENERAL_DIRECTOR** |
| **attestation_basis** | PER-0016 **active** (AT-W2C-SIBCAR-01); ORG-0006 **active** (AT-W1C-01); E1 EV-W1C-CC-01 §21–§24 — «Руководитель Карандашов Максим Петрович»; LE-0005 `document_signatory` identical string; chief accountant same subject §23–§24; duplicate review W2C-SIBCAR-D-03 **Pass** |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Director / document signatory / chief accountant. Exact director title **SAFE UNKNOWN**. |

**REL-SIBCAR-01 taxonomy alignment (W2C-SIBCAR-TAX-01):** Operator label **GENERAL_DIRECTOR**; canonical taxonomy family **REPRESENTATIVE** (Person → Organization) with `role_qualifier: general_director` per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1 and RR-02 — consistent with REL-ZPM-01 / REL-0015 Triumph precedent.

### 3.2 REL-SIBCAR-02 — PER-0017 → ORG-0006

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SIBCAR-02 |
| **source_person** | PER-0017 Хаял |
| **target_organization** | ORG-0006 SIBCAR |
| **relationship_type** | **REPRESENTATIVE** |
| **attestation_basis** | PER-0017 **active** (AT-W2C-SIBCAR-02); ORG-0006 **active**; E0 EV-W2C-SIBCAR-OP-01 — operator-direct identity, Telegram @Khayal8888, primary operational contact; CC silent on Хаял (EFV-06) |
| **evidence_tier** | **E0** |
| **lifecycle_state** | **active** |
| **notes** | Main communication channel between Polygon and SIBCAR via Telegram. Not document signatory. «Business Owner» — role signal only. Diadoc signer **SAFE UNKNOWN**. EMPLOYEE type **not** selected per operator scope. |

---

## 4. Organization pointer update

| Field | Prior | Attested |
|-------|-------|----------|
| ORG-0006 `primary_contact_person_id` | **SAFE UNKNOWN** | **PER-0017** |
| Basis | — | REL-SIBCAR-02 primary operational contact; steward confirmed at 2C attestation |

**Org register sync note:** Cross-reference recommended in [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) at next documentation sync pass (analog ZPM-C-01 remediation for ORG-0005).

---

## 5. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PER-0017 → ORG-0006 **OWNER** | **Excluded** — «Business Owner» operator signal only |
| PER-0017 → ORG-0006 **EMPLOYEE** | **Excluded** — operator approved REPRESENTATIVE |
| Diadoc / EDO signer relationship | **Excluded** — **SAFE UNKNOWN** |
| Person ↔ Person edges | **Rejected** |
| Person ↔ Project edges | **Rejected** — PRJ-0011 attested without Person edges |
| REL-0041 CLIENT_OF ORG-0006 → ORG-0001 | **Already attested** — Wave 6B; not re-minted |
| ORG-0006 ↔ ORG-0005 commercial edges | **Deferred** |
| New entities | **Not created** |
| Foundation documents | **Not modified** |
| Project / Website / Domain entities | **Not modified** |

---

## 6. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | 2 directed Person→Org edges to ORG-0006 — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) | REPRESENTATIVE in baseline — **Pass**; GENERAL_DIRECTOR via W2C-SIBCAR-TAX-01 — **Pass with note** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Both edges **active** post attestation — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) | Endpoints PER-0016/0017 / ORG-0006 attested active — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship state `active` — **Pass** |
| [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md) | Steward path; no draft substitution — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation act per relationship batch — **Pass** |
| EFV-01 / EFV-06 / CPV-01 | CC read before PER-0016 conclusions; CC silence honored for PER-0017 — **Pass** |

**Foundation modified:** **No**  
**Wave 1 / Wave 2 / Wave 2 ZPM / Waves 3–5 SIBCAR modified:** **No**  
**New entity types:** **No**  
**New relationship families:** **No** (Person → Organization only)

---

## 7. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W2C-SIBCAR-01** | Diadoc / EDO specific signer (ORG-0006) | Medium *(signatory ops)* | Does not block downstream — no edge minted |
| **SU-W2C-SIBCAR-02** | PER-0017 not named in EV-W1C-CC-01 | Medium *(identity corroboration)* | E0 attestation sufficient; optional future CC supplement |
| **SU-W2C-SIBCAR-03** | PER-0017 full patronymic **SAFE UNKNOWN** | Medium | Given name + Telegram sufficient at E0 |
| **SU-W2C-SIBCAR-04** | GENERAL_DIRECTOR taxonomy explicit type | Low | W2C-SIBCAR-TAX-01 role qualifier sufficient |
| **SU-W2C-SIBCAR-05** | PER-0016 exact director title | Low | CC «Руководитель» label |
| **SU-W2C-SIBCAR-06** | PER-0016 / PER-0017 phone / email contacts | Low | Optional operator supplement |
| **SU-W2C-SIBCAR-07** | EDO participant id (ME-W1C-03 carry-forward) | Low | CC update |
| **SU-W2C-SIBCAR-08** | Org register `primary_contact_person_id` cross-ref | Low | Documentation sync — analog ZPM-C-01 |

**Blocking gaps remaining:** **None**

---

## 8. SIBCAR Person layer completion assessment

### 8.1 Criteria

| Criterion | Status |
|-----------|--------|
| ORG-0006 Organization **active** | **Pass** — AT-W1C-01 |
| LE-0005 legal entity **active** | **Pass** — AT-W1C-01 |
| Wave 2C SIBCAR Persons **active** (PER-0016, PER-0017) | **Pass** — AT-W2C-SIBCAR-01..02 |
| Wave 2C SIBCAR Person→Org edges | **Pass** — 2/2 attested |
| No false OWNER / EMPLOYEE / Diadoc edges | **Pass** |
| No Person↔Person attested | **Pass** |
| Primary operational contact bound | **Pass** — PER-0017 via REL-SIBCAR-02 |
| Director / signatory bound | **Pass** — PER-0016 via REL-SIBCAR-01 |
| `primary_contact_person_id` set | **Pass** — PER-0017 |
| Commercial REL-0041 unchanged | **Pass** — not re-minted |

### 8.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | SIBCAR Person layer incomplete |
| **PARTIALLY READY** | Person layer complete for subset only |
| **WAVE 2C SIBCAR PERSON LAYER — COMPLETE** | Org + Person + Person→Org anchor complete for SIBCAR |

### 8.3 Verdict

```text
WAVE 2C SIBCAR PERSON LAYER — COMPLETE
```

**Conditions:**

1. Downstream Waves 3–5 SIBCAR (Project, Website, Domain) already attested — **no retroactive Person↔Project edges required**.
2. Diadoc signer remains **SAFE UNKNOWN** — no inferred relationship.
3. CLIENT_OF REL-0041 remains **unchanged** — Wave 6B authority.
4. W2C-SIBCAR-TAX-01 (GENERAL_DIRECTOR) does not block operational use.

---

## 9. Attestation verdict

```text
WAVE 2C SIBCAR RELATIONSHIP ATTESTATION — COMPLETE
2 / 2 Person → Organization relationships attested active
ORG-0006.primary_contact_person_id = PER-0017
0 relationships deferred from approved 2C-SIBCAR list
SIBCAR Person layer — COMPLETE
```

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 2C SIBCAR RELATIONSHIP POPULATION** | [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) §11 | **Superseded** — REL-SIBCAR-01, REL-SIBCAR-02 now **active** |

**Discovery register findings resolved:**

| Finding | Prior | Disposition |
|---------|-------|-------------|
| SIBCAR-W2D-01 | Zero attested Person entities | **Resolved** — PER-0016, PER-0017 **active** |
| SIBCAR-W2D-02 | Zero Person→Org edges | **Resolved** — REL-SIBCAR-01, REL-SIBCAR-02 **active** |
| SIBCAR-W2D-03 | primary_contact_person_id unset | **Resolved** — PER-0017 |
| SIBCAR-W2D-04 | No operator mission pack | **Resolved** — EV-W2C-SIBCAR-OP-01 |
| SIBCAR-W2D-08 | Wave 2C doc pack not authored | **Resolved** — 7 files complete |

---

## 10. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1C SIBCAR (ORG-0006, LE-0005) ──► AT-W1C-01 (COMPLETE)
        │
        ├── Waves 3–5 SIBCAR (PRJ-0011, WEB-SIBCAR-01, DOM-SIBCAR-01) ──► attested (prior)
        │
        ├── Wave 6B REL-0041 CLIENT_OF ──► attested (prior)
        │
        ├── Wave 2C SIBCAR Person (PER-0016, PER-0017) ──► AT-W2C-SIBCAR-01..02 (COMPLETE)
        │
        └── Wave 2C SIBCAR Relationship (REL-SIBCAR-01..02) ──► AT-W2C-SIBCAR-REL-01..02 (THIS ACT)
                    │
                    └──► SIBCAR Person layer COMPLETE
```

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-REGISTER-v1.md) | Attested relationship roster |
| [ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE2C-SIBCAR-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE2C-SIBCAR-PERSON-ACTIVE-ATTESTATION-v1.md) | Person attestation prerequisite |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Organization attestation prerequisite |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](../audit/ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) | Discovery authority |
| [ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) | Parity template |

---

*ATLAS Wave 2C SIBCAR Relationship Attestation v1 — documentation only.*
