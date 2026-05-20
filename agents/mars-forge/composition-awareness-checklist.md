# Compositional structure awareness checklist — MARS Forge (overlay v0)

**Mandatory companion:** [compositional-structure-awareness.md](../../projects/mars-website-factory/compositional-structure-awareness.md) — concepts, detection rules, decision model, freeze semantics.  
**Taxonomy reference:** [composition-drift-taxonomy.md](../../projects/mars-website-factory/composition-drift-taxonomy.md).

**Nature:** **human-supervised** governance checklist — **not** automated DOM analysis, **not** layout AI, **not** silent structural rewrites.

**When:** **Gate G7** — run **with** or **immediately after** gate G6 ([`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md)), **before** final responsive QA closure and freeze — see [`semantic-source-lock.md`](semantic-source-lock.md) §5 and [`workflow.md`](workflow.md).

Record pass / partial / fail in REPORT **Forge execution** under `COMPOSITION FINDINGS` and link decision **A / B / C / D** per companion doc §5.

---

## Gate G7 — Compositional structure (pre-freeze)

- [ ] **Charter** — Same screen anchor as G6; active source path named.  
- [ ] **Cluster read** — Short bullet list: which elements the **design** treats as **one composition cluster** vs separate in this band.  
- [ ] **DOM map** — Note which **wrappers / sections / includes** hold those elements; flag **splits** that cross cluster boundaries.  
- [ ] **D1–D7 questions** — Answered per [compositional-structure-awareness.md §4](../../projects/mars-website-factory/compositional-structure-awareness.md); any “yes” → note evidence.  
- [ ] **Spacing honesty** — If tightening/loosening mainly **compensates** for **wrong** DOM splits, flag **accidental composition split** or **composition fragmentation** — do not treat as pure visual polish.  
- [ ] **Framing** — Source cluster has **shared** frame/band/card; build **does/does not** — if mismatch, type **framing mismatch**.  
- [ ] **CTA cluster** — Price, urgency, primary/secondary actions: **one beat** in source vs **split** DOM? Note **CTA cluster separation** if applicable.  
- [ ] **Ceiling check** — If semantic + responsive pass but visual parity still short, ask whether **structure** is the ceiling (**B/C/D**).  
- [ ] **Drift typed** — Labels from [composition-drift-taxonomy.md](../../projects/mars-website-factory/composition-drift-taxonomy.md) + optional cross-tags from [visual-drift-taxonomy.md](../../projects/mars-website-factory/visual-drift-taxonomy.md).  
- [ ] **Escalation** — **A** local tuning | **B** insufficient / unclear | **C** regrouping recommended (human approval) | **D** SAFE UNKNOWN — **recorded**.  
- [ ] **No silent regroup** — No markup/include boundary change for composition **without STRUCTURE CHANGE / HITL** — see [`AGENT.md`](AGENT.md) anti-drift.  
- [ ] **Freeze disposition** — PASS | PARTIAL (composition noted) | FAIL; if PARTIAL, cite **composition-vs-DOM** explicitly for freeze honesty.

---

## REPORT stub (copy shape)

```text
COMPOSITION FINDINGS — <section or block_id> — <source ref>

Cluster read (design):
- <e.g. price + offer framing + primary CTA = one cluster>

DOM map (brief):
- <e.g. price in partial A, CTA in partial B, framing copy in hero include>

Detection:
- D1–D7: <yes/no + one line each where yes>

Drift types:
- <e.g. composition fragmentation, CTA cluster separation>

Decision: A | B | C | D
If C: proposed structural change (human approval required): <outline only>

Disposition: PASS | PARTIAL | FAIL
```

---

## Not claimed (v0)

- Automatic grouping inference from screenshots.  
- DOM-diff or AST tooling as gate.  
- Authority to merge/split sections without human approval.

---

## Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial G7 checklist for compositional structure awareness. |
