# CURRENT-DELIVERY-STATE-MACHINE

```
UNSEEN event_id
  → Dedupe Classify FIRST_SEEN
  → Claim Insert: intake_state=FIRST_SEEN, delivery_state=PENDING, event_status=<normalized>
  → Respond Accepted HTTP 202
  → Telegram Notify Accepted (side effect)
  → END  (delivery_state remains PENDING even if Telegram succeeded)
```

Duplicate fingerprint → HTTP 200 DUPLICATE_SUPPRESSED → no Telegram.
Conflict → HTTP 409 → no Telegram.

**Observed gap (D5R2A):** Telegram `message_id=7` success; Data Table `delivery_state=PENDING`.

**Live Data Table nodes:** get + insert only.
