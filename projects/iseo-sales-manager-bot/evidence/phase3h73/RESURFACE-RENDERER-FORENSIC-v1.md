# RESURFACE RENDERER FORENSIC

Phase 3H.7.2 `phase3h72-06-real-leads-resurface.mjs` built a **special simplified card**:

- title suffix `operator resurface`
- `Контакт:` from `primary_contact || phone` (no formula-error filter)
- generic draft fallback when `first_reply_text` empty
- footer `lead:<suffix> · REAL_REOPEN_*`
- **did not** call OPS `Format Telegram Lead Card` / `formatLeadCard` / approved template router

Canonical production path uses `formatLeadCard` (sm-msg-v2.4) + Expand Delivery personalization.

## Matrix
- REAL_REOPEN_A (6e4c68e4): formula_error=true special_renderer=true canonical_fixture_ok=true
- REAL_REOPEN_B (259d186f): formula_error=true special_renderer=true canonical_fixture_ok=true
- REAL_REOPEN_C (d0f1e764): formula_error=false special_renderer=true canonical_fixture_ok=true
