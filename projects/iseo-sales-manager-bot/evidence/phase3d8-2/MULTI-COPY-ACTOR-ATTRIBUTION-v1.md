# MULTI-COPY ACTOR ATTRIBUTION v1

- Resolve actor once in Handle Callback Action.
- Expand Card Sync Copies reuses the same edit_text (same actor label) for all known delivered copies.
- Do not resolve actor per recipient.
- Do not use recipient identity as actor.
- Per-copy edit failures remain isolated; lifecycle mutation is not rolled back.
