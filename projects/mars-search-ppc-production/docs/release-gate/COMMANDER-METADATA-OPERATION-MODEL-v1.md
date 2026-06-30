# Commander Metadata Operation Model v1

**Status:** IMPLEMENTED  
**Module:** `tools/commander-transport/src/metadata-operation-model.mjs`

## Four explicit semantics

| State | Meaning | Transport behavior |
|-------|---------|-------------------|
| `MISSING` | Property absent from payload | Documented default (not infer from truthiness) |
| `PRESERVE` | Keep template value | Omit from patch map |
| `EXPLICIT_CLEAR` | Force blank | Omit from patch + explicit cell clear |
| `SET_VALUE` | Set supplied value | Include in patch map |

## Typed declaration

```json
{ "operation": "set", "value": "..." }
{ "operation": "clear" }
{ "operation": "preserve" }
```

## Prohibited pattern

```javascript
if (value !== '') out[key] = value;  // FORBIDDEN — erases clear vs preserve
```

## Legacy compatibility

Empty string in Russian-key patches maps to `EXPLICIT_CLEAR`, not skip.

## Fields covered

campaign_negatives, organization, campaign_type, promotion_url, currency, optimize_text.
