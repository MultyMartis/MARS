# FINAL-PRODUCTION-STATE-v1

**Phase:** 3D.1  
**Observed after live patch + Admin regression + observe window**

| Workflow | Active | Role |
|----------|--------|------|
| Sales-Manager-v2 | **false** | rollback source |
| i-SEO Sales Manager - Operational.dev | **true** | sole production Gmail intake |
| i-SEO Sales Manager - Admin.dev | **true** | admin commands |
| Sales-Manager-v1 | false | legacy inactive |

| CONFIG | Value |
|--------|-------|
| environment | production |
| ai_enabled | false |
| health_ai_probe_enabled | false (probe skipped) |

| Gate | Result |
|------|--------|
| Active Gmail intake count | **1** |
| Operational node count | **34** |
| Parser | `sm-parser-v3.1` live on Parse Lead |
| Exactly-once guard | preserved |
| New workflows created | **0** |
| AI provider calls (observe) | **0** |
| Automatic client messages | **0** |
| Clean lead accepted | **pending** |
| Rollback performed | **no** (patch retained) |
