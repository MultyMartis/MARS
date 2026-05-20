# MARS Website Factory — Visual drift taxonomy

**Status:** **documented** — pattern vocabulary for **human-supervised** visual reconciliation.  
**Not:** automated detection, ML classifiers, screenshot diff, or enforcement engines.

**Parent methodology:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Checklist:** [`../../agents/mars-forge/visual-reconciliation-checklist.md`](../../agents/mars-forge/visual-reconciliation-checklist.md).  
**Icon-specific companion:** [font-awesome-governance-layer.md](font-awesome-governance-layer.md) — semantic fidelity, family consistency, optical rhythm, and icon drift labels.  
**Sibling (structural grouping):** [compositional-structure-awareness.md](compositional-structure-awareness.md), [composition-drift-taxonomy.md](composition-drift-taxonomy.md) — **composition-vs-DOM** mismatch vocabulary; **not** a substitute for this file.

**Purpose:** Name recurring ways builds **diverge in visual intent** while still passing **semantic** checks. Operators and agents use shared labels to report drift without implying pixel metrics.

---

## How to use this doc

- Reference **drift type + short evidence** in REPORT under `VISUAL FINDINGS`.  
- One section may exhibit **multiple** drift types; list the dominant few.  
- Prefer **SAFE UNKNOWN** from [visual-reconciliation-layer.md §7](visual-reconciliation-layer.md) when the source does not support a confident read.

---

## A. Taxonomy (definitions)

| Drift type | Definition | Typical implementation clues |
|------------|------------|--------------------------------|
| **Hierarchy drift** | Relative importance of text blocks differs from source — primary reads secondary or vice versa | Matched font sizes for headline vs subhead; weak weight steps; wrong color tier |
| **CTA dilution** | Primary action does not dominate; CTAs feel **peer-level** | Two equal buttons; outline vs solid inverted; oversized secondary |
| **Density collapse** | Section gains or loses **felt** compactness vs source — often **everything tighter** or **everything airy** | Grid `gap` shrunk/grown vs siblings; paragraph margins homogenized |
| **Accidental equalization** | Sibling items styled to **same visual weight** when source shows **intentional rank** | Cards same elevation, icon size, title size for “first” vs “rest” |
| **Visual flattening** | Page/section reads as **one plane** — no focal depth | Uniform backgrounds; no contrast bands; borders all-or-none |
| **Trust displacement** | Proof/trust cluster **steals** focal path or sits in **wrong narrative order** vs source | Trust strip above-the-fold competitor to hero CTA; logos oversized |
| **Spacing inflation** | Vertical rhythm **stretches**; sections feel **disconnected** or list-like | Large default `margin-bottom` stacks; token mismatch |
| **Over-centering** | Everything stacks **symmetrically** when source is **weighted** | Auto-centered text blocks where source is left-weighted + media offset |
| **Symmetry drift** | Layout **over-balanced** left/right vs deliberate **asymmetry** in source | 50/50 columns where source is 40/60 or offset grid |
| **Visual noise** | Extra borders, icons, badges, or dividers **compete** with primary message | Decorative rows not in source; redundant labels |
| **Composition collapse** | **Flow** breaks — eye traps, orphaned blocks, unclear scan path | Wrong column order on stack; imagery facing out of flow |
| **Focal competition** | Two or more elements **fight** for first fixation within one band | Dual CTAs + large visual + trust logos in one viewport |
| **Foundation contamination bias** | **Global foundation defaults** (site-wide theme, inherited surfaces, prior-section styling) **silently overpower** chartered **screen-local** visual role — often **semantic PASS**, **visual FAIL** vs source. *Expanded entry:* [§D](#d-foundation-contamination-bias--expanded-taxonomy-entry). | Dark global foundation applied to a **light** screen composition; CTA/typography/trust tokens inherited mechanically; section loses intended contrast band vs neighbors |
| **Icon rhythm / semantic drift** | Icon selection, weight, or alignment weakens the intended visual and semantic read. Use detailed labels from [font-awesome-governance-layer.md §8](font-awesome-governance-layer.md#8-icon-drift-taxonomy). | Same-looking glyph reused for different meanings; `fal`/`fas` mixed without role boundary; icon column wobbles; decorative icons compete with CTA/copy |

---

## B. Triumph V2 — reference illustrations (documentation lessons)

These tie taxonomy labels to **documented** Triumph Manipulator Landing V2 governance — **not** to automated proof.

| Lesson (from project docs) | Drift types it exemplifies |
|----------------------------|----------------------------|
| **Fleet / multi-card semantics vs one-machine flow** ([V2-CLEANUP-DECISION-LOG.md](../triumph-manipulator-landing/V2-CLEANUP-DECISION-LOG.md) — `equipment-prices` quarantine, matrix conflicts) | **Accidental equalization**, **density collapse**, **hierarchy drift** — catalog grids normalize sibling weight and **flatten** a hero-first story. |
| **Archive / V1 vs active V2** (forbidden paths; version isolation) | **Composition collapse**, **trust displacement** when **wrong-era** proof or layout order leaks in. |
| **Semantic contamination** (cleanup log §7 — mixed-era residue) | **Visual noise**, **focal competition** — extra blocks add **competing** anchors. |
| **Hero vs supporting role** enforced in semantic lock but needing **visual read** | **CTA dilution**, **over-centering** if hero CTAs are styled like footer links. |
| **Screen 02 — light composition vs global dark foundation** ([§D expanded entry](#d-foundation-contamination-bias--expanded-taxonomy-entry)) | **Foundation contamination bias**, often with **visual flattening** or wrong **section emphasis** if dark chrome overpowers light hierarchy. |
| **Triumph V2 icon-bearing rebuild areas** (trust strip, specification rows, CTA/support icons, prohibition/transport lists, social/contact icons) | **Icon rhythm / semantic drift** when FA glyphs are visually plausible but semantically weak, mixed-weight, or optically uneven. |

**SAFE UNKNOWN reminder:** If `design/v2` (or active charter path) does not show breakpoint behavior, do not invent **mobile emphasis** — record gap per [visual-reconciliation-layer.md §7](visual-reconciliation-layer.md).

---

## C. Disposition mapping (non-normative hint)

| Severity hint | Example dispositions |
|---------------|---------------------|
| **Blocking for freeze** | CTA dilution on hero; trust displacement breaking focal path on primary viewport |
| **Partial / defer** | Minor spacing inflation in supporting section; tablet-only symmetry drift with **recorded** follow-up |
| **Non-blocking note** | Subtle noise element that does not change hierarchy; still document |

Exact blocking authority remains **project HITL** and factory freeze rules — this table is **reporting guidance** only.

---

## D. FOUNDATION CONTAMINATION BIAS — expanded taxonomy entry

**Canonical example (documentation):** Triumph Manipulator Landing **V2 Screen 02** — chartered source describes a **light surface**, **white cards**, and **light composition hierarchy**; an interpreter that defaults to the site’s **global dark foundation** can ship a build that remains **semantically acceptable** and **structurally stable** yet **visually wrong** relative to the screen export.

**Governance rule (interpretation discipline, not runtime):** When the canonical screen source clearly indicates a visual role that differs from pipeline or site-wide defaults, **screen intent overrides foundation defaults** — as a **human-supervised** production read, **not** a theme engine, dynamic styling product, or autonomous visual adaptation.

### Definitions (vocabulary)

| Term | Meaning |
|------|--------|
| **Foundation layer** | Site-wide or workflow-default visual assumptions applied **before** or **without** a disciplined screen-local read: global tokens, default section shells, dominant site chrome (e.g. dark page frame), default typography mood, “usual” component variants chosen for **cross-page consistency**. |
| **Screen-local visual intent** | The chartered visual **role** of **this** screen/section per approved exports and implementation pack: surface treatment (light vs dark band), card/frame treatments, hierarchy mood, contrast relative to adjacent narrative, spacing rhythm **for this beat**. |
| **Contamination** | Foundation-layer defaults **overwrite** or **mask** screen-local intent **without charter alignment** — yielding correct semantics and stable structure but **incorrect emphasis and atmosphere** vs source. |
| **Visual inheritance drift** | Mechanical carry-forward of styling from **global theme**, **previous sections**, or **neighboring screens** so the section **reads as inherited** rather than **authored to this screen’s source**. |

**Clarification:** A **globally coherent** design system can still produce **wrong screen interpretation** if the agent applies **global defaults** instead of reading **local screen role**. Consistency with “how the rest of the site usually looks” is **not** proof of fidelity to **this** export.

### Symptoms

- Dark (or heavy) **surface** inherited into a composition that the source shows as **light** — or the inverse.
- **CTA styling** matches the previous section or global primary pattern while the source expects a **local** emphasis tier (e.g. quiet secondary on a light panel).
- **Typography mood** (weight, contrast, “marketing shout” vs editorial calm) inherited from site defaults; headline/body relationships feel **global**, not **screen-native**.
- **Section rhythm** applied mechanically (same vertical cadence, same band rules) where the source **breaks** rhythm for contrast or narrative reset.
- **Trust / proof** styling copied from another screen (strip density, logo scale, bar treatment) **leaking** into a section with a different proof role.
- **Contrast role** lost: the screen should read as **reset**, **breathing room**, or **inversion** vs neighbors, but the build **blends** into the surrounding foundation.

### Causes

- **Single global skin** assumed for all sections without per-screen **surface read**.
- **Order-of-implementation bias**: previous section’s tokens reused for speed or “consistency.”
- **Strong site brand defaults** (dark UI frame, accent rules) applied **before** checking the export’s **local band**.
- **Missing explicit** implementation-pack note for **exceptions** to global rules (light island inside dark site, etc.).

### Examples

| Example | Note |
|---------|------|
| **Triumph V2 Screen 02** | **Canonical documentation example:** light surface + white cards + light hierarchy in source; build interpreted through **global dark site foundation** → acceptable semantics, wrong visual role. |
| Dark hero DNA on a light catalog band | Global hero tokens spill into non-hero screen |
| Neighbor trust strip styling on an editorial block | Trust **visual language** copied; focal path shifts |

### Mitigation guidance

- **Anchor first** to the **chartered screen** (export + pack): explicitly note **surface**, **card/frame**, and **hierarchy mood** before choosing tokens.
- **State the override:** when source contradicts global defaults, record in REPORT that **screen-local intent** governed token choice (still **no** unapproved redesign).
- **Per-screen reconciliation:** compare build to **this** export, not to “last section” or “default theme.”
- **Typed drift:** label **Foundation contamination bias** in `VISUAL FINDINGS` so reviewers see inheritance vs hierarchy-only issues.
- **SAFE UNKNOWN** when local role is unclear — do **not** guess light vs dark or mood from globals alone (see [visual-reconciliation-layer.md §7](visual-reconciliation-layer.md)).

---

## E. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial taxonomy + Triumph V2 doc tie-ins. |
| v0.1 | 2026-05-16 | **Foundation contamination bias** — table row, expanded §D, Screen 02 illustration link. |
| v0.2 | 2026-05-16 | Added icon rhythm / semantic drift pointer to Font Awesome governance layer. |
