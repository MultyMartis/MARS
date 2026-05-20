# MARS — Runtime mythology pressure review v0

**Status:** **documented** — lightweight review (Phase 2).  
**Date:** 2026-05-19.  
**Complements:** [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md), [enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md).

**Does not:** remove runtime research, attack experiments, or shrink `mars-runtime/` contracts.

**Goal:** reduce **accidental overclaim** from vocabulary density.

---

## 1. Highest mythology-pressure terminology

| Term / phrase | Pressure | Why |
|---------------|----------|-----|
| **Runtime** (unqualified) | **Critical** | Readers equate folder name with **shipped product** |
| **Orchestrator / orchestration** | **Critical** | Stage 13 docs + Factory “multi-agent” prose |
| **Control plane** | **High** | `control-plane/` sounds implemented |
| **Validator** (Factory) | **High** | Implies automated QA engine |
| **Execution bridge** (as live) | **High** | R1 demo vs contract v0 |
| **Registry** (any) | **High** | Row → running service |
| **Operational** (alone) | **Medium** | Conflicts with “documentation-only operational” |
| **Active** (project status) | **Medium** | Means “in use” docs, not deployed system |
| **Factory** (as engine) | **High** | “Website Factory runs …” |
| **Agent** (without HITL) | **High** | Card exists → bot runs |
| **Validated / verification** | **Medium** | Who validated? |
| **Platform / system** (capitalized) | **Medium** | Prestige nouns |

---

## 2. Highest confusion-risk areas

| Zone | Confusion | Safe framing |
|------|-----------|--------------|
| `mars-runtime/` folder | Contracts + R1 JS coexist | **“Contracts (conceptual) + R1 (experimental only)”** |
| Factory validation docs | Filenames contain `runtime`, `validator` | Lead with **documentation-only validation semantics** |
| `master-build-map.md` stages 8–15 | “Complete” vs implemented | **“Documentation milestone”** (lifecycle evt pattern) |
| MetaBOT + R1 adapter | Adapter implies MARS owns MetaBOT | **“Experimental handoff sketch; n8n owns execution”** |
| Registry `active` | Live service | **“Active documentation / human workflow”** |
| Triumph reference case | Factory proof | **“Calibration case; not Factory engine evidence”** |
| WPilot “bridge” | Plugin exists | **“Planned bridge — no plugin source in tree”** |
| tools/ helpers | Governance enforcement | **“Manual assist; REPORT still human-owned”** |

---

## 3. Runtime-vocabulary overload zones

| Path pattern | Overload type | Mitigation |
|--------------|---------------|------------|
| `projects/mars-website-factory/*validation*` | Executable implication | Point to `safe-unknown-boundary.md` first |
| `projects/mars-website-factory/*execution*` | Engine implication | Pair with `execution-semantics-overview-v0.md` banner |
| `mars-runtime/*orchestr*` | Product implication | README + [runtime-registry-boundaries.md](runtime-registry-boundaries.md) |
| `control-plane/`, `workflows/` | Shipped stack | Folder README **planned contract** line in first paragraph |
| `agents/cards/*` | Autonomous agent | Card = **role contract**; HITL required |
| `web-gpt-sources/02-core/*` | Legacy live paths | **historical import** label |

---

## 4. Conceptual vs operational confusion

| Reads as operational | Actually |
|----------------------|----------|
| “MARS executes the workflow” | Human + Cursor executes; MARS **documents** workflow |
| “Factory Stage N complete” | Artifact/checkpoint language — verify human sign-off |
| “Bridge connected MetaBOT” | One-off R1 script possible — **not** platform integration |
| “ORCA reviewed the SERP” | Human operator used ORCA **checklists** |
| “Governance enforces …” | Human review + honesty rules — **no** enforcer |
| “IdeaBox remembers context” | Markdown capture — **not** agent memory |

---

## 5. Small wording / boundary improvements (proposed)

Apply on **next touch** of affected files — **no** mass find-replace in Phase 2.

| Location | Current risk | Proposed tweak |
|----------|--------------|----------------|
| Unqualified “runtime” in new docs | Overclaim | Prefer **“runtime research (experimental R1)”** or **“runtime contracts (documentation only)”** |
| Factory `validation-runtime-overview-v0.md` | Filename | Add/retain top banner: **“Semantics only — not a validator service”** |
| README “Operationally verified” | MARS automation | Keep glossary: **“human-controlled repo work”** |
| Project registry `active` | Deployed | Footnote already good — link **reality index** in registry header |
| New agent cards | Autonomy | Opening line: **“Documentation role — human-supervised”** |
| REPORT templates | Validation | **“Validation = human meaning unless script named”** |
| Cross-pack READMEs | Factory engine | **“Methodology pack”** not **“runs pipelines”** |

**Canonical term discipline:** [canonical-terminology-registry.md](canonical-terminology-registry.md) — prefer **CONCEPTUAL**, **EXPERIMENTAL**, **BOUNDARY ONLY** over **PLANNED** in new stabilization prose.

---

## 6. Pressure relief order (stabilization)

1. Session bootstrap: [mars-reality-index-v0.md](mars-reality-index-v0.md)  
2. Runtime lane: read `mars-runtime/README.md` before any `*-v0.md` contract  
3. Factory lane: `safe-unknown-boundary.md` before validation cluster  
4. External lane: [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md)  
5. Before public claims: [forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md) scan  

---

## 7. SAFE UNKNOWN

- Per-reader misread rate — **not measured**  
- Whether renaming `validation-runtime-*` files is worth link churn — **editorial judgment**  

---

*Runtime mythology review — vocabulary discipline; does not deprecate runtime research.*
