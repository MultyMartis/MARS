# OPERATOR TELEGRAM SANDBOX BINDING v1

## Verdict

**PASS.** The sandbox destination was resolved from the existing Sales Manager bot send contour.

## Sanitized binding

- Destination is an operator private chat, not a production manager group.
- The positive, private-user-shaped chat/user identifier is represented only by sanitized hash `3FBE21323E22BFC1`.
- Allowlist size: `1`.
- Manager-card and Admin reply destinations resolve to the same private operator chat.
- No raw Telegram ID, token, username, or personal data is recorded in this artifact.

## Boundary

This binding is for Phase 3B.2 synthetic acceptance only. It does not authorize a production manager-group destination or production activation.
