// Phase 3E.2.1 — OPS Expand Delivery Recipients (runOnceForAllItems)
// Fail-closed ledger read. Claim-before-send. Secondary CONFIG tg_delivered guards.
// Deterministic delivery_key = lead_delivery:<stable_lead_ref>:<opaque_recipient_ref>
// Never treat Sheets error objects as empty ledger → never blind-resend.

function sha256hex(ascii) {
  const mathPow = Math.pow;
  const maxWord = mathPow(2, 32);
  const lengthProperty = 'length';
  let i, j;
  let result = '';
  const words = [];
  const asciiBitLength = ascii[lengthProperty] * 8;
  let hash = (sha256hex.h = sha256hex.h || []);
  const k = (sha256hex.k = sha256hex.k || []);
  let primeCounter = k[lengthProperty];
  const isComposite = {};
  for (let candidate = 2; primeCounter < 64; candidate++) {
    if (!isComposite[candidate]) {
      for (i = 0; i < 313; i += candidate) isComposite[i] = candidate;
      hash[primeCounter] = (mathPow(candidate, 0.5) * maxWord) | 0;
      k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
    }
  }
  ascii += '\x80';
  while ((ascii[lengthProperty] % 64) - 56) ascii += '\x00';
  for (i = 0; i < ascii[lengthProperty]; i++) {
    j = ascii.charCodeAt(i);
    if (j >> 8) return '';
    words[i >> 2] |= j << (((3 - i) % 4) * 8);
  }
  words[words[lengthProperty]] = (asciiBitLength / maxWord) | 0;
  words[words[lengthProperty]] = asciiBitLength;
  for (j = 0; j < words[lengthProperty]; ) {
    const w = words.slice(j, (j += 16));
    const oldHash = hash;
    hash = hash.slice(0, 8);
    for (i = 0; i < 64; i++) {
      const w15 = w[i - 15];
      const w2 = w[i - 2];
      const a = hash[0];
      const e = hash[4];
      const temp1 =
        hash[7] +
        (((e >>> 6) | (e << 26)) ^ ((e >>> 11) | (e << 21)) ^ ((e >>> 25) | (e << 7))) +
        ((e & hash[5]) ^ (~e & hash[6])) +
        k[i] +
        (w[i] =
          i < 16
            ? w[i]
            : (w[i - 16] +
                (((w15 >>> 7) | (w15 << 25)) ^ ((w15 >>> 18) | (w15 << 14)) ^ (w15 >>> 3)) +
                w[i - 7] +
                (((w2 >>> 17) | (w2 << 15)) ^ ((w2 >>> 19) | (w2 << 13)) ^ (w2 >>> 10))) |
              0);
      const temp2 =
        (((a >>> 2) | (a << 30)) ^ ((a >>> 13) | (a << 19)) ^ ((a >>> 22) | (a << 10))) +
        ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
      hash = [(temp1 + temp2) | 0].concat(hash);
      hash[4] = (hash[4] + temp1) | 0;
      hash.pop();
    }
    for (i = 0; i < 8; i++) hash[i] = (hash[i] + oldHash[i]) | 0;
  }
  for (i = 0; i < 8; i++) {
    for (j = 3; j + 1; j--) {
      const b = (hash[i] >> (j * 8)) & 255;
      result += (b < 16 ? '0' : '') + b.toString(16);
    }
  }
  return result;
}
function idHash(v) { return sha256hex(String(v || '')).slice(0, 16).toUpperCase(); }
function opaqueUserRef(userId) { return 'u:' + idHash(userId).slice(0, 12); }
function deliveryKey(leadRef, recipientRef) { return 'lead_delivery:' + leadRef + ':' + recipientRef; }
function isValidPrivateChatTarget(userId) {
  const s = String(userId || '').trim();
  return /^-?\d{5,20}$/.test(s) && s !== '0' && s !== '44';
}
function parseBool(v, d = null) {
  if (v === true || v === 'true' || v === '1' || v === 1) return true;
  if (v === false || v === 'false' || v === '0' || v === 0) return false;
  return d;
}
function parseTs(v) {
  const t = Date.parse(String(v || ''));
  return Number.isFinite(t) ? t : 0;
}
function isSheetsErrorItem(row) {
  if (!row || typeof row !== 'object') return true;
  if (row.error || row.errors) return true;
  const msg = String(row.message || row.description || row.name || '');
  if (/too many requests|quota|rate.?limit|RESOURCE_EXHAUSTED|429|service is receiving/i.test(msg)) return true;
  // n8n continueOnFail error-shaped objects often lack delivery_key and have only error metadata
  if (row.code && !row.delivery_key && !row.telegram_user_id && !row.stable_lead_ref) return true;
  return false;
}

const MAX_RETRY = 5;

let lead = {};
try { lead = $('Format Telegram Lead Card').first().json || {}; } catch (e) { lead = $input.first().json || {}; }

// --- Fail-closed ledger read ---
let ledger_read_ok = false;
let ledger_read_error = false;
let ledger_read_error_code = '';
let priorRows = [];
try {
  const rawLed = $('Read LEAD_DELIVERIES').all().map((i) => i.json);
  const errors = rawLed.filter(isSheetsErrorItem);
  const usable = rawLed.filter((r) => r && !isSheetsErrorItem(r) && (r.delivery_key || r.stable_lead_ref || r.recipient_ref));
  if (errors.length && !usable.length) {
    ledger_read_ok = false;
    ledger_read_error = true;
    ledger_read_error_code = 'ledger_read_quota_or_error';
    priorRows = [];
  } else if (errors.length && usable.length) {
    // Mixed batch: keep usable rows, but do not treat error items as empty gaps for those keys
    ledger_read_ok = true;
    ledger_read_error = false;
    priorRows = usable;
  } else {
    ledger_read_ok = true;
    ledger_read_error = false;
    priorRows = usable;
  }
} catch (e) {
  ledger_read_ok = false;
  ledger_read_error = true;
  ledger_read_error_code = 'ledger_read_exception';
  priorRows = [];
}

const accessRaw = $input.all().map((i) => i.json);
const accessErrors = accessRaw.filter(isSheetsErrorItem);
const accessRows = accessRaw.filter((r) => r && r.telegram_user_id && !isSheetsErrorItem(r));

// ACCESS_CONTROL read failure → fail closed (no recipients) rather than inventing targets
if (accessErrors.length && !accessRows.length) {
  return [{
    json: {
      ...lead,
      stable_lead_ref: String(lead.lead_id || lead.stable_lead_ref || '').trim(),
      skip_telegram: true,
      force_telegram_fail: true,
      __expect_telegram_send: false,
      delivery_status: 'failed_retryable',
      error_code: 'access_control_read_error',
      error_stage: 'delivery_expand',
      ledger_read_ok,
      ledger_read_error,
      reconciliation_required: true,
      claim_before_send: true,
      recipient_count: 0,
      delivery_results_empty: true,
    },
  }];
}

if (ledger_read_error) {
  return [{
    json: {
      ...lead,
      stable_lead_ref: String(lead.lead_id || lead.stable_lead_ref || '').trim(),
      skip_telegram: true,
      force_telegram_fail: true,
      __expect_telegram_send: false,
      delivery_status: 'failed_retryable',
      error_code: ledger_read_error_code || 'ledger_read_error',
      error_stage: 'delivery_expand',
      ledger_read_ok: false,
      ledger_read_error: true,
      reconciliation_required: true,
      claim_before_send: true,
      recipient_count: 0,
      delivery_results_empty: true,
      // zero cards — fail closed
    },
  }];
}

const seen = new Set();
const recipients = [];
const ineligible = [];

for (const raw of accessRows) {
  const role = String(raw.role || '').trim().toLowerCase();
  const status = String(raw.status || '').trim().toLowerCase();
  const uid = String(raw.telegram_user_id || '').trim();
  if (!uid) { ineligible.push({ reason: 'malformed' }); continue; }
  if (seen.has(uid)) { ineligible.push({ reason: 'duplicate_identity' }); continue; }
  if (status === 'pending' || status === 'revoked' || status === 'blocked' || role === 'public') {
    ineligible.push({ reason: status === 'pending' || status === 'revoked' || status === 'blocked' ? status : 'public' });
    continue;
  }
  if (!((role === 'admin' || role === 'moderator') && status === 'active')) {
    ineligible.push({ reason: 'not_active_staff' });
    continue;
  }
  const privateOk = isValidPrivateChatTarget(uid) && Boolean(String(raw.last_seen_at || raw.first_seen_at || raw.approved_at || '').trim());
  const explicitPrivate = parseBool(raw.telegram_private_chat_available, null);
  const chatOk = explicitPrivate === null ? privateOk : explicitPrivate;
  const explicitEnabled = parseBool(raw.lead_delivery_enabled, null);
  let enabled = explicitEnabled === null ? (chatOk) : explicitEnabled;
  if (!chatOk) enabled = false;
  if (!enabled) { ineligible.push({ reason: chatOk ? 'delivery_disabled' : 'missing_private_chat' }); continue; }
  seen.add(uid);
  recipients.push({
    telegram_delivery_chat_id: uid,
    recipient_ref: opaqueUserRef(uid),
    recipient_role: role,
    is_admin_anchor: role === 'admin',
  });
}

recipients.sort((a, b) => (a.is_admin_anchor === b.is_admin_anchor ? a.recipient_ref.localeCompare(b.recipient_ref) : (a.is_admin_anchor ? -1 : 1)));

const stable = String(lead.lead_id || lead.stable_lead_ref || '').trim();
const gid = String(lead.gmail_message_id || '').trim();
const cfg = lead.config || {};
const now = new Date().toISOString();
const priorMap = new Map();
for (const d of priorRows) {
  const dStable = String(d.stable_lead_ref || '').trim();
  const key = String(d.delivery_key || '').trim() || deliveryKey(dStable, d.recipient_ref);
  if (!key || !stable) continue;
  if (dStable && dStable !== stable) continue;
  if (!key.includes(stable) && dStable !== stable) continue;
  const prev = priorMap.get(key);
  const prevTs = Math.max(parseTs(prev?.updated_at), parseTs(prev?.last_attempt_at), parseTs(prev?.delivered_at));
  const curTs = Math.max(parseTs(d.updated_at), parseTs(d.last_attempt_at), parseTs(d.delivered_at));
  if (!prev || curTs >= prevTs) priorMap.set(key, { ...d, delivery_key: key });
}

const businessAlready =
  lead.telegram_already_delivered === true ||
  (lead.skip_telegram === true && String(lead.delivery_status || '') === 'delivered') ||
  (String(lead.duplicate_status || '') === 'reprocessed' && String(lead.delivery_status || '') === 'delivered') ||
  (gid && Boolean(String(cfg['tg_delivered:' + gid] || cfg['telegram_delivered:' + gid] || '').trim()));

const allDeliveredInLedger = recipients.length > 0 && recipients.every((r) => {
  const prev = priorMap.get(deliveryKey(stable, r.recipient_ref));
  return String(prev?.delivery_status || '') === 'delivered';
});

if (!recipients.length) {
  return [{
    json: {
      ...lead,
      stable_lead_ref: stable,
      skip_telegram: true,
      force_telegram_fail: true,
      __expect_telegram_send: false,
      delivery_status: 'failed_terminal',
      error_code: 'no_delivery_recipients',
      error_stage: 'delivery_expand',
      recipient_count: 0,
      ineligible_count: ineligible.length,
      is_admin_anchor: false,
      delivery_results_empty: true,
      claim_before_send: true,
      ledger_read_ok: true,
      ledger_read_error: false,
    },
  }];
}

const out = [];
for (const r of recipients) {
  const key = deliveryKey(stable, r.recipient_ref);
  const prev = priorMap.get(key);
  const prevStatus = String(prev?.delivery_status || '');
  const attempts = Number(prev?.attempt_number || 0);
  const fallbackKey = 'tg_delivered:' + stable + ':' + r.recipient_ref;
  const fallbackHit = Boolean(String(cfg[fallbackKey] || '').trim())
    || (gid && Boolean(String(cfg['tg_delivered:' + gid + ':' + r.recipient_ref] || '').trim()));

  let delivery_status = 'planned';
  let skip_telegram = false;
  let __expect_telegram_send = true;
  let attempt_number = attempts + 1;
  let error_code = '';
  let claim_action = 'claim';
  let reconciliation_required = false;

  if (businessAlready || allDeliveredInLedger || prevStatus === 'delivered' || fallbackHit) {
    delivery_status = 'delivered';
    skip_telegram = true;
    __expect_telegram_send = false;
    attempt_number = Math.max(attempts, 1);
    claim_action = fallbackHit && prevStatus !== 'delivered' ? 'noop_fallback_delivered' : 'noop_delivered';
  } else if (prevStatus === 'failed_terminal' || attempts >= MAX_RETRY) {
    delivery_status = 'failed_terminal';
    skip_telegram = true;
    __expect_telegram_send = false;
    attempt_number = attempts;
    error_code = prev?.error_code || 'telegram_retry_exhausted';
    claim_action = 'noop_terminal';
  } else if (prevStatus === 'skipped_ineligible') {
    delivery_status = 'skipped_ineligible';
    skip_telegram = true;
    __expect_telegram_send = false;
    attempt_number = attempts;
    claim_action = 'noop_skipped';
  } else if (prevStatus === 'claimed' || prevStatus === 'reconciliation_required' || prevStatus === 'uncertain') {
    // Do NOT blind-resend. Successful Telegram without durable stamp must be reconciled.
    delivery_status = 'reconciliation_required';
    skip_telegram = true;
    __expect_telegram_send = false;
    attempt_number = attempts;
    error_code = 'claimed_or_uncertain_needs_reconcile';
    claim_action = 'block_reconcile';
    reconciliation_required = true;
  } else if (prevStatus === 'failed_retryable') {
    delivery_status = 'planned';
    skip_telegram = false;
    __expect_telegram_send = true;
    attempt_number = attempts + 1;
    claim_action = 'retry_claim';
  } else {
    delivery_status = 'planned';
    skip_telegram = false;
    __expect_telegram_send = true;
    claim_action = 'claim';
  }

  out.push({
    json: {
      ...lead,
      stable_lead_ref: stable,
      recipient_ref: r.recipient_ref,
      recipient_role: r.recipient_role,
      is_admin_anchor: !!r.is_admin_anchor,
      telegram_delivery_chat_id: String(r.telegram_delivery_chat_id),
      telegram_chat_id: String(r.telegram_delivery_chat_id),
      delivery_channel: 'telegram_private',
      delivery_key: key,
      delivery_status,
      attempt_number,
      skip_telegram,
      __expect_telegram_send,
      lifecycle_status_at_send: String(lead.manager_status || 'pending'),
      card_version: String(lead.message_format_version || 'sm-msg-v2.4'),
      delivery_timestamp: now,
      last_attempt_at: now,
      updated_at: now,
      delivered_at: delivery_status === 'delivered' ? (prev?.delivered_at || now) : (prev?.delivered_at || ''),
      telegram_message_ref: prev?.telegram_message_ref || '',
      error_code,
      recipient_count: recipients.length,
      ineligible_count: ineligible.length,
      multi_recipient_delivery: true,
      claim_before_send: true,
      claim_action,
      business_already_delivered: !!(businessAlready || allDeliveredInLedger || fallbackHit),
      ledger_read_ok: true,
      ledger_read_error: false,
      reconciliation_required,
      config_fallback_key: fallbackKey,
    },
  });
}

return out;
