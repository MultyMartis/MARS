// Phase 3H.7.3 — Aggregate Card Sync Result
// Contracts: iseo-lead-callback-ack-v1.0 + iseo-lead-card-instance-registry-v1
// Semantic status acknowledgement is INDEPENDENT of historical-card sync noise.
const ACK = {
  processed: 'Лид отмечен как обработанный.',
  spam: 'Лид отмечен как спам.',
  reopen: 'Лид возвращён в обработку.',
  already_pending: 'Заявка уже находится в обработке.',
  already_processed: 'Заявка уже отмечена как обработанная.',
  already_spam: 'Заявка уже отмечена как спам.',
  not_found: 'Заявка не найдена в рабочем реестре. Обратитесь к администратору.',
};

function resolveSemanticAck(h) {
  const outcome = String(h.callback_outcome || '');
  const eventType = String(h.event_type || '');
  const newStatus = String(h.new_status || '');
  const prior = String(h.prior_status || '');
  const action = String(h.action || h.callback_action || '');
  const lastAction = String(h.last_manager_action || '');

  if (outcome === 'unknown_lead') return ACK.not_found;
  if (outcome === 'unauthorized') return String(h.answer_text || 'Недостаточно прав для изменения статуса.');
  if (outcome === 'unknown' || outcome === 'storage_error' || outcome === 'ambiguous' || outcome === 'archived') {
    return String(h.answer_text || 'OK');
  }

  if (outcome === 'applied') {
    if (
      eventType === 'manager_reopened' ||
      lastAction === 'reopened' ||
      (action === 'reopen' && newStatus === 'pending')
    ) {
      return ACK.reopen;
    }
    if (newStatus === 'spam' || eventType === 'manager_marked_spam') return ACK.spam;
    if (newStatus === 'processed' || eventType === 'manager_marked_processed') return ACK.processed;
    return String(h.answer_text || 'OK');
  }

  if (outcome === 'idempotent') {
    if (eventType === 'manager_reopen_duplicate_ignored' || action === 'reopen') return ACK.already_pending;
    if (prior === 'spam' || action === 'spam' || newStatus === 'spam') return ACK.already_spam;
    if (prior === 'processed' || action === 'processed' || newStatus === 'processed') return ACK.already_processed;
    return String(h.answer_text || 'Этот статус уже установлен.');
  }

  if (outcome === 'conflict') {
    return String(h.answer_text || 'Статус лида уже изменён другим сотрудником.');
  }

  return String(h.answer_text || 'OK');
}

const h = (() => {
  try { return $('Handle Callback Action').first().json || {}; } catch (e) { return {}; }
})();

const items = $input.all().map((i) => i.json || {});
if (items.some((x) => x.skip_card_edits)) {
  const answer = resolveSemanticAck(h);
  return [{ json: {
    ...h,
    edit_ok: true,
    card_sync_attempted: 0,
    card_sync_failed: 0,
    card_sync_ok: 0,
    answer_text: answer,
    reply_text: answer,
    chat_id: String(h.chat_id || h.edit_chat_id || ''),
    ack_contract: 'iseo-lead-callback-ack-v1.0',
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
    acknowledgements: 1,
  } }];
}

let failed = 0;
let ok = 0;
for (const j of items) {
  const isFail = Boolean(j.error || j.message?.error_code || j.ok === false || j.edit_ok === false);
  if (isFail) failed += 1;
  else ok += 1;
}

const semantic = resolveSemanticAck(h);
// Do NOT replace semantic acknowledgement with vague sync warning.
// Current authoritative sync failures are recorded separately for operators/ops.
const answer = semantic;
const card_sync_warning = (String(h.callback_outcome || '') === 'applied' && failed > 0)
  ? 'Не все текущие копии карточки удалось обновить.'
  : '';

return [{ json: {
  ...h,
  edit_ok: failed === 0,
  card_sync_attempted: items.length,
  card_sync_failed: failed,
  card_sync_ok: ok,
  answer_text: answer,
  reply_text: answer,
  card_sync_warning,
  chat_id: String(h.chat_id || h.edit_chat_id || ''),
  event_type_extra: failed > 0 ? 'lead_delivery_card_update_failed' : 'lead_delivery_card_updated',
  ack_contract: 'iseo-lead-callback-ack-v1.0',
  card_instance_registry: 'iseo-lead-card-instance-registry-v1',
  acknowledgements: 1,
  last_callback_summary: {
    status: failed > 0 ? 'partial_current_sync' : 'ok',
    action: h.action || h.new_status || h.prior_status || '',
    outcome: h.callback_outcome || '',
    copies_ok: ok,
    copies_total: items.length,
    semantic_ack: semantic,
    at: h.last_manager_action_at || new Date().toISOString(),
  },
} }];
