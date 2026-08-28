# OLYA-PRE-MAINTENANCE-BASELINE-v1

**Scope:** MOD_B actor events (sanitized, no PII).

**Note:** Dedicated pre-revoke snapshot was overwritten by post-restore run @ 2026-08-28T11:40:02Z. Initial ACCESS and post-restore baseline below establish production continuity.

**Post-restore baseline (integrity anchor):**

- lead_count: **14**
- status_counts: pending **1**, spam **13**
- mod_b_access: **active** (E67145502141)

Lead hashes only (authoritative status @ capture):

| lead_hash12 | status | latest_action |
|---|---|---|
| bd9c7ee3f398 | pending | queue_opened |
| 41a8f2a23eaf | spam | applied |
| ca1ac8b0f87c | spam | applied |
| (+ 11 more spam, see forensic JSON) |

**Olya real leads baseline (post-restore):** 14

**Do not use** lead `bd9c7ee3f398` for synthetic status-transition tests.
