# Approvals — triumph-manipulyator-zakaz-pack-v1

Human authority only. AI authoring does not constitute approval.

## Approval gates (default)

```yaml
approved_for_factory: false
approved_for_client_export: false
approved_for_ads: false
approved_for_launch: false
```

## Sign-off checklist

| # | Question | Sign-off |
|---|----------|----------|
| 1 | H1 strategy covers primary ad variant(s)? | ☐ |
| 2 | Machine specs match all active ads (5 т / 3 т / 14 м)? | ☐ |
| 3 | No fleet / fake pricing claims in pack or implementation? | ☐ |
| 4 | Qualification line acceptable in hero + tasks? | ☐ |
| 5 | Visual semantics bundle accepted for Factory? | ☐ |
| 6 | Productive drift list accepted; destructive list empty or mitigated? | ☐ |
| 7 | `intent_continuity_ack` set true in PPC instance when ready? | ☐ |

## Roles

| Role | Responsibility |
|------|----------------|
| Operator | Final copy, gates, launch |
| ORCA maintainer | Pack + PPC instance alignment |
| Factory implementer | Presentation only under MODE 1 |

## Approval log

| Date | Gate | Approver | Notes |
|------|------|----------|-------|
| — | — | — | No human sign-off recorded |

## Explicit non-approvals

- Pack does **not** approve live POST endpoint for forms
- Pack does **not** approve «От 30 минут» SLA as factual claim
- Pack does **not** approve conversion rates or A/B outcomes
