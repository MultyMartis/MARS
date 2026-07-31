/**
 * sm-parser-v3.1 — real website form field extraction.
 * Pure JS module for local harness; Operational.dev Code node embeds the same logic.
 * No require/crypto.
 */

export const PARSER_VERSION = 'sm-parser-v3.1';

const INVALID = new Set([
  '44', '#error!', 'unknown', 'telegram', 'whatsapp', 'viber',
  'телефон', 'email', 'e-mail', 'почта', 'сайт', 'n/a', 'na', '-', '—', '–',
  'null', 'undefined', 'phone', 'messenger', 'contact', 'контакт', 'нет', 'no',
  'имя', 'name', 'test',
]);

/** Ordered label definitions: value ends at the next known label or form-title boundary. */
const LABEL_DEFS = [
  { key: 'name', re: /(?:От\s*кого|Имя)\s*[:：]/gi },
  { key: 'contact_method', re: /Способ\s*связи\s*[:：]/gi },
  { key: 'contact', re: /Контакт\s*[:：]/gi },
  { key: 'phone_direct', re: /Телефон\s*[:：]/gi },
  { key: 'email_direct', re: /(?:E[\u2011\u2010\-]?mail|Email|Почта)\s*[:：]/gi },
  { key: 'site', re: /(?:Адрес\s*сайта|Сайт)\s*[:：]/gi },
  { key: 'comment', re: /(?:Комментарий|Сообщение)\s*[:：]/gi },
  { key: 'page', re: /Отправлено\s+со\s+страницы\s*[:：]/gi },
];

/** Non-capturing boundaries that end a previous field value. */
const BOUNDARY_DEFS = [
  { key: '__audit_title', re: /Заявка\s+на\s+бесплатный\s+аудит/gi },
  { key: '__forward', re: /^-{2,}\s*Forwarded\s*-{2,}/gim },
];

export function normalizeSpaces(raw) {
  return String(raw ?? '')
    .replace(/\u00a0/g, ' ')
    .replace(/[\u2007\u202F\u2009\u200A]/g, ' ')
    .replace(/\r\n/g, '\n')
    .replace(/\r/g, '\n');
}

function isInvalidToken(v) {
  const s = String(v || '').trim().toLowerCase();
  return !s || INVALID.has(s);
}

export function extractLabeledFields(raw) {
  const text = normalizeSpaces(raw);
  const hits = [];
  for (const def of LABEL_DEFS) {
    const re = new RegExp(def.re.source, def.re.flags);
    let m;
    while ((m = re.exec(text)) !== null) {
      hits.push({ key: def.key, start: m.index, end: m.index + m[0].length, boundary: false });
      if (!re.global) break;
    }
  }
  for (const def of BOUNDARY_DEFS) {
    const re = new RegExp(def.re.source, def.re.flags);
    let m;
    while ((m = re.exec(text)) !== null) {
      hits.push({ key: def.key, start: m.index, end: m.index + m[0].length, boundary: true });
    }
  }
  hits.sort((a, b) => a.start - b.start || a.end - b.end);

  const fields = {};
  for (let i = 0; i < hits.length; i++) {
    const h = hits[i];
    if (h.boundary) continue;
    if (fields[h.key] != null) continue; // first wins
    const valueEnd = i + 1 < hits.length ? hits[i + 1].start : text.length;
    let val = text.slice(h.end, valueEnd).trim();
    val = val.replace(/^[\s:：\-–—|]+/, '').replace(/\s+/g, ' ').trim();
    // Do not allow value to still contain a known label header
    for (const def of LABEL_DEFS) {
      const probe = new RegExp(def.re.source, 'i');
      if (probe.test(val)) {
        const cut = val.search(probe);
        if (cut > 0) val = val.slice(0, cut).trim();
      }
    }
    val = val.replace(/\s*Заявка\s+на\s+бесплатный\s+аудит\s*/gi, ' ').replace(/\s+/g, ' ').trim();
    fields[h.key] = val;
  }
  return { fields, text };
}

export function digits(p) {
  return String(p || '').replace(/\D/g, '');
}

export function looksLikePhone(p) {
  if (isInvalidToken(p)) return false;
  const d = digits(p);
  if (!d || d.length < 10 || d.length > 15) return false;
  if (INVALID.has(d)) return false;
  return true;
}

export function looksLikeEmail(e) {
  const v = String(e || '').trim().toLowerCase();
  if (!v || isInvalidToken(v) || v.length > 254) return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]{2,24}$/.test(v);
}

export function looksLikeMessenger(m) {
  const v = String(m || '').trim();
  if (!v || isInvalidToken(v)) return false;
  if (/^@[a-zA-Z0-9_]{4,32}$/.test(v)) return true;
  if (/^(t\.me\/|https?:\/\/t\.me\/)[a-zA-Z0-9_]{4,}/i.test(v)) return true;
  // bare username only when method is telegram
  return false;
}

export function normalizePhoneDisplay(raw) {
  const src = String(raw || '').trim();
  if (!looksLikePhone(src)) return '';
  return src.replace(/\s+/g, ' ').trim();
}

export function normalizeSite(raw) {
  let s = String(raw || '').trim();
  if (!s || isInvalidToken(s)) return '';
  s = s.replace(/^[\s"'«»(<[{]+/, '').replace(/[\s"'«».,;:!?)\]}>]+$/g, '').trim();
  if (!s || isInvalidToken(s)) return '';
  // Accept with or without scheme; keep path; do not DNS-check.
  if (/^https?:\/\//i.test(s)) return s.replace(/\s+/g, '');
  if (/^www\./i.test(s)) return s.replace(/\s+/g, '');
  // host.tld or host.tld/path — including .example operator tests
  if (/^[a-z0-9][\w.-]*\.[a-z0-9][\w.-]*(?:\/\S*)?$/i.test(s)) return s.replace(/\s+/g, '');
  return '';
}

export function interpretContactMethod(methodRaw, contactRaw, extras = {}) {
  const method = String(methodRaw || '').trim().toLowerCase();
  const contact = String(contactRaw || '').trim();
  let phone = String(extras.phone_direct || '').trim();
  let email = String(extras.email_direct || '').trim();
  let messenger = '';

  const methodPhone = /телефон|phone|звон/i.test(method);
  const methodEmail = /e[\u2011\u2010\-]?mail|email|почта|mail/i.test(method);
  const methodTg = /telegram|телеграм/i.test(method);
  const methodWa = /whats\s*app|ватсап|вацап/i.test(method);

  if (methodPhone) {
    if (looksLikePhone(contact)) phone = phone || contact;
  } else if (methodEmail) {
    if (looksLikeEmail(contact)) email = email || contact;
    else if (looksLikeEmail(contact.replace(/\s+/g, ''))) email = email || contact.replace(/\s+/g, '');
  } else if (methodTg) {
    if (looksLikeMessenger(contact) || /^@[a-zA-Z0-9_]{4,32}$/.test(contact) || /^[a-zA-Z0-9_]{5,32}$/.test(contact)) {
      messenger = contact.startsWith('@') || /t\.me/i.test(contact) ? contact : '@' + contact.replace(/^@/, '');
      if (!looksLikeMessenger(messenger) && !/^@[a-zA-Z0-9_]{5,32}$/.test(messenger)) messenger = contact;
    } else if (looksLikePhone(contact)) {
      phone = phone || contact;
    }
  } else if (methodWa) {
    if (looksLikePhone(contact)) phone = phone || contact;
    else if (contact) messenger = contact;
  } else if (contact) {
    // unknown method — infer
    if (looksLikePhone(contact)) phone = phone || contact;
    else if (looksLikeEmail(contact)) email = email || contact;
    else if (looksLikeMessenger(contact) || /^@[a-zA-Z0-9_]{4,32}$/.test(contact)) messenger = contact;
  }

  if (phone && !looksLikePhone(phone)) phone = '';
  if (email && !looksLikeEmail(email)) email = '';
  if (messenger && isInvalidToken(messenger)) messenger = '';

  let contact_method = 'unknown';
  if (methodPhone || (phone && !email && !messenger)) contact_method = 'phone';
  else if (methodEmail || (email && !phone && !messenger)) contact_method = 'email';
  else if (methodTg) contact_method = 'telegram';
  else if (methodWa) contact_method = 'whatsapp';
  else if (messenger) contact_method = 'messenger';

  return {
    contact_method,
    phone: normalizePhoneDisplay(phone),
    email: email ? email.toLowerCase() : '',
    messenger: String(messenger || '').trim(),
  };
}

export function detectAuditForm(raw) {
  return /Заявка\s+на\s+бесплатный\s+аудит/i.test(String(raw || ''));
}

export function stripLabeledPayload(raw) {
  const text = normalizeSpaces(raw);
  const { fields } = extractLabeledFields(text);
  // Build a free-text residual: remove known "label: value" spans
  let residual = text;
  const labelUnion = LABEL_DEFS.map((d) => d.re.source).join('|');
  residual = residual.replace(new RegExp('(?:' + labelUnion + ')\\s*[^]*?(?=(?:' + labelUnion + ')|$)', 'gi'), ' ');
  residual = residual.replace(/\s+/g, ' ').trim();
  return { fields, residual };
}

/**
 * Parse a Gmail-like or synthetic lead item into Parse Lead output fields.
 * @param {object} j input json
 */
export function parseLeadItem(j = {}) {
  const now = new Date().toISOString();
  const isSynth = Boolean(j.synthetic_fixture || j.fixture_id || j.__synthetic);

  const subject = String(j.email_subject || j.subject || '').trim();
  const sender = String(j.sender_email || j.from || '').trim();
  const thread = String(j.gmail_thread_id || j.threadId || '').trim();
  const received = String(j.received_at || '').trim();

  let gmail_message_id = String(j.gmail_message_id || j.id || j.messageId || '').trim();
  if (!gmail_message_id) {
    if (isSynth) gmail_message_id = 'msg_synth_' + String(j.fixture_id || 'X');
    else {
      // stable hash without crypto (fnv+djb2) — mirrored in Code node
      const raw = [thread, received, sender, subject, String(j.request_text || j.snippet || '').slice(0, 120)]
        .map((p) => String(p ?? '').trim().toLowerCase()).join('|');
      let h1 = 0x811c9dc5;
      for (let i = 0; i < raw.length; i++) { h1 ^= raw.charCodeAt(i); h1 = Math.imul(h1, 0x01000193); }
      let h2 = 5381;
      for (let i = 0; i < raw.length; i++) h2 = ((h2 << 5) + h2) ^ raw.charCodeAt(i);
      gmail_message_id = 'msg_' + ((h1 >>> 0).toString(16).padStart(8, '0')) + ((h2 >>> 0).toString(16).padStart(8, '0'));
    }
  }
  const lead_id = String(j.lead_id || ('lead_' + gmail_message_id));

  const rawBody = String(j.request_text || j.text || j.textPlain || j.snippet || j.body || j.raw_text || '');
  const normalizedBody = normalizeSpaces(rawBody);
  const { fields } = extractLabeledFields(normalizedBody);

  // Prefer explicit pre-parsed synthetic fields when provided
  const extractedName = (!isInvalidToken(fields.name) ? String(fields.name || '').trim() : '');
  const site = normalizeSite(fields.site || '');
  const page = String(fields.page || '').trim();
  const comment = String(fields.comment || '').trim();

  const interpreted = interpretContactMethod(fields.contact_method, fields.contact, {
    phone_direct: fields.phone_direct,
    email_direct: fields.email_direct,
  });

  const parsed_name = String(j.parsed_name || j.client_name || j.name || extractedName || '').trim();
  const parsed_phone = String(j.parsed_phone || j.phone || interpreted.phone || '').trim();
  const parsed_email = String(j.parsed_email || j.email || interpreted.email || '').trim();
  const parsed_messenger = String(j.parsed_messenger || j.messenger || interpreted.messenger || '').trim();
  const parsed_site = String(j.parsed_site || j.site || site || '').trim();

  const isAudit = detectAuditForm(normalizedBody) || /\/audit/i.test(page) || /аудит/i.test(subject);
  const form_name = String(j.form_name || (isAudit ? 'Заявка на бесплатный аудит' : '')).trim();

  // Clean request text: prefer comment; else residual without labels; keep enough signal for service detection
  let request_text = comment;
  if (!request_text) {
    const { residual } = stripLabeledPayload(normalizedBody);
    request_text = residual || normalizedBody;
  }
  if (isAudit && request_text && !/аудит/i.test(request_text)) {
    request_text = ('Заявка на бесплатный аудит. ' + request_text).trim();
  } else if (isAudit && !request_text) {
    request_text = 'Заявка на бесплатный аудит';
  }
  request_text = request_text.slice(0, 4000);

  const hasContact = Boolean(parsed_phone || parsed_email || parsed_messenger);
  const parse_status = hasContact || request_text
    ? (parsed_name || parsed_site || request_text.length > 10 ? 'ok' : 'partial')
    : 'failed';

  const warnings = [];
  if (fields.contact && !hasContact) warnings.push('contact_unrecognized');
  if (fields.site && !parsed_site) warnings.push('site_rejected');

  return {
    ...j,
    lead_id,
    gmail_message_id,
    gmail_thread_id: thread,
    received_at: j.received_at || now,
    source: j.source || (isSynth ? 'synthetic' : 'gmail'),
    email_subject: subject,
    sender_email: sender,
    request_page: j.request_page || page || '',
    form_name,
    utm_source: j.utm_source || '',
    utm_medium: j.utm_medium || '',
    utm_campaign: j.utm_campaign || '',
    utm_term: j.utm_term || '',
    utm_content: j.utm_content || '',
    parsed_name,
    parsed_phone,
    parsed_email,
    parsed_messenger,
    parsed_site,
    contact_method: interpreted.contact_method,
    request_text,
    calc_detected: String(j.calc_detected || 'false'),
    calc_data: j.calc_data || '',
    ip: j.ip || '',
    parser_version: PARSER_VERSION,
    parse_status,
    parse_warnings: warnings.join(',') || j.parse_warnings || '',
    workflow_version: 'operational.dev.phase3d1',
    raw_logged_at: now,
    raw_text: String(j.raw_text || normalizedBody).slice(0, 8000),
    __synthetic: isSynth,
    fixture_id: j.fixture_id || null,
    marker: j.marker || (isSynth ? 'SYNTHETIC_TEST' : ''),
    phase_marker: j.phase_marker || (isSynth ? 'PHASE_3D1' : ''),
  };
}
