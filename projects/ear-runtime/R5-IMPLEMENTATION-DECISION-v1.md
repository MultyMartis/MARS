# R5 — Implementation Decision v1

**Type:** Human gate decision record — engineering start for R5 EAR Validate Layer  
**Date:** 2026-06-06  
**Charter:** [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md)  
**Prior decision:** [R5-DECISION-v1.md](R5-DECISION-v1.md) — **APPROVED WITH NOTES** (R5 program charter)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | May **R5 engineering** (implementation charter scope) proceed and **R5.1+ contract work** begin after human sign-off? |
| **Outcome** | **APPROVED WITH NOTES** |
| **Scope of approval** | R5 mission, engineering scope, work packages R5.1–R5.9, Validation Result model, validation categories, quality possession model, redaction review model, Validate Report contract, Publish Eligibility contract, Validate Engine scope, validation boundary review, readiness review gate, success/stop criteria per [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) |
| **Explicitly not approved by this decision** | R5 runtime code, Validate automation implementation, Publish execution, Store redesign, snapshot assembly, evidence generation, OCPilot integration, live acquisition, SITE-001 / PILOT execution, per-category R5-V-* rule implementation |

---

## Rationale

1. **R5 charter gate satisfied** — [R5-DECISION-v1.md](R5-DECISION-v1.md) authorizes Implementation Charter; R5 mission, scope, quality ownership, and R5→R4 publish boundary documented in [R5-CHARTER-v1.md](R5-CHARTER-v1.md).

2. **Architecture alignment** — Implementation charter maps [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R5 Validation Helpers to contract models without absorbing R3 assembly or R4 Publish.

3. **Upstream dependency chain** — R3 **COMPLETE WITH NOTES**; `--contract-snapshot` provides traceable candidate input; R2.4 and R3.6 validation boundaries referenced; distinct artefacts mandated (N-R5-03).

4. **Validation split preserved** — ValidationResult PASS / PASS WITH NOTES / FAIL distinct from R2/R3 eligibility; Publish Eligibility Recommendation (ELIGIBLE / ELIGIBLE WITH NOTES / NOT ELIGIBLE) advisory only — R4 decides (VAL-INV-02; VB-R3-02).

5. **Quality ownership explicit** — R3 candidate L0 placeholder ≠ R5 certified possession; L0–L3 certification concepts chartered without scoring formulas; only R5 may certify (Q-INV-R5-01).

6. **R3 debt acknowledged** — In-memory candidate, Store persist adapter, bulk expansion carried as notes — not blockers for implementation charter per R3 readiness decision.

**APPROVED WITH NOTES** (not bare **APPROVED**): human sign-off required before first R5 code merge per N-R5-10 and R1/R2/R3 gate pattern; per-category R5-V-* rules, validated Store marker, and report serialization remain **SAFE UNKNOWN** until R5.1+ implementation resolves.

**FAIL** would apply if implementation charter chartered Publish as R5, omitted R5→R4 boundary, assigned quality certification to R3, merged Validate with assembly, or proposed runtime code in charter phase — **none apply**.

---

## Notes (implementation)

| Note | Action |
|------|--------|
| N-R5I-01 | First engineering milestone: **R5.1 Validation Result Model** |
| N-R5I-02 | Do not implement Publish, assembly, or evidence generation in R5 |
| N-R5I-03 | Emit distinct artefacts: `ValidationResult`, `ValidateReport`, `PublishEligibilityRecommendation` — never reuse R2/R3 outputs |
| N-R5I-04 | R3 assembly pass is Validate entry precondition — implement VB-R3-01 at engine entry gate |
| N-R5I-05 | Human HITL mandatory for pilot — helpers assist, do not replace operator Validate sign-off |
| N-R5I-06 | FAIL ValidationResult → NOT ELIGIBLE recommendation — fail closed |
| N-R5I-07 | Disambiguate R2 structural / R3 assembly eligibility / R5 EAR Validate in all R5 docs |
| N-R5I-08 | Per-category R5-V-* rules — deferred to post R5.2 implementation milestones |
| N-R5I-09 | Contract-path Store persist and bulk expansion — schedule parallel or pre-live Validate (R3 debt) |
| N-R5I-10 | Human approver must record approval below before R5.1 code |

---

## Conditions for human code approval

| ID | Condition | Status |
|----|-----------|--------|
| AP-R5-01 | [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) reviewed and accepted | Pending |
| AP-R5-02 | R5/R3 boundary (certification only, no section population) — accepted | Documented in charter |
| AP-R5-03 | R5/R4 boundary (recommendation only, no Publish) — accepted | Documented in charter |
| AP-R5-04 | R3.1 `SnapshotPackage` authoritative input; R1.7 deprecated at Validate boundary — accepted | Documented |
| AP-R5-05 | Mock-first Validate; live path requires Execution Authorization — accepted | Documented |
| AP-R5-06 | External `output_root` only; no Validate bulk in git — accepted | R1.8B + EAR-STORAGE-MODEL |
| AP-R5-07 | PILOT-001 / SITE-001 execution **not** implied | Acknowledged |

---

## Conditions that block live pilot (not R5 mock contract work)

| ID | Blocker | Owner |
|----|---------|-------|
| BL-R5-01 | PILOT-001 Execution Authorization | Pilot governance |
| BL-R5-02 | Operator `credential_ref` and output root bindings | Operator |
| BL-R5-03 | Live SFTP connected acquire | R1 connector + pilot charter |
| BL-R5-04 | R4 Publish implementation | R4 — post R5 Validate |
| BL-R5-05 | Bulk expansion for live L1+ possession | R3 / R2 debt |

R5 contract-model work (R5.1–R5.6) may proceed after AP-R5-01–AP-R5-07 without BL-R5-01–BL-R5-05 resolved. Validate **code** (R5.7+) requires R5.9 Readiness Review pass.

---

## Gate transition

| Gate | Before Implementation Charter | After Implementation Charter |
|------|------------------------------|------------------------------|
| R5 Charter | **COMPLETE** | **COMPLETE** |
| R5 Implementation Charter | **NEXT** | **COMPLETE** |
| R5 Status | AUTHORIZED FOR IMPLEMENTATION CHARTER | **AUTHORIZED FOR R5.1** |
| R5 Implementation (code) | **NOT AUTHORIZED** | **NOT AUTHORIZED** until R5.9 + human sign-off AP-R5-10 |
| R5.1 Validation Result Model | **NOT STARTED** | **NEXT** |
| R4 Publish | **PLANNED** | **PLANNED** — remains after R5 implementation path |

---

## Sign-off record

| Role | Record |
|------|--------|
| Charter executor | Agent architecture charter 2026-06-06 |
| Human implementation approval | **PENDING** (AP-R5-10) |

---

## Evidence

| # | Evidence | Location |
|---|----------|----------|
| D-R5I-01 | R5 program charter | [R5-CHARTER-v1.md](R5-CHARTER-v1.md) |
| D-R5I-02 | R5 charter gate — APPROVED WITH NOTES | [R5-DECISION-v1.md](R5-DECISION-v1.md) |
| D-R5I-03 | R3 closure — READY FOR R5 WITH NOTES | [R3-READINESS-DECISION-v1.md](R3-READINESS-DECISION-v1.md) |
| D-R5I-04 | R3/R5 validation boundary | [R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md](R3.6-VALIDATION-BOUNDARY-REVIEW-v1.md) |
| D-R5I-05 | R2/R5 evidence validation boundary | [R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md](R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md) |
| D-R5I-06 | OpenCart quality mapping | [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../shared/external-access-runtime/EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| D-R5I-07 | Readiness gates | [EAR-READINESS-GATES-v1.md](../../shared/external-access-runtime/EAR-READINESS-GATES-v1.md) |
| D-R5I-08 | Backlog R5 definition | [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) |
| D-R5I-09 | R5 Implementation Charter artifact | [R5-IMPLEMENTATION-CHARTER-v1.md](R5-IMPLEMENTATION-CHARTER-v1.md) |
