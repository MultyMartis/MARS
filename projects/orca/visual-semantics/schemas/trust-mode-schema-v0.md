# Trust Mode Schema v0

## `trust_mode`

| Value | Allowed hero proof |
|-------|-------------------|
| `social_proof` | Star line + review sources (exact copy from pack) |
| `operational_proof` | 2–4 ops facts, no invented SLA |
| `hybrid_proof` | Max 3 items: 1 social + 2 ops recommended |

## `proof_priority`

| Value | Placement |
|-------|-----------|
| `hero_strip` | `hero-proof--v5` |
| `below_fold` | Trust section only |
| `deferred_reviews_only` | No hero strip — rare |

## `proof_visibility`

| Value | Visual treatment |
|-------|------------------|
| `prominent` | Full strip, icon+label |
| `subtle` | Smaller type, 2 items max |
| `hidden_hero` | Social deferred |

## Required companion

```yaml
trust_reviews_section_required: true  # boolean — always true for Triumph
```

## Triumph as-built

```yaml
trust_mode: operational_proof
proof_priority: hero_strip
proof_visibility: prominent
```

Blueprint expected:

```yaml
trust_mode: social_proof  # drift → ambiguous unless operator accepts ops-only
```
