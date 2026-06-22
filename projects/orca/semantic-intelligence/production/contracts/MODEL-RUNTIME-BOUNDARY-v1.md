# Model and Runtime Boundary v1

**Status:** `NOT VALIDATED` — live semantic model execution  
**Assessor default:** `deterministic-assessor.mjs` (regex/heuristic — fixture/diagnostic only)

## Provider

| Field | Value |
|-------|-------|
| Provider | **MISSING** — no executable LLM provider in repository |
| Model identifier | N/A |
| Structured output mode | Contract defined; not wired |
| Credentials | Not stored in Git |
| Live execution | `NOT VALIDATED` |

## Deterministic test mode

Production runner uses `assessors/deterministic-assessor.mjs` which wraps `pilot-assessor-v1.mjs`. Suitable for:

- Fixture tests
- Scale/reconciliation tests
- P0-I diagnostic comparison

**Not suitable for** production semantic accuracy claims.

## Future model integration (planned)

When authorized:

- Provider-neutral contract: `assessors/assessor-contract.mjs`
- Required: structured JSON output, rate limits, cost controls, retry policy, batching
- Privacy: no secrets in Git; operator-supplied credentials via environment
- Fallback: deterministic mode on provider failure (degraded, not silent ACCEPT)
- Logging: assessor version + model version on every record

## Honest maturity

```text
Wave 3 enforcement pipeline — IMPLEMENTED
Live semantic model — NOT VALIDATED
Production semantic intelligence operational — NOT CLAIMED
```
