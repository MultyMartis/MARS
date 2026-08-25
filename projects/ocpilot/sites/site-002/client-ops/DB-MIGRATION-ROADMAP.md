# SITE-002 — Data Table → PostgreSQL Migration Roadmap (Future)

**Do not execute migration in this phase.**

## Phases (suggested)

0. Freeze current Data Table semantics in contracts (done in this pack).
1. Design schema + tenancy + constraints.
2. Dual-write shadow (optional) behind feature flag.
3. Read-path verification vs Data Table.
4. Cutover delivery authority with kill switch / rollback.
5. Retention + archive of Data Table rows.
6. Multi-site expansion only after SITE-002 stable.

## No big-bang

Keep n8n as orchestration adapter initially; move **state authority** first if needed.

## Acceptance before cutover

- Parallel proof window
- Replay/dedupe parity
- Kill switch parity
- Recovery drill
- Operator acceptance
