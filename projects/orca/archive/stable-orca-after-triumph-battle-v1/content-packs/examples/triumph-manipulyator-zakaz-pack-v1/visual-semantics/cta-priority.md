# Visual semantics — CTA priority

## Field

`cta_priority: form`

## Weight model

| CTA | `cta_weight` | Notes |
|-----|--------------|-------|
| Form submit | primary_dominant | red button in aside |
| Tel (hero form) | secondary | outline |
| Header tel | secondary | sticky |
| Cargo modals | tertiary | noise risk if styled as primary |

## Ambiguous: call-first doctrine

- Blueprint: call-first mobile flow
- Instance A1: `primary_cta: call`
- As-built hero: form column dominant

**Resolution owner:** operator — not Factory-only.

## Visual rules

- One primary red CTA per viewport zone
- Cargo cards should use ghost/outline if they compete (calibration H2-6 recommendation)

## Mobile pack vNext

```yaml
mobile_critical_add: call
recommended_order: [call, form_submit]  # if operator confirms
```
