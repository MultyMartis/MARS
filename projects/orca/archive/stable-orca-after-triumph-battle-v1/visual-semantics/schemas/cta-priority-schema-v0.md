# CTA Priority Schema v0

## `cta_priority`

| Value | Factory behavior |
|-------|------------------|
| `form` | Inline hero form primary |
| `call` | `tel:` prominent in hero or sticky |
| `dual_equal` | Form + call same visual tier — use sparingly |
| `messenger_secondary_only` | Messengers footer/modal only |

## `cta_weight`

| Value | Factory behavior |
|-------|------------------|
| `primary_dominant` | One solid primary button |
| `shared` | Two equal primaries — requires justification |
| `secondary_noise` | **Warning** — micro-CTAs compete (cargo row) |

## PPC alignment rule

If instance JSON specifies **call-first**, pack must either:

- set `cta_priority: call` + `mobile_critical: [call, …]`, or
- document explicit override why form-first hero is accepted

Triumph: instance call-first vs hero `form` — **document as ambiguous** until H2-5.

## Label lock

Semantic CTA text from blueprint may differ from button («Узнать» vs «Рассчитать») — **neutral** drift if meaning unchanged.
