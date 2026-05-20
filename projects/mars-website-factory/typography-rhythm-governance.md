# MARS Website Factory — Typography Rhythm Governance

**Status:** **documented** — governance and production **methodology** only.  
**Not:** runtime typography engine, autonomous enforcement, automatic cadence analysis, or universal typographic truth.

**Purpose:** Formalize a deterministic typography rhythm model for Website Factory landing production so headings, paragraphs, CTAs, and supporting text keep a readable cadence across a page instead of drifting through arbitrary line-height math.

**Forge checklist:** [`../../agents/mars-forge/rhythm-governance-checklist.md`](../../agents/mars-forge/rhythm-governance-checklist.md).  
**Related visual layer:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md).  
**Related vertical layer:** [vertical-rhythm-governance.md](vertical-rhythm-governance.md).

---

## 1. Positioning

Typography rhythm governance is a **preferred Website Factory operational rhythm model**, especially suitable for **marketing landing systems** where a single page must keep strong hierarchy, fast readability, and predictable scan cadence.

It is **not** a claim that every project must use this forever. A project may define another approved rhythm model in its implementation pack, but it must be explicit, consistent, and reviewable. Silent mixed systems are drift.

---

## 2. Preferred Landing Rhythm Model

### 2.1 Canonical rule

For Website Factory landing work, the preferred deterministic line-height rule is:

```text
line-height = font-size + 4px
```

Examples:

| Font size | Preferred line-height |
|-----------|------------------------|
| `48px` | `52px` |
| `32px` | `36px` |
| `24px` | `28px` |
| `20px` | `24px` |
| `16px` | `20px` |

This model creates a simple **4px readability buffer** around text rows. It keeps headings compact without forcing decimal multipliers, and keeps paragraph/list text readable without random leading.

### 2.2 Allowed project variation

Variation is allowed only when an approved project implementation pack states a different rule for a named text role or breakpoint. The variation must be:

- **Named** — e.g. `hero-display-tight`, `button-single-line`, `legal-caption`.
- **Scoped** — section, component, or breakpoint clear.
- **Reviewable** — visible in QA notes or implementation pack.
- **Consistent** — not a one-off value invented during visual nudging.

---

## 3. Typography Cadence

### 3.1 Heading cadence

Heading cadence governs the ladder between `h1`, `h2`, `h3`, card titles, eyebrow text, and CTA labels. The operator should read:

- Whether the heading scale descends predictably from hero to supporting sections.
- Whether line-height follows the preferred model or a named approved exception.
- Whether heading blocks keep comparable title → subtitle → body spacing across landing sections.
- Whether mobile heading reductions preserve hierarchy without producing crowded wraps.

### 3.2 Paragraph cadence

Paragraph cadence governs body copy, lead text, lists, captions, and helper labels. The operator should read:

- Whether body and list text use deterministic line-height, not inherited browser defaults.
- Whether paragraph stacks keep a repeatable text rhythm inside cards, bands, and forms.
- Whether dense sections reduce content volume before compressing line-height below readability.
- Whether caption and metadata text remain legible rather than being squeezed to save vertical space.

### 3.3 Operational readability

Operational readability means a landing page can be scanned without typography forcing the eye to re-learn rhythm on every section. It is a governance target, not a conversion guarantee.

Readability failures include text that feels mechanically correct in isolation but becomes exhausting across the full landing because each section uses different line-height logic, title spacing, or paragraph beat.

---

## 4. Typography Continuity Across Landing

A landing page should preserve a recognizable typography pulse across:

- Hero headline → next-section heading.
- Section heading → section body.
- Card title → card body.
- CTA label → nearby proof or helper text.
- Desktop → tablet → mobile breakpoints.

The goal is **continuity**, not sameness. A hero can be larger and tighter than a supporting paragraph, but the underlying rhythm model should remain legible and explainable.

---

## 5. Forbidden Typography Drift

The following are anti-patterns unless explicitly approved and documented in the project implementation pack:

| Drift | Why it is unsafe |
|-------|------------------|
| Arbitrary `53px`, `57px`, `61px` line-heights | Creates unreviewable typography math and cross-section cadence breaks. |
| Random decimal rhythm | Values such as `1.08` or `1.13` hide actual pixel cadence and drift across sizes. |
| `line-height: 1.08` | Usually too tight for landing headings/body unless a named design exception exists. |
| `line-height: 1.13` | Looks intentional but often becomes arbitrary when mixed with px values. |
| Uncontrolled typography math | Operators cannot tell whether the value came from design, code inheritance, or guesswork. |
| Mixed cadence systems | One section uses px, another uses decimals, another inherits default line-height. |
| Accidental inheritance drift | Typography changes because a parent selector, reset, or global class leaks into a section. |
| Breakpoint-only line-height improvisation | Mobile values invented during responsive fixes without preserving the rhythm model. |

---

## 6. Triumph V2 Lessons Captured

Triumph V2 exposed the need for typography rhythm governance through production observations:

- Random line-height values make visual reconciliation harder because the page may be semantically correct but typographically unstable.
- Arbitrary typography math creates inconsistent heading cadence across screen slices.
- Landing continuity weakens when each section has its own invisible line-height logic.
- Dense marketing sections should resolve pressure through content/layout decisions before compressing text rhythm.

These are **documentation lessons**, not a claim that MARS has automated typography analysis or runtime correction.

---

## 7. Forge Implications

When Forge is selected, typography rhythm should be reviewed as part of pre-freeze QA:

- Check heading cadence and paragraph cadence against the project implementation pack.
- Prefer the `font-size + 4px` model unless the project pack defines a named exception.
- Record `RHYTHM FINDINGS` in REPORT when typography cadence is pass / partial / fail.
- Treat unknown typography authority as **SAFE UNKNOWN**, not a silent inheritance guess.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Missing typography pack | Cannot verify whether the preferred model or a project-specific model governs. |
| Conflicting design exports | Different screens imply different heading or paragraph cadence for the same role. |
| Raster source is unreadable | Line-height cannot be inferred reliably from a blurred or cropped export. |
| Global CSS conflicts with pack | Cannot know whether inherited rhythm is intentional or contamination. |
| Mobile typography not specified | Breakpoint cadence cannot be chartered beyond responsive survival. |

**Action:** document what would resolve it: implementation-pack typography table, annotated export, token decision, or explicit HITL approval.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-16 | Initial Typography Rhythm Governance — preferred landing rhythm model, anti-random line-height policy, Forge reporting hook. |
