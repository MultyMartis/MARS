# Website Factory — Content Validation Roadmap v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** maturity evolution path — **architecture only**  
**Связь:** [CONTENT-VALIDATION-GAPS-v1.md](CONTENT-VALIDATION-GAPS-v1.md), [page-block-validation/VALIDATION-ROADMAP-v1.md](../page-block-validation/VALIDATION-ROADMAP-v1.md)

**Не является:** delivery schedule, product roadmap with dates, runtime deployment plan.

---

## Maturity model

```text
Documentation  →  Manual Validation  →  Semi-Automatic  →  Automated  →  Runtime
     ↑ v1 HERE
```

| Phase | Description | Evidence | Status (2026-06-01) |
|-------|-------------|----------|---------------------|
| **1 — Documentation** | Contracts, rules, matrix, failure library, severity | 8 artefacts in `content-validation/` | **CURRENT** |
| **2 — Manual Validation** | Operator checklist per page/block; YAML/markdown runs | Project logs, HITL evidence refs | **NEXT** (human-operated) |
| **3 — Semi-Automatic** | Import stack + emit contract-shaped diff; human approves | Helper scripts (S5 boundary) | NOT STARTED |
| **4 — Automated** | CI/static analysis of architecture declarations | CVG-04, CVG-08 | NOT STARTED |
| **5 — Runtime** | CMS/build-time gates on publish | CVG-07 | NOT STARTED |

---

## Phase 1 — Documentation (v1 deliverable)

**Delivered:**

- CONTENT-VALIDATION-SYSTEM-v1
- CONTENT-VALIDATION-CONTRACT-v1
- CONTENT-VALIDATION-RULES-v1
- CONTENT-SIGNAL-VALIDATION-MATRIX-v1
- CONTENT-FAILURE-LIBRARY-v1
- CONTENT-SEVERITY-SYSTEM-v1
- CONTENT-VALIDATION-GAPS-v1
- CONTENT-VALIDATION-ROADMAP-v1 (this doc)

**Gate:** Operator acceptance of v1 docs. No runtime claimed.

---

## Phase 2 — Manual Validation

**Goal:** Repeatable operator runs using contract fields on real projects (e.g. Triumph pilot patterns).

**Activities:**

1. Attach content validation run to page-block validation PASS record.
2. Per REQUIRED block — fill `required_signals` / `missing_signals` / `status`.
3. Page-level run for PAGE-CONTENT-CONTRACTS.
4. Log FAIL → CVF id from failure library.

**Not in scope:** Auto-fill copy, generation.

**Exit criteria (documentation):** ≥1 pilot project with archived validation runs — **FUTURE evidence**.

---

## Phase 3 — Semi-Automatic

**Goal:** Reduce transcription error; human remains authority.

**Candidate capabilities (see CVG-09):**

- Parse declared block stack → pre-fill `required_signals`
- Diff architecture doc vs matrix → highlight missing R / present F
- Export PASS/FAIL summary for HITL sign-off

**Boundary:** [governance/operational-tooling-overview.md](../../governance/operational-tooling-overview.md) — helpers assist; do not auto-approve.

---

## Phase 4 — Automated

**Goal:** CI or pre-commit checks on **architecture artefacts** (not live site HTML).

**Depends on:** CVG-08 schema; stable project IA export format — **UNKNOWN format**.

**Not in scope for Phase 4:** LLM copy judging, fact checking (→ CVG-01, CVG-02).

---

## Phase 5 — Runtime

**Goal:** Publish-time gate in CMS or static build.

**Depends on:** Frontend slot model, Generation Contracts, evidence store — **multiple UNKNOWNs**.

**Warning:** Do not claim Phase 5 exists from documentation alone.

---

## Relationship to Page Block Validation roadmap

| Layer | Maturity today | Next step |
|-------|----------------|-----------|
| Page → Block Validation | Documentation + manual (ACCEPTED) | Semi-automatic (shared VALIDATION-ROADMAP) |
| Content Validation | Documentation (v1) | Manual validation pilots |

Content Validation **follows** Page Block Validation in pipeline; never replaces it.

---

## Relationship to Generation Contracts

Generation Contracts (**NOT QUEUED**) sit **between** Content Validation documentation and generated-text validation (CVG-01). Sequence:

```text
Content Contracts (ACCEPTED)
        ↓
Content Validation v1 (documentation → manual)
        ↓
Generation Contracts (future charter)
        ↓
Generated text validation (CVG-01)
```

---

## SAFE UNKNOWN

- Calendar dates per phase — **not in this document**
- CI vendor/tooling — **UNKNOWN**
- Operator acceptance criteria for leaving Phase 1 — **operator decision**

---

*Content Validation Roadmap version: v1.*
