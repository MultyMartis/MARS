# FINAL WORKFLOW STATE v1 — Phase 3E.2.1

Observed after restore (sanitized):

| Contour | Active | Nodes | Notes |
|---------|--------|------:|-------|
| Operational.dev | **true** | 45 | sole Gmail intake; Schedule enabled; OpenRouter disabled |
| Admin.dev | **true** | 59 | unchanged callbacks / ACCESS_CONTROL |
| Sales-Manager-v2 | **false** | — | must stay inactive |

## Versions (intent)

- `parser_version=sm-parser-v3.3`
- `first_reply_version=sm-reply-v2.1`
- `human_reply_style_version=sm-human-v1.0`
- `message_format_version=sm-msg-v2.4`
- AI OFF

## Safety

- workflows created = 0
- access-role changes = 0
- AI provider calls = 0
- client auto-messages = 0
