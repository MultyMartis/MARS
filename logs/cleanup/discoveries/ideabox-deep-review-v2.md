# IdeaBox Deep Review v2

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2 Discovery  
**Mode:** Investigation + classification only (**no moves**, **no registry edit**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb`)  
**Prior evidence:** Census A-001; Wave 1 W1-019; `continuity/README.md`, governance terminology

---

## Executive determination

| Question | Answer |
|----------|--------|
| What is IdeaBox supposed to do? | **Human-operated continuity workflow** — capture ideas, discoveries, decisions in markdown under `continuity/` |
| Is it still valuable? | **Yes** — low entropy, bounded; fills gap between chat session loss and heavy governance |
| Canonical incubation layer? | **Could** — with **REDEFINE** of promotion path to programs/governance (today: manual only) |
| Recommended band | **KEEP** + **REDEFINE** (promotion/incubation charter) — **not** ARCHIVE CANDIDATE |

---

## 1. Intended workflow

| Element | Evidence |
|---------|----------|
| **Filesystem SoT** | `continuity/README.md` — markdown files are truth; no hidden index |
| **Markers** | `/ideabox`, `/discovery`, `/decision` in `continuity/protocols/session-behavior.md` — chat conventions, **not** runtime commands |
| **Protocol** | `continuity/protocols/ideabox-protocol-v1.md` — Cursor assists formatting; human decides |
| **Templates** | `continuity/templates/ideabox-entry-template.md` |
| **Subdirs** | `ideabox/`, `discoveries/`, `decisions/` (+ `.gitkeep` placeholders) |
| **Navigation** | `continuity/registry/master-index.md` — **manual only**, mostly empty |
| **Authority** | Human edits governance/registries **only** on explicit instruction — not from IdeaBox context |

**Workflow summary:**

```text
Operator marker (/ideabox | /discovery | /decision)
        → Cursor drafts markdown (Russian prose, English ids/paths)
        → Human approves path + filename
        → File under continuity/{ideabox|discoveries|decisions}/
        → Optional link in master-index (manual)
        → Promotion to program/governance = separate explicit human task
```

---

## 2. Current repository state

| Path | Files (verified) |
|------|------------------|
| `continuity/README.md` | Pack charter (RU) |
| `continuity/protocols/` | ideabox-protocol-v1, session-behavior |
| `continuity/templates/` | ideabox-entry-template |
| `continuity/registry/master-index.md` | Empty sections (operator-filled) |
| `continuity/ideabox/` | 1 idea + `.gitkeep` |
| `continuity/discoveries/` | 1 discovery + `.gitkeep` |
| `continuity/decisions/` | `.gitkeep` only |

### 2.1 Sample content

| File | Type | Links outward |
|------|------|---------------|
| `ideabox/website-factory-visual-density-budget-idea-v0.md` | draft idea | Factory contracts (blueprint, template, block-registry) |
| `discoveries/ai-multi-objective-layout-collapse-v0.md` | discovery | Links to ideabox idea above |

**Usage level:** **Low volume, high clarity** — discipline exists; corpus is small (appropriate for anti-entropy design).

---

## 3. References across repository

| Source | Classification |
|--------|----------------|
| `registry/project-registry.md` | Explicitly **not** a `project_id` row — OPERATIONAL discipline |
| `governance/registry-architecture.md` | Continuity / IdeaBox = documentation catalog + discipline |
| `governance/canonical-terminology-registry.md` | IdeaBox term — forbidden: “remembers”, autonomous memory |
| `governance/context-continuity-rules.md` | Optional filesystem workflow; not cross-chat memory product |
| `governance/operational-survivability.md` | Complements survivability; does not replace lifecycle log |
| `governance/mars-operational-first-priority-v0.md` | Optional capture — **not** SoT |
| `projects/mars-survivability/registries/protected-zones-registry-v1.md` | `continuity/` protected |
| Census / Wave 1 | **KEEP** — correctly excluded from registry |

**Reference density:** Broad governance **boundary** citations; **few** inbound links from program packs (except Factory idea).

---

## 4. Differentiation matrix

| Dimension | IdeaBox (`continuity/`) | Archive (`archive/`, Cold Brain) | Incoming (`incoming/`) | Knowledge Center | Registry |
|-----------|-------------------------|----------------------------------|------------------------|------------------|----------|
| **Purpose** | Session continuity, ideas, light discoveries | Retired bulk / historical trees | External drops, quarantine, transport | Operator navigation, Visual Brain | Project/agent **identity** rows |
| **Trust model** | Operator-authored markdown | Historical, not live SoT | **Untrusted until intake** | Navigation mirror, out-of-git | Normative **current** state |
| **Automation** | None | None | Partial (MIG adapter) | None | None |
| **SoT for execution** | **No** | **No** | **No** (transport only) | **No** | **Yes** (identity) |
| **Typical content** | Hypotheses, session notes | ORCA LRL foundation, etc. | n8n JSON, raw packs, legal docs | Canvas copies, program cards | project_id rows |
| **Promotion path** | Manual to governance/program | N/A (cold storage) | Intake → project pack | Copy from git docs | Human registry edit |

**Key distinction:** IdeaBox is **incubation / hygiene**, not **intake quarantine** (Incoming) or **identity** (Registry) or **cold bulk** (Archive/KC).

---

## 5. Overlap risks

| Risk | Severity | Mitigation (proposed) |
|------|----------|------------------------|
| IdeaBox vs `logs/cleanup/discoveries/` | **Medium** | REDEFINE: cleanup = ecosystem audit; IdeaBox = operator session capture — different charters |
| IdeaBox vs program `discoveries/` | **Low** | Program packs own execution findings; link, don’t duplicate |
| “IdeaBox remembers” mythology | **High** if violated | Terminology registry forbids — already documented |
| Empty master-index | **Low** | Expected; files in dirs are SoT |

---

## 6. Could IdeaBox become canonical incubation layer?

| Criterion | Current state | Gap for “canonical incubation” |
|-----------|---------------|--------------------------------|
| Bounded scope | ✓ | — |
| Human authority | ✓ | — |
| Promotion rules | Implicit only | Need written **incubation → program** checklist (REDEFINE) |
| Link to lifecycle log | None | Optional: append evt when idea → registry |
| Volume governance | Anti-entropy prose | No prune cadence doc |

**Assessment:** **Feasible** without runtime — as **documented incubation lane** under `continuity/` with explicit promotion to `projects/*` or governance. **Not** a substitute for Incoming (external material) or Registry (identity).

---

## 7. Recommended classification (Wave 2 — no execution)

| Action | Detail |
|--------|--------|
| **KEEP** | `continuity/` discipline; remain **non-project** row |
| **REDEFINE** | Add short `continuity/INCUBATION-PATH-v0.md` (future) — idea → discovery → decision → program promotion |
| **REDEFINE** | Clarify vs `logs/cleanup/discoveries/` in operator training |
| **Do not** | Register as `project_id`; archive; imply autonomous memory |
| **INVESTIGATE** | Whether Factory visual-density idea should promote to Factory contract — **operator** |

---

## 8. Proposed operator decisions (deferred)

| ID | Question |
|----|----------|
| I-01 | Author incubation promotion checklist? |
| I-02 | Populate `master-index.md` or keep directory-first navigation? |
| I-03 | Require Russian filenames in ideabox/ or keep mixed convention? |

---

## 9. SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Count of IdeaBox captures only in chat (never filed) | Not measurable |
| Operator Obsidian workflows using KC for ideas vs `continuity/` | Out-of-git |
| Future autonomous memory products | Explicitly out of scope — not evidenced |

---

*IdeaBox Deep Review v2 — Wave 2 Discovery evidence only.*
