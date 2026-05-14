# MARS — Experiment to pattern transition

**Status:** **documented** — governance-only, **Phase S7**. **Not** an automated promotion pipeline, **not** CI gates.

**Purpose:** Define how experiments **may** become **stabilized operational patterns** (documentation, helpers, or procedures) **without** auto-promotion or silent canonization.

---

## 1. Principle: no auto-promote

Experiments **do not** become canonical because:

- they exist in the repo;  
- they ran successfully once;  
- adjacent docs mention them;  
- a helper “feels” official.

Promotion is a **deliberate human** sequence with explicit artifacts—see §2.

---

## 2. Stabilization requirements (checklist)

| Requirement | Notes |
|-------------|--------|
| **Repeatability** | At least **two** independent reruns **or** two operators **or** one rerun plus documented equivalence rationale—limits and env captured per [experiment-evidence-rules.md](experiment-evidence-rules.md). |
| **Governance review** | Conflicts with SoT, terminology, and registry rules resolved—[registry-source-of-truth.md](registry-source-of-truth.md), [identity-and-naming-rules.md](identity-and-naming-rules.md). |
| **Naming normalization** | Remove misleading “core/runtime/production” language unless separately true per [AGENTS.md](../AGENTS.md). |
| **Documentation cleanup** | Merge or supersede draft pages; update indices—[documentation-entropy-rules.md](documentation-entropy-rules.md), `governance/README.md` if the pattern is governance-facing. |
| **Boundary restatement** | Re-affirm what the pattern is **not** (orchestration, daemon, autonomous agent) if drift-prone—[tooling-boundary-rules.md](tooling-boundary-rules.md). |
| **Lifecycle labels** | Artifacts tagged draft → stabilized (or deprecated if failed)—[artifact-lifecycle-rules.md](artifact-lifecycle-rules.md). |

Skipping items defaults the item to **still experimental**.

---

## 3. Failed experiments

- **Deprecation:** Mark failed spikes clearly; archive or delete only per repo policy and explicit instruction—default: label **deprecated** / **historical** with pointer to lesson—[operational-lessons-and-postmortems.md](operational-lessons-and-postmortems.md).  
- **No shame narrative:** Failure is valid evidence; mythology is not.

---

## 4. Migration into canonical docs

When promoting:

1. Identify **single** canonical home (avoid duplicate truths).  
2. Move unique content; leave stubs with “see …” where history matters.  
3. Add **SAFE UNKNOWN** where evidence still gaps.  
4. Optional: lifecycle log entry for traceability—[logs/lifecycle-log.md](../logs/lifecycle-log.md) if project practice uses it.

---

## 5. What stays human-reviewed

- Meaning of “repeatable” for the specific domain.  
- Whether registry rows or capability language may change.  
- Security and external-system posture—[external-system-boundaries.md](external-system-boundaries.md).  
- Whether expansion should pause—[stabilization-vs-expansion.md](stabilization-vs-expansion.md).

---

## 6. SAFE UNKNOWN

If repeatability or governance impact is unclear, the artifact remains **experimental** until resolved—**SAFE UNKNOWN** is preferable to silent promotion.
