// Phase 3D.8.2 — Handle Callback Action (actor attribution)
// Lead token: FNV dual-hash (sync with OPS Format). Actor refs: sha256.
/**
 * Pure JS SHA-256 (hex lowercase). n8n task-runner disallows the Node crypto module.
 */
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

function computeActionToken(leadId) {
  // Phase 3F.2 canonical: dual-FNV fnvToken (synced OPS Format ↔ Admin Handle).
  // Never use Node crypto/sha256 — n8n task-runner disallows it and previously
  // caused Admin/OPS divergence when one side fell back and the other did not.
  return fnvToken(String(leadId || ''));
}

function fnvToken(s) {
  const str = String(s || '');
  let h1 = 0x811c9dc5 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h1 ^= str.charCodeAt(i);
    h1 = Math.imul(h1, 0x01000193);
  }
  let h2 = 0x9e3779b9 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h2 ^= str.charCodeAt(i);
    h2 = Math.imul(h2, 0x85ebca6b);
    h2 = (h2 << 13) | (h2 >>> 19);
  }
  const hex1 = (h1 >>> 0).toString(16).padStart(8, '0');
  const hex2 = (h2 >>> 0).toString(16).padStart(8, '0');
  return (hex1 + hex2).slice(0, 12);
}


function actorHash(userId) {
  return 'u:' + sha256hex('actor:' + String(userId || '')).slice(0, 12);
}

function esc(s) {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function fmtMoscow(v) {
  const d = v ? new Date(v) : new Date();
  if (Number.isNaN(d.getTime())) return '—';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return get('day') + '.' + get('month') + '.' + get('year') + ' ' + get('hour') + ':' + get('minute') + ' МСК';
}

function codeField(label, value) {
  const v = String(value ?? '').trim();
  if (!v) return '';
  const lower = v.toLowerCase();
  if (['unknown', '44', '#error!', '#value!', '#ref!', '#n/a', 'n/a', 'na', '-', '—', 'null', 'undefined'].includes(lower)) {
    return '';
  }
  if (/#error!|#value!|#ref!|#n\/a|formula\s*parse\s*error|^#\w+!/i.test(v)) return '';
  return label + '\n<code>' + esc(v) + '</code>\n';
}

function normalizeDisplayName(s) {
  return String(s ?? '').trim().replace(/\s+/g, ' ').slice(0, 80);
}

function normalizeUsernameLabel(u) {
  let s = String(u ?? '').trim();
  if (!s || s === '@' || s === '—' || s.toLowerCase() === 'n/a') return '';
  if (!s.startsWith('@')) s = '@' + s;
  s = s.replace(/^@+/, '@');
  if (s.length < 2) return '';
  return s.slice(0, 40);
}

/** ACCESS_CONTROL fields only — never callback profile names. */
function buildSafeActorLabel(displayName, username) {
  const dn = normalizeDisplayName(displayName);
  const un = normalizeUsernameLabel(username);
  let label = '';
  if (dn && un) {
    const dnBare = dn.replace(/^@/, '').toLowerCase();
    const unBare = un.replace(/^@/, '').toLowerCase();
    label = dnBare === unBare ? (dn.startsWith('@') ? dn : un) : (dn + ' · ' + un);
  } else if (dn) {
    label = dn;
  } else if (un) {
    label = un;
  } else {
    label = 'сотрудник';
  }
  if (label.length > 64) label = label.slice(0, 63) + '…';
  return label;
}

function buildActionButtons(token) {
  return {
    inline_keyboard: [
      [
        { text: '✅ Обработано', callback_data: 'sm:p:' + token },
        { text: '🚫 Спам', callback_data: 'sm:s:' + token },
      ],
      [
        { text: '📄 Исходная заявка', callback_data: 'sm:i:' + token },
      ],
    ],
  };
}

function buildReopenButtons(token) {
  return {
    inline_keyboard: [
      [
        { text: '↩️ Вернуть в обработку', callback_data: 'sm:r:' + token },
      ],
      [
        { text: '📄 Исходная заявка', callback_data: 'sm:i:' + token },
      ],
    ],
  };
}



var LITERAL_RAW_CONTRACT = 'iseo-literal-raw-source-v1.0';
var TELEGRAM_HARD_LIMIT = 4096;
var TITLE = '📄 Исходная заявка';
var TITLE_CONT = '📄 Исходная заявка — продолжение';
var EMPTY_COPY = 'В исходном письме нет содержимого заявки.';
var MISSING_COPY = 'Исходная заявка для этого лида не найдена.';
var TRANSIENT_COPY = 'Исходную заявку сейчас не удалось прочитать. Попробуйте ещё раз через минуту.';

function rsEsc(s) {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
function decodeHtmlEntities(s) {
  return String(s || '')
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;|&apos;/gi, "'")
    .replace(/&#x([0-9a-f]+);/gi, function (_, h) {
      const n = parseInt(h, 16);
      return n ? String.fromCharCode(n) : _;
    })
    .replace(/&#(\d+);/g, function (_, d) {
      const n = parseInt(d, 10);
      return n ? String.fromCharCode(n) : _;
    });
}
function htmlToReadableText(input) {
  var s = String(input || '');
  if (!/<\/?[a-z][\s\S]*>/i.test(s)) return s;
  s = s.replace(/<script\b[\s\S]*?<\/script>/gi, ' ');
  s = s.replace(/<style\b[\s\S]*?<\/style>/gi, ' ');
  s = s.replace(/<head\b[\s\S]*?<\/head>/gi, ' ');
  s = s.replace(/<!--[\s\S]*?-->/g, ' ');
  s = s.replace(/<img\b[^>]*>/gi, ' ');
  s = s.replace(/<br\s*\/?>/gi, '\n');
  s = s.replace(/<\/(p|div|tr|li|h[1-6]|blockquote|table|section|article|header|footer)>/gi, '\n');
  s = s.replace(/<(p|div|tr|li|h[1-6]|blockquote|br|hr)\b[^>]*>/gi, '\n');
  s = s.replace(/<\/td>/gi, ' ');
  s = s.replace(/<hr\b[^>]*>/gi, '\n');
  s = s.replace(/<[^>]+>/g, ' ');
  s = decodeHtmlEntities(s);
  return s;
}
function stripTransportAndInternal(s) {
  var t = String(s || '');
  t = t.replace(/^\s*(?:From|To|Cc|Bcc|Subject|Date|MIME-Version|Content-Type|Content-Transfer-Encoding)\s*:[^\n]*\n/gim, '');
  t = t.replace(/\b(?:Message-ID|X-Mailer|Return-Path|Received|DKIM-Signature|X-Google-.*)\s*[:：][^\n]*/ig, '');
  t = t.replace(/https?:\/\/(?:ci[0-9]\.googleusercontent|mail\.google|n8n\.)\S+/ig, '');
  t = t.replace(/\b(?:gmail_message_id|n8n|workflow|execution)[_ :][A-Za-z0-9._-]*/ig, '');
  t = t.replace(/\bIP\s*[:：]\s*\S+/ig, '');
  t = t.replace(/\b(?:\d{1,3}\.){3}\d{1,3}\b/g, '');
  return t;
}
function normalizeLiteralWhitespace(s) {
  var t = String(s || '').replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  t = t.replace(/[ \t]+\n/g, '\n');
  t = t.replace(/\n{4,}/g, '\n\n\n');
  t = t.replace(/[ \t]{3,}/g, '  ');
  return t.replace(/^\s+|\s+$/g, '');
}
function pickAuthoritativeBody(rawRow) {
  const row = rawRow && typeof rawRow === 'object' ? rawRow : {};
  if (row.source_body_full != null && String(row.source_body_full).trim().length) {
    return { field: 'source_body_full', value: String(row.source_body_full) };
  }
  if (row.raw_text != null && String(row.raw_text).length) return { field: 'raw_text', value: String(row.raw_text) };
  if (row.raw_text != null) return { field: 'raw_text', value: String(row.raw_text) };
  return { field: 'raw_text', value: '' };
}
function hasAuthoritativeRecord(rawRow) {
  return Boolean(rawRow && typeof rawRow === 'object' && (
    rawRow.lead_id ||
    rawRow.gmail_message_id ||
    rawRow.raw_text != null ||
    rawRow.request_text != null
  ));
}
function cleanupLiteralBody(raw) {
  var t = String(raw || '');
  t = htmlToReadableText(t);
  t = stripTransportAndInternal(t);
  t = normalizeLiteralWhitespace(t);
  return t;
}
function chunkLiteralMessages(title, body, limit) {
  var max = limit || TELEGRAM_HARD_LIMIT;
  var chunks = [];
  var prefix1 = title + '\n\n';
  var prefix2 = TITLE_CONT + '\n\n';
  if (!body) {
    chunks.push(prefix1);
    return chunks;
  }
  var room1 = max - prefix1.length;
  if (body.length <= room1) {
    chunks.push(prefix1 + body);
    return chunks;
  }
  var first = body.slice(0, room1);
  var cut = first.lastIndexOf('\n');
  if (cut < room1 * 0.5) cut = first.lastIndexOf(' ');
  if (cut < room1 * 0.5) cut = room1;
  first = body.slice(0, cut).replace(/\s+$/g, '');
  var rest = body.slice(first.length).replace(/^\s+/g, '');
  chunks.push(prefix1 + first);
  while (rest && chunks.length < 8) {
    var room = max - prefix2.length;
    if (rest.length <= room) {
      chunks.push(prefix2 + rest);
      break;
    }
    var piece = rest.slice(0, room);
    var c2 = piece.lastIndexOf('\n');
    if (c2 < room * 0.5) c2 = piece.lastIndexOf(' ');
    if (c2 < room * 0.5) c2 = room;
    piece = rest.slice(0, c2).replace(/\s+$/g, '');
    chunks.push(prefix2 + piece);
    rest = rest.slice(piece.length).replace(/^\s+/g, '');
  }
  if (chunks.length > 2) chunks = chunks.slice(0, 2);
  return chunks;
}
function classifyLiteralSource(rawRow, rawReadFailed) {
  if (rawReadFailed) return { state: 'RAW_TRANSIENT_READ_FAILURE' };
  if (!hasAuthoritativeRecord(rawRow)) return { state: 'RAW_RECORD_NOT_FOUND' };
  var picked = pickAuthoritativeBody(rawRow);
  var cleaned = cleanupLiteralBody(picked.value);
  if (!cleaned) return { state: 'RAW_EMPTY_BODY', body: '', field: picked.field };
  return { state: 'RAW_LITERAL_AVAILABLE', body: cleaned, field: picked.field };
}
function buildLiteralRawResponse(rawRow, rawReadFailed) {
  var classified = classifyLiteralSource(rawRow, rawReadFailed);
  var answer = 'Исходная заявка';
  var eventType = 'manager_raw_source_viewed';
  var chunks = [];
  var customFieldLabelsUsed = false;
  if (classified.state === 'RAW_TRANSIENT_READ_FAILURE') {
    chunks = [TITLE + '\n\n' + TRANSIENT_COPY];
    answer = TRANSIENT_COPY;
    eventType = 'manager_raw_source_read_failure';
  } else if (classified.state === 'RAW_RECORD_NOT_FOUND') {
    chunks = [TITLE + '\n\n' + MISSING_COPY];
    answer = MISSING_COPY;
    eventType = 'manager_raw_source_not_found';
  } else if (classified.state === 'RAW_EMPTY_BODY') {
    chunks = [TITLE + '\n\n' + EMPTY_COPY];
    answer = EMPTY_COPY;
    eventType = 'manager_raw_source_empty';
  } else {
    chunks = chunkLiteralMessages(TITLE, classified.body, TELEGRAM_HARD_LIMIT);
    eventType = 'manager_raw_source_viewed';
  }
  var htmlChunks = chunks.map(function (c) { return rsEsc(c); });
  return {
    state: classified.state,
    contract: LITERAL_RAW_CONTRACT,
    source_field: classified.field || 'raw_text',
    custom_field_labels_used: customFieldLabelsUsed,
    html: htmlChunks[0] || rsEsc(TITLE),
    html_continued: htmlChunks[1] || '',
    chunks_html: htmlChunks,
    chunk_count: htmlChunks.length,
    answer_text: answer,
    event_type: eventType,
    body_len: classified.body ? classified.body.length : 0,
  };
}


function buildRawSourceHtml(rawRow) {
  return buildLiteralRawResponse(rawRow, false).html;
}
function buildRawSourceResponse(rawRow, lead, rawReadFailed) {
  return buildLiteralRawResponse(rawRow, rawReadFailed);
}

function buildCanonicalStatusCardText(lead, desired, when, actorLabelHtml) {
  // Phase 3H.7.3.1 — full canonical body for authoritative status sync.
  // Must NOT collapse to status-only reduced card.
  const escLocal = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const valid = (v) => {
    const s = String(v ?? '').trim();
    if (!s) return false;
    const lower = s.toLowerCase();
    if (['unknown', '44', '#error!', '#value!', '#ref!', '#n/a', 'n/a', 'na', '-', '—', 'null', 'undefined'].includes(lower)) return false;
    if (/#error!|#value!|#ref!|#n\/a|formula\s*parse\s*error|^#\w+!/i.test(s)) return false;
    return true;
  };
  const codeBlock = (label, value) => {
    if (!valid(value)) return '';
    return label + '\n<code>' + escLocal(value) + '</code>\n';
  };
  const status = desired === 'pending' ? 'pending' : (desired === 'processed' ? 'processed' : 'spam');
  const statusLine = status === 'pending'
    ? '🕓 Ожидает обработки'
    : (status === 'processed' ? '✅ Обработан' : '🚫 Спам');
  const dup = String(lead.duplicate_status || 'new').toLowerCase();
  const heading = dup === 'repeat'
    ? '🟡 Повторный лид'
    : (dup === 'possible' ? '🟠 Возможный повтор' : (dup === 'reprocessed' ? '🔵 Повторная обработка' : '🟢 Новый лид'));

  let text = heading + '\n' + statusLine + '\n\n';
  text += codeBlock('Клиент', lead.client_name || lead.client_name_normalized);
  text += codeBlock('Телефон', lead.phone || lead.phone_normalized);
  text += codeBlock('Email', lead.email || lead.email_normalized);
  if (valid(lead.messenger)) text += codeBlock('Telegram', lead.messenger);

  const site = lead.website_normalized || lead.site || lead.website || '';
  if (valid(site) && !/t\.me|telegram\.me/i.test(site)) text += codeBlock('Сайт', site);

  const interest = lead.resolved_service_label || lead.service_label || lead.service || lead.resolved_service || '';
  if (String(interest).trim()) text += 'Интерес: ' + escLocal(interest) + '\n';

  const comment = String(lead.client_comment || lead.comment_normalized || lead.summary || '').trim();
  if (comment) {
    text += '\nКомментарий клиента\n' + escLocal(comment.slice(0, 800)) + '\n';
  }

  const quality = lead.lead_quality_label
    || ({ sufficient: 'Данных достаточно', ok: 'Данных достаточно', needs_clarification: 'Нужны уточнения', needs_data: 'Нужны уточнения', insufficient: 'Недостаточно данных', bad: 'Недостаточно данных', poor: 'Недостаточно данных', unusable: 'Недостаточно данных', test: 'Тестовая заявка' }[String(lead.lead_quality || lead.quality_status || '').toLowerCase()] || '');
  if (quality) text += 'Качество: ' + escLocal(quality) + '\n';

  const missing = String(lead.missing_fields || lead.missing_information || '').trim();
  if (missing) {
    text += '\nНе хватает\n' + escLocal(missing) + '\n';
  }

  const nextStep = String(lead.next_step || lead.manager_recommendation || '').trim();
  if (nextStep) {
    text += '\nСледующий шаг\n' + escLocal(nextStep) + '\n';
  }

  const reply = String(lead.personalized_reply_text || lead.first_reply_text || '').trim();
  const guidance = String(lead.manager_guidance_text || lead.manager_guidance || '').trim();
  if (reply) {
    text += '\n✉️ Готовый первый ответ — нажмите, чтобы скопировать\n';
    text += '<pre>' + escLocal(reply) + '</pre>\n';
    text += 'Ответ клиенту автоматически не отправляется.\n';
    if (guidance) text += '\n' + escLocal(guidance) + '\n';
  } else {
    text += '\nЧерновик ответа не сформирован.\nОтвет клиенту автоматически не отправляется.\n';
  }

  // Status attribution — additive only; never replace body.
  if (status !== 'pending') {
    if (actorLabelHtml) text += '\nКем: ' + String(actorLabelHtml) + '\n';
    if (when) text += 'Время: ' + when + '\n';
  } else if (actorLabelHtml) {
    text += '\nВозвращено в обработку: ' + String(actorLabelHtml) + '\n';
    if (when) text += 'Время: ' + when + '\n';
  }

  text = text.replace(/\n{3,}/g, '\n\n').trimEnd();
  // Hard guards
  if (/REAL_REOPEN_|operator resurface|#ERROR!/i.test(text)) {
    text = text.replace(/REAL_REOPEN_[ABC]/gi, '').replace(/operator resurface/gi, '').replace(/#ERROR!/gi, '');
  }
  return text;
}

function buildFinalCard(lead, desired, when, actorLabelHtml) {
  return buildCanonicalStatusCardText(lead, desired, when, actorLabelHtml);
}

function buildLeadCardSnapshot(lead, desired, when, actorLabelHtml) {
  return {
    lead_id: String(lead.lead_id || ''),
    client_name: lead.client_name || '',
    phone: lead.phone || '',
    email: lead.email || '',
    messenger: lead.messenger || '',
    site: lead.site || lead.website_normalized || '',
    website_normalized: lead.website_normalized || lead.site || '',
    website_state: lead.website_state || (lead.site || lead.website_normalized ? 'provided' : ''),
    service: lead.service || '',
    resolved_service: lead.resolved_service || lead.service || '',
    resolved_service_label: lead.resolved_service_label || lead.service_label || '',
    comment_normalized: lead.comment_normalized || lead.summary || '',
    summary: lead.summary || '',
    quality_status: lead.quality_status || '',
    lead_quality: lead.lead_quality || '',
    lead_quality_label: lead.lead_quality_label || '',
    missing_fields: lead.missing_fields || '',
    next_step: lead.next_step || lead.manager_recommendation || '',
    manager_recommendation: lead.manager_recommendation || '',
    first_reply_text: lead.first_reply_text || '',
    first_reply_source: lead.first_reply_source || '',
    manager_guidance_text: lead.manager_guidance_text || '',
    duplicate_status: lead.duplicate_status || 'new',
    manager_status: desired,
    status_when: when,
    status_actor_html: actorLabelHtml || '',
    card_renderer: 'iseo-canonical-lead-card-renderer-v1',
    authoritative_instance_contract: 'iseo-authoritative-card-instance-v1.1',
  };
}


const auth = $('Check User Authorization').first().json;
const allItems = $('Read CLEAN for Callback').all();
const rows = allItems.map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);
const myIndex = allItems.findIndex((i) => i === $input.first());
if (myIndex > 0) return [];

const nowIso = new Date().toISOString();
const actor = actorHash(auth.user_id);
const action = String(auth.action || auth.callback_action || '');
const token = String(auth.action_token || '').trim();

// Authoritative ACCESS_CONTROL display fields (not Telegram callback profile).
const actorDisplaySnapshot = buildSafeActorLabel(auth.access_display_name, auth.access_username);
const actorDisplaySnapshotHtml = esc(actorDisplaySnapshot);
const actorRoleSnapshot = String(auth.auth_role || auth.identity_role || '').toLowerCase();

const outBase = {
  ...auth,
  callback_outcome: 'error',
  sheets_mutate: false,
  telegram_edit: false,
  append_lead_event: false,
  answer_text: 'Не удалось сохранить статус. Попробуйте ещё раз.',
  event_type: '',
  prior_status: '',
  new_status: '',
  lead_id: '',
  edit_text: '',
  remove_keyboard: true,
  workflow_version: 'Admin.dev',
  manager_status_source: 'telegram_callback',
  last_manager_action_at: nowIso,
  actor_ref: actor,
  actor_role_snapshot: actorRoleSnapshot,
  actor_display_snapshot: actorDisplaySnapshot,
  event_id: 'evt_' + Date.now().toString(36),
  callback_query_id: String(auth.callback_query_id || ''),
  edit_chat_id: String(auth.callback_chat_id || auth.chat_id || ''),
  edit_message_id: String(auth.callback_message_id || ''),
  chat_id: String(auth.chat_id || auth.callback_chat_id || ''),
  early_ack_done: true,
};

if (!auth.authorized || !auth.manager_action_authorized) {
  const denyText = String(auth.deny_reply || auth.answer_text || '').trim() || 'Недостаточно прав.';
  return [{ json: {
    ...outBase,
    callback_outcome: 'unauthorized',
    answer_text: denyText,
    reply_text: denyText,
    event_type: 'manager_action_unauthorized',
    detail: JSON.stringify({ outcome: 'unauthorized', actor, source: 'telegram_callback', deny_reason: auth.deny_reason || '' }),
  } }];
}

if (!token || (action !== 'processed' && action !== 'spam' && action !== 'reopen' && action !== 'raw_source')) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'unknown',
    answer_text: 'Не удалось распознать действие.',
    event_type: 'manager_action_unauthorized',
    detail: JSON.stringify({ outcome: 'invalid_action', actor, source: 'telegram_callback' }),
  } }];
}

// Phase 3F.2 canonical lookup
if (!rows.length) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'storage_error',
    answer_text: 'Не удалось проверить заявку. Попробуйте ещё раз через минуту.',
    event_type: 'manager_action_storage_error',
    detail: JSON.stringify({ outcome: 'storage_error_lead_lookup', actor, source: 'telegram_callback' }),
  } }];
}

const leadMatches = rows.filter((r) => {
  const archiveState = String(r.archive_state || r.production_generation || '').toLowerCase();
  // archived markers checked after match
  const stored = String(r.telegram_action_token || r.callback_token || '').trim();
  if (stored && stored === token) return true;
  return computeActionToken(String(r.lead_id || '')) === token;
});

if (leadMatches.length > 1) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'ambiguous',
    answer_text: 'Не удалось проверить заявку. Попробуйте ещё раз через минуту.',
    event_type: 'manager_action_ambiguous',
    detail: JSON.stringify({ outcome: 'ambiguous_duplicate', actor, source: 'telegram_callback' }),
  } }];
}

const lead = leadMatches[0];

if (lead && (String(lead.archive_state || '').toLowerCase() === 'archived' || String(lead.legacy_data_mode || '') === 'archive_excluded' || String(lead.stats_included || '').toLowerCase() === 'false' && String(lead.production_generation || '') === 'legacy')) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'archived',
    answer_text: 'Эта карточка относится к архивному периоду и больше не изменяет рабочую статистику.',
    event_type: 'manager_action_archived',
    detail: JSON.stringify({ outcome: 'archived_card', actor, source: 'telegram_callback' }),
  } }];
}

if (!lead || !lead.lead_id) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'unknown_lead',
    answer_text: 'Заявка не найдена в рабочем реестре. Обратитесь к администратору.',
    event_type: 'manager_action_unauthorized',
    detail: JSON.stringify({ outcome: 'unknown_lead', actor, source: 'telegram_callback' }),
  } }];
}

let prior = String(lead.manager_status || 'pending').toLowerCase();
if (!prior || prior === 'new') prior = 'pending';
const desired = action === 'reopen' ? 'pending' : action;
const when = fmtMoscow(lead.manager_status_updated_at || lead.closed_at || nowIso);
const contract = 'iseo-lead-reopen-v1.0';
const ackContract = 'iseo-lead-callback-ack-v1.0';

// --- raw_source: literal original message body; no field reconstruction; no lifecycle mutation ---
if (action === 'raw_source') {
  if (typeof $itemIndex === 'number' && $itemIndex > 0) return [];
  let rawRows = [];
  let rawReadFailed = false;
  try {
    const rawItems = $('Read RAW for Callback').all();
    rawReadFailed = rawItems.some((i) => i.json && (i.json.error || i.json.errorMessage || i.json.errorDescription));
    rawRows = rawItems.map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error && !r.errorMessage && (r.lead_id || r.raw_text != null || r.source_body_full != null || r.gmail_message_id || r.request_text != null));
    // Prefer current item if Decide/Attach already enriched it
    try {
      const cur = $input.first().json;
      if (cur && (cur.source_body_full || cur.raw_text != null) && !cur.error) {
        rawRows = [cur].concat(rawRows.filter((r) => String(r.lead_id||'') !== String(cur.lead_id||'')));
      }
    } catch (e) {}
  } catch (e) {
    rawReadFailed = true;
    rawRows = [];
  }
  const leadId = String(lead.lead_id || '');
  const gmail = String(lead.source_message_id || '');
  let rawRow = rawRows.find((r) => String(r.lead_id || '') === leadId)
    || rawRows.find((r) => gmail && String(r.gmail_message_id || '') === gmail)
    || null;
  if (rawRow && String(rawRow.lead_id || '') === '__raw_resolve_none__') rawRow = null;
  const rendered = buildLiteralRawResponse(rawRow, rawReadFailed);
  return [{ json: {
    ...outBase,
    callback_outcome: 'raw_inspected',
    sheets_mutate: false,
    telegram_edit: false,
    skip_card_edits: true,
    append_lead_event: false,
    lead_id: leadId,
    source_message_id: gmail,
    prior_status: prior,
    new_status: prior,
    answer_text: rendered.answer_text,
    reply_text: rendered.html,
    reply_text_2: rendered.html_continued || '',
    raw_source_text: rendered.html,
    raw_state: rendered.state,
    telegram_has_buttons: false,
    remove_keyboard: false,
    event_type: rendered.event_type,
    detail: JSON.stringify({
      outcome: rendered.state,
      actor,
      source: 'telegram_callback',
      contract: 'iseo-literal-raw-source-v1.0',
      lifecycle_mutation: false,
      custom_field_labels_used: false,
      chunk_count: rendered.chunk_count,
      source_field: rendered.source_field,
      raw_match: rawRow ? (String(rawRow.lead_id || '') === leadId ? 'lead_id' : 'gmail_message_id') : null,
    }),
  } }];
}

// --- reopen: processed|spam -> pending ---
if (action === 'reopen') {
  if (prior === 'pending') {
    return [{ json: {
      ...outBase,
      callback_outcome: 'idempotent',
      lead_id: String(lead.lead_id),
      prior_status: prior,
      new_status: prior,
      event_type: 'manager_reopen_duplicate_ignored',
      telegram_edit: true,
      answer_text: 'Заявка уже находится в обработке.',
      edit_text: buildFinalCard(lead, 'pending', when, ''),
      telegram_reply_markup: buildActionButtons(token),
      telegram_callback_processed: 'sm:p:' + token,
      telegram_callback_spam: 'sm:s:' + token,
      telegram_callback_raw_source: 'sm:i:' + token,
      edit_keyboard_mode: 'pending_actions',
      remove_keyboard: false,
      detail: JSON.stringify({ prior, desired: 'pending', outcome: 'idempotent', actor, source: 'telegram_callback', contract }),
    } }];
  }
  if (prior !== 'processed' && prior !== 'spam') {
    return [{ json: {
      ...outBase,
      callback_outcome: 'conflict',
      lead_id: String(lead.lead_id),
      prior_status: prior,
      new_status: prior,
      event_type: 'manager_reopen_conflict',
      answer_text: 'Эту заявку нельзя вернуть в обработку из текущего статуса.',
      detail: JSON.stringify({ prior, outcome: 'conflict', actor, source: 'telegram_callback', contract }),
    } }];
  }
  const appliedWhen = fmtMoscow(nowIso);
  const editText = buildFinalCard(lead, 'pending', appliedWhen, actorDisplaySnapshotHtml);
  return [{ json: {
    ...outBase,
    callback_outcome: 'applied',
    sheets_mutate: true,
    telegram_edit: true,
    append_lead_event: true,
    lead_id: String(lead.lead_id),
    source_message_id: String(lead.source_message_id || ''),
    prior_status: prior,
    new_status: 'pending',
    manager_status: 'pending',
    manager_status_updated_at: nowIso,
    manager_status_updated_by: actor,
    manager_status_source: 'telegram_callback',
    last_manager_action: 'reopened',
    last_manager_action_at: nowIso,
    closed_at: '',
    close_reason: '',
    assigned_to: lead.assigned_to || '',
    spam_at: lead.spam_at || '',
    spam_by: lead.spam_by || '',
    spam_reason: lead.spam_reason || '',
    manager_action_processed_at: lead.manager_action_processed_at || '',
    manager_action_processed_by: lead.manager_action_processed_by || '',
    telegram_message_ref: String(auth.callback_message_id || lead.telegram_message_ref || ''),
    telegram_chat_ref_hash: actorHash(auth.callback_chat_id || auth.chat_id),
    telegram_action_token: token,
    telegram_reply_markup: buildActionButtons(token),
    telegram_callback_processed: 'sm:p:' + token,
    telegram_callback_spam: 'sm:s:' + token,
      telegram_callback_raw_source: 'sm:i:' + token,
    edit_keyboard_mode: 'pending_actions',
    remove_keyboard: false,
    event_type: 'manager_reopened',
    answer_text: 'Лид возвращён в обработку.',
    edit_text: editText,
    detail: JSON.stringify({
      prior,
      new_status: 'pending',
      outcome: 'applied',
      actor,
      actor_role: actorRoleSnapshot,
      actor_display: actorDisplaySnapshot,
      source: 'telegram_callback',
      reason: 'manual_reopen',
      contract,
      redistribution: false,
      workflow_version: 'Admin.dev',
    }),
  } }];
}

if (prior === desired) {
  return [{ json: {
    ...outBase,
    callback_outcome: 'idempotent',
    lead_id: String(lead.lead_id),
    prior_status: prior,
    new_status: prior,
    event_type: 'manager_action_duplicate_ignored',
    telegram_edit: true,
    telegram_reply_markup: buildReopenButtons(token),
  telegram_callback_reopen: 'sm:r:' + token,
  telegram_callback_raw_source: 'sm:i:' + token,
  edit_keyboard_mode: 'reopen',
  remove_keyboard: false,
    answer_text: desired === 'spam'
      ? 'Заявка уже отмечена как спам.'
      : 'Заявка уже отмечена как обработанная.',
    edit_text: buildFinalCard(lead, prior, when, actorDisplaySnapshotHtml),
    detail: JSON.stringify({ prior, desired, outcome: 'idempotent', actor, source: 'telegram_callback', workflow_version: 'Admin.dev' }),
  } }];
}

if (prior !== 'pending') {
  return [{ json: {
    ...outBase,
    callback_outcome: 'conflict',
    lead_id: String(lead.lead_id),
    prior_status: prior,
    new_status: prior,
    event_type: 'manager_action_duplicate_ignored',
    telegram_edit: true,
    telegram_reply_markup: buildReopenButtons(token),
  telegram_callback_reopen: 'sm:r:' + token,
  telegram_callback_raw_source: 'sm:i:' + token,
  edit_keyboard_mode: 'reopen',
  remove_keyboard: false,
    answer_text: 'Статус лида уже изменён другим сотрудником.',
    edit_text: buildFinalCard(lead, prior === 'spam' ? 'spam' : 'processed', when, actorDisplaySnapshotHtml),
    detail: JSON.stringify({ prior, desired, outcome: 'conflict', actor, source: 'telegram_callback', workflow_version: 'Admin.dev' }),
  } }];
}

const appliedWhen = fmtMoscow(nowIso);
const editText = buildFinalCard(lead, desired, appliedWhen, actorDisplaySnapshotHtml);
const detailObj = {
  prior,
  new_status: desired,
  outcome: 'applied',
  actor,
  actor_role: actorRoleSnapshot,
  actor_display: actorDisplaySnapshot,
  source: 'telegram_callback',
  workflow_version: 'Admin.dev',
};

return [{ json: {
  ...outBase,
  callback_outcome: 'applied',
  sheets_mutate: true,
  telegram_edit: true,
  append_lead_event: true,
  lead_id: String(lead.lead_id),
  source_message_id: String(lead.source_message_id || ''),
  prior_status: prior,
  new_status: desired,
  manager_status: desired,
  manager_status_updated_at: nowIso,
  manager_status_updated_by: actor,
  manager_status_source: 'telegram_callback',
  last_manager_action: desired === 'processed' ? 'marked_processed' : 'marked_spam',
  last_manager_action_at: nowIso,
  closed_at: nowIso,
  close_reason: desired === 'processed' ? 'processed' : 'spam',
  assigned_to: actor,
  spam_at: desired === 'spam' ? nowIso : (lead.spam_at || ''),
  spam_by: desired === 'spam' ? actor : (lead.spam_by || ''),
  spam_reason: desired === 'spam' ? 'manager_callback' : (lead.spam_reason || ''),
  manager_action_processed_at: desired === 'processed' ? nowIso : (lead.manager_action_processed_at || ''),
  manager_action_processed_by: desired === 'processed' ? actor : (lead.manager_action_processed_by || ''),
  telegram_message_ref: String(auth.callback_message_id || lead.telegram_message_ref || ''),
  telegram_chat_ref_hash: actorHash(auth.callback_chat_id || auth.chat_id),
  telegram_action_token: token,
  event_type: desired === 'processed' ? 'manager_marked_processed' : 'manager_marked_spam',
  answer_text: desired === 'processed'
    ? 'Лид отмечен как обработанный.'
    : 'Лид отмечен как спам.',
  telegram_reply_markup: buildReopenButtons(token),
  telegram_callback_reopen: 'sm:r:' + token,
  telegram_callback_raw_source: 'sm:i:' + token,
  edit_keyboard_mode: 'reopen',
  remove_keyboard: false,
  edit_text: editText,
  detail: JSON.stringify(detailObj),
} }];
