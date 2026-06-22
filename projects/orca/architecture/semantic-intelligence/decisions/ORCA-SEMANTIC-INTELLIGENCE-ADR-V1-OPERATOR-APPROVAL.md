# ORCA Semantic Intelligence — ADR v1 Operator Approval Record

**Record ID:** `orca-semantic-intelligence-adr-v1-operator-approval`  
**Version:** v1  
**Date:** 2026-06-22  
**Authority:** Human operator — MARS ORCA governance

---

## Purpose

Formal record of operator approval for ORCA Semantic Intelligence Architecture Decision Record v1 and authorization of P0-B Semantic Taxonomy and Record Schema work.

---

## A1 — ADR status

**Decision:** `APPROVED — IMPLEMENTATION NOT STARTED`

ADR v1 is approved as the target architecture specification. No classifier, benchmark, annotation guideline, or runtime implementation is authorized by this approval.

---

## A2 — Architecture model

**Approved:**

- SI-01 through SI-17 multi-stage layer model;
- no monolithic classifier as commercial authority;
- strict layer separation and prohibited shortcuts per flow v1;
- authority order per authority model v1;
- explicit human review at SI-09 and SI-13;
- Semantic Core Authority (SI-14) must reach `APPROVED` before Campaign Production (SI-15).

---

## A3 — Admission model

**Approved outputs:**

- `ACCEPT`
- `REJECT`
- `ABSTAIN`

**Mandatory rule:** ABSTAIN is required when commercial intent is insufficiently supported by evidence. ABSTAIN is a valid terminal automated outcome, not a processing failure.

---

## A4 — Corvonero risk mode

**Decision:** `CONSERVATIVE`

Corvonero clean-room v1 remains frozen. Initial admission risk mode after future gate passage is CONSERVATIVE. Corvonero rerun is not authorized by this record.

---

## A5 — Approved pilot thresholds

| Threshold | Value | Status |
|-----------|-------|--------|
| Commercial precision on auto-accept | `>= 0.95` | Operator approved |
| Protected-strata FPR per class | `<= 0.01` | Operator approved |

**Protected classes:**

- career
- educational
- DIY/how-to
- regulatory
- navigational

---

## A6 — Abstention rate

Research suggestion of early abstention rate `>= 0.15` is **not** an approved mandatory production threshold.

**Recorded as:** `DIAGNOSTIC INDICATOR — BENCHMARK VALIDATION REQUIRED`

This indicator must not be used as a production blocker until benchmark validation under P0-D/E/G.

---

## A7 — P0-B authorization

**Decision:** `AUTHORIZED`

Operator authorizes P0-B — Semantic Taxonomy and Record Schema. P0-B deliverables remain `PROPOSED — OPERATOR APPROVAL REQUIRED` until separate operator sign-off.

---

## Cross-references

| Artifact | Path |
|----------|------|
| ADR v1 | `../ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md` |
| Operator decisions D1–D7 | `../../../research/ppc-semantic-intelligence/world-practice-2026-06/decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md` |
| Promotion matrix | `../ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md` |

---

## Consequences

1. P0-A architecture package may be checkpointed to version control.
2. P0-B taxonomy and schema work may proceed under approved ADR authority.
3. Implementation, classifier, benchmark, and Corvonero rerun remain blocked.
4. Campaign production and Commander remain blocked.
