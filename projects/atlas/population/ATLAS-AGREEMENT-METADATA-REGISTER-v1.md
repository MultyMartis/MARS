# ATLAS Agreement Metadata Register v1



**Status:** **attested** — canonical Agreement metadata roster after Wave AGM-01 attestation act.  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-10 (AGM-01) · **sync:** 2026-06-10 (E2-AGR-DATES-01)  

**Wave:** AGM-01 — Agreement Metadata Layer · E2-AGR-DATES-01 date extract cross-ref  

**Parent:** [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-METADATA-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-METADATA-MODEL-v1.md) · [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md)  

**Is not:** runtime export, database table, contract archive, requisites store.



---



## 1. Purpose



Канонический **реестр операционных метаданных** для attested Agreement records (AGL-01). Одна строка — один metadata overlay на parent Agreement. **No contract text. No structured requisites inline.**



**Register summary:**



| Metric | Count |

|--------|-------|

| Total metadata rows | **8** |

| operational_status ACTIVE | **6** |

| operational_status EXPIRED | **2** |

| start_date attested | **0** |

| end_date attested | **0** |

| renewal_posture ONGOING | **6** |

| renewal_posture EXPIRED | **2** |

| document_expectation PROJECT_DELIVERY | **7** |

| document_expectation MONTHLY_REPORT | **1** |

| counterparty_profile with LE ref | **8** |



---



## 2. Attested metadata roster — full table



| agreement_id | operational_status | start_date | end_date | renewal_posture | counterparty_profile | document_expectation | evidence_level | attestation_ref | notes |

|--------------|-------------------|------------|----------|-----------------|----------------------|----------------------|----------------|-----------------|-------|

| AGR-0001 | **EXPIRED** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **EXPIRED** | LE-0003; EV-0005 | PROJECT_DELIVERY | E1 | AT-AGM-01 | Historical; PRJ-0004 deprecated |

| AGR-0002 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0003; EV-0005 | PROJECT_DELIVERY | E1 | AT-AGM-02 | Ongoing delivery PRJ-0005 |

| AGR-0003 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0003; EV-0005 | **MONTHLY_REPORT** | E1 | AT-AGM-03 | SEO_RETAINER; WF-01 contour |

| AGR-0004 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0003; EV-0005 | PROJECT_DELIVERY | E1 | AT-AGM-04 | Ongoing delivery PRJ-0007 |

| AGR-0005 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0003; EV-0005 | PROJECT_DELIVERY | E1 | AT-AGM-05 | WF-01/WF-02 pilot anchor PRJ-0008 |

| AGR-0006 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0004; EV-W1B-CC-01 | PROJECT_DELIVERY | E0 | AT-AGM-06 | WIP catalog PRJ-0009 |

| AGR-0007 | **EXPIRED** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **EXPIRED** | LE-0004; EV-W1B-CC-01 | PROJECT_DELIVERY | E0 | AT-AGM-07 | Historical; PRJ-0010 deprecated |

| AGR-0008 | **ACTIVE** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **ONGOING** | LE-0005; EV-W1C-CC-01 | PROJECT_DELIVERY | E0 | AT-AGM-08 | OCPilot WIP PRJ-0011 |



---



## 3. Attested roster — by operational status



### 3.1 ACTIVE — 6 rows



| agreement_id | renewal_posture | document_expectation | counterparty_profile | evidence_level |

|--------------|-----------------|----------------------|----------------------|----------------|

| AGR-0002 | ONGOING | PROJECT_DELIVERY | LE-0003; EV-0005 | E1 |

| AGR-0003 | ONGOING | MONTHLY_REPORT | LE-0003; EV-0005 | E1 |

| AGR-0004 | ONGOING | PROJECT_DELIVERY | LE-0003; EV-0005 | E1 |

| AGR-0005 | ONGOING | PROJECT_DELIVERY | LE-0003; EV-0005 | E1 |

| AGR-0006 | ONGOING | PROJECT_DELIVERY | LE-0004; EV-W1B-CC-01 | E0 |

| AGR-0008 | ONGOING | PROJECT_DELIVERY | LE-0005; EV-W1C-CC-01 | E0 |



### 3.2 EXPIRED — 2 rows



| agreement_id | renewal_posture | document_expectation | counterparty_profile | evidence_level |

|--------------|-----------------|----------------------|----------------------|----------------|

| AGR-0001 | EXPIRED | PROJECT_DELIVERY | LE-0003; EV-0005 | E1 |

| AGR-0007 | EXPIRED | PROJECT_DELIVERY | LE-0004; EV-W1B-CC-01 | E0 |



---



## 4. Attested roster — by document expectation



| document_expectation | Count | agreement_ids |

|---------------------|-------|---------------|

| PROJECT_DELIVERY | **7** | AGR-0001, 0002, 0004, 0005, 0006, 0007, 0008 |

| MONTHLY_REPORT | **1** | AGR-0003 |

| MONTHLY_CLOSING | **0** | — |

| MIXED | **0** | — |

| UNKNOWN | **0** | — |



---



## 5. Attested roster — by renewal posture



| renewal_posture | Count | agreement_ids |

|-----------------|-------|---------------|

| ONGOING | **6** | AGR-0002..0006, AGR-0008 |

| EXPIRED | **2** | AGR-0001, AGR-0007 |

| FIXED_TERM | **0** | — |

| UNKNOWN | **0** | — |



---



## 6. Counterparty profile index



| counterparty_profile | client_org | agreements | CC storage pointer |

|---------------------|------------|------------|-------------------|

| LE-0003; EV-0005 | ORG-0004 Триумф | AGR-0001..0005 | `triumph\` under external CC root |

| LE-0004; EV-W1B-CC-01 | ORG-0005 ЗПМ | AGR-0006, AGR-0007 | `bzpm\Реквизиты.docx` |

| LE-0005; EV-W1C-CC-01 | ORG-0006 SIBCAR | AGR-0008 | `sibcar\Реквизиты.docx` |



**Requisites consumption rule:** OPS follows LE id + EV ref to external storage — no inline INN/bank fields in this register.



---



## 7. Metadata coverage vs parent Agreement register



| Parent field (AGL-01) | Metadata overlay adds |

|-----------------------|----------------------|

| status | operational_status (mirrored) + renewal_posture |

| start_date / end_date | unchanged SAFE UNKNOWN — E2-AGR-DATES-01 reviewed; 0/8 attested ([ATLAS-AGREEMENT-DATE-REGISTER-v1.md](ATLAS-AGREEMENT-DATE-REGISTER-v1.md)) |

| agreement_type | document_expectation (operational mapping) |

| client_org | counterparty_profile (LE + CC pointer) |

| evidence_level | copied — not upgraded |



---



## 8. Deferred register (not populated)



| Item | Reason |

|------|--------|

| Agreement ISO dates (all rows) | E2-AGR-DATES-01 complete — still 0/8 attested; await E2 extract pointer |

| MONTHLY_CLOSING rows | No calendar closing attestation |

| MIXED document expectation | No multi-class attestation |

| Makita metadata | No parent Agreement row |

| Signing expectation fields | Out of AGM-01 scope — Person contact channels absent |

| Structured requisites block | CC pointer only |



---



## 9. Evidence index



| Ref | Artifact | Metadata rows supported |

|-----|----------|------------------------|

| AT-AGM-01..08 | [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) | All register rows |

| AT-AGL-01..08 | [ATLAS-AGREEMENT-ATTESTATION-v1.md](ATLAS-AGREEMENT-ATTESTATION-v1.md) | Parent agreement basis |

| LE-0003..0005 | Integrity snapshot / Wave 1 registers | counterparty_profile |

| EV-0005 | Triumph commercial spreadsheet | AGR-0001..0005 |

| EV-W1B-CC-01 | ZPM CC | AGR-0006, AGR-0007 |

| EV-W1C-CC-01 | SIBCAR CC | AGR-0008 |

| OPS-WF02-LIVE-PILOT | WF-02 pilot AGR-0005 | document_expectation corroboration |
| AT-E2-01..08 | [ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md](ATLAS-AGREEMENT-DATE-ATTESTATION-v1.md) | Date extract pass — all SAFE UNKNOWN |



Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).



---



## 10. Related documents



| Doc | Role |

|-----|------|

| [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | Parent Agreement roster |

| [ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md) | ACTIVE metadata completeness act |

| [REPORT-atlas-agreement-metadata-layer-v1.md](../reports/REPORT-atlas-agreement-metadata-layer-v1.md) | Wave pass record |
| [ATLAS-AGREEMENT-DATE-REGISTER-v1.md](ATLAS-AGREEMENT-DATE-REGISTER-v1.md) | E2 date fact roster |
| [REPORT-atlas-agreement-date-extract-v1.md](../reports/REPORT-atlas-agreement-date-extract-v1.md) | E2-AGR-DATES-01 pass record |



---



*ATLAS Agreement Metadata Register v1 — Wave AGM-01. Attested operational metadata only.*

