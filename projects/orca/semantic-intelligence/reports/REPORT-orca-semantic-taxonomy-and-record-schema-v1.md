# REPORT — ORCA SEMANTIC INTELLIGENCE — SEMANTIC TAXONOMY AND RECORD SCHEMA V1

**Task:** P0-B — Semantic Taxonomy and Record Schema  
**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`  
**P0-A checkpoint commit:** `f17c270`  
**Status:** Complete — P0-B uncommitted pending operator approval

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` ✓ |
| Research checkpoint `b130068` in history | ✓ (`git log`) |
| Architecture package existed uncommitted | ✓ (was `?? projects/orca/architecture/`) |
| ADR status before task | `PROPOSED — OPERATOR APPROVAL REQUIRED` ✓ |
| Unrelated WIP not staged for P0-A commit | ✓ (only 28 P0-A files committed) |
| Corvonero frozen | ✓ |
| Implementation not started | ✓ |
| HEAD after task | `d446468` (unrelated FP-0002 work after P0-A checkpoint) |

---

## 2. Operator Approval A1–A7

Recorded in:

- `projects/orca/architecture/semantic-intelligence/decisions/ORCA-SEMANTIC-INTELLIGENCE-ADR-V1-OPERATOR-APPROVAL.md`
- `projects/orca/architecture/semantic-intelligence/decisions/orca-semantic-intelligence-adr-v1-operator-approval.json`

| ID | Decision |
|----|----------|
| A1 | `APPROVED — IMPLEMENTATION NOT STARTED` |
| A2 | SI-01–SI-17, no monolithic classifier, layer separation, authority order, human review, Semantic Core before Campaign Production |
| A3 | ACCEPT / REJECT / ABSTAIN; mandatory ABSTAIN when commercial intent insufficient |
| A4 | Corvonero risk mode `CONSERVATIVE` |
| A5 | Commercial precision auto-accept `>= 0.95`; protected-strata FPR `<= 0.01` per class |
| A6 | Abstention rate `>= 0.15` → `DIAGNOSTIC INDICATOR — BENCHMARK VALIDATION REQUIRED` (not production blocker) |
| A7 | P0-B `AUTHORIZED` |

---

## 3. Approved Architecture Updates

- ADR v1 MD/JSON status → `APPROVED — IMPLEMENTATION NOT STARTED`
- Promotion matrix status → `APPROVED — ADR OPERATOR SIGNED`; PENDING ADR items → `APPROVED (ADR v1)`
- Architecture validation updated — operator approval recorded; criterion 20 → ADR approved status
- Architecture README updated with checkpoint status

---

## 4. Selective Architecture Checkpoint

| Field | Value |
|-------|-------|
| Commit | `f17c270` |
| Message | `docs(orca): approve semantic intelligence architecture v1` |
| Push | Success → `origin/mars/post-cycle8-live-tests` |
| Files | 28 (architecture package + OPERATIONAL-INDEX + README map lines) |
| P0-B excluded | ✓ |

---

## 5. P0-B Authority Inputs

**Authoritative:** ADR v1, authority model, admission policy, risk modes, quality gates, A1–A7, D1–D7.

**Analytical:** world-practice research, normalized companion, source ledger, promotion matrix.

**Diagnostic evidence:** Corvonero clean-room failure examples, ORCA over-admission examples, pipeline failures.

**Forbidden as taxonomy authority:** old Corvonero phrase labels, ACTIVE/HOLD/EXCLUDE, classifier outputs, old group structures, defective dataset field names.

---

## 6. Taxonomy Design Principles

Created `taxonomy/ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md` — 15 principles including topic≠intent, ABSTAIN for ambiguity, service mapping after ACCEPT, no export-time decisions.

---

## 7. Primary Intent Taxonomy

- `taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`
- `taxonomy/orca-primary-intent-taxonomy-v1.json`
- **26 primary intents** (all required IDs from task specification)
- Protected classes: career, educational, diy_how_to, regulatory, navigational mapped to intent IDs
- Primary intent explicitly not final PPC decision

---

## 8. User Goal Taxonomy

- `taxonomy/ORCA-USER-GOAL-TAXONOMY-v1.md`
- `taxonomy/orca-user-goal-taxonomy-v1.json`
- 23 goals including separate `SEEK_EMPLOYMENT`, `HIRE_EMPLOYEE`, `HIRE_PROVIDER`

---

## 9. Signal Taxonomy

- `taxonomy/ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`
- `taxonomy/orca-semantic-signal-taxonomy-v1.json`
- 31 signals; strengths NONE→EXPLICIT; evidence span, token, source, confidence, conflict_flag

---

## 10. Ambiguity Taxonomy

- `taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md`
- `taxonomy/orca-ambiguity-taxonomy-v1.json`
- 13 ambiguity types; severities LOW→CRITICAL; mandatory ABSTAIN rules documented

---

## 11. Commercial Eligibility Taxonomy

- `taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`
- `taxonomy/orca-commercial-eligibility-taxonomy-v1.json`
- ACCEPT / REJECT / ABSTAIN with reason families and required record fields

---

## 12. Risk Taxonomy

- `taxonomy/ORCA-SEMANTIC-RISK-TAXONOMY-v1.md`
- `taxonomy/orca-semantic-risk-taxonomy-v1.json`
- 12 risk dimensions; aggregation; high risk may require ABSTAIN not auto-REJECT

---

## 13. Review Status Taxonomy

- `taxonomy/ORCA-SEMANTIC-REVIEW-STATUS-v1.md`
- `taxonomy/orca-semantic-review-status-v1.json`
- 11 workflow statuses; distinct from eligibility

---

## 14. Canonical Semantic Record Schema

- `schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`
- `schemas/orca-semantic-record-schema-v1.json`
- `schemas/orca-semantic-record-schema-v1.schema.json` (JSON Schema draft **2020-12**)
- All required top-level field groups per ADR

---

## 15. Null and Unknown Policy

- `schemas/ORCA-SEMANTIC-NULL-UNKNOWN-POLICY-v1.md`
- Canonical machine values; forbids numeric sentinels and `[object Object]`

---

## 16. Schema Invariants

- `contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`
- `contracts/orca-semantic-record-invariants-v1.json`
- 20 invariants including topic≠ACCEPT, service candidate before ACCEPT, ABSTAIN as valid terminal

---

## 17. Decision Trace Model

- `schemas/ORCA-SEMANTIC-DECISION-TRACE-v1.md`
- `schemas/orca-semantic-decision-trace-v1.schema.json`

---

## 18. Fixtures

**Purpose:** schema shape and invariant validation only — **NOT gold labels**.

| Type | Count | Examples |
|------|-------|----------|
| Valid | 9 | hire service, integration, career, DIY, ABSTAIN short head, ABSTAIN problem, product reject, human ACCEPT, operator override |
| Invalid | 9 | service-term-only ACCEPT, high ambiguity ACCEPT, REJECT no reason, ABSTAIN no question, ownership before ACCEPT, campaign field, numeric placeholder, object text, missing provenance |

Manifest: `fixtures/fixture-manifest-v1.json`

---

## 19. Validation

- `validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md`
- `validation/orca-semantic-taxonomy-and-schema-validation-v1.json`
- **Result:** `PASS — DOCUMENTATION VALIDATION`
- No benchmark or classifier created
- Heavy JSON Schema runtime dependency not added

---

## 20. P0-B Decision Record

- `decisions/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-DECISION-v1.md`
- `decisions/orca-semantic-taxonomy-and-schema-decision-v1.json`
- **Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## 21. Map and Backlog Updates

Updated (uncommitted):

- `projects/orca/OPERATIONAL-INDEX.md` — P0-B locus section
- `projects/orca/README.md` — P0-B entry
- `projects/orca/architecture/semantic-intelligence/README.md` — P0-B status
- `research/.../promotion/ORCA-PPC-SEMANTIC-INTELLIGENCE-PROMOTION-BACKLOG-v1.md`
- `research/.../promotion/orca-ppc-semantic-intelligence-promotion-backlog-v1.json`

| Item | Status |
|------|--------|
| P0-A | APPROVED — CHECKPOINTED (`f17c270`) |
| P0-B | PROPOSED — OPERATOR REVIEW |
| P0-C | BLOCKED UNTIL P0-B APPROVAL |
| Corvonero | FROZEN |
| Campaign production | BLOCKED |

---

## 22. Files Created or Changed

### Committed (P0-A — `f17c270`)

`projects/orca/architecture/semantic-intelligence/**` (28 files), `OPERATIONAL-INDEX.md`, `README.md` (P0-A lines)

### Uncommitted (P0-B)

`projects/orca/semantic-intelligence/**` (~47 files), map/backlog updates listed above

---

## 23. Git Status

- P0-A: committed and pushed at `f17c270`
- P0-B: `?? projects/orca/semantic-intelligence/`
- Map updates: modified, not staged
- No P0-B files committed per task instructions

---

## 24. SAFE UNKNOWN

- Automated JSON Schema validation against fixtures via AJV not executed in CI for this locus (validator exists in Triumph tooling but not wired to P0-B path). Documentation validation PASS; runtime schema validation deferred to P0-F implementation gate.
- Exact production abstention rate threshold remains diagnostic until P0-D/E/G benchmark.

---

## 25. Operator Approval Items

Operator must approve P0-B package:

1. Taxonomy principles and 6 taxonomy families
2. Canonical semantic record schema v1
3. Null/unknown policy
4. 20 invariants
5. Decision trace model
6. Fixture scope (schema validation only)
7. P0-B decision record

---

## 26. Next Gate

**OPERATOR APPROVAL OF ORCA SEMANTIC TAXONOMY AND RECORD SCHEMA V1**

Then: **P0-C — Annotation Guideline**

---

## 27. Stop Condition

Stop conditions met:

- ADR approval recorded ✓
- P0-A committed and pushed ✓
- Taxonomy v1 created ✓
- Semantic record schema v1 created ✓
- Invariants and decision trace defined ✓
- Schema fixtures created ✓
- P0-B package validated (documentation) ✓
- Maps updated ✓
- P0-B not committed ✓
- No annotation guideline, benchmark, classifier, Corvonero rerun, or campaign production ✓
