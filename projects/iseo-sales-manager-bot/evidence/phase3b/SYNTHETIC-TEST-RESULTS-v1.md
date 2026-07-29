# SYNTHETIC TEST RESULTS v1

Local MetaBOT-style harness over Operational.dev Code nodes (no live Gmail/Telegram/OpenRouter provider calls).

| Fixture | Mode | Expected | Actual | Result |
|---------|------|----------|--------|--------|
| STRUCT | structure | G1-G11 structural | {"nodeCount":29,"edgeCount":30,"aiFalse":["Merge AI or Fallback"],"tgFail":["Error Handler"]} | PASS |
| F05 AI OFF | AI OFF | deterministic template, no OpenRouter | {"service":"Audit","quality":"poor","mode":"ai_off","ai_status":"skipped","duplicate":"new","replySource":"template","hasSeparators":true} | PASS |
| F06 AI OFF | AI OFF | deterministic template, no OpenRouter | {"service":"SEO","quality":"ok","mode":"ai_off","ai_status":"skipped","duplicate":"new","replySource":"template","hasSeparators":true} | PASS |
| F01 AI OFF | AI OFF | deterministic template, no OpenRouter | {"service":"Other","quality":"poor","mode":"ai_off","ai_status":"skipped","duplicate":"new","replySource":"template","hasSeparators":true} | PASS |
| DEDUP F12 reprocessed | dedupe | reprocessed/same_message | {"duplicate_status":"reprocessed","duplicate_match_type":"same_message"} | PASS |
| DEDUP F13 repeat phone | dedupe | repeat/phone | {"duplicate_status":"repeat","duplicate_match_type":"phone"} | PASS |
| DEDUP F14 possible site | dedupe | possible/site_only | {"duplicate_status":"possible","duplicate_match_type":"site_only"} | PASS |
| DEDUP invalid keys 44 and #ERROR! | dedupe | reject 44 and #ERROR! | {"rejected":["44","#ERROR!","44","#ERROR!"]} | PASS |
| AI ON invalid JSON fallback | AI ON mocked | invalid JSON -> fallback | {"ai_valid":false,"mode":"ai_fallback","fallback":true} | PASS |
| AI ON unsafe promise fallback | AI ON mocked | unsafe promise -> fallback | {"reason":"unsafe_promise","mode":"ai_fallback"} | PASS |
| Telegram special chars | telegram | escaped special chars, no raw enums | {"hasEscapes":true,"hasSep":true} | PASS |

**Pass:** 11 / **Fail:** 0

Telegram delivery to production manager chat: **not performed**. Destination policy: PENDING operator sandbox chat. Formatter validated locally.

Gmail label mutations on real messages: **not performed** (graph-only).
