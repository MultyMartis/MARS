# REMINDER PARTIAL FAILURE — Phase 3H.6

Harness/dry-run against live Reminder Build Claims model:

- Independent claim per recipient
- Failed recipient does not invalidate successful claims
- Retry limited to unclaimed/failed keys only
- Bounded by window + ledger status
- Next-day window independent
- Once-per-date protection retained

Live failure injection not performed (unsafe on production contour).
