# Search PPC ad copy standard v1

**Implementation:** `ad-copy-validator.mjs`

## Requirements

- Headline reflects group intent (WARNING if weak token overlap)
- LOCAL proposition includes Novosibirsk/visit framing (OPERATOR_REVIEW)
- REMOTE must not promise local visit without remote framing (HARD_FAIL)
- Unsupported claims flagged (OPERATOR_REVIEW)
- Character limits: headline ≤56, text ≤81
- Landing URL aligned with group plan
- Display path aligned with authority (`validateAuthorityArtifactEquality`)

## Mode rules

| Mode | Proposition |
|------|-------------|
| LOCAL | Novosibirsk / выезд |
| REMOTE | Удалённая работа по России; no false local visit |

## Generic copy

Forbidden template: «Услуги 1С для бизнеса: настройка, доработки и поддержка.» — detect via `detectGenericAdReuse`.
