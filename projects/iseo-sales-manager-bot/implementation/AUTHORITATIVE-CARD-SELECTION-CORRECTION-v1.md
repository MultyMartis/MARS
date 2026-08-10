# AUTHORITATIVE CARD SELECTION CORRECTION — v1.1

Contract: `iseo-authoritative-card-instance-v1.1`

## Rules
1. Exactly one authoritative current card per lead + recipient.
2. Recipient identity is case-normalized (`u:ABC` ≡ `u:abc`).
3. Preference order:
   - `acceptance_canonical`
   - `operator_resurface_parity`
   - `operator_resurface`
   - initial `lead_delivery`
4. After explicit resurface / parity / acceptance canonicalization, the new card is authoritative.
5. Older instances are superseded for **current sync accounting only**.
6. Callbacks on superseded cards still resolve the same lead safely.
7. Superseded callbacks cannot make the old message authoritative again.
8. Expected current sync set = one card × active recipients (4).

## Implementation
- Runtime: `selectAuthoritativeCardInstances` in `canonical-lead-card-renderer-v1.mjs`
- Live Admin node: **Expand Card Sync Copies**
