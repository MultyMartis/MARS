# ATLAS Agreement Metadata Attestation v1



**Status:** **attested** — Wave AGM-01 Agreement Metadata Layer attestation methodology and act.  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-10  

**Wave:** AGM-01 — Agreement Metadata Layer  

**Attestor role:** Registry Steward (delegated)  

**Parent:** [ATLAS-AGREEMENT-METADATA-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-METADATA-MODEL-v1.md) · [ATLAS-AGREEMENT-METADATA-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-METADATA-POPULATION-PLAN-v1.md) · [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md)  

**Is not:** runtime export, legal validity confirmation, date extraction act.



---



## 1. Purpose



Настоящий акт фиксирует **каноническую attestation** Wave AGM-01: **8** Agreement Metadata records переведены в attested register state — overlay on AGL-01 Agreement roster.



**Scope:**



| In attestation | Out of attestation |

|----------------|-------------------|

| Operational metadata fields per AGM-01 model | Contract text / PDF storage |

| Pointer refs to LE and CC evidence | Structured requisites extraction |

| document_expectation and renewal_posture | Legal workflows, accounting |

| Evidence-only population | Runtime, API, OPS record creation |



---



## 2. Attestation methodology



### 2.1 Preconditions



Metadata record **must** satisfy **all** rows to enter register:



| # | Requirement |

|---|-------------|

| 1 | Parent Agreement row attested in AGL-01 register |

| 2 | `operational_status` matches parent Agreement `status` |

| 3 | All required metadata fields present — **SAFE UNKNOWN** where evidence insufficient |

| 4 | No fabricated dates |

| 5 | `counterparty_profile` uses attested LE binding or **SAFE UNKNOWN** |

| 6 | `document_expectation` assigned only per AGM-DE rules |

| 7 | `renewal_posture` assigned only per AGM-RP rules |

| 8 | `evidence_level` copied from parent — not upgraded without new act |



**Absence of parent Agreement row → no metadata row.**



### 2.2 Field attestation rules



| Field | Attestation source |

|-------|-------------------|

| operational_status | Mirror AGL-01 register status |

| start_date / end_date | E2+ extract only — else **SAFE UNKNOWN** |

| renewal_posture | EXPIRED from status; ONGOING from active delivery/retainer attestation; else UNKNOWN |

| counterparty_profile | LE-* bound to client_org + optional EV-* CC ref |

| document_expectation | Type-derived per AGM-DE-01/02 only; no MONTHLY_CLOSING without explicit attestation |

| evidence_level | Copy from Agreement register |



### 2.3 Evidence tiers (unchanged from AGL-01)



| Tier | Metadata assignment |

|------|---------------------|

| **E0** | Operator + structural graph — metadata conservative |

| **E1** | CC or commercial spreadsheet — counterparty_profile includes EV ref |

| **E2+** | **Not used in AGM-01** — no date extract attested |



---



## 3. Attestation act — tranche summary



| Tranche | agreement_id | Basis | Outcome |

|---------|--------------|-------|---------|

| **AT-AGM-01** | AGR-0001 | EXPIRED parent; LE-0003; EV-0005; DEVELOPMENT historical | **Attested** |

| **AT-AGM-02** | AGR-0002 | ACTIVE parent; LE-0003; EV-0005; ongoing PRJ-0005 | **Attested** |

| **AT-AGM-03** | AGR-0003 | ACTIVE parent; SEO_RETAINER; LE-0003; EV-0005 | **Attested** |

| **AT-AGM-04** | AGR-0004 | ACTIVE parent; LE-0003; EV-0005; ongoing PRJ-0007 | **Attested** |

| **AT-AGM-05** | AGR-0005 | ACTIVE parent; WF-02 pilot; LE-0003; EV-0005 | **Attested** |

| **AT-AGM-06** | AGR-0006 | ACTIVE parent; LE-0004; EV-W1B-CC-01; E0 | **Attested** |

| **AT-AGM-07** | AGR-0007 | EXPIRED parent; LE-0004; EV-W1B-CC-01; E0 | **Attested** |

| **AT-AGM-08** | AGR-0008 | ACTIVE parent; LE-0005; EV-W1C-CC-01; E0 | **Attested** |



**Result:** **8/8** metadata rows attested · **0** rejected · **0** deferred within scope.



---



## 4. Per-row attestation detail



### 4.1 AT-AGM-01 — AGR-0001



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | EXPIRED | AT-AGL-01 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | EXPIRED | Deprecated PRJ-0004 |

| counterparty_profile | LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | PROJECT_DELIVERY | DEVELOPMENT completed phase |

| evidence_level | E1 | Parent copy |



### 4.2 AT-AGM-02 — AGR-0002



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-02 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | ONGOING | Active PRJ-0005; ongoing delivery notes |

| counterparty_profile | LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | PROJECT_DELIVERY | DEVELOPMENT active delivery |

| evidence_level | E1 | Parent copy |



### 4.3 AT-AGM-03 — AGR-0003



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-03 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | ONGOING | SEO_RETAINER + active PRJ-0006 |

| counterparty_profile | LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | MONTHLY_REPORT | SEO_RETAINER per AGM-DE-01 |

| evidence_level | E1 | Parent copy |



### 4.4 AT-AGM-04 — AGR-0004



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-04 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | ONGOING | Active PRJ-0007 |

| counterparty_profile | LE-0003; EV-0005 | Wave 1 + commercial evidence |

| document_expectation | PROJECT_DELIVERY | DEVELOPMENT active delivery |

| evidence_level | E1 | Parent copy |



### 4.5 AT-AGM-05 — AGR-0005



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-05; WF-02 pilot |

| start_date / end_date | SAFE UNKNOWN | WF-02 gap documented |

| renewal_posture | ONGOING | Active PRJ-0008; WF-01 contour |

| counterparty_profile | LE-0003; EV-0005 | WF-02 pilot consumed |

| document_expectation | PROJECT_DELIVERY | WF-02 live pilot validated |

| evidence_level | E1 | Parent copy |



### 4.6 AT-AGM-06 — AGR-0006



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-06 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | ONGOING | Active PRJ-0009 WIP |

| counterparty_profile | LE-0004; EV-W1B-CC-01 | AT-W1B-01 |

| document_expectation | PROJECT_DELIVERY | DEVELOPMENT WIP |

| evidence_level | E0 | Parent copy — not upgraded |



### 4.7 AT-AGM-07 — AGR-0007



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | EXPIRED | AT-AGL-07 |

| start_date / end_date | SAFE UNKNOWN | Narrative «~5 years» not ISO-attested |

| renewal_posture | EXPIRED | Deprecated PRJ-0010 |

| counterparty_profile | LE-0004; EV-W1B-CC-01 | AT-W1B-01 |

| document_expectation | PROJECT_DELIVERY | Historical DEVELOPMENT |

| evidence_level | E0 | Parent copy |



### 4.8 AT-AGM-08 — AGR-0008



| Field | Value | Basis |

|-------|-------|-------|

| operational_status | ACTIVE | AT-AGL-08 |

| start_date / end_date | SAFE UNKNOWN | No E2 extract |

| renewal_posture | ONGOING | Active PRJ-0011; OCPilot WIP |

| counterparty_profile | LE-0005; EV-W1C-CC-01 | AT-W1C-01 |

| document_expectation | PROJECT_DELIVERY | DEVELOPMENT WIP |

| evidence_level | E0 | Parent copy |



---



## 5. Verification checklist



| Check | Result |

|-------|--------|

| Every metadata row has parent Agreement | **Pass** (8/8) |

| operational_status matches parent | **Pass** (8/8) |

| No dates invented | **Pass** |

| counterparty_profile uses attested LE only | **Pass** (8/8) |

| document_expectation per AGM-DE rules | **Pass** (8/8) |

| No contract text stored | **Pass** |

| Makita — no assumed metadata | **Pass** |



---



## 6. Related documents



| Document | Role |

|----------|------|

| [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) | Canonical metadata roster |

| [ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md) | ACTIVE completeness act |

| [REPORT-atlas-agreement-metadata-layer-v1.md](../reports/REPORT-atlas-agreement-metadata-layer-v1.md) | Wave pass record |



---



*ATLAS Agreement Metadata Attestation v1 — Wave AGM-01. Methodology and attestation act.*

