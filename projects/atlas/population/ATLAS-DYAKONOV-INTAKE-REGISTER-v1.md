# ATLAS Dyakonov Contractor Intake Register v1

**Status:** **documented** — Contractor intake register (pre-population).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Intake slug:** `dyakonov`  
**Parent:** [ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md](ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** canonical Organization registry, Person registry, attested export, `ORG-*` / `LE-*` / `PER-*` / `PRJ-*` / `REL-*` assignment.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Contractor Organization intake candidates | **1** |
| Legal Entity intake candidates *(ИП)* | **1** |
| Person intake candidates *(reference)* | **1** |
| Website asset candidates | **0** |
| Domain asset candidates | **0** |
| Relationships created | **0** |
| Projects created | **0** |
| `ORG-*` assigned | **0** |
| `LE-*` assigned | **0** |
| `PER-*` assigned | **0** |
| Counterparty Card files | **0** |
| Evidence tier (intake) | **E0** |

---

## 2. Contractor Organization intake candidates

| intake_label | org_slug | proposed_display_name | wave_tier *(target)* | business_role *(target)* | legal_entity | org_id | evidence_tier | evidence_ref | lifecycle | intake_verdict |
|--------------|----------|----------------------|----------------------|--------------------------|--------------|--------|---------------|--------------|-----------|----------------|
| DYAKONOV-INTAKE-CAND-O01 | dyakonov | **ИП Дьяконов** | W1-B *(proposed)* | CONTRACTOR | DYAKONOV-INTAKE-CAND-LE01 *(proposed)* | **none** | **E0** | EV-DYAK-OP-01; EV-DYAK-OP-02 | **intake** | **Hold — CC required** |

**CC requirement:**

| Field | Value |
|-------|-------|
| Required path | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\` |
| Filesystem state (2026-06-07) | **Absent** |
| CPV status | Inventory complete — **0** non-placeholder files |

---

## 3. Legal Entity intake candidates *(not minted)*

| intake_label | proposed_legal_form | proposed_legal_name | INN | ОГРНИП | le_id | org_binding | evidence_ref | intake_verdict |
|--------------|--------------------|--------------------|-----|--------|-------|-------------|--------------|----------------|
| DYAKONOV-INTAKE-CAND-LE01 | **ИП** *(E0 signal)* | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **none** | DYAKONOV-INTAKE-CAND-O01 | EV-DYAK-OP-01 | **Hold** — CC required |

**Explicit:** Do **not** mint `LE-*` at intake.

---

## 4. Person intake candidates *(reference — not minted)*

| intake_label | proposed_name | role_signal | contacts | person_id | evidence_ref | intake_verdict |
|--------------|---------------|-------------|----------|-----------|--------------|----------------|
| DYAKONOV-INTAKE-CAND-P01 | **Дьяконов** *(surname signal only)* | ИП owner / contractor developer | **SAFE UNKNOWN** | **none** | EV-DYAK-OP-01 | **Hold** — full name unknown |

---

## 5. Population path register

| Decision | Value | rationale_ref |
|----------|-------|---------------|
| **Primary path** | **Organization + Legal Entity** | Analysis §4.1 — ИП precedent (LE-0001, LE-0002) |
| **Secondary path** | **Person** (after CC) | CONTRACTOR → ORG-0001; OWNER → own ИП org |
| **Rejected: Org only** | Insufficient | ИП requires LE binding |
| **Rejected: Person only** | Insufficient | Operator label is ИП business subject |

---

## 6. Classification register

| Field | Value | evidence_ref |
|-------|-------|--------------|
| **Primary classification** | **Contractor** | EV-DYAK-OP-02 |
| **business_role (target)** | CONTRACTOR | EV-DYAK-OP-01; EV-DYAK-OP-02 |
| **relationship_type (target)** | CONTRACTOR (Person → ORG-0001) | EV-DYAK-OP-02 |
| **Secondary (deferred)** | VENDOR_OF (contractor ORG → ORG-0001) | Wave 6+ — CC + commercial review |
| **Rejected: Subcontractor** | No intermediary chain evidence | Analysis §4.5 |
| **Rejected: Representative** | No representation authority evidence | Analysis §4.5 |
| **Open: EMPLOYEE vs CONTRACTOR** | E0 favours CONTRACTOR; CC may refine | SU-DYAK-11 |

---

## 7. Operational context register *(informational — no edges)*

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Organization anchor | ORG-0001 Веб-студия «Полигон» | EV-DYAK-OP-01 |
| Business role | Polygon contractor | EV-DYAK-OP-02 |
| Operational role | Programmer / developer | EV-DYAK-OP-01 |
| Evidence source | Operator-direct statement | EV-DYAK-OP-01 |

**No REL-* created.** CONTRACTOR / VENDOR_OF / PARTICIPATES deferred to future waves.

---

## 8. Candidate relationship families *(not created)*

| family | subject → object | type_code *(target)* | wave *(target)* | status |
|--------|------------------|----------------------|-----------------|--------|
| Person ↔ Organization | Person → ORG-0001 | **CONTRACTOR** | Wave 2B-class | **Deferred** |
| Person ↔ Organization | Person → own ИП ORG | **OWNER** / **REPRESENTATIVE** | Wave 2B-class | **Deferred** |
| Organization ↔ Organization | Contractor ORG → ORG-0001 | **VENDOR_OF** | Wave 6+ | **Deferred** |
| Person ↔ Project | Person → PRJ-* | **PARTICIPATES** | Wave 3+ | **Deferred** — scope unknown |

---

## 9. Minimum evidence register

| id | item | tier | blocks_population | status |
|----|------|------|-------------------|--------|
| E-MIN-01 | Counterparty Card | E1+ | **Yes** | **Missing** |
| E-MIN-02 | Legal form verification | E1+ | **Yes** | **SAFE UNKNOWN** |
| E-MIN-03 | Natural person full name | E1 | **Yes** | **SAFE UNKNOWN** |
| E-MIN-04 | Duplicate review (INN/ОГРНИП) | E1+ | **Yes** | **Open** |
| E-MIN-05 | Operator contractor confirmation | E0 | No | **Present** |
| E-MIN-06 | Contract / engagement letter | E1–E2 | No | **Missing** |
| E-MIN-07 | Contact channels | E1 | No | **SAFE UNKNOWN** |
| E-MIN-08 | Project participation | E1 | No | **SAFE UNKNOWN** |

---

## 10. Evidence index

| Ref | Artifact | Tier |
|-----|----------|------|
| EV-DYAK-OP-01 | Steward intake inputs (2026-06-07) | **E0** |
| EV-DYAK-OP-02 | Operator-direct statement — Polygon contractor | **E0** |
| *(pending)* | Counterparty Card — `…\dyakonov\` | **E1+ expected** |

---

## 11. Duplicate review index

| review_id | verdict | register impact |
|-----------|---------|-----------------|
| DYAK-D-01..06 | **Distinct** vs ORG-0001..0006 | No merge |
| DYAK-D-07..08 | **Distinct** vs LE-0001..0002 | No merge |
| DYAK-D-09..10 | **Distinct** vs PER-0001..0013 *(preliminary)* | No merge |
| INN/ОГРНИП cross-check | **Open** — CC absent | Blocks **Pass** |

**Duplicate review summary:** **Open** on legal identity; preliminary distinctness **Pass**.

**Integrity checks:** ORG-0001 anchor intact **Pass** · ZPM **Pass** · SIBCAR **Pass** · No merge **Pass**

---

## 12. SAFE UNKNOWN index

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-DYAK-01 | Legal form verification | **Yes** |
| SU-DYAK-02 | INN | **Yes** |
| SU-DYAK-03 | ОГРНИП | **Yes** |
| SU-DYAK-04 | Legal vs trade name | **Yes** |
| SU-DYAK-05 | Natural person full name | **Yes** |
| SU-DYAK-06 | Contacts | **No** |
| SU-DYAK-07 | Websites | **No** |
| SU-DYAK-08 | Domains | **No** |
| SU-DYAK-09 | Project participation | **No** |
| SU-DYAK-10 | Contractual scope | **No** |
| SU-DYAK-11 | EMPLOYEE vs CONTRACTOR final lock | **No** |
| SU-DYAK-12 | Subcontract intermediary chain | **No** |

---

## 13. Validation summary

| Check | Result |
|-------|--------|
| No entities created | **Pass** |
| No relationships created | **Pass** |
| No graph changes | **Pass** |
| No lifecycle changes | **Pass** |
| Intake register complete | **Pass** |
| EFV / CPV applied | **Pass** |
| CC folder inventory | **Pass** — documented absent |
| Population | **Deferred** |
| **Overall** | **READY FOR EVIDENCE COLLECTION** |

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md](ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md) | Full analysis |
| [ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md](ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md) | Summary |

---

*ATLAS Dyakonov Contractor Intake Register v1 — pre-population intake only.*
