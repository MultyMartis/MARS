# RESURFACE MESSAGE PERSISTENCE — Phase 3H.7.3.2

## Finding
Acceptance_canonical send for LIVE_CARD_PROOF_1 initiator persisted NEW telegram_message_ref MSG_898 with chat_id present.

Other three recipients' acceptance_canonical rows reused prior message refs (MSG_884/885/886) — consistent with in-place edit during canonicalization (same visible cards).

## Defect class for this phase
Not missing persistence of MSG_898. Defect was **selection scoring** preferring older parity MSG_883 over persisted MSG_898.

## Required mapping (initiator) after acceptance_canonical
- lead_id: LIVE_CARD_PROOF_1
- recipient_id: RECIPIENT_A
- delivery_key: acceptance_canonical:…
- chat_id: present
- message_id: MSG_898
- delivery_type: acceptance_canonical
- created_at: 2026-08-10T10:24:43Z
- current intent: true (after v1.2 selection)
