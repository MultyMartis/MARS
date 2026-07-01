# Search PPC negative keyword standard v1

**Implementation:** `negative-keyword-policy.mjs`, `metadata-operation-model.mjs`

## Policy modes

| Mode | XLSX E9 | TXT import |
|------|---------|------------|
| `blank` (default Corvonero) | EXPLICIT_CLEAR | Separate per-campaign TXT |
| `set` | SET_VALUE | Optional supplement |
| `txt_separate` | Blank in XLSX | Required validated TXT |

## Metadata operations

- `MISSING` — property absent
- `PRESERVE` — keep template value (only when contract permits)
- `EXPLICIT_CLEAR` — force empty (blank string maps here, **not** PRESERVE)
- `SET_VALUE` — explicit negative string

## Syntax

- Quoted negatives (`"лицензия 1с"`) rejected — pseudo phrase-match
- Included-keyword conflict detection required

## Cross-campaign negatives

Disabled until explicitly approved per project.

## Post-launch

Search-query expansion negatives — operator judgement, separate from generation gate.
