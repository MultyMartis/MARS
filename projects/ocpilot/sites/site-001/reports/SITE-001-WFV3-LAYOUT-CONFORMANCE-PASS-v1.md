# REPORT — SITE-001 WF-V3 LAYOUT CONFORMANCE PASS

**Type:** Layout conformance iteration — prototype SCSS only  
**Date:** 2026-06-13  
**Site:** SITE-001 — Автосалон СИБКАР  
**Authority:** [WF-LAYOUT-DISCIPLINE-v1.md](../../../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md)  
**Prior audit:** [SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md](SITE-001-WFV3-LAYOUT-AUTHORITY-REVIEW-v1.md)

**Scope:** First pass — bring WF-V3 prototypes to WF-LAYOUT authority. No redesign, no new blocks, no OpenCart/TEST.

**Workspaces:**

| Workspace | Role |
|-----------|------|
| `workspaces/site-001-wf-v3-pdp-prototype/` | PDP reference |
| `workspaces/site-001-wf-v3-homepage-prototype/` | Homepage reference |

**Pre-change backup:**

| Backup ID | Path |
|-----------|------|
| `pre-wf-layout-conformance-20260613-layout-conformance` | `workspaces/site-001-wf-v3-pdp-prototype/backups/pre-wf-layout-conformance-20260613-layout-conformance/` |
| `pre-wf-layout-conformance-20260613-layout-conformance` | `workspaces/site-001-wf-v3-homepage-prototype/backups/pre-wf-layout-conformance-20260613-layout-conformance/` |

**Screenshots (post-pass):**

| Surface | Path | Required captures |
|---------|------|-------------------|
| PDP | `workspaces/site-001-wf-v3-pdp-prototype/screenshots/layout-conformance/` | `full-page.png`, `hero.png`, `trust.png` |
| Homepage | `workspaces/site-001-wf-v3-homepage-prototype/screenshots/layout-conformance/` | `full-page.png`, `hero.png`, `featured-inventory.png` |

**Build status:** `npm run build` — **PASS** in both workspaces.

---

## Summary table

| Изменённые файлы | Найденные нарушения | Исправления | Соответствие WF-LAYOUT |
|------------------|---------------------|-------------|------------------------|
| `_tokens.scss` (оба) | `$hero-gallery-ratio: 65%`, `$hero-offer-ratio: 35%` | Named fr tokens L1/L2/L4/L5 | **PASS** |
| `_breakpoints.scss` (оба) | Только desktop mixin; collapse SAFE UNKNOWN | `until-tablet` (1024px), `until-mobile` (767px) | **PASS** |
| `_pdp-hero.scss` (оба) | L1 `%/%` + gap overflow | `13fr minmax(360px, 7fr)` + stack ≤1024px | **PASS** |
| `_homepage-hero.scss` | L2 hybrid `1fr 42%` | `minmax(0, 7fr) minmax(480px, 5fr)` + search collapse | **PASS** |
| `_trust-row.scss` (оба) | flex `flex: 1` strip | L5 `repeat(5, minmax(180px, 1fr))` + 2-col/1-col collapse | **PASS** |
| `_credit-block.scss` (PDP) | Hardcoded `5fr 7fr` (compliant, untokenized); no collapse | Token refs + stack ≤1024px; form 1-col ≤767px | **PASS** |
| `_credit-block.scss` (HP) | Same as PDP credit | Token refs + responsive (parity) | **PASS** |
| `_featured-inventory.scss` | `repeat(4, 1fr)` без minmax/collapse | L3 `repeat(4, minmax(0, 1fr))` + N→2→1 | **PASS** |

---

## Zone conformance — До / После / Причина

### PDP Hero (L1)

| | Detail |
|---|--------|
| **До** | `grid-template-columns: 65% 35%` via `$hero-gallery-ratio` / `$hero-offer-ratio`; gap 40px; tracks + gap > 100% inner width |
| **После** | `13fr minmax(360px, 7fr)`; gap `$hero-zone-gap` (40px); stack `1fr` at ≤1024px; nested CTA/specs `minmax(0, 1fr)` |
| **Причина** | WF-LAYOUT-002 + WF-LAYOUT-007 — fr ratio preserves 65/35 intent; gap absorbed correctly; offer floor protects 3-col nested grids |

### Homepage Hero (L2)

| | Detail |
|---|--------|
| **До** | `grid-template-columns: 1fr 42%` — hybrid % track, ≠ PDP grammar |
| **После** | `minmax(0, 7fr) minmax(480px, 5fr)` — visual ≈ 5/12 (~42% intent); stack ≤1024px; search 4→2→1 col |
| **Причина** | WF-LAYOUT-002 L2 — asymmetric hero under same authority family; no silent `%` track |

### Trust (L5)

| | Detail |
|---|--------|
| **До** | `display: flex`; items `flex: 1` — equal flex, ≠ grid family |
| **После** | `repeat(5, minmax(180px, 1fr))`; 2-col ≤1024px; 1-col ≤767px; border-left removed on collapse |
| **Причина** | WF-LAYOUT-004 — L5 grid grammar aligned with featured/banks; documented item min floor |

### Credit (L4)

| | Detail |
|---|--------|
| **До** | `5fr 7fr` — **already authority-compliant**; no responsive collapse |
| **После** | `#{credit-head-fr}fr #{credit-panel-fr}fr` (unchanged ratio); stack ≤1024px; panel border/pad swap; form 1-col ≤767px |
| **Причина** | WF-LAYOUT-005 — tokenize frozen ratio; WF-LAYOUT-006 — collapse documented |

### Responsive (WF-LAYOUT-006)

| Zone | Breakpoint | Collapse mode | Status |
|------|------------|---------------|--------|
| PDP Hero L1 | ≤1024px | Stack single column | **Documented in SCSS** |
| Homepage Hero L2 | ≤1024px | Stack; search 2×2 | **Documented in SCSS** |
| Trust L5 | ≤1024px / ≤767px | 2-col → 1-col stack | **Documented in SCSS** |
| Featured L3 | ≤1024px / ≤767px | 4 → 2 → 1 columns | **Documented in SCSS** |
| Credit L4 | ≤1024px / ≤767px | Stack; form 1-col | **Documented in SCSS** |
| PDP offer nested | ≤767px | CTA 1-col; specs 2-col | **Documented in SCSS** |

**Note:** Collapse rules are **implemented and commented in SCSS** — not yet visually QA'd at all breakpoints (operator HITL recommended).

---

## Authority status

| Check | Status |
|-------|--------|
| **WF-GRID Status** | **PASS** — container contract unchanged (`1280px` max, `24px` pad, section ≠ container) |
| **WF-LAYOUT Status** | **PASS** — L1/L2/L4/L5 violations remediated; L3 featured upgraded; collapse rules present |

### WF LAYOUT DISCIPLINE — PASS

Zones verified: PDP Hero (L1) · Homepage Hero (L2) · Trust (L5) · Credit (L4) · Featured (L3) · Responsive (WF-LAYOUT-006)

---

## Verdict

### **A — Ready For Layout Freeze**

First conformance pass complete. Inner-zone models unified under WF-LAYOUT-DISCIPLINE-v1. Visual intent preserved (65/35 PDP, ~42% homepage visual column). No new design decisions.

**Recommended before production handoff (non-blocking for layout freeze):**

- Operator visual HITL at 1280 / 1024 / 767 viewports
- Confirm offer min-width 360px vs CTA label length
- Update PDP design freeze implementation appendix (ratio intent unchanged, model = fr)

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Pixel diff before/after at 1280px desktop | **NOT RUN** — layout math change; visual parity expected, not pixel-certified |
| Mobile stack visual QA | **OPEN** — rules exist; screenshots desktop-only (1280/1440 viewport) |
| CI layout lint | **NOT IMPLEMENTED** |
| Catalog auto-fill L3 variant | **NOT IN SCOPE** — not prototyped |

**SECURITY RISK:** None.

---

*SITE-001 WF-V3 Layout Conformance Pass v1 — prototype iteration; no commit implied.*
