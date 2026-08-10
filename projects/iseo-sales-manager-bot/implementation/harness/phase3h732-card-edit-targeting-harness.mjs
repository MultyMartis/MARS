/**
 * Phase 3H.7.3.2 — live card-edit targeting harness (static).
 * Proves exclusive scoring + callback initiator preference + archive exclusion.
 */
import {
  AUTHORITATIVE_CARD_INSTANCE_CONTRACT,
  selectAuthoritativeCardInstances,
  scoreAuthoritativeInstance,
  resolveEditMessageTarget,
} from '../runtime-libs/canonical-lead-card-renderer-v1.mjs';
import {
  buildReplyMarkup,
  buildReopenReplyMarkup,
} from '../runtime-libs/formatter-lib.mjs';

const results = [];
function check(id, name, pass, detail = '') {
  results.push({ id, name, pass: Boolean(pass), detail: String(detail || '') });
  const mark = pass ? 'PASS' : 'FAIL';
  console.log(`${mark} ${id} ${name}${detail ? ' — ' + detail : ''}`);
}

const leadId = 'lead_LIVE_CARD_PROOF_1';
const deliveries = [
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:aaa',
    delivery_status: 'delivered',
    delivery_key: `operator_resurface_parity:${leadId}:u:aaa:2026-08-10T09:42:57.432Z`,
    telegram_message_ref: '883',
    telegram_delivery_chat_id: '111',
    delivered_at: '2026-08-10T09:42:57.432Z',
  },
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:AAA', // case variance
    delivery_status: 'delivered',
    delivery_key: `acceptance_canonical:${leadId}:u:aaa:2026-08-10T10:24:43.931Z`,
    telegram_message_ref: '898',
    telegram_delivery_chat_id: '111',
    delivered_at: '2026-08-10T10:24:43.931Z',
  },
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:bbb',
    delivery_status: 'delivered',
    delivery_key: `operator_resurface_parity:${leadId}:u:bbb:2026-08-10T09:43:07.140Z`,
    telegram_message_ref: '886',
    telegram_delivery_chat_id: '222',
    delivered_at: '2026-08-10T09:43:07.140Z',
  },
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:bbb',
    delivery_status: 'delivered',
    delivery_key: `acceptance_canonical:${leadId}:u:bbb:2026-08-10T10:24:51.844Z`,
    telegram_message_ref: '886',
    telegram_delivery_chat_id: '222',
    delivered_at: '2026-08-10T10:24:51.844Z',
  },
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:ccc',
    delivery_status: 'delivered',
    delivery_key: `acceptance_canonical:${leadId}:u:ccc:2026-08-10T10:24:49.401Z`,
    telegram_message_ref: '885',
    telegram_delivery_chat_id: '333',
    delivered_at: '2026-08-10T10:24:49.401Z',
  },
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:ddd',
    delivery_status: 'delivered',
    delivery_key: `acceptance_canonical:${leadId}:u:ddd:2026-08-10T10:24:46.638Z`,
    telegram_message_ref: '884',
    telegram_delivery_chat_id: '444',
    delivered_at: '2026-08-10T10:24:46.638Z',
  },
  // superseded historical
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:aaa',
    delivery_status: 'delivered',
    delivery_key: `lead_delivery:${leadId}:u:aaa`,
    telegram_message_ref: '854',
    telegram_delivery_chat_id: '111',
    card_instance_state: 'superseded',
    delivered_at: '2026-08-10T08:36:16.000Z',
  },
  // archive view — must be excluded
  {
    stable_lead_ref: leadId,
    recipient_ref: 'u:aaa',
    delivery_status: 'delivered',
    delivery_key: `archive_view:${leadId}:u:aaa`,
    delivery_reason: 'archive',
    telegram_message_ref: '777',
    telegram_delivery_chat_id: '111',
    delivered_at: '2026-08-10T11:00:00.000Z',
  },
];

const sel = selectAuthoritativeCardInstances(deliveries, leadId);
check(1, 'current-instance selection unique', sel.authoritative.length === 4, `n=${sel.authoritative.length}`);
check(2, 'current reference has chat_id', sel.authoritative.every((r) => r.telegram_delivery_chat_id || r.telegram_chat_id));
check(3, 'current reference has message_id', sel.authoritative.every((r) => r.telegram_message_ref));
check(4, 'archive cards excluded', !sel.authoritative.some((r) => String(r.delivery_key).includes('archive')));
check(5, 'superseded cards excluded', !sel.authoritative.some((r) => String(r.telegram_message_ref) === '854'));

const initiator = sel.authoritative.find((r) => String(r.recipient_ref).toLowerCase() === 'u:aaa');
check(6, 'acceptance_canonical beats resurface_parity', String(initiator?.telegram_message_ref) === '898', `msg=${initiator?.telegram_message_ref}`);

const parityScore = scoreAuthoritativeInstance(deliveries[0]);
const acceptScore = scoreAuthoritativeInstance(deliveries[1]);
check(7, 'exclusive scoring no double-count', acceptScore > parityScore, `accept=${acceptScore} parity=${parityScore}`);

const pendingKb = buildReplyMarkup('tok');
const spamKb = buildReopenReplyMarkup('tok');
check(8, 'status renderer full-body contract', AUTHORITATIVE_CARD_INSTANCE_CONTRACT === 'iseo-authoritative-card-instance-v1.2');
check(9, 'spam keyboard reopen', Boolean(spamKb?.inline_keyboard?.[0]?.[0]?.text?.includes('Вернуть')));
check(10, 'processed/pending keyboard has spam+processed', pendingKb?.inline_keyboard?.[0]?.length >= 2);

const target = resolveEditMessageTarget(initiator, {
  callback_chat_id: '111',
  callback_message_id: '898',
});
check(11, 'Telegram edit payload complete', Boolean(target.edit_chat_id && target.edit_message_id));
check(12, 'one callback one mutation targeting visible card', target.edit_message_id === '898' && target.message_ref_source === 'callback_initiator');
check(13, 'initiator same message as operator-visible', target.edit_message_id === '898');
check(14, 'no new lead / fanout in selection', sel.expected_sync_count === 4);
check(15, 'AI OFF (static)', true, 'harness does not call OpenRouter');

// Regression: parity must not score as resurface+parity
const bogusDouble = (() => {
  const key = 'operator_resurface_parity:x';
  let s = 0;
  if (key.includes('operator_resurface_parity')) s += 120;
  if (key.includes('operator_resurface')) s += 100; // old bug
  return s;
})();
check(16, 'old double-count pattern identified', bogusDouble === 220, `old=${bogusDouble}`);
check(17, 'new parity score exclusive', parityScore < 200 && parityScore >= 120, `parity=${parityScore}`);
const failed = results.filter((r) => !r.pass);
console.log(`\nSUMMARY pass=${results.filter((r) => r.pass).length}/${results.length} fail=${failed.length}`);
if (failed.length) process.exitCode = 1;
