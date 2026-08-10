# FAILED ACCEPTANCE LEAD IDENTIFICATION

## Primary reduced/status-only defect during live acceptance
**REAL_REOPEN_A** (suffix `6e4c68e4`)

- Observed shape: pending status-only card with client/site/service/request + «Возвращено в обработку»
- Cause: Telegram callback reopen after Phase 3H.7.3 parity repair used reduced `buildFinalCard` edit_text on authoritative cards

## Spam lifecycle lead (acks correct; body degraded)
**REAL_REOPEN_C** (suffix `d0f1e764`)

- Live Spam → Reopen → Spam acknowledgements were correct
- Current authoritative status at repair start: **spam**
- Cards had been overwritten by the same reduced status-sync renderer

## Full canonical lead that remained good
**REAL_REOPEN_B** (suffix `259d186f`)

- Remained full canonical pending after 3H.7.3 until used for controlled lifecycle proof in 3H.7.3.1

## Method
Live `lead_clean_v2` + `LEAD_DELIVERIES` + Handle source inspection. Not screenshot order alone.
