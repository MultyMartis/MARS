# MARS — Validation chain semantics

**Status:** **documented** — governance-only, **Phase S4**. Clarifies **meaning** of “validation” **in documentation and human process**. **Not** a shipped validator product, **not** repo-wide automated enforcement.

**Purpose:** Reduce **validation-chain ambiguity** and the risk that a **mention** of validation is read as “**automated** validation **exists**.”

---

## 1. Core rule (normative for honesty)

**Validation mention ≠ automated validation exists.**

Whenever a doc, task, or checklist says “validate,” **name the layer**: human, checklist, governance read, external system, experimental script, or **planned** runtime hook. Default for MARS-wide claims: **human** or **governance** unless evidence exists.

---

## 2. Validation kinds (semantic)

| Kind | Meaning | Automation claim |
|------|---------|------------------|
| **Human review** | A person reads diffs/docs and accepts risk. | **None** implied. |
| **Checklist validation** | Structured manual steps (merge checklist, release checklist). | **None** unless a **named** tool runs the checklist—then say **which** tool. |
| **Runtime validation** | **Future** or **narrow in-tree** behavior that executes checks as code in a **proven** path. | **Only** if files/runtime behavior demonstrate it **for that path**; else **SAFE UNKNOWN** or “planned.” |
| **Experimental validation** | Ad-hoc or demo scripts (e.g. under `mars-runtime/` experiments). | **Local / narrow**; **not** “MARS validates everything.” |
| **External-system validation** | CI, linter, vendor dashboard, deployment gate **outside** MARS governance semantics. | **Third-party**; do not conflate with “MARS Control Plane validated.” |
| **Governance validation** | Consistency pass: terminology, SoT links, forbidden-claim cues—[enforcement/](enforcement/README.md) is **documentation aids only**. | **Not** automated policy engine. |
| **Operational verification** | “We ran the build / smoke / manual test **for this task scope**.” | States **what** was run; **no** universal MARS harness implied. |
| **SAFE UNKNOWN outcomes** | Acceptance criteria cannot be met because evidence is missing; proceed only if policy allows bounded ambiguity—[AGENTS.md](../AGENTS.md), [system-signals-dictionary.md](system-signals-dictionary.md). | **Explicit** human acknowledgment. |

---

## 3. Chains, not magic pipelines

A **validation chain** is an **ordered narrative** of what must be true before the next step—**for example**: “author self-review → second human → optional CI.” Chains are **descriptive** unless a **specific** automation is **proven**.

- **Do not** imply a single global chain covers all MARS tasks.  
- **Do not** treat **green CI** as governance validation unless the task says so **and** CI scope matches governance scope.

---

## 4. Relation to task envelope

Task envelopes should state **validation expectations** per [task-envelope-standard.md](task-envelope-standard.md)—especially when **SECURITY RISK** or production lanes are nearby.

---

## 5. SAFE UNKNOWN

- Whether a **future** MARS runtime will unify these kinds under one signal bus.  
- Exact mapping from external CI job names to MARS **task ids**—unless documented case-by-case.
