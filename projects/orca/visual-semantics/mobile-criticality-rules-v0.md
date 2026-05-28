# Mobile Criticality Rules v0

**Evidence:** `_v5-hero-extensions.scss` breakpoints (760px, 420px), `mobile-risk-observations-v1.md`.  
**No device QA in repo** — rules are implementation hints + operator checklist.

## `mobile_critical` field

Multi-select. Factory must ensure each selected item is reachable on **390px width** without «excessive» scroll.

| Value | Triumph zakaz status |
|-------|---------------------|
| `call` | **At risk** — instance call-first; form dominates hero stack |
| `form_submit` | Present after H1+lead+5 specs on ≤760px |
| `primary_cta` | Form button — OK if scroll acceptable |
| `qualification_line` | **FAIL** — removed from hero |
| `capability_scan` | 5 specs visible before form if stacked — **partial** |

## Breakpoint behavior (documented)

| Band | Behavior |
|------|----------|
| Desktop | 2-col: content | form |
| ≤760px | Stack: content then form; stronger overlay |
| ≤420px | Type/button tuning per Factory reports |

## Risk register (hypotheses)

| Risk | Mechanism | Severity |
|------|-----------|----------|
| Form below fold | Stack order | high |
| CTA collapse | Call link under consent | medium |
| Cargo 2×3 grid | Tap crowding | medium |
| Consent wrap | Long legal links | medium |
| Call ad → no early `tel:` | Header sticky — **verify** on device | medium |
| Horizontal overflow | Marked UNKNOWN for zakaz | UNKNOWN |
| LCP on 4G | Hero bg 2560×1440 | UNKNOWN |

## Mitigations (vNext — not implemented in v0 layer)

1. `mobile_hero_cta_order: [call, form]` when PPC call-first
2. Sticky bottom: Позвонить | Рассчитать
3. `cargo_cards_max: 4` on mobile
4. Qualification notice above cargo in `hero__lower`

## Operator QA checklist

- [ ] iPhone SE / 390px: primary CTA without excessive scroll
- [ ] Android Chrome: no horizontal overflow through FAQ
- [ ] Tap `tel:` from header and hero
- [ ] Form submit + consent error state
- [ ] Hero LCP on 4G — UNKNOWN

## Pack example

```yaml
mobile_critical: [call, form_submit, capability_scan]
mobile_hero_cta_order: [call, form]  # vNext field
cargo_cards_max_mobile: 4
```

## SAFE UNKNOWN

All conversion impact claims; «excessive scroll» not measured in px.
