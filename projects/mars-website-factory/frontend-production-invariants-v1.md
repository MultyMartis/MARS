# MARS Website Factory — Frontend Production Invariants v1

**Status:** **documented** — compact **anti-drift** rules from Triumph Manipulator V5 FAQ + CTA + build/debug incidents.  
**Not:** runtime enforcement, automated lint, or project-specific handoff replacement.

**Purpose:** Stop repeat failures in responsive breakpoints, container geometry, native FAQ state, CSS multicol browser compatibility, typography ties, build verification, and Windows dist locks.

**Reference signal (lessons only — not copy source):** Triumph V5 FAQ/CTA/build incidents in `workspaces/triumph-manipulator-landing-v5/reports/`; WPilot footer multicol incident on dev.gktriumph.ru — [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md).

**Related:** [frontend-production-rules-v0.md](frontend-production-rules-v0.md) · [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) · [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) · [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) · [terminal-survivability-governance.md](terminal-survivability-governance.md) · [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md) · [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md) · [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) · [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md)

---

## 1. Responsive invariants

| Rule | Detail |
|------|--------|
| **Project breakpoints only** | Use breakpoints defined in handoff, tokens, or project SCSS — **do not invent local breakpoints** in section partials. |
| **Triumph V5 / current V5 lane** | **Desktop:** `1025px+` · **Tablet/mobile:** `max-width: 1024px` |
| **Forbidden drift** | Ad-hoc `980px` / `981px` (or similar) unless **explicitly** defined by the project handoff or token file. |

When handoff and project tokens disagree, stop and report **SAFE UNKNOWN** — do not silently pick a convenience breakpoint.

---

## 2. Container discipline

| Rule | Detail |
|------|--------|
| **Split layouts inside shell** | 50/50, FAQ+CTA, and other column splits must live inside the canonical **content container** / **section-shell** unless the prompt explicitly requests full-bleed. |
| **50/50 meaning** | “50/50” means **50/50 inside the content shell**, not viewport-wide columns that bypass max-width. |
| **No shell bypass** | Do not break out of `section-shell` / container width system to “fix” alignment — adjust grid/flex **within** the shell. |
| **Section ≠ container** | Do not put container width class on `<section>` / `<nav>` — see [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) (WF-GRID-001). |
| **No default % hero splits** | Inner-zone hero/card/trust/finance layout follows [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) — fr/minmax authority; `%` only via documented exception (WF-LAYOUT-007). |

---

## 3. Layout geometry / decorative elements

| Rule | Detail |
|------|--------|
| **Decorators ≠ geometry** | Decorative borders, dividers, and accent lines must **not** alter required layout geometry. |
| **Equal splits stay symmetric** | In equal column splits, **do not** shift one column with `padding-left` + `border-left` (or equivalent) while the sibling stays flush. |
| **Safe divider pattern** | Use `::before` / `::after` pseudo-elements or **absolute** positioning for decorative dividers so column widths and gutters remain symmetric. |

---

## 4. Native `<details>` / `<summary>` rules

| Rule | Detail |
|------|--------|
| **`open` is SoT** | For native `<details>`, the **`open` attribute** is the single source of truth for expanded/collapsed state. |
| **No hybrid visibility** | **Forbidden:** combining native `<details>` toggle with JS-driven inline `max-height` / `display` / `visibility` accordion logic on the same panel. |
| **Allowed JS scope** | JS may coordinate **single-open** behavior (close siblings) and **ARIA sync** only — not replace native open/close. |
| **Custom animation path** | If fully custom animation or non-native state is required, use a **custom** `button` / `motion` / `data-*` accordion — **not** a hybrid native/custom component. |

---

## 5. FAQ pattern rule

| Rule | Detail |
|------|--------|
| **Avoid 2-col grid accordion** | Do **not** use two-column CSS Grid for FAQ items when answers expand vertically — grid rows **stretch neighboring cards**. |
| **Preferred desktop layout** | For short FAQ answers, prefer **single-column FAQ** with adjacent CTA/sidebar when desktop space must be used. |
| **Mandatory QA** | Open · close · single-open · **neighbor stretch** · viewport jump · keyboard · mobile stack |

Full FAQ QA checklist: [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) § FAQ interaction checks.

---

## 6. Typographic non-breaking spaces

**Authority for CSS overflow:** [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md).

| Do | Do not |
|----|--------|
| `&nbsp;` after short prepositions, conjunctions, service words | Glue **long semantic word pairs** in adaptive headings |
| Units, dates, abbreviations: `5&nbsp;т`, `14&nbsp;м`, `и&nbsp;т.д.` | Chains of `&nbsp;` as a **layout fix** |
| `в&nbsp;Краснодаре` | `заказать&nbsp;манипулятор`, `Нужно заказать&nbsp;манипулятор?` |

For headings under width pressure: prefer **container width**, **font-size**, and **`text-wrap: balance`** over non-breaking chains.

---

## 7. CSS multicol masonry — Chrome / Firefox compatibility

**Authority (full lesson):** [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md)

| Rule | Detail |
|------|--------|
| **Separate engine QA** | CSS `columns` / `column-count` masonry-style groupings must be checked in **Chrome desktop**, **Firefox desktop**, and **mobile Chromium** — not one engine only. |
| **Firefox ≠ Chrome proof** | Do **not** treat Firefox-correct layout as proof for Chrome. |
| **Group wrapper display** | Prefer **`display: block`** on column group wrappers with `break-inside: avoid` (+ `-webkit-column-break-inside`, `page-break-inside`). |
| **Avoid inline-block default** | Do **not** default to **`display: inline-block`** on multicol group wrappers without verified cross-browser reason. |

**Scope:** Website Factory static frontends, MARS Forge, WPilot footer edits, legacy WordPress/The7/WPBakery footers, any footer/link-cloud multicol layout.

---

## 8. Build verification / stale dist

| Rule | Detail |
|------|--------|
| **Failed build = no success claim** | If `npm run build` (or project equivalent) **fails**, do **not** claim success in REPORT. |
| **Stale dist assumption** | On build failure, assume **`dist/` may be stale** — prior output does not prove current source state. |
| **Browser claims need build** | Do **not** claim browser-visible changes are applied until build **succeeds** and output is verified. |
| **Dist verification** | When the operator checks `dist/index.html`, verify **compiled dist CSS/HTML** — not source-only edits. |

Inherits [frontend-production-rules-v0.md](frontend-production-rules-v0.md) §1–§2 (source-first, no dist edits).

---

## 9. Windows build survivability

| Rule | Detail |
|------|--------|
| **EBUSY on dist root** | On Windows, deleting the **`dist/` folder root** can fail with **EBUSY** when files are open in browser, editor, or static server. |
| **Prefer contents delete** | Prefer deleting **dist contents** (files inside) instead of removing the `dist/` folder itself, when the build pipeline supports it. |
| **Report lock clearly** | On EBUSY, report the lock in REPORT; tell the operator to close browser tab, editor handle, or local server serving `dist/`. |

See also [terminal-survivability-governance.md](terminal-survivability-governance.md).

---

## 10. Scroll Process Timeline — approved commercial interaction pattern

**Authority (full pattern):** [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md)  
**Registry:** [registries.md](registries.md) §3 — `pattern_id`: `scroll_process_timeline` · token: `WF-SCROLL-PROCESS-TIMELINE`

| Rule | Detail |
|------|--------|
| **User-controlled motion** | Scroll-driven progress only — **no** autoplay, loops, or decorative motion without user scroll |
| **Track-relative movement** | Vehicle/progress moves relative to **track width**, not element `translateX(100%)` self-width |
| **Zero start** | `setProgress(0)` on load — no mid-route jump on large viewports |
| **Scoped implementation** | Scoped CSS/JS; no theme or cross-page leakage; WPBakery Raw HTML allowed when scoped |
| **Reverse scroll** | Scroll-up must decrease progress — progress line and vehicle stay synchronized |

Full QA checklist and Triumph case study: [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md).

---

## 11. Reusable prompt invariant block (V5 / frontend tasks)

Paste into Cursor frontend execution prompts when scope is V5 lane or Triumph-class Gulp static work:

```text
Project invariants:
- Main breakpoint: 1024/1025.
- Do not invent 980/981 breakpoints.
- Desktop: 1025px+.
- Tablet/mobile: max-width 1024px.
- Keep split layouts inside existing section-shell/content container.
- Do not use &nbsp; between long words in headings.
- For native <details>, open is the single source of truth.
- If build fails, dist is stale; do not claim success.
- Do not touch forms unless explicitly requested.
```

Canonical copy also lives in [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) §3b.

---

## REPORT lines (optional add-ons)

```text
FRONTEND INVARIANTS — PASS | partial (list) | FAIL | SAFE UNKNOWN
CSS MULTICOL MASONRY BROWSER QA — PASS (Chrome + Firefox + mobile Chromium) | partial (list) | FAIL | N/A | SAFE UNKNOWN
SCROLL PROCESS TIMELINE — PASS | partial (list) | FAIL | N/A | SAFE UNKNOWN
BUILD / DIST — PASS (command + exit 0) | FAIL | STALE (build not run or failed)
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — Triumph V5 FAQ/CTA/build incident lessons; responsive, container, FAQ, build, Windows dist rules |
| 2026-06-17 | §7 — CSS multicol masonry Chrome/Firefox compatibility; link to [css-multicol-masonry-browser-compatibility-lesson-v1.md](css-multicol-masonry-browser-compatibility-lesson-v1.md) |
| 2026-06-18 | §10 — Scroll Process Timeline approved commercial interaction pattern; link to [scroll-process-timeline-pattern-v1.md](scroll-process-timeline-pattern-v1.md) |
