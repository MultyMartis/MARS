# MARS Search PPC Lifecycle — Repair Roadmap v1

**Date:** 2026-06-22  
**Status:** `APPROVED — WAVE 1 CHECKPOINTED — WAVE 1.1 OPERATOR REVIEW`  
**Lifecycle authority:** `APPROVED — CHECKPOINTED` (`43c4271`)  
**Wave 1 runtime:** `CORE APPROVED — CHECKPOINTED` (`2b3020d`)  
**Wave 1.1:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`  
**Wave 2:** `BLOCKED PENDING WAVE 1.1 REVIEW`  
**Basis:** [MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md), [MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)  
**Corvonero default:** `FROZEN` — no Corvonero production work until Wave 3+ operator charter per item

---

## Wave overview

| Wave | Theme | Primary owner | Corvonero dependency |
|------|-------|---------------|----------------------|
| 1 | Lifecycle authority and state enforcement | MARS Search PPC / Operator | **CORE APPROVED — CHECKPOINTED** (`2b3020d`) |
| 1.1 | Entry-point wiring and bypass closure | MARS Search PPC / MIG / ORCA | **IMPLEMENTED — OPERATOR REVIEW REQUIRED** |
| 2 | MIG evidence production | MIG | **BLOCKED PENDING WAVE 1.1 REVIEW** |
| 3 | ORCA production semantic intelligence | ORCA Semantic Intelligence | Frozen until operator approves lifecycle + Wave 3 charter |
| 4 | Analytical pack and AI PPC Strategist | Cross-system + Strategist role | Frozen |
| 5 | Campaign production and QA | Campaign Production / ORCA | Frozen |
| 6 | Commander and launch | Commander Export + Operator | Frozen |
| 7 | Post-launch learning | Post-Launch Learning | Requires launched reference project (not Corvonero) |

---

## Wave 1 — Lifecycle Authority and State Enforcement

**Goal:** Operator-approved canonical lifecycle is enforceable at task boundaries.

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W1-01 | Lifecycle PROPOSED | Operator APPROVED status on lifecycle + contract | Operator | Gap audit review | Operator signs [decision record](../decisions/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md) | Decision record status = APPROVED | P0 | None |
| W1-02 | Validator opt-in only | Validator invoked in Cursor/Web-GPT task templates by default | MARS Search PPC | W1-01 | Update operational indexes; add validation step to subsystem READMEs | Task reports include validator output | P0 | None |
| W1-03 | No real project manifests | First empty manifest template instantiated per new PPC project | Operator / ATLAS | W1-01 | Copy `project-ppc-state-manifest-template-v1.json` to project locus | Validator runs clean at SPPC-01 NOT STARTED | P1 | None |
| W1-04 | Subsystems ignore manifest | Manifest path flag on MIG/ORCA/Campaign entry CLIs | MARS + ORCA + MIG | W1-02 | Add `--manifest` optional then required on production commands | CLI exits 2 when lifecycle BLOCKED | P0 | None |
| W1-05 | Web-GPT discipline-only | Sync pack addendum referencing execution contract | Web-GPT maintainer | W1-01 | Publish sync pack delta | Opening status block in pilot chat | P1 | None |
| W1-06 | Cursor starter exists | All PPC Cursor tasks use starter template | Operator | W1-02 | Enforce in AGENTS.md cross-reference | Sample task obeys template | P2 | None |

**Wave 1 exit criteria:** Lifecycle operator-approved; validator mandatory at task boundary; at least one non-synthetic manifest exists.

---

## Wave 2 — MIG Evidence Production

**Goal:** MIG produces SPPC-02, 03, 10, 11 artifacts with dated provenance.

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W2-01 | Source registry partial | `source_registry` JSON schema + writer aligned to SPPC-02 | MIG | W1-01 | Extend `MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1` | Registry validates; dates mandatory | P0 | Read-only ledger replay OK |
| W2-02 | No full-corpus guard | Intake artifact proves row count matches source registry | MIG | W2-01 | Corpus intake validator script | Rejects 200-row pilot as production corpus | P0 | Use Corvonero corpus counts as test vectors only |
| W2-03 | **PAID SERP mode MISSING** | MIG mode `PAID SERP — BUSINESS HOURS` with time passport | MIG | W2-01 | New contract + collection runbook | Evidence JSON includes local time, weekday, device | P0 | **Do not collect for Corvonero until unfrozen** |
| W2-04 | Competitor audit partial | `competitor_advertising_audit` pack schema | MIG | W2-03 | Extend competitor discovery contract v0 → v1 | Pack validates against lifecycle artifact type | P1 | None |
| W2-05 | Handoff human-only | Machine handoff bundle MIG → ORCA for SPPC-03/04 | MIG + ORCA | W2-02 | Version `mig-orca-handoff-contract-v0` → v1 | End-to-end fixture handoff | P1 | Read-only |

**Wave 2 exit criteria:** SPPC-10 artifact producible; source date passport enforced; corpus guard rejects pilot substitution.

---

## Wave 3 — ORCA Production Semantic Intelligence

**Goal:** Full-corpus SPPC-04–09 with automated ABSTAIN ladder.

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W3-01 | Admission runtime 200-phrase pilot | Full-corpus admission batch path | ORCA SI | W2-05, W1-04 | Extend `orca-admission.mjs` batch mode | Corvonero-scale dry run (read-only) | P0 | **Operator charter required to process Corvonero corpus** |
| W3-02 | T1–T5 documented only | `demand_tier_registry` producer | ORCA SI | W3-01 | Tier assignment module | Rejects frequency-only rationale | P0 | Frozen until W3-01 charter |
| W3-03 | Ownership partial | `service_ownership_registry` after ACCEPT only | ORCA SI | W3-01 | Enforce int-neg-007 in production path | Integration tests | P0 | Frozen |
| W3-04 | Clustering missing | `semantic_cluster_registry` producer | ORCA SI | W3-03 | Clustering module per SPPC-08 | Cluster QA fixtures | P1 | Frozen |
| W3-05 | Negatives partial | `negative_intelligence_pack` with conflict detection | ORCA SI | W3-04 | Negative intelligence module | Cross-negative blocks export flag | P1 | Frozen |
| W3-06 | I-09 deferred | Automated reassessment + adjudication for ABSTAIN | ORCA SI | W3-01 | Implement escalation ladder | ABSTAIN rate bounded; human queue shrinking | P1 | Frozen |
| W3-07 | P0-I pilot diagnostic | Pilot remains labeled diagnostic only | Operator | W1-01 | Keep reclassification decision visible | No production claims from pilot | P0 | None |

**Wave 3 exit criteria:** Full Corvonero corpus processable under charter OR second project pilot; tiers/ownership/clusters/negatives artifacts emitted.

---

## Wave 4 — Analytical Pack and AI PPC Strategist

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W4-01 | No pack assembler | `dated_analytical_pack` human + machine views | Cross-system (ORCA lead) | W2-03, W3-05 | Pack builder script | Completeness gate blocks SPPC-13 | P0 | Frozen |
| W4-02 | Strategist chat-local | `ppc_strategy_decision_record` schema with evidence pointers | AI PPC Strategist | W4-01 | Strategy record template + validator | Competitor fields require MIG pointers | P0 | Frozen |
| W4-03 | Degraded SERP partial | Strategy records degradation impact | Strategist | W2-03 | Required fields in strategy schema | Validator checks degradation section | P1 | Frozen |

**Wave 4 exit criteria:** Pack + strategy artifacts validate; lifecycle allows SPPC-13 only with complete pack.

---

## Wave 5 — Campaign Production and QA

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W5-01 | Triumph-specific pipeline | Universal campaign architecture registry | Campaign Production | W4-02 | Generalize ORCA campaign contract consumer | Non-Triumph fixture | P0 | **BLOCKED — Corvonero campaign frozen** |
| W5-02 | Distribution partial | Keyword/negative distribution with conflict detection | Campaign Production | W5-01 | SPPC-15 producer | Duplicates/cross-campaign overlap flagged | P0 | Frozen |
| W5-03 | Ads partial | Ad production pack per SPPC-16 | Campaign Production | W5-02 | Ad generator discipline | No generic substitution templates | P1 | Frozen |
| W5-04 | Landing QA docs only | Landing alignment report per SPPC-17 | QA | W5-03 | Landing QA checklist tool | Outcomes READY / DO NOT LAUNCH | P1 | Frozen |
| W5-05 | Bidding branch partial | Manual + automated branches with analytics gate | Campaign Production | W5-04 | Bidding validator | Auto branch blocked without goals | P0 | Frozen |
| W5-06 | QA partial | `campaign_qa_report` with BLOCKER/MAJOR/MINOR | QA / Validators | W5-05 | QA runner integrating campaign + lifecycle contracts | Unresolved BLOCKER prevents export | P0 | Frozen |

**Wave 5 exit criteria:** SPPC-14–19 artifacts for a pilot project; QA blocks export on BLOCKER.

---

## Wave 6 — Commander and Launch

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W6-01 | Triumph export only | Lifecycle-gated Commander export CLI | Commander Export | W5-06 | Bind exporter to manifest + QA artifact | Parity diff vs production SoT | P0 | **Frozen — no Corvonero XLSX** |
| W6-02 | Dry run docs | Operator approval package SPPC-21 | Operator | W6-01 | Approval bundle generator | Campaign-level approval recorded | P1 | Frozen |
| W6-03 | Launch inferred risk | Import + launch evidence separate from export | Operator / Platform | W6-02 | SPPC-22 checklist | `launch_evidence_pack` without export alone | P0 | Frozen |
| W6-04 | Triumph duplication | Document Triumph as reference implementation, not universal | ORCA | W6-01 | Operational index labels | Second project reuses path | P2 | None |

**Wave 6 exit criteria:** Export requires SPPC-19; launch requires SPPC-21 approval; Triumph path generalized or explicitly scoped.

---

## Wave 7 — Post-Launch Learning

| ID | Current state | Required result | Owner | Dependencies | Implementation task | Validation | Priority | Corvonero dependency |
|----|---------------|-----------------|-------|--------------|---------------------|------------|----------|----------------------|
| W7-01 | SPPC-23 missing | `post_launch_learning_log` producer | Post-Launch Learning | W6-03 | Learning log schema + intake | No direct SoT mutation | P1 | Requires **launched** reference project (Triumph or future) |
| W7-02 | Silent core mutation risk | Governed proposal queue for tier/cluster/negative changes | ORCA SI + Operator | W7-01 | Proposal workflow | Proposals versioned; approved changes reopen stages | P0 | Frozen until launch exists |
| W7-03 | Search term feedback | Search-term evidence ingestion | MIG / Platform | W7-01 | Import discipline doc | Proposals cite search-term evidence | P2 | N/A |

**Wave 7 exit criteria:** Post-launch proposals cannot mutate Semantic Core without operator approval and stage reopen.

---

## Recommended execution order

```text
Wave 1 (approve + enforce)
  → Wave 2 (MIG evidence — especially SPPC-10)
    → Wave 3 (ORCA full semantic — Corvonero charter gate)
      → Wave 4 (pack + strategist)
        → Wave 5 (campaign + QA)
          → Wave 6 (Commander + launch)
            → Wave 7 (learning)
```

**Parallel allowed:** W1-05/06 while W2 contracts draft; Triumph documentation (W6-04) anytime.

---

## Corvonero unfreeze gate

Corvonero may resume **only** when **all** are true:

1. Operator approves lifecycle (W1-01).
2. Wave 2 corpus + SERP evidence modes exist.
3. Wave 3 operator charter issued for full-corpus semantic processing.
4. Bypass audit items #7, #10, #18 have repairs deployed or waived with documented risk.

Until then: **FROZEN PENDING SEARCH PPC PRODUCTION LIFECYCLE IMPLEMENTATION AND GAP CLOSURE**.

---

## Related artifacts

- Gap audit: [../reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)
- Bypass audit: [../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](../reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)
- Operator decision: [../decisions/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md](../decisions/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md)
