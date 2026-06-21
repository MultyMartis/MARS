# ATLAS Agreement Date Attestation v1

**Status:** **attested** — Wave E2-AGR-DATES-01 Agreement date extract attestation methodology and act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** E2-AGR-DATES-01 — Agreement Date Extract Pass  
**Attestor role:** Registry Steward (delegated)  
**Parent:** [ATLAS-AGREEMENT-DATE-EXTRACT-PLAN-v1.md](ATLAS-AGREEMENT-DATE-EXTRACT-PLAN-v1.md) · [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) · [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-REALITY-MODEL-v1.md)  
**Is not:** contract storage, legal validity confirmation, OCR output.

---

## 1. Purpose

Настоящий акт фиксирует **каноническую attestation** Wave E2-AGR-DATES-01: review of existing evidence for **AGR-0001..AGR-0008** date facts (`start_date`, `end_date`).

**Scope:**

| In attestation | Out of attestation |
|----------------|-------------------|
| Date fact evaluation per Agreement row | Contract text / PDF storage |
| Evidence-only negative attestation (SAFE UNKNOWN) | Date inference from project lifecycle |
| Pointer review of EV-* / LE-* / CC artifacts | renewal_posture / document_expectation changes |
| Register population | Runtime, API, OPS changes |

---

## 2. Attestation methodology

### 2.1 Preconditions

Date attestation **requires** **all** rows:

| # | Requirement |
|---|-------------|
| 1 | Parent Agreement row attested in AGL-01 register |
| 2 | Parent metadata overlay attested in AGM-01 register |
| 3 | E2+ contract date extract **reference** attested by steward — or **SAFE UNKNOWN** |
| 4 | No fabricated dates |
| 5 | No inference from project start/end, CC filename year, or operator narrative |

### 2.2 Field attestation rules

| Field | Attestation source |
|-------|-------------------|
| start_date | E2+ extract with explicit ISO start — else **SAFE UNKNOWN** |
| end_date | E2+ extract with explicit ISO end — else **SAFE UNKNOWN** |
| status | ATTESTED (both dates) · PARTIAL (one date) · SAFE_UNKNOWN (insufficient) |
| confidence | Assigned only when at least one ISO date attested |

### 2.3 Rejected inference paths

| Path | Rule | Example rejected |
|------|------|------------------|
| Project lifecycle → end_date | AGR-ST-01 | PRJ-0004 deprecated → AGR-0001 end_date |
| CC filename year → start_date | AT-E-05 | `triumph/…2024.xlsx` → 2024-01-01 |
| Operator narrative → ISO date | SU-ZPM-PRJ-01 | «~5 years ago» → AGR-0007 end_date |
| EXPIRED status → end_date | AGR-ST-01 | Status alone does not attest end_date |
| Retainer type → open-ended end | — | SEO_RETAINER does not attest dates |

### 2.4 Evidence tiers for dates

| Tier | Date attestation |
|------|------------------|
| **E0** | **Insufficient** for ISO dates |
| **E1** | CC / spreadsheet — **insufficient** unless explicit contract period fields steward-attested |
| **E2+** | **Required** for date attestation — **none attested in E2-AGR-DATES-01** |
| **E3** | System timestamps — **not used** for agreement period |

---

## 3. Attestation act — tranche summary

| Tranche | agreement_id | Basis | start_date | end_date | Outcome |
|---------|--------------|-------|------------|----------|---------|
| **AT-E2-01** | AGR-0001 | EV-0005 reviewed; PRJ-0004 deprecated; no E2 extract | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-02** | AGR-0002 | EV-0005 reviewed; active PRJ-0005; no E2 extract | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-03** | AGR-0003 | EV-0005 reviewed; SEO_RETAINER; no E2 extract | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-04** | AGR-0004 | EV-0005 reviewed; active PRJ-0007; no E2 extract | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-05** | AGR-0005 | EV-0005 + WF-02 pilot; no E2 extract | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-06** | AGR-0006 | EV-W1B-CC-01 requisites only; SU-W6B-03 | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-07** | AGR-0007 | EV-W1B-CC-01; SU-ZPM-PRJ-01 narrative rejected | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |
| **AT-E2-08** | AGR-0008 | EV-W1C-CC-01; ME-W3-SIBCAR-01; no SOW dates | SAFE UNKNOWN | SAFE UNKNOWN | **SAFE_UNKNOWN** |

**Result:** **8/8** rows evaluated · **0** dates attested · **0** rejected (scope) · **8** SAFE_UNKNOWN outcomes.

---

## 4. Per-row attestation detail

### 4.1 AT-E2-01 — AGR-0001

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | EXPIRED from lifecycle — not date inference |
| evidence_source | AGL-01; EV-0005; AT-E2-01 | CC reviewed — no period fields attested |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.2 AT-E2-02 — AGR-0002

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | Ongoing delivery — no term extract |
| evidence_source | AGL-01; EV-0005; AT-E2-02 | CC reviewed |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.3 AT-E2-03 — AGR-0003

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | Retainer ongoing — no term extract |
| evidence_source | AGL-01; EV-0005; AT-E2-03 | CC reviewed |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.4 AT-E2-04 — AGR-0004

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | Active PRJ-0007 — no term extract |
| evidence_source | AGL-01; EV-0005; AT-E2-04 | CC reviewed |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.5 AT-E2-05 — AGR-0005

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | WF-02 pilot documents period binding blocked |
| evidence_source | AGL-01; EV-0005; OPS-WF02; AT-E2-05 | Strongest OPS contour — dates still unknown |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.6 AT-E2-06 — AGR-0006

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | EV-W1B-CC-01 requisites only |
| end_date | SAFE UNKNOWN | SU-W6B-03 — E2 extract existence unknown |
| evidence_source | AGL-01; EV-W1B-CC-01; AT-E2-06 | CC pointer reviewed |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.7 AT-E2-07 — AGR-0007

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | No E2 contract date extract |
| end_date | SAFE UNKNOWN | Operator «~5 years ago» — narrative not ISO (SU-ZPM-PRJ-01) |
| evidence_source | AGL-01; EV-W1B-CC-01; AT-E2-07 | Historical EXPIRED — dates not inferred |
| status | SAFE_UNKNOWN | Both dates unknown |

### 4.8 AT-E2-08 — AGR-0008

| Field | Value | Basis |
|-------|-------|-------|
| start_date | SAFE UNKNOWN | EV-W1C-CC-01 requisites only |
| end_date | SAFE UNKNOWN | ME-W3-SIBCAR-01 — no contract-dated SOW |
| evidence_source | AGL-01; EV-W1C-CC-01; AT-E2-08 | CC pointer reviewed |
| status | SAFE_UNKNOWN | Both dates unknown |

---

## 5. Validation checklist

| Check | Result |
|-------|--------|
| All 8 Agreement rows evaluated | **Pass** |
| No dates invented | **Pass** |
| No contract text stored | **Pass** |
| No inference from project lifecycle | **Pass** |
| Narrative dates rejected (SU-ZPM-PRJ-01) | **Pass** |
| Metadata fields unchanged except dates review | **Pass** |
| Parent Agreement register unchanged | **Pass** |

---

## 6. Attestation verdict

```text
E2-AGR-DATES-01 COMPLETE — 0/8 date pairs attested — all SAFE UNKNOWN
```

**Conditions for future date attestation:**

1. Steward attests E2 contract date extract **pointer** (not text) per agreement.
2. Re-run E2 date extract pass to populate [ATLAS-AGREEMENT-DATE-REGISTER-v1.md](ATLAS-AGREEMENT-DATE-REGISTER-v1.md).
3. Update [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) date fields only where attested.
4. Re-evaluate renewal_posture FIXED_TERM candidates only when bounded dates attested.

---

*ATLAS Agreement Date Attestation v1 — Wave E2-AGR-DATES-01.*
