# DISTINCT-EVENT-B-v1

**Fixture B:** `lead_synth_cleandup_b01` / `msg_synth_cleandup_b01` (distinct SOURCE_EVENT_ID from A)

| Check | Result |
|-------|--------|
| After B upsert | A count = 1, B count = 1 |
| Combined | 2 distinct events → 2 logical CLEAN leads |
| false_dedupe_events | **0** |

B was not suppressed by A's identity. Archived with A before closeout.
