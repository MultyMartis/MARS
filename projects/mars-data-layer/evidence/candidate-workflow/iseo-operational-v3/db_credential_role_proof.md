# DB credential / role proof (sanitized)

| Field | Value |
|---|---|
| Credential name | `ISEO Runtime PG (v3)` |
| Credential ID | `XCmmOgzZ1RWT4Fg3` |
| DB role | `iseo_runtime` |
| Host/service | `mars-postgres` |
| Port | `5432` |
| Database | `mars` |
| Schema | `app_iseo_sales` |
| TLS | disable |
| Superuser used for app runtime | NO |
| `mars_admin` / `mars_migrator` used by candidate | NO |
| Password in Git / report / chat | NO |
| Secret contour | local approved path under `X:\AI MARS\local\infrastructure\VEESP-N8N-01\postgres\` (file present; not committed) |
| Production Operational.dev uses this credential | NO |
| Login enabled for `iseo_runtime` | YES (required for n8n PG credential) |
| encryptionKey rotation | NOT performed |
| Security residual | `SECURITY REMEDIATION DEFERRED TO SEPARATE SERVER OPS WAVE` |

Evidence refs: `orchestrator_result.json`, `active_state_proof.json`, `migration_apply_stdout.txt`.
