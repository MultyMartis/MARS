// Phase 3H.7.3.2 — Aggregate Card Sync Result
// Contracts: iseo-lead-callback-ack-v1.0 + iseo-authoritative-card-instance-v1.2
// Semantic status acknowledgement is INDEPENDENT of card-sync success.
// Per-card Telegram results required; do not claim global PASS from status mutation alone.
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

function classifyTelegramEditFailure(j) {
  const raw = String(
    j.error ||
    j.message?.description ||
    j.description ||
    j.errorDescription ||
    ''
  ).toLowerCase();
  if (!raw && j.ok !== false && !j.message?.error_code) return '';
  if (raw.includes('message to edit not found') || raw.includes('message_id_invalid')) return 'message_to_edit_not_found';
  if (raw.includes('message is not modified')) return 'message_not_modified';
  if (raw.includes('chat not found')) return 'chat_not_found';
  if (raw.includes("message can't be edited") || raw.includes('message can\'t be edited')) return 'message_cant_be_edited';
  if (raw.includes('bad request')) return 'bad_request';
  if (raw.includes('reply markup') || raw.includes('inline keyboard')) return 'reply_markup_invalid';
  if (j.message?.error_code === 400) return 'bad_request';
  if (j.ok === false) return 'telegram_ok_false';
  if (j.error) return 'telegram_edit_error';
  return '';
}

function isTelegramEditFail(j) {
  if (j.ok === true) return false;
  if (j.ok === false) return true;
  if (j.edit_ok === false) return true;
  if (j.error) return true;
  if (j.message?.error_code) return true;
  // n8n Telegram success typically returns message payload with message_id / chat
  if (j.message_id || j.chat?.id || j.result?.message_id) return false;
  // Unknown shape without explicit success markers — treat as fail (no false PASS).
  return true;
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
    authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.2',
    acknowledgements: 1,
  } }];
}

let failed = 0;
let ok = 0;
const perCard = [];
const failureClasses = [];
for (const j of items) {
  const failClass = classifyTelegramEditFailure(j);
  const isFail = isTelegramEditFail(j);
  if (isFail) {
    failed += 1;
    if (failClass) failureClasses.push(failClass);
  } else {
    ok += 1;
  }
  perCard.push({
    recipient_ref: String(j.recipient_ref || ''),
    delivery_key: String(j.delivery_key || ''),
    message_ref_source: String(j.message_ref_source || ''),
    edit_ok: !isFail,
    telegram_ok: j.ok === true || Boolean(j.message_id || j.chat?.id || j.result?.message_id),
    failure_class: failClass || (isFail ? 'unknown_edit_failure' : ''),
  });
}

const semantic = resolveSemanticAck(h);
const answer = semantic;
const uniqueFailClasses = [...new Set(failureClasses)];
const card_sync_warning = (String(h.callback_outcome || '') === 'applied' && failed > 0)
  ? ('Не все текущие копии карточки удалось обновить.' + (uniqueFailClasses.length ? (' [' + uniqueFailClasses.join(',') + ']') : ''))
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
  card_sync_failure_classes: uniqueFailClasses,
  card_sync_per_card: perCard,
  chat_id: String(h.chat_id || h.edit_chat_id || ''),
  event_type_extra: failed > 0 ? 'lead_delivery_card_update_failed' : 'lead_delivery_card_updated',
  ack_contract: 'iseo-lead-callback-ack-v1.0',
  card_instance_registry: 'iseo-lead-card-instance-registry-v1',
  authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.2',
  acknowledgements: 1,
  last_callback_summary: {
    status: failed > 0 ? 'partial_current_sync' : (ok === items.length && items.length > 0 ? 'ok' : 'ok'),
    action: h.action || h.new_status || h.prior_status || '',
    outcome: h.callback_outcome || '',
    copies_ok: ok,
    copies_total: items.length,
    semantic_ack: semantic,
    failure_classes: uniqueFailClasses,
    at: h.last_manager_action_at || new Date().toISOString(),
  },
} }];
