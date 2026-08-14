// Phase 3H.8.2.2 — Reminder Mark Window Complete + current-state selector observability
// Phase 3H.8.2 — Reminder Mark Window Complete + observability v1.1 + 429 error stamps
// - Always stamp last evaluation/decision
// - Stamp pending_reminder_last_window ONLY on successful window completion
// - ERROR / 429 / CURRENT_STATE MUST NOT mark the business date as sent

const j = $input.first().json;
const nowIso = new Date().toISOString();
const reason = String(j.reminder_skip_reason || '');
const send = j.reminder_send === true;
const markComplete = j.reminder_mark_window_complete === true || reason === 'all_recipients_done';

function decisionOf() {
  if (markComplete && (reason === 'all_recipients_done' || j.reminder_last_recipient_count)) return 'SENT';
  if (reason === 'zero_pending' || reason === 'below_min_count') return 'SKIPPED_ZERO_PENDING';
  if (reason === 'already_completed' || reason === 'all_recipients_done') return 'SKIPPED_ALREADY_SENT';
  if (reason === 'disabled' || reason === 'outside_window' || reason === 'invalid_config') {
    return reason === 'outside_window' ? 'SKIPPED_OUTSIDE_WINDOW' : (reason === 'disabled' ? 'SKIPPED_DISABLED' : 'ERROR');
  }
  if (reason === 'current_state_resolution_error' || String(j.reminder_decision_code || '') === 'ERROR_CURRENT_STATE_RESOLUTION') {
    return 'ERROR_CURRENT_STATE_RESOLUTION';
  }
  if (reason === 'no_recipients' || reason === 'access_read_error' || reason === 'ledger_read_error' || reason === 'sheets_429' || reason === 'sheets_permanent') return 'ERROR';
  if (!send && reason) return 'ERROR';
  return 'ERROR';
}

const decision = decisionOf();
const pendingSnap = (j.pending_count_snapshot != null && j.pending_count_snapshot !== '')
  ? String(j.pending_count_snapshot)
  : '';

const evaluationWrites = [
  { key: 'pending_reminder_last_evaluation_at', value: nowIso, description: 'Phase 3H.8.2.2 last reminder evaluation' },
  { key: 'pending_reminder_last_decision', value: decision, description: 'Phase 3H.8.2.2 reminder decision' },
  { key: 'pending_reminder_last_check_at', value: nowIso, description: 'Phase 3H.8.2.2 last reminder check' },
];
if (pendingSnap !== '') {
  evaluationWrites.push({
    key: 'pending_reminder_last_pending_count',
    value: pendingSnap,
    description: 'Phase 3H.8.2.2 authoritative pending count at last evaluation',
  });
}
if (j.raw_candidate_rows != null && String(j.raw_candidate_rows) !== '') {
  evaluationWrites.push({
    key: 'pending_reminder_last_raw_candidate_rows',
    value: String(j.raw_candidate_rows),
    description: 'Phase 3H.8.2.2 raw CLEAN pending candidate rows',
  });
}
if (j.unique_candidate_leads != null && String(j.unique_candidate_leads) !== '') {
  evaluationWrites.push({
    key: 'pending_reminder_last_unique_candidate_leads',
    value: String(j.unique_candidate_leads),
    description: 'Phase 3H.8.2.2 unique candidate lead ids',
  });
}
if (j.safe_unknown_count != null && String(j.safe_unknown_count) !== '') {
  evaluationWrites.push({
    key: 'pending_reminder_last_safe_unknown_count',
    value: String(j.safe_unknown_count),
    description: 'Phase 3H.8.2.2 SAFE_UNKNOWN lead count',
  });
}
if (j.reminder_selector_contract) {
  evaluationWrites.push({
    key: 'pending_reminder_selector_contract',
    value: String(j.reminder_selector_contract),
    description: 'Phase 3H.8.2.2 selector contract id',
  });
}

if (decision === 'ERROR' || decision === 'ERROR_CURRENT_STATE_RESOLUTION' || /^ERROR/.test(decision)) {
  evaluationWrites.push(
    { key: 'pending_reminder_last_error_safe', value: String(j.last_error_safe || (decision === 'ERROR_CURRENT_STATE_RESOLUTION' ? 'ошибка current-state селектора' : 'ошибка чтения таблицы')), description: 'Phase 3H.8.2.2 safe error' },
    { key: 'pending_reminder_last_error_class', value: String(j.last_error_class || j.reminder_decision_code || decision || 'ERROR'), description: 'Phase 3H.8.2.2 error class' },
    { key: 'pending_reminder_last_error_stage', value: String(j.last_error_stage || (decision === 'ERROR_CURRENT_STATE_RESOLUTION' ? 'CURRENT_STATE' : '')), description: 'Phase 3H.8.2.2 error stage' },
    { key: 'pending_reminder_last_error_at', value: nowIso, description: 'Phase 3H.8.2.2 error time' },
    { key: 'pending_reminder_last_retry_attempts', value: String(j.sheets_retry_attempts || j.sheets_fail_count || 0), description: 'Phase 3H.8.2.2 retry attempts' },
  );
} else {
  evaluationWrites.push(
    { key: 'pending_reminder_last_error_safe', value: '', description: 'Phase 3H.8.2.2 clear error' },
    { key: 'pending_reminder_last_error_class', value: '', description: 'Phase 3H.8.2.2 clear error class' },
    { key: 'pending_reminder_last_error_stage', value: '', description: 'Phase 3H.8.2.2 clear error stage' },
  );
}

let config_write = null;
const config_write_extra = evaluationWrites.slice();

if (markComplete) {
  config_write = {
    key: 'pending_reminder_last_window',
    value: String(j.reminder_window || ''),
    type: 'string',
    updated_at: nowIso,
    updated_by: 'reminder_schedule',
    description: 'Phase 3F.1/3H.8 completed reminder window',
  };
  config_write_extra.push(
    { key: 'pending_reminder_last_success_at', value: nowIso, description: 'Phase 3H.8 last successful reminder send' },
    { key: 'pending_reminder_last_recipient_count', value: String(j.reminder_last_recipient_count || j.recipient_count || ''), description: 'Phase 3H.8 recipients at last success' },
  );
  const dec = config_write_extra.find((x) => x.key === 'pending_reminder_last_decision');
  if (dec) dec.value = 'SENT';
} else if (!config_write && evaluationWrites.length) {
  const first = evaluationWrites[0];
  config_write = {
    key: first.key,
    value: String(first.value),
    type: 'string',
    updated_at: nowIso,
    updated_by: 'reminder_schedule',
    description: first.description || '',
  };
  config_write_extra.splice(0, 1);
}

return [{ json: {
  ...j,
  reminder_decision: decision,
  config_write,
  config_write_extra,
} }];
