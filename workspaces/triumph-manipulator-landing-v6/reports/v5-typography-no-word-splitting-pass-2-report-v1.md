# REPORT — V5 Typography No Word Splitting Pass 2

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Page scope:** `index.html` (PPC zakaz) + its partials only for HTML  
**Build:** `npm run build` — **PASS** (exit 0, ~1.27s)  
**Date:** 2026-05-24

---

## Root CSS cause

Two compounding causes produced mid-word breaks (e.g. `манипулято` / `р?`):

1. **Global `overflow-wrap: break-word` on `body`** (`src/scss/base/_base.scss`) — inherited by all text, including headings and UI labels.
2. **Over-aggressive `&nbsp;` in visible headings** — strings like `Для&nbsp;каких&nbsp;задач&nbsp;подходит&nbsp;манипулятор` and `Нужно&nbsp;заказать&nbsp;манипулятор?` formed one long unbreakable run. When the line did not fit, the browser broke **inside** words instead of at normal spaces.

Pass 2 removes the global break-word inheritance and restores normal word boundaries in headings while keeping selective RU typography ties.

---

## Global rules changed

| File | Change |
|------|--------|
| `src/scss/base/_base.scss` | Removed `overflow-wrap: break-word` from `body`. Added `html, body { word-break: normal; hyphens: manual; }`. |
| `src/scss/base/_typography-protection.scss` | **New** — centralized no-split rules for headings/UI; explicit `overflow-wrap: break-word` allowlist for paragraph/body copy only. |
| `src/scss/style.scss` | Imports `base/typography-protection` after `base/base`. |

**Not set globally:** `overflow-wrap: break-word`, `overflow-wrap: anywhere`, `word-break: break-all`, `word-break: break-word`, `hyphens: auto`.

---

## Protected selectors

Hard protection (`overflow-wrap: normal; word-break: normal; hyphens: manual`) in `_typography-protection.scss`:

**Headings:** `h1–h4`, `.section-title`, `.hero__title`, `.hero__title span`, `.machine-showcase__title`, `.machine-transport__heading`, `.machine-transport__heading span`, `.trust__title`, `.review-panel__title`, `.faq__title`, `.contact-cta h2`.

**UI chrome:** `.button`, `.site-header a`, `.hero__specs li`, `.hero__cargo-card`, `.machine-showcase__specs dt/dd`, `.machine-transport__list li`, `.faq-item summary`, `.site-form label`, `.site-form__consent-text`, `.proof-strip__item`, `.landing-footer a`.

**Reinforced in existing files:** `_final-contact-cta.scss` (`.contact-cta h2`), prior pass-1 rules in section/component SCSS retained.

**Body copy allowlist** (break-word permitted): `p`, `.section-lead`, hero/showcase/transport notes, `.faq-item__body p`, contact/trust/pricing/order-steps paragraphs, form lead/note text.

---

## Broken blocks fixed

### 1. `.machine-transport__heading`

- **HTML:** `Для&nbsp;каких&nbsp;задач&nbsp;подходит&nbsp;манипулятор` → `Для&nbsp;каких задач подходит манипулятор` — normal spaces allow multi-line wrap without splitting `манипулятор`.
- **Layout:** PPC grid breakpoint raised in `_v5-page01-overrides.scss` from `1180px` → **`1320px`** so `.machine-transport__card--allowed` spans full width earlier; heading gets full card width instead of a narrow first column in the 3-column grid.

### 2. `.contact-cta h2`

- **HTML:** `Нужно&nbsp;заказать&nbsp;манипулятор?` → `Нужно заказать манипулятор?`
- **CSS:** explicit no-split on `.contact-cta h2` in `_final-contact-cta.scss` + typography-protection block.

### 3. Other headings on index (манипулятор / машины / Краснодар)

- Hero H1: `Аренда манипулятора <span>в&nbsp;Краснодаре</span>` — removed nbsp between every word; kept `в&nbsp;Краснодаре`.
- `.machine-showcase__title`: `Параметры нашей машины` — normal spaces.
- `.section-title` (order/pricing): `Как&nbsp;заказать манипулятор`, `Стоимость аренды манипулятора`.
- FAQ summaries: normal spaces; no nbsp chains on questions containing «манипулятор».

---

## Visible text typography

**Index partials updated (visible text only; meta/alt/JSON-LD/href/src/data-* untouched):**

| Partial | Fixes |
|---------|-------|
| `v5-ppc/zakaz/screen-01-hero.html` | Hero title/lead — selective nbsp: `5&nbsp;т`, `и&nbsp;краю`, `Без&nbsp;посредников`, `в&nbsp;Краснодаре` |
| `v5-ppc/zakaz/screen-02-specs.html` | Showcase title/lead/ops — numbers+units, short ties |
| `v5-ppc/zakaz/screen-02-tasks.html` | Transport heading (see above) |
| `v5-ppc/zakaz/screen-02b-order-steps.html` | Section title; `до&nbsp;выезда` |
| `v5-ppc/zakaz/screen-02c-pricing-factors.html` | Section title/lead; em dash `—` |
| `v5-ppc/zakaz/screen-04-faq.html` | Summaries + answers — normal spaces; units `5&nbsp;т`, `14&nbsp;м`, `2&nbsp;часа`; `до&nbsp;выезда`, `по&nbsp;краю` |
| `v5-ppc/zakaz/final-contact-cta.html` | CTA H2 + lead — em dash, selective nbsp |

Shared partials (`header`, `trust`, `footer`, `callback-modal`) already had reasonable typography from pass 1; not re-edited unless included in index includes without changes needed.

---

## Build validation

```
npm run build → exit 0
```

**`dist/assets/css/style.css` scan:**

| Rule | Result |
|------|--------|
| `overflow-wrap: anywhere` | **None** |
| `word-break: break-all` | **None** |
| `word-break: break-word` | **None** |
| `hyphens: auto` | **None** |
| `overflow-wrap: break-word` | **2 occurrences** — body-copy allowlist block (~line 302: `p`, `.section-lead`, …) and `.faq-item__body p` (~line 2952). **Allowed.** |
| `html, body { word-break: normal; hyphens: manual; }` | **Present** at top of compiled CSS |

---

## Remaining SAFE UNKNOWN

| Item | Status |
|------|--------|
| Visual QA on real devices after pass 2 | **UNKNOWN** — build + CSS scan pass; no browser screenshot in this task |
| Ultra-narrow (<360px) overflow for longest FAQ summary strings | **UNKNOWN** — protected with `overflow-wrap: normal`; may need layout tweak if clip observed |
| `text-wrap: pretty` / `balance` interaction with protected headings on Safari | **UNKNOWN** |
| Other PPC pages (not index) still carry pass-1 nbsp chains in headings | **UNKNOWN for this task** — HTML edits scoped to index partials only |
| Long English tokens (Telegram, WhatsApp) in footer/contact | **UNKNOWN** — may wrap whole token or overflow on very narrow widths |

---

## Browser QA required

Manual check recommended at these widths on **`dist/index.html`**:

- **320px, 375px, 390px** — hero H1, `.machine-transport__heading`, `.contact-cta h2`, FAQ summaries
- **760px** — transport card stack, contact CTA grid
- **1180–1320px** — transport grid transition (allowed card full width)
- **Desktop ≥1400px** — three-column transport grid; heading should wrap on spaces, never split `манипулятор` / `машины`

**Verify:** no `манипулято-`, `Краснод-`, `маш-` style splits; headings wrap only at spaces; body paragraphs may wrap long lines normally.

---

## Changed files (pass 2 only)

**SCSS (5):**  
`_base.scss`, `_typography-protection.scss` (new), `style.scss`, `_final-contact-cta.scss`, `_v5-page01-overrides.scss`

**HTML — index partials (7):**  
`zakaz/screen-01-hero.html`, `screen-02-specs.html`, `screen-02-tasks.html`, `screen-02b-order-steps.html`, `screen-02c-pricing-factors.html`, `screen-04-faq.html`, `final-contact-cta.html`

**Report (1):** this file

**Git:** no commit, no push (per task).
