# REPORT — ORCA SEMANTIC INTELLIGENCE — ARCHITECTURE DECISION RECORD V1

**Task:** P0-A — ORCA Semantic Intelligence Architecture Decision Record  
**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` ✓ |
| Pre-task HEAD | `59b7e92` |
| Research package exists | ✓ `projects/orca/research/ppc-semantic-intelligence/` |
| Canonical SHA-256 | `984192DAFC79AA9E7071C5F915CD30A630924C5EEBAE22BFD6C26CCD43CE5ACD` ✓ (verified) |
| D1–D7 | ✓ `decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md` |
| Gap matrix | ✓ |
| Promotion backlog | ✓ P0-A through P0-H |
| Corvonero diagnostic freeze | ✓ `corvonero-direct-v2-clean-room/PROJECT.md` |
| Unrelated WIP present | ✓ OCPilot, Website Factory, FP-0002, `.recovery-temp/` — **not staged** |

---

## 2. Selective Git Checkpoint

| Field | Value |
|-------|-------|
| Status | **COMMITTED AND PUSHED** |
| Commit | `b130068` |
| Message | `docs(orca): register PPC semantic intelligence research gate` |
| Files | 21 (research package + Corvonero PROJECT.md + OPERATIONAL-INDEX + README) |
| Push | `origin/mars/post-cycle8-live-tests` — success |
| Isolation | Verified — no unrelated files in staged diff |

---

## 3. Architecture Inputs

| Source class | Artifacts used |
|--------------|----------------|
| Operator decisions | D1–D7 |
| Analytical | World-practice research, normalized companion, source ledger, research review, gap matrix |
| Evidence | Corvonero clean-room v1 failure; Triumph laws; Campaign Production Contract v1 |
| Forbidden as authority | Corvonero v1 semantic decisions; old XLSX; defective pipeline heuristics |

---

## 4. Research Promotion Matrix

Created with 20 assessed items:

| Status | Count |
|--------|-------|
| PROMOTED | 10 |
| PROMOTED WITH ADAPTATION | 7 |
| DEFERRED | 2 (second-model review, active learning) |
| REJECTED | 0 |
| SAFE UNKNOWN | 0 |

---

## 5. ADR

**ORCA Semantic Intelligence ADR v1** — status: `PROPOSED — OPERATOR APPROVAL REQUIRED`

23 required sections documented. Selected architecture: managed multi-stage system SI-01 through SI-17 — **not** a monolithic classifier.

---

## 6. Architecture Goals and Non-Goals

**Goals:** Separate authorities; hierarchical gates; ACCEPT/REJECT/ABSTAIN; human review; semantic freeze; export transport-only; post-launch proposals only.

**Non-goals:** Classifier implementation; benchmark; annotation guideline; Corvonero rerun; campaign/Commander authorization; runtime claims.

---

## 7. Selected Layer Model

17 layers SI-01 (Operator Authority) through SI-17 (Post-Launch Learning) documented with inputs, outputs, and prohibitions in flow document.

---

## 8. Authority Model

12-rank strict hierarchy. Operator decisions and approved Semantic Core at top. Export and post-launch at bottom. Lower layers cannot override higher.

---

## 9. Information Flow

Documented high-level flow from Operator + Market Evidence through Normalization → Understanding → Screening → Intent → Eligibility → mapping → clusters → negatives → core → campaign → export QA → post-launch proposals.

---

## 10. State Machine

Phrase lifecycle states from `RAW` through `APPROVED` / `EXPORT_QA` with prohibited shortcuts table (e.g. SI-11 before SI-08, SI-15 phrase addition).

---

## 11. Admission Policy

ACCEPT / REJECT / ABSTAIN with mandatory abstain conditions per D4. Three risk modes: CONSERVATIVE (Corvonero initial), BALANCED, EXPLORATORY.

---

## 12. Risk Modes

Corvonero initial mode: **CONSERVATIVE** — highest ACCEPT threshold, largest ABSTAIN queue, strictest protected-strata handling.

---

## 13. Quality Gates

Operator-approved (D3/D4/D7): commercial precision ≥ 0.95; protected-strata FPR ≤ 0.01; ABSTAIN mandatory; no campaign before approved core.

Additional metrics marked `PROPOSED — BENCHMARK VALIDATION REQUIRED`.

---

## 14. Component Responsibility Matrix

8 components: deterministic rules, weak supervision, supervised classifier, embeddings, LLM, human reviewer, operator, validator. Pure LLM is not core authority.

---

## 15. Contract Family Plan

12 contracts defined — all status `PLANNED`. Full schemas deferred to P0-B onward.

---

## 16. Migration Boundary

**Reusable:** intake, scope, MIG ledger, corpus, normalized/canonical registry, research, compatible production contract elements.

**Diagnostic only:** clean-room v1 semantic decisions; v1–v7.1 production.

**Must create later:** taxonomy, guideline, benchmark, gold labels, baselines, harness, approved Semantic Core.

No semantic decision migration from diagnostic layers.

---

## 17. Architecture Risks

18 risks registered (R-01 through R-18). Top blocking: over-admission, campaign-layer contamination, post-launch feedback leakage.

---

## 18. Architecture Validation

**PASS — DOCUMENTATION VALIDATION** (20/20 checks). Not implementation validation.

---

## 19. ORCA Map Updates

Updated (uncommitted):

- `projects/orca/OPERATIONAL-INDEX.md` — Semantic Intelligence Architecture v1 section; P0-A status; next gate P0-B
- `projects/orca/README.md` — architecture entry point
- `projects/orca/architecture/semantic-intelligence/README.md` — layer index

---

## 20. Files Created or Changed

### Committed (research checkpoint `b130068`)

21 files under research package, Corvonero PROJECT.md, OPERATIONAL-INDEX, README (research gate state).

### Created — uncommitted (architecture package)

| File |
|------|
| `architecture/semantic-intelligence/README.md` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-adr-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-research-promotion-matrix-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-authority-model-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-FLOW-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-flow-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-ADMISSION-POLICY-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-admission-policy-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-quality-gates-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-COMPONENT-RESPONSIBILITY-MATRIX-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-component-responsibility-matrix-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-CONTRACT-FAMILY-PLAN-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-contract-family-plan-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-MIGRATION-BOUNDARY-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-migration-boundary-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-RISKS-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-architecture-risks-v1.json` |
| `architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-VALIDATION-v1.md` |
| `architecture/semantic-intelligence/orca-semantic-intelligence-architecture-validation-v1.json` |
| `architecture/semantic-intelligence/reports/REPORT-orca-semantic-intelligence-architecture-decision-record-v1.md` |

### Modified — uncommitted

- `projects/orca/OPERATIONAL-INDEX.md`
- `projects/orca/README.md`

---

## 21. Git Status After Architecture Work

- **HEAD:** `b130068` (research checkpoint only)
- **Architecture files:** untracked / uncommitted per task instruction
- **Unrelated WIP:** unchanged and unstaged

---

## 22. SAFE UNKNOWN

- Optimal production abstention rate (research suggests ≥ 0.15 early — not operator-validated).
- Exact classifier architecture selection (deferred to P0-F).
- Full external source URL resolvability from research bytes.
- Whether Triumph laws alone suffice without new Semantic Intelligence contracts (partial overlap documented).

---

## 23. Operator Approval Items

1. Approve or reject **ORCA Semantic Intelligence ADR v1** as proposed architecture.
2. Confirm 17-layer model and authority hierarchy.
3. Confirm ACCEPT / REJECT / ABSTAIN admission policy and CONSERVATIVE mode for Corvonero.
4. Confirm D3 thresholds remain binding.
5. Confirm selective promotion matrix (no wholesale research adoption).
6. Authorize P0-B start after ADR approval.

---

## 24. Next Gate

**OPERATOR APPROVAL OF ORCA SEMANTIC INTELLIGENCE ADR V1**

Then: **P0-B — Semantic Taxonomy and Record Schema**

---

## 25. Stop Condition

Task complete. Stopped per instruction.

| Item | Status |
|------|--------|
| Research checkpoint | COMMITTED AND PUSHED |
| Research findings | SELECTIVELY PROMOTED |
| ADR v1 | PROPOSED — OPERATOR APPROVAL REQUIRED |
| Target architecture | DOCUMENTED — NOT IMPLEMENTED |
| Admission model | ACCEPT / REJECT / ABSTAIN |
| Corvonero mode | CONSERVATIVE |
| Corvonero clean-room | FROZEN |
| Benchmark | NOT STARTED |
| Annotation guideline | NOT STARTED |
| Classifier | NOT STARTED |
| Campaign production | BLOCKED |
| Commander | BLOCKED |

**Not performed:** ADR operator approval; classifier; benchmark; annotation; Corvonero rerun; campaigns; Commander files; architecture commit.
