# AFFECTED H RECONCILIATION v1

**Marker:** `ISEO_SM_FR2_H_PROBABLE_TEST` only.

## Actions

- Identified one stable synthetic business lead family for the marker.
- Preserved RAW/CLEAN business records (no mass delete).
- Marked successful recipient deliveries as delivered / guarded.
- Collapsed further **resend eligibility** via LEAD_DELIVERIES + CONFIG `tg_delivered:*` guards without deleting audit evidence.
- Did **not** delete already-delivered Telegram cards.
- Lifecycle buttons remain idempotent for old duplicates.
- Fixtures A–G and real leads not mutated.

## Counts (sanitized)

| Metric | Value |
|--------|------:|
| Send waves reconciled | 4 |
| Delivery keys reconciled | 8 |
| Duplicate cards estimated (historical) | 8 |
| Gmail-hash guards written | 4 |
| Further resend eligibility | blocked |

## Note

Synthetic webhook fixtures often lack a real Gmail id for PROCESSED finalization; CONFIG + ledger guards are the permanent stop for this marker.
