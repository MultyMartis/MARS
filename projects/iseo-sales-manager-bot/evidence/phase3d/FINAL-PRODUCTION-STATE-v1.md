# FINAL-PRODUCTION-STATE-v1

**Phase:** 3D  
**Observed after idempotency patch + Admin acceptance + clean-lead wait window**

| Workflow | Active | Role |
|----------|--------|------|
| Sales-Manager-v2 | **false** | rollback source |
| i-SEO Sales Manager - Operational.dev | **true** | sole Gmail intake |
| i-SEO Sales Manager - Admin.dev | **true** | operator Admin |
| Sales-Manager-v1 | **false** | legacy inactive (pre-existing; not created this phase) |

| CONFIG | Value |
|--------|-------|
| environment | production (Admin `/config` working contour) |
| ai_enabled | false |
| health_ai_probe_enabled | false |

| Gate | Result |
|------|--------|
| Active Gmail intake count | **1** |
| New workflows this phase | **0** |
| Retry flood guard | **patched** |
| Clean valid-contact test lead | **pending operator** |
| Automatic client messages | **0** |
| AI provider calls | **0** |
| Rename .dev → production names | **deferred** |
| Registry status change | **not applied** (separate gate) |

## Naming decision

Defer rename of Operational.dev / Admin.dev until after clean-lead acceptance and operator confirmation that Trigger registration risk is acceptable. Sales-Manager-v2 name unchanged.
