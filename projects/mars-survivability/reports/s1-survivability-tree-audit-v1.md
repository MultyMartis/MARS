# S1 Survivability Tree Audit (v1)

**Status:** Human-reviewed audit — documentation only  
**Date:** 2026-05-24  
**Scope:** Full tree under `projects/mars-survivability/`  
**Phase:** S1 stabilization — drift identification, not feature expansion

---

## 1. Executive summary

The survivability tree is **structurally complete** for G0–G4 with drill evidence (D-01/D-02). Primary issues are **semantic drift** (stale phase status in GitGuard docs), **dual taxonomies** (R1–R4 vs SAFE–FORBIDDEN), **pre-drill scorecard staleness**, and **minor tooling friction** documented in D-01. No missing core files; no broken internal links found in index targets.

**Verdict:** Fit for **S1 baseline freeze** after targeted corrections applied in this checkpoint.

---

## 2. Inventory summary

| Area | Files (approx) | Status |
|------|----------------|--------|
| contracts/ | 8 (+ terminology freeze) | Complete |
| protocols/ | 11 | Complete |
| registries/ | 3 | Complete |
| guardrails/ | 3 | Complete |
| templates/ | 5 | Complete |
| reports/ | 7 pre-S1 + 6 S1 | Complete |
| tools/validator/ | CLI + rules + examples | Implemented |
| tools/helpers/ | 2 CLI + 4 doc advisors | Implemented |
| tools/observability/ | 4 CLI + schema + procedure | Implemented |

**Infrastructure (outside tree, referenced):** `workspaces/_snapshots|_sandbox|_quarantine|_recovery/` — README present; drill artifacts from D-01/D-02 exist.

---

## 3. Duplicated semantics

| Topic | Locations | Severity | Resolution |
|-------|-----------|----------|------------|
| FORBIDDEN ops | destructive-operations-policy, agent-operation-risk-classes, enforcement-rules-registry, validator JSON | Low — intentional cross-ref | Keep; registry is catalogue; policy is normative |
| GitGuard definition | gitguard-system-entry, gitguard-advisory-layer, gitguard-evolution, gitguard-tooling-map | Low | S1 positioning review consolidates; phase table corrected |
| Snapshot requirement | risk-classes, enforcement-registry, snapshot-standard, preflight checklist | Low — aligned | No change |
| Observability ≠ control | observability-philosophy, operational-log-format, gitguard-advisory-layer | Low — reinforcing | No change |
| Risk taxonomy **R3/R4** vs **SAFE–FORBIDDEN** | safe-execution-layer vs agent-operation-risk-classes | **Medium** | Terminology freeze: prefer SAFE–FORBIDDEN for new material; R3/R4 retained only in safe-execution-layer git/FS tiers |

---

## 4. Stale references (corrected in S1)

| File | Issue | S1 action |
|------|-------|-----------|
| `registries/gitguard-system-entry-v1.md` | G2/G3 marked **Planned** while implemented | **Fixed** — G2/G3 Done; G3+ hooks Planned |
| `contracts/gitguard-survivability-evolution-v1.md` | Same phase table drift | **Fixed** |
| `contracts/gitguard-advisory-layer-v1.md` | G4 tools listed as Planned | **Fixed** — Done (G4) |
| `README.md` | "G0–G1 ops" only | **Fixed** — G0–G4 + QUICKSTART |
| `reports/mars-survivability-scorecard-v1.md` | Pre-G0/G1/D-01 baseline (2026-05-23) | **Flagged** — historical; superseded by D-02 readiness + S1 maturity review |
| `protocols/safe-execution-layer-v1.md` | Mermaid "Planned helper layer" | **Flagged** — cosmetic; helpers now exist; defer diagram update to avoid scope creep |

---

## 5. Broken links

| Reference | Result |
|-----------|--------|
| OPERATIONAL-INDEX → `workspaces/_*/README.md` | **Valid** — files exist on disk |
| OPERATIONAL-INDEX → governance / AGENTS / tool-safety-model | **Valid** |
| All protocol/contract cross-links sampled | **Valid** |
| `projects/gitguard/` future paths in evolution doc | **Intentional future** — labeled design-only |

**No broken links requiring immediate fix.**

---

## 6. Inconsistent terminology

| Issue | Example | Mitigation |
|-------|---------|------------|
| "GitGuard blocked/recovered" vs advisory | evolution doc sequence diagram labels "GitGuard helper" | Use "advisory tooling recommended"; human executes — terminology freeze |
| Self-healing as **non-goal** vs phrase in rollback-advisor comparison table | rollback-advisor § comparison | Acceptable — listed as anti-pattern |
| Scorecard "HIGH RISK" domain rating vs risk-class "HIGH RISK" | scorecard vs agent-operation-risk-classes | Different domains — scorecard = posture; classes = operation — note in maturity review |

---

## 7. Unfinished placeholders

| Location | Type | Acceptable? |
|----------|------|-------------|
| snapshot-manifest-template FILL fields | Operator fill-in | **Yes** — by design |
| snapshot-helper manifest draft | FILL placeholders | **Yes** — D-01 validated |
| gitguard-survivability-evolution `projects/gitguard/rollback-map.json` | Future schema | **Yes** — labeled future |
| G5+ items in OPERATIONAL-INDEX | Planned charter | **Yes** — SAFE UNKNOWN |

---

## 8. Overlapping docs

| Cluster | Overlap | Recommendation |
|---------|---------|----------------|
| diff-advisor + diff-advisor-workflow | Workflow extends advisor | Keep both — advisor = principles; workflow = steps |
| gitguard-tooling-map + gitguard-advisory-layer | Tooling vs framework | Keep — map is inventory; layer is positioning |
| preflight + pre-execution-check-assistant | Both pre-agent | Keep — checklist template vs CLI-oriented short list |
| D-02 readiness + d02-human-operated-restore-review | Readiness vs narrative | Keep — different audiences |

**No merge required for S1.**

---

## 9. Naming drift

| Pattern | Observation |
|---------|-------------|
| File suffix `-v1` | Consistent across tree |
| Report ids D-01/D-02 vs filenames d01/d02 | Consistent lowercase in paths |
| snap-* snapshot ids | Consistent in D-01 logs |
| Lane B labeling | Consistent in README, OPERATIONAL-INDEX, drills |

---

## 10. Risk class consistency

| Source | Classes | Aligned? |
|--------|---------|----------|
| agent-operation-risk-classes-v1.md | SAFE → FORBIDDEN | Canonical |
| enforcement-rules-registry-v1.md | MEDIUM+ snapshot triggers | **Yes** |
| snapshot-helper-v1.mjs | Maps to same labels | **Yes** — minor gap: HIGH not elevating rollbackImportance (D-01 FP) |
| validator-rules-registry-v1.json | DENY patterns for F-01–F-14 equivalents | **Yes** |
| safe-execution-layer R3/R4 | Parallel git/FS tier | Document legacy; terminology freeze clarifies |

---

## 11. Validator wording consistency

| Aspect | Status |
|--------|--------|
| Output enum ALLOW / DENY / NEED_HUMAN | Consistent across architecture, report format, CLI |
| SAFE UNKNOWN in reports | Consistent — deny default |
| NEED_HUMAN vs NEED HUMAN APPROVAL | Minor spacing variance in guardrails vs validator | Low — both mean halt for human |

---

## 12. Known friction (from D-01, not regressions)

| ID | Component | Issue |
|----|-----------|-------|
| FP-01 | Validator | Sandbox write → NEED_HUMAN |
| FP-S01 | Scope analyzer | Sandbox → PROTECTED-ZONE-HIT label noise |
| FP-O01 | Integrity checker | Absolute Windows path handling |
| RD-030 | Registry drift linter | Pre-existing doc/rule mismatch |

---

## 13. Recommendations (S1 applied vs deferred)

| Action | Status |
|--------|--------|
| Fix GitGuard phase tables | **Applied** |
| Harden OPERATIONAL-INDEX | **Applied** |
| Create terminology freeze | **Applied** |
| Create QUICKSTART | **Applied** |
| Link from governance/operational-survivability.md | **Applied** |
| Update scorecard post-D-02 | **Deferred** — keep as historical 2026-05-23 baseline |
| Fix safe-execution-layer mermaid | **Deferred** — cosmetic |
| Sandbox Q-tier SAFE label in scope-analyzer | **Deferred** — G5 charter |
| registry JSON auto-sync | **Deferred** — explicitly not automated |

---

## 14. SAFE UNKNOWN

- Long-term retention policy for drill artifacts in `_snapshots/` and `_quarantine/`
- Operator sign-off on S1 baseline
- Whether Website Factory OPERATIONAL-INDEX should link survivability pack (see ecosystem integration review)

---

*End of S1 Survivability Tree Audit v1.*
