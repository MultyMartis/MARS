# Mobile Risk Observations v1

**Evidence:** SCSS breakpoints in `_v5-hero-extensions.scss` (760px, 420px bands in hardening reports); **no** agent browser QA.

## Breakpoint model

| Band | Behavior (from SCSS / reports) |
|------|--------------------------------|
| Desktop | Hero 2-column; form right |
| ≤760px | Stronger overlay; title span inline; grid stacks |
| ≤420px | H1 / H2 / button tuning per batch-b report |

## Risks (human reasoning)

| Risk | Mechanism | Severity |
|------|-----------|----------|
| **Form below fold** | Stack: H1 → lead → 5 specs → then form | high |
| **CTA collapse** | Call link below consent checkbox | medium |
| **Cargo grid wrap** | 6 cards → 2×3 or scroll | medium |
| **Consent text wrap** | Long legal links in hero form | medium |
| **Tap target crowding** | Cargo buttons adjacent | medium |
| **CLS** | Hero img — mitigated if 2560×1440 set | low (if built dist current) |
| **Fonts offline** | Google Fonts CDN | medium for file:// QA |
| **Horizontal overflow** | QA on 5-ton marked UNKNOWN | UNKNOWN for zakaz |

## Call-first mobile flow (PPC instance)

Instance: `call-first` + phrase «Заказать по телефону».

**As-built:** sticky header phone — **verify** in `header-v5-page01.html` on real device.

**Risk:** User from call ad does not see prominent `tel:` until scroll if form dominates.

## Mitigations (for vNext — not implemented here)

1. `mobile_hero_cta_order`: call → form
2. Sticky bottom bar: Позвонить | Рассчитать
3. Reduce cargo to 4 on mobile
4. Move qualification notice above cargo

## QA checklist (operator)

- [ ] iPhone SE / 390px: primary CTA without excessive scroll
- [ ] Android Chrome: no horizontal overflow through FAQ
- [ ] Tap `tel:` from header and hero
- [ ] Form submit + consent error state
- [ ] Hero bg LCP acceptable on 4G — **UNKNOWN**

## Status

All mobile conversion claims in this file are **risk hypotheses**, not measured friction.
