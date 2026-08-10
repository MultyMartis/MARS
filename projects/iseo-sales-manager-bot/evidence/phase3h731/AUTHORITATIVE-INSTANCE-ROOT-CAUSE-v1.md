# AUTHORITATIVE INSTANCE ROOT CAUSE

## Primary root cause
`Handle Callback Action` → `buildFinalCard()` produces **reduced status-only** `edit_text`.
`Expand Card Sync Copies` then edits **all authoritative current cards** with that reduced text.

Therefore any live Spam / Processed / Reopen after Phase 3H.7.3 parity repair **degrades** previously canonical cards.

## Contributing selection issues addressed in v1.1
- recipient_ref case variance (`u:ABC` vs `u:abc`) could split one recipient into two slots
- multiple historical deliveries (initial / resurface / parity) require deterministic preference for latest parity/canonical instance
- superseded historical failures must not affect current 4/4 sync accounting

## Not the cause
- Missing LEADS row
- Canonical object lacking fields
- Archive compactness contract
