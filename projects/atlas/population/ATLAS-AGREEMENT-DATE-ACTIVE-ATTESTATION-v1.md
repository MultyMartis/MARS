# ATLAS Agreement Date Active Attestation v1

**Status:** **attested** — Wave E2-AGR-DATES-01 ACTIVE Agreement date visibility verification act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** E2-AGR-DATES-01 — Agreement Date Extract Pass  
**Attestor role:** Registry Steward (delegated)  
**Parent:** [ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-DATE-REGISTER-v1.md](ATLAS-AGREEMENT-DATE-REGISTER-v1.md) · [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md)  
**Is not:** renewal schedule, legal validity confirmation, contract storage.

---

## 1. Purpose

For each **ACTIVE** Agreement in AGL-01 register, classify **date visibility** only:

| Class | Meaning |
|-------|---------|
| **GOOD** | start_date present **and** end_date present (both ISO-attested) |
| **PARTIAL** | Exactly one of start_date or end_date attested |
| **WEAK** | Both dates SAFE UNKNOWN |

**Normative question answered:**

> Which ACTIVE agreements have operationally visible agreement periods for OPS consumption?

Classification is **date-only** — does not re-evaluate AGM-01 metadata completeness (GOOD/PARTIAL there).

---

## 2. Classification criteria

| Field | GOOD | PARTIAL | WEAK |
|-------|------|---------|------|
| start_date | ISO attested | — | SAFE UNKNOWN |
| end_date | ISO attested | — | SAFE UNKNOWN |
| Combined | Both attested | One attested | Both unknown |

**Note:** OPEN-ended agreements with attested start_date only would classify **PARTIAL** — none attested in E2-AGR-DATES-01.

---

## 3. ACTIVE date visibility roster

| agreement_id | client_org | start_date | end_date | date visibility | notes |
|--------------|------------|------------|----------|-----------------|-------|
| AGR-0002 | ORG-0004 Триумф | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | EV-0005 reviewed — no period |
| AGR-0003 | ORG-0004 Триумф | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | SEO retainer — no term dates |
| AGR-0004 | ORG-0004 Триумф | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | Active PRJ-0007 |
| AGR-0005 | ORG-0004 Триумф | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | WF-02 period binding blocked |
| AGR-0006 | ORG-0005 ЗПМ | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | CC requisites only |
| AGR-0008 | ORG-0006 SIBCAR | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | No contract-dated SOW |

---

## 4. EXPIRED agreements — date visibility (reference)

| agreement_id | start_date | end_date | date visibility | notes |
|--------------|------------|----------|-----------------|-------|
| AGR-0001 | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | Historical — dates not inferred from EXPIRED |
| AGR-0007 | SAFE UNKNOWN | SAFE UNKNOWN | **WEAK** | SU-ZPM-PRJ-01 narrative rejected |

---

## 5. Summary counts

### 5.1 ACTIVE subset (6 rows)

| Class | Count | agreement_ids |
|-------|-------|---------------|
| **GOOD** | **0** | — |
| **PARTIAL** | **0** | — |
| **WEAK** | **6** | AGR-0002, AGR-0003, AGR-0004, AGR-0005, AGR-0006, AGR-0008 |

### 5.2 All agreements (8 rows)

| Class | Count |
|-------|-------|
| **GOOD** | **0** |
| **PARTIAL** | **0** |
| **WEAK** | **8** |

---

## 6. OPS date visibility questions

| Question | Answer | Visibility |
|----------|--------|------------|
| Which ACTIVE agreements have attested start? | **None** | **WEAK** |
| Which ACTIVE agreements have attested end? | **None** | **WEAK** |
| Can WF-02 derive document period from Agreement? | **No** — all dates UNKNOWN | **Blocked** |
| Can WF-03 schedule renewal follow-up from end_date? | **No** | **Blocked** |
| Triumph contour (4 ACTIVE) date visibility? | All **WEAK** | Uniform gap |
| ZPM / SIBCAR ACTIVE date visibility? | **WEAK** each | E0 + no E2 extract |

---

## 7. Validation checklist

| Check | Result |
|-------|--------|
| All 6 ACTIVE rows classified | **Pass** |
| Classification based on date fields only | **Pass** |
| No dates invented to upgrade class | **Pass** |
| EXPIRED rows documented separately | **Pass** |

---

## 8. Verdict

```text
ACTIVE DATE VISIBILITY: WEAK — 0/6 GOOD — 6/6 WEAK
```

**Unblock path:** E2 contract date extract pointer attestation per agreement → re-run E2-AGR-DATES-01 classification.

---

*ATLAS Agreement Date Active Attestation v1 — Wave E2-AGR-DATES-01.*
