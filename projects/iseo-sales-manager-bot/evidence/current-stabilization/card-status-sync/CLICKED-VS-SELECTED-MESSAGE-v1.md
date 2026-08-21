# CLICKED VS SELECTED MESSAGE — exec 36629

## Contract in force

`iseo-authoritative-card-instance-v1.2`  
`message_ref_source = callback_initiator`

## Comparison

| Ref | chat_id_h8 | message_id_h8 |
|-----|------------|---------------|
| Clicked (`callback.message`) | `3fbe2132` | `216da54b` |
| Selected edit target | `3fbe2132` | `216da54b` |

**Match:** YES — workflow attempted to edit the SAME card the operator clicked.

## Resolver notes

| Field | Value |
|-------|-------|
| card_sync_mode | `authoritative_current` |
| card_sync_count | 1 |
| registry_found | true |
| registry_source | ACCESS_CONTROL |
| superseded_historical_ignored | 0 |
| skip_card_edits | false |

## Conclusion

This regression is **not** the historical stale `message_id` selection defect. Clicked == selected.
