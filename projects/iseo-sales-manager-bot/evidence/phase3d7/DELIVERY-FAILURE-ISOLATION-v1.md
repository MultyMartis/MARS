# DELIVERY FAILURE ISOLATION v1

## Accepted finalization policy (Admin-anchor)

A lead is operationally finalized for Gmail when:

1. At least one **Admin** destination receives the card (`delivered`);
2. All other active recipients are `delivered`, `failed_retryable`, `failed_terminal`, or `skipped_ineligible`;
3. Business CLEAN row is stored safely.

Moderator delivery failures:

- do **not** cause duplicate business processing;
- do **not** resend Admin cards;
- are recorded per recipient in LEAD_DELIVERIES.

Incoming Gmail labels remain until this policy is satisfied.
