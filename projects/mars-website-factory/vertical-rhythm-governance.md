# MARS Website Factory — Vertical Rhythm Governance

**Status:** **documented** — governance and production **methodology** only.  
**Not:** runtime spacing engine, autonomous enforcement, automatic visual fatigue scoring, screenshot diff, or layout generation.

**Purpose:** Formalize deterministic inter-section and intra-landing vertical rhythm so Website Factory landing pages preserve breathing, density transitions, CTA pacing, and continuity from hero to footer.

**Core cadence canon:** [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md).  
**Full-page continuity layer:** [full-page-cadence-continuity-governance.md](full-page-cadence-continuity-governance.md).  
**Cadence tier model:** [cadence-tier-model.md](cadence-tier-model.md).  
**Forge checklist:** [`../../agents/mars-forge/rhythm-governance-checklist.md`](../../agents/mars-forge/rhythm-governance-checklist.md).  
**Forge cadence checklist:** [`../../agents/mars-forge/cadence-governance-checklist.md`](../../agents/mars-forge/cadence-governance-checklist.md).  
**Related typography layer:** [typography-rhythm-governance.md](typography-rhythm-governance.md).  
**Related visual layer:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Related composition layer:** [compositional-structure-awareness.md](compositional-structure-awareness.md).

---

## 1. Positioning

Vertical rhythm governance describes **human-supervised cadence decisions** for marketing landing production. It helps operators avoid random section spacing, accidental compression, and abrupt density shifts while keeping every section anchored to the approved design source and project implementation pack.

This layer does **not** claim universal spacing truth. A project may define its own scale, but the scale must be explicit, consistent, and reviewable.

For Website Factory production, the canonical framing is: **inter-screen spacing = narrative pacing**. This file governs vertical rhythm details; the core cadence canon defines page-level tier vocabulary, density bridges, and `CADENCE FINDINGS`.

---

## 2. Core Concepts

| Concept | Meaning |
|---------|---------|
| **Section cadence** | The repeatable vertical beat between section starts, headings, body groups, CTAs, and exits. |
| **Vertical breathing** | The perceived air around content that lets the eye reset before the next message. |
| **Rhythm collapse** | A section or breakpoint loses breathing and becomes compressed, even if it technically fits. |
| **Density spike** | A sudden local increase in text/cards/forms/icons that disrupts the landing’s pacing. |
| **Spacing contamination** | A previous section, global class, or inherited wrapper imposes spacing that the current screen did not charter. |
| **Cadence continuity** | The page keeps a predictable pacing arc across adjacent sections without feeling mechanical. |
| **Section pressure** | A section carries too many visual obligations for its allotted height or spacing. |
| **Visual fatigue** | The cumulative effect of crowded, irregular, or over-expanded sections tiring the reader. |
| **Transition harshness** | The boundary between sections feels abrupt because contrast, spacing, or density changes without a reset beat. |

---

## 3. Inter-Section Spacing Cadence

Inter-section cadence governs the boundary between landing sections. Operators should read:

- Whether adjacent sections have a deliberate top/bottom spacing relationship.
- Whether a dark/light transition includes enough reset space to feel intentional.
- Whether section exits lead into the next section without collision or dead whitespace.
- Whether repeated section types keep comparable rhythm unless the source clearly changes role.

The question is not “are all paddings identical?” The question is whether the landing keeps a **controlled pacing system** from one narrative beat to the next.

Vertical rhythms are **system-owned**. A section may declare local padding, but it does not independently own the page-level beat between screens.

Rules:

- Same-background transitions usually use only one boundary rhythm, commonly the previous section's bottom rhythm or the next section's top rhythm, to avoid double-gap duplication.
- Different-background transitions may use both upper and lower rhythm when contrast, density, or atmosphere needs a reset.
- Rhythm values should stay globally consistent through named tiers or project scale.
- Exceptions must be intentional, source-backed, and documented.

---

## 4. Density Transitions

Density transitions govern movement between sparse hero bands, proof strips, dense card grids, forms, and footer material.

Review:

- Sparse → dense transitions should include a readable approach, not a sudden wall of content.
- Dense → sparse transitions should provide a reset, not a jarring void.
- Card grids and proof rows should not crowd CTAs or headings.
- Long sections should reduce section pressure through structure before arbitrary spacing compression.

---

## 5. Breathing Rhythm

Vertical breathing is the landing’s ability to let the reader pause between content obligations.

Governance questions:

- Does the hero have enough exit breathing before proof or technical detail?
- Do headings have consistent title-block breathing before content begins?
- Do CTA clusters have enough separation from supporting copy and trust material?
- Does the footer retain enough breathing to avoid reading like an afterthought?

---

## 6. Dark / Light Transition Spacing

Dark/light section changes often need deliberate vertical rhythm because contrast changes amplify spacing errors.

Review:

- Whether a light island inside a dark landing has adequate entry and exit space.
- Whether a dark band after a light section feels like a purposeful transition, not a collision.
- Whether global foundation styles contaminate a screen-local surface role.
- Whether the transition changes both mood and density too abruptly.

This is a human visual read. It is not a runtime theme system.

---

## 7. CTA Spacing Rhythm

CTA spacing rhythm governs primary actions, secondary links, trust hints, forms, and follow-up contact blocks.

Review:

- Primary CTAs should have enough isolation to remain the conversion focal point.
- Secondary CTAs should not crowd primary actions or visually equalize them by accident.
- Form fields, helper text, consent text, and submit buttons should use deterministic vertical gaps.
- CTA sections should not be compressed merely to fit a viewport screenshot.

---

## 8. Mobile Vertical Rhythm

Mobile cadence is not desktop spacing divided by guesswork. It requires a smaller but still deterministic rhythm.

Review:

- Heading wraps should not collapse the space between title and body.
- Card stacks should preserve a readable gap between items.
- CTAs should remain tappable and visually isolated.
- Dense technical lists should not become uninterrupted walls.
- Footer groups should have enough spacing for scan and tap.

When mobile source is missing, record **SAFE UNKNOWN** for exact cadence and validate only survivability plus reasonable rhythm based on the project pack.

---

## 9. Forbidden Vertical Rhythm Drift

The following are anti-patterns unless explicitly approved and documented:

| Drift | Why it is unsafe |
|-------|------------------|
| Random section paddings | Destroys page-level cadence and makes QA subjective. |
| Accidental spacing inheritance | Current section spacing comes from globals or neighbors, not the source. |
| Section collision | Adjacent sections visually crash; no transition breathing. |
| Giant dead whitespace | The page loses momentum because spacing expands without narrative purpose. |
| Compressed transitions | Dark/light or dense/sparse boundaries change too abruptly. |
| Inconsistent cadence | Similar section roles use unrelated spacing systems. |
| CTA crowding | Conversion focal point is visually buried by nearby text, cards, or trust elements. |
| Footer suffocation | Footer content lacks terminal breathing and reads cramped or bolted on. |
| Breakpoint spacing improvisation | Mobile/tablet gaps are patched by feel without scale or source authority. |
| Spacing contamination | A previous screen’s rhythm leaks into the next screen and overrides screen-local intent. |
| Same-background spacing duplication | Adjacent same-surface sections accumulate both top and bottom padding until the boundary feels accidental. |
| Isolated-block feeling | Sections look acceptable alone but fail to read as one landing narrative. |

---

## 10. Landing Continuity Pacing

Landing continuity pacing asks whether the page reads as one controlled narrative instead of isolated screens stitched together.

Review:

- Hero sets the first cadence without over-expanding the page.
- Proof and trust sections support the conversion story without density spikes.
- Technical or feature sections do not overtake the visual hierarchy through spacing pressure.
- Lead forms and final CTAs have enough terminal rhythm to feel deliberate.
- Footer closes the landing without suffocation or excessive dead space.

---

## 11. Triumph V2 Lessons Captured

Triumph V2 exposed vertical rhythm risks that this layer now names:

- Global section spacing can shift frozen sections during single-screen work.
- Inter-screen spacing may drift when implementation follows current DOM instead of the active `design/v2/NN.png` cadence.
- Adjacent dense/light middle sequences such as `03 → 04 → 05` require page-level cadence breathing, not isolated per-screen margin fixes.
- Dark/light surface transitions can become harsh when foundation defaults overpower screen-local intent.
- CTA clusters can lose dominance when nearby proof, price, or form material crowds the beat.
- Footer and terminal sections need explicit cadence governance, not leftover spacing.

These are **documentation lessons** and vocabulary for future reviews, not claims of automatic cadence analysis.

---

## 12. Forge Implications

When Forge is selected, vertical rhythm should be reviewed before freeze:

- Run section-spacing and density-continuity checks with the visual reconciliation pass.
- Run cadence continuity, transition pacing, density-stack, footer closure, and mobile cadence survivability checks via [`cadence-governance-checklist.md`](../../agents/mars-forge/cadence-governance-checklist.md).
- Record `CADENCE FINDINGS` for inter-screen narrative pacing and `RHYTHM FINDINGS` for typography / vertical rhythm detail.
- Record `RHYTHM FINDINGS` in REPORT for typography and vertical rhythm.
- Classify pass / partial / fail by section or screen slice.
- Escalate **SAFE UNKNOWN** when spacing authority is unclear.
- Do not silently mass-edit section paddings to “normalize” a page without scoped approval.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Missing spacing pack | No authority for default section cadence. |
| Conflicting visual exports | Adjacent screens imply incompatible transition spacing. |
| Missing mobile source | Mobile cadence cannot be chartered beyond survivability. |
| Current DOM differs from source order | Inter-section rhythm may be based on provisional implementation, not approved sequence. |
| Inherited global spacing unclear | Cannot tell whether the inherited gap is intentional or contamination. |

**Action:** document the resolver: annotated screen, implementation-pack spacing table, operator decision, or section-source matrix update.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-16 | Initial Vertical Rhythm Governance — inter-section cadence, density continuity, anti-random spacing policy, Forge reporting hook. |
| v0.1 | 2026-05-16 | Linked canonical vertical cadence system, cadence tier model, Forge `CADENCE FINDINGS`, and Triumph V2 `03 → 04 → 05` dense/light sequence lesson. |
| v0.2 | 2026-05-18 | Added V4 system-owned rhythm, same-background/different-background transition rules, and isolated-block drift lessons. |
