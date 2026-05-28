# V5 Production Hardening Batch B Report

**Date:** 2026-05-24  
**Baseline:** `f86dd59` — `checkpoint: add Triumph landing v5 baseline`  
**Scope:** Batch B only (typography, mobile overflow, line-height +4px, nowrap/anywhere cleanup)  
**Built page:** `src/pages/index.html` → `dist/index.html` (zakaz / page-01)

---

## Scope

| Allowed | Done |
|---------|------|
| V5 `src/scss/**` typography/overflow fixes | Yes |
| V5 `reports/` | Yes |
| `npm run build` (regen `dist/`) | Yes — **PASS** |

| Forbidden | Status |
|-----------|--------|
| Redesign / layout / sections | Not touched |
| Forms backend / `form.js` | Not touched |
| Assets / schema / HTML partials | Not touched |
| 12-page generator rollout | Not touched |
| V4, ORCA, governance, survivability | Not touched |
| commit / push | Not done |

---

## Changes by area

### H1 / H2 wrapping

| File | Change |
|------|--------|
| `_v5-hero-extensions.scss` | H1: added **420px** band; removed fixed `line-height: 42px` at 320px → ratio **1.12**; consistent mobile wrapping |
| `_section-headings.scss` | Section H2: added **375px** font step; **420px** line-height **1.12** |
| `_final-contact-cta.scss` | Contact H2 lead copy: `line-height: calc(1em + 4px)` on mobile |

### Header nowrap cleanup

| File | Change |
|------|--------|
| `_header.scss` | Removed `white-space: nowrap` from nav, phone, CTA; added `overflow-wrap: break-word`, `flex-wrap` on nav; narrow-desktop actions wrap (761–1240px); `line-height: calc(1em + 4px)` |

### Specs nowrap / line-height

| File | Change |
|------|--------|
| `_screen-02-prices.scss` | `dd`: `line-height: calc(1em + 4px)`; `nowrap` scoped to **≥761px** only; mobile `break-word` (was `anywhere`) |
| `_v5-page01-overrides.scss` | Mobile spec `dd`: explicit `overflow-wrap: break-word` |

### overflow-wrap: anywhere → break-word

| Selector | File |
|----------|------|
| `.button` (mobile PPC) | `_v5-page01-overrides.scss` |
| `.machine-showcase__specs dd` @760px | `_screen-02-prices.scss` |
| Footer nav/contacts/legal/requisites | `_landing-footer.scss` |

**Remaining `nowrap`:** `.machine-showcase__specs dd` at `min-width: 761px` only (desktop single-line spec values — intentional).

### Buttons / CTA wrapping

| File | Change |
|------|--------|
| `_button.scss` | Base: `min-width: 0`, `line-height: calc(1em + 4px)`; mobile: `white-space: normal`, `break-word`, `text-wrap: balance`; **420px** font step |
| `_v5-page01-overrides.scss` | PPC mobile `.button`: same wrap policy |

### FAQ text spacing

| File | Change |
|------|--------|
| `_screen-04-faq.scss` | Body: `line-height: calc(1em + 4px)` (was `1.35em` ratio); improved summary/body padding; **420px** band for tighter mobile spacing |

### Consent text wrapping

| File | Change |
|------|--------|
| `_forms.scss` | `.site-form__consent-text`: `overflow-wrap: break-word`; `line-height: calc(1em + 4px)`; **420px** band with reduced padding/font for long legal copy |

### Mobile 375–420px band

| Breakpoint | Coverage |
|------------|----------|
| **420px** | Section H2, hero H1, FAQ, buttons, consent |
| **375px** | Section H2 font clamp |
| **390px** | Hero H1 (existing, line-height aligned) |

---

## Build verification

```
npm run build  →  PASS (gulp build, styles compiled without errors)
```

---

## SAFE UNKNOWN

- Live browser QA at **375 / 390 / 420 / 768 / 1024 / 1180** — **not run** in this batch (CSS-only pass).
- Desktop spec `dd` nowrap at ≥761px — verify no horizontal clip at 1024–1180 with long values.
- `text-wrap: balance` on buttons — unsupported in older browsers; degrades to normal wrap.

---

## Recommended next step

Human browser check at 375–420px on `dist/index.html`, then Batch C (asset hygiene) per audit v1.

---

*Batch B — typography/mobile hardening. No HTML, backend, assets, or schema changes.*
