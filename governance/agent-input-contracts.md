# MARS — Agent input contracts (governance)

**Status:** **documented** — governance semantics only. **Not** runtime code, **not** orchestration, **not** agent-to-agent messaging, **not** queues or event buses.

**Purpose:** Establish **explicit input/output contracts** for MARS **agents and agent-shaped workflows** so operators and contributors do not rely on hidden assumptions, implicit context, or “autonomous coordination” narratives.

**Version:** v0.

---

## 1. No runtime assumption

MARS governance and Website Factory describe **document-driven, human-supervised** work. Execution today aligns with [execution-model.md](execution-model.md) and [AGENTS.md](../AGENTS.md): **human-orchestrated pipelines**, not an in-repo autonomous MARS process.

An **agent input contract** is a **governance artifact**: something humans fill, review, and attach to a role or lane. It does **not** imply enforcement by a scheduler, dispatcher, or inter-agent protocol.

---

## 2. Definition

An **agent input contract** declares, for a named agent or workflow slice:

| Facet | Meaning |
|-------|---------|
| **Required inputs** | Must be present **before** implementation or downstream claims of “done.” Absence → [§3](#3-missing-inputs--safe-unknown). |
| **Optional inputs** | Improve quality or speed; absence must **not** be silently invented. |
| **Forbidden inputs** | Must **not** be used as authority (e.g. deprecated exports, wrong semantic generation). Using them → **SAFE UNKNOWN** / quarantine / HITL per policy. |
| **Outputs** | Named artifacts and handoff shapes the role produces. |
| **Input validation** | Explicit **pre-flight check** (human or checklist): what was verified, what failed. |
| **SAFE UNKNOWN response** | What the role does when binding is missing or ambiguous (**stop**, report gaps, downgrade confidence)—never silent guessing. |
| **Quarantine conditions** | When output must **not** be treated as canonical (labels, paths, freeze rules). |

**Template:** [../templates/agent-input-contract-template.md](../templates/agent-input-contract-template.md).

---

## 3. Missing inputs → SAFE UNKNOWN

If **required** inputs are missing or invalid:

1. **Stop** proceeding as if context were complete.  
2. **Report** missing or invalid inputs (task REPORT, checklist, or contract section—per lane rules).  
3. **Downgrade confidence**; do not imply production-ready or frozen output.  
4. **Quarantine** output when policy requires (see template **Quarantine conditions**).

This aligns with **semantic source ambiguity** lessons: treat unresolved inputs as **governance risk**, not as a prompt to hallucinate structure or copy.

---

## 4. Contracts over autonomy

MARS prefers **explicit contracts** over hidden autonomy:

- Agents do **not** **call each other automatically**, route tasks automatically, build runtime queues, self-dispatch, or form orchestration loops—as **design posture** for governance and Website Factory lanes unless and until a **future**, **evidenced** implementation exists and is documented without exaggeration.

**Contrast:** [execution-contracts-overview.md](execution-contracts-overview.md) covers task-level execution semantics; **agent input contracts** specialize **per-role I/O and pre-flight validation** for agents and specialist packs.

---

## 5. Relation to other artifacts

| Artifact | Relationship |
|----------|----------------|
| [Agent card](../agents/agent-card-template.md) | Cards retain summary **`inputs`** / **`outputs`**; substantive I/O detail may live in a linked **agent input contract** (same repo path or project lane). |
| [Task contract v0](../workflows/task-contract-v0.md) | Task **`inputs`** / **`outputs`** bundle work-unit intent; agent contracts refine **what a specific role must receive** to execute safely. |
| [Task envelope standard](task-envelope-standard.md) | Lightweight envelope for human-operated handoff; agent contracts can be **referenced** from envelopes without becoming runtime payloads. |
| Website Factory | Frontend/handoff lanes should treat **handoff + semantic maps + exports** as contract-shaped inputs—see [§6](#6-website-factory-and-frontend-lanes). |

---

## 6. Website Factory and frontend lanes

Website Factory work should **name** required artifacts (e.g. visual exports, semantic section matrix, production rules) **before** implementation prompts. An agent input contract (or equivalent filled template) makes **input validation** visible:

- Example posture: **INPUT CHECK** — listed artifacts ✓/✗ → **STATUS: SAFE UNKNOWN** when required items are absent.
- **Canonical Design Implementation Pack** (per-version **`design/vN/`** semantics + implementation-pack + validation): bridges approved design → machine-readable locks; authoring role — [Design Governance Agent](../agents/design-governance-agent.md); architecture — [design-governance-layer.md](../projects/mars-website-factory/design-governance-layer.md), [canonical-implementation-pack-architecture.md](../projects/mars-website-factory/canonical-implementation-pack-architecture.md). **Governance documentation only** — not runtime enforcement.

This complements [frontend-handoff-contract-v0.md](../projects/mars-website-factory/frontend-handoff-contract-v0.md), [frontend-prompt-discipline-v0.md](../projects/mars-website-factory/frontend-prompt-discipline-v0.md), and foundation/overlay packs (`agents/frontend-gulp-agent/`, `agents/mars-forge/`).

---

## 7. Future-compatible note

A **future** runtime or orchestration layer **may** consume these contracts as metadata. Until then, contracts remain **governance-first**: human-readable, voluntarily maintained, **not** infrastructure.

---

## 8. SAFE UNKNOWN

- Exact **machine-readable** schema for contracts repo-wide.  
- Whether every registry agent will have a standalone contract file vs. inlined card sections.  
- Automated validation hooks (none asserted here).

---

## 9. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial agent input contracts governance layer and template link; §6 — **Canonical Design Implementation Pack** + [Design Governance Agent](../agents/design-governance-agent.md) cross-reference (**governance docs only**). |
