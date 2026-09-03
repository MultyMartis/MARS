# Cutover plan — DESIGN ONLY (do not execute)

1. Accept Operational.v3.dev candidate (this wave gate)
2. Freeze/fence old Sheets writer paths for Operational family
3. Final Sheets→PG delta import
4. Reconcile counts / idempotency keys / open deliveries
5. Switch authoritative SoT declaration to PostgreSQL (`app_iseo_sales`)
6. Deactivate `Operational.dev` (`xSnXPy8cEHoZw6xG`)
7. Activate `Operational.v3.dev` (`NH4uV145Amrgnmkm`) with live Gmail Trigger (single poller)
8. Confirm concurrent Gmail intake = 1 (v3 only)
9. Observe one natural lead end-to-end (inbound→lead→outbox→Telegram)
10. Hold rollback gate open for controlled window

**This wave executed none of the above.**
