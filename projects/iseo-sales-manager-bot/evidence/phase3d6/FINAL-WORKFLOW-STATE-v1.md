# FINAL WORKFLOW STATE v1

| Workflow | State | Nodes | Role |
|---|---|---:|---|
| Sales-Manager-v2 (`h8I2Tl2yl4uzhUnB`) | inactive | — | preserved rollback source |
| Operational.dev (`xSnXPy8cEHoZw6xG`) | active | 36 | sole Gmail intake |
| Admin.dev (`wLrLp4WQHm1VJmxz`) | active | 54 | Telegram access, `/my_status`, role notifications |

Runtime configuration: `environment=production`, `ai_enabled=false`, `parser_version=sm-parser-v3.2`, `message_format_version=sm-msg-v2.2`.

Hotfix marker: `3d6b-my-status-code-mode`.

Code-node modes (accepted live):

| Node | Mode |
|---|---|
| My Status | `runOnceForAllItems` |
| Finalize Access Notification | `runOnceForAllItems` |

Restore Admin Reply Target: hardened Prepare lookup present.

No OpenRouter AI call is enabled on Operational. Workflows created: 0. Client auto-messages: 0. Admin.dev node count remains **54** after the mode hotfix (connections unchanged).
