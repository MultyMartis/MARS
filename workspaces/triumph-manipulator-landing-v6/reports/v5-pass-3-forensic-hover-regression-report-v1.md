# REPORT — V5 Pass 3 Forensic Hover Regression

**Workspace:** `workspaces/triumph-manipulator-landing-v5/`  
**Scope:** PPC zakaz (`index.html`) + shared SCSS  
**Baseline commit:** `6a2c89d` (Pass 2 freeze)  
**Pass 2 authority:** `reports/v5-typography-no-word-splitting-pass-2-report-v1.md`  
**Pass 3 authority:** `reports/v5-typography-live-qa-pass-3-report-v1.md`  
**Build:** `npm run build` — **PASS** (exit 0, ~1.13s)  
**Date:** 2026-05-24

---

## STEP 1 — Pass 3 forensic diff (vs `6a2c89d`)

### SCSS files changed in Pass 3 (9)

| File | Pass 3 changes |
|------|----------------|
| `src/scss/utils/_section-headings.scss` | Tablet H2 `clamp(40px, 5.2vw, 64px)` ≤1180px; line-height 1.1→1.08; mixin adds `text-wrap: balance` |
| `src/scss/base/_base.scss` | `.section-title` `pretty`→`balance`; new `.section-heading--center .section-title { max-width: min(920px, 100%) }` |
| `src/scss/sections/_v5-page01-overrides.scss` | `.machine-transport__heading` + `text-wrap: balance`; PPC transport stack breakpoint **1320→1440px**; contact CTA `pretty`→`balance` |
| `src/scss/sections/_v5-pricing-factors.scss` | 2-col pricing grid ≤1440px; `min-width: 0`; word-boundary rules; tiered `max-width` |
| `src/scss/sections/_v5-hero-extensions.scss` | H1 `pretty`→`balance`; mobile span `display: inline` ≤760px |
| `src/scss/sections/_final-contact-cta.scss` | CTA H2 `pretty`→`balance` |
| `src/scss/sections/_screen-04-faq.scss` | `.faq__title` balance; summary `text-wrap: pretty`; `.faq-item summary span { white-space: nowrap }` |
| `src/scss/sections/_screen-03-trust-reviews.scss` | `.trust__title` `text-wrap: balance` |
| `src/scss/sections/_v5-order-steps.scss` | Step titles `overflow-wrap: normal; word-break: normal; text-wrap: pretty` |

**Not changed in Pass 3 diff vs `6a2c89d`:** `src/scss/components/_interactions.scss` (hover rules pre-existed baseline).

### HTML partials changed in Pass 3 (5 — zakaz/index only)

| Partial | Pass 3 changes |
|---------|----------------|
| `v5-ppc/zakaz/screen-02-tasks.html` | Heading tie `подходит&nbsp;манипулятор`; list spans → normal spaces + selective units |
| `v5-ppc/zakaz/screen-01-hero.html` | Notice → selective ties (removed full `&nbsp;` chain) |
| `v5-ppc/zakaz/screen-02b-order-steps.html` | `Как заказать&nbsp;манипулятор` |
| `v5-ppc/zakaz/screen-02c-pricing-factors.html` | `Стоимость аренды&nbsp;манипулятора` |
| `v5-ppc/zakaz/final-contact-cta.html` | `Нужно заказать&nbsp;манипулятор?` |

### Rules added (Pass 3)

- Global/mixin `text-wrap: balance` on section H2 mixin (`_section-headings.scss`)
- `.section-heading--center .section-title { max-width: min(920px, 100%) }`
- `.machine-transport__heading { text-wrap: balance }`
- `@media (max-width: 1440px)` PPC transport single-column stack (was 1320)
- Pricing factors 2-col breakpoint at 1440 + max-width tiers
- FAQ summary `text-wrap: pretty` + number span `white-space: nowrap`
- Hero mobile span `display: inline` ≤760px
- Order step title overflow-safe + `text-wrap: pretty`

### Rules changed (Pass 3)

- Multiple headings: `text-wrap: pretty` → `text-wrap: balance` (section titles, hero H1, contact CTA, trust title)
- PPC transport stack media query threshold: **1320px → 1440px**

### Rules that could affect `.machine-transport__heading`

| Change | Mechanism | Impact on heading |
|--------|-----------|-------------------|
| `text-wrap: balance` on `.machine-transport__heading` | Browser tries to equalize line lengths | In narrow card (~501px @1440 3-col) forces awkward 3-line rhythm |
| Breakpoint **1320→1440** | Delays single-column stack | At 1321–1440px heading stays in **1.58fr column (~583px)** instead of full card width (~1185px) |
| HTML `подходит&nbsp;манипулятор` | Unbreakable last two words | With balance + narrow width, earlier lines break at worse points |
| `_section-headings.scss` clamp/line-height | Does **not** apply — heading uses own `clamp(28px, 3.6vw, 50px)` | No direct font-size regression |

---

## Unauthorized hover root cause

### Exact location

```scss
// src/scss/components/_interactions.scss (lines 204–218 pre-fix)
.machine-transport__card,
.proof-strip__item,
.machine-showcase__media {
    @include hover-lift;
}

.machine-transport__card {
    @include motion-safe {
        &:hover,
        &:focus-within {
            transform: translateY(-1px);
            box-shadow: 0 16px 36px rgba(9, 15, 27, 0.1);
        }
    }
}
```

### Was it in `6a2c89d`?

**Yes.** Identical block present in commit `6a2c89d` and initial baseline `f86dd59`. Pass 3 **did not modify** `_interactions.scss` — hover was **not introduced by Pass 3 diff**, but was **latent from V5 baseline** and became visible/attributed during typography QA cycles.

### Relation to typography task

**None.** Typography Pass 2/3 scope was word-boundary protection, `&nbsp;` discipline, `text-wrap`, breakpoints for **line breaks** — not card interaction polish. Hover lift + elevated shadow is a **visual enhancement** on a non-interactive `<section>` card.

### Why unauthorized

- Task charter: typography / no word-splitting QA — **no hover/focus effects authorized**
- Cards are informational containers, not buttons/links — hover implies false affordance
- `transform` + `box-shadow` change is **motion + visual design**, outside typography scope
- Pass 3 report did not document this rule — operator discovery = scope drift from baseline interactions layer

---

## Transport heading regression root cause

**Symptom:** «Для каких задач подходит манипулятор» wraps worse after Pass 3; list item «Работа на строительных объектах» improved.

**Exact cause (compound, not guessed):**

1. **Grid breakpoint regression (primary)**  
   Pass 2 (`6a2c89d`): `@media (max-width: 1320px)` → single-column stack, allowed card spans full width.  
   Pass 3: threshold raised to **1440px** → at viewports **1321–1440px** the 3-column grid remains:

   ```scss
   // _screen-02-prices.scss
   grid-template-columns: minmax(0, 1.58fr) minmax(310px, 1.02fr) minmax(250px, 0.78fr);
   ```

   Allowed card width drops from ~1185px (stacked) to ~**583px** (1.58fr of ~1305px shell). Heading at `clamp(28px, 3.6vw, 50px)` uppercase has far less horizontal space.

2. **`text-wrap: balance` on heading (secondary)**  
   Pass 2: no `text-wrap` on desktop `.machine-transport__heading`.  
   Pass 3: added `text-wrap: balance` — in ~583px column, balance algorithm produces **3 tight uneven lines** instead of natural space breaks.

3. **HTML nbsp tie (tertiary)**  
   Pass 2: `Для&nbsp;каких задач подходит манипулятор`  
   Pass 3: `Для&nbsp;каких задач подходит&nbsp;манипулятор`  
   The `подходит&nbsp;манипулятор` pair cannot split — in a narrow column this forces the break earlier in the phrase.

**Why list items improved:** Pass 3 removed per-word `&nbsp;` chains in `<span>` text (e.g. `Работа на&nbsp;строительных объектах`) — correct typography fix, unrelated to heading grid width.

---

## What was reverted

| Item | Action |
|------|--------|
| `.machine-transport__card:hover` / `:focus-within` block | **Removed** from `_interactions.scss` |
| `.machine-transport__card` from `@include hover-lift` group | **Removed** (no transition/hover on card) |
| PPC transport stack breakpoint | **1440px → 1320px** (Pass 2 value) |
| `.machine-transport__heading { text-wrap: balance }` | **Removed** (Pass 2: no desktop text-wrap) |
| Heading HTML nbsp tie | **`подходит&nbsp;манипулятор` → `подходит манипулятор`** (Pass 2 value) |

**Kept from Pass 3 (non-regressive):** list item normal spaces, hero notice ties, section-title balance, pricing grid, FAQ nowrap, other Pass 3 HTML partials unchanged in this forensic pass.

---

## What was minimally fixed

1. Unauthorized card hover/focus — deleted, not replaced.
2. Transport heading — restored Pass 2 breakpoint + removed balance + restored Pass 2 nbsp pattern for this phrase only.
3. List typography improvements from Pass 3 retained.

---

## Build validation

```
npm run build → exit 0 (~1.13s)
```

| Check | Result |
|-------|--------|
| Build PASS | **Yes** |
| `.machine-transport__card:hover` in dist CSS | **None** |
| `.machine-transport__card:focus-within` in dist CSS | **None** |
| `0 16px 36px` shadow (card hover) in dist CSS | **None** |
| `.machine-transport__heading` has `text-wrap: balance` | **None** (desktop block) |
| PPC transport stack `@media (max-width: 1320px)` | **Present** (lines ~4330, ~4685) |
| `overflow-wrap: anywhere` / `word-break: break-all` / `break-word` / `hyphens: auto` | **None** in dist scan |
| Compiled heading HTML | `Для&nbsp;каких задач подходит манипулятор` |

**Headless line-break proof:** not run in this task — browser QA required.

---

## Governance lesson

### Why hover appeared during typography work

| Classification | Assessment |
|----------------|------------|
| Prompt too broad? | **Partial** — Pass 3 preset allows layout rhythm (breakpoints, max-width) but does not explicitly forbid **reading/re-surfacing** pre-existing interaction CSS |
| Visual enhancement drift? | **Yes** — hover on static cards is polish, not typography |
| Agent overreach? | **Yes (attribution)** — Pass 3 agent likely did not add hover, but baseline interactions were not scoped out; operator correctly flagged as unauthorized for typography lane |
| Missing forbidden rule? | **Yes** — no explicit **「typography QA MUST NOT touch `_interactions.scss` or add hover/focus/transform/box-shadow」** in task envelope |

### Proposed Website Factory rule (NOT implemented)

Add to typography QA task template / `ru-landing-qa-preset-v1.md` enforcement block:

> **Typography-only scope lock:** Agents MUST NOT add, modify, or retain hover/focus/active visual effects (`transform`, `box-shadow`, `filter`, `opacity` transitions) unless the task charter explicitly authorizes interaction polish. Pre-existing interaction rules in `components/_interactions.scss` are **out of scope** — report as FINDING, do not extend. Allowed: `font-size`, `line-height`, `letter-spacing`, `text-wrap`, `max-width`, selective `&nbsp;`, grid breakpoints **only when justified by line-break evidence**.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Visual wrap quality at 1320–1440px after revert | **UNKNOWN** — CSS logic restored to Pass 2; no browser screenshot |
| Safari/Firefox `text-wrap` on other Pass 3 headings still using `balance` | **UNKNOWN** — unchanged in this pass |
| Whether removing hover-lift transition on card affects perceived card static shadow | **UNKNOWN** — card base shadow from `_screen-02-prices.scss` unchanged |
| Other PPC pages transport headings | **UNKNOWN** — HTML fix scoped to zakaz partial only |

---

## Browser QA required

Manual check on **`dist/index.html`** at:

- **1320px, 1366px, 1440px** — transport heading should stack full-width ≤1320; no 3-col squeeze at 1320
- **1180px, 760px, 375px, 320px** — heading wraps at spaces only; no mid-word split on «манипулятор»
- **Hover** — `.machine-transport__card` must NOT lift or change shadow on hover/focus-within

---

## Changed files (this forensic pass)

**SCSS (2):** `_interactions.scss`, `_v5-page01-overrides.scss`  
**HTML (1):** `v5-ppc/zakaz/screen-02-tasks.html`  
**Report (1):** this file  

**Git:** no commit, no push (per task).
