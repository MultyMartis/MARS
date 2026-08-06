# Pre-Create Gates — Client Ops Bridge

Deterministic gates before inactive sandbox create.

| Gate | Rule | Local template result |
|------|------|------------------------|
| Workflow name | Exactly `MARS Client Ops Bridge — bzpm.ru` | PASS |
| Graph node count | 8–12 | PASS (9) |
| Allowed node types | webhook, code, if, respondToWebhook only | PASS |
| Exact typeVersions | webhook 2.1, code 2, if 2.3, respondToWebhook 1.1 | PASS |
| No Telegram | Forbidden | PASS |
| No HTTP Request | Forbidden unless later justified | PASS |
| No external business nodes | Forbidden | PASS |
| No credential values | Forbidden | PASS |
| No secret patterns | Forbidden (placeholder marker allowed) | PASS |
| No webhookId | Omit | PASS |
| Inactive | `active=false` | PASS |
| responseMode | `responseNode` | PASS |
| Terminal branches | Both reach Respond to Webhook | PASS |
| No dangling connections | All sources/targets exist | PASS |
| No duplicate node names | Unique | PASS |
| Auth placeholder | Present until HITL bind; blocked-inactive apply allowed under Phase 1B-B | PASS (present) / blocked-inactive create authorized |
| Fixture harness | PASS | PASS (28/28) |
| Baseline Git commit | Client Ops baseline present | Operator attest |
| Locus clean / narrowly understood | Foreign WIP excluded | Operator attest |
| Rollback plan present | Runbook exists | PASS |
| Operator HITL | Required for apply | Phase 1B-B charter + confirmation phrase |

**Apply readiness:** Phase 1B-D3 controlled synthetic producer HTTPS proven; workflow inactive (executions=31; Data Table rows=2); generic live mode BLOCKED; D3 charter CONSUMED. Next: D4 real-source adapter design / manual dry-run. Concurrent producers / scheduler / production activation remain blocked. Never schedule Client Ops jobs from dirty `X:\AI MARS`.
