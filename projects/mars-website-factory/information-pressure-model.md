# MARS Website Factory — Information Pressure Model

**Status:** **documented** — companion model for [Content Density Governance](content-density-governance.md).  
**Not:** automatic scoring, universal section classifier, copy-length law, AI readability engine, or runtime pressure detector.

**Purpose:** Give Website Factory and Forge a shared vocabulary for reading **low**, **medium**, and **high** information pressure across commercial frontend sections.

---

## 1. Core Model

Information pressure is the amount of attention demanded by a section or sequence.

Pressure comes from:

- text volume and paragraph length;
- number of cards, rows, table cells, bullets, badges, and icons;
- proof density: reviews, logos, ratings, metrics, certificates, cases;
- CTA count, CTA proximity, helper text, and form complexity;
- visual competition between headings, surfaces, borders, media, and microcopy;
- viewport state: mobile stacks usually raise perceived pressure.

Pressure is not good or bad by itself. The governance question is whether pressure is **intentional, sequenced, readable, and followed by recovery when needed**.

---

## 2. Low-Pressure Sections

Low-pressure sections ask little from the reader and often create orientation or recovery.

Common roles:

- hero opening with one clear promise;
- short CTA bridge;
- visual reset between dense chapters;
- brand mood or narrative transition;
- footer closure when not overloaded;
- simple section intro before a grid.

Governance risks:

- empty premium theater with too little commercial substance;
- giant whitespace desert;
- weak proof before a high-commitment CTA;
- low-pressure section pretending to solve trust without evidence.

Use low pressure to create **information breathing**, not to remove meaning.

---

## 3. Medium-Pressure Sections

Medium-pressure sections carry explanation, moderate proof, or structured service detail without exhausting the reader.

Common roles:

- service explanation;
- 3–6 feature cards;
- short process or step section;
- moderate trust/proof band;
- short FAQ group;
- compact benefit grid;
- CTA with supporting microcopy.

Governance requirements:

- clear scanning ladder;
- distinct primary/supporting text;
- controlled card copy length;
- proof paced to the claim it supports;
- CTA remains visible and not crowded by helper text;
- mobile stack includes resets and grouping.

Medium pressure is often the safest default for commercial readability, but it can still drift into overload when every card becomes a mini-landing page.

---

## 4. High-Pressure Sections

High-pressure sections carry dense proof, comparison, technical detail, prices, inventory, FAQ, or operational constraints.

Common roles:

- specs or equipment matrix;
- pricing / package comparison;
- dense FAQ;
- proof wall or testimonial set;
- certifications, guarantees, and compliance evidence;
- complex service geography or scenarios;
- detailed process constraints;
- high-intent form with multiple fields.

High density is allowed when:

- the section has a clear commercial reason;
- hierarchy makes scanning possible;
- details are grouped by decision role;
- proof is paced, not sprayed;
- CTA is protected from burial;
- neighboring sections provide approach and recovery;
- mobile density is separately reviewed.

High-pressure sections are harmful when they become uncontrolled: endless cards, SEO text wall, proof spam, dense-table collapse, trust-wall drift, or CTA dilution by density.

---

## 5. Transition Balancing

Pressure changes should be sequenced, not accidental.

| Transition | Governance read |
|------------|-----------------|
| **Low → Medium** | Good for explanation after orientation; ensure the pressure rise is clear and not abrupt. |
| **Medium → High** | Needs setup: the reader should know why detail is coming. |
| **High → Low** | Should provide readability recovery; avoid a void that feels like missing content. |
| **High → High** | Risky; requires strong grouping, cadence reset, or section split. |
| **Low → High** | Usually needs a bridge; direct jump can feel like a wall of content. |

Pressure transitions interact with [canonical vertical cadence](canonical-vertical-cadence-system.md): spacing can pace a transition, but spacing alone cannot fix uncontrolled information load.

---

## 6. Density Sequencing

Density sequencing is the page-level order of information pressure.

Review:

- Does the page start with orientation before heavy detail?
- Are proof-heavy sections distributed or concentrated intentionally?
- Does the page alternate density with recovery rather than stacking overload?
- Do trust elements support key claims instead of appearing everywhere?
- Does the CTA appear after enough proof but before exhaustion?
- Does mobile sequencing preserve recovery beats?

Bad sequencing makes each section individually defensible while the page as a whole feels noisy, flattened, or commercially less serious.

---

## 7. Proof Pacing

Proof must arrive at the moment it helps a decision.

Proof pacing rules:

- Place proof near the claim it validates.
- Avoid repeating the same proof type in every section.
- Do not let trust badges replace specific evidence.
- Reserve high proof density for sections where proof is the point.
- Use summary proof before detail when the reader needs orientation.
- On mobile, avoid long uninterrupted review/logo/certificate stacks.

Proof saturation lowers trust when every proof item competes at equal volume.

---

## 8. Informational Breathing

Informational breathing is the recovery space between pressure beats. It can be created through:

- shorter intro or bridge sections;
- clearer headings and subhead summaries;
- grouped cards instead of raw card volume;
- staggered proof rather than proof wall;
- visual cadence resets;
- reducing microcopy around CTA;
- mobile section breaks or summary-first ordering when approved.

Breathing is not merely whitespace. It is a semantic and visual pause that lets the reader process density before the next obligation.

---

## 9. Readability Recovery

Readability recovery is required after sustained pressure.

Signals recovery is needed:

- reader must parse many equal cards;
- proof row follows proof row;
- dense table follows dense grid;
- CTA is surrounded by caveats and badges;
- mobile stack runs longer than one readable beat;
- section role changes but pressure does not drop.

Recovery can be low-pressure, but it can also be medium-pressure with strong hierarchy. The key is a clear change in scanning demand.

---

## 10. Cadence-Density Interaction

Cadence and density must be read together:

- High density with tight cadence creates overload.
- High density with excessive whitespace can feel fragmented and slow.
- Low density with large cadence can become empty theater.
- Medium density with stable cadence can carry serious commercial explanation.
- Mobile cadence must account for taller stacks and fewer simultaneous scan anchors.

Use [cadence-tier-model.md](cadence-tier-model.md) for spacing intention and this model for information pressure intention. Neither replaces the other.

---

## 11. Forge / QA Hook

When pressure is in scope, record findings under:

```text
CONTENT DENSITY FINDINGS
```

Include:

- section pressure level: low / medium / high / SAFE UNKNOWN;
- pressure sequence vs neighbors;
- proof pacing;
- CTA survival;
- mobile density;
- overload taxonomy matches;
- disposition: PASS / PARTIAL / FAIL / SAFE UNKNOWN.

---

## 12. SAFE UNKNOWN

Record **SAFE UNKNOWN** when pressure intent cannot be established from approved sources, copy authority, SEO brief, design pack, mobile export, or HITL decision.

Do not trim, split, hide, summarize, or add copy by taste when authority is missing.

---

## 13. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Information Pressure Model — low/medium/high pressure, sequencing, proof pacing, breathing, recovery, cadence-density interaction. |
