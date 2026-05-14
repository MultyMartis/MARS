# Operational helper maturity review (PILOT 01 & 02)

**Status:** governance / operations documentation — **human review artifact**, **not** automated scoring, **not** enforcement.

**Scope:** [`governance-scanner/`](governance-scanner/README.md), [`registry-checker/`](registry-checker/README.md).

**Maturity vocabulary:** [operationalization-maturity-levels.md](../governance/operationalization-maturity-levels.md) (Phase S6).

---

## PILOT 01 — `governance-scanner`

| Dimension | Assessment |
|-----------|------------|
| **Helper type** | Governance-only, read-only **narrow validator** (phrase scan on Markdown) — [experimental-tooling-status.md](../governance/experimental-tooling-status.md) |
| **Current maturity (S6)** | **Locally executable.** **Operator-verified** is **SAFE UNKNOWN** repo-wide (no single mandated log of every operator run). Repeatability toward **operationally repeatable** would require a short runbook + dated human verification notes per scenario. |
| **Explicit limitations** | Substring-only; no NLP; negation / “this is a quote” not modeled; docs that *define* forbidden wording may still *contain* it — expect noise. |
| **Known false positives** | Hits in `governance/enforcement/**` and similar where phrases are **intentionally** cited; table cells and examples; legitimate historical references. |
| **Governance risks** | **Over-trust:** treating stdout as proof of policy violation or as excuse to skip human reading — collides with [registry-source-of-truth.md](../governance/registry-source-of-truth.md) and [validation-chain-semantics.md](../governance/validation-chain-semantics.md). **Bypass risk:** “scanner green” used to justify edits without scope review. |
| **Runtime-risk level** | **Low** for product/runtime lanes if used only as documented (read-only, local, no daemon). Risk rises if wired into **mandatory** CI gates without governance agreement — then it behaves like **undeclared enforcement**. |
| **Operational usefulness** | Fast **triage** for suspicious wording themes aligned with [forbidden-runtime-claims.md](../governance/enforcement/forbidden-runtime-claims.md) and [tooling-boundary-rules.md](../governance/tooling-boundary-rules.md). |
| **Stabilization recommendation** | **Keep experimental.** Optional doc-only promotion: add a **minimal** runbook + “how to triage hits” in task notes — still **not** a platform. Do **not** rename as “governance validator product” or default-on CI without explicit human process. |
| **Remain experimental?** | **Yes** — until a **human** stabilization narrative (bounded scope, recorded verification, false-positive playbook) is explicitly adopted; even then it remains a **helper**, not SoT. |

---

## PILOT 02 — `registry-checker`

| Dimension | Assessment |
|-----------|------------|
| **Helper type** | Governance-only, read-only **local-only tool** + **narrow validator** (regex / file heuristics / duplicate hints). |
| **Current maturity (S6)** | **Locally executable.** Optional `--dry-run` supports configuration visibility. **Operator-verified** and **operationally repeatable** are **SAFE UNKNOWN** unless recorded per use case. |
| **Explicit limitations** | No completeness claim; weak Markdown semantics; cross-file duplicate hints may reflect **intentional** repetition (examples, mirrors, legacy packs). |
| **Known false positives** | “Missing SoT cue on same line” when cue is in adjacent prose; adapter paths flagged without context; duplicate backticks that are **not** registry drift. |
| **Governance risks** | **SoT confusion:** hints mistaken for authoritative registry reconciliation — contradicts [registry-source-of-truth.md](../governance/registry-source-of-truth.md). **Silent creep:** expanding `registry-rules.json` into a large undeclared policy set without review — [operationalization-drift-warnings.md](../governance/operationalization-drift-warnings.md). |
| **Runtime-risk level** | **Low** when confined to `governance/**` (or agreed roots) and read-only. **Medium** if `--scan-js-json` is run across large trees and output is misread as **proof** of adapter/runtime truth — runtime code does **not** override governance per [execution-boundary-clarification.md](../governance/execution-boundary-clarification.md). |
| **Operational usefulness** | Surfaces **candidates** for human registry / identity hygiene review; useful when paired with explicit triage time. |
| **Stabilization recommendation** | **Keep experimental.** If stabilized later, stabilize **documentation** first: rule purpose per row, known false positives, and “when not to run.” Avoid **sync** or **auto-fix** language. |
| **Remain experimental?** | **Yes** — heuristic hints must not become **de facto** enforcement or registry engine. |

---

## Cross-cutting conclusion

Both pilots sit at **locally executable** maturity with **experimental** posture. Neither is **operationally repeatable** as a **repo-wide** standard without explicit human runbooks and evidence. Neither constitutes **experimentally interoperable** or **runtime-scoped experimental** product claims — they are **governance-adjacent triage scripts**.

**Index:** [README.md](README.md) · **Lessons:** [helper-lessons-learned.md](helper-lessons-learned.md) · **Anti-drift rules:** [helper-stabilization-rules.md](helper-stabilization-rules.md)
