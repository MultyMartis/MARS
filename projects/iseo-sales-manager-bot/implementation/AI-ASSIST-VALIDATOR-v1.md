# AI ASSIST VALIDATOR v1

**Lib:** `implementation/runtime-libs/ai-assist-validator-v1.mjs`  
**Schema:** `iseo-ai-assist-schema-v1.0`

## Functions

- `buildAiAssistSystemPrompt({ templateId })` — locks template; forbids CTA/name/company rewrite
- `buildAiAssistUserPayload(leadContext, route)` — sanitized excerpt (emails/phones redacted)
- `validateAiAssistOutput(raw, ctx)`
- `applyAiAssistOrFallback(rawAi, ctx)`
- `resolveGenerationMode(config)` — default `DETERMINISTIC_TEMPLATE`

## Reject reasons (examples)

`invalid_json`, `guarantee_language`, `price_language`, `deadline_language`, `unsupported_site_review_claim`, `sender_name_changed`, `company_changed`, `full_client_message_forbidden`, `injection_artifact`

## Production

AI OFF restored/default. Validator exists for future constrained assist; not globally enabled.
