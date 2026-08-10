/**
 * iseo-canonical-lead-card-renderer-v1
 *
 * ONE human-facing lead card renderer for:
 * - normal production intake
 * - operator_resurface of an existing lead
 *
 * Internal delivery_reason must NOT alter human-facing card structure.
 */
import {
  formatLeadCard,
  buildReplyMarkup,
  buildReopenReplyMarkup,
  isValidContactValue,
  MESSAGE_FORMAT_VERSION,
} from './formatter-lib.mjs';
import { routeApprovedTemplate } from './approved-template-router-v1.mjs';
import { renderApprovedReply } from './approved-template-renderer-v1.mjs';
import { resolveRecipientReplyProfile } from './reply-profile-lib.mjs';

export const CANONICAL_LEAD_CARD_RENDERER_CONTRACT = 'iseo-canonical-lead-card-renderer-v1';
export const CARD_INSTANCE_REGISTRY_CONTRACT = 'iseo-lead-card-instance-registry-v1';
/** Phase 3H.7.3.1 — authoritative current-card selection. */
export const AUTHORITATIVE_CARD_INSTANCE_CONTRACT = 'iseo-authoritative-card-instance-v1.1';

const FORMULA_ERROR_RE = /#ERROR!|#N\/A|#VALUE!|#REF!|^#\w+!/i;

/**
 * Strip spreadsheet formula-error tokens from contact-like fields.
 * Never present #ERROR! as customer contact.
 */
export function sanitizeContactField(value) {
  const v = String(value ?? '').trim();
  if (!v) return '';
  if (FORMULA_ERROR_RE.test(v)) return '';
  if (!isValidContactValue(v)) return '';
  return v;
}

/**
 * Map authoritative LEADS / lead_clean row into formatter-ready lead object.
 * Prefer canonical LEADS phone/email over derived primary_contact.
 */
export function normalizeLeadForCanonicalCard(raw = {}, { managerStatus = 'pending' } = {}) {
  const phone = sanitizeContactField(raw.phone || raw.phone_normalized);
  const email = sanitizeContactField(raw.email || raw.email_normalized);
  const messenger = sanitizeContactField(raw.messenger || raw.telegram_contact_normalized);
  // Never fall back to primary_contact when it is a formula error.
  const primary = sanitizeContactField(raw.primary_contact);
  const contactType = String(raw.contact_type || '').trim().toLowerCase();

  let resolvedPhone = phone;
  let resolvedEmail = email;
  let resolvedMessenger = messenger;
  if (!resolvedPhone && !resolvedEmail && !resolvedMessenger && primary) {
    if (contactType === 'email' || primary.includes('@')) resolvedEmail = primary;
    else if (contactType === 'telegram' || contactType === 'messenger' || primary.startsWith('@')) {
      resolvedMessenger = primary;
    } else resolvedPhone = primary;
  }

  const site = String(raw.website || raw.site || raw.website_normalized || '').trim();
  const clientName = String(raw.client_name || raw.client_name_normalized || '').trim();

  return {
    ...raw,
    lead_id: String(raw.lead_id || raw.stable_lead_ref || '').trim(),
    client_name: clientName,
    phone: resolvedPhone,
    email: resolvedEmail,
    messenger: resolvedMessenger,
    // Keep primary_contact sanitized so no renderer can leak formula errors.
    primary_contact: sanitizeContactField(raw.primary_contact),
    site,
    website: site,
    website_normalized: site,
    service: raw.resolved_service_code || raw.resolved_service || raw.service || '',
    resolved_service: raw.resolved_service_code || raw.resolved_service || raw.service || '',
    resolved_service_label: raw.resolved_service_label || raw.service_label || '',
    comment_normalized: String(raw.client_comment || raw.comment_normalized || raw.summary || '').trim(),
    request_summary: String(raw.request_summary || raw.summary || '').trim(),
    manager_status: managerStatus,
    duplicate_status: raw.duplicate_status || 'new',
    message_format_version: MESSAGE_FORMAT_VERSION,
    delivery_reason: raw.delivery_reason || '',
  };
}

/**
 * Build personalized production-parity card for one recipient.
 * deliveryReason is internal metadata only — never shown in card text.
 */
export function renderCanonicalLeadCard({
  lead,
  recipientProfile,
  managerStatus = 'pending',
  deliveryReason = '',
} = {}) {
  const normalized = normalizeLeadForCanonicalCard(lead, { managerStatus });
  const profile = resolveRecipientReplyProfile(recipientProfile || {});

  const routing = routeApprovedTemplate(normalized);
  const rendered = renderApprovedReply({
    leadContext: normalized,
    route: routing,
    recipientProfileRow: recipientProfile || {},
  });

  const cardInput = {
    ...normalized,
    manager_status: managerStatus,
    personalized_reply_text: rendered.customer_reply_text || '',
    first_reply_text: rendered.customer_reply_text || '',
    first_reply_ready: Boolean(rendered.customer_reply_text),
    first_reply_source: rendered.customer_reply_text ? 'approved_template' : (normalized.first_reply_source || 'none'),
    manager_guidance_text: rendered.manager_guidance || '',
    recipient_reply_state: rendered.recipient_reply_state || profile.recipient_reply_state || '',
    selected_template_id: routing.selected_template_id,
    // Explicitly do NOT pass human aliases / delivery reason into visible fields.
    delivery_reason: deliveryReason || normalized.delivery_reason || '',
  };

  const card = formatLeadCard(cardInput);
  const text = String(card.telegram_text || '');

  // Hard guard: no internal markers in human-facing text
  const forbidden = [
    'operator resurface',
    'operator_resurface',
    'REAL_REOPEN_A',
    'REAL_REOPEN_B',
    'REAL_REOPEN_C',
    'delivery_reason',
  ];
  for (const f of forbidden) {
    if (text.toLowerCase().includes(f.toLowerCase())) {
      throw new Error(`canonical_renderer_leaked_internal_marker:${f}`);
    }
  }
  if (/#ERROR!|#N\/A|#VALUE!|#REF!/i.test(text)) {
    throw new Error('canonical_renderer_leaked_formula_error');
  }

  const status = String(managerStatus || 'pending').toLowerCase();
  const token = card.telegram_action_token;
  let markup = card.telegram_reply_markup;
  if (status === 'spam' || status === 'processed') {
    markup = buildReopenReplyMarkup(token);
  } else {
    markup = buildReplyMarkup(token);
  }

  return {
    contract: CANONICAL_LEAD_CARD_RENDERER_CONTRACT,
    lead_id: normalized.lead_id,
    manager_status: status,
    delivery_reason: deliveryReason || '',
    selected_template_id: routing.selected_template_id,
    reply_sender_name: profile.reply_sender_name || '',
    telegram_text: text,
    telegram_reply_markup: markup,
    telegram_callback_processed: 'sm:p:' + token,
    telegram_callback_spam: 'sm:s:' + token,
    telegram_callback_reopen: 'sm:r:' + token,
    telegram_action_token: token,
    card_version: MESSAGE_FORMAT_VERSION,
    human_visible_internal_markers: 0,
  };
}

/**
 * Normalize recipient identity for authoritative selection.
 * Case-fold recipient_ref so u:ABC and u:abc collapse to one slot.
 */
export function normalizeRecipientKey(r = {}) {
  const ref = String(r.recipient_ref || '').trim().toLowerCase();
  if (ref) return ref;
  const chat = String(r.telegram_delivery_chat_id || r.telegram_chat_id || '').trim();
  return chat ? `chat:${chat}` : '';
}

/**
 * Append status-transition attribution WITHOUT collapsing canonical body.
 */
export function appendStatusAttribution(telegramText, {
  managerStatus = 'pending',
  actorLabelHtml = '',
  whenMoscow = '',
} = {}) {
  const base = String(telegramText || '').trimEnd();
  const status = String(managerStatus || 'pending').toLowerCase();
  const when = String(whenMoscow || '').trim();
  const actor = String(actorLabelHtml || '').trim();
  const lines = [];
  if (status === 'spam' || status === 'processed') {
    if (actor) lines.push('Кем: ' + actor);
    if (when) lines.push('Время: ' + when);
  } else if (actor) {
    lines.push('Возвращено в обработку: ' + actor);
    if (when) lines.push('Время: ' + when);
  }
  if (!lines.length) return base;
  return (base + '\n\n' + lines.join('\n')).trimEnd();
}

/**
 * Select authoritative current card instances for status sync.
 * Contract: iseo-authoritative-card-instance-v1.1
 * Exactly one current instance per recipient. Superseded excluded from sync accounting.
 * After explicit operator resurface / parity repair, newer canonical cards win.
 * Stale callbacks must not promote superseded messages back to authoritative.
 */
export function selectAuthoritativeCardInstances(deliveries = [], leadId) {
  const lid = String(leadId || '');
  const rows = (deliveries || []).filter((r) => {
    if (String(r.stable_lead_ref || r.lead_id || '') !== lid) return false;
    if (String(r.delivery_status || '') !== 'delivered') return false;
    if (!r.telegram_message_ref) return false;
    if (!(r.telegram_delivery_chat_id || r.telegram_chat_id)) return false;
    if (String(r.card_instance_state || '').toLowerCase() === 'superseded') return false;
    if (String(r.active_sync || '').toLowerCase() === 'false') return false;
    return true;
  });

  const byRecipient = new Map();
  for (const r of rows) {
    const key = normalizeRecipientKey(r);
    if (!key) continue;
    const prev = byRecipient.get(key);
    if (!prev) {
      byRecipient.set(key, r);
      continue;
    }
    byRecipient.set(key, preferAuthoritativeInstance(prev, r));
  }

  const authoritative = [...byRecipient.values()].map((r) => ({
    ...r,
    card_instance_state: 'authoritative',
    active_sync: 'true',
  }));
  const authKeys = new Set(authoritative.map((r) => String(r.delivery_key || `${r.recipient_ref}:${r.telegram_message_ref}`)));
  const superseded = rows
    .filter((r) => !authKeys.has(String(r.delivery_key || `${r.recipient_ref}:${r.telegram_message_ref}`)))
    .map((r) => ({ ...r, card_instance_state: 'superseded', active_sync: 'false' }));

  return {
    contract: AUTHORITATIVE_CARD_INSTANCE_CONTRACT,
    registry_contract: CARD_INSTANCE_REGISTRY_CONTRACT,
    lead_id: lid,
    authoritative,
    superseded,
    expected_sync_count: authoritative.length,
  };
}

function preferAuthoritativeInstance(a, b) {
  const score = (r) => {
    let s = 0;
    const key = String(r.delivery_key || '');
    const reason = String(r.delivery_reason || '').toLowerCase();
    const state = String(r.card_instance_state || '').toLowerCase();
    // Explicit parity / resurface / acceptance-canonicalization beats historical initial.
    if (key.includes('acceptance_canonical') || reason.includes('acceptance_canonical')) s += 140;
    if (key.includes('operator_resurface_parity') || reason === 'operator_resurface_parity') s += 120;
    if (reason === 'operator_resurface' || key.includes('operator_resurface')) s += 100;
    if (state === 'authoritative') s += 50;
    if (state === 'current') s += 40;
    if (state === 'superseded') s -= 1000;
    // Prefer rows that still have a usable chat id (syncable).
    if (r.telegram_delivery_chat_id || r.telegram_chat_id) s += 20;
    const ts = Date.parse(String(r.delivered_at || r.delivery_timestamp || r.updated_at || '')) || 0;
    s += ts / 1e13;
    return s;
  };
  return score(b) >= score(a) ? b : a;
}

/**
 * Full canonical card for callback status sync (pending/spam/processed).
 * Never use a reduced status-only body for authoritative current cards.
 */
export function renderCanonicalStatusCard({
  lead,
  recipientProfile,
  managerStatus = 'pending',
  actorLabelHtml = '',
  whenMoscow = '',
  deliveryReason = 'status_sync',
} = {}) {
  const rendered = renderCanonicalLeadCard({
    lead,
    recipientProfile,
    managerStatus,
    deliveryReason,
  });
  const telegram_text = appendStatusAttribution(rendered.telegram_text, {
    managerStatus,
    actorLabelHtml,
    whenMoscow,
  });
  return {
    ...rendered,
    telegram_text,
    authoritative_instance_contract: AUTHORITATIVE_CARD_INSTANCE_CONTRACT,
  };
}
