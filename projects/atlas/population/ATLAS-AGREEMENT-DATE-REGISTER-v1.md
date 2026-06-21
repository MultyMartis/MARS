# ATLAS Agreement Date Register v1

**Status:** **attested** — canonical Agreement date fact roster after Wave E2-AGR-DATES-01 attestation act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** E2-AGR-DATES-01 — Agreement Date Extract Pass  
**Parent:** [ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-DATE-EXTRACT-PLAN-v1.md](ATLAS-AGREEMENT-DATE-EXTRACT-PLAN-v1.md) · [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md)  
**Is not:** contract archive, legal repository, runtime export.

---

## 1. Purpose

Канонический **реестр attested date facts** для Agreement records AGR-0001..AGR-0008. Одна строка — один Agreement. **Facts only — no contract text.**

**Register summary:**

| Metric | Count |
|--------|-------|
| Total date rows | **8** |
| start_date attested | **0** |
| end_date attested | **0** |
| Both dates attested (ATTESTED) | **0** |
| One date attested (PARTIAL) | **0** |
| Both SAFE UNKNOWN | **8** |

---

## 2. Attested date roster — full table

| agreement_id | start_date | end_date | evidence_source | confidence | status | notes |
|--------------|------------|----------|-----------------|------------|--------|-------|
| AGR-0001 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-0005; AT-E2-01 | — | **SAFE_UNKNOWN** | EXPIRED parent; no E2 extract |
| AGR-0002 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-0005; AT-E2-02 | — | **SAFE_UNKNOWN** | Active PRJ-0005; no E2 extract |
| AGR-0003 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-0005; AT-E2-03 | — | **SAFE_UNKNOWN** | SEO_RETAINER; no E2 extract |
| AGR-0004 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-0005; AT-E2-04 | — | **SAFE_UNKNOWN** | Active PRJ-0007; no E2 extract |
| AGR-0005 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-0005; OPS-WF02; AT-E2-05 | — | **SAFE_UNKNOWN** | WF-02 pilot confirms gap |
| AGR-0006 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-W1B-CC-01; AT-E2-06 | — | **SAFE_UNKNOWN** | Requisites only; SU-W6B-03 |
| AGR-0007 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-W1B-CC-01; AT-E2-07 | — | **SAFE_UNKNOWN** | SU-ZPM-PRJ-01 narrative rejected |
| AGR-0008 | **SAFE UNKNOWN** | **SAFE UNKNOWN** | AGL-01; EV-W1C-CC-01; AT-E2-08 | — | **SAFE_UNKNOWN** | ME-W3-SIBCAR-01; no SOW dates |

---

## 3. Status vocabulary

| status | Meaning |
|--------|---------|
| **ATTESTED** | Both start_date and end_date attested as ISO dates |
| **PARTIAL** | Exactly one of start_date or end_date attested |
| **SAFE_UNKNOWN** | Insufficient evidence for one or both dates |

---

## 4. Confidence vocabulary

| confidence | When used |
|------------|-----------|
| **HIGH** | E2+ extract pointer with explicit ISO dates steward-attested |
| **MEDIUM** | E1 document with unambiguous date fields steward-attested |
| **LOW** | Single indirect reference — not used in E2-AGR-DATES-01 |
| **—** | No date attested — confidence not applicable |

---

## 5. Attested roster — by status

### 5.1 ATTESTED — 0 rows

*(none)*

### 5.2 PARTIAL — 0 rows

*(none)*

### 5.3 SAFE_UNKNOWN — 8 rows

| agreement_id | parent status | blocker |
|--------------|---------------|---------|
| AGR-0001 | EXPIRED | No E2 contract date extract |
| AGR-0002 | ACTIVE | No E2 contract date extract |
| AGR-0003 | ACTIVE | No E2 contract date extract |
| AGR-0004 | ACTIVE | No E2 contract date extract |
| AGR-0005 | ACTIVE | No E2 contract date extract |
| AGR-0006 | ACTIVE | No E2 contract date extract |
| AGR-0007 | EXPIRED | No E2 extract; narrative rejected |
| AGR-0008 | ACTIVE | No E2 contract date extract |

---

## 6. Coverage metrics

| Metric | Value |
|--------|-------|
| Date field coverage (16 fields: 8 × 2) | **0/16 attested (0%)** |
| Agreement full-date coverage (both dates) | **0/8 (0%)** |
| ACTIVE agreement full-date coverage | **0/6 (0%)** |
| Remaining SAFE UNKNOWN (date fields) | **16/16 (100%)** |
| Remaining SAFE UNKNOWN (agreements — at least one unknown) | **8/8 (100%)** |

---

## 7. Evidence index

| Ref | Artifact | Date rows supported |
|-----|----------|---------------------|
| AT-E2-01..08 | [ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md) | All register rows — negative attestation |
| AT-AGL-01..08 | [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Parent agreement basis |
| EV-0005 | `triumph/…2024.xlsx` | Reviewed — no contract period |
| EV-W1B-CC-01 | `bzpm\Реквизиты.docx` | Reviewed — requisites only |
| EV-W1C-CC-01 | `sibcar\Реквизиты.docx` | Reviewed — requisites only |
| OPS-WF02-LIVE-PILOT | WF-02 pilot AGR-0005 | Gap corroboration |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) | Parent metadata overlay — dates unchanged |
| [ATLAS-AGREEMENT-DATE-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ACTIVE-ATTESTATION-v1.md) | ACTIVE date visibility act |
| [REPORT-atlas-agreement-date-extract-v1.md](../reports/REPORT-atlas-agreement-date-extract-v1.md) | Wave pass record |

---

*ATLAS Agreement Date Register v1 — Wave E2-AGR-DATES-01. Date facts only.*
