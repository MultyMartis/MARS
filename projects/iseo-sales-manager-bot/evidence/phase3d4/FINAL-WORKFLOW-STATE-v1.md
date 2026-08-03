# FINAL WORKFLOW STATE v1

**Phase:** 3D.4  
**Date:** 2026-08-03

---

## Workflow inventory

| Workflow | ID | Active | Nodes |
|----------|-----|--------|-------|
| Sales-Manager-v1 | cJGoQUqIIHull4p7 | false | — |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | **false** | — |
| Operational.dev | **xSnXPy8cEHoZw6xG** | **true** | 36 |
| Admin.dev | **wLrLp4WQHm1VJmxz** | **true** | 42 |

---

## Runtime CONFIG (safe summary)

| Key | Value |
|-----|-------|
| `environment` | production |
| `ai_enabled` | **false** |
| `parser_version` | **sm-parser-v3.2** |
| `message_format_version` | **sm-msg-v2.1** |
| `admin_user_ids` count | **1** |
| `manager_action_user_ids` count | **2** |
| Active Gmail intake workflows | **1** (Operational.dev only) |

---

## Contour notes

- Admin Telegram Trigger: `message` + `callback_query`.
- Role-aware `/start` / `/help` routed in Admin.dev (manager vs admin paths).
- No third workflow; Sales-Manager-v2 remains inactive rollback source.
- AI OFF — zero OpenRouter execution in production path.

---

*Related: evidence/phase3d3/FINAL-WORKFLOW-STATE-v1.md (prior baseline).*
