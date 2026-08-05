# APPROVED TEMPLATE RENDERER v1

**Lib:** `implementation/runtime-libs/approved-template-renderer-v1.mjs`  
**Assist version:** `iseo-manager-assist-v1.0`

## API

- `renderApprovedReply({ leadContext, route, recipientProfileRow, generationMode, aiFields })`
- `validateCustomerReply(text, ctx)`
- `buildDeterministicManagerGuidance(route, opts)`
- `buildSharedReplyMetadata(route, generationMode)`

## Generation modes

- `DETERMINISTIC_TEMPLATE` (default / AI OFF)
- `AI_ASSISTED_TEMPLATE` (constrained; not production-default)

## Render guarantees

- Customer copy starts with `Добрый день!`
- Exact intro sentence with approved first name + company
- Guidance never inside customer `<pre>`
- Nickname **Мопс** rejected in client copy
- Missing approved name → warning + no unsafe draft (delivery continues)
- Shared LEADS metadata keeps legacy `first_reply_version_legacy=sm-reply-v2.1` for rollback history only

## No auto-send

Renderer produces drafts only.
