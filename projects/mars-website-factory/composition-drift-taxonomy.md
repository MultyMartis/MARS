# MARS Website Factory — Composition drift taxonomy

**Status:** **documented** — pattern vocabulary for **human-supervised** composition-vs-DOM review.  
**Not:** automated structure diff, AST analysis products, or enforcement engines.

**Parent methodology:** [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Checklist:** [`../../agents/mars-forge/composition-awareness-checklist.md`](../../agents/mars-forge/composition-awareness-checklist.md).

**Purpose:** Name recurring ways **visual composition intent** diverges from **DOM segmentation** so operators can report **structural** mismatch **without** implying autonomous regrouping.

**Distinction:** [visual-drift-taxonomy.md](visual-drift-taxonomy.md) focuses on **visual-emphasis** outcomes (hierarchy drift, CTA dilution, etc.). This file focuses on **grouping and container structure** relative to the design’s clusters.

---

## How to use this doc

- Reference **drift type + evidence** in REPORT under `COMPOSITION FINDINGS` (alongside `VISUAL FINDINGS` when both apply).  
- Link to **decision path A/B/C/D** from [compositional-structure-awareness.md §5](compositional-structure-awareness.md).  
- **Structural regrouping** remains **human-approved** only — typing a drift does **not** authorize markup changes.

---

## A. Taxonomy (definitions)

| Drift type | Definition | Typical DOM / implementation clues |
|------------|------------|-----------------------------------|
| **Composition fragmentation** | One **composition cluster** in the source is **split** across multiple DOM regions so the eye’s “unit” does not match markup’s “unit” | Price, CTA, and framing live under **different** wrappers or includes; shared visual beat **broken** by section boundaries |
| **False separation** | Elements that should **read together** are **isolated** by markup or spacing conventions as if they were unrelated siblings | Large vertical gaps **implied by structure** between items that share one **offer** read |
| **Accidental composition split** | Refactor, component reuse, or handoff slots **separated** a cluster **without** intentional design authority | Card partial reused in two zones; hero subcopy torn from CTA group |
| **Visual grouping collapse** | DOM puts **too much** in one container; distinct source clusters **merge** visually | Single column stacks **offer + proof + secondary CTA** when source shows **separate** bands |
| **Hierarchy container mismatch** | Semantic or heading hierarchy **follows** DOM, but **visual hierarchy** fights **where** containers break | Subhead “belongs” visually to CTA cluster but sits **outside** the CTA wrapper in markup |
| **CTA cluster separation** | Primary action, supporting actions, urgency/scarcity, or **price-before-click** read as **one conversion beat** in source but **multiple** DOM hooks | Buttons in one partial, price in another, framing text in a third — tuning margins **approximates** one card |
| **Framing mismatch** | Source uses **one** panel/band/card frame for the cluster; build **lacks** shared background, border, or enclosure | Design shows unified **offer block**; build shows **floating** pieces on shared page background |
| **Composition-vs-DOM drift** | **Umbrella** label when reporting the class of issue: **visual composition** and **DOM grouping** are **misaligned** — local polish hits a **ceiling** | Repeated PARTIAL after G6; D1–D7 questions in compositional-structure-awareness §4 trend positive |

---

## B. Triumph V2 Screen 01 — reference illustration (documentation only)

| Observation (from factory narrative) | Drift types it exemplifies |
|--------------------------------------|---------------------------|
| **Price band + CTA cluster + offer framing** read as **one** compositional unit in the source | **Composition fragmentation**, **CTA cluster separation**, **framing mismatch** if DOM spreads them across zones |
| Local spacing improves **perception** but **full** cluster parity **eludes** without shared framing or regrouping | **Composition-vs-DOM drift** with escalation **B** or **C** per decision model |

**SAFE UNKNOWN:** If the chartered screen does not define **one vs two** clusters, do not guess — record per [compositional-structure-awareness.md §8](compositional-structure-awareness.md).

---

## C. Overlap with visual drift taxonomy (co-tagging)

One slice may need **both** taxonomies:

| Composition drift | Often co-occurs with visual drift (examples) |
|-------------------|-----------------------------------------------|
| CTA cluster separation | CTA dilution, focal competition |
| Framing mismatch | Visual flattening, density collapse |
| Visual grouping collapse | Accidental equalization, trust displacement |

Co-tagging improves REPORT clarity: **visual** symptom + **structural** suspected cause.

---

## D. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial composition drift taxonomy + Screen 01 illustration pointer. |
