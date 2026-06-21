# FP-0002 — Exception Registry v1

**Document type:** Project Exception Registry — rank-1 overrides of Operator Law  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-14  
**Status:** **ACTIVE** — closes authority conflict gate before new M2 pass  

**Scope:** FP-0002 project artefact only. **Not** Factory governance, **not** a new enforcement layer, **not** runtime code.

**Purpose:** Explicitly register every **approved** deviation of **FP-0002 Production Standards v3 (rank 1)** from **Approved Operator Laws (rank 2)** so M2 agents can resolve EG-01 / EG-02 / EG-04 without interpretation.

**Authority chain:**

| Layer | Document |
|-------|----------|
| Rank 1 SSOT | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) — **APPROVED WITH ANDREY CORRECTIONS** (2026-06-13) |
| Rank 2 laws | [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) §3 OL-01–OL-07 |
| Enforcement | [website-factory-enforcement-pack-v1.md](../../../projects/mars-website-factory/website-factory-enforcement-pack-v1.md) §4–§5 |
| Decision route | [frontend-compliance-decision-model-v1.md](../../../projects/mars-website-factory/frontend-compliance-decision-model-v1.md) CASE B → C |
| Execution context | [FP-0002-EXECUTION-BRAIN-v1.md](FP-0002-EXECUTION-BRAIN-v1.md) §7–§9 |

**Mandatory fields (Factory §4):** decision id · owner · justification · authority citation — present in every registered exception below.

**Compliance rule:** Rank-1 permit **≠** auto-WAIVED OL. With **complete** registry entry → **CASE C → WAIVED** on EG-01 / EG-02 / EG-04 for the scoped property. Without registry → **CASE B → FAIL**.

---

## 1. How to use (M2 agent)

```text
Compiled CSS value detected
        ↓
Is property in OL-01 scope (gap / margin / padding)?
        ↓ No → not OL-01 (dimensions, radius, font-size, line-height tiers — see §3)
        ↓ Yes
Value on OL-01 scale?
        ↓ Yes → PASS (no exception lookup)
        ↓ No
Value explicitly permitted by v3 SSOT token or §6.2 / §8 applied table?
        ↓ No → CASE D → FAIL (map to OL nearest or STOP HITL)
        ↓ Yes
Matching EX-* row in §2 with all mandatory fields?
        ↓ Yes → CASE C → WAIVED (cite decision id in REPORT)
        ↓ No → CASE B → FAIL
```

**Line-height:** v3 §4.1 named tiers → **NO EXCEPTION REQUIRED** (OL-05 built-in rank-1 win — see §3.5).

**Storage:** This file is the canonical registry. QA REPORT may duplicate rows in an **Exception Registry** subsection; this file remains SSOT for FP-0002.

---

## 2. Registered exceptions

### EX-001 — Project 4px-base spacing scale (master)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-001** (`PD-05-EX-001`) |
| **Conflict** | FP-0002 **4px-base production spacing scale** (`space-0`…`space-16`) vs **OL-01** discrete scales (gap: 5·10·20·30·40·50·70; margin/padding: 5·10·15·20·25·30·40·50·70·90) |
| **Rank-1 Authority** | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §6.1 · **PD-05** (Production Decisions §12) |
| **Conflicting Authority** | **OL-01** — [frontend-production-authority-order-v1.md](../../../projects/mars-website-factory/frontend-production-authority-order-v1.md) §3 |
| **Decision** | **PERMIT** — implement v3 spacing tokens; OL-01 waived for listed tokens when this registry is cited (CASE C) |
| **Justification** | Lead-approved production SSOT replaces Normalization draft mapping to OL nearest-neighbour. Raw PDF clusters (72/56/24/16/32 px) normalized to 4px-base grid (`space-12`=80, `space-16`=240, etc.) per Normalization §4 + Lead v3 freeze. OL-01 nearest mapping would distort card gutter (24→20/30), form rhythm (16→15/20), and section boundaries documented in PD-16 + Factory section-spacing rule. |
| **Owner** | **Андрей** — Frontend Lead / Project Lead |
| **Status** | **ACTIVE** — approved with v3 (2026-06-13); registry formalized 2026-06-14 |

**Permitted off-OL-01 scale tokens (rank-1 only — do not invent unlisted px):**

| Token | px | OL-01 nearest | v3 authority |
|-------|-----|---------------|--------------|
| `space-1` | 4 | 5 (gap) / 5 (pad) | §6.1 scale |
| `space-2` | 8 | 10 / 10 | §6.1 · §8.2 label gap · §8.6 pagination gap |
| `space-3` | 12 | 10 / 15 | §6.1 · §8.2 input padding-y |
| `space-4` | 16 | 20 / 15–20 | §6.1 · §6.2 inline stacks · §8 FAQ/form |
| `space-5` | 20 | 20 / 20 | §6.1 · §3.1 mobile padding-x (**on OL when used as padding**) |
| `space-6` | 24 | 20–30 / 25 | §6.1 · §6.2 card gap/padding · §8 cards |
| `space-7` | 32 | 30 / 30 | §6.1 · §6.2 breadcrumb · §3.6 article gap · §8.1 button padding-x |
| `space-8` | 40 | 40 / 40 | §6.1 · §3.1 desktop padding-x (**on OL — no waiver needed for 40px alone**) |
| `space-9` | 48 | 50 / 50 | §6.1 scale · §8.2 input height context |
| `space-10` | 56 | 50 / 50 | §6.1 · §6.2 diff-bg mid transition |
| `space-11` | 64 | 70 / 70 | §6.1 · §6.2 mobile inter-section |
| `space-12` | 80 | 70 / 70 | §6.2 same-bg gap · section padding-y · §8.8 footer |
| `space-13` | 96 | 70 / 90 | §6.1 scale (reserved) |
| `space-14` | 120 | 70 / 90 | §6.1 scale (reserved) |
| `space-15` | 160 | 70 / 90 | §6.1 scale (reserved) |
| `space-16` | 240 | 70 / 90 | §6.2 band transition |

**Note:** `space-8` (40px) and `space-5` (20px) **match OL-01** for their primary uses (page padding). They remain in EX-001 because the **scale system** as a whole deviates from OL-01; individual on-scale values do not require separate waiver when used as documented.

---

### EX-002 — Gap 8px (`space-2`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-002** (`PD-05-EX-002`) |
| **Conflict** | **`gap: 8px`** (pagination, form label offset) vs OL-01 gap scale (nearest **10px**) |
| **Rank-1 Authority** | v3 §8.2 (8px below label) · §8.6 (pagination gap 8px) · token `space-2` §6.1 |
| **Conflicting Authority** | **OL-01** gap scale |
| **Decision** | **PERMIT** — use `space-2` / 8px in cited contexts only |
| **Justification** | Component metrics from Normalization §8; pagination and label-to-field rhythm preserved from PDF sampling. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-003 — Padding / gap 12px (`space-3`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-003** (`PD-05-EX-003`) |
| **Conflict** | **`padding: 12px`** (input padding-y) vs OL-01 margin/padding scale (nearest **10px** or **15px**) |
| **Rank-1 Authority** | v3 §8.2 Inputs — «16px x / **12px y**» · token `space-3` §6.1 |
| **Conflicting Authority** | **OL-01** margin/padding scale |
| **Decision** | **PERMIT** — input/textarea vertical padding only |
| **Justification** | 48px field height + 16px horizontal padding + 12px vertical padding = production form family SSOT; not arbitrary agent rounding. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-004 — Gap / padding 16px (`space-4`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-004** (`PD-05-EX-004`) |
| **Conflict** | **`gap: 16px`**, **`padding: 16px`** vs OL-01 (gap nearest **20px**; padding nearest **15px** or **20px**) |
| **Rank-1 Authority** | v3 §6.2 (`space-4` inline stacks, form field gap) · §8.2 inputs/textarea · §8.4 FAQ item gap · §3.6 form grid gap |
| **Conflicting Authority** | **OL-01** |
| **Decision** | **PERMIT** — cited contexts only |
| **Justification** | Dominant PDF inline rhythm (Numeric v2); form BLK-035 two-column gap; FAQ accordion item separation. Historical M2 false PASS root cause: **16px gap in compiled CSS** — this registry converts CASE B → CASE C when v3-cited. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-005 — Gap / padding 24px (`space-6`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-005** (`PD-05-EX-005`) |
| **Conflict** | **`gap: 24px`**, **`padding: 24px`**, **`margin` using 24px** vs OL-01 (nearest gap **20/30**; padding **25**) |
| **Rank-1 Authority** | v3 §3.3–§3.6 card grids · §6.2 card gap/padding · §8.1 header callback padding-x · §8.3 cards |
| **Conflicting Authority** | **OL-01** |
| **Decision** | **PERMIT** — card family and grid gutter only |
| **Justification** | CONFIRMED derived 3-col pitch from service hub PDF (`Numeric v2`); changing to OL-20/25/30 breaks grid math at 1170px container. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-006 — Gap / padding 32px (`space-7`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-006** (`PD-05-EX-006`) |
| **Conflict** | **`gap: 32px`**, **`padding-x: 32px`** vs OL-01 (nearest **30px**) |
| **Rank-1 Authority** | v3 §6.2 breadcrumb-to-hero · §3.6 article TOC stack · §8.1 primary CTA padding-x 32px |
| **Conflicting Authority** | **OL-01** |
| **Decision** | **PERMIT** — breadcrumb band, article gap, primary button horizontal padding |
| **Justification** | Breadcrumb cluster confirmed in Numeric v2; primary button min-width family uses 32px horizontal inset per Normalization §8. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-007 — Gap 56px (`space-10`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-007** (`PD-05-EX-007`) |
| **Conflict** | **Section gap 56px** (different-background mid transition) vs OL-01 gap scale (nearest **50px**) |
| **Rank-1 Authority** | v3 §6.2 — «may use **56px** (`space-10`) mid transitions» |
| **Conflicting Authority** | **OL-01** gap scale |
| **Decision** | **PERMIT** — diff-bg section transitions only |
| **Justification** | Preserves Numeric v2 medium cluster (56px) on 4px-base grid; Factory section-spacing rule allows tokenized exceptions. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-008 — Gap 64px mobile inter-section (`space-11`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-008** (`PD-05-EX-008`) |
| **Conflict** | **`section-gap-mobile: 64px`** vs OL-01 gap scale (nearest **70px**) |
| **Rank-1 Authority** | v3 §6.2 · Start Sequence Step 6 · Charter §9 |
| **Conflicting Authority** | **OL-01** gap scale |
| **Decision** | **PERMIT** — mobile inter-section default |
| **Justification** | Mobile reduction from 80px same-bg token; 64px on 4px-base (`space-11`); Enforcement Pack provenance example (`64px` vs OL) resolved by this row. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-009 — Gap / padding 80px section rhythm (`space-12`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-009** (`PD-05-EX-009`) |
| **Conflict** | **Section gap / padding 80px** vs OL-01 (nearest **70px**) |
| **Rank-1 Authority** | v3 §6.2 same-bg gap · section-padding-y · §8.8 footer vertical padding · Start Sequence spacing demo labels |
| **Conflicting Authority** | **OL-01** |
| **Decision** | **PERMIT** — section vertical rhythm (single-boundary rule per Factory section-spacing) |
| **Justification** | Raw PDF 72px → normalized 80px (`space-12`) on 4px grid (Normalization §4.2); Lead approved in PD-16 + §6.2. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

### EX-010 — Gap 240px band transition (`space-16`)

| Field | Value |
|-------|-------|
| **Exception ID** | **EX-010** (`PD-05-EX-010`) |
| **Conflict** | **Band transition 240px** vs OL-01 (nearest **70px** gap / **90px** padding) |
| **Rank-1 Authority** | v3 §6.2 `section-gap-band` · Start Sequence Step 2 spacing demo (band **240px**) |
| **Conflicting Authority** | **OL-01** |
| **Decision** | **PERMIT** — full-bleed / major band transitions only |
| **Justification** | Raw PDF ~250px band → `space-16`=240px on 4px-base; hero exit / CTA band semantics. |
| **Owner** | **Андрей** |
| **Status** | **ACTIVE** |

---

## 3. NO EXCEPTION REQUIRED (audited — not rank-1 ↔ rank-2 conflicts)

| ID | Surfaced issue | Audit result | Agent action |
|----|----------------|--------------|--------------|
| **NEX-01** | **C-02 — Layout Pattern naming gap** (formal LP-* IDs absent in v3) | **Documentation debt only** — Mapping QA §4, §11.1 **PASS WITH NOTES**; layout chain functionally reconstructible from Normalization §6 + v3 §3. **Not** a numeric OL conflict. | M-MUST-16: infer LP-* from Normalization §6 at implement time; cite WF-GRID → WF-LAYOUT → inferred LP in REPORT. **Do not** treat as Exception Registry row. |
| **NEX-02** | **C-03 — PROJECT-STATUS drift** | `PROJECT-STATUS.md` (2026-06-11) stale vs PRE-M2 restore. **Not** an authority conflict on production values. | Use [REPORTS/FP-0002-RESET-COMPLETE.md](REPORTS/FP-0002-RESET-COMPLETE.md) + Charter + v3 — **not** PROJECT-STATUS for execution truth. |
| **NEX-03** | **C-04 — Token / workspace path drift** | Snapshot restore moved ops → `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`; frontend → `workspaces/fp-0002-shpigovsky-frontend/` ([RESET-COMPLETE](REPORTS/FP-0002-RESET-COMPLETE.md)). **Not** rank-1 vs OL conflict. | Use canonical paths from Execution Brain §3 / R-11. **Do not** register as OL exception. |
| **NEX-04** | **C-05 — OL-05 vs explicit v3 line-heights** | **OL-05 explicitly defers to rank-1 named tiers:** «Project Production Standards win over this default when both define the same token» (authority-order §3 OL-05). v3 §4.1 defines every tier (H1 84/50, H2 44/28, body 28/24, etc.). | Implement v3 §4.1 line-heights **as SSOT** — **PASS** on OL-05 without registry. **Do not** emit WAIVED for typography tiers when v3 table cites the tier. |
| **NEX-05** | Page padding **40px / 20px** | Values **on OL-01** scale (`space-8`, `space-5`). | **PASS** — no exception. |
| **NEX-06** | Border radius **30 / 10 / 999px** | **No OL** governs radius. Rank-1 vs deprecated v2 scale only (CF-02 — resolved by v3). | Implement v3 §7 — no OL exception. |
| **NEX-07** | Desktop-first @ **1024px** | Rank-1 (PD-07) vs Industry Best Practice (rank 5) — **not** OL conflict. | Desktop-first per v3 §9 — no exception. |
| **NEX-08** | Typography law (`letter-spacing`, `word-break`, `overflow-wrap`) | v3 §4.3 PD-14/15 **aligns with OL-06** — stricter project SSOT, not deviation. | **PASS** — forbidden properties stay forbidden. |
| **NEX-09** | Section spacing Factory rule | v3 **adopts** [frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) via PD-16 — rank-1 + rank-3 **aligned**, not conflicting. | Apply Factory rule + v3 token map §6.2. |
| **NEX-10** | Container **1170px**, colors, Inter, weights | Dimensions / color / font — **outside OL-01** scope. | SSOT §2–§5 — no OL exception. |
| **NEX-11** | Article TOC **280px** + `1fr` | Uses **`fr` grid** — OL-04 compliant; not OL-01. | PD-12 placeholder — no spacing exception. |

---

## 4. Confirmed no-conflict domains (charter cross-check)

Aligned between v3, Charter v1, Start Sequence v1 — **no rank-1 ↔ rank-2 exception needed:**

| Domain | Value | Sources |
|--------|-------|---------|
| Font | Inter | v3 · Charter · Start Sequence |
| Desktop / mobile padding | 40px / 20px | v3 PD-13 · Charter CF resolved |
| Breakpoint | 1024px desktop-first | v3 PD-07 |
| Min viewport | 320px | v3 §9.3 |
| Shell-first before Home | Mandatory Phase 0–7 | v3 §16 · Start Sequence Step 8 gate |
| Foundation entry | `ui-demo.html` | Start Sequence Step 1 |
| RU typography law | Forbidden break properties | v3 §4.3 · OL-06 aligned |

---

## 5. M2 compiled-CSS lookup (quick reference)

| Observed in `dist/*.css` | v3 cite | Exception ID | Verdict when registry cited |
|--------------------------|---------|--------------|----------------------------|
| `gap: 8px` | §8.2 · §8.6 | EX-002 | WAIVED |
| `padding: 12px` (input y) | §8.2 | EX-003 | WAIVED |
| `gap: 16px` | §6.2 · §8 | EX-004 | WAIVED |
| `padding: 16px` | §8.2 | EX-004 | WAIVED |
| `gap: 24px` | §3.6 · §6.2 · §8.3 | EX-005 | WAIVED |
| `padding: 24px` | §8.1 · §8.3 | EX-005 | WAIVED |
| `gap: 32px` | §6.2 · §3.6 | EX-006 | WAIVED |
| `padding: 32px` (CTA x) | §8.1 | EX-006 | WAIVED |
| `gap: 56px` | §6.2 diff-bg | EX-007 | WAIVED |
| `gap: 64px` (mobile section) | §6.2 | EX-008 | WAIVED |
| `gap` / `padding: 80px` | §6.2 · §8.8 | EX-009 | WAIVED |
| `gap: 240px` | §6.2 band | EX-010 | WAIVED |
| `padding: 40px` / `20px` page-x | §3.1 | — | **PASS** (on OL-01) |
| `line-height: 44px` (H2 desktop) | §4.1 tier table | — | **PASS** (OL-05 rank-1 tier) |
| `gap: 17px` / any unlisted px | — | — | **FAIL** (CASE D) |

---

## 6. Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Created | 2026-06-14 |
| Parent SSOT | FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3 |
| Closes | Execution Brain §3.3 «Exception Registry not created» · EG-04 blocker |
| Modifies Factory governance | **No** |
| Modifies frontend workspace | **No** |
| Commit / push | Not performed |

---

*Project Exception Registry only. Human-operated compliance aid — not automated enforcement.*
