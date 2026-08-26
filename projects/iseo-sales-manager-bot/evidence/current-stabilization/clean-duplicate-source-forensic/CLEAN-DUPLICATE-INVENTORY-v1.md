# CLEAN-DUPLICATE-INVENTORY-v1

**Captured:** 2026-08-26 (Admin reminder exec `40846` CLEAN read, 155 rows; sanitized analysis private/dup-analysis-40846.json)  
**Mutation:** none (Phase A read-only)

## Summary counters

| Metric | Value |
|--------|------:|
| CLEAN rows | 155 |
| unique `lead_id` | 112 |
| duplicate `lead_id` clusters | 3 |
| extra rows vs unique lead_id | 43 |
| PRODUCTION_REAL_DUPLICATE clusters | 2 |
| SAFE_UNKNOWN_DUPLICATE clusters | 0 |
| PROVEN_TEST_RESIDUAL clusters | 1 |

## Clusters

| Cluster (logical id) | Stable/logical identity | CLEAN rows | RAW rows | Source Gmail ids (sanitized) | First/last timestamp | Current status | Classification |
|---|---|---:|---:|---|---|---|---|
| `lead_synth_p3b1_c01` | lead_id = synth fixture family; 1 source_message_id | 24 | SAFE_UNKNOWN (not fully traced this wave) | `msg_synth_C01_*` (1 unique sid) | 2026-07-30 08:51:14 / same | new | PROVEN_TEST_RESIDUAL |
| `lead_19fcce0e42028e45` | lead_id == lead_ + gmail_message_id; 1 SOURCE_EVENT_ID | 16 | SAFE_UNKNOWN (not required for source proof) | `19fcce0e42028e45` (1) | 2026-08-04 13:05:36 → 13:13:12 (~30s cadence) | pending (mixed rows in cluster snapshot) | PRODUCTION_REAL_DUPLICATE |
| `lead_19fb7df740e51e26` | same pattern; 1 SOURCE_EVENT_ID | 6 | SAFE_UNKNOWN | `19fb7df740e51e26` (1) | timestamps sparse in snapshot | new | PRODUCTION_REAL_DUPLICATE |

## Notes

- Clustering key = exact `lead_id` (not display name).
- Both production-real clusters show **one** `source_message_id` / Gmail id for many CLEAN rows → same SOURCE_EVENT_ID re-appended, not two distinct Gmail events.
- SAFE_UNKNOWN_DUPLICATE by lead_id: **0** in this inventory.
- Historical rows **not** deleted in this phase.
