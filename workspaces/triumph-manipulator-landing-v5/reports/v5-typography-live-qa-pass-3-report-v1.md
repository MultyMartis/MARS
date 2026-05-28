# REPORT — V5 Typography Live QA Pass 3

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Scope:** `index.html` (PPC zakaz) + shared typography SCSS  
**Authority:** [russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md), [ru-landing-qa-preset-v1.md](../../../projects/mars-website-factory/ru-landing-qa-preset-v1.md)  
**Build:** `npm run build` — **PASS** (exit 0)  
**Date:** 2026-05-24

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — partial (320px drawer scroll; other PPC pages not re-tested)
```

---

## Method

- Read governance canon + preset + integrity/stabilization reports (authority order).
- Headless Chromium (Playwright) line-break analysis on `dist/index.html` at preset widths: **320 · 375 · 390 · 420 · 760 · 1180 · 1320 · 1440**.
- CSS source scan for forbidden word-breaking rules.
- Fixes limited to typography rhythm (font-size, line-height, max-width, `text-wrap`, grid breakpoints, selective `&nbsp;`) — **no** layout redesign, color, or semantic changes.

---

## Issues found (before fixes)

| Area | Widths | Issue |
|------|--------|-------|
| `.section-title` (order, pricing) | 1180, 1320 | 72px H2 in full container → awkward multi-line rhythm; risk of widow «манипулятора» |
| `.machine-transport__heading` | 1440 | 3-column grid → card ~501px; 50px uppercase heading wrapped to 3 tight lines |
| `.machine-transport` cards | 1440 | Allowed/denied/CTA columns **583 / 377 / 288 px** — too narrow for current type scale |
| `.pricing-factors__list` | 1180–1440 | 3-column grid → cells **~315 px** — tight for RU labels |
| `.faq-item summary` | 320–390 | FAQ number (`3.`, `5.`) orphaned on its own line |
| `.hero__notice` | all | Full `&nbsp;` chain — governance drift (pass-2 heuristic) |
| `.machine-transport__list` (zakaz) | all | `&nbsp;` between every word in list spans |
| `.hero__title span` | 320–420 | Block span forced «в Краснодаре» onto separate short line |
| Horizontal scroll | 320–420 | **425px** scroll width — mostly **off-canvas mobile drawer**, not body copy |

**No** `overflow-wrap: anywhere`, `word-break: break-all`, `word-break: break-word`, or `hyphens: auto` in `src/`.

---

## Fixes applied

### SCSS

| File | Change |
|------|--------|
| `utils/_section-headings.scss` | Tablet H2 scale `clamp(40px, 5.2vw, 64px)` ≤1180px; tighter line-height; mixin adds `text-wrap: balance` |
| `base/_base.scss` | `.section-title` → `text-wrap: balance`; centered titles `max-width: min(920px, 100%)` |
| `sections/_v5-page01-overrides.scss` | PPC transport stack breakpoint **1320 → 1440px**; `.machine-transport__heading` + contact CTA → `text-wrap: balance` |
| `sections/_v5-pricing-factors.scss` | 2-column pricing grid ≤**1440px** (was 3-col at 1440); card `min-width: 0`; normal word boundaries on list items |
| `sections/_v5-hero-extensions.scss` | H1 `text-wrap: balance`; mobile span `display: inline` (≤760px) to reduce orphan location line |
| `sections/_final-contact-cta.scss` | CTA H2 `text-wrap: balance` |
| `sections/_screen-04-faq.scss` | `.faq__title` balance; summary `text-wrap: pretty`; number span `white-space: nowrap` |
| `sections/_screen-03-trust-reviews.scss` | `.trust__title` `text-wrap: balance` |
| `sections/_v5-order-steps.scss` | Step titles overflow-safe + `text-wrap: pretty` |

### HTML (zakaz / index partials only)

| Partial | Change |
|---------|--------|
| `screen-02c-pricing-factors.html` | `Стоимость аренды&nbsp;манипулятора` (widow tie) |
| `screen-02b-order-steps.html` | `Как заказать&nbsp;манипулятор` |
| `screen-02-tasks.html` | Heading tie `подходит&nbsp;манипулятор`; list items → normal spaces + selective units |
| `screen-01-hero.html` | Notice → selective ties only (no word chains) |
| `final-contact-cta.html` | `Нужно заказать&nbsp;манипулятор?` |

---

## Viewport-specific findings (after fixes)

| Width | Transport card W | Pricing cell W | H-scroll | Notes |
|-------|------------------|----------------|----------|-------|
| **320** | 284px | 284px | **347px** (drawer) | Main content fits; drawer still extends past viewport |
| **375** | 324px | 324px | none | FAQ number orphans mitigated (`nowrap` on index span) |
| **390** | 339px | 339px | none | — |
| **420** | 369px | 369px | none | — |
| **760** | 709px | 709px | none | Section H2 uses mobile scale |
| **1180** | 980px (stacked) | **421px** (2-col) | none | H2 ~64px max via mixin |
| **1320** | 1185px | 421px | none | — |
| **1440** | **1305px** (stacked) | **471px** (2-col) | none | Was 583/315px 3-col — **resolved** |

**Mid-word splits:** none detected on protected headings/UI in headless pass.  
**Orphan heuristics:** FAQ `3.` / `5.` at 320 — **mitigated** via `summary span { white-space: nowrap }`.

---

## Governance regression check

| Rule | Result |
|------|--------|
| No global `break-word` / `anywhere` / `break-all` | **PASS** — pass-2 `_typography-protection.scss` intact |
| Headings/UI `overflow-wrap: normal` | **PASS** |
| `overflow-wrap: break-word` only on long body | **PASS** (allowlist unchanged) |
| Selective `&nbsp;` only | **PASS** on index partials touched; **other PPC pages** still have pass-1 chains — **SAFE UNKNOWN** |
| `text-wrap: balance` on headings | **Allowed** — applied where safe; not on buttons |

### Old rules vs implementation

- **No conflict** with canon on forbidden CSS.
- **Supplementary** generic QA widths (375/768) vs preset **760/1180** — operator tested preset list; no doc conflict during implementation.
- **Forge/hardening** stricter `word-break: break-word` ban — not triggered; only `overflow-wrap: break-word` on body allowlist retained.

---

## Remaining SAFE UNKNOWN

| Item | Status |
|------|--------|
| 320px horizontal scroll (off-canvas drawer ~347px) | **UNKNOWN** if operator-visible; not fixed (header drawer, out of typography scope) |
| Safari / Firefox `text-wrap: balance` rendering | **UNKNOWN** — Chromium used for pass |
| Other PPC landings (armatura, bytovki, …) | **UNKNOWN** — HTML `&nbsp;` chains may remain |
| Trust section long H2 at 72px on very wide cards | **UNKNOWN** — balance added; no screenshot sign-off |
| CMS / dynamic copy | **UNKNOWN** per canon §5 |

---

## Build validation

```
npm run build → exit 0 (~1.4s)
```

---

## Changed files (pass 3)

**SCSS (9):**  
`_section-headings.scss`, `_base.scss`, `_v5-page01-overrides.scss`, `_v5-pricing-factors.scss`, `_v5-hero-extensions.scss`, `_final-contact-cta.scss`, `_screen-04-faq.scss`, `_screen-03-trust-reviews.scss`, `_v5-order-steps.scss`

**HTML — zakaz index (5):**  
`screen-01-hero.html`, `screen-02-tasks.html`, `screen-02b-order-steps.html`, `screen-02c-pricing-factors.html`, `final-contact-cta.html`

**Report (1):** this file

**Diagnostic (local, not committed):** `tools/typography-qa-pass3.mjs`, `tools/typography-qa-pass3-dump.cjs`

**Git:** no commit, no push (per task).
