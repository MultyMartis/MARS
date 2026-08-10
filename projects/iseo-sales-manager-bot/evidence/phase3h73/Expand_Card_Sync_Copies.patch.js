// Phase 3H.7.3 — Expand Card Sync Copies (iseo-lead-card-instance-registry-v1)
// Sync ONLY authoritative current card instances (one per recipient).
// Superseded / historical deliveries do not count as current sync failures.
const h = (() => {
  try { return $('Handle Callback Action').first().json || {}; } catch (e) { return $input.first().json || {}; }
})();

const outcome = String(h.callback_outcome || '');
const shouldSync = (outcome === 'applied' || outcome === 'idempotent' || outcome === 'conflict') && h.telegram_edit === true;
const leadId = String(h.lead_id || '');
const editText = String(h.edit_text || '');

if (!shouldSync) {
  return [{ json: {
    ...h,
    skip_card_edits: true,
    card_sync_count: 0,
    edit_chat_id: '',
    edit_message_id: '',
    edit_text: editText,
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
  } }];
}

let rows = [];
try { rows = $input.all().map((i) => i.json).filter(Boolean); } catch (e) { rows = []; }
rows = rows.filter((r) => r && !r.error && !r.errorMessage);

function preferAuthoritative(a, b) {
  const score = (r) => {
    let s = 0;
    const key = String(r.delivery_key || '');
    const reason = String(r.delivery_reason || '');
    const state = String(r.card_instance_state || '').toLowerCase();
    if (reason === 'operator_resurface' || key.includes('operator_resurface')) s += 100;
    if (state === 'authoritative' || state === 'current') s += 50;
    if (state === 'superseded') s -= 1000;
    const ts = Date.parse(String(r.delivered_at || r.delivery_timestamp || r.updated_at || '')) || 0;
    s += ts / 1e13;
    return s;
  };
  return score(b) >= score(a) ? b : a;
}

const candidates = rows.filter((r) => {
  if (String(r.stable_lead_ref || '') !== leadId) return false;
  if (String(r.delivery_status || '') !== 'delivered') return false;
  if (!r.telegram_message_ref) return false;
  if (!(r.telegram_delivery_chat_id || r.telegram_chat_id)) return false;
  if (String(r.card_instance_state || '').toLowerCase() === 'superseded') return false;
  if (String(r.active_sync || '').toLowerCase() === 'false') return false;
  return true;
});

const byRecipient = new Map();
for (const r of candidates) {
  const key = String(r.recipient_ref || r.telegram_delivery_chat_id || r.telegram_chat_id || '');
  if (!key) continue;
  const prev = byRecipient.get(key);
  byRecipient.set(key, prev ? preferAuthoritative(prev, r) : r);
}

const authoritative = [...byRecipient.values()];
const authKeySet = new Set(authoritative.map((r) => String(r.delivery_key || `${r.recipient_ref}:${r.telegram_message_ref}`)));
const superseded_count = candidates.filter((r) => !authKeySet.has(String(r.delivery_key || `${r.recipient_ref}:${r.telegram_message_ref}`))).length;

if (!authoritative.length) {
  return [{ json: {
    ...h,
    skip_card_edits: false,
    card_sync_count: 1,
    card_sync_mode: 'initiator_fallback',
    edit_chat_id: String(h.edit_chat_id || h.callback_chat_id || h.chat_id || ''),
    edit_message_id: String(h.edit_message_id || h.callback_message_id || h.telegram_message_ref || ''),
    edit_text: editText,
    recipient_ref: 'callback_initiator',
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
    superseded_historical_ignored: superseded_count,
  } }];
}

return authoritative.map((c) => ({
  json: {
    ...h,
    skip_card_edits: false,
    card_sync_count: authoritative.length,
    card_sync_mode: 'authoritative_current',
    edit_chat_id: String(c.telegram_delivery_chat_id || c.telegram_chat_id || ''),
    edit_message_id: String(c.telegram_message_ref || ''),
    edit_text: editText,
    recipient_ref: String(c.recipient_ref || ''),
    delivery_key: String(c.delivery_key || ''),
    card_instance_state: 'authoritative',
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
    superseded_historical_ignored: superseded_count,
  },
}));
