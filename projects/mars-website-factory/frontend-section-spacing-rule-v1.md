# MARS Website Factory — Frontend Section Spacing Rule v1

**Status:** **documented** — operational rule for **inter-section** and **intra-section** vertical spacing in Gulp static frontends.  
**Not:** runtime spacing engine, automatic margin calculator, or universal px truth for all projects.

**Authority chain (methodology):**

| Layer | Document | Role |
|-------|----------|------|
| Canon | [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md) | Narrative pacing vocabulary |
| Methodology | [vertical-rhythm-governance.md](vertical-rhythm-governance.md) | Same-bg / different-bg transition rules |
| Tiers | [cadence-tier-model.md](cadence-tier-model.md) | XS–XL intent bands → project tokens |

**Consolidated in:** [frontend-production-rules-v0.md](frontend-production-rules-v0.md) §14 (pointer only).

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

---

## 1. Purpose

Provide a **deterministic, project-mappable** rule for section spacing so operators do not infer gaps from a single PDF block or neighbor DOM.

Every Factory project with a **Project Production Standards** document must map this rule to named tokens before page production begins.

---

## 2. Core rule (Factory default)

### 2.1 Same-background sections

When two adjacent sections share the **same surface role** (same `background-color` / wash / band):

| Rule | Detail |
|------|--------|
| **Single boundary** | Apply **one** spacing rhythm at the boundary — typically the **previous section’s bottom padding** **or** the **next section’s top padding**, **not both** at full value. |
| **Forbidden** | Double-gap duplication (`padding-bottom: 80px` + `padding-top: 80px` → 160px accidental desert). |
| **Default tier** | Map to project **M** (standard) inter-section token unless block evidence requires **S** (continuation) or **L** (reset). |

### 2.2 Different-background sections

When adjacent sections change **surface role** (page wash → elevated card band, light → footer band, full-bleed media, contrast reset):

| Rule | Detail |
|------|--------|
| **Reset allowed** | Both **top** and **bottom** inner padding may apply when contrast, density, or atmosphere requires a cadence reset. |
| **Band transitions** | Full-bleed or wide bands may use a **band-gap** token (project **XL** tier) separate from standard section gap. |
| **Dark/light** | Prefer **L** or **XL** tier at the boundary — see [vertical-rhythm-governance.md](vertical-rhythm-governance.md) §6. |

### 2.3 Inner section padding (inside `main`)

| Region | Rule |
|--------|------|
| **Content sections** | Vertical padding **top + bottom** per section type; values from project spacing scale — **not** copied from one hero block in PDF. |
| **Wide / full-bleed sections** | Background may be `100vw`; **inner** content aligns to `container-max`; padding applies to inner shell, not bleed media edges. |
| **First section after header** | Use project **breadcrumb-to-content** or **header-to-main** token — measure from shell, not hero guesswork. |
| **Last section before footer** | Terminal rhythm token — avoid footer suffocation or dead whitespace. |

### 2.4 Mobile reduction

| Rule | Detail |
|------|--------|
| **Default** | Inter-section and inner padding **may reduce** one step on mobile (e.g. 80px → 64px) when vertical scroll pressure is high. |
| **Forbidden** | Arbitrary per-block mobile padding without project token or block-specific charter. |
| **Exceptions preserved** | Header, footer, mobile sticky bar (BLK-004 class), special promo bands — **excluded** from generic section-gap inheritance. |

### 2.5 Anti-patterns

| Anti-pattern | Action |
|--------------|--------|
| Infer gap from one PDF slice | **STOP** — map tiers to project scale first. |
| Same-bg double padding | Fix to single-boundary rhythm. |
| Global `section { padding: … }` without types | Replace with typed section classes / tokens. |
| Spacing contamination from prior project | Reset to project Production Standards SSOT. |

### 2.6 Section Owns Its Rhythm Law (mandatory)

Spacing between major page regions belongs to the **section or layout region** — not the first/last internal child.

| Ownership | Owner | Examples |
|-----------|-------|----------|
| Section/layout-region rhythm | `.site-header`, `.site-footer`, `section`, `.section` | `padding-block` on layout region |
| Internal component spacing | Component | card padding, control padding, list `gap` |
| Inter-component spacing | Parent of siblings | content grid `gap` |
| Exact geometry | Local exception | evidenced unique geometry |

**Forbidden boundary workarounds:**

```scss
.site-header__bottom { padding-bottom: 18px; } // if this is header-to-hero gap only
.section__last-row { margin-bottom: 70px; }    // if this is section bottom air only
```

**Preferred:** core spacing scale tokens (`--pad-x`, `--pad-y`, `--pad-gap`, `--pad-gap-line`, `--pad-box`) consumed directly by layout regions — **not** selector-named aliases (`--header-padding-block-end`, `--footer-padding-block`). See [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md).

**Rhythm modifiers:** `compact` · `standard` · `large` · `none` — use `--section-padding-compact`, `--section-padding-standard`, `--section-padding-large`.

**Gate:** `SECTION RHYTHM GATE — FAIL` when first/last child simulates section boundary spacing.

**Enforcement:** **MANDATORY DOCUMENTED PRODUCTION GATES** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

**Authority link:** [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) §6.

---

## 3. Project mapping requirement

Before **Frontend Production** (Stage 11), the project **Production Standards** document must include:

| Field | Example |
|-------|---------|
| `section-gap-same-bg` | Inter-section token for same-surface neighbors |
| `section-gap-diff-bg` | Token or rule for surface-change boundaries |
| `section-gap-band` | Full-bleed / major band transition |
| `section-padding-y-default` | Default inner top/bottom inside content sections |
| `section-gap-mobile` | Mobile reduction for inter-section gaps |
| `exceptions` | Header, footer, sticky bar, named special bands |

If mapping is absent → record **SAFE UNKNOWN**; do not start Home page production.

---

## 4. FP-0002 (Shpigovsky.ru) production mapping

> **LEGACY for FP-0002 V6 CLEAN ROOM.** V6 must not import v3 px values. Use `workspaces/fp-0002-shpigovsky-v6/foundation/` + [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md).

**SSOT (v3 instance — read-only for other lanes):** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §6.

| Token / rule | Value | Tier | Usage |
|--------------|-------|------|-------|
| `section-gap-same-bg` | **80px** (`space-12`) | M | Same wash / same elevated surface — **single boundary** only |
| `section-gap-diff-bg` | **80px** default; **56px** (`space-10`) mid transitions | M / S | Surface role change without full band |
| `section-gap-band` | **240px** (`space-16`) | XL | Full-bleed band transitions (hero exit, major CTA bands) |
| `section-padding-y-default` | **80px** top/bottom (`space-12`) engineering default | M | Standard content sections inside `main` |
| `section-gap-mobile` | **64px** (`space-11`) | M (compressed) | Default mobile inter-section unless block override |
| `breadcrumb-to-hero` | **32px** (`space-7`) | — | Wayfinding band |
| **Exceptions** | Header (BLK-001/002), footer (BLK-003), mobile sticky (BLK-004) | — | Do not inherit generic `section-gap` |

---

## 5. Forge / QA hook

Record in REPORT:

```text
SECTION SPACING — PASS | partial (list) | FAIL | SAFE UNKNOWN
```

Use [cadence-governance-checklist.md](../../agents/mars-forge/cadence-governance-checklist.md) for narrative cadence; this rule supplies **token-level** expectations.

---

## 6. Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — created from FP-0002 audit; consolidates vertical-rhythm canon into operational Factory rule. |
| 2026-06-22 | v1.1 — Section Owns Its Rhythm Law §2.6 |
