# MARS Website Factory — Frontend Precision Governance v1

**Status:** **documented** — mandatory **Factory-level** precision rules for design-to-production normalization, pre-flight, and QA.  
**Not:** runtime linter, CI gate, automated px audit, or project-specific token values.

**Purpose:** Stop AI improvisation during layout and typography work. Fix deterministic, high-quality frontend production rules before multi-page work (e.g. FP-0002 M2).

**Authority chain:** Canonical 6-layer order — [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md). **This doc is rank 3 (Factory Governance detail)** — not rank 1.

| Rank | Layer | Role |
|------|-------|------|
| **1** | Project Production Standards (approved) | **Wins** all conflicts below — per-project SSOT |
| **2** | Approved Operator Laws (OL-01–OL-07) | Operator production law — see authority-order doc §3 |
| **3** | **This doc** + related Factory governance | Precision normalization, scales, forbidden patterns — default until rank 1–2 apply |
| **4** | Layout Pattern Library (LP-* / WF zones) | Named patterns before ad-hoc column math |
| **5–6** | Industry Best Practice · Agent Preference | **Never** override ranks 1–4 |

**Specialized (detail under rank 3):** [typography-rhythm-governance.md](typography-rhythm-governance.md), [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md), [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md), WF-GRID, WF-LAYOUT — cited here, not duplicated.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Project instance (read-only):** FP-0002 v3 remains its own SSOT — **do not edit** for Factory evolution.

---

## 1. Design-to-Factory normalization

When translating design exports (Figma, PDF, PNG) into production CSS/HTML:

| Rule | Behavior |
|------|----------|
| **Nearest approved value** | Map raw px to the **closest** value on the approved Factory scale (§2–§3). Example: design ≈ 64px → **70px**; design ≈ 48px → **50px**. |
| **No invented numbers** | Values like `64px`, `72px`, `80px`, `53px` line-height, `1.08` unitless ratios are **forbidden** unless the **Project Production Standards** document names them as approved tokens. |
| **Document mapping** | Production Standards Draft must record design → production mapping in **Production Decisions** ([production-standards-governance-v1.md](production-standards-governance-v1.md) C-12). |
| **Interpretation direction** | Round **toward** scale — never invent intermediate values “for better look.” |
| **Project override** | Lead-approved project tokens supersede Factory defaults for that project only — cite version + decision ID in charter. |

---

## 2. Spacing scale policy

### 2.1 Gap scale (gap, grid-gap, column-gap, row-gap)

**Use only:**

`5px` · `10px` · `20px` · `30px` · `40px` · `50px` · `70px`

### 2.2 Margin / padding scale

**Use only:**

`5px` · `10px` · `15px` · `20px` · `25px` · `30px` · `40px` · `50px` · `70px` · `90px`

### 2.3 Percentage padding (large containers only)

For **large internal padding** where volume / air is intentional:

`5%` · `10%` · `15%` · `20%` · `30%`

| Allowed | Forbidden default |
|---------|-------------------|
| Large section shells, hero inner bands, volumetric content blocks | Percentage **grid splits** (see §7) |
| Conscious preservation of design proportion at multiple viewports | `%` padding on small UI controls |

### 2.4 Section spacing cross-ref

Inter-section rhythm tokens remain governed by [frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md). Project Production Standards **must map** section-gap values to named tokens; values must either fit §2.1–§2.2 or be **explicitly approved** in project SSOT with decision record.

---

## 3. Typography px policy

| Rule | Detail |
|------|--------|
| **Font sizes in CSS** | Always **`px`** for production UI type — no `rem`/`em` font-size on landing UI unless project SSOT documents a named exception. |
| **Line-height rule (mandatory default)** | **`line-height = font-size + 4px`** — see [typography-rhythm-governance.md](typography-rhythm-governance.md) §2.1. |
| **Implementation** | Prefer explicit px pairs: `font-size: 18px; line-height: 22px;` or `line-height: calc(<font-size> + 4px)` when font-size is a single token. |
| **Named exceptions** | Hero display, legal micro-copy, button single-line — **named in Production Standards** with scoped selector/breakpoint. |
| **Forbidden drift** | Arbitrary line-heights (`53px`, `57px`), random decimals (`1.08`, `1.13`), mixed px + unitless systems on one page. |

### 3.1 Pre-flight + QA elevation

The `font-size + 4px` rule existed as **preferred** in [typography-rhythm-governance.md](typography-rhythm-governance.md) but was not wired into shell-first / calibration REPORT lines — agents treated it as optional. **From v1 of this doc:**

- **Pre-flight (Shell / Global Styles):** type table in Production Standards must list line-heights; default rows must satisfy `+4px` or cite named exception.
- **Design Calibration:** spot-check every type row — [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) §5.1.
- **Foundation QA REPORT line:**

```text
TYPOGRAPHY PRECISION (line-height = font-size + 4px) — PASS | partial (list) | FAIL | N/A (project exceptions documented)
```

---

## 4. No word breaking policy

**Forbidden without separate operator approval + Exception Registry:**

| Property | Status |
|----------|--------|
| `letter-spacing` | **Forbidden** — **any value** (including `0`, `normal`, `initial`, `inherit`, `unset`) |
| `word-break` | **Forbidden** — **any value** (including `normal`, `break-word`, `break-all`) |
| `overflow-wrap` | **Forbidden** — **any value** (including `normal`, `break-word`, `anywhere`) |
| `hyphens` | **Forbidden** — **any value** (including `manual`, `auto`, `none`) |

**Detection rule:** **property presence in `src/scss/**` or compiled `dist/*.css` = FAIL.** Value does not matter. Grep each property name — required count = **0** unless registered exception.

**Authority:** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) §1.1 — layout + HTML typograph policy; **not** permission to emit these properties in CSS.

**Overflow resolution order:**

1. Container width / `min-width: 0` on flex children  
2. Font-size adjustment within approved type scale  
3. HTML line breaks / copy edit  
4. Layout pattern change ([frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md))  
5. Selective RU HTML typography (§5) — **not** word-breaking CSS  

---

## 5. Russian HTML typography policy

All **Russian** (and mixed RU) visible copy in frontend HTML must be typographed at **HTML level**:

| Apply to | Do not apply to |
|----------|-----------------|
| Body, headings, buttons, links, captions, cards, forms | `meta`, code, class names, `data-*`, URLs, `href` tel/mailto, JSON-LD, technical values |

**Goals:** non-breaking spaces after short prepositions; correct quotes and em dash; preposition ties; no `&nbsp;` chains between every heading word.

**Authority:** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) §2.

**REPORT line (unchanged):**

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

---

## 6. Layout pattern selection policy

Agents **must select** a documented layout pattern — **not** assemble grids by eye.

| Layer | Authority |
|-------|-----------|
| Container (section vs inner width) | [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) |
| Inner zones (hero, cards, trust, finance) | [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) |
| Pattern library requirement | [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md) |

### 6.1 No default percentage splits

**Forbidden as default:**

```scss
grid-template-columns: 65% 35%;
grid-template-columns: 60% 40%;
grid-template-columns: 1fr 42%;
```

**Use instead:**

```scss
grid-template-columns: minmax(0, 13fr) minmax(0, 7fr);
/* or other approved fr / minmax / repeat patterns */
```

Percentage splits require `/* WF-LAYOUT-EXCEPTION: reason — approver — date */` per WF-LAYOUT-007.

### 6.2 Bootstrap-like grid thinking

- One measurement system per page (container contract + spacing scale).  
- Prefer **ready patterns** (2-col, 3-col, hero split, sidebar) over one-off column math.  
- CSS Grid **or** Flex — pick the pattern family declared in Production Standards C-11.

---

## 7. No arbitrary values rule

| Category | Rule |
|----------|------|
| Spacing | §2 scales only — or project SSOT token |
| Type line-height | §3 — or named exception |
| Layout columns | §6 — fr/minmax/repeat — or WF-LAYOUT exception |
| Colors / radius | Project Production Standards — Factory does not invent hex or radius per block |
| Breakpoints | Project + [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) — no ad-hoc `981px` |

**Agent stop rule:** If a value is not on scale and not in approved Production Standards → **STOP** — map to nearest scale value or escalate HITL; do not ship arbitrary px.

---

## 8. Evidence chain

Precision compliance must be **provable** in REPORT — not chat claims.

| Stage | Evidence |
|-------|----------|
| **Production Standards Draft** | Type table with line-heights; spacing token table mapped to §2; layout zone table (C-11) |
| **Shell / Global Styles** | Demo page renders tokens; no forbidden CSS in global partials |
| **Design Calibration** | §5 checks + `TYPOGRAPHY PRECISION` line + **COMPILED CSS SPOT-CHECK** on `dist/*.css` |
| **Foundation QA** | `WF GRID DISCIPLINE`, `WF LAYOUT DISCIPLINE`, `RU TYPOGRAPHY`, `TYPOGRAPHY PRECISION`, `OPERATOR LAW COMPLIANCE`, `COMPILED CSS COMPLIANCE`, `INLINE STYLE COMPLIANCE`, `ROOT COMPLIANCE` lines |
| **Page production** | Block REPORT cites standards version; deviations = STRUCTURE CHANGE |

**Enforcement authority:** [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) — source-only SCSS review does **not** satisfy compiled-output gates.

---

## 9. Relationship to project SSOT

| Situation | Rule |
|-----------|------|
| New greenfield project | Factory precision defaults apply until Lead approves project-specific tokens |
| Approved project (e.g. FP-0002 v3) | Project SSOT **wins** for that project; Factory precision informs **future** projects and **gap analysis** |
| Conflict discovered at calibration | Fix code **or** amend standards via change control — never silent drift |

See **FP-0002 impact** in pack REPORT — conflicts listed; FP-0002 **not modified** by this pack.

---

## 10. Agent / operator behavior

| Situation | Response |
|-----------|----------|
| Raw design says 64px gap | Map to **70px** (or **50px** if context is tighter) — record in Production Decisions |
| Agent proposes `line-height: 1.22` | **Reject** — use px `font-size + 4px` or named exception |
| Hero split `70% / 30%` | **Reject** — use fr pair per WF-LAYOUT-002 |
| User requests Home without precision pre-flight | **STOP** — shell-first + calibration gates |
| RU text overflows | Layout fix first — see §4 |

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Frontend Precision Governance Pack: spacing scales, percentage padding, typography px + mandatory line-height pre-flight, no word-break, RU HTML typography, layout pattern selection, evidence chain. |
| 2026-06-13 | v1.1 — Authority chain aligned to [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — Project SSOT rank 1; this doc rank 3. |
| 2026-06-14 | v1.2 — Enforcement Pack v1: compiled CSS evidence chain; ROOT COMPLIANCE cross-ref. |
