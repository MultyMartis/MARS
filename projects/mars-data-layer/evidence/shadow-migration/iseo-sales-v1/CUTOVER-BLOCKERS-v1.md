# Cutover blockers — before `PG_CANDIDATE_VALIDATED` / SoT switch

Shadow migration can pass while these remain **required before cutover**:

1. **Candidate workflow not built** — Operational.v3.dev (or equivalent) must be designed/built in a later wave; not done here.
2. **Final delta at freeze** — prove incremental import after T0 against live Sheets drift.
3. **Unresolved delivery orphans** — 67 historical deliveries with null `lead_id`; decide archive vs repair mapping before cutover UX.
4. **1 malformed delivery unknown** — classify/drop permanently.
5. **DEDUP empty-key hygiene** — Sheets DEDUP still mostly empty keys; PG constraints + synth keys OK for shadow; product may still want Sheets hygiene fix.
6. **lead_id mint algorithm (Q1)** — freeze generator before Toolkit mint helper.
7. **Lifecycle vocabulary (Q4)** — soft product decision for Admin UX labels.
8. **Off-host backup gate** — confirm ops backup policy for `mars` beyond on-host `/root/mars-backups/postgres/`.
9. **Seed fixture cleanup** — 3 synthetic `sheets_quota_exceeded` rows remain (neutralized); optional purge under destructive charter.
10. **No production n8n PostgreSQL credential** until candidate wave explicitly binds it.
11. **ACCESS snapshot drift** — only 1 active admin at T0; confirm Olya/moderator live state at cutover freeze (Sheets remains truth until then).
12. **Outbox/history safety review** — second-pass that no historical `pending` can be resumed by candidate workers.

Non-blockers for **this** wave (`PG_SHADOW VALIDATED`):

- Shadow reconcile matrix PASS
- Idempotency PASS
- pending_deliveries = 0
- Live prove: 0 postgres credentials / 0 postgres nodes; Sheets workflows still active
