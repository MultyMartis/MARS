# AUTHORITATIVE CARD INSTANCE v1.1

Contract: `iseo-authoritative-card-instance-v1.1`

Generated: `2026-08-10T10:23:18.629Z`

## Rules
1. Exactly one current authoritative card instance per lead + recipient
2. Recipient key is case-normalized
3. Preference: acceptance_canonical > operator_resurface_parity > operator_resurface > initial
4. After explicit operator resurface / parity / acceptance canonicalization, the new card becomes authoritative
5. Older instances are superseded for current sync accounting
6. Callbacks on superseded cards still resolve the same lead safely
7. Superseded callbacks cannot make the superseded message authoritative again
8. Expected current sync set = one card per active recipient (4)

## Nodes
- Expand Card Sync Copies (selection)
- Handle Callback Action (full canonical edit body; no status-only renderer for authoritative pending/terminal cards)
