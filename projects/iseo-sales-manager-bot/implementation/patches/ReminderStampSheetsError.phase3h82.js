// Phase 3H.8.2 — terminal Sheets error item already classified; pass through to observability.
const j = $input.first().json;
return [{ json: {
  ...j,
  reminder_send: false,
  reminder_mark_window_complete: false,
  pending_count_snapshot: j.pending_count_snapshot || 'not_computed',
} }];
