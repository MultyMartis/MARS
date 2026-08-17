# RAW LEAD ACCESS REPAIR v1

**Phase:** 3H.9  
**Workflow:** Admin.dev `wLrLp4WQHm1VJmxz` (same ID; no new workflows)

## Proven defect

Same ADMIN_A identity:

| Alias | Exec | MSK | ACCESS/CONFIG | Auth result | Telegram |
|---|---|---|---|---|---|
| RAW_ACCESS_PASS_LEAD | 33304 | 2026-08-17 08:41 | reads OK | admin active authorized | raw viewed |
| RAW_ACCESS_DENIED_LEAD | 33500–33502 | 2026-08-17 14:26 | `invalid_grant` | `deny_reason=registry_unavailable` but Answer Callback Deny hardcoded permission text | operator saw permission deny |

Divergence: **Read ACCESS_CONTROL / Read Authorization Config failed** (Google Sheets OAuth grant invalid). Not per-card ownership. Not missing raw payload. Not an ACCESS_CONTROL role change.

## Patch

1. `Check User Authorization` emits `deny_reply` from `denyReply()`.
2. `Answer Callback Deny` uses `{{$json.deny_reply || $json.answer_text || "Недостаточно прав."}}`.
3. Unauthorized callback copy is `Недостаточно прав.` (charter).
4. Registry/credential failure copy remains service-unavailable.
5. Missing raw copy: `Исходная заявка для этого лида не найдена.`

Live Sheets OAuth reconnect is still required before a new ADMIN_A raw PASS can be proven after 14:26.

Patches: `implementation/patches/CheckUserAuthorization.phase3h9.js`, `HandleCallbackAction.phase3h9.js`, `DenyReply.phase3h9.js`.
