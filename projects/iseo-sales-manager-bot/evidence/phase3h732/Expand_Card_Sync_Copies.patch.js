// Phase 3H.7.3.2 — Expand Card Sync Copies (iseo-authoritative-card-instance-v1.2)
// Sync ONLY authoritative current card instances (one per recipient, case-normalized).
// Exclusive delivery-class scoring: operator_resurface_parity must NOT also match operator_resurface.
// Callback initiator chat prefers the clicked message_id (operator-visible card).
// Archive / pending-view cards excluded. Superseded excluded.
const h = (() => {
  try { return $('Handle Callback Action').first().json || {}; } catch (e) { return $input.first().json || {}; }
})();

const outcome = String(h.callback_outcome || '');
const shouldSync = (outcome === 'applied' || outcome === 'idempotent' || outcome === 'conflict') && h.telegram_edit === true;
const leadId = String(h.lead_id || '');
const editText = String(h.edit_text || '');
const callbackChat = String(h.callback_chat_id || h.edit_chat_id || h.chat_id || '').trim();
const callbackMsg = String(h.callback_message_id || h.edit_message_id || '').trim();

if (!shouldSync) {
  return [{ json: {
    ...h,
    skip_card_edits: true,
    card_sync_count: 0,
    edit_chat_id: '',
    edit_message_id: '',
    edit_text: editText,
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
    authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.2',
  } }];
}

let rows = [];
try { rows = $input.all().map((i) => i.json).filter(Boolean); } catch (e) { rows = []; }
rows = rows.filter((r) => r && !r.error && !r.errorMessage);

function normalizeRecipientKey(r) {
  const ref = String(r.recipient_ref || '').trim().toLowerCase();
  if (ref) return ref;
  const chat = String(r.telegram_delivery_chat_id || r.telegram_chat_id || '').trim();
  return chat ? ('chat:' + chat) : '';
}

function scoreAuthoritative(r) {
  let s = 0;
  const key = String(r.delivery_key || '');
  const reason = String(r.delivery_reason || '').toLowerCase();
  const state = String(r.card_instance_state || '').toLowerCase();
  const keyLower = key.toLowerCase();
  // EXCLUSIVE classes — do not let parity also match includes('operator_resurface').
  if (keyLower.includes('acceptance_canonical') || reason.includes('acceptance_canonical')) s += 140;
  else if (keyLower.includes('operator_resurface_parity') || reason === 'operator_resurface_parity') s += 120;
  else if (reason === 'operator_resurface' || keyLower.startsWith('operator_resurface:') || keyLower.includes(':operator_resurface:')) s += 100;
  if (state === 'authoritative' || state === 'current') s += 50;
  if (state === 'superseded') s -= 1000;
  if (r.telegram_delivery_chat_id || r.telegram_chat_id) s += 20;
  const ts = Date.parse(String(r.delivered_at || r.delivery_timestamp || r.updated_at || '')) || 0;
  s += ts / 1e11;
  const mid = Number(r.telegram_message_ref);
  if (Number.isFinite(mid) && mid > 0) s += mid / 1e9;
  return s;
}

function preferAuthoritative(a, b) {
  return scoreAuthoritative(b) >= scoreAuthoritative(a) ? b : a;
}

const candidates = rows.filter((r) => {
  if (String(r.stable_lead_ref || '') !== leadId) return false;
  if (String(r.delivery_status || '') !== 'delivered') return false;
  if (!r.telegram_message_ref) return false;
  if (!(r.telegram_delivery_chat_id || r.telegram_chat_id)) return false;
  if (String(r.card_instance_state || '').toLowerCase() === 'superseded') return false;
  if (String(r.active_sync || '').toLowerCase() === 'false') return false;
  const key = String(r.delivery_key || '').toLowerCase();
  const reason = String(r.delivery_reason || '').toLowerCase();
  if (key.includes('archive') || reason.includes('archive') || reason.includes('pending_view')) return false;
  return true;
});

const byRecipient = new Map();
for (const r of candidates) {
  const key = normalizeRecipientKey(r);
  if (!key) continue;
  const prev = byRecipient.get(key);
  byRecipient.set(key, prev ? preferAuthoritative(prev, r) : r);
}

const authoritative = [...byRecipient.values()];
const authKeySet = new Set(authoritative.map((r) => String(r.delivery_key || (r.recipient_ref + ':' + r.telegram_message_ref))));
const superseded_count = candidates.filter((r) => !authKeySet.has(String(r.delivery_key || (r.recipient_ref + ':' + r.telegram_message_ref)))).length;

if (!authoritative.length) {
  return [{ json: {
    ...h,
    skip_card_edits: false,
    card_sync_count: 1,
    card_sync_mode: 'initiator_fallback',
    edit_chat_id: String(callbackChat || ''),
    edit_message_id: String(callbackMsg || ''),
    edit_text: editText,
    message_ref_source: 'callback_initiator_fallback',
    recipient_ref: 'callback_initiator',
    card_instance_registry: 'iseo-lead-card-instance-registry-v1',
    authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.2',
    superseded_historical_ignored: superseded_count,
  } }];
}

return authoritative.map((c) => {
  const cardChat = String(c.telegram_delivery_chat_id || c.telegram_chat_id || '');
  const registryMsg = String(c.telegram_message_ref || '');
  const useCallback = Boolean(callbackChat && cardChat && callbackChat === cardChat && callbackMsg);
  return {
    json: {
      ...h,
      skip_card_edits: false,
      card_sync_count: authoritative.length,
      card_sync_mode: 'authoritative_current',
      edit_chat_id: cardChat,
      edit_message_id: useCallback ? callbackMsg : registryMsg,
      edit_text: editText,
      message_ref_source: useCallback ? 'callback_initiator' : 'authoritative_registry',
      registry_message_ref: registryMsg,
      recipient_ref: String(c.recipient_ref || ''),
      delivery_key: String(c.delivery_key || ''),
      card_instance_state: 'authoritative',
      card_instance_registry: 'iseo-lead-card-instance-registry-v1',
      authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.2',
      superseded_historical_ignored: superseded_count,
    },
  };
});
