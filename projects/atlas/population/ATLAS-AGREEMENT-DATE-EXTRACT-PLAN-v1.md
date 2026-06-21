# ATLAS Agreement Date Extract Plan v1

**Status:** **documented** — Wave E2-AGR-DATES-01 evidence evaluation (no runtime).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** E2-AGR-DATES-01 — Agreement Date Extract Pass  
**Parent:** [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-REALITY-MODEL-v1.md) · [ATLAS-AGREEMENT-METADATA-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-METADATA-MODEL-v1.md) · [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) · [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md)  
**Is not:** contract storage, OCR job, legal repository, accounting layer, runtime export.

---

## 1. Purpose

Review **existing attested evidence** for **AGR-0001..AGR-0008** and determine whether `start_date` and `end_date` can be **attested** as ISO date facts.

**Normative rule:** No guessing. No estimation. No inference from project lifecycle, CC intake dates, or operator narrative. E2+ contract date extract reference required per [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) §2.2.

---

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| 8 attested Agreement rows (AGL-01) | ORG-0007 Makita — no Agreement rows |
| Existing EV-* / LE-* / CC / attestation refs | New evidence creation or external fetch |
| Date fact extraction only | renewal_posture, document_expectation, counterparty_profile changes |
| Metadata register date field review | Agreement register status changes |
| OPS impact analysis (WF-01..03) | Runtime, API, registry file mutation |

---

## 3. Evidence sources reviewed

| Ref | Artifact | Date-relevant content | Verdict |
|-----|----------|----------------------|---------|
| AGL-01 register | [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | All rows: start/end **SAFE UNKNOWN** | No ISO dates |
| AGM-01 register | [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) | 0/8 date fields attested | No ISO dates |
| AGL-01 attestation | [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | E2+ **not used** in AGL-01 | No date extract |
| AGM-01 attestation | [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) | start/end require E2+ extract | No date extract |
| EV-0005 | `triumph/…2024.xlsx` (Triumph CC) | Counterparty contacts, org context — **not** contract period | **Insufficient** |
| EV-0003 | `polygon/ИП Русецкий А. А.pdf` | Vendor LE context | **Insufficient** |
| EV-W1B-CC-01 | `bzpm\Реквизиты.docx` | Requisites only | **Insufficient** |
| EV-W1C-CC-01 | `sibcar\Реквизиты.docx` | Requisites only | **Insufficient** |
| Dataset v0.4 | `ATLAS-WAVE1-DATASET-v0.4.xlsx` | Projects / Relationships — no Agreement date columns attested | **Insufficient** |
| Wave 3 project registers | PRJ-0004..0011 | Lifecycle active/deprecated — **not** agreement period (AGR-ST-01) | **Insufficient** |
| Wave 6A / 6B commercial | REL-0016, REL-0040, REL-0041 | SU-W6A-03 / SU-W6B-03: E2 contract extract existence **UNKNOWN** | **Insufficient** |
| SU-ZPM-PRJ-01 | PRJ-0010 historical dates | Operator «~5 years» narrative — **not ISO-attested** | **Rejected** |
| ME-W3-SIBCAR-01 | PRJ-0011 | No contract-dated SOW | **Insufficient** |
| OPS WF-02 pilot | [REPORT-ops-wf02-live-pilot-v1.md](../../ops/reports/REPORT-ops-wf02-live-pilot-v1.md) | Confirms dates SAFE UNKNOWN on all AGR-* | Corroboration only |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 4. Field-level attestability matrix

| Field | AGR-0001..0005 (Triumph) | AGR-0006..0007 (ZPM) | AGR-0008 (SIBCAR) |
|-------|--------------------------|----------------------|-------------------|
| start_date | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** |
| end_date | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** |

**Cross-cutting blockers:**

| Blocker | Affected rows |
|---------|---------------|
| No E2 contract date extract attested in ATLAS | All 8 |
| CC artifacts contain requisites/contacts only | AGR-0001..0008 |
| Project lifecycle ≠ agreement period (AGR-ST-01) | AGR-0001, AGR-0007 (EXPIRED status without dates) |
| Operator narrative rejected for ISO conversion | AGR-0007 (SU-ZPM-PRJ-01) |

---

## 5. Per-agreement evaluation

### 5.1 AGR-0001 — Triumph / Редизайн (EXPIRED)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract; EV-0005 CC has no contract period |
| end_date | **SAFE UNKNOWN** | PRJ-0004 deprecated does not attest end_date (AGR-ST-01) |

### 5.2 AGR-0002 — Triumph / Грузотакси (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract |
| end_date | **SAFE UNKNOWN** | Active ongoing delivery — no bounded term attested |

### 5.3 AGR-0003 — Triumph / SEO (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract; retainer type does not substitute date |
| end_date | **SAFE UNKNOWN** | SEO_RETAINER ongoing — no term extract |

### 5.4 AGR-0004 — Triumph / Блог (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract |
| end_date | **SAFE UNKNOWN** | Active PRJ-0007 — no term extract |

### 5.5 AGR-0005 — Triumph / Манипулятор (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract; WF-02 pilot confirms gap |
| end_date | **SAFE UNKNOWN** | WF-02 period binding blocked — no attested end |

### 5.6 AGR-0006 — ZPM / Каталог-платформа (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | EV-W1B-CC-01 requisites only; SU-W6B-03 E2 extract UNKNOWN |
| end_date | **SAFE UNKNOWN** | Active WIP — no term extract |

### 5.7 AGR-0007 — ZPM / Исходный сайт (EXPIRED)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | No E2 date extract |
| end_date | **SAFE UNKNOWN** | Operator «~5 years ago» narrative — **not ISO-attested** (SU-ZPM-PRJ-01) |

### 5.8 AGR-0008 — SIBCAR / OpenCart dealership (ACTIVE)

| Field | Verdict | Basis |
|-------|---------|-------|
| start_date | **SAFE UNKNOWN** | EV-W1C-CC-01 requisites only; ME-W3-SIBCAR-01 no contract-dated SOW |
| end_date | **SAFE UNKNOWN** | Active WIP — no term extract |

---

## 6. Population summary

| Metric | Count |
|--------|-------|
| Agreements evaluated | **8** |
| start_date attested | **0** |
| end_date attested | **0** |
| Both dates attested | **0** |
| One date attested (PARTIAL) | **0** |
| Both SAFE UNKNOWN | **8** |

---

## 7. Deferred — requires new evidence

| Item | Reason | Unblock condition |
|------|--------|-------------------|
| Agreement ISO dates (all 8 rows) | No E2 contract date extract pointer attested | Steward attests E2 extract ref (pointer only) per agreement |
| SU-W6A-03 | Triumph formal contract extract existence external | Operator or steward E2 pointer |
| SU-W6B-03 | ZPM / SIBCAR formal contract extract existence external | Operator or steward E2 pointer |
| SU-ZPM-PRJ-01 | Historical contract dates PRJ-0010 | E2 extract with ISO dates — narrative insufficient |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-AGREEMENT-DATE-REGISTER-v1.md](ATLAS-AGREEMENT-DATE-REGISTER-v1.md) | Canonical date fact roster |
| [ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md) | Formal attestation act |
| [REPORT-atlas-agreement-date-extract-v1.md](../reports/REPORT-atlas-agreement-date-extract-v1.md) | Wave pass record |

---

*ATLAS Agreement Date Extract Plan v1 — Wave E2-AGR-DATES-01. Evidence review only.*
