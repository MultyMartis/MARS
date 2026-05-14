# MARS — Task envelope standard

**Status:** **documented** — governance-only, **Phase S4**. **Lightweight** canonical **shape** for how to **think** and **write** about a task handoff. **No** mandated JSON Schema, **no** API, **no** persistence format.

**Purpose:** Reduce **task envelope inconsistency** and **adapter-vs-system** confusion by separating **governance contract**, **runtime payload** (if any, **future**), **human instructions**, and **external workflow payloads**.

---

## 1. Envelope vs other bundles

| Kind | Definition | Typical carrier |
|------|------------|-----------------|
| **Governance contract** | This envelope: scope, lane, risks, validation **expectations**, exclusions—**human-readable** discipline. | Chat preamble, REPORT, governance notes, runbook steps. |
| **Runtime payload** | **Planned** / **experimental** structured object for a **future** or **narrow** runtime—**only** when files in-repo prove that path applies to **this** task. | **SAFE UNKNOWN** as universal default for “MARS runtime task object.” |
| **Human instructions** | Natural-language **prompt** to an operator or editor agent: do X in paths Y, do not touch Z. | Cursor prompt, Web-GPT pack output, email. |
| **External workflow payloads** | Bodies produced/consumed by **non-MARS** systems (e.g. automation platforms, ticketing). May **mirror** envelope fields; **not** automatically SoT for MARS governance. | Webhook JSON, third-party forms. |

**Rule:** Do **not** treat an external JSON blob or a **planned** task schema row as proof that **MARS** executed or validated anything—verify layer per [validation-chain-semantics.md](validation-chain-semantics.md).

---

## 2. Recommended envelope fields (conceptual)

Operators should be able to answer these **without** a heavy template file:

| Field | Meaning |
|-------|---------|
| **Task identity** | Stable **human-usable** label (e.g. “S4 governance: execution contracts”) + optional link to lifecycle/registry row. **Not** a claim of global UUID service. |
| **Scope** | **In** / **out**: paths, projects, doc sets—align [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) **lane**. |
| **Lane** | **Production execution** vs **MARS core** (or explicit bridge) per parallel-chat doc. |
| **Constraints** | Timebox, “no commit,” no `workspaces/*`, no `mars-runtime/` unless stated, locale, secrecy, tooling limits. |
| **Execution mode** | e.g. **documentation-only**, **doc + narrow script**, **read-only audit**—explicitly **not** “autonomous agent run” unless proven. |
| **Validation expectations** | **Which** validation **meanings** apply (human review, checklist, governance read)—not “CI green = MARS validated” by default. |
| **Outputs** | Expected **artifacts** and **states** (see [artifact-lifecycle-rules.md](artifact-lifecycle-rules.md)). |
| **Exclusions** | Forbidden paths or work types to prevent **scope creep** and lane bleed. |
| **Risks** | **SECURITY RISK**, integration touch, PII, production—per [risk-register.md](risk-register.md) posture when relevant. |
| **SAFE UNKNOWN expectations** | What is **unknown**, who may resolve, whether work may proceed under bounded ambiguity. |

Optional cross-reference: design-heavy field list in [../workflows/task-contract-v0.md](../workflows/task-contract-v0.md) (**planned** control-plane shape)—use for **alignment**, not as proof of runtime.

---

## 3. Minimal one-paragraph envelope (example pattern)

Use plain prose; adapt per task:

> **Identity:** … **Lane / scope:** MARS core; `governance/*` only; out: `workspaces/*`, `mars-runtime/*`. **Mode:** documentation-only. **Validation:** human review + governance consistency; no automated MARS validator claimed. **Outputs:** new/edited `.md` under `governance/`, README index row. **Exclusions:** no factory expansion beyond links. **Risks:** none / list. **UNKNOWN:** …

This pattern is **documentation**; it is **not** a wire format.

---

## 4. Anti-patterns

- **Silent conflation:** “Task object in doc” = “task running in runtime.”  
- **Envelope sprawl:** mandatory giant forms for tiny edits—prefer [documentation-entropy-rules.md](documentation-entropy-rules.md).  
- **Registry as executor:** updating `registry.md` does **not** execute work.

---

## 5. SAFE UNKNOWN

- Whether your program will adopt a **machine-readable** envelope file in-repo.  
- Exact field parity with any **external** ticket or automation schema.
