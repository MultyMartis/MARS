# FULL CANONICAL RE-RENDER ON AUTHORITATIVE CARD

At: `2026-08-10T10:23:18.742Z`

## Change
Handle Callback Action no longer uses reduced status-only `buildFinalCard` body for authoritative edits.

Pending / spam / processed authoritative cards now receive:
- full production heading + status
- client / contact / site
- interest / comment / quality / missing / next step
- approved first-reply block when present on lead
- additive status attribution (Кем/Время or Возвращено в обработку)

## Apply checks
- handle_canonical_builder: **true**
- handle_no_reduced_usluga_builder: **true**
- handle_interest_field: **true**
- handle_reply_block: **true**
- expand_v11: **true**
- expand_case_normalize: **true**
- expand_parity_preference: **true**
- agg_semantic_independent: **true**
- admin_active: **true**
- node_count: **87**
