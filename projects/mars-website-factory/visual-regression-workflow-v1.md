# Visual regression workflow v1 (Wave 5)

**Status:** **documented** — **human-supervised** screenshot discipline for Website Factory workspaces.  
**Not:** AI/CV diff tooling, **not** CI automation, **not** visual testing product claims.

**Pair with:** [production-hardening-rules-v1.md](production-hardening-rules-v1.md), [operational-qa-entry-v1.md](operational-qa-entry-v1.md).

---

## Purpose

Catch layout regressions after section swap, token change, or migration — without building a test platform.

---

## Baseline posture

| Rule | Operator action |
|------|-----------------|
| **When to baseline** | After first `npm run build` PASS on a frozen slice (Standard+) or before replacing a section |
| **Where to store** | `workspaces/<slug>/qa/screenshots/<date>-<block_id>/` — committed only if team policy allows; otherwise local + REPORT path |
| **Naming** | `{viewport}-{state}-{block_id}.png` e.g. `375-default-hero.png`, `768-modal-open-pricing.png` |
| **Browser** | One browser per project (document which — Chrome/Edge typical) |
| **Zoom** | 100% — no OS scaling surprises |

---

## Breakpoint capture discipline

**RU commercial landings:** typography and overflow QA widths are **authoritative** in [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md). The three-width table below is a **supplementary** screenshot minimum for layout regression — not a substitute for the RU preset.

Capture **three widths** minimum per slice (supplementary):

| Viewport | Width | Required states |
|----------|-------|-----------------|
| Mobile | **375px** | default; modal open if slice has `data-modal-open`; sticky visible if `sticky_cta` |
| Tablet | **768px** | default; pricing/social_proof grid if present |
| Desktop | **≥1280px** | default; full page fold if hero/header changed |

**Optional:** 480px when Triumph-style 2-col grids break (document in REPORT).

---

## Before / after comparison flow

```text
1. Baseline   — screenshot PASS slice → store under qa/screenshots/
2. Change     — implement slice (section swap, SCSS, token)
3. Rebuild    — npm run build — record PASS/FAIL
4. After      — same viewport + state names as baseline
5. Compare    — human side-by-side (OS viewer or design tool)
6. REPORT     — list viewports compared; note intentional deltas
```

**Fail criteria (human):** new horizontal scroll, clipped CTA, modal under sticky, overlapping header, broken grid, unreadable hero overlay.

---

## Replacement validation flow

When using [section-replacement-contract-v1.md](section-replacement-contract-v1.md):

1. Screenshot **before** `destroySection` swap (375 + desktop).  
2. Run swap + `initSection`.  
3. Screenshot **after** — same scroll position where possible.  
4. Open modal from new section CTA — one 375 shot.  
5. If form inside section — submit lock visual (disabled state), not live endpoint.

---

## Modal / sticky / overflow validation

| Check | 375px | Desktop |
|-------|-------|---------|
| Modal open | backdrop covers page; body not scrollable | ESC closes; focus visible |
| Sticky CTA | does not cover focused input / footer CTA | below modal z-index |
| Overflow | `document.documentElement.scrollWidth` ≈ viewport | no clipped cards |
| Long FAQ / pricing | accordion/details expand without layout jump breaking sticky | — |

---

## Responsive validation

- Resize manually in DevTools — do not rely on chat descriptions.  
- Record **PASS / FAIL / SAFE UNKNOWN** per viewport in REPORT.  
- If `npm run build` not run — mark visual checks **SAFE UNKNOWN**.

---

## QA evidence posture

REPORT snippet:

```markdown
## Visual regression
- Baseline: workspaces/<slug>/qa/screenshots/2026-05-21-hero/
- Compared: 375 default, 768 default, 1280 default — PASS | FAIL (describe)
- Modal/sticky: 375 modal-open — PASS
- Intentional delta: (none | listed)
```

**Not required:** pixel-diff scores, Percy, Chromatic, or agent vision claims.

*Wave 5 — compact human-supervised visual regression.*
