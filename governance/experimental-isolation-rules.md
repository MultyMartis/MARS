# MARS — Experimental isolation rules

**Status:** **documented** — governance-only, **Phase S7**. **Not** filesystem enforcement, **not** sandbox automation.

**Purpose:** Reduce **experimental chaos**: keep spikes, pilots, and sketches from masquerading as stable layers, governance core, or product runtime.

---

## 1. Separation from governance core

- **Core** rows in `governance/README.md` and SoT docs ([registry-source-of-truth.md](registry-source-of-truth.md)) change through **editorial** stabilization—[experiment-to-pattern-transition.md](experiment-to-pattern-transition.md)—not via adjacent draft files “leaking” authority.  
- Draft governance experiments should avoid contradicting canonical sections without a visible **experimental** banner or sibling doc until reviewed.

---

## 2. Lane discipline

- Respect **execution boundaries**—[execution-boundary-clarification.md](execution-boundary-clarification.md).  
- Do not use experimental helpers to mutate unrelated lanes (e.g. Website Factory production narratives) without explicit scope—user policy may forbid entirely; this doc states **governance intent**: experiments stay in declared lanes.  
- Cross-lane artifacts must declare **both** source and target lanes in headers or REPORTs.

---

## 3. Runtime-scoped experimental handling

- Code under runtime-scoped or demo paths must carry **lifecycle** honesty—[artifact-lifecycle-rules.md](artifact-lifecycle-rules.md).  
- README and scripts must **not** imply “this is how MARS runs in production” unless evidenced and scoped per [AGENTS.md](../AGENTS.md).

---

## 4. Local-only handling

- Prefer explicit **local** / **dev-only** notes in README snippets for experiments—[lightweight-script-guidelines.md](lightweight-script-guidelines.md).  
- Secrets, machine paths, and one-off env vars belong in operator notes, **not** implied as repo-default behavior.

---

## 5. Naming expectations

- Avoid names that sound productized (`core-runtime`, `orchestrator`, `control-plane`) for experimental trees unless the name is **clearly** historical or quoted as external—[identity-and-naming-rules.md](identity-and-naming-rules.md).  
- Prefer prefixes/suffixes like `experiment-`, `pilot-`, `draft-`, or explicit `experimental` lifecycle tag in doc front-matter if used.

---

## 6. Visibility requirements

- **How to run**, **what it touches**, and **what it does not** prove must be visible in-repo or linked REPORT.  
- Hidden entrypoints (undocumented npm scripts, magic env toggles) increase **hidden-runtime** risk—[tooling-escalation-warnings.md](tooling-escalation-warnings.md).

---

## 7. Explicit experimental labeling

Docs, scripts, and adapters that are not stabilized must be labeled **experimental** (wording or lifecycle) so readers do not merge them mentally with canonical architecture—[experimental-tooling-status.md](experimental-tooling-status.md).

---

## 8. SAFE UNKNOWN

If labeling and lane ownership are missing, treat the artifact as **high governance-risk** and **high runtime-risk** until clarified—[experiment-classification.md](experiment-classification.md).
