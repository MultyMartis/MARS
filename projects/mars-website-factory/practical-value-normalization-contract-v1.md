# Website Factory Practical Value Normalization Contract v1

**Status:** **documented** — canonical contract between visual evidence extraction and production token proposal.  
**Not:** runtime normalizer, automated rounding engine, or project-specific px truth.

**Authority chain:**

| Rank | Document | Role |
|------|----------|------|
| 1 | Project Site-Wide Style Foundation (per project) | Approved production tokens for that project |
| 2 | [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §3 OL-01 | Approved Operator spacing scale |
| 3 | **This contract** | Normalization procedure, traceability, exception rules |
| 4 | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Detail under OL-01 |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Supersedes:** ad-hoc “round to nice numbers” behavior without traceability. Does **not** supersede OL-01 or project foundation when approved.

---

## Purpose

Translate **observed** design measurements into **production-stable** values without losing evidence. Prevents mechanical JPEG-to-CSS transfer and prevents arbitrary per-block magic numbers.

Normalization sits **after** Design Foundation Extraction and **before** Site-Wide Style Foundation approval.

---

## Inputs

| Input | Required | Source |
|-------|----------|--------|
| Grounded visual audit | Yes | Project audit artefacts (e.g. JPG visual audit + grounding review) |
| Design foundation extraction | Yes | Observed families only — no production values |
| Operator production rules | Yes | OL-01 via [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md); operator directives |
| Practical spacing scale | Yes | OL-01 gap/margin scales unless project foundation overrides |

**Forbidden inputs for project values:** legacy project workspaces, superseded audits, FIG/PDF when project policy forbids them.

---

## Outputs

| Output | Description |
|--------|-------------|
| Normalized token proposal | Named tokens with proposed px values |
| Exception register | Values outside scale with evidence + approver slot |
| Source-to-value traceability table | Evidence ID → observed → normalized → reason |
| `REQUIRES OPERATOR APPROVAL` flags | Where foundation is proposal-only |

---

## Core rule

**Identical semantic visual patterns must receive identical production values.**

Examples of semantic pattern classes:

- same-bg section continuation gap
- standard content section vertical padding
- 3-column card grid gap
- primary CTA button height family
- H2 section heading block

Different component classes (e.g. compact FAQ row vs hero CTA band) may map to different tokens when JPG evidence shows distinct families.

---

## Value classes

| Class | Meaning |
|-------|---------|
| **exact source value** | Observed measurement recorded as evidence only — not shipped to CSS without normalization step |
| **normalized production value** | Mapped to OL-01 scale or approved project token |
| **calculated responsive value** | Derived from desktop token + project responsive rule (document formula) |
| **exceptional value** | Outside scale — requires exception register row + operator approval |
| **SAFE UNKNOWN** | Pattern visible but measurement or class not provable — no CSS value |

---

## Default practical spacing scale

**Canonical Factory scale (OL-01):**

**Gap** (`gap`, `grid-gap`, `column-gap`, `row-gap`):

`5` · `10` · `20` · `30` · `40` · `50` · `70` (px)

**Margin / padding:**

`5` · `10` · `15` · `20` · `25` · `30` · `40` · `50` · `70` · `90` (px)

**Production anchors (primary normalization targets):**

`20` · `30` · `50` · `70`

**Extended scale (full OL-01 list above)** — use when anchors do not fit evidence band.

Values outside scale are allowed only as:

- technical necessity (browser subpixel, 1px hairline border)
- exact geometric constraint provable from source (component intrinsic size)
- component-specific dimension (icon box, avatar) with component binding
- pixel-perfect exception with operator approval
- documented SAFE UNKNOWN hold — no value until resolved

---

## Normalization procedure

1. Record **observed range** per pattern family in Design Foundation Extraction — no production px.
2. Classify pattern (section padding, grid gap, card padding, heading-to-content, etc.).
3. Map to **nearest** OL-01 value **toward** scale center — not “prettier” arbitrary values.
4. Record **delta** and **confidence**.
5. If two families collapse to one token, verify JPG shows same semantic class.
6. If families differ visually, **do not** force one token.
7. Emit proposal row; mark `REQUIRES OPERATOR APPROVAL` until Site-Wide Style Foundation is operator-approved.

---

## Normalization examples (mechanism only — not auto-rules)

| Observed | Normalized candidate | Notes |
|----------|---------------------|-------|
| 18–22px | 20px | Anchor band |
| 27–33px | 30px | Anchor band |
| 46–54px | 50px | Anchor band |
| 64–76px | 70px | Anchor band |
| 47–54px section padding | 50px | Requires same-bg/diff-bg rhythm check per [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) |

These are **illustrations**. Operator must confirm against visual deviation tolerance.

---

## Prohibited behavior

| Prohibited | Why |
|------------|-----|
| Local random gap without component reason | Breaks semantic consistency |
| Different values for same semantic pattern | Token drift |
| Direct JPEG measurement → CSS without normalization row | No traceability |
| Universal rounding without visual deviation check | False precision |
| New token per block without family justification | Foundation bloat |
| QA fix via arbitrary magic numbers | Bypasses foundation |
| Importing legacy project px as V6 truth | Violates clean-room policy |
| Duplicate base container geometry per block | Violates Single Base Container Law — [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) §4 |
| Section-boundary padding on first/last internal child | Violates Section Owns Its Rhythm Law — [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) §2.6 |

---

## Traceability table (required per project)

| Evidence ID | Observed value | Pattern class | Normalized value | Delta | Reason | Confidence | Exception |
| ----------- | -------------- | ------------- | ---------------- | ----- | ------ | ---------- | --------- |

Store in project `*-PRACTICAL-VALUE-NORMALIZATION.md` and reference from Site-Wide Style Foundation.

---

## Gate integration

| From | To | Gate |
|------|-----|------|
| Design Foundation Extraction | Practical Value Normalization | Extraction complete; observed families documented |
| Practical Value Normalization | Site-Wide Style Foundation | Traceability table complete; exceptions flagged |
| Site-Wide Style Foundation | Block Implementation Specification | `implementation_authorized: false` until operator approval |

**STOP:** Block HTML/SCSS if spacing/type/color value lacks foundation token or registered exception.

**CSS Variable First Law:** [css-variable-first-law-v1.md](css-variable-first-law-v1.md) — production SCSS must use `var(--token)` after lookup; arbitrary px without classification is a gate violation.

---

## Relationship to legacy FP-0002 materials

[frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md) §4 references FP-0002 v3 Production Standards — **LEGACY for FP-0002 V6**. V6 projects must derive values from JPG evidence + this contract + operator approval only.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Cross-layer audit; connects audit → normalization → foundation pipeline |
| 2026-06-22 | v1.1 — Link CSS Variable First Law at SCSS gate |
