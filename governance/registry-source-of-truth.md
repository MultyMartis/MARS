# MARS — Registry source-of-truth rules

**Status:** **documented** — governance only. **Version:** v0 (Phase S2).

**Purpose:** Define what may be treated as **canonical** in-repo, what may **not** override governance silently, and how **humans** resolve conflicts. **No** automation, **no** sync engine, **no** hidden persistence.

---

## 1. What may become canonical

| Artifact | May be canonical for… |
|----------|------------------------|
| Explicit governance tables (e.g. `registry/project-registry.md`, `agents/registry.md`, `tools/registry.md`) | The **fields and semantics** those files declare — **only** after human review and version notes per [versioning-model.md](versioning-model.md) when applicable |
| Stated **normative** contracts (`workflows/*.md`, `control-plane/*.md`, designated `*-v0.md` packs) | The **documented** behavior and vocabulary of that contract |
| **External live systems** (n8n, cloud consoles) | **Their** execution truth — **not** automatically the same as MARS governance rows |

Anything not listed in a governance registry row or explicit contract remains **SAFE UNKNOWN** at registry level until a human adds or updates documentation.

---

## 2. What must never silently override governance docs

| Source | Rule |
|--------|------|
| **Runtime code** (`mars-runtime/**/*.js`, adapters, demos) | **Does not** override governance contracts. Code proves **what was typed** for an experiment; it does **not** retroactively change `tools/registry.md` or agent rows. |
| **External systems** | **Do not** become MARS-canonical **automatically**. A new n8n node ID or workflow name does **not** create or rewrite a MARS entity without a **human** doc/registry update. |
| **README files** | **Not** always authoritative. Root `README.md` is orientation; per-pack READMEs may lag. **Prefer** the registry row or the pack’s stated normative file when they disagree — then **fix** the drift in a deliberate edit. |
| **`logs/lifecycle-log.md`** | Records **events** (milestones, decisions, scope). It is **not** a substitute for implementation truth and **not** an auto-synced registry. |
| **Ad-hoc chat or tickets** | Non-canonical unless copied into governance/registry with intent |

---

## 3. Precedence model (documentation disputes)

**Order for resolving “what does MARS claim?”** (highest first for **in-repo claimed design**):

1. **Explicit governance / contract file** for that topic (e.g. project facts → `registry/project-registry.md`).  
2. **Specialized boundary doc** referenced from governance (e.g. MetaBOT → [external-system-boundaries.md](external-system-boundaries.md), pack → `integration-boundary.md`).  
3. **Pack index / operational index** for navigation — **if** conflict, open a governance ticket-style note in the lifecycle log or fix the pack; do not treat index as silent winner.  
4. **Legacy / imported** material (`web-gpt-sources/`) — **input** to design; may contradict current governance; **human** reconciliation required.  
5. **Experimental runtime** — **lowest**; illustrative only.

**Execution truth** for an external bot always belongs to **that system’s live config**, not to a Markdown row alone.

---

## 4. Conflict examples (illustrative)

| Conflict | Wrong response | Human resolution flow |
|----------|----------------|----------------------|
| `tool_id` in `mars-runtime/runtime/tool-registry.js` ≠ row in `tools/registry.md` | Assume JS is “the real registry” | Decide: either update **governance** row to match an **intended** tool, or treat JS key as **demo-only** and document that in runtime README / boundaries doc |
| n8n workflow renamed in production; MARS workflow map unchanged | Assume map is still exact | Operator verifies live graph; **sanitized** export or prose map updated **or** map marked **stale** with date |
| `README.md` says “active tool” but `tools/registry.md` says `planned` | Pick README because it is shorter | **Registry / contract wins** for status vocabulary; README corrected in a focused edit |
| Lifecycle log **evt** says “Stage X closed” but `master-build-map.md` still shows residual | Assume log overrides map | **master-build-map** remains authoritative for **per-stage** doc status; log entry may mean “milestone recorded” — align wording in a deliberate governance pass |

**Every resolution:** a **human** edits the authoritative file(s), adds a short rationale (commit message, lifecycle note, or row `notes`), and **does not** claim automated sync occurred.

---

## 5. SAFE UNKNOWN

- Which external dashboard is “primary” for a given integration until the team records it.  
- Whether two Markdown tables are duplicates or intentional parallel views until a maintainer consolidates or cross-links them.

---

*No claim of automated conflict detection, policy engines, or registry synchronization is made by this document.*
