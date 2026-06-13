# MARS Website Factory — Frontend Production Authority Order v1

**Status:** **documented** — canonical **decision hierarchy** for Website Factory frontend production.  
**Not:** runtime enforcement, CI gate, linter, or project-specific token values.

**Purpose:** Fix the official order in which frontend production decisions are resolved. Website Factory is built around **operator production practice** and **accumulated real-project experience** — not generic industry defaults or agent improvisation.

**Supersedes (interpretation only):** Any implicit hierarchy that ranked **Industry Best Practice** or **Agent Preference** above **Project Production Standards** or **Approved Operator Laws**.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Project instances (read-only):** FP-0002 v3, SITE-001 governance artefacts — **do not edit** for Factory evolution.

---

## 1. Canonical authority hierarchy

When resolving a frontend production decision, apply sources **in this order** — higher levels **always** beat lower levels on conflict:

| Rank | Authority layer | What it is | Primary documents |
|------|-----------------|------------|-------------------|
| **1** | **Project Production Standards** | Lead-approved per-project SSOT — px, hex, radius, breakpoints, typography exceptions, layout zone bindings | `<PROJECT>-PRODUCTION-STANDARDS-APPROVAL-vN.md` · [production-standards-governance-v1.md](production-standards-governance-v1.md) |
| **2** | **Approved Operator Laws** | Factory-fixed production laws derived from operator practice — **this doc §3 (OL-01–OL-07)** | This document |
| **3** | **Website Factory Governance** | Factory process, gates, precision packs, invariants, shell-first, calibration | [frontend-production-rules-v0.md](frontend-production-rules-v0.md) · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) · [production-standards-governance-v1.md](production-standards-governance-v1.md) · related `*-governance.md` |
| **4** | **Website Factory Layout Pattern Library** | Named layout patterns — pick, don't invent column math | [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) · WF-GRID · WF-LAYOUT · reference workspace patterns |
| **5** | **Industry Best Practices** | Generic web/CSS/accessibility conventions (mobile-first defaults, rem stacks, Bootstrap habits, Lighthouse heuristics, etc.) | **Advisory only** — never override ranks 1–4 |
| **6** | **Agent Preference** | Model convenience, “cleaner look,” template habit, unstated assumptions | **Forbidden as override** — never override ranks 1–5 |

```text
Project Production Standards
        ↓ wins over
Approved Operator Laws (OL-01–OL-07)
        ↓ wins over
Website Factory Governance
        ↓ wins over
Layout Pattern Library (LP-* / WF zones)
        ↓ wins over
Industry Best Practices
        ↓ wins over
Agent Preference
```

---

## 2. Critical conflict rules

These rules are **non-negotiable** for all Website Factory frontend work:

| Conflict | Winner | Agent action on violation |
|----------|--------|----------------------------|
| **Project Production Standards** vs **Agent Preference** | **Project Production Standards** | **STOP** — implement project SSOT; do not “improve” silently |
| **Approved Operator Law** vs **Industry Best Practice** | **Approved Operator Law** | **STOP** — cite OL-*; escalate HITL only if project SSOT must override OL |
| **Project Production Standards** vs **Approved Operator Law** | **Project Production Standards** | Use project value; record in Production Decisions (C-12) |
| **Approved Operator Law** vs **Factory Governance detail** | **Approved Operator Law** | OL-* wins when this doc and a governance pack disagree on the same numeric/layout rule |
| **Factory Governance** vs **Industry Best Practice** | **Factory Governance** | Never substitute generic best practice for Factory gate or precision rule |
| **Layout Pattern Library** vs **ad-hoc `%` splits** | **Layout Pattern Library** (or OL-04) | Pick LP-* / fr / minmax — not eyeball percentages |

**Agent Preference (rank 6) never overrides ranks 1–5.** If an agent cannot cite an authority at rank 1–5 for a production value → **STOP** and escalate HITL.

---

## 3. Approved Operator Laws

The following **Operator Laws (OL)** are **Approved Operator Laws** — rank **2** in the hierarchy. They encode production practice validated across real Factory projects. Individual laws may be **narrowed or overridden** only by **Project Production Standards (rank 1)** with explicit decision record.

---

### OL-01 — Spacing Scale

**Gap** (`gap`, `grid-gap`, `column-gap`, `row-gap`) — **use only:**

`5` · `10` · `20` · `30` · `40` · `50` · `70` (px)

**Margin / padding** — **use only:**

`5` · `10` · `15` · `20` · `25` · `30` · `40` · `50` · `70` · `90` (px)

**Interpretation:** Design measurements map to the **nearest** scale value. **Arbitrary values are forbidden.**

**Cross-ref:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2.

---

### OL-02 — Percentage Padding

**Allowed values:** `5%` · `10%` · `15%` · `20%` · `30%`

**Scope:** Large internal containers and sections only — volumetric inner padding where proportion matters.

**Forbidden:** Percentage **grid column splits** (see OL-04).

**Cross-ref:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2.3.

---

### OL-03 — Layout Pattern First

**Forbidden:** Assembling layout “by eye” without a named pattern.

**Required sequence:**

1. Determine **Layout Pattern** (LP-* ID or WF zone type).  
2. Apply the pattern (grid/flex grammar from pattern library or Production Standards C-11).  
3. Place content inside the pattern structure.

**Cross-ref:** [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §6.

---

### OL-04 — No Arbitrary Grid Splits

**Forbidden as default:**

- `65% 35%` · `70% 30%` · `60% 40%` · and similar ad-hoc percentage column splits.

**Use instead:**

- `fr` · `minmax` · `repeat` · or **approved Layout Patterns** (LP-* / WF-LAYOUT zone).

Percentage splits require documented exception per WF-LAYOUT-007 **and** project Lead acknowledgment.

**Cross-ref:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §6.1 · WF-LAYOUT-002 · WF-LAYOUT-007.

---

### OL-05 — Typography Precision

**Body text default:**

`line-height = font-size + 4px`

**Headings default:** Same rule — unless **Project Production Standards** approve a different value for a named heading tier, selector, or breakpoint.

**Priority:** **Project Production Standards win** over this default when both define the same token.

**Cross-ref:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3 · [typography-rhythm-governance.md](typography-rhythm-governance.md).

---

### OL-06 — No Word Breaking

**Forbidden without direct operator instruction:**

- `letter-spacing` (non-zero)  
- `word-break` (any value)  
- `overflow-wrap: break-word`  
- `hyphens` (including `hyphens: auto`)

**Overflow resolution:** Layout and copy fixes first — see [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md).

**Cross-ref:** [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §4.

---

### OL-07 — Russian HTML Typography

**Typograph at HTML level:**

- Headings · body text · buttons · links · cards · forms

**Do not typograph:**

- `meta` · code · class names · `data-*` · URLs · email · `href` values · technical / JSON-LD / service data

**Cross-ref:** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §5.

---

## 4. Relationship to Factory governance packs

| Document | Role under this order |
|----------|----------------------|
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Process for **rank 1** authorship, approval, freeze |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | **Rank 3** detail — implements OL-01, OL-02, OL-05, OL-06, OL-07 in precision pack form |
| [frontend-production-rules-v0.md](frontend-production-rules-v0.md) | **Rank 3** operator consolidation — must defer to this authority order |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | **Rank 3** start gate — does not override project SSOT |
| [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) | **Rank 4** pattern obligation — supports OL-03, OL-04 |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | **Rank 3** — design source extraction, layout transfer chain, Mapping QA gate |

**Duplication note:** OL-* are the **canonical Operator Law statements**. Precision governance **must not** be read as a parallel authority above Project Production Standards.

---

## 5. Agent / operator behavior

| Situation | Required response |
|-----------|-------------------|
| Agent prefers `mobile-first` but project SSOT says **desktop-first** | **Desktop-first** — rank 1 wins |
| Generic “use rem for accessibility” vs project **px** type table | **Project px table** — rank 1; rem is rank 5 |
| Design export ≈ 64px gap | Map to **70px** (OL-01) — not agent round to 60px |
| Agent wants `grid-template-columns: 65% 35%` | **Reject** (OL-04) — use fr pattern unless project SSOT + exception |
| Conflict between OL and unapproved chat suggestion | **STOP** — cite rank 1–4 source |
| Value not on any rank 1–5 authority | **STOP** — HITL; do not ship |

**REPORT expectation:** When resolving a non-obvious conflict, cite **authority rank + document** (e.g. `Authority: FP-0002 v3 §7 radius — rank 1` or `Authority: OL-01 spacing — rank 2`).

---

## 6. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Frontend Production Authority Order: canonical 6-layer hierarchy; Approved Operator Laws OL-01–OL-07; critical conflict rules; agent stop behavior. |
