# GMAIL FINALIZATION BOUNDARY v1

## Incident failure

Gmail finalization (`Add Gmail PROCESSED` → `Remove Gmail Incoming`) sits **after** Aggregate → IF Telegram Success. During the incident, Stamp crashed → Aggregate never ran → Gmail labels never applied → message stayed intake-eligible → infinite poll loop.

## Required policy (3D.7.1)

After business storage and **Admin-anchor delivery**:

1. Apply PROCESSED label.
2. Remove intake/incoming label per workflow policy.
3. **Do not wait** for every moderator delivery to succeed.
4. Moderator delivery errors remain isolated and retryable via LEAD_DELIVERIES.
5. Gmail finalization failure must **not** resend already-delivered recipients (ledger owns skip).

## Aggregate change

Previously: `finalizeGmail = adminAnchorOk && othersSettled`  
Now: `finalizeGmail = adminAnchorOk` (policy `admin_anchor_delivered`)

If no admin in batch (fail-soft): finalize only when ≥1 delivered and all settled.

## Business second guard

CONFIG key `tg_delivered:<gmail_message_id>` is written on successful finalize path via Update Last Success (now prefers Aggregate Delivery Finalizer over disconnected Telegram Result Gate).
