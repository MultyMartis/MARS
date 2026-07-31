# FINAL-WORKFLOW-STATE v1

**Phase:** 3D.2  
**Host:** n8n.ai-metacode.com

| Workflow | Active | Role |
|----------|--------|------|
| Sales-Manager-v2 | **false** | rollback source |
| i-SEO Sales Manager - Operational.dev | **true** | sole Gmail intake (34 nodes) |
| i-SEO Sales Manager - Admin.dev | **true** | Telegram Admin (28 nodes after `/start`) |

Also present inactive: Sales-Manager-v1 (historical; not part of production gate trio).

## Gates

- Active Gmail intake count: **1**
- `environment=production`
- `ai_enabled=false`
- `parser_version=sm-parser-v3.1` (CONFIG + code)
- Telegram Trigger enabled
- OpenRouter node remains disabled
- New workflows created this phase: **0**
- Rollback performed: **no**
- Optional rename Operational.dev / Admin.dev → deferred
