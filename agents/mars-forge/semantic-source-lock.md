# Semantic source lock — MARS Forge (mandatory overlay)

**Normative for:** `mars_forge_frontend_agent` when implementing design-driven static frontend (human or Cursor-assisted).  
**Nature:** governance / methodology — **not** runtime enforcement, **not** a substitute for [`../frontend-gulp-agent/`](../frontend-gulp-agent/) foundation rules.

**Related:** [`AGENT.md`](AGENT.md) (gates), [`qa-checklist.md`](qa-checklist.md) (gate G5), [`workflow.md`](workflow.md) (screen cadence), [`source-interpretation-checklist.md`](source-interpretation-checklist.md) (source confidence / ambiguity before implementation).

---

## 0. Rationale (lessons learned, non‑normative)

Real validation failures (e.g. Triumph Manipulator Landing V2) showed **semantic drift** when the executor mixed visual inspiration, archived mockups, legacy PDF/rules, DOM guesses from other versions, or “marketing improvement” instinct with the **active** design source. This document adds a **mandatory** layer so implementation **locks meaning and copy** to the chartered source, not to older screens or untrusted docs.

---

## 1. Active design version required (pre‑flight)

Before **any** implementation work, the **task / prompt charter** must state explicitly:

| Charter field | Example (illustrative only) |
|---------------|----------------------------|
| **Active design version** | e.g. `v2` |
| **Canonical visual source path** | e.g. `projects/<site>/design/v2/` (repo‑relative paths) |
| **Forbidden design versions / paths** | e.g. `design/v1/`, stray `design/mockups/` archives |
| **Allowed `shared-assets` path** (if any) | e.g. `projects/<site>/design/shared-assets/` — **assets only**, see §3 |
| **Workspace / target repo path** | where `src/` (or equivalent) is edited |

**If any of the above are missing or contradictory:** stop implementation, report **SAFE UNKNOWN**, and request an updated charter — **do not** guess the active version or “pick the nicest mockup.”

---

## 2. Semantic source lock (what must not drift)

During implementation the agent **locks** the following to the **active** canonical matrix / screens / handoff (as named in the charter), unless the **same prompt** documents a human‑approved rewrite:

- **Section meaning** (what the section *is for* — not a different product story).
- **Section order** vs canonical page flow.
- **Title text** (headings as shown in source; no invented marketing titles).
- **Key copy** taken from the mockup / copy deck tied to the active version.
- **Number of represented entities** (e.g. one machine vs fleet catalog — must match source).
- **CTA meaning** (what the user is offered / asked to do).
- **Visual role of each screen** (hero vs supporting vs footer cluster — no role swap).

**Do not rewrite meaning** to “improve” conversion or aesthetics without an explicit, documented approval in the task or handoff.

**Illustrative anti‑patterns (forbidden):**

- One‑machine presentation → multi‑machine fleet or pricing grid.
- Section “Наша техника” (or any source title) → unrelated invented headline.
- Archive or V1 reference **overrides** a V2 screen for structure or copy.
- Guessed semantics when the mockup is unclear → must be **SAFE UNKNOWN**, not fabrication.

---

## 3. Version isolation

| Source | Allowed use in implementation |
|--------|-------------------------------|
| **Active version folder** (e.g. `design/v2/`) | Defines **layout, semantics, copy, section order** for that build. |
| **Older version folder** (e.g. `design/v1/`) | **Historical comparison only** — not default structure, copy, or flow. |
| **`shared-assets/`** | **Reusable images, icons, logos, raw media paths** — **never** authoritative for section structure, order, titles, entity count, or CTA semantics. |

**Never** treat deprecated layout trees, stale `design/mockups/` trees, or mixed folders as SoT unless the **current charter** explicitly upgrades them.

---

## 4. Old rules / PDF safety

- **Legacy PDFs, withdrawn rule files, old “design packets,”** or chat excerpts are **not** trusted unless **listed by name/path** in the **current task** as **canonical** alongside the visual source.
- If a legacy PDF or old rules doc **conflicts** with the **current** SoT (charter + active matrix + active screens), **follow current SoT** and note the conflict in REPORT — **do not** silently prefer the PDF.

---

## 5. Screen‑by‑screen implementation (validation builds)

For **validation** or **first‑pass fidelity** builds, advance **screen‑by‑screen** (each screen / major fold matching one source artifact or defined slice):

1. **Source screen** — identify the exact file(s) in the **active** path.  
2. **Visual reading** — short human read of intended **hierarchy, focal path, CTA dominance, density, trust placement** vs source (governance: [`../../projects/mars-website-factory/visual-reconciliation-layer.md`](../../projects/mars-website-factory/visual-reconciliation-layer.md)).  
3. **Source interpretation confidence** — separate observed / inferred / assumed / unknown, record material ambiguity per [`source-interpretation-checklist.md`](source-interpretation-checklist.md), [source-confidence-model.md](../../projects/mars-website-factory/source-confidence-model.md), and [source-ambiguity-taxonomy.md](../../projects/mars-website-factory/source-ambiguity-taxonomy.md).  
4. **Semantic extraction** — list meaning, titles, entities, CTAs (short written lock).  
5. **Content lock** — freeze that list for this slice unless HITL updates the charter.  
6. **Layout implementation** — structure → layout → style (Forge phases; responsive work **during** implementation remains required).  
7. **Semantic QA** — §6 checklist.  
8. **Visual reconciliation** — gate **G6** [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md): compare built UI **visual intent** to source; **not** pixel diff, **not** autonomous AI.  
9. **Compositional structure awareness** — gate **G7** [`composition-awareness-checklist.md`](composition-awareness-checklist.md): **composition-vs-DOM** cluster read; **not** silent regroup; structural change **human-approved** only.  
10. **Final responsive QA** — closing viewport spot checks **after** G6/G7 (survival **and** emphasis at breakpoints).  
11. **Freeze** — per [`AGENT.md`](AGENT.md).

**Do not** implement “later” screens using **older DOM guesses**, a different version’s HTML, or recalled structure from a prior session without re‑anchoring to the **current** source screen.

**Note:** “Screen” may map to handoff `block_id` slices; the rule is **one semantic source anchor per slice**, not whole‑page dumps that blur version boundaries.

---

## 6. Semantic QA gate (before PASS / freeze)

Before marking a section **PASS** or **frozen**, confirm:

- [ ] **Title** matches source **or** a **documented approved rewrite** in task/handoff.  
- [ ] **Section meaning** matches source (no fleet/pricing/catalog invention).  
- [ ] **Entity count** matches source (cards, machines, steps, etc.).  
- [ ] **CTA meaning** matches source.  
- [ ] **No V1/V2 (or cross‑version) blending** in the same section.  
- [ ] **No archive / deprecated path contamination** of structure or copy.  
- [ ] **No invented fleet, pricing, or catalog logic** absent from source.

Record pass / fail / partial in REPORT **Forge execution** and link evidence (file paths, matrix row ids if used).

---

## 7. Quarantine rule (unconfirmed sections)

If the implementation contains a **section or block** **not** confirmed by the **canonical matrix / handoff / active charter**:

- **Do not** silently treat it as production‑ready on the homepage.  
- Mark it as **quarantine candidate** in REPORT: what it is, why it appeared, which source (if any) was used.  
- **Require human decision** before it is accepted as live homepage scope.

---

## 8. Source priority (frontend implementation)

When sources disagree, apply this order (**lower number wins**). **Archive and legacy must never override active V2 (or whatever the charter names as active).**

| Priority | Source |
|----------|--------|
| **P0** | **Current task charter** (explicit scope, version, paths, approvals). |
| **P1** | **Active Source of Truth / canonical matrix** (project‑specific doc or handoff field). |
| **P2** | **Active design version screens** (e.g. `design/v2/` mockups agreed in charter). |
| **P3** | **Approved design system / CSS rules** for the project (tokens, components). |
| **P4** | **`shared-assets`** — media only; does not override P0–P3 for meaning. |
| **P5** | **Archive versions / legacy references** — comparison or asset salvage only with charter. |
| **P6** | **Old chats, old PDFs, old mockups** — **never** override P0–P2. |

---

## SAFE UNKNOWN (semantic layer)

- Which folder is **active** if the repo has multiple `v*` trees and the prompt does not name one.  
- Whether a given PDF or note is **still canonical** if not listed in the current task.  
- Exact copy where the mockup is illegible or missing — **flag**, do not invent.  
- Whether a block exists in the canonical matrix — if unknown, **quarantine** per §7.

---

## Revision history

| Date | Change |
|------|--------|
| 2026-05-16 | Initial **semantic source lock** overlay after Triumph V2 SoT failure — charter, isolation, QA gate, quarantine, P0–P6 priority. |
| 2026-05-16 | **Screen cadence** §5: insert **visual reading**, **visual reconciliation** (G6), **compositional structure** (G7), **final responsive QA** ordering before freeze; align with [visual-reconciliation-layer.md](../../projects/mars-website-factory/visual-reconciliation-layer.md) and [compositional-structure-awareness.md](../../projects/mars-website-factory/compositional-structure-awareness.md). |
| 2026-05-17 | Added source interpretation confidence step before semantic extraction; links source interpretation checklist, confidence model, and ambiguity taxonomy. |
