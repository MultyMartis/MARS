# WF-FRONTEND-VISUAL-AUTHORITY-CONTRACT-v1

**Document type:** Visual authority chain — Phase F4  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Production mode:** `PIXEL_PERFECT`

---

## 1. Authority chain (FP-0002 v2)

For **visual structure, layout, spacing relationships, assets, and visible copy placement**, resolve conflicts in this order:

| Rank | Layer | Source | Scope |
|------|-------|--------|-------|
| **V1** | **FIG** | `INCOMING/01_DESIGN/Шпиговский.fig` | All page templates; components; text nodes; embedded rasters |
| **V2** | **PDF** | 24-file pack in `INCOMING/01_DESIGN/` | Cross-check; numeric sampling; coordinator reference |
| **V3** | **JPG** | `HOME-PAGE-FULL-MOCKUP.jpg` | **Home desktop visual control only** — not other templates |
| **V4** | **OPERATOR** | Human tie-breaker | Conflicts; IA gaps; approval locks |

**Engineering token SSOT (separate rank-1 lane):** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) governs **implemented px/hex/radius** after mapping — does **not** override FIG for **content** or **composition** without C-12 record.

**Factory hierarchy for production decisions:** [frontend-production-authority-order-v1.md](../projects/mars-website-factory/frontend-production-authority-order-v1.md) — Project Production Standards (rank 1) beats Operator Laws beats Factory governance.

---

## 2. Who wins when sources conflict

| Conflict type | Winner | Action |
|---------------|--------|--------|
| FIG frame text vs PDF text (same node scope) | **FIG (V1)** | Record in deviation register if PDF differs materially |
| FIG vs JPG — Home header phones/schedule | **OPERATOR (V4)** after FIG+JPG evidence | Legacy Header Text Lock pattern — **ADOPT** |
| PDF vs JPG — Home only | **FIG first**; JPG for scale/label verification | Operator if still ambiguous |
| XLSX IA vs visible header/menu labels | **FIG/JPG visible copy** over sheet labels | XLSX for URLs/slug only |
| FIG vs Production Standards v3 numeric token | **Production Standards** for **CSS output**; FIG for **audit evidence** | C-12 Production Decision if mapping changes SSOT |
| FIG layer index vs FIG `bounds.y` section order | **`bounds.y` primary**; layer index fallback | **HITL (V4)** when delta > threshold — FAIL-007 lesson |
| Missing mobile PDF for a template | **FIG mobile frame** if present | Else **SAFE UNKNOWN** — no invented mobile layout |
| Agent preference vs any rank V1–V4 | **Forbidden** | **STOP** |

---

## 3. How conflicts are recorded

Every unresolved or resolved conflict **must** appear in:

| Register | Minimum fields |
|----------|----------------|
| **Production Decisions (C-12)** | Source A vs B; winner; justification; approver |
| **Visual Deviation Register (L5)** | Section/block; expected vs built; evidence path; verdict |
| **Text lock delta log** | FIG node id; string hash; operator ack if override |
| **SAFE UNKNOWN register** | What is unknown; verify-by plan; blocker class |

**REPORT line (mandatory when conflict handled):**

```text
AUTHORITY CONFLICT — <id> — RESOLVED: <V1|V2|V3|V4> — RECORD: <C-12|L5|UNKNOWN>
```

**Forbidden:** Silent pick of convenience source; chat memory as authority.

---

## 4. SAFE UNKNOWN — visual authority

| Situation | Required response | Build permission |
|-----------|-------------------|------------------|
| Text node unreadable in FIG/PDF | **SAFE UNKNOWN** — do not guess | **STOP** for that text slot |
| Asset node ambiguous (multi-brand) | **SAFE UNKNOWN** — run Brand Asset Gate | **STOP** until operator selects hash |
| Mobile layout absent for scoped block | **SAFE UNKNOWN** | **STOP** mobile implementation |
| Section order ambiguous (y vs layer) | **SAFE UNKNOWN** until operator decision | **STOP** assembly |
| Pixel spacing not measurable | **SAFE UNKNOWN** in PF-* | May proceed only with SSOT mapped value + C-12 |

**SAFE UNKNOWN is not a waiver.** It blocks **VERIFIED** status until resolved or operator **WAIVE** with dated scope.

---

## 5. Source roles — explicit non-authority

| Source | Role | Not authority for |
|--------|------|-------------------|
| XLSX content pack | IA, SEO, URLs | Visible marketing copy when FIG/PDF conflict |
| Legacy `_fig_full_build_extract.json` | Forensic reference | Current build without regeneration |
| Legacy workspace HTML | Failure evidence | Any v2 markup |
| Reference slices / Triumph demo | Pattern survival | Project visual truth |
| Agent audit PASS | Technical check | Operator visual acceptance |

---

## 6. Operator approval lock

Authority chain **V1→V4** is **draft** until operator records:

```text
FP-0002 v2 VISUAL AUTHORITY — APPROVED — <date>
```

Until then: Discovery and inventory may proceed; **implementation HTML/SCSS remains blocked** except as authorized by separate foundation-start task.

---

## 8. FP-0002 V6 sole-authority laws (2026-06-23 append)

When a project declares **one** visual source as canonical (e.g. `HOME-PAGE-FULL-MOCKUP.jpg` for FP-0002 V6 Home):

| Law | Rule |
|-----|------|
| **SOLE VISUAL AUTHORITY** | Archived layouts, `GROUP-*` exports, PDFs, old workspaces, and previous generated implementations **must not** participate in structural reconstruction. |
| **NO PLACEHOLDER DUPLICATION** | Unreadable or missing content **stops** implementation. Agents **must not** duplicate neighboring cards, text, or assets to fill an incomplete section. |
| **ANALYSIS-BEFORE-IMPLEMENTATION** | After operator visual rejection, the next task is **audit-only**. No HTML/SCSS until operator approves crop, boundaries, structure, and content map. |
| **OPERATOR REJECTION OVERRIDE** | A technically successful build/report does **not** make a visually incorrect section acceptable. Operator rejection sets status to **REJECTED**. |
| **CROP COMPLETENESS GATE** | A section crop is invalid if any repeated item, card row, decorative object, section ending, or next-section marker is cut off. |
| **BOUNDARY LINE RULE** | A section boundary line must never pass through content belonging to that section. |
| **MAP ACCURACY RULE** | Content and geometry frames must enclose the actual visual element. They must not overlap unrelated heading, paragraph, list or card zones. |

**Evidence:** [FP-0002-V6-HOME-SECTION-01-REJECTION.md](../workspaces/fp-0002-shpigovsky-v6/reviews/main-content/FP-0002-V6-HOME-SECTION-01-REJECTION.md) · [FP-0002-V6-HOME-SECTION-01-CORRECTED-AUDIT-V2.md](../workspaces/fp-0002-shpigovsky-v6/reviews/main-content/FP-0002-V6-HOME-SECTION-01-CORRECTED-AUDIT-V2.md)

---

## 7. Contract status

**VISUAL AUTHORITY LOCKED — YES** (pending operator sign-off on §6)

---

*End of contract — v1.*
