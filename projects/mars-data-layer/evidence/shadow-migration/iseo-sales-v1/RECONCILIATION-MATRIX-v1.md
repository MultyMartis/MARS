# ISEO Sales Shadow — Reconciliation Matrix v1

**Snapshot cutoff (apply T0):** `2026-09-03T09:11:28Z` (`20260903T091128Z`)  
**Authority:** Google Sheets authoritative · PostgreSQL = `PG_SHADOW`  
**Semantic note:** Sheets row counts are append-history; PG stores collapsed current identities.

| Domain | Sheets authoritative (semantic) | PG shadow count | Exact matches | Transformed | Excluded | Unknown | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| inbound / RAW (`gmail_message_id`) | 59 unique non-synth | 59 | 59 | collapse ~17.5k→59 | 78 synth | 0 | PASS |
| leads / CLEAN (`lead_id` latest) | 65 unique non-synth | 65 | 65 | collapse ~7.9k→65 | 93 synth + archives | 0 | PASS |
| DEDUP → `lead_dedup_keys` | 7927 sheet rows (mostly empty key) | 129 | 129 synth/composable | compose from gmail + lead fields | 78 synth; ~7.8k empty | 0 | PASS (constraint reconciliation) |
| lead_events | 126 migrated sheet events (+65 bootstrap) | 191 | 126 sheet + 65 `lead.migrated_from_sheets` | orphans/test excluded | 96 test + 19 orphan | 0 | PASS |
| ACCESS | 5 rules | 5 | 5 | tg:{id} principal | 0 | 0 | PASS |
| deliveries (lead_card + reminder) | 251 + 13 | 264 | 264 | orphan lead_id→NULL; pending→cancelled/sent | 1 malformed | 1 | PASS |
| config | 340 | 340 | 340 | secretish flagged | secrets skipped if pattern | 0 | PASS |
| errors | 1 historical non-synth | 1 shadow-import (+3 seed fixtures neutralized) | 1 | retryable=false resolved=true | 2951 synth | 0 | PASS |
| pending_deliveries | n/a | **0** | — | historical never re-queued | — | — | PASS |

## Status distribution (leads)

| Status | Sheets (collapsed) | PG | Difference |
|---|---:|---:|---:|
| new | 4 | 4 | 0 |
| pending | 29 | 29 | 0 |
| processed | 3 | 3 | 0 |
| spam | 29 | 29 | 0 |

## FK / orphan

| Check | Count | Verdict |
|---|---:|---|
| orphan_events | 0 | PASS |
| orphan_dedup | 0 | PASS |
| pending_deliveries | 0 | PASS |

## Residuals (documented, non-blocking for shadow)

1. **1 unknown:** malformed LEAD_DELIVERIES webhook-dump row — not imported.
2. **67 deliveries** with `stable_lead_ref` not in collapsed CLEAN set → stored with `lead_id NULL` (intentional; no fake FK).
3. **DEDUP_INDEX** sheet keys largely empty for business rows → protection reconstructed via synthesized `lead_dedup_keys` + UNIQUE constraints.
4. **3 schema-seed synthetic error fixtures** remain in table but `retryable=false` / `resolved=true` after import neutralize.
