// Prepare Callback Answer — durable reply payload; toast already early-acked
function flattenInlineKeyboardUi(ui, slotCount, padText, padCb) {
  const slots = Math.max(1, Number(slotCount) || 1);
  const padT = String(padText || '📋 Все').slice(0, 64);
  const padC = String(padCb || 'sm:g:all');
  const flat = [];
  for (const block of (ui && ui.rows) || []) {
    for (const b of (block && block.row && block.row.buttons) || []) {
      const text = String(b.text || '').trim().slice(0, 64);
      const cb = String((b.additionalFields && b.additionalFields.callback_data) || b.callback_data || '').trim();
      if (text && cb) flat.push({ text, cb });
    }
  }
  // SAFETY: only use All pad when ZERO real buttons (empty-keyboard fallback).
  // Never fill unused fixed slots with duplicate All (UNUSED_SLOT_DEFAULTS_TO_ALL regression).
  if (!flat.length) flat.push({ text: padT, cb: padC });
  const used = Math.min(flat.length, slots);
  const out = { rm_kb_n: used, telegram_has_buttons: true };
  for (let i = 1; i <= slots; i++) {
    if (i <= used) {
      out['rm_b' + i + '_text'] = flat[i - 1].text;
      out['rm_b' + i + '_cb'] = flat[i - 1].cb;
    } else {
      out['rm_b' + i + '_text'] = '';
      out['rm_b' + i + '_cb'] = '';
    }
  }
  return out;
}
function chooseReplyKbBand(n) {
  const c = Math.max(1, Number(n) || 1);
  if (c <= 4) return 4;
  if (c <= 8) return 8;
  if (c <= 12) return 12;
  return 14;
}

const h = (() => {
  try { return $('Handle Callback Action').first().json || {}; } catch (e) { return {}; }
})();
const j = $input.first().json || {};
const action = String(j.action || h.action || j.callback_action || h.callback_action || '');
const outcome = String(j.callback_outcome || h.callback_outcome || '');
const isRaw = outcome === 'raw_inspected' || action === 'raw_source';
const isDigestView = action === 'queue_open' || action === 'full_card' || action === 'group_open' || outcome === 'queue_opened' || outcome === 'full_card_viewed' || outcome === 'queue_all' || outcome === 'group_opened';
const answer = String(j.answer_text || h.answer_text || 'OK');
const suppressVisible = Boolean(j.suppress_visible_reply || h.suppress_visible_reply);
let reply = (isRaw || isDigestView)
  ? String(j.raw_source_text || j.reply_text || h.raw_source_text || h.reply_text || answer)
  : answer;
if (suppressVisible) reply = '';
const reply2 = isRaw ? String(j.reply_text_2 || h.reply_text_2 || '') : '';
const _kbUi = (j.telegram_inline_keyboard_ui || h.telegram_inline_keyboard_ui || null);
const _hasBtn = Boolean(j.telegram_has_buttons || h.telegram_has_buttons);
let _flat = {};
if (_hasBtn) {
  const tmp = flattenInlineKeyboardUi(_kbUi, 14, '📋 Все', 'sm:g:all');
  const exact = Math.max(1, Math.min(14, Number(tmp.rm_kb_n) || 1));
  _flat = flattenInlineKeyboardUi(_kbUi, exact, '📋 Все', 'sm:g:all');
  // Exact slot count for Switch — do not round up to 4/8/12/14 (that reintroduced All pads).
  _flat.rm_kb_band = exact;
  _flat.telegram_has_buttons = true;
} else {
  _flat = { telegram_has_buttons: false, rm_kb_n: 0, rm_kb_band: 0 };
}
return [{ json: {
  ...h,
  ...j,
  ..._flat,
  answer_callback: false,
  skip_late_answer_callback: true,
  callback_query_id: String(h.callback_query_id || j.callback_query_id || ''),
  answer_text: answer,
  reply_text: reply,
  reply_text_2: reply2,
  chat_id: String(h.chat_id || j.chat_id || h.edit_chat_id || ''),
  raw_source_contract: isRaw ? 'iseo-literal-raw-source-v1.0' : (j.raw_source_contract || h.raw_source_contract || ''),
  digest_action_contract: isDigestView ? 'iseo-pending-digest-action-v1.0' : '',
  suppress_visible_reply: suppressVisible,
} }];
