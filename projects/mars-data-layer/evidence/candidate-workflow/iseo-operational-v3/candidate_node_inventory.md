# Candidate node inventory — Operational.v3.dev

Workflow ID: `NH4uV145Amrgnmkm`  
Name: `i-SEO Sales Manager - Operational.v3.dev`  
Active: `false`  
Credential: `ISEO Runtime PG (v3)` / `XCmmOgzZ1RWT4Fg3` / role `iseo_runtime`

| Node | Type | Role |
|---|---|---|
| Manual Inject (fixtures only) | manualTrigger | No Gmail poller — inactive candidate safety |
| Normalize Fixture | Code | Map fixture → commit payload; `dry_run_telegram=true` |
| PG Commit (process_gmail_inbound_commit) | Postgres | Parameterized call to DB commit function |
| Gmail Finalize Gate (after PG) | Code | Allows finalize only if `gmail_finalize_allowed`; simulated while inactive |
| Claim Delivery Outbox | Postgres | `claim_pending_deliveries` |
| Telegram Dry-Run (NO SEND) | Code | Marks intent processed without Telegram API |
| Mark Delivery Result | Postgres | `mark_delivery_result` |

Notes:
- No Sheets nodes on critical path.
- No Telegram send nodes.
- No concurrent Gmail Trigger with production.
