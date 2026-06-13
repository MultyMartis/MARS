# MARS Website Factory — Frontend Layout Pattern Library Requirement v1

**Status:** **documented** — mandatory **requirement** for Website Factory production readiness.  
**Not:** the pattern library itself, runtime layout engine, or SCSS implementation.

**Purpose:** Before full production layout work, Website Factory must **have or explicitly choose** documented layout patterns — so agents pick **named patterns** instead of improvising column math.

**Related:**

| Document | Role |
|----------|------|
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Spacing + no-%-split policy |
| [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) | Container layer |
| [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) | Zone types L1–L5 |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | C-11 Grid / layout discipline in Production Standards |

---

## 1. Requirement statement

**Before** multi-section Home / catalog / PDP production freeze, the project **must** satisfy **one** of:

| Option | Condition |
|--------|-----------|
| **A — Factory reference library** | Adopt patterns from `workspaces/website-factory-reference-v1/` (or successor) with documented mapping in Production Standards C-11 |
| **B — Project charter patterns** | Project Production Standards lists **named pattern IDs** + SCSS/token bindings for each required zone |
| **C — Explicit SAFE UNKNOWN + freeze block** | No production freeze until patterns are chosen — WF-LAYOUT-006 / WF-LAYOUT-008 |

**This v1 doc does not create the library.** It only **requires** that one exists or is selected.

---

## 2. Mandatory pattern categories

Production Standards C-11 (or linked layout charter) **must account for** each category below — by reference ID, WF zone type, or explicit waiver:

| # | Category | Typical WF zone | Notes |
|---|----------|-----------------|-------|
| **LP-01** | **2-column grid patterns** | L1 hero split, L4 head/panel | fr ratio pairs — no default `%` |
| **LP-02** | **3-column grid patterns** | L3 `repeat(3, …)` | Documented `N=3` at desktop |
| **LP-03** | **4-column grid patterns** | L3 `repeat(4, …)` | Featured rows, icon grids |
| **LP-04** | **Hero split patterns** | L1, L2 | PDP proportional vs homepage asymmetric |
| **LP-05** | **Card grid patterns** | L3 | Curated vs catalog auto-fill — separate charters |
| **LP-06** | **Content / sidebar patterns** | L2 variant, article TOC | e.g. `280px + 1fr` — minmax not `%` |
| **LP-07** | **Flex row patterns** | Toolbars, inline CTAs | When flex is chosen over grid — document why |
| **LP-08** | **Responsive collapse patterns** | WF-LAYOUT-006 | Per-zone breakpoint + stack/reduce-N behavior |

---

## 3. Selection rules (agents)

| Rule | Detail |
|------|--------|
| **Pick, don't invent** | Implementation must cite pattern ID or WF zone type in SCSS comment or Production Standards table |
| **One grammar per zone family** | Hero L1 on PDP and sibling pages share pattern **family** |
| **Gap from scale** | [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §2 — no ad-hoc gap breaking ratio math |
| **Collapse documented** | LP-08 required before freeze — **SAFE UNKNOWN** blocks freeze per WF-LAYOUT-006 |

Example SCSS annotation:

```scss
/* LP-01 / WF-LAYOUT L1 — hero 13fr 7fr — FP-0002 charter §6.6 */
```

---

## 4. Production gate

| Gate | Condition |
|------|-----------|
| **READY for page production (multi-section)** | LP-01–LP-08 addressed in C-11 or layout charter; WF-GRID PASS; WF-LAYOUT PASS or documented partial with Lead ack |
| **NOT READY** | Agent-built `%` splits; undocumented column counts; missing collapse table |

**Shell / Visual Foundation** may proceed with **placeholder** pattern rows marked TBD — but **Home Production** with multi-column blocks requires LP categories closed or waived with HITL.

---

## 5. Future library (out of scope for v1)

When the Factory pattern library is authored, expected location:

```text
workspaces/website-factory-reference-v1/frontend-rules/layout-patterns/
  OR
projects/mars-website-factory/layout-patterns/
```

Minimum deliverables (future task):

- SCSS/CSS snippet per LP category  
- Responsive collapse table per pattern  
- Promotion report (same model as WF-GRID / WF-LAYOUT promotion)

**Do not** block current FP-0002 charter on library existence — FP-0002 C-11 + WF-LAYOUT zone types satisfy option **B** when populated.

---

## 6. REPORT line

```text
LAYOUT PATTERN LIBRARY — PASS | partial (list LP-*) | NOT READY | N/A (foundation only)
```

---

## 7. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — requirement only; no pattern library implementation. |
