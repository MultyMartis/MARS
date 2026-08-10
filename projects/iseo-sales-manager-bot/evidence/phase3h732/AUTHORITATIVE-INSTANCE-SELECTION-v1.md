# AUTHORITATIVE INSTANCE SELECTION — v1.2

## Bug (v1.1)
`key.includes('operator_resurface')` also matched `operator_resurface_parity` → double score 220 vs acceptance_canonical 160.

## Fix (v1.2)
Exclusive if/else-if delivery-class scoring + stronger recency + callback initiator message preference + archive exclusion.

Contract: `iseo-authoritative-card-instance-v1.2`

Post-fix sim for LIVE_CARD_PROOF_1: initiator registry+edit → MSG_898.
