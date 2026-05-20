# MARS Website Factory — Mobile Composition Preservation

**Status:** **documented** — human-supervised mobile composition methodology for Website Factory frontend work.  
**Not:** mobile redesign engine, automatic layout synthesis, mandatory mobile aesthetic, or universal breakpoint law.

**Purpose:** define how mobile implementations preserve **dominant clusters**, **CTA hierarchy**, **reading flow**, **grouping**, **rhythm**, **section identity**, and **transition pacing** when desktop or tablet composition collapses.

**Parent layer:** [responsive-intent-governance.md](responsive-intent-governance.md).  
**Companion taxonomy:** [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md).

---

## 1. Positioning

Mobile composition preservation is not “turn every grid into one long stack.”

It asks whether the narrow viewport still communicates the same authored section role:

- what wins attention;
- what supports the decision;
- what belongs together;
- where the user should pause;
- where the CTA should appear;
- where the section starts, breathes, and ends.

If the mobile version fits but the section reads as a different story, responsive intent has drifted.

---

## 2. Preserve Dominant Clusters

A **dominant cluster** is the visual group that carries the section’s primary meaning or conversion job: hero claim + CTA, price + offer + action, proof headline + trust row, service description + media, etc.

Rules:

- Preserve the dominant cluster as a perceptual unit after collapse.
- Do not scatter dominant-cluster elements through a long stack unless the source or HITL charters that reading flow.
- Do not let supporting cards, badges, icons, or secondary proof visually overtake the dominant cluster.
- If DOM structure prevents cluster preservation, record composition / responsive intent finding instead of forcing cosmetic fixes.

---

## 3. Preserve CTA Hierarchy

Mobile CTA behavior must preserve **meaning and pressure balance**.

Check:

- Primary CTA remains the clearest action without becoming a mobile “screaming” block.
- Secondary CTA supports, explains, or defers; it does not become a peer by size, order, or sticky treatment.
- Repeated CTAs are paced; they do not appear after every dense stack by reflex.
- CTA adjacency to price, proof, or form context remains readable.
- Tap zones are safe without inflating buttons into dominant objects when the source does not intend that dominance.

CTA hierarchy may need **rebalance** on mobile, but rebalance is not permission to invent a new conversion system.

---

## 4. Preserve Reading Flow

Mobile reading flow is sequential, but it should not become accidental.

Rules:

- Preserve the logical ladder: claim → context → proof → action, or the project-approved variant.
- Avoid responsive hierarchy inversion where media, badges, trust rows, or secondary cards precede the primary meaning by accident.
- Do not copy desktop left/right order mechanically if the mobile flow becomes incoherent.
- Do not reorder content for aesthetics if it changes the semantic argument.
- When source authority is missing, prefer **SAFE UNKNOWN** over confident mobile re-sequencing.

---

## 5. Preserve Grouping

Grouping must survive grid collapse.

Preserve:

- shared card / panel / band relationships;
- heading + body + proof item association;
- price + conditions + CTA grouping;
- media + caption / context grouping;
- trust markers attached to the claim they support.

Forbidden drift:

- stack flattening that turns all children into equal independent cards;
- separating helper text from the action it qualifies;
- placing trust proof so far from the claim that it reads as a different section;
- using identical mobile gaps between unrelated and related objects.

---

## 6. Preserve Rhythm

Mobile rhythm is a separate cadence problem, not desktop spacing divided by a number.

Mobile must preserve:

- title/body breathing;
- paragraph readability;
- item-to-item gaps that distinguish related vs unrelated objects;
- CTA isolation;
- dense-section recovery space;
- transition pacing between sections.

Compression becomes drift when the user can no longer tell which objects belong together, which object matters most, or when to pause.

---

## 7. Preserve Section Identity

Each section should remain recognizable by role after mobile collapse.

| Section role | Mobile preservation risk |
|--------------|--------------------------|
| **Hero** | Turns into generic centered intro; proof/CTA dominance confused. |
| **Proof** | Becomes dashboard cards or endless review stack. |
| **Explanation** | Compresses into text wall without rhythm. |
| **Dense specs / services** | Overloads the viewport with equal cards and icons. |
| **CTA / lead** | Becomes too aggressive, too repeated, or visually detached from context. |
| **Footer** | Loses closure cadence and becomes another dense navigation block. |

Mobile adaptation may change layout mechanics, but section identity must remain legible.

---

## 8. Preserve Transition Pacing

Mobile pages are vulnerable to endless-stack fatigue because every section becomes vertical.

Review transitions:

- Does the previous section release attention before the next one starts?
- Does a dense section get breathing before another dense, CTA, or footer section?
- Does dark/light or mood transition still have a reset?
- Does CTA repetition create pressure rather than confidence?
- Does the page feel like authored narrative beats or a concatenated feed?

Transition pacing is part of responsive intent, not optional polish.

---

## 9. Decision Model

| Decision | Meaning | Action |
|----------|---------|--------|
| **Preserve as-is** | Existing collapse preserves hierarchy, grouping, and cadence. | Pass responsive intent check. |
| **Tune within structure** | Intent drift can be corrected with spacing, order within approved scope, type, surface, or CTA weight. | Implement bounded responsive tuning. |
| **Partial with deferral** | Mobile source or authority missing; survivability passes but fidelity cannot be proven. | Record **PARTIAL — responsive intent**. |
| **Escalate structure** | Existing DOM cannot preserve dominant clusters or grouping. | Require HITL / STRUCTURE CHANGE. |
| **Reject redesign** | Proposed mobile pattern changes the approved narrative or aesthetic without authority. | Do not implement; document finding. |

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| No mobile export | Dominant cluster behavior cannot be verified beyond general rules. |
| Desktop-only source | Mobile cadence and reordering require interpretation. |
| Ambiguous CTA order | Cannot determine primary/secondary mobile relationship. |
| Section identity unclear | The same content could be proof, specs, CTA support, or navigation. |
| Compression threshold unclear | No authority for when a dense section should split, disclose, or remain full. |

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial mobile composition preservation methodology. |
