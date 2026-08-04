# WEBSITE STATE MODEL v1 — Phase 3E.1 evidence

**Architecture:** research → [SITE-FIELD-STATE-MODEL-v1.md](../../research/parser-3.3/SITE-FIELD-STATE-MODEL-v1.md) (**implemented**)  
**Harness:** H07–H11, P33-04, H21

| State | Rule | Card behavior |
|-------|------|---------------|
| `provided` | valid domain/URL | show normalized site; reply may omit site ask |
| `explicitly_absent` | explicit no-site / need-site phrases | do not show fake URL; reply must not ask for existing site when building |
| `alternative_contact` | t.me / @handle / messenger in site slot | contact channel only; **not** under Сайт |
| `invalid_or_placeholder` | `n/a`, `-`, `#ERROR!`, junk | treat as unusable |
| `missing` | no value and no explicit absence | missing-info rules apply |

States are separate from raw `site_value`. Messenger must never render as website.
