# MARS — Experimental tooling status rules

**Status:** **documented** — governance-only, **Phase S5**. **Not** a registry of every script; **not** automated classification.

**Purpose:** Clarify **how to describe** utilities so readers do not confuse **experimental helpers** with **MARS runtime capability**.

---

## 1. Core rule

**Experimental tooling ≠ MARS runtime capability.**

Presence of a script, adapter, or local utility in the repository is **evidence of files**, not evidence of a **deployed** operational platform, orchestration layer, or autonomous system. See [AGENTS.md](../AGENTS.md).

---

## 2. Status labels (documentation vocabulary)

| Label | Meaning |
|-------|---------|
| **Draft utility** | Early sketch; behavior or scope may change; not relied upon for governance truth. |
| **Experimental helper** | Narrow, may break; for demos or operator experiments; must not silently update SoT. |
| **Local-only tool** | Expected to run on a developer machine; not a shared “service level” commitment. |
| **Operator utility** | Explicitly for human operators; invoked manually; outputs reviewed before commit. |
| **Narrow validator** | Checks one concern (e.g. links, phrases); **read/report**; human triages results. |
| **Operationally verified** | A human has **run** it for a defined scenario and recorded outcome (e.g. in a REPORT or runbook note). **Not** continuous verification unless separately stated and evidenced. |
| **Governance-only helper** | Aids drafting or checking **markdown governance**; **does not** execute product workflows. |
| **Deprecated utility** | Kept for history or migration; **do not** extend; prefer replacement or removal per task scope. |

---

## 3. What labels do **not** imply

- **Not** “approved for production deployment.”  
- **Not** “enforced repo-wide” unless a **separate** human process (e.g. CI) exists and is documented as such — [validation-chain-semantics.md](validation-chain-semantics.md).  
- **Not** upgrade of **registry** or **execution** semantics without explicit human edits to authoritative docs — [registry-source-of-truth.md](registry-source-of-truth.md).

---

## 4. SAFE UNKNOWN

**Pilot reference:** [`tools/governance-scanner/`](../tools/governance-scanner/) — local-only phrase scan; see its README (**not** runtime capability, **not** enforcement).

If a utility has **no** stated status in README, header comment, or nearby doc, default to **experimental / unclassified** for **reader caution**, not “runtime feature.”
