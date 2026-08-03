# COMMAND CONTEXT PRESERVATION v1

## Hazard

Sheets lookup items must never replace Telegram trigger context (`chat_id`, `user_id`, `message_id`, `text`, `command`).

## Repair pattern (Phase 3D.5.2)

1. `Normalize Command` extracts chat/sender/message/text/update fields once.
2. `Read Authorization Config` may fan out rows.
3. **`Collapse Authorization Context`** re-attaches `$('Normalize Command').first().json` and emits **exactly one** item with `config_map` + preserved `chat_id` / `user_id` / `command`.
4. `Read ACCESS_CONTROL` runs once.
5. `Check User Authorization` reads command context from Normalize (not from Sheets cells) and returns one auth item including `chat_id`.
6. `Safe Telegram Reply` chat target prefers `$json.chat_id` / callback chat / Normalize fallback — never a Sheets row id.

## Guarantees

| Condition | Output items from auth stage |
|---|---|
| Registry row found | 1 (`registry_found=true`) |
| Registry empty | 1 (`registry_found=false`) |
| Registry technical failure | 1 (`registry_read_ok=false`) |
| CONFIG technical failure | 1 + deny/service path |
| Public / blocked / revoked | 1 explicit decision |
