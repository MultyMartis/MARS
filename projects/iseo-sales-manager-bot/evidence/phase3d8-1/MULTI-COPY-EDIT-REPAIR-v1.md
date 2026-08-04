# MULTI-COPY EDIT REPAIR v1

## Admin.dev changes

- IF Callback Mutate **false** → Read LEAD_DELIVERIES (skip LEAD_EVENTS append on non-applied)
- Expand Card Sync: ignore error rows; support applied + idempotent + conflict converge
- Edit Lead Card Message: already `continueRegularOutput` / continue on fail
- Aggregate: partial vs success initiator texts; counts `card_sync_ok/failed`

## Expected acceptance topology

Two delivered copies (Admin + active moderator) → two edits → buttons removed on both.
