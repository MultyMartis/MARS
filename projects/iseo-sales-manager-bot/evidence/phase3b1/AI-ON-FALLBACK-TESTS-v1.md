# AI ON FALLBACK TESTS v1

CONFIG remained `ai_enabled=false` as normal state. AI ON validated via **mocked** Validate/Merge nodes only (no provider-backed OpenRouter calls).

| Fixture | Result | Notes |
|---------|--------|-------|
| AI_VALID_JSON | **PASS** | {"ai_valid":true,"reason":"","mode":"ai_on","fallback":false,"ai_status":"success"} |
| AI_INVALID_JSON | **PASS** | {"ai_valid":false,"reason":"invalid_json","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |
| AI_EMPTY | **PASS** | {"ai_valid":false,"reason":"invalid_json","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |
| AI_BAD_SERVICE | **PASS** | {"ai_valid":false,"reason":"bad_service","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |
| AI_UNSAFE_PRICE | **PASS** | {"ai_valid":false,"reason":"unsafe_promise","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |
| AI_DEADLINE | **GAP** | {"ai_valid":true,"reason":"","mode":"ai_on","fallback":false,"ai_status":"success"} |
| AI_GUARANTEE | **PASS** | {"ai_valid":false,"reason":"unsafe_promise","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |
| AI_FABRICATED | **PASS** | {"ai_valid":true,"reason":"","mode":"ai_on","fallback":false,"ai_status":"success"} |
| AI_TIMEOUT_SIM | **PASS** | {"ai_valid":false,"reason":"invalid_json","mode":"ai_fallback","fallback":true,"ai_status":"fallback"} |

## Gaps

- `AI_DEADLINE`: detector currently accepts deadline phrasing — recorded as **GAP** (tighten unsafe detector before production AI ON).
- Fabricated-client-fact detection remains soft (accepts fallback or ai_on).

## Final CONFIG

`ai_enabled=false` confirmed after tests.
