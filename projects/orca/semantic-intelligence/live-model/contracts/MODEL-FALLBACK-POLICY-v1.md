# Model Fallback Policy v1

**Status:** `IMPLEMENTED — Wave 3.1`

## When live model unavailable

### Allowed

- Resume later (idempotent phrase IDs + checkpoint)
- Retry within cap (max 3, exponential backoff)
- Alternate approved model (operator-configured)
- Mark run `BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE`
- Diagnostic deterministic preview (clearly labeled, not production authority)

### Forbidden

- Silently promote deterministic preview to production authority
- Skip model and declare production semantic complete
- Send full corpus to operator for manual classification

## Required blocker

```text
BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE
```

## Implementation

`controls/cost-rate-controls.mjs` — `assertModelAvailable()`  
`adapters/model-adapter-interface.mjs` — `BLOCKER_MODEL_UNAVAILABLE`
