# Visual semantics — Mobile criticality

## Field

`mobile_critical: [form_submit, capability_scan]`

## Critical paths

1. User sees **5 т / 3 т / 14 м** without horizontal scroll
2. User can **submit form** or **call** within acceptable thumb reach

## Risks (calibration)

| Risk | Severity |
|------|----------|
| Form after 5 specs on stack | **high** |
| call not in hero first tap | **medium** |
| 6 cargo buttons | **medium** |
| Notice below cargo — unread | **medium** |
| Horizontal overflow | **UNKNOWN** — QA |

## Rules reference

`projects/orca/visual-semantics/mobile-criticality-rules-v0.md`

## Pack recommendations (non-binding)

```yaml
cargo_cards_max_mobile: 4
mobile_hero_cta_order: [call, form_submit]  # pending operator
sticky_call_header: true  # verify in header partial
```

## QA matrix (operator)

- iPhone SE width
- Android 360px
- Desktop 1400px three-column transport (tasks section)
