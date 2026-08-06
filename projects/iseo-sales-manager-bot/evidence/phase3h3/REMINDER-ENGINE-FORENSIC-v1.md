# Reminder engine forensic

- Placement: Admin.dev internal 15-minute Schedule Trigger (not a new workflow)
- Source after Phase 3H.3 patch: **LEADS** (was lead_clean_v2 — corrected)
- Pending definition: manager_status/lifecycle_status pending
- min count: 1
- schedule display time: 10:00 Europe/Moscow
- active recipients only; revoked excluded
- tests excluded via CONFIG `pending_reminder_include_tests=false`
- claim ledger: REMINDER_DELIVERIES (headers repaired to contract)
- once per business date via window key + CONFIG last window stamps
