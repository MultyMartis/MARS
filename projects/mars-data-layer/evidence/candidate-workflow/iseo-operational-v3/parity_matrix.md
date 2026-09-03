# Functional parity matrix — Operational.dev → Operational.v3.dev

Baseline production: `Operational.dev` (`xSnXPy8cEHoZw6xG`, ACTIVE, Sheets SoT).  
Candidate: `Operational.v3.dev` (`NH4uV145Amrgnmkm`, INACTIVE, PG runtime).

| Current function | Operational.dev | v3 PG implementation | Equivalent? |
|---|---|---|---|
| Gmail intake (live poller) | Gmail Trigger / poll → process | **Not wired** in candidate (Manual Inject only) — by design while INACTIVE | Parity deferred to cutover (single poller rule) |
| Filtering / spam heuristics | Sheets + Code nodes | Fixture/normalize + `manager_status` / `change_lead_status` | YES (status path); filter rules remain in Code layer at cutover |
| Lead parsing/normalization | Code + Sheets CLEAN write | Normalize Fixture → `process_gmail_inbound_commit` / `upsert_lead` | YES |
| Dedupe | DEDUP_INDEX Sheet | Unique `(source_system, source_id)` + delivery idempotency keys | YES (stronger) |
| RAW lifecycle | RAW Sheet rows | `inbound_events` | YES |
| CLEAN lifecycle | CLEAN Sheet rows | `leads` | YES |
| CONFIG behavior | CONFIG Sheet poll | `get_active_config` (non-secretish keys); secrets stay in n8n/env | YES (secrets not migrated) |
| Access decisions | ACCESS Sheet / shared state | Read `access_rules` / `list_delivery_recipients` (no ACCESS redesign) | YES (read-only use) |
| Telegram delivery prep | Direct Telegram send path | Outbox `deliveries` → claim → dry-run mark (NO SEND) | YES (durable); live send deferred |
| Gmail labels/state | Label after Sheets write | Finalize gate **after** PG commit; simulated while inactive | YES (ordering); live labels at cutover |
| Error handling | ERRORS Sheet | `errors` + `record_error` | YES |
| Processed commit point | Sheets write then Gmail | Atomic `process_gmail_inbound_commit` then Gmail finalize | YES (improved) |
| Retries / defer | Sheets Quota Defer Gate / loops | `jobs` + `enqueue_job` / bounded `available_at` | YES (no Sheets 429 core) |
| Exactly-once | n8n + Sheet keys | DB uniqueness + commit short-circuit + outbox idempotency | YES |
| Sheets quota defer | Wave-5 gate on critical path | **Removed** from v3 architecture | N/A (intentionally not ported) |
