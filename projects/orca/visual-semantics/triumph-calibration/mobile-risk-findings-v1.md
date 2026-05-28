# Mobile Risk Findings v1

**Source:** `mobile-risk-observations-v1.md`  
**Status:** risk hypotheses — **no** agent browser QA in loop.

## Breakpoints

| Band | Effect |
|------|--------|
| Desktop | 2-col hero |
| ≤760px | stack content → form |
| ≤420px | type/button tuning |

## Top risks

| ID | Risk | `mobile_critical` |
|----|------|-------------------|
| M1 | Form below fold after 5 specs | `form_submit` |
| M2 | call-first instance vs form hero | `call` |
| M3 | 6 cargo tap crowding | — |
| M4 | consent link wrap | — |
| M5 | zakaz horizontal overflow | UNKNOWN |

## Mitigations (documented, not built)

- `mobile_hero_cta_order: [call, form]`
- sticky tel + form bar
- cargo cap 4 on mobile
- qualification above cargo

## QA checklist

See [mobile-criticality-rules-v0.md](../mobile-criticality-rules-v0.md).

## SAFE UNKNOWN

LCP, conversion, scroll depth — not measured.
