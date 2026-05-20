# MARS Website Factory — Source Ambiguity Taxonomy

**Status:** **documented** — ambiguity and drift vocabulary for human-supervised source interpretation.  
**Not:** automated ambiguity detection, screenshot diff, CV taxonomy, runtime source-reading engine, or universal design truth.

**Purpose:** name common ways source interpretation collapses into drift so Forge and Website Factory reports can surface uncertainty instead of hiding it.

**Companion documents:** [source-interpretation-governance.md](source-interpretation-governance.md), [source-confidence-model.md](source-confidence-model.md).  
**Forge checklist:** [`../../agents/mars-forge/source-interpretation-checklist.md`](../../agents/mars-forge/source-interpretation-checklist.md).

---

## 1. Taxonomy Use

Use this taxonomy when:

- A screenshot, source matrix, implementation pack, or design export can be read more than one way.
- A visible detail may be artifact, noise, accident, or undocumented design intent.
- Implementation would require invented hierarchy, grouping, interaction, asset, or responsive behavior.
- A confident implementation report would hide missing source authority.

Each finding should include:

```text
Pattern:
Source evidence:
Confidence:
Implementation risk:
Disposition: proceed | approximate with disclosure | SAFE UNKNOWN | HITL | stop
Resolver:
```

---

## 2. Ambiguity / Drift Patterns

| Pattern | Definition | Typical risk | Required response |
|---------|------------|--------------|-------------------|
| **Screenshot hallucination** | Reading structure, state, interaction, copy, or component logic from pixels that do not prove it. | Invented UX or markup. | Label confidence; escalate if material. |
| **Inferred semantics drift** | Weakly implied meaning becomes implemented as explicit source truth. | Wrong story, CTA, entity, or role. | Use confidence model; SAFE UNKNOWN if source cannot confirm. |
| **Accidental redesign** | Implementation “improves” unclear source instead of preserving or escalating. | Unapproved creative change. | Stop redesign; request HITL or source clarification. |
| **Fake hierarchy extraction** | A visual size/color relationship is converted into a semantic or content hierarchy without enough evidence. | Wrong headings, card priority, CTA weight. | Distinguish visual read from semantic authority. |
| **Missing mobile assumptions** | Desktop-only source is treated as full responsive specification. | Fake mobile hierarchy, collapse drift. | SAFE UNKNOWN or HITL for material breakpoint behavior. |
| **False grouping** | Proximity, accidental alignment, or screenshot crop is treated as confirmed composition grouping. | Wrong wrappers, cards, or cluster behavior. | Cross-check composition awareness; report inferred grouping. |
| **Invisible-source guessing** | Hidden states, below-fold regions, hover, modal, animation, or content not visible in source are guessed. | Invented interaction or missing content. | Stop when behavior is material; request source. |
| **Overconfident interpretation** | Report language presents weak implication or ambiguity as certainty. | False PASS / freeze. | Downgrade confidence and disclose ambiguity. |
| **Visual ambiguity collapse** | Multiple credible visual reads are collapsed into one without reporting alternatives. | Misread layout, density, dominance, surface role. | Record alternatives; choose only with source/HITL authority. |
| **Screenshot literalism** | Every pixel-level detail is copied as design law, including artifacts and accidental spacing. | Brittle CSS, wrong spacing, noise replication. | Treat low-confidence details as approximation. |
| **Asset hallucination** | Icons, images, logos, illustrations, or decorative assets are invented or replaced without source authority. | Brand drift, semantic icon mismatch. | Use approved assets or mark SAFE UNKNOWN. |
| **Invented interaction logic** | Tabs, forms, accordions, sliders, hover states, sticky behavior, validation, or JS flow are created from incomplete source. | UX behavior absent from charter. | HITL required unless handoff explicitly defines behavior. |
| **Source contradiction masking** | Conflicting approved-looking sources are silently reconciled by taste. | Wrong version, mixed source, hidden SoT conflict. | Report contradiction; apply priority model or HITL. |
| **Undocumented intent inflation** | A plausible intent is treated as documented intent. | Implementation overclaims fidelity. | Mark inferred/assumed; do not freeze as fully source-proven. |
| **Interpretation contamination** | Prior versions, old PDFs, global foundation, neighboring sections, or previous sessions bias the current source read. | Cross-version drift or foundation contamination. | Re-anchor to active charter; quarantine contamination. |
| **Hallucinated structure** | New wrappers, sections, cards, lists, catalogs, pricing grids, or page flows are invented. | Structural drift and accidental redesign. | Stop unless STRUCTURE CHANGE / HITL approves. |

---

## 3. Screenshot Detail Authority

Not every visible screenshot detail is authoritative.

| Detail type | Interpretation posture |
|-------------|--------------------------|
| **Raster artifacts** | Do not implement as borders, shadows, gradients, or texture without corroboration. |
| **Compression noise** | Treat as non-authoritative visual noise. |
| **Export artifacts** | Do not infer design tokens from export errors. |
| **Accidental alignment** | Do not convert into grid law unless repeated or documented. |
| **Hidden responsive intent** | Desktop source cannot prove mobile collapse by itself. |
| **Missing hover states** | No hover / active / focus behavior may be invented as source truth. |
| **Absent interaction states** | Tabs, modals, forms, sliders, and validation states require explicit authority. |
| **Low-resolution spacing** | Use approximate spacing with disclosure or source pack tokens. |
| **Cropped regions** | Do not infer section boundaries or below-fold content from cropped source. |

---

## 4. Severity

| Severity | Meaning | Example |
|----------|---------|---------|
| **S0 — note** | Ambiguity exists but does not affect implementation choice. | Tiny raster noise in decorative background. |
| **S1 — report** | Implementation can proceed with disclosed approximation. | Weak spacing read where design tokens provide safe fallback. |
| **S2 — partial / HITL** | Ambiguity affects hierarchy, grouping, responsive intent, CTA, asset, or state. | Missing mobile source for dense CTA cluster. |
| **S3 — stop** | Implementation would invent meaning, structure, interaction, or source authority. | Adding a pricing catalog absent from source. |

---

## 5. Anti-Patterns

Forbidden ambiguity handling:

- Pretending certainty.
- Silent guessing.
- Screenshot worship.
- Inferred certainty inflation.
- Collapsing contradictory sources into taste-based decisions.
- Inventing hierarchy or UX to “complete” a screenshot.
- Treating desktop screenshots as full responsive truth.
- Reporting PASS when material source confidence is weak, ambiguous, unknown, or contradictory.
- Implementing approximation without disclosure.

---

## 6. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial source ambiguity taxonomy for Website Factory interpretation governance. |
