# TEST FIXTURE CLEANUP v1

Phase 3H.1 cleared TEST_LEADS data rows and repaired corrupted reminder/recipient-reply schemas.
Do not delete historical production LEADS/reporting rows.
Synthetic legacy lead_clean_v2 rows may remain but must not drive reminders or /stats.
