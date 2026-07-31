# PARSER-VERSION-ALIGNMENT v1

**Phase:** 3D.2

## Code

| Check | Result |
|-------|--------|
| Live Parse Lead hash | `F1067600843486FD` (matches Phase 3D.1) |
| Code stamp | `sm-parser-v3.1` |
| Fixture suite | PASS |
| Normalize CONFIG default fallback | updated to `sm-parser-v3.1` |

## CONFIG sheet

| Field | Before | After |
|-------|--------|-------|
| `parser_version` | `sm-parser-v3` | `sm-parser-v3.1` |

`/config` harness reply shows: `Версия парсера: sm-parser-v3.1`

## Claim gate

Version 3.1 claimed only because live Parse Lead hash matches accepted 3D.1 parser, fixtures pass, and CONFIG display is aligned.
