# FINAL WORKFLOW STATE v1

| Workflow | State | Nodes | Role |
|---|---|---:|---|
| Sales-Manager-v2 | inactive | — | preserved rollback source |
| Operational.dev | active | 36 | sole Gmail intake |
| Admin.dev | active | 54 | Telegram access, `/my_status`, role notifications |

Runtime configuration: `environment=production`, `ai_enabled=false`, `parser_version=sm-parser-v3.2`, `message_format_version=sm-msg-v2.2`.

No OpenRouter AI call is enabled on Operational. Workflows created: 0. Client auto-messages: 0. Admin.dev node delta is `51 → 54`, limited to `My Status`, `Finalize Access Notification`, and `Append ACCESS_EVENTS Notify`.
