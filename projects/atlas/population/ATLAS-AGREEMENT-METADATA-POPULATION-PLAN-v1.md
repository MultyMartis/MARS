# ATLAS Agreement Metadata Population Plan v1



**Status:** **documented** — Wave AGM-01 evidence evaluation (no runtime).  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-10  

**Wave:** AGM-01 — Agreement Metadata Layer  

**Parent:** [ATLAS-AGREEMENT-METADATA-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-METADATA-MODEL-v1.md) · [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) · [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-POPULATION-PLAN-v1.md)  

**Is not:** runtime export, date extraction job, contract OCR plan.



---



## 1. Purpose



Evaluate **AGR-0001..AGR-0008** for Agreement Metadata Layer population: which metadata fields can be **attested** from existing ATLAS evidence, and which remain **SAFE UNKNOWN**.



**Normative rule:** No guessing. Evidence only. No date inference.



---



## 2. Scope



| In scope | Out of scope |

|----------|--------------|

| 8 attested Agreement rows (AGL-01) | ORG-0007 Makita — no Agreement rows |

| Metadata overlay fields per AGM-01 model | Legal Entity layer changes |

| Pointer refs to LE and CC evidence | Structured requisites extraction |

| OPS consumer field mapping | Runtime, API, OPS record creation |



---



## 3. Evidence sources reviewed



| Ref | Artifact | Metadata use |

|-----|----------|--------------|

| AGL-01 register | [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | Parent status, type, evidence_level |

| AGL-01 attestation | [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Per-row attestation basis |

| ACTIVE act | [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset |

| Integrity snapshot | [ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md](../audit/ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md) | LE-0001..0005 bindings |

| Wave 6B commercial | [ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6B-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | LE client context |

| EV-0005 | Triumph commercial spreadsheet | Triumph E1 overlay |

| EV-W1B-CC-01 | ZPM counterparty card | ORG-0005 CC pointer |

| EV-W1C-CC-01 | SIBCAR counterparty card | ORG-0006 CC pointer |

| OPS WF-02 pilot | [REPORT-ops-wf02-live-pilot-v1.md](../../ops/reports/REPORT-ops-wf02-live-pilot-v1.md) | Document closing contour AGR-0005 |



---



## 4. Field-level attestability matrix



| Field | AGR-0001..0005 (Triumph) | AGR-0006..0007 (ZPM) | AGR-0008 (SIBCAR) |

|-------|--------------------------|----------------------|-------------------|

| operational_status | **Attest** — from register | **Attest** — from register | **Attest** — from register |

| start_date | **SAFE UNKNOWN** — no E2 extract | **SAFE UNKNOWN** | **SAFE UNKNOWN** |

| end_date | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** |

| renewal_posture | EXPIRED (0001) / ONGOING (0002..0005) | EXPIRED (0007) / ONGOING (0006) | ONGOING |

| counterparty_profile | LE-0003; EV-0005 | LE-0004; EV-W1B-CC-01 | LE-0005; EV-W1C-CC-01 |

| document_expectation | MONTHLY_REPORT (0003) / PROJECT_DELIVERY (others) | PROJECT_DELIVERY | PROJECT_DELIVERY |

| evidence_level | E1 — copy from register | E0 — copy from register | E0 — copy from register |



---



## 5. Per-agreement evaluation



### 5.1 AGR-0001 — Triumph / Редизайн (EXPIRED)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** EXPIRED | Register; PRJ-0004 deprecated |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** EXPIRED | EXPIRED status + deprecated project |

| counterparty_profile | **Attest** LE-0003; EV-0005 | Wave 1 + EV-0005 |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + completed delivery phase |

| evidence_level | **Attest** E1 | Register copy |



### 5.2 AGR-0002 — Triumph / Грузотакси (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** ONGOING | Active PRJ-0005; notes «ongoing delivery» |

| counterparty_profile | **Attest** LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + active delivery |

| evidence_level | **Attest** E1 | Register copy |



### 5.3 AGR-0003 — Triumph / SEO (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** ONGOING | SEO_RETAINER type + active PRJ-0006 |

| counterparty_profile | **Attest** LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | **Attest** MONTHLY_REPORT | SEO_RETAINER per AGM-DE-01 |

| evidence_level | **Attest** E1 | Register copy |



### 5.4 AGR-0004 — Triumph / Блог (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** ONGOING | Active PRJ-0007; ongoing delivery |

| counterparty_profile | **Attest** LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + active delivery |

| evidence_level | **Attest** E1 | Register copy |



### 5.5 AGR-0005 — Triumph / Манипулятор (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act; WF-02 pilot anchor |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract; WF-02 gap confirmed |

| renewal_posture | **Attest** ONGOING | Active PRJ-0008; WF-01/WF-02 contour |

| counterparty_profile | **Attest** LE-0003; EV-0005 | WF-02 pilot consumed LE-0003 |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT; WF-02 live pilot validated |

| evidence_level | **Attest** E1 | Register copy |



### 5.6 AGR-0006 — ZPM / Каталог-платформа (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** ONGOING | Active PRJ-0009; WIP delivery |

| counterparty_profile | **Attest** LE-0004; EV-W1B-CC-01 | AT-W1B-01; CC attested |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + active WIP |

| evidence_level | **Attest** E0 | Register copy — not upgraded |



### 5.7 AGR-0007 — ZPM / Исходный сайт (EXPIRED)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** EXPIRED | Register; PRJ-0010 deprecated |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract; operator «~5 years ago» is narrative not ISO date |

| renewal_posture | **Attest** EXPIRED | EXPIRED status + deprecated project |

| counterparty_profile | **Attest** LE-0004; EV-W1B-CC-01 | AT-W1B-01 |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + historical delivery |

| evidence_level | **Attest** E0 | Register copy |



### 5.8 AGR-0008 — SIBCAR / OpenCart dealership (ACTIVE)



| Field | Verdict | Basis |

|-------|---------|-------|

| operational_status | **Attest** ACTIVE | ACTIVE attestation act |

| start_date / end_date | **SAFE UNKNOWN** | No E2 date extract |

| renewal_posture | **Attest** ONGOING | Active PRJ-0011; OCPilot WIP |

| counterparty_profile | **Attest** LE-0005; EV-W1C-CC-01 | AT-W1C-01 |

| document_expectation | **Attest** PROJECT_DELIVERY | DEVELOPMENT + active WIP |

| evidence_level | **Attest** E0 | Register copy |



---



## 6. Population summary



| Metric | Count |

|--------|-------|

| Agreements evaluated | **8** |

| Metadata rows to populate | **8** |

| start_date attested | **0** |

| end_date attested | **0** |

| renewal_posture UNKNOWN | **0** |

| document_expectation UNKNOWN | **0** |

| counterparty_profile UNKNOWN | **0** |

| FIXED_TERM posture | **0** |

| MONTHLY_CLOSING expectation | **0** |

| MIXED expectation | **0** |



---



## 7. Deferred (not in AGM-01 register)



| Item | Reason |

|------|--------|

| Agreement dates (all rows) | No E2 contract date extract attested |

| MONTHLY_CLOSING on any row | No calendar closing cadence attestation |

| MIXED document class | No multi-class operator attestation |

| Makita metadata | No parent Agreement row |

| Structured requisites inline | CC pointer only — extraction deferred |

| Signing expectations | Person contact channels absent — SAFE UNKNOWN at OPS layer |



---



## 8. Related documents



| Document | Role |

|----------|------|

| [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) | Output register |

| [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) | Attestation act |

| [REPORT-atlas-agreement-metadata-layer-v1.md](../reports/REPORT-atlas-agreement-metadata-layer-v1.md) | Wave pass record |



---



*ATLAS Agreement Metadata Population Plan v1 — Wave AGM-01. Evidence-based evaluation only.*

